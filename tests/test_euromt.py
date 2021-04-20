# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroMT representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroMT
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euromt():
    """test_euromt."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euromt = EuroMT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euromt.amount == decimal
    assert euromt.numeric_code == '978'
    assert euromt.alpha_code == 'EUR'
    assert euromt.decimal_places == 2
    assert euromt.decimal_sign == '.'
    assert euromt.grouping_sign == ','
    assert not euromt.international
    assert euromt.symbol == '€'
    assert euromt.symbol_ahead
    assert euromt.symbol_separator == ''
    assert euromt.convertion == ''
    assert euromt.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromt.__repr__() == (
        'EuroMT(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert euromt.__str__() == '€0.14'


def test_euromt_negative():
    """test_euromt_negative."""
    amount = -100
    euromt = EuroMT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euromt.numeric_code == '978'
    assert euromt.alpha_code == 'EUR'
    assert euromt.decimal_places == 2
    assert euromt.decimal_sign == '.'
    assert euromt.grouping_sign == ','
    assert not euromt.international
    assert euromt.symbol == '€'
    assert euromt.symbol_ahead
    assert euromt.symbol_separator == ''
    assert euromt.convertion == ''
    assert euromt.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromt.__repr__() == (
        'EuroMT(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert euromt.__str__() == '€-100.00'


def test_euromt_custom():
    """test_euromt_custom."""
    amount = 1000
    euromt = EuroMT(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euromt.amount == decimal
    assert euromt.numeric_code == '978'
    assert euromt.alpha_code == 'EUR'
    assert euromt.decimal_places == 5
    assert euromt.decimal_sign == ','
    assert euromt.grouping_sign == '.'
    assert euromt.international
    assert euromt.symbol == '€'
    assert not euromt.symbol_ahead
    assert euromt.symbol_separator == '_'
    assert euromt.convertion == ''
    assert euromt.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromt.__repr__() == (
        'EuroMT(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert euromt.__str__() == 'EUR 1,000.00000'


def test_euromt_changed():
    """test_ceuromt_changed."""
    euromt = EuroMT(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromt.international = True


def test_euromt_math_add():
    """test_euromt_math_add."""
    euromt_one = EuroMT(amount=1)
    euromt_two = EuroMT(amount=2)
    euromt_three = EuroMT(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euromt_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroMT\'> '
                   'and <class \'str\'>.')):
        _ = euromt_one.__add__('1.00')
    assert (
        euromt_one +
        euromt_two) == euromt_three


def test_euromt_slots():
    """test_euromt_slots."""
    euromt = EuroMT(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroMT\' '
                'object has no attribute \'new_variable\'')):
        euromt.new_variable = 'fail'  # pylint: disable=assigning-non-slot
