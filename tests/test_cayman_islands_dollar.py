# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Cayman Islands Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CaymanIslandsDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cayman_islands_dollar():
    """test_cayman_islands_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cayman_islands_dollar = CaymanIslandsDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cayman_islands_dollar.amount == decimal
    assert cayman_islands_dollar.numeric_code == '136'
    assert cayman_islands_dollar.alpha_code == 'KYD'
    assert cayman_islands_dollar.decimal_places == 2
    assert cayman_islands_dollar.decimal_sign == '.'
    assert cayman_islands_dollar.grouping_sign == ','
    assert not cayman_islands_dollar.international
    assert cayman_islands_dollar.symbol == '$'
    assert cayman_islands_dollar.symbol_ahead
    assert cayman_islands_dollar.symbol_separator == ''
    assert cayman_islands_dollar.convertion == ''
    assert cayman_islands_dollar.__hash__() == hash((decimal, 'KYD', '136'))
    assert cayman_islands_dollar.__repr__() == (
        'CaymanIslandsDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KYD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "136", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert cayman_islands_dollar.__str__() == '$0.14'


def test_cayman_islands_dollar_negative():
    """test_cayman_islands_dollar_negative."""
    amount = -100
    cayman_islands_dollar = CaymanIslandsDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cayman_islands_dollar.numeric_code == '136'
    assert cayman_islands_dollar.alpha_code == 'KYD'
    assert cayman_islands_dollar.decimal_places == 2
    assert cayman_islands_dollar.decimal_sign == '.'
    assert cayman_islands_dollar.grouping_sign == ','
    assert not cayman_islands_dollar.international
    assert cayman_islands_dollar.symbol == '$'
    assert cayman_islands_dollar.symbol_ahead
    assert cayman_islands_dollar.symbol_separator == ''
    assert cayman_islands_dollar.convertion == ''
    assert cayman_islands_dollar.__hash__() == hash((decimal, 'KYD', '136'))
    assert cayman_islands_dollar.__repr__() == (
        'CaymanIslandsDollar(amount: -100, '
        'alpha_code: "KYD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "136", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert cayman_islands_dollar.__str__() == '$-100.00'


def test_cayman_islands_dollar_custom():
    """test_cayman_islands_dollar_custom."""
    amount = 1000
    cayman_islands_dollar = CaymanIslandsDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert cayman_islands_dollar.amount == decimal
    assert cayman_islands_dollar.numeric_code == '136'
    assert cayman_islands_dollar.alpha_code == 'KYD'
    assert cayman_islands_dollar.decimal_places == 5
    assert cayman_islands_dollar.decimal_sign == ','
    assert cayman_islands_dollar.grouping_sign == '.'
    assert cayman_islands_dollar.international
    assert cayman_islands_dollar.symbol == '$'
    assert not cayman_islands_dollar.symbol_ahead
    assert cayman_islands_dollar.symbol_separator == '_'
    assert cayman_islands_dollar.convertion == ''
    assert cayman_islands_dollar.__hash__() == hash((decimal, 'KYD', '136'))
    assert cayman_islands_dollar.__repr__() == (
        'CaymanIslandsDollar(amount: 1000, '
        'alpha_code: "KYD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "136", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert cayman_islands_dollar.__str__() == 'KYD 1,000.00000'


def test_cayman_islands_dollar_changed():
    """test_ccayman_islands_dollar_changed."""
    cayman_islands_dollar = CaymanIslandsDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cayman_islands_dollar.international = True


def test_cayman_islands_dollar_math_add():
    """test_cayman_islands_dollar_math_add."""
    cayman_islands_dollar_one = CaymanIslandsDollar(amount=1)
    cayman_islands_dollar_two = CaymanIslandsDollar(amount=2)
    cayman_islands_dollar_three = CaymanIslandsDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KYD and OTHER.'):
        _ = cayman_islands_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.CaymanIslandsDollar\'> '
                   'and <class \'str\'>.')):
        _ = cayman_islands_dollar_one.__add__('1.00')
    assert (
        cayman_islands_dollar_one +
        cayman_islands_dollar_two) == cayman_islands_dollar_three


def test_cayman_islands_dollar_slots():
    """test_cayman_islands_dollar_slots."""
    cayman_islands_dollar = CaymanIslandsDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CaymanIslandsDollar\' '
                'object has no attribute \'new_variable\'')):
        cayman_islands_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
