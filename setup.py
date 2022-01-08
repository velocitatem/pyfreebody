#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyfreebody',
    version='0.2.0',
    author="Daniel Rosel",
    url="https://github.com/danalves24com/pyfreebody",
    packages=find_packages(include=['pyfreebody']),
        install_requires=[
            "Pillow"
        ]

)
