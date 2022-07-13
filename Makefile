# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

# Project Macros/Variables
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PROJECT_DIR := $(realpath $(dir $(MAKEFILE_PATH)))
PACKAGE_NAME := $(notdir $(PROJECT_DIR))
PYPROJECT_TOML := $(PROJECT_DIR)/pyproject.toml
SOURCE_DIR := $(PROJECT_DIR)/src
VENV_DIR := $(PROJECT_DIR)/.venv

BUILD_ARTIFACTS := build dist src/*.egg-info src/"$(PACKAGE_NAME)"/*.so
CACHE_ITEMS := .mypy_cache .pytest_cache .coverage*

# Shell
SHELL := /bin/sh
.SHELLFLAGS += -e

# Tools
AUTOPEP := autopep8
PDOC := pdoc3
PIP := pip3
PYLINT := pylint
PYTEST := pytest
PYTHON := python3
STUBGEN := stubgen
TWINE := twine
VERMIN := vermin

FIND := find
MV := mv
RM := rm -rf

# Tools options
AUTOPEP_ARGS += --aggressive --aggressive --in-place --recursive
PDOC_ARGS += --force --html --skip-errors
PIP_ARGS += --quiet --upgrade --editable
PYLINT_ARGS += --exit-zero
PYTEST_ARGS += --quiet --no-header --color=auto --code-highlight=yes
PYTEST_DOC_ARGS += --doctest-modules --doctest-continue-on-failure
STUBGEN_ARGS += --quiet --export-less
VERMIN_ARGS += --quiet --eval-annotations --no-parse-comments

# Rules
.NOTPARALLEL:

.ONESHELL:

.PHONY: build default dev docs help clean clean-all format lint tests publish \
	publish-test

# Targets
default: help

$(VENV_DIR)/bin/activate: $(PYPROJECT_TOML)
	@echo "Creating the 'venv'..."
	@$(PYTHON) -m venv --upgrade-deps "$(VENV_DIR)"
	@echo "Instaling requirements..."
	@"$(VENV_DIR)"/bin/$(PIP) install $(PIP_ARGS) "$(PROJECT_DIR)"[dev]
	@echo "Instaling project..."
	@"$(VENV_DIR)"/bin/$(PIP) install $(PIP_ARGS) "$(PROJECT_DIR)"

_clean-build:
	@echo "Cleaning build artifacts..."
	@$(RM) $(foreach artifact, $(BUILD_ARTIFACTS), "$(PROJECT_DIR)"/$(artifact))

_clean-cache:
	@echo "Cleaning cache..."
	@$(RM) $(addprefix $(PROJECT_DIR)/, $(CACHE_ITEMS))
	@$(FIND) "$(PROJECT_DIR)" -type f -name "*.py[co]" -delete \
		-o -type d -name "__pycache__" -delete

_clean-dev:
	@echo "Deleting the 'venv'..."
	@$(RM) "$(VENV_DIR)"/*
ifdef VIRTUAL_ENV
	@echo
	@echo "!! Python venv active. !!"
	@echo "Deactivate it using the following command:"
	@echo "deactivate"
	@echo
endif

_clean-docs:
	@echo "Cleaning documentation..."
	@$(FIND) "$(PROJECT_DIR)"/docs -type f -not -name '.*' -delete \
		-o -type d -delete

_clean-stubs:
	@echo "Deleting stubs..."
	@find "$(SOURCE_DIR)/$(PACKAGE_NAME)" -type f -name "*.pyi" -delete

build: $(VENV_DIR)/bin/activate _clean-build
	@echo "Building wheel..."
	@"$(VENV_DIR)"/bin/$(PYTHON) -m build "$(PROJECT_DIR)"

clean: _clean-build _clean-cache

clean-all: clean _clean-stubs _clean-dev

dev: $(VENV_DIR)/bin/activate

docs: $(VENV_DIR)/bin/activate _clean-docs
	@echo "Checking documentation examples..."
	@"$(VENV_DIR)"/bin/$(PYTEST) $(PYTEST_ARGS) $(PYTEST_DOC_ARGS) \
		--rootdir="$(PROJECT_DIR)" "$(SOURCE_DIR)/$(PACKAGE_NAME)"
	@echo "Generating documentation..."
	@"$(VENV_DIR)"/bin/$(PDOC) $(PDOC_ARGS) \
		--template-dir "$(SOURCE_DIR)"/docs/templates \
		--output-dir "$(PROJECT_DIR)/docs" \
		"$(SOURCE_DIR)/$(PACKAGE_NAME)"
	@$(MV) "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"/* "$(PROJECT_DIR)/docs/"
	@$(RM) "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"

format: $(VENV_DIR)/bin/activate
	@echo "Formating code..."
	@"$(VENV_DIR)"/bin/$(AUTOPEP) $(AUTOPEP_ARGS) "$(SOURCE_DIR)/$(PACKAGE_NAME)"

lint: $(VENV_DIR)/bin/activate
	@echo "Checking the code..."
	@"$(VENV_DIR)"/bin/$(PYLINT) $(PYLINT_ARGS) "$(SOURCE_DIR)/$(PACKAGE_NAME)"

minversion: $(VENV_DIR)/bin/activate
	@echo "Finding minimum Python version..."
	@"$(VENV_DIR)"/bin/$(VERMIN) $(VERMIN_ARGS) "$(SOURCE_DIR)/$(PACKAGE_NAME)"

publish: $(VENV_DIR)/bin/activate
ifeq (,$(wildcard $(PROJECT_DIR)/dist))
	@echo "Packages not found."
	@echo "Run 'make build' first to create them."
else
	@echo "Publishing to 'pypi.org'..."
	@"$(VENV_DIR)"/bin/$(TWINE) upload "$(PROJECT_DIR)"/dist/*
endif

publish-test: $(VENV_DIR)/bin/activate
ifeq (,$(wildcard $(PROJECT_DIR)/dist))
	@echo "Packages not found."
	@echo "Run 'make build' first to create them."
else
	@echo "Publishing to test.pypi.org..."
	@"$(VENV_DIR)"/bin/$(TWINE) upload --repository testpypi \
		"$(PROJECT_DIR)"/dist/*
endif

stubs: $(VENV_DIR)/bin/activate
	@echo "Generating stubs..."
	@"$(VENV_DIR)"/bin/$(STUBGEN) $(STUBGEN_ARGS) --package "$(PACKAGE_NAME)" \
		--search-path "$(SOURCE_DIR)" --output $(SOURCE_DIR)

tests: $(VENV_DIR)/bin/activate
	@echo "Running tests..."
	@"$(VENV_DIR)"/bin/$(PYTEST) $(PYTEST_ARGS) --cov="$(PACKAGE_NAME)" \
		--rootdir="$(PROJECT_DIR)"

help:
	@echo "make <target>"
	@echo
	@echo "targets:"
	@echo "  build"
	@echo "      Create library package(s)."
	@echo "  clean"
	@echo "      cleans the project caches and builds."
	@echo "  clean-all"
	@echo "      cleans everything."
	@echo "  dev"
	@echo "      creates the development environment."
	@echo "  docs"
	@echo "      creates the project documentation."
	@echo "  format"
	@echo "      formats the code."
	@echo "  lint"
	@echo "      check the project for code smells."
	@echo "  minversion"
	@echo "      calculates python minimum version required."
	@echo "  publish"
	@echo "      Uploads the project to 'pypi.org'."
	@echo "  publish-test"
	@echo "      Uploads the project to 'test.pypi.org'."
	@echo "  stubs"
	@echo "      generates stubs for the project."
	@echo "  tests"
	@echo "      runs the tests."
	@echo
