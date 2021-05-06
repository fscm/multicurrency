# Project Macros/Variables                    Project Macros/Variables --------
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PROJECT_DIR := $(realpath $(dir $(MAKEFILE_PATH)))
PACKAGE_NAME := $(notdir $(PROJECT_DIR))

# Tools
AUTOPEP := autopep8
PDOC := pdoc3
PIP := pip3
PYLINT := pylint
PYTEST := pytest
PYTHON := python3
STUBGEN := stubgen
TWINE := twine

# Shell                                                          Shell --------
SHELL := /bin/sh

# Python Macros/Variables                      Python Macros/Variables --------
REQUIREMENTS := requirements.txt
REQUIREMENTS_DEV := requirements-dev.txt
SOURCE_DIR := $(PROJECT_DIR)
SOURCE_FILES := $(wildcard $(SOURCE_DIR)/$(PACKAGE_NAME)/*.py)
VENV_DIR := $(PROJECT_DIR)/venv

PYTHON_LIBS = $(wildcard $(VENV_DIR)/lib/python*)/site-packages

# Rules                                                          Rules --------
.NOTPARALLEL:

.ONESHELL:

.PHONY: default all
.PHONY: clean clean-all clean-build clean-cache clean-dev clean-docs clean-stubs
.PHONY: dev autopep8 docs lint stubs tests tests-verbose
.PHONY: build publish publish-test

# Project Targets                                      Project Targets --------
# -- default                                                       default ----
default: help

# -- all                                                               all ----
all: stubs autopep8 lint docs tests build

# Cleaning Targets                                    Cleaning Targets --------
# -- clean                                                           clean ----
clean: clean-build clean-cache

# -- clean all                                                   clean all ----
clean-all: clean-build clean-cache clean-stubs clean-docs clean-dev

# -- clean build                                               clean build ----
clean-build:
	@echo "Cleaning build artifacts..."
	@rm -rf "$(PROJECT_DIR)"/build \
		"$(PROJECT_DIR)"/dist \
		"$(PROJECT_DIR)"/*.egg-info

# -- clean cache                                               clean cache ----
clean-cache:
	@echo "Cleaning cache..."
	@rm -rf "$(PROJECT_DIR)"/.mypy_cache \
		"$(PROJECT_DIR)"/.pytest_cache \
		"$(SOURCE_DIR)/$(PACKAGE_NAME)"/__pycache__ \
		"$(PROJECT_DIR)"/tests/__pycache__ \
		"$(PROJECT_DIR)"/.coverage
	@find "$(VENV_DIR)" -type f -name "*.pyc" -delete

# -- clean dev                                                   clean dev ----
clean-dev:
	@echo "Deleting the 'venv'..."
	@rm -rf "$(PROJECT_DIR)"/venv/*
ifdef VIRTUAL_ENV
	@echo
	@echo "!! Python venv active. !!"
	@echo "Deactivate it using the following command:"
	@echo "deactivate"
	@echo
endif

# -- clean docs                                                 clean docs ----
clean-docs:
	@echo "Cleaning documentation..."
	@rm -rf "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"
	@rm -rf "$(PROJECT_DIR)/docs"/*.html

# -- clean stubs                                               clean stubs ----
clean-stubs:
	@echo "Deleting stubs..."
	@rm -rf "$(SOURCE_DIR)"/$(PACKAGE_NAME)/*.pyi

# Python Targets                                        Python Targets --------
# -- venv                                                             venv ----
$(VENV_DIR)/bin/activate: $(PROJECT_DIR)/$(REQUIREMENTS)
	@echo "Creating the 'venv'..."
	@$(PYTHON) -m venv "$(VENV_DIR)"
	@echo "Instaling requirements..."
	@"$(VENV_DIR)"/bin/$(PIP) --quiet install --upgrade \
		--requirement "$(PROJECT_DIR)/$(REQUIREMENTS)" \
		--requirement "$(PROJECT_DIR)/$(REQUIREMENTS_DEV)"

# -- dev                                                               dev ----
dev: $(VENV_DIR)/bin/activate
	@echo "Adding the project to Python libs..."
	@echo "$(PROJECT_DIR)/src" > "$(PYTHON_LIBS)/$(PACKAGE_NAME).pth"

# -- autopep8                                                     autopep8 ----
autopep8: $(VENV_DIR)/bin/activate
	@echo "Formating code..."
	@"$(VENV_DIR)"/bin/$(AUTOPEP) --aggressive --aggressive --in-place \
		--recursive --global-config "$(PROJECT_DIR)"/.pep8 \
		"$(SOURCE_DIR)/$(PACKAGE_NAME)"
	@echo "Formating tests..."
	@"$(VENV_DIR)"/bin/$(AUTOPEP) --aggressive --aggressive --in-place \
		--recursive --global-config "$(PROJECT_DIR)"/.pep8 \
		"$(PROJECT_DIR)/tests"

# -- docs                                                             docs ----
docs: $(VENV_DIR)/bin/activate
	@echo "Generating documentation..."
	@"$(VENV_DIR)"/bin/$(PDOC) --force --html --config show_source_code=False \
		--output-dir "$(PROJECT_DIR)/docs" "$(SOURCE_DIR)/$(PACKAGE_NAME)"
	@mv "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"/*.html "$(PROJECT_DIR)/docs/"
	@rm -rf "$(PROJECT_DIR)/docs/$(PACKAGE_NAME)"

# -- lint                                                             lint ----
lint: $(VENV_DIR)/bin/activate
	@echo "Checking the code..."
	@"$(VENV_DIR)"/bin/$(PYLINT) --verbose --exit-zero \
		--rcfile "$(PROJECT_DIR)/.pylintrc" \
		"$(SOURCE_DIR)/$(PACKAGE_NAME)"

# -- stubs                                                           stubs ----
stubs: $(VENV_DIR)/bin/activate
	@echo "Generating stubs..."
	@"$(VENV_DIR)"/bin/$(STUBGEN) --export-less --package "$(PACKAGE_NAME)" \
		--search-path "$(SOURCE_DIR)" --output $(SOURCE_DIR)

# -- tests                                                           tests ----
tests: $(VENV_DIR)/bin/activate
	@echo "Running tests..."
	@"$(VENV_DIR)"/bin/$(PYTEST) --quiet --no-header --color=auto \
		--rootdir="$(PROJECT_DIR)"

tests-verbose: $(VENV_DIR)/bin/activate
	@echo "Running tests (verbose mode)..."
	@"$(VENV_DIR)"/bin/$(PYTEST) --verbose --cache-clear --color=auto \
		--capture=tee-sys --rootdir="$(PROJECT_DIR)"

# Build Targets                                          Build Targets --------
# -- build                                                           build ----
build: $(VENV_DIR)/bin/activate clean-build
	@echo "Building wheel..."
	@cd "$(PROJECT_DIR)"
	@"$(VENV_DIR)"/bin/$(PYTHON) -m build

# -- publish                                                       publish ----
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

# Help Targets                                            Help Targets --------
# -- help                                                             help ----
help:
	@echo "make <option>"
	@echo
	@echo "options:"
	@echo "  autopep8"
	@echo "      Format the code."
	@echo "  clean"
	@echo "      Cleans the project caches and builds."
	@echo "  clean-all"
	@echo "      Cleans everything."
	@echo "  clean-cache"
	@echo "      Cleans all Python (and tools) caches."
	@echo "  clean-dev"
	@echo "      Removes the entire dev environment (venv)."
	@echo "  clean-docs"
	@echo "      Removes the documentation."
	@echo "  dev"
	@echo "      Creates the dev environment for this project (including venv)."
	@echo "  docs"
	@echo "      Creates the project documentation."
	@echo "  lint"
	@echo "      Check the project for code smells."
	@echo "  stubs"
	@echo "      Generates stubs for the project."
	@echo "  tests"
	@echo "      Runs the tests."
	@echo "  tests-verbose"
	@echo "      Runs the tests in verbose mode."
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
