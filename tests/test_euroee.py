# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroEE representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroEE
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroee():
    """test_euroee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroee = EuroEE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroee.amount == decimal
    assert euroee.numeric_code == '978'
    assert euroee.alpha_code == 'EUR'
    assert euroee.decimal_places == 2
    assert euroee.decimal_sign == ','
    assert euroee.grouping_sign == '\u202F'
    assert not euroee.international
    assert euroee.symbol == '€'
    assert not euroee.symbol_ahead
    assert euroee.symbol_separator == '\u00A0'
    assert euroee.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroee.__repr__() == (
        'EuroEE(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert euroee.__str__() == '0,14 €'


def test_euroee_negative():
    """test_euroee_negative."""
    amount = -100
    euroee = EuroEE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroee.numeric_code == '978'
    assert euroee.alpha_code == 'EUR'
    assert euroee.decimal_places == 2
    assert euroee.decimal_sign == ','
    assert euroee.grouping_sign == '\u202F'
    assert not euroee.international
    assert euroee.symbol == '€'
    assert not euroee.symbol_ahead
    assert euroee.symbol_separator == '\u00A0'
    assert euroee.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroee.__repr__() == (
        'EuroEE(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert euroee.__str__() == '-100,00 €'


def test_euroee_custom():
    """test_euroee_custom."""
    amount = 1000
    euroee = EuroEE(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroee.amount == decimal
    assert euroee.numeric_code == '978'
    assert euroee.alpha_code == 'EUR'
    assert euroee.decimal_places == 5
    assert euroee.decimal_sign == '\u202F'
    assert euroee.grouping_sign == ','
    assert euroee.international
    assert euroee.symbol == '€'
    assert not euroee.symbol_ahead
    assert euroee.symbol_separator == '_'
    assert euroee.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroee.__repr__() == (
        'EuroEE(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert euroee.__str__() == 'EUR 1,000.00000'


def test_euroee_changed():
    """test_ceuroee_changed."""
    euroee = EuroEE(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroee.international = True


def test_euroee_math_add():
    """test_euroee_math_add."""
    euroee_one = EuroEE(amount=1)
    euroee_two = EuroEE(amount=2)
    euroee_three = EuroEE(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroEE\'> '
                   'and <class \'str\'>.')):
        _ = euroee_one.__add__('1.00')
    assert (
        euroee_one +
        euroee_two) == euroee_three


def test_euroee_slots():
    """test_euroee_slots."""
    euroee = EuroEE(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroEE\' '
                'object has no attribute \'new_variable\'')):
        euroee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
