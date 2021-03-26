# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Currency exceptions."""

from typing import Any


class CurrencyException(Exception):
    """Generic Currency exception."""


class CurrencyInvalidDivision(CurrencyException, TypeError):
    """Invalid division.

    Args:
        first (Any): Object.
        second (Any): Object.
    """

    def __init__(self, first: 'Currency', second: Any) -> None:
        super().__init__(
            'division not supported between '
            f'{type(first)} and {type(second)}.')


class CurrencyInvalidMultiplication(CurrencyException, TypeError):
    """Invalid multiplication.

    Args:
        first (Any): Object.
        second (Any): Object.
    """

    def __init__(self, first: 'Currency', second: Any) -> None:
        super().__init__(
            'multiplication not supported between '
            f'{type(first)} and {type(second)}.')


class CurrencyInvalidOperation(CurrencyException, TypeError):
    """Invalid operation.

    Args:
        operation (str): Operation name.
        element (Any): Object.
    """

    def __init__(self, operation: str, element: Any) -> None:
        super().__init__(
            f'unsupported operation \'{operation}\' with {type(element)}.')


class CurrencyMismatchException(CurrencyException, ValueError):
    """Invalid operation between objects of different currencies.

    Args:
        first (str): Currency.
        second (str): Currency.
    """

    def __init__(self, first: str, second: str) -> None:
        super().__init__(
            'unsupported operation between currency '
            f'{first} and {second}.')


class CurrencyTypeException(CurrencyException, TypeError):
    """Invalid operation with objects of type other than `Currency`.

    Args:
        first (Any): Object.
        second (Any): Object.
    """

    def __init__(self, first: Any, second: Any) -> None:
        super().__init__(
            f'unsupported operation between {type(first)} and {type(second)}.')
