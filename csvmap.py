#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""CSV Mapper."""

import click
import sys
import yaml
from csv import DictReader, DictWriter


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
            for (src, dst) in self.mapper["map"].items():
                value = item.get(src)
                if value is not None:
                    out_el[dst] = value
            ret.append(out_el)
        return ret

    def generate(self, dctlst, out):
        """Generate the csv."""
        mapped = self.map(dctlst)
        writer = DictWriter(out, self.mapper["fieldnames"])
        writer.writeheader()
        writer.writerows(mapped)


@click.command()
@click.option(
    "-o", "--out", type=click.File("w"), default=sys.stdout,
    help="Output path"
)
@click.argument("map_cfg", type=click.File("r"))
@click.argument("file_in", type=click.File("r"))
def main(file_in, map_cfg, out):
    """Entrypoint."""
    mapper = Mapper(yaml.load(map_cfg))
    csvreader = DictReader(file_in)
    mapper.generate(csvreader, out)
    print("Done")


if __name__ == '__main__':
    main()
