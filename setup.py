# -*- coding: utf-8 -*-

import sys

import setuptools

if sys.version_info < (3, 9, 0):
    sys.exit("The ha_vector module requires Python 3.10.0 or later")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ha_vector",
    description="Home Assistant Vector SDK implementation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Malene Trab",
    author_email="malene@trab.dk",
    license="MIT",
    url="https://github.com/mtrab/ha_vector",
    packages=setuptools.find_packages(),
    project_urls={
        "Bug Tracker": "https://github.com/mtrab/ha_vector/issues",
    },
    install_requires=[
        "aiogrpc==1.8",
        "cryptography==36.0.2",
        "flask==2.1.2",
        "googleapis-common-protos==1.56.3",
        "numpy==1.23.0",
        "Pillow==9.2.0",
        "requests==2.28.0",
        "grpcio-tools==1.47.0",
    ],
)
