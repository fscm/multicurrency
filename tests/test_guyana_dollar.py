# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Guyana Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, GuyanaDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_guyana_dollar():
    """test_guyana_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    guyana_dollar = GuyanaDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guyana_dollar.amount == decimal
    assert guyana_dollar.numeric_code == '328'
    assert guyana_dollar.alpha_code == 'GYD'
    assert guyana_dollar.decimal_places == 2
    assert guyana_dollar.decimal_sign == '.'
    assert guyana_dollar.grouping_sign == ','
    assert not guyana_dollar.international
    assert guyana_dollar.symbol == '$'
    assert guyana_dollar.symbol_ahead
    assert guyana_dollar.symbol_separator == ''
    assert guyana_dollar.__hash__() == hash((decimal, 'GYD', '328'))
    assert guyana_dollar.__repr__() == (
        'GuyanaDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GYD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "328", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert guyana_dollar.__str__() == '$0.14'


def test_guyana_dollar_negative():
    """test_guyana_dollar_negative."""
    amount = -100
    guyana_dollar = GuyanaDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guyana_dollar.numeric_code == '328'
    assert guyana_dollar.alpha_code == 'GYD'
    assert guyana_dollar.decimal_places == 2
    assert guyana_dollar.decimal_sign == '.'
    assert guyana_dollar.grouping_sign == ','
    assert not guyana_dollar.international
    assert guyana_dollar.symbol == '$'
    assert guyana_dollar.symbol_ahead
    assert guyana_dollar.symbol_separator == ''
    assert guyana_dollar.__hash__() == hash((decimal, 'GYD', '328'))
    assert guyana_dollar.__repr__() == (
        'GuyanaDollar(amount: -100, '
        'alpha_code: "GYD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "328", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert guyana_dollar.__str__() == '$-100.00'


def test_guyana_dollar_custom():
    """test_guyana_dollar_custom."""
    amount = 1000
    guyana_dollar = GuyanaDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert guyana_dollar.amount == decimal
    assert guyana_dollar.numeric_code == '328'
    assert guyana_dollar.alpha_code == 'GYD'
    assert guyana_dollar.decimal_places == 5
    assert guyana_dollar.decimal_sign == ','
    assert guyana_dollar.grouping_sign == '.'
    assert guyana_dollar.international
    assert guyana_dollar.symbol == '$'
    assert not guyana_dollar.symbol_ahead
    assert guyana_dollar.symbol_separator == '_'
    assert guyana_dollar.__hash__() == hash((decimal, 'GYD', '328'))
    assert guyana_dollar.__repr__() == (
        'GuyanaDollar(amount: 1000, '
        'alpha_code: "GYD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "328", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert guyana_dollar.__str__() == 'GYD 1,000.00000'


def test_guyana_dollar_changed():
    """test_cguyana_dollar_changed."""
    guyana_dollar = GuyanaDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guyana_dollar.international = True


def test_guyana_dollar_math_add():
    """test_guyana_dollar_math_add."""
    guyana_dollar_one = GuyanaDollar(amount=1)
    guyana_dollar_two = GuyanaDollar(amount=2)
    guyana_dollar_three = GuyanaDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GYD and OTHER.'):
        _ = guyana_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.GuyanaDollar\'> '
                   'and <class \'str\'>.')):
        _ = guyana_dollar_one.__add__('1.00')
    assert (
        guyana_dollar_one +
        guyana_dollar_two) == guyana_dollar_three


def test_guyana_dollar_slots():
    """test_guyana_dollar_slots."""
    guyana_dollar = GuyanaDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'GuyanaDollar\' '
                'object has no attribute \'new_variable\'')):
        guyana_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
