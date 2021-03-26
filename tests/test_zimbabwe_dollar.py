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
    assert zimbabwe_dollar.code == '932'
    assert zimbabwe_dollar.currency == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 2
    assert zimbabwe_dollar.decimal_sign == ','
    assert zimbabwe_dollar.grouping_sign == '.'
    assert not zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: 0.1428571428571428571428571429, '
        'currency: "ZWL", '
        'symbol: "$", '
        'code: "932", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert zimbabwe_dollar.__str__() == '$0,14'


def test_zimbabwe_dollar_negative():
    """test_zimbabwe_dollar_negative."""
    amount = -100
    zimbabwe_dollar = ZimbabweDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zimbabwe_dollar.code == '932'
    assert zimbabwe_dollar.currency == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 2
    assert zimbabwe_dollar.decimal_sign == ','
    assert zimbabwe_dollar.grouping_sign == '.'
    assert not zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: -100, '
        'currency: "ZWL", '
        'symbol: "$", '
        'code: "932", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert zimbabwe_dollar.__str__() == '$-100,00'


def test_zimbabwe_dollar_custom():
    """test_zimbabwe_dollar_custom."""
    amount = 1000
    zimbabwe_dollar = ZimbabweDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert zimbabwe_dollar.amount == decimal
    assert zimbabwe_dollar.code == '932'
    assert zimbabwe_dollar.currency == 'ZWL'
    assert zimbabwe_dollar.decimal_places == 5
    assert zimbabwe_dollar.decimal_sign == '.'
    assert zimbabwe_dollar.grouping_sign == ','
    assert zimbabwe_dollar.international
    assert zimbabwe_dollar.symbol == '$'
    assert zimbabwe_dollar.__hash__() == hash((decimal, 'ZWL', '932'))
    assert zimbabwe_dollar.__repr__() == (
        'ZimbabweDollar(amount: 1000, '
        'currency: "ZWL", '
        'symbol: "$", '
        'code: "932", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
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
        zimbabwe_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zimbabwe_dollar.code = '978'
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
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZWL and OTHER.'):
        _ = zimbabwe_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'zimbabwe_dollar.ZimbabweDollar\'> '
                   'and <class \'str\'>.')):
        _ = zimbabwe_dollar_one.__add__('1.00')
    assert (zimbabwe_dollar_one + zimbabwe_dollar_two) == zimbabwe_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ZimbabweDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ZimbabweDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
