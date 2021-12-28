#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Setup."""

from setuptools import find_packages, setup
from multicurrency import (
    __author__, __license__, __project__, __version__)


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3 :: Only',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Topic :: Software Development :: Libraries',
    'Typing :: Typed']
DESCRIPTION = 'Currency representation library.'
KEYWORDS = ['currency', 'library', 'monetary']
PROJECT_URLS = {
    'Documentation': f'http://fscm.github.io/{__project__}',
    'Source': f'https://github.com/fscm/{__project__}'}
PYTHON_REQUIRES = '>=3.6, <4'
URL = f'https://github.com/fscm/{__project__}'


with open('requirements.txt', 'r', encoding='utf-8') as r:
    DEPENDENCIES = [p.strip() for p in r if not p.strip().startswith('#')]

with open('README.md', 'r', encoding='utf-8') as d:
    LONG_DESCRIPTION = d.read()


if __name__ == '__main__':
    setup(
        author=__author__,
        classifiers=CLASSIFIERS,
        description=DESCRIPTION,
        entry_points={},
        install_requires=DEPENDENCIES,
        keywords=KEYWORDS,
        license=__license__,
        license_files=['LICENSE'],
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        name=__project__,
        package_data={__project__: ['py.typed', '*.pyi']},
        packages=find_packages(exclude=['tests']),
        project_urls=PROJECT_URLS,
        python_requires=PYTHON_REQUIRES,
        url=URL,
        version=__version__)
