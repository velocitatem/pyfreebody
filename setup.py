#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='pyfreebody',
    version='0.4.2',
    author="Daniel Rosel",
    author_email='daniel@alves.world',
    description='A package for generating freebody diagrams.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/velocitatem/pyfreebody",
    packages=find_packages(),
        install_requires=[
            'Pillow==10.4.0',
        ]

)
