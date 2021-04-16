# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroLT representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroLT
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurolt():
    """test_eurolt."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurolt = EuroLT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolt.amount == decimal
    assert eurolt.numeric_code == '978'
    assert eurolt.alpha_code == 'EUR'
    assert eurolt.decimal_places == 2
    assert eurolt.decimal_sign == ','
    assert eurolt.grouping_sign == '\u202F'
    assert not eurolt.international
    assert eurolt.symbol == '€'
    assert not eurolt.symbol_ahead
    assert eurolt.symbol_separator == '\u00A0'
    assert eurolt.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolt.__repr__() == (
        'EuroLT(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurolt.__str__() == '0,14 €'


def test_eurolt_negative():
    """test_eurolt_negative."""
    amount = -100
    eurolt = EuroLT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolt.numeric_code == '978'
    assert eurolt.alpha_code == 'EUR'
    assert eurolt.decimal_places == 2
    assert eurolt.decimal_sign == ','
    assert eurolt.grouping_sign == '\u202F'
    assert not eurolt.international
    assert eurolt.symbol == '€'
    assert not eurolt.symbol_ahead
    assert eurolt.symbol_separator == '\u00A0'
    assert eurolt.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolt.__repr__() == (
        'EuroLT(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurolt.__str__() == '-100,00 €'


def test_eurolt_custom():
    """test_eurolt_custom."""
    amount = 1000
    eurolt = EuroLT(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurolt.amount == decimal
    assert eurolt.numeric_code == '978'
    assert eurolt.alpha_code == 'EUR'
    assert eurolt.decimal_places == 5
    assert eurolt.decimal_sign == '\u202F'
    assert eurolt.grouping_sign == ','
    assert eurolt.international
    assert eurolt.symbol == '€'
    assert not eurolt.symbol_ahead
    assert eurolt.symbol_separator == '_'
    assert eurolt.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolt.__repr__() == (
        'EuroLT(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert eurolt.__str__() == 'EUR 1,000.00000'


def test_eurolt_changed():
    """test_ceurolt_changed."""
    eurolt = EuroLT(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolt.international = True


def test_eurolt_math_add():
    """test_eurolt_math_add."""
    eurolt_one = EuroLT(amount=1)
    eurolt_two = EuroLT(amount=2)
    eurolt_three = EuroLT(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurolt_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroLT\'> '
                   'and <class \'str\'>.')):
        _ = eurolt_one.__add__('1.00')
    assert (
        eurolt_one +
        eurolt_two) == eurolt_three


def test_eurolt_slots():
    """test_eurolt_slots."""
    eurolt = EuroLT(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroLT\' '
                'object has no attribute \'new_variable\'')):
        eurolt.new_variable = 'fail'  # pylint: disable=assigning-non-slot
