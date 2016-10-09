# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='robot',
    version='0.0.1',
    description='Simple Python test for look-a-head',
    long_description=readme,
    author='Nicolas Laffaye',
    author_email='nicolas.laffaye@gmail.com',
    url='https://github.com/nicolaslaffaye/Robot',
    license=license,
    packages=find_packages(exclude=('tests'))
)

