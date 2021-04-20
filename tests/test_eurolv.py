# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroLV representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroLV
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurolv():
    """test_eurolv."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurolv = EuroLV(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolv.amount == decimal
    assert eurolv.numeric_code == '978'
    assert eurolv.alpha_code == 'EUR'
    assert eurolv.decimal_places == 2
    assert eurolv.decimal_sign == ','
    assert eurolv.grouping_sign == '\u202F'
    assert not eurolv.international
    assert eurolv.symbol == '€'
    assert not eurolv.symbol_ahead
    assert eurolv.symbol_separator == '\u00A0'
    assert eurolv.convertion == ''
    assert eurolv.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolv.__repr__() == (
        'EuroLV(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert eurolv.__str__() == '0,14 €'


def test_eurolv_negative():
    """test_eurolv_negative."""
    amount = -100
    eurolv = EuroLV(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolv.numeric_code == '978'
    assert eurolv.alpha_code == 'EUR'
    assert eurolv.decimal_places == 2
    assert eurolv.decimal_sign == ','
    assert eurolv.grouping_sign == '\u202F'
    assert not eurolv.international
    assert eurolv.symbol == '€'
    assert not eurolv.symbol_ahead
    assert eurolv.symbol_separator == '\u00A0'
    assert eurolv.convertion == ''
    assert eurolv.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolv.__repr__() == (
        'EuroLV(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert eurolv.__str__() == '-100,00 €'


def test_eurolv_custom():
    """test_eurolv_custom."""
    amount = 1000
    eurolv = EuroLV(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurolv.amount == decimal
    assert eurolv.numeric_code == '978'
    assert eurolv.alpha_code == 'EUR'
    assert eurolv.decimal_places == 5
    assert eurolv.decimal_sign == '\u202F'
    assert eurolv.grouping_sign == ','
    assert eurolv.international
    assert eurolv.symbol == '€'
    assert not eurolv.symbol_ahead
    assert eurolv.symbol_separator == '_'
    assert eurolv.convertion == ''
    assert eurolv.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolv.__repr__() == (
        'EuroLV(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurolv.__str__() == 'EUR 1,000.00000'


def test_eurolv_changed():
    """test_ceurolv_changed."""
    eurolv = EuroLV(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolv.international = True


def test_eurolv_math_add():
    """test_eurolv_math_add."""
    eurolv_one = EuroLV(amount=1)
    eurolv_two = EuroLV(amount=2)
    eurolv_three = EuroLV(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurolv_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroLV\'> '
                   'and <class \'str\'>.')):
        _ = eurolv_one.__add__('1.00')
    assert (
        eurolv_one +
        eurolv_two) == eurolv_three


def test_eurolv_slots():
    """test_eurolv_slots."""
    eurolv = EuroLV(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroLV\' '
                'object has no attribute \'new_variable\'')):
        eurolv.new_variable = 'fail'  # pylint: disable=assigning-non-slot
