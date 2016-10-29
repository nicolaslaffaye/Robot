#!/usr/bin/env python3
import sys

from setuptools import setup, find_packages


setup(
    name='robot',
    version='0.0.2',
    description='Simple Python test for look-a-head',
    author='Nicolas Laffaye',
    author_email='nicolas.laffaye@gmail.com',
    url='https://github.com/nicolaslaffaye/Robot',
    packages=find_packages(exclude=('tests')),
    scripts=['bin/robot']
)

