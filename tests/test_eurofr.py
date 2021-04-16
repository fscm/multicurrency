# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroFR representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroFR
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurofr():
    """test_eurofr."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurofr = EuroFR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurofr.amount == decimal
    assert eurofr.numeric_code == '978'
    assert eurofr.alpha_code == 'EUR'
    assert eurofr.decimal_places == 2
    assert eurofr.decimal_sign == ','
    assert eurofr.grouping_sign == '\u202F'
    assert not eurofr.international
    assert eurofr.symbol == '€'
    assert not eurofr.symbol_ahead
    assert eurofr.symbol_separator == '\u00A0'
    assert eurofr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofr.__repr__() == (
        'EuroFR(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurofr.__str__() == '0,14 €'


def test_eurofr_negative():
    """test_eurofr_negative."""
    amount = -100
    eurofr = EuroFR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurofr.numeric_code == '978'
    assert eurofr.alpha_code == 'EUR'
    assert eurofr.decimal_places == 2
    assert eurofr.decimal_sign == ','
    assert eurofr.grouping_sign == '\u202F'
    assert not eurofr.international
    assert eurofr.symbol == '€'
    assert not eurofr.symbol_ahead
    assert eurofr.symbol_separator == '\u00A0'
    assert eurofr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofr.__repr__() == (
        'EuroFR(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurofr.__str__() == '-100,00 €'


def test_eurofr_custom():
    """test_eurofr_custom."""
    amount = 1000
    eurofr = EuroFR(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurofr.amount == decimal
    assert eurofr.numeric_code == '978'
    assert eurofr.alpha_code == 'EUR'
    assert eurofr.decimal_places == 5
    assert eurofr.decimal_sign == '\u202F'
    assert eurofr.grouping_sign == ','
    assert eurofr.international
    assert eurofr.symbol == '€'
    assert not eurofr.symbol_ahead
    assert eurofr.symbol_separator == '_'
    assert eurofr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofr.__repr__() == (
        'EuroFR(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert eurofr.__str__() == 'EUR 1,000.00000'


def test_eurofr_changed():
    """test_ceurofr_changed."""
    eurofr = EuroFR(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofr.international = True


def test_eurofr_math_add():
    """test_eurofr_math_add."""
    eurofr_one = EuroFR(amount=1)
    eurofr_two = EuroFR(amount=2)
    eurofr_three = EuroFR(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurofr_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroFR\'> '
                   'and <class \'str\'>.')):
        _ = eurofr_one.__add__('1.00')
    assert (
        eurofr_one +
        eurofr_two) == eurofr_three


def test_eurofr_slots():
    """test_eurofr_slots."""
    eurofr = EuroFR(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroFR\' '
                'object has no attribute \'new_variable\'')):
        eurofr.new_variable = 'fail'  # pylint: disable=assigning-non-slot
