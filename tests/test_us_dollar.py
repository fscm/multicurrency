# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the US Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, USDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_us_dollar():
    """test_us_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    us_dollar = USDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert us_dollar.amount == decimal
    assert us_dollar.numeric_code == '840'
    assert us_dollar.alpha_code == 'USD'
    assert us_dollar.decimal_places == 2
    assert us_dollar.decimal_sign == '.'
    assert us_dollar.grouping_sign == ','
    assert not us_dollar.international
    assert us_dollar.symbol == '$'
    assert us_dollar.symbol_ahead
    assert us_dollar.symbol_separator == ''
    assert us_dollar.__hash__() == hash((decimal, 'USD', '840'))
    assert us_dollar.__repr__() == (
        'USDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "USD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "840", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert us_dollar.__str__() == '$0.14'


def test_us_dollar_negative():
    """test_us_dollar_negative."""
    amount = -100
    us_dollar = USDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert us_dollar.numeric_code == '840'
    assert us_dollar.alpha_code == 'USD'
    assert us_dollar.decimal_places == 2
    assert us_dollar.decimal_sign == '.'
    assert us_dollar.grouping_sign == ','
    assert not us_dollar.international
    assert us_dollar.symbol == '$'
    assert us_dollar.symbol_ahead
    assert us_dollar.symbol_separator == ''
    assert us_dollar.__hash__() == hash((decimal, 'USD', '840'))
    assert us_dollar.__repr__() == (
        'USDollar(amount: -100, '
        'alpha_code: "USD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "840", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert us_dollar.__str__() == '$-100.00'


def test_us_dollar_custom():
    """test_us_dollar_custom."""
    amount = 1000
    us_dollar = USDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert us_dollar.amount == decimal
    assert us_dollar.numeric_code == '840'
    assert us_dollar.alpha_code == 'USD'
    assert us_dollar.decimal_places == 5
    assert us_dollar.decimal_sign == ','
    assert us_dollar.grouping_sign == '.'
    assert us_dollar.international
    assert us_dollar.symbol == '$'
    assert not us_dollar.symbol_ahead
    assert us_dollar.symbol_separator == '_'
    assert us_dollar.__hash__() == hash((decimal, 'USD', '840'))
    assert us_dollar.__repr__() == (
        'USDollar(amount: 1000, '
        'alpha_code: "USD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "840", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert us_dollar.__str__() == 'USD 1,000.00000'


def test_us_dollar_changed():
    """test_cus_dollar_changed."""
    us_dollar = USDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        us_dollar.international = True


def test_us_dollar_math_add():
    """test_us_dollar_math_add."""
    us_dollar_one = USDollar(amount=1)
    us_dollar_two = USDollar(amount=2)
    us_dollar_three = USDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency USD and OTHER.'):
        _ = us_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.USDollar\'> '
                   'and <class \'str\'>.')):
        _ = us_dollar_one.__add__('1.00')
    assert (
        us_dollar_one +
        us_dollar_two) == us_dollar_three


def test_us_dollar_slots():
    """test_us_dollar_slots."""
    us_dollar = USDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'USDollar\' '
                'object has no attribute \'new_variable\'')):
        us_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
