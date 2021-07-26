# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroCY representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroCY
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurocy():
    """test_eurocy."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurocy = EuroCY(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurocy.amount == decimal
    assert eurocy.numeric_code == '978'
    assert eurocy.alpha_code == 'EUR'
    assert eurocy.decimal_places == 2
    assert eurocy.decimal_sign == ','
    assert eurocy.grouping_places == 3
    assert eurocy.grouping_sign == '.'
    assert not eurocy.international
    assert eurocy.symbol == '€'
    assert not eurocy.symbol_ahead
    assert eurocy.symbol_separator == '\u00A0'
    assert eurocy.convertion == ''
    assert eurocy.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurocy.__repr__() == (
        'EuroCY(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurocy.__str__() == '0,14 €'


def test_eurocy_negative():
    """test_eurocy_negative."""
    amount = -100
    eurocy = EuroCY(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurocy.numeric_code == '978'
    assert eurocy.alpha_code == 'EUR'
    assert eurocy.decimal_places == 2
    assert eurocy.decimal_sign == ','
    assert eurocy.grouping_places == 3
    assert eurocy.grouping_sign == '.'
    assert not eurocy.international
    assert eurocy.symbol == '€'
    assert not eurocy.symbol_ahead
    assert eurocy.symbol_separator == '\u00A0'
    assert eurocy.convertion == ''
    assert eurocy.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurocy.__repr__() == (
        'EuroCY(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurocy.__str__() == '-100,00 €'


def test_eurocy_custom():
    """test_eurocy_custom."""
    amount = 1000
    eurocy = EuroCY(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurocy.amount == decimal
    assert eurocy.numeric_code == '978'
    assert eurocy.alpha_code == 'EUR'
    assert eurocy.decimal_places == 5
    assert eurocy.decimal_sign == '.'
    assert eurocy.grouping_places == 2
    assert eurocy.grouping_sign == ','
    assert eurocy.international
    assert eurocy.symbol == '€'
    assert not eurocy.symbol_ahead
    assert eurocy.symbol_separator == '_'
    assert eurocy.convertion == ''
    assert eurocy.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurocy.__repr__() == (
        'EuroCY(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurocy.__str__() == 'EUR 10,00.00000'


def test_eurocy_changed():
    """test_ceurocy_changed."""
    eurocy = EuroCY(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurocy.international = True


def test_eurocy_math_add():
    """test_eurocy_math_add."""
    eurocy_one = EuroCY(amount=1)
    eurocy_two = EuroCY(amount=2)
    eurocy_three = EuroCY(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurocy_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroCY\'> '
                   'and <class \'str\'>.')):
        _ = eurocy_one.__add__('1.00')
    assert (
        eurocy_one +
        eurocy_two) == eurocy_three


def test_eurocy_slots():
    """test_eurocy_slots."""
    eurocy = EuroCY(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroCY\' '
                'object has no attribute \'new_variable\'')):
        eurocy.new_variable = 'fail'  # pylint: disable=assigning-non-slot
