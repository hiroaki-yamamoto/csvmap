#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CSV Mapper."""

import sys

import dateutil.parser as dateparser

from csv import DictWriter


class Mapper(object):
    """CSV Mapper."""

    def __init__(self, mapper):
        """Init."""
        self.mapper = mapper

    def map(self, dctlst):
        """Map the field."""
        ret = []
        for item in dctlst:
            out_el = {}
            for (key, value) in self.mapper.get("default_value", {}).items():
                out_el.setdefault(key, value)
            for (src, dst_item) in self.mapper["map"].items():
                value = item.get(src)
                dst = dst_item
                suffix = ""
                prefix = ""
                format = ""
                if isinstance(dst_item, dict):
                    dst = dst_item["dest"]
                    suffix = dst_item.get("suffix", "")
                    prefix = dst_item.get("prefix", "")
                    format = dst_item.get("format", "")
                if value:
                    out_el[dst] = ("{}{}{}").format(
                        suffix,
                        prefix,
                        value
                    )
                    if format and format[0:5] == "date:":
                        out_el[dst] = dateparser.parse(out_el[dst]).date()
                        if format[5:] == "iso":
                            out_el[dst] = out_el[dst].isoformat()
                        else:
                            out_el[dst] = out_el[dst].strftime(format[5:])
            ret.append(out_el)
        return ret

    def generate(self, dctlst, out_path):
        """Generate the csv."""
        sep_out = self.mapper.get("sep_out") or ","
        enc_out = self.mapper.get("enc_out") or "utf-8"
        out = sys.stdout if out_path == "--" \
            else open(out_path, "w", encoding=enc_out)
        mapped = self.map(dctlst)
        writer = DictWriter(out, self.mapper["fieldnames"], delimiter=sep_out)
        writer.writeheader()
        writer.writerows(mapped)
        if out is not sys.stdout:
            out.close()
