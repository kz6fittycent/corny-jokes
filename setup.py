#!/usr/bin/env python3

from setuptools import setup

setup(
    name="cornyjokes",
    version="2.0.0",
    description="A collection of corny, clean jokes for the terminal",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libcornyjokes"],
    scripts=["cornyjokes"],
    package_data={"libcornyjokes": ["data/*"]},
)
