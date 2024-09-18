#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyfreebody',
    version='0.4.0',
    author="Daniel Rosel",
    url="https://github.com/velocitatem/pyfreebody",
    packages=find_packages(include=['pyfreebody']),
        install_requires=[
            'Pillow==10.4.0',
        ]

)
