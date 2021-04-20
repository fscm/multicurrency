# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bermudian Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BermudianDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bermudian_dollar():
    """test_bermudian_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bermudian_dollar = BermudianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bermudian_dollar.amount == decimal
    assert bermudian_dollar.numeric_code == '060'
    assert bermudian_dollar.alpha_code == 'BMD'
    assert bermudian_dollar.decimal_places == 2
    assert bermudian_dollar.decimal_sign == '.'
    assert bermudian_dollar.grouping_sign == ','
    assert not bermudian_dollar.international
    assert bermudian_dollar.symbol == '$'
    assert bermudian_dollar.symbol_ahead
    assert bermudian_dollar.symbol_separator == ''
    assert bermudian_dollar.convertion == ''
    assert bermudian_dollar.__hash__() == hash((decimal, 'BMD', '060'))
    assert bermudian_dollar.__repr__() == (
        'BermudianDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BMD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "060", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert bermudian_dollar.__str__() == '$0.14'


def test_bermudian_dollar_negative():
    """test_bermudian_dollar_negative."""
    amount = -100
    bermudian_dollar = BermudianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bermudian_dollar.numeric_code == '060'
    assert bermudian_dollar.alpha_code == 'BMD'
    assert bermudian_dollar.decimal_places == 2
    assert bermudian_dollar.decimal_sign == '.'
    assert bermudian_dollar.grouping_sign == ','
    assert not bermudian_dollar.international
    assert bermudian_dollar.symbol == '$'
    assert bermudian_dollar.symbol_ahead
    assert bermudian_dollar.symbol_separator == ''
    assert bermudian_dollar.convertion == ''
    assert bermudian_dollar.__hash__() == hash((decimal, 'BMD', '060'))
    assert bermudian_dollar.__repr__() == (
        'BermudianDollar(amount: -100, '
        'alpha_code: "BMD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "060", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert bermudian_dollar.__str__() == '$-100.00'


def test_bermudian_dollar_custom():
    """test_bermudian_dollar_custom."""
    amount = 1000
    bermudian_dollar = BermudianDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert bermudian_dollar.amount == decimal
    assert bermudian_dollar.numeric_code == '060'
    assert bermudian_dollar.alpha_code == 'BMD'
    assert bermudian_dollar.decimal_places == 5
    assert bermudian_dollar.decimal_sign == ','
    assert bermudian_dollar.grouping_sign == '.'
    assert bermudian_dollar.international
    assert bermudian_dollar.symbol == '$'
    assert not bermudian_dollar.symbol_ahead
    assert bermudian_dollar.symbol_separator == '_'
    assert bermudian_dollar.convertion == ''
    assert bermudian_dollar.__hash__() == hash((decimal, 'BMD', '060'))
    assert bermudian_dollar.__repr__() == (
        'BermudianDollar(amount: 1000, '
        'alpha_code: "BMD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "060", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert bermudian_dollar.__str__() == 'BMD 1,000.00000'


def test_bermudian_dollar_changed():
    """test_cbermudian_dollar_changed."""
    bermudian_dollar = BermudianDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bermudian_dollar.international = True


def test_bermudian_dollar_math_add():
    """test_bermudian_dollar_math_add."""
    bermudian_dollar_one = BermudianDollar(amount=1)
    bermudian_dollar_two = BermudianDollar(amount=2)
    bermudian_dollar_three = BermudianDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BMD and OTHER.'):
        _ = bermudian_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.BermudianDollar\'> '
                   'and <class \'str\'>.')):
        _ = bermudian_dollar_one.__add__('1.00')
    assert (
        bermudian_dollar_one +
        bermudian_dollar_two) == bermudian_dollar_three


def test_bermudian_dollar_slots():
    """test_bermudian_dollar_slots."""
    bermudian_dollar = BermudianDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BermudianDollar\' '
                'object has no attribute \'new_variable\'')):
        bermudian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
