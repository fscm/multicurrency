# Changelog

## [v2.1.0](https://github.com/fscm/multicurrency/tree/v2.1.0) (2023-09-19)

### [changes](https://github.com/fscm/multicurrency/compare/v2.0.2...v2.1.0)

* fixed tests
* added 'ruff' linter
* replaced 'setuptools' with 'hatchling' as the build system
* replaced 'make' (Makefile) with 'just' (justfile)
* removed the no longer needed 'setup.py' file

## [v2.0.2](https://github.com/fscm/multicurrency/tree/v2.0.2) (2022-11-16)

### [changes](https://github.com/fscm/multicurrency/compare/v2.0.1...v2.0.2)

* precision behaviour changed to match the Decimal behaviour

## [v2.0.1](https://github.com/fscm/multicurrency/tree/v2.0.1) (2022-07-13)

### [changes](https://github.com/fscm/multicurrency/compare/v2.0.0...v2.0.1)

* small optimizations
* source code clean up

## [v2.0.0](https://github.com/fscm/multicurrency/tree/v2.0.0) (2022-07-13)

### [changes](https://github.com/fscm/multicurrency/compare/v1.0.1...v2.0.0)

* major refactoring of library code
* breaks compatibiliy with previous versions

## [v1.0.1](https://github.com/fscm/multicurrency/tree/v1.0.1) (2022-03-17)

### [changes](https://github.com/fscm/multicurrency/compare/v1.0.0...v1.0.1)

* small changes to comply with 'pyanalyze'

## [v1.0.0](https://github.com/fscm/multicurrency/tree/v1.0.0) (2022-01-12)

### [changes](https://github.com/fscm/multicurrency/compare/v0.11.0...v1.0.0)

* 'pstr' deprecated and replaced with 'precision'
* 'lstr' deprecated and replaced with 'localized'
* 'currency' and 'exceptions' are now private
* documentation updated
* generator tool updated
* first stable release

## [v0.11.0](https://github.com/fscm/multicurrency/tree/v0.11.0) (2021-12-28)

### [changes](https://github.com/fscm/multicurrency/compare/v0.10.0...v0.11.0)

* .nojekyll added to the 'docs' folder
* added support for python 3.10
* f-string used in setup.py
* documentation updated ('lstr' method was missing)
* fixed hash method tests

## [v0.10.0](https://github.com/fscm/multicurrency/tree/v0.10.0) (2021-10-26)

### [changes](https://github.com/fscm/multicurrency/compare/v0.9.0...v0.10.0)

* added localized representation of the currencies
* documentation examples checked with doctest
* MANIFEST.in added to fix build issue with the 'requirements.txt' file

## [v0.9.0](https://github.com/fscm/multicurrency/tree/v0.9.0) (2021-07-26)

### [changes](https://github.com/fscm/multicurrency/compare/v0.8.0...v0.9.0)

* 'grouping_places' added to 'Currency'
* basic formatting support added (with the '__format__()' method)

## [v0.8.0](https://github.com/fscm/multicurrency/tree/v0.8.0) (2021-06-22)

### [changes](https://github.com/fscm/multicurrency/compare/v0.7.0...v0.8.0)

* 'Ethereum' cryptocurrency added
* number of decimal places for the Stellar Lumens cryptocurrency changed (to 7)

## [v0.7.0](https://github.com/fscm/multicurrency/tree/v0.7.0) (2021-06-08)

### [changes](https://github.com/fscm/multicurrency/compare/v0.6.0...v0.7.0)

* python minimum version required changed to 3.6 (from 3.9)

## [v0.6.0](https://github.com/fscm/multicurrency/tree/v0.6.0) (2021-05-21)

### [changes](https://github.com/fscm/multicurrency/compare/v0.5.0...v0.6.0)

* added support for (some) cryptocurrencies
* currency symbols (and format) updated
* python minimum version changed to 3.8 (from 3.9)
* build tools updated
* changed 'venv' folder to '.venv'

## [v0.5.0](https://github.com/fscm/multicurrency/tree/v0.5.0) (2021-05-10)

### [changes](https://github.com/fscm/multicurrency/compare/v0.4.0...v0.5.0)

* added '__rsub__' method and tests
* added '__deepcopy__' method and tests
* fix: 'Makefile' issue with project lib path
* added  extra verbose arg to the 'Makefile' 'tests-v
* dev-upgrade added to 'Makefile'
* dev requirements changed to a file (requirements-dev.txt)
* '.gitignore' file updated
* feature: 'Changelog.md' file added
* fix: fixed 'Makefile' issue with 'dev' target
* documentation update

## [v0.4.0](https://github.com/fscm/multicurrency/tree/v0.4.0) (2021-04-22)

### [changes](https://github.com/fscm/multicurrency/compare/v0.3.0...v0.4.0)

* bitcoin symbol updated on the 'README.md' file
* preparing docs for github pages
* 'generator' script cleanup (easier to catch IDE errors now)
* removed the grouping and decimal signs from the 'convertion' string
* added localization to some currencies representation

## [v0.3.0](https://github.com/fscm/multicurrency/tree/v0.3.0) (2021-04-16)

### [changes](https://github.com/fscm/multicurrency/compare/v0.2.0...v0.3.0)

* added symbol position and spacing
* replaced 'space' with 'non-breaking space'
* renamed: currency.currency -> currency.alpha_code
* renamed: currency.code -> currency.numeric_code
* 'README.md' file updated
* Ireland Euro format (EuroIE) added
* remove space in a list comprehesion of the 'generator' tool
* tests: added another precision test
* optimizations on 'currency.py' __str__ and pstr
* cleaning the 'profiler' tool
* cleaning the 'generator' tool
* fix 'workfolder' value on 'generator' tool
* optimizations on 'currency.py' '__str__' and 'pstr'
* removed unused var from 'setup.py'
* small optimization on currency.py

## [v0.2.0](https://github.com/fscm/multicurrency/tree/v0.2.0) (2021-04-07)

### [changes](https://github.com/fscm/multicurrency/compare/v0.1.0...v0.2.0)

* currencies gruped by 'class'.
* '.gitignore' file updated

## [v0.1.0](https://github.com/fscm/multicurrency/tree/v0.1.0) (2021-03-26)

### changes

* Initial commit
