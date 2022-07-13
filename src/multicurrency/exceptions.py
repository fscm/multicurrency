# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency exceptions."""


class CurrencyException(Exception):
    """Generic Currency exception."""


class CurrencyInvalidDivision(CurrencyException, TypeError):
    """Invalid division."""

    def __init__(self, *args: object) -> None:
        super().__init__('Unsupported division operation.', *args)


class CurrencyInvalidFormat(CurrencyException, ValueError):
    """Invalid format."""

    def __init__(self, *args: object) -> None:
        super().__init__('Invalid currency format.', *args)


class CurrencyInvalidMultiplication(CurrencyException, TypeError):
    """Invalid multiplication."""

    def __init__(self, *args: object) -> None:
        super().__init__('Unsupported multiplication operation.', *args)


class CurrencyInvalidOperation(CurrencyException, TypeError):
    """Invalid operation."""

    def __init__(self, *args: object) -> None:
        super().__init__('Unsupported operation.', *args)


class CurrencyMismatchException(CurrencyException, TypeError):
    """Invalid operation between objects of different currencies."""

    def __init__(self, *args: object) -> None:
        super().__init__(
            'Unsupported operation for different currencies.', *args)


class CurrencyTypeException(CurrencyException, TypeError):
    """Invalid operation with objects of type other than `Currency`."""

    def __init__(self, *args: object) -> None:
        super().__init__(
            'Unsupported operation with non-Currency object.', *args)
