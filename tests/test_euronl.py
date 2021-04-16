# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroNL representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroNL
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euronl():
    """test_euronl."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euronl = EuroNL(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euronl.amount == decimal
    assert euronl.numeric_code == '978'
    assert euronl.alpha_code == 'EUR'
    assert euronl.decimal_places == 2
    assert euronl.decimal_sign == ','
    assert euronl.grouping_sign == '.'
    assert not euronl.international
    assert euronl.symbol == '€'
    assert euronl.symbol_ahead
    assert euronl.symbol_separator == '\u00A0'
    assert euronl.__hash__() == hash((decimal, 'EUR', '978'))
    assert euronl.__repr__() == (
        'EuroNL(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euronl.__str__() == '€ 0,14'


def test_euronl_negative():
    """test_euronl_negative."""
    amount = -100
    euronl = EuroNL(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euronl.numeric_code == '978'
    assert euronl.alpha_code == 'EUR'
    assert euronl.decimal_places == 2
    assert euronl.decimal_sign == ','
    assert euronl.grouping_sign == '.'
    assert not euronl.international
    assert euronl.symbol == '€'
    assert euronl.symbol_ahead
    assert euronl.symbol_separator == '\u00A0'
    assert euronl.__hash__() == hash((decimal, 'EUR', '978'))
    assert euronl.__repr__() == (
        'EuroNL(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euronl.__str__() == '€ -100,00'


def test_euronl_custom():
    """test_euronl_custom."""
    amount = 1000
    euronl = EuroNL(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euronl.amount == decimal
    assert euronl.numeric_code == '978'
    assert euronl.alpha_code == 'EUR'
    assert euronl.decimal_places == 5
    assert euronl.decimal_sign == '.'
    assert euronl.grouping_sign == ','
    assert euronl.international
    assert euronl.symbol == '€'
    assert not euronl.symbol_ahead
    assert euronl.symbol_separator == '_'
    assert euronl.__hash__() == hash((decimal, 'EUR', '978'))
    assert euronl.__repr__() == (
        'EuroNL(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert euronl.__str__() == 'EUR 1,000.00000'


def test_euronl_changed():
    """test_ceuronl_changed."""
    euronl = EuroNL(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euronl.international = True


def test_euronl_math_add():
    """test_euronl_math_add."""
    euronl_one = EuroNL(amount=1)
    euronl_two = EuroNL(amount=2)
    euronl_three = EuroNL(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euronl_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroNL\'> '
                   'and <class \'str\'>.')):
        _ = euronl_one.__add__('1.00')
    assert (
        euronl_one +
        euronl_two) == euronl_three


def test_euronl_slots():
    """test_euronl_slots."""
    euronl = EuroNL(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroNL\' '
                'object has no attribute \'new_variable\'')):
        euronl.new_variable = 'fail'  # pylint: disable=assigning-non-slot
