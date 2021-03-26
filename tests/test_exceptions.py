# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Exceptions of Currency module."""

from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyException,
    CurrencyInvalidDivision,
    CurrencyInvalidMultiplication,
    CurrencyInvalidOperation,
    CurrencyMismatchException,
    CurrencyTypeException)


def aux_currency_mismatch_exception():
    euro = Currency(amount=1.0, currency='EUR')
    dollar = Currency(amount=1.0, currency='USD')
    raise CurrencyMismatchException(euro.currency, dollar.currency)


def aux_multicurrency_exception():
    raise CurrencyException()


def aux_multicurrency_invalid_division_exception():
    currency = Currency(amount=1.0)
    raise CurrencyInvalidDivision(currency, 'string')


def aux_multicurrency_invalid_multiplication_exception():
    currency = Currency(amount=1.0)
    raise CurrencyInvalidMultiplication(currency, 'string')


def aux_multicurrency_invalid_operation_exception():
    currency = Currency(amount=1.0)
    raise CurrencyInvalidOperation('name', currency)


def aux_multicurrency_type_exception():
    currency = Currency(amount=1.0)
    raise CurrencyTypeException(currency, 'currency')


def test_currency_mismatch_exception():
    """test_currency_mismatch_exception."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        aux_currency_mismatch_exception()


def test_multicurrency_exception():
    """test_multicurrency_exception."""
    with raises(
            CurrencyException,
            match=''):
        aux_multicurrency_exception()


def test_multicurrency_invalid_division_exception():
    """test_multicurrency_invalid_division_exception."""
    with raises(
            CurrencyInvalidDivision,
            match=('division not supported between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        aux_multicurrency_invalid_division_exception()


def test_multicurrency_invalid_multiplication_exception():
    """test_multicurrency_invalid_multiplication_exception."""
    with raises(
            CurrencyInvalidMultiplication,
            match=('multiplication not supported between <class '
                   '\'multicurrency.currency.Currency\'> and <class '
                   '\'str\'>.')):
        aux_multicurrency_invalid_multiplication_exception()


def test_multicurrency_invalid_operation_exception():
    """test_multicurrency_invalid_operation_exception."""
    with raises(
            CurrencyInvalidOperation,
            match=('unsupported operation \'name\' with <class '
                   '\'multicurrency.currency.Currency\'>.')):
        aux_multicurrency_invalid_operation_exception()


def test_multicurrency_type_exception():
    """test_multicurrency_type_exception."""
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        aux_multicurrency_type_exception()
