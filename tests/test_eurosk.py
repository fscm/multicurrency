# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroSK representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroSK
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurosk():
    """test_eurosk."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurosk = EuroSK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosk.amount == decimal
    assert eurosk.numeric_code == '978'
    assert eurosk.alpha_code == 'EUR'
    assert eurosk.decimal_places == 2
    assert eurosk.decimal_sign == ','
    assert eurosk.grouping_sign == '\u202F'
    assert not eurosk.international
    assert eurosk.symbol == '€'
    assert not eurosk.symbol_ahead
    assert eurosk.symbol_separator == '\u00A0'
    assert eurosk.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosk.__repr__() == (
        'EuroSK(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurosk.__str__() == '0,14 €'


def test_eurosk_negative():
    """test_eurosk_negative."""
    amount = -100
    eurosk = EuroSK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosk.numeric_code == '978'
    assert eurosk.alpha_code == 'EUR'
    assert eurosk.decimal_places == 2
    assert eurosk.decimal_sign == ','
    assert eurosk.grouping_sign == '\u202F'
    assert not eurosk.international
    assert eurosk.symbol == '€'
    assert not eurosk.symbol_ahead
    assert eurosk.symbol_separator == '\u00A0'
    assert eurosk.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosk.__repr__() == (
        'EuroSK(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurosk.__str__() == '-100,00 €'


def test_eurosk_custom():
    """test_eurosk_custom."""
    amount = 1000
    eurosk = EuroSK(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurosk.amount == decimal
    assert eurosk.numeric_code == '978'
    assert eurosk.alpha_code == 'EUR'
    assert eurosk.decimal_places == 5
    assert eurosk.decimal_sign == '\u202F'
    assert eurosk.grouping_sign == ','
    assert eurosk.international
    assert eurosk.symbol == '€'
    assert not eurosk.symbol_ahead
    assert eurosk.symbol_separator == '_'
    assert eurosk.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosk.__repr__() == (
        'EuroSK(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert eurosk.__str__() == 'EUR 1,000.00000'


def test_eurosk_changed():
    """test_ceurosk_changed."""
    eurosk = EuroSK(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosk.international = True


def test_eurosk_math_add():
    """test_eurosk_math_add."""
    eurosk_one = EuroSK(amount=1)
    eurosk_two = EuroSK(amount=2)
    eurosk_three = EuroSK(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurosk_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroSK\'> '
                   'and <class \'str\'>.')):
        _ = eurosk_one.__add__('1.00')
    assert (
        eurosk_one +
        eurosk_two) == eurosk_three


def test_eurosk_slots():
    """test_eurosk_slots."""
    eurosk = EuroSK(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroSK\' '
                'object has no attribute \'new_variable\'')):
        eurosk.new_variable = 'fail'  # pylint: disable=assigning-non-slot
