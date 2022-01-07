#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyfreebody',
    version='0.1.0',
    author="Daniel Rosel",
    url="https://github.com/danalves24com/pyfreebody",
    long_description = "README.md",
    packages=find_packages(include=['pyfreebody']),
        install_requires=[
            "Pillow"
        ]

)
