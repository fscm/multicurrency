# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Hong Kong Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, HongKongDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_hong_kong_dollar():
    """test_hong_kong_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    hong_kong_dollar = HongKongDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert hong_kong_dollar.amount == decimal
    assert hong_kong_dollar.code == '344'
    assert hong_kong_dollar.currency == 'HKD'
    assert hong_kong_dollar.decimal_places == 2
    assert hong_kong_dollar.decimal_sign == '.'
    assert hong_kong_dollar.grouping_sign == ','
    assert not hong_kong_dollar.international
    assert hong_kong_dollar.symbol == '$'
    assert hong_kong_dollar.__hash__() == hash((decimal, 'HKD', '344'))
    assert hong_kong_dollar.__repr__() == (
        'HongKongDollar(amount: 0.1428571428571428571428571429, '
        'currency: "HKD", '
        'symbol: "$", '
        'code: "344", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert hong_kong_dollar.__str__() == '$0.14'


def test_hong_kong_dollar_negative():
    """test_hong_kong_dollar_negative."""
    amount = -100
    hong_kong_dollar = HongKongDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert hong_kong_dollar.code == '344'
    assert hong_kong_dollar.currency == 'HKD'
    assert hong_kong_dollar.decimal_places == 2
    assert hong_kong_dollar.decimal_sign == '.'
    assert hong_kong_dollar.grouping_sign == ','
    assert not hong_kong_dollar.international
    assert hong_kong_dollar.symbol == '$'
    assert hong_kong_dollar.__hash__() == hash((decimal, 'HKD', '344'))
    assert hong_kong_dollar.__repr__() == (
        'HongKongDollar(amount: -100, '
        'currency: "HKD", '
        'symbol: "$", '
        'code: "344", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert hong_kong_dollar.__str__() == '$-100.00'


def test_hong_kong_dollar_custom():
    """test_hong_kong_dollar_custom."""
    amount = 1000
    hong_kong_dollar = HongKongDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert hong_kong_dollar.amount == decimal
    assert hong_kong_dollar.code == '344'
    assert hong_kong_dollar.currency == 'HKD'
    assert hong_kong_dollar.decimal_places == 5
    assert hong_kong_dollar.decimal_sign == ','
    assert hong_kong_dollar.grouping_sign == '.'
    assert hong_kong_dollar.international
    assert hong_kong_dollar.symbol == '$'
    assert hong_kong_dollar.__hash__() == hash((decimal, 'HKD', '344'))
    assert hong_kong_dollar.__repr__() == (
        'HongKongDollar(amount: 1000, '
        'currency: "HKD", '
        'symbol: "$", '
        'code: "344", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert hong_kong_dollar.__str__() == 'HKD 1.000,00000'


def test_hong_kong_dollar_changed():
    """test_chong_kong_dollar_changed."""
    hong_kong_dollar = HongKongDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hong_kong_dollar.international = True


def test_hong_kong_dollar_math_add():
    """test_hong_kong_dollar_math_add."""
    hong_kong_dollar_one = HongKongDollar(amount=1)
    hong_kong_dollar_two = HongKongDollar(amount=2)
    hong_kong_dollar_three = HongKongDollar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency HKD and OTHER.'):
        _ = hong_kong_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.HongKongDollar\'> '
                   'and <class \'str\'>.')):
        _ = hong_kong_dollar_one.__add__('1.00')
    assert (
        hong_kong_dollar_one +
        hong_kong_dollar_two) == hong_kong_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = HongKongDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'HongKongDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot