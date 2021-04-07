# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Belize Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BelizeDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_belize_dollar():
    """test_belize_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    belize_dollar = BelizeDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert belize_dollar.amount == decimal
    assert belize_dollar.code == '084'
    assert belize_dollar.currency == 'BZD'
    assert belize_dollar.decimal_places == 2
    assert belize_dollar.decimal_sign == '.'
    assert belize_dollar.grouping_sign == ','
    assert not belize_dollar.international
    assert belize_dollar.symbol == '$'
    assert belize_dollar.__hash__() == hash((decimal, 'BZD', '084'))
    assert belize_dollar.__repr__() == (
        'BelizeDollar(amount: 0.1428571428571428571428571429, '
        'currency: "BZD", '
        'symbol: "$", '
        'code: "084", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert belize_dollar.__str__() == '$0.14'


def test_belize_dollar_negative():
    """test_belize_dollar_negative."""
    amount = -100
    belize_dollar = BelizeDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert belize_dollar.code == '084'
    assert belize_dollar.currency == 'BZD'
    assert belize_dollar.decimal_places == 2
    assert belize_dollar.decimal_sign == '.'
    assert belize_dollar.grouping_sign == ','
    assert not belize_dollar.international
    assert belize_dollar.symbol == '$'
    assert belize_dollar.__hash__() == hash((decimal, 'BZD', '084'))
    assert belize_dollar.__repr__() == (
        'BelizeDollar(amount: -100, '
        'currency: "BZD", '
        'symbol: "$", '
        'code: "084", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert belize_dollar.__str__() == '$-100.00'


def test_belize_dollar_custom():
    """test_belize_dollar_custom."""
    amount = 1000
    belize_dollar = BelizeDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert belize_dollar.amount == decimal
    assert belize_dollar.code == '084'
    assert belize_dollar.currency == 'BZD'
    assert belize_dollar.decimal_places == 5
    assert belize_dollar.decimal_sign == ','
    assert belize_dollar.grouping_sign == '.'
    assert belize_dollar.international
    assert belize_dollar.symbol == '$'
    assert belize_dollar.__hash__() == hash((decimal, 'BZD', '084'))
    assert belize_dollar.__repr__() == (
        'BelizeDollar(amount: 1000, '
        'currency: "BZD", '
        'symbol: "$", '
        'code: "084", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert belize_dollar.__str__() == 'BZD 1.000,00000'


def test_belize_dollar_changed():
    """test_cbelize_dollar_changed."""
    belize_dollar = BelizeDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belize_dollar.international = True


def test_belize_dollar_math_add():
    """test_belize_dollar_math_add."""
    belize_dollar_one = BelizeDollar(amount=1)
    belize_dollar_two = BelizeDollar(amount=2)
    belize_dollar_three = BelizeDollar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BZD and OTHER.'):
        _ = belize_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.BelizeDollar\'> '
                   'and <class \'str\'>.')):
        _ = belize_dollar_one.__add__('1.00')
    assert (belize_dollar_one + belize_dollar_two) == belize_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BelizeDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BelizeDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
