#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyfreebody',
    version='0.3.2',
    author="Daniel Rosel",
    url="https://github.com/velocitatem/pyfreebody",
    packages=find_packages(include=['pyfreebody']),
        install_requires=[
            'Pillow==9.5.0',
        ]

)
