# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yuan representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Yuan
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_yuan():
    """test_yuan."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    yuan = Yuan(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert yuan.amount == decimal
    assert yuan.numeric_code == '156'
    assert yuan.alpha_code == 'CNY'
    assert yuan.decimal_places == 2
    assert yuan.decimal_sign == '.'
    assert yuan.grouping_sign == ','
    assert not yuan.international
    assert yuan.symbol == '¥'
    assert yuan.__hash__() == hash((decimal, 'CNY', '156'))
    assert yuan.__repr__() == (
        'Yuan(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CNY", '
        'symbol: "¥", '
        'numeric_code: "156", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert yuan.__str__() == '¥0.14'


def test_yuan_negative():
    """test_yuan_negative."""
    amount = -100
    yuan = Yuan(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert yuan.numeric_code == '156'
    assert yuan.alpha_code == 'CNY'
    assert yuan.decimal_places == 2
    assert yuan.decimal_sign == '.'
    assert yuan.grouping_sign == ','
    assert not yuan.international
    assert yuan.symbol == '¥'
    assert yuan.__hash__() == hash((decimal, 'CNY', '156'))
    assert yuan.__repr__() == (
        'Yuan(amount: -100, '
        'alpha_code: "CNY", '
        'symbol: "¥", '
        'numeric_code: "156", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert yuan.__str__() == '¥-100.00'


def test_yuan_custom():
    """test_yuan_custom."""
    amount = 1000
    yuan = Yuan(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert yuan.amount == decimal
    assert yuan.numeric_code == '156'
    assert yuan.alpha_code == 'CNY'
    assert yuan.decimal_places == 5
    assert yuan.decimal_sign == ','
    assert yuan.grouping_sign == '.'
    assert yuan.international
    assert yuan.symbol == '¥'
    assert yuan.__hash__() == hash((decimal, 'CNY', '156'))
    assert yuan.__repr__() == (
        'Yuan(amount: 1000, '
        'alpha_code: "CNY", '
        'symbol: "¥", '
        'numeric_code: "156", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert yuan.__str__() == 'CNY 1.000,00000'


def test_yuan_changed():
    """test_cyuan_changed."""
    yuan = Yuan(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yuan.international = True


def test_yuan_math_add():
    """test_yuan_math_add."""
    yuan_one = Yuan(amount=1)
    yuan_two = Yuan(amount=2)
    yuan_three = Yuan(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CNY and OTHER.'):
        _ = yuan_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'yuan.Yuan\'> '
                   'and <class \'str\'>.')):
        _ = yuan_one.__add__('1.00')
    assert (yuan_one + yuan_two) == yuan_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Yuan(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Yuan\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
