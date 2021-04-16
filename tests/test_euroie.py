# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroIE representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroIE
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroie():
    """test_euroie."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroie = EuroIE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroie.amount == decimal
    assert euroie.numeric_code == '978'
    assert euroie.alpha_code == 'EUR'
    assert euroie.decimal_places == 2
    assert euroie.decimal_sign == '.'
    assert euroie.grouping_sign == ','
    assert not euroie.international
    assert euroie.symbol == '€'
    assert euroie.symbol_ahead
    assert euroie.symbol_separator == ''
    assert euroie.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroie.__repr__() == (
        'EuroIE(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert euroie.__str__() == '€0.14'


def test_euroie_negative():
    """test_euroie_negative."""
    amount = -100
    euroie = EuroIE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroie.numeric_code == '978'
    assert euroie.alpha_code == 'EUR'
    assert euroie.decimal_places == 2
    assert euroie.decimal_sign == '.'
    assert euroie.grouping_sign == ','
    assert not euroie.international
    assert euroie.symbol == '€'
    assert euroie.symbol_ahead
    assert euroie.symbol_separator == ''
    assert euroie.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroie.__repr__() == (
        'EuroIE(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert euroie.__str__() == '€-100.00'


def test_euroie_custom():
    """test_euroie_custom."""
    amount = 1000
    euroie = EuroIE(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroie.amount == decimal
    assert euroie.numeric_code == '978'
    assert euroie.alpha_code == 'EUR'
    assert euroie.decimal_places == 5
    assert euroie.decimal_sign == ','
    assert euroie.grouping_sign == '.'
    assert euroie.international
    assert euroie.symbol == '€'
    assert not euroie.symbol_ahead
    assert euroie.symbol_separator == '_'
    assert euroie.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroie.__repr__() == (
        'EuroIE(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert euroie.__str__() == 'EUR 1,000.00000'


def test_euroie_changed():
    """test_ceuroie_changed."""
    euroie = EuroIE(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroie.international = True


def test_euroie_math_add():
    """test_euroie_math_add."""
    euroie_one = EuroIE(amount=1)
    euroie_two = EuroIE(amount=2)
    euroie_three = EuroIE(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroie_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroIE\'> '
                   'and <class \'str\'>.')):
        _ = euroie_one.__add__('1.00')
    assert (
        euroie_one +
        euroie_two) == euroie_three


def test_euroie_slots():
    """test_euroie_slots."""
    euroie = EuroIE(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroIE\' '
                'object has no attribute \'new_variable\'')):
        euroie.new_variable = 'fail'  # pylint: disable=assigning-non-slot
