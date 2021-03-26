PACKAGE_NAME := multicurrency
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PROJECT_DIR := $(realpath $(dir $(MAKEFILE_PATH)))
PDOC := pdoc3
AUTOPEP := autopep8
PIP := pip3
PYLINT := pylint
PYTEST := pytest
PYTHON := python3
REQUIREMENTS := requirements.txt
REQUIREMENTS_DEV := autopep8 build mypy pdoc3 pylint pytest pytest-cov pytest-mock twine
SHELL := /bin/sh
STUBGEN := stubgen
#SOURCES := $(wildcard "$(PROJECT_DIR)/$(PACKAGE_NAME)"/*.py)
TWINE := twine

PYTHON_LIBS = "$(wildcard $(PROJECT_DIR)/venv/lib/python*)/site-packages"

.NOTPARALLEL:

.ONESHELL:

.PHONY: default
default: help

.PHONY: all
all: stubs autopep8 lint doc tests build

.PHONY: autopep8
autopep8:
ifdef VIRTUAL_ENV
	@echo "Formating code..."
	@$(AUTOPEP) --aggressive --aggressive --in-place --recursive \
		--global-config "$(PROJECT_DIR)"/.pep8 "$(PROJECT_DIR)/$(PACKAGE_NAME)"
	@echo "Formating tests..."
	@$(AUTOPEP) --aggressive --aggressive --in-place --recursive \
		--global-config "$(PROJECT_DIR)"/.pep8 "$(PROJECT_DIR)/tests"
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: build
build:
ifdef VIRTUAL_ENV
  ifeq (,$(wildcard $(PROJECT_DIR)/build))
	@echo "Building wheel..."
	@cd "$(PROJECT_DIR)"
	@$(PYTHON) -m build
  else
	@echo "Previous build detected."
	@echo "Run 'make clean-build' to remove it first."
  endif
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: clean clean-all clean-build clean-cache clean-dev clean-doc
clean: clean-cache clean-dev

clean-all: clean-build clean-cache clean-dev clean-doc

clean-build:
	@echo "Cleaning build artifacts..."
	@rm -rf "$(PROJECT_DIR)"/build \
		"$(PROJECT_DIR)"/dist \
		"$(PROJECT_DIR)"/*.egg-info

clean-cache:
	@echo "Cleaning cache..."
	@rm -rf "$(PROJECT_DIR)"/.mypy_cache \
		"$(PROJECT_DIR)"/.pytest_cache \
		"$(PROJECT_DIR)/$(PACKAGE_NAME)"/__pycache__ \
		"$(PROJECT_DIR)"/tests/__pycache__ \
		"$(PROJECT_DIR)"/.coverage

clean-dev:
ifndef VIRTUAL_ENV
	@echo "Cleaning venv..."
	@rm -rf "$(PROJECT_DIR)"/venv/*
else
	@echo "venv enabled."
	@echo "Run 'deactivate' to disable the venv first."
endif

clean-doc:
	@echo "Cleaning documentation..."
	@rm -rf "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"

.PHONY: dev _dev
_dev:
ifndef VIRTUAL_ENV
  ifeq (,$(wildcard $(PROJECT_DIR)/venv/created))
	@echo "Creating 'venv'..."
	@$(PYTHON) -m venv "$(PROJECT_DIR)"/venv/
	@date > "$(PROJECT_DIR)/venv/created"
	@echo "Instaling requirements..."
	@source "$(PROJECT_DIR)"/venv/bin/activate; \
		$(PIP) --quiet install --upgrade --requirement \
		"$(PROJECT_DIR)/$(REQUIREMENTS)" $(REQUIREMENTS_DEV)
  else
	@echo "'venv' already created."
	@echo "Run 'make clean-dev' to remove it first."
  endif
else
	@echo "venv enabled."
	@echo "Run 'deactivate' to disable the venv first."
endif

dev: _dev
	@echo "Adding project to Python..."
	@echo "$(PROJECT_DIR)" > "$(PYTHON_LIBS)/$(PACKAGE_NAME).pth"

.PHONY: doc
doc:
ifdef VIRTUAL_ENV
	@echo "Generating documentation..."
	@$(PDOC) --force --html --config show_source_code=False \
		--output-dir "$(PROJECT_DIR)/docs" "$(PROJECT_DIR)/$(PACKAGE_NAME)"
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: lint
lint:
ifdef VIRTUAL_ENV
	@echo "Checking the code..."
	@$(PYLINT) -v --exit-zero --rcfile "$(PROJECT_DIR)/.pylintrc" \
		"$(PROJECT_DIR)/$(PACKAGE_NAME)"
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: publish publish-test
publish:
ifdef VIRTUAL_ENV
  ifeq (,$(wildcard $(PROJECT_DIR)/dist))
	@echo "Packages not found."
	@echo "Run 'make build' first to create them."
  else
	@echo "Publishing to 'pypi.org'..."
	@$(TWINE) upload "$(PROJECT_DIR)"/dist/*
  endif
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

publish-test:
ifdef VIRTUAL_ENV
  ifeq (,$(wildcard $(PROJECT_DIR)/dist))
	@echo "Packages not found."
	@echo "Run 'make build' first to create them."
  else
	@echo "Publishing to test.pypi.org..."
	@$(TWINE) upload --repository testpypi "$(PROJECT_DIR)"/dist/*
  endif
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: stubs
stubs:
ifdef VIRTUAL_ENV
	@echo "Generating stubs..."
	@$(STUBGEN) --export-less --package "$(PACKAGE_NAME)" \
		--search-path "$(PROJECT_DIR)" --output .
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: tests tests-debug
tests:
ifdef VIRTUAL_ENV
	@echo "Running tests..."
	@cd "$(PROJECT_DIR)"
	@$(PYTEST) --color=auto --quiet
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

tests-verbose:
ifdef VIRTUAL_ENV
	@echo "Running tests..."
	@cd "$(PROJECT_DIR)"
	@$(PYTEST) --cache-clear --color=auto --capture=tee-sys --verbose
else
	@echo "venv not enabled."
	@echo "Run 'source $(PROJECT_DIR)/venv/bin/activate' to enable the venv."
endif

.PHONY: help
help:
	@echo "make <option>"
	@echo
	@echo "options:"
	@echo "  autopep8"
	@echo "      Format the code."
	@echo "  clean"
	@echo "      Cleans the development environment."
	@echo "  clean-all"
	@echo "      Cleans everything."
	@echo "  clean-cache"
	@echo "      Cleans all Python (and tools) caches."
	@echo "  clean-dev"
	@echo "      Removes the entire dev environment."
	@echo "  clean-doc"
	@echo "      Removes the documentation."
	@echo "  dev"
	@echo "      Prepares the dev environment for this project (including venv)."
	@echo "  doc"
	@echo "      Create project documentation."
	@echo "  lint"
	@echo "      Check the project for code smells."
	@echo "  stubs"
	@echo "      Generates stubs for the project."
	@echo "  tests"
	@echo "      Runs the tests."
	@echo
	@echo "build options:"
	@echo "  build"
	@echo "      Create library packages."
	@echo "  clean-build"
	@echo "      Cleans build artifacts."
	@echo "  publish"
	@echo "      Uploads the project to 'pypi.org'."
	@echo "  publish-test"
	@echo "      Uploads the project to 'test.pypi.org'."
	@echo
