#!/usr/bin/env -S just --justfile
# -*- coding: UTF-8 -*-
#
# copyright: 2023, Electric Mass Records
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

set windows-powershell := true

PROJECT_DIR := absolute_path(justfile_directory())
PACKAGE_NAME := file_name(PROJECT_DIR)
DOCS_DIR := 'docs'
SOURCE_DIR := 'src'
VENV_DIR := '.venv'
VENV_BIN_DIR := join(VENV_DIR, if os() == 'windows' { 'Scripts' } else { 'bin' })
_EXT_ := if os() == 'windows' { '.exe' } else { '' }
_LIST_SEP_ := if os() == 'windows' { ', ' } else { ' ' }

BUILD_ARTIFACTS := 'build*' + _LIST_SEP_ + 'dist*'
CACHE_ITEMS := '.mypy_cache*' + _LIST_SEP_ + '.pytest_cache*' + _LIST_SEP_ + '.coverage*' + _LIST_SEP_ + '.ruff_cache*'

AUTOPEP := 'autopep8' + _EXT_
LINT := 'ruff' + _EXT_
PDOC := 'pdoc3' + _EXT_
PYLINT := 'pylint' + _EXT_
PYTEST := 'pytest' + _EXT_
PYTHON := 'python' + if os() == 'windows' { _EXT_ } else { '3' }
STUBGEN := 'stubgen' + _EXT_
TWINE := 'twine' + _EXT_
VERMIN := 'vermin' + _EXT_

FIND := if os() == 'windows' { 'gci' } else { 'find' }
MV := 'mv'
RM := if os() == 'windows' { 'ri -Recurse -Force' } else { 'rm -rf' }

AUTOPEP_ARGS := '--aggressive --aggressive --recursive'
LINT_ARGS := 'check --exit-zero'
PDOC_ARGS := '--force --html --skip-errors'
PIP_ARGS := '--quiet --upgrade --editable'
PYLINT_ARGS := '--exit-zero'
PYTEST_ARGS := '--quiet --no-header --color=auto --code-highlight=yes'
PYTEST_DOC_ARGS := '--doctest-modules --doctest-continue-on-failure --suppress-no-test-exit-code'
STUBGEN_ARGS := '--quiet --export-less'
VERMIN_ARGS := '--no-tips --eval-annotations --no-parse-comments'

[private]
default: help

# Creates the library package(s).
build: build-clean
    # Building package(s)...
    @{{join(VENV_BIN_DIR, PYTHON)}} -m build

# Cleans the build artifacts.
[private]
build-clean:
    # Cleaning build artifacts...
    @{{RM}} {{BUILD_ARTIFACTS}}

# Cleans the project caches.
[private, unix]
cache-clean:
    # Cleaning caches...
    @{{RM}} {{CACHE_ITEMS}}
    @{{FIND}} '.' -mindepth 1 -type f -name "*.py[co]" -delete \
        -o -type d -name "__pycache__" -delete

# Cleans the project caches.
[private, windows]
cache-clean:
    # Cleaning caches...
    @{{RM}} {{CACHE_ITEMS}}
    @{{FIND}} '.' -Directory -Recurse -Name '__pycache__' | {{RM}}
    @{{FIND}} '.' -File -Recurse -Include '*.pyc', '*.pyo' | {{RM}}

# Cleans the project caches and builds.
clean: build-clean cache-clean

# Cleans everything.
clean-all: clean init-clean

# Creates the project documentation.
docs: docs-clean
    # Checking documentation examples...
    @{{join(VENV_BIN_DIR, PYTEST)}} {{PYTEST_ARGS}} {{PYTEST_DOC_ARGS}} \
        '{{join(SOURCE_DIR, PACKAGE_NAME)}}'
    # Generating documentation...
    @{{join(VENV_BIN_DIR, PDOC)}} {{PDOC_ARGS}} \
        --template-dir '{{join(SOURCE_DIR, "docs", "templates")}}' \
        --output-dir '{{DOCS_DIR}}' '{{join(SOURCE_DIR, PACKAGE_NAME)}}'
    @{{MV}} {{join(DOCS_DIR, PACKAGE_NAME, '*')}} '{{DOCS_DIR}}'
    @{{RM}} '{{join(DOCS_DIR, PACKAGE_NAME)}}'

# Cleans the documentation folder.
[private]
[unix]
docs-clean:
    # Cleaning documentation...
    @{{FIND}} '{{DOCS_DIR}}' -mindepth 1 \
        -type f -not \( -name '.nojekyll' -o -name '.gitkeep' \) -delete -o \
        -type d -delete

# Cleans the documentation folder.
[private]
[windows]
docs-clean:
    # Cleaning documentation...
    @{{FIND}} '{{DOCS_DIR}}' -Recurse -Force \
        -Exclude '.gitkeep', '.nojekyll' | {{RM}}

# Formats the code.
format:
    # Formating code...
    @{{join(VENV_BIN_DIR, AUTOPEP)}} {{AUTOPEP_ARGS}} --in-place \
        '{{join(SOURCE_DIR, PACKAGE_NAME)}}'

# Shows the required code formats.
format-show:
    # Getting required code formats...
    @{{join(VENV_BIN_DIR, AUTOPEP)}} {{AUTOPEP_ARGS}} \
        --diff '{{join(SOURCE_DIR, PACKAGE_NAME)}}'

# Shows this help message.
help:
    @just --list

# (Re)Creates the development environment.
init: init-clean && init-show
    # Creating the venv...
    @{{PYTHON}} -m venv --upgrade-deps '{{VENV_DIR}}'
    # Instaling project requirements...
    @{{join(VENV_BIN_DIR, PYTHON)}} -m pip install {{PIP_ARGS}} .[dev]

# Cleans the venv.
[private]
init-clean _active=env_var_or_default('VIRTUAL_ENV', ''):
    # Deleting the venv...
    @{{RM}} {{VENV_DIR}}*
    {{ if _active != "" { '# !! Python venv active. Deactivate it using the command "deactivate".' } else { '' } }}

# Shows venv info
init-show:
    # Getting venv information...
    @echo 'VIRTUAL_ENV="{{join(PROJECT_DIR, VENV_DIR)}}"'
    @{{join(VENV_BIN_DIR, PYTHON)}} \
        -c "import sys; print(f'Python ' + sys.version.replace('\n',''))"
    @{{join(VENV_BIN_DIR, PYTHON)}} -m pip --version

# Checks the project for code smells.
lint:
    # Checking the code...
    @{{join(VENV_BIN_DIR, LINT)}} {{LINT_ARGS}} \
        '{{join(SOURCE_DIR, PACKAGE_NAME)}}'

# Uploads the project to 'pypi.org'.
publish: build
    # Publishing to 'pypi.org'...
    @{{join(VENV_BIN_DIR, TWINE)}} upload {{join('dist', '*')}}

# Uploads the project to 'test.pypi.org'.
publish-test: build
    # Publishing to 'test.pypi.org'...
    @{{join(VENV_BIN_DIR, TWINE)}} upload --repository testpypi \
        {{join('dist', '*')}}

# Checks the project for code smells.
pylint:
    # Checking the code...
    @{{join(VENV_BIN_DIR, PYLINT)}} {{PYLINT_ARGS}} \
        '{{join(SOURCE_DIR, PACKAGE_NAME)}}'

# Calculates python minimum version required.
pyversion:
    #Finding minimum Python version...
    @{{join(VENV_BIN_DIR, VERMIN)}} {{VERMIN_ARGS}} \
        '{{join(SOURCE_DIR, PACKAGE_NAME)}}'

# Generates stubs for the project.
stubs: stubs-clean
    # Generating stubs...
    @{{join(VENV_BIN_DIR, STUBGEN)}} {{STUBGEN_ARGS}} \
        --package {{PACKAGE_NAME}} --search-path '{{SOURCE_DIR}}' \
        --output '{{SOURCE_DIR}}'

# Deletes the stubs.
[private]
[unix]
stubs-clean:
    # Deleting stubs...
    @{{FIND}} '{{join(SOURCE_DIR, PACKAGE_NAME)}}' -mindepth 1 -type f \
        -name "*.pyi" -delete

# Deletes the stubs.
[private]
[windows]
stubs-clean:
    # Deleting stubs...
    @{{FIND}} '{{join(SOURCE_DIR, PACKAGE_NAME)}}' -Recurse -File \
        -Filter "*.pyi" | {{RM}}

# Runs the tests.
tests:
    # Running tests...
    @{{join(VENV_BIN_DIR, PYTEST)}} {{PYTEST_ARGS}} --cov={{PACKAGE_NAME}}
