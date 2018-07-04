#!/usr/bin/env python
# coding=utf-8
"""Setup script."""

import sys
from os import path
from setuptools import setup, find_packages

dependencies = ["click", "PyYAML", "dateutils"]
name = "csvmap"
desc = "Simple CSV Mapper"
license = "MIT License"
url = "https://github.com/hiroaki-yamamoto/csvmap"
keywords = "csvmap"
version = "0.0.0"

category = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3"
]

version_file = \
    path.join(path.abspath(path.dirname(__file__)), "VERSION")

if path.exists(version_file):
    with open(version_file) as v:
        version = v.read()

author = "Hiroaki Yamamoto"
author_email = "hiroaki@hysoftware.net"

if sys.version_info < (3, 6):
    raise RuntimeError("Not supported on earlier then python 3.6.")

try:
    with open('README.md') as readme:
        long_desc = readme.read()
except Exception:
    long_desc = None

setup(
    name=name,
    version=version,
    description=desc,
    long_description=long_desc,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=dependencies,
    zip_safe=False,
    author=author,
    author_email=author_email,
    license=license,
    keywords=keywords,
    url=url,
    entry_points={
        'console_scripts': [
            "correct=csvmap.app:main",
        ]
    },
    classifiers=category
)
