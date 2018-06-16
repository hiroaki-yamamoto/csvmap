#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Application script."""


import click
import yaml
from csv import DictReader

from .lib import Mapper


@click.command()
@click.option(
    "-o", "--out", type=click.Path(writable=True), default="--",
    help="Output path"
)
@click.argument("map_cfg", type=click.File("r"))
@click.argument("file_in_path", type=click.Path(exists=True))
def main(file_in_path, map_cfg, out):
    """Entrypoint."""
    config = yaml.load(map_cfg)
    sep_in = config.get("sep_in") or ","
    enc_in = config.get('enc_in') or "utf-8"
    mapper = Mapper(config)

    with open(file_in_path, "r", encoding=enc_in) as file_in:
        csvreader = DictReader(file_in, delimiter=sep_in)
        mapper.generate(csvreader, out)
    print("Done")


if __name__ == '__main__':
    main()
