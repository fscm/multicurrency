# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroAT representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroAT
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroat():
    """test_euroat."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroat = EuroAT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroat.amount == decimal
    assert euroat.numeric_code == '978'
    assert euroat.alpha_code == 'EUR'
    assert euroat.decimal_places == 2
    assert euroat.decimal_sign == ','
    assert euroat.grouping_places == 3
    assert euroat.grouping_sign == '.'
    assert not euroat.international
    assert euroat.symbol == '€'
    assert euroat.symbol_ahead
    assert euroat.symbol_separator == '\u00A0'
    assert euroat.convertion == ''
    assert euroat.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroat.__repr__() == (
        'EuroAT(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert euroat.__str__() == '€ 0,14'


def test_euroat_negative():
    """test_euroat_negative."""
    amount = -100
    euroat = EuroAT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroat.numeric_code == '978'
    assert euroat.alpha_code == 'EUR'
    assert euroat.decimal_places == 2
    assert euroat.decimal_sign == ','
    assert euroat.grouping_places == 3
    assert euroat.grouping_sign == '.'
    assert not euroat.international
    assert euroat.symbol == '€'
    assert euroat.symbol_ahead
    assert euroat.symbol_separator == '\u00A0'
    assert euroat.convertion == ''
    assert euroat.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroat.__repr__() == (
        'EuroAT(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert euroat.__str__() == '€ -100,00'


def test_euroat_custom():
    """test_euroat_custom."""
    amount = 1000
    euroat = EuroAT(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroat.amount == decimal
    assert euroat.numeric_code == '978'
    assert euroat.alpha_code == 'EUR'
    assert euroat.decimal_places == 5
    assert euroat.decimal_sign == '.'
    assert euroat.grouping_places == 2
    assert euroat.grouping_sign == ','
    assert euroat.international
    assert euroat.symbol == '€'
    assert not euroat.symbol_ahead
    assert euroat.symbol_separator == '_'
    assert euroat.convertion == ''
    assert euroat.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroat.__repr__() == (
        'EuroAT(amount: 1000, '
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
    assert euroat.__str__() == 'EUR 10,00.00000'


def test_euroat_changed():
    """test_ceuroat_changed."""
    euroat = EuroAT(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroat.international = True


def test_euroat_math_add():
    """test_euroat_math_add."""
    euroat_one = EuroAT(amount=1)
    euroat_two = EuroAT(amount=2)
    euroat_three = EuroAT(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroat_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroAT\'> '
                   'and <class \'str\'>.')):
        _ = euroat_one.__add__('1.00')
    assert (
        euroat_one +
        euroat_two) == euroat_three


def test_euroat_slots():
    """test_euroat_slots."""
    euroat = EuroAT(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroAT\' '
                'object has no attribute \'new_variable\'')):
        euroat.new_variable = 'fail'  # pylint: disable=assigning-non-slot
