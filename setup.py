#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Setup."""

from setuptools import setup
from multicurrency import (
    __author__, __license__, __project__, __version__)

with open('requirements.txt', 'r', encoding='utf-8') as r:
    dependencies = [p.strip() for p in r if not p.strip().startswith('#')]

if __name__ == '__main__':
    setup(
        author=__author__,
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.9',
            'Topic :: Software Development :: Libraries',
            'Typing :: Typed'],
        description=('Currency representation library.'),
        entry_points={},
        install_requires=dependencies,
        license=__license__,
        long_description=open('README.md', 'r', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        name=__project__,
        packages=[__project__],
        package_data={'': ['LICENSE'], __project__: ['py.typed', '*.pyi']},
        python_requires='~=3.9',
        url='https://github.com/fscm/multicurrency',
        version=__version__)
