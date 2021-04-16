# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Zimbabwe Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ZimbabweDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_zimbabwe_dollar():
    """test_zimbabwe_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    zimbabwe_dollar = ZimbabweDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zimbabwe_dollar.amount == decimal
    assert zimbabwe_dollar.numeric_code == '932'
    assert zimbabwe_dollar.alpha_code == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 2
    assert zimbabwe_dollar.decimal_sign == '.'
    assert zimbabwe_dollar.grouping_sign == ','
    assert not zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert zimbabwe_dollar.symbol_ahead
    assert zimbabwe_dollar.symbol_separator == '\u00A0'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ZWL", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "932", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert zimbabwe_dollar.__str__() == '$ 0.14'


def test_zimbabwe_dollar_negative():
    """test_zimbabwe_dollar_negative."""
    amount = -100
    zimbabwe_dollar = ZimbabweDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zimbabwe_dollar.numeric_code == '932'
    assert zimbabwe_dollar.alpha_code == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 2
    assert zimbabwe_dollar.decimal_sign == '.'
    assert zimbabwe_dollar.grouping_sign == ','
    assert not zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert zimbabwe_dollar.symbol_ahead
    assert zimbabwe_dollar.symbol_separator == '\u00A0'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: -100, '
        'alpha_code: "ZWL", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "932", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert zimbabwe_dollar.__str__() == '$ -100.00'


def test_zimbabwe_dollar_custom():
    """test_zimbabwe_dollar_custom."""
    amount = 1000
    zimbabwe_dollar = ZimbabweDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert zimbabwe_dollar.amount == decimal
    assert zimbabwe_dollar.numeric_code == '932'
    assert zimbabwe_dollar.alpha_code == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 5
    assert zimbabwe_dollar.decimal_sign == ','
    assert zimbabwe_dollar.grouping_sign == '.'
    assert zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert not zimbabwe_dollar.symbol_ahead
    assert zimbabwe_dollar.symbol_separator == '_'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: 1000, '
        'alpha_code: "ZWL", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "932", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert zimbabwe_dollar.__str__() == 'ZWL 1,000.00000'


def test_zimbabwe_dollar_changed():
    """test_czimbabwe_dollar_changed."""
    zimbabwe_dollar = ZimbabweDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.international = True


def test_zimbabwe_dollar_math_add():
    """test_zimbabwe_dollar_math_add."""
    zimbabwe_dollar_one = ZimbabweDollar(amount=1)
    zimbabwe_dollar_two = ZimbabweDollar(amount=2)
    zimbabwe_dollar_three = ZimbabweDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZWL and OTHER.'):
        _ = zimbabwe_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.ZimbabweDollar\'> '
                   'and <class \'str\'>.')):
        _ = zimbabwe_dollar_one.__add__('1.00')
    assert (
        zimbabwe_dollar_one +
        zimbabwe_dollar_two) == zimbabwe_dollar_three


def test_zimbabwe_dollar_slots():
    """test_zimbabwe_dollar_slots."""
    zimbabwe_dollar = ZimbabweDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ZimbabweDollar\' '
                'object has no attribute \'new_variable\'')):
        zimbabwe_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
