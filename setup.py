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


DESCRIPTION = 'Currency representation library.'
KEYWORDS = ['currency', 'library', 'monetary']

with open('requirements.txt', 'r', encoding='utf-8') as r:
    DEPENDENCIES = [p.strip() for p in r if not p.strip().startswith('#')]

if __name__ == '__main__':
    setup(
        author=__author__,
        classifiers=[
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
            'Topic :: Software Development :: Libraries',
            'Typing :: Typed'],
        description=DESCRIPTION,
        entry_points={},
        install_requires=DEPENDENCIES,
        keywords=KEYWORDS,
        license=__license__,
        license_files=['LICENSE'],
        long_description=open('README.md', 'r', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        name=__project__,
        package_data={__project__: ['py.typed', '*.pyi']},
        packages=find_packages(exclude=['tests']),
        project_urls={
            'Documentation': 'http://fscm.github.io/multicurrency',
            'Source': 'https://github.com/fscm/multicurrency'},
        python_requires='>=3.6, <4',
        url='https://github.com/fscm/multicurrency',
        version=__version__)
