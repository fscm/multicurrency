# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Exceptions of Currency module."""

from pytest import mark, raises
from multicurrency.exceptions import (
    CurrencyException,
    CurrencyInvalidDivision,
    CurrencyInvalidFormat,
    CurrencyInvalidMultiplication,
    CurrencyInvalidOperation,
    CurrencyMismatchException,
    CurrencyTypeException)


@mark.parametrize('exception,message,expected', [
    (CurrencyException, None, r"^$"),
    (CurrencyException, 'extra message', r"^extra message$"),
    (CurrencyInvalidDivision, None, r"^Unsupported division operation.$"),
    (CurrencyInvalidDivision, 'extra message', r"^\('Unsupported division operation.', 'extra message'\)$"),
    (CurrencyInvalidFormat, None, r"^Invalid currency format.$"),
    (CurrencyInvalidFormat, 'extra message', r"^\('Invalid currency format.', 'extra message'\)$"),
    (CurrencyInvalidMultiplication, None, r"^Unsupported multiplication operation.$"),
    (CurrencyInvalidMultiplication, 'extra message', r"^\('Unsupported multiplication operation.', 'extra message'\)$"),
    (CurrencyInvalidOperation, None, r"^Unsupported operation.$"),
    (CurrencyInvalidOperation, 'extra message', r"^\('Unsupported operation.', 'extra message'\)$"),
    (CurrencyMismatchException, None, r"^Unsupported operation for different currencies.$"),
    (CurrencyMismatchException, 'extra message', r"^\('Unsupported operation for different currencies.', 'extra message'\)$"),
    (CurrencyTypeException, None, r"^Unsupported operation with non-Currency object.$"),
    (CurrencyTypeException, 'extra message', r"^\('Unsupported operation with non-Currency object.', 'extra message'\)$")
])
def test_currency_exceptions(exception, message, expected):
    with raises(exception, match=expected):
        if message:
            raise exception(message)
        raise exception()
