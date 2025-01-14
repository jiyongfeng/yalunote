#!/usr/bin/env python
# coding=utf-8

'''
Author       : JIYONGFENG jiyongfeng@163.com
Date         : 2025-01-08 14:20:09
LastEditors  : JIYONGFENG jiyongfeng@163.com
LastEditTime : 2025-01-08 14:23:08
Description  :
Copyright (c) 2025 by ZEZEDATA Technology CO, LTD, All Rights Reserved.
'''

# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='yalunote',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Kenneth Reitz',
    author_email='me@kennethreitz.com',
    url='https://github.com/kennethreitz/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

