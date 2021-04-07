# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Brunei Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BruneiDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_brunei_dollar():
    """test_brunei_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    brunei_dollar = BruneiDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert brunei_dollar.amount == decimal
    assert brunei_dollar.code == '096'
    assert brunei_dollar.currency == 'BND'
    assert brunei_dollar.decimal_places == 2
    assert brunei_dollar.decimal_sign == '.'
    assert brunei_dollar.grouping_sign == ','
    assert not brunei_dollar.international
    assert brunei_dollar.symbol == '$'
    assert brunei_dollar.__hash__() == hash((decimal, 'BND', '096'))
    assert brunei_dollar.__repr__() == (
        'BruneiDollar(amount: 0.1428571428571428571428571429, '
        'currency: "BND", '
        'symbol: "$", '
        'code: "096", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert brunei_dollar.__str__() == '$0.14'


def test_brunei_dollar_negative():
    """test_brunei_dollar_negative."""
    amount = -100
    brunei_dollar = BruneiDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert brunei_dollar.code == '096'
    assert brunei_dollar.currency == 'BND'
    assert brunei_dollar.decimal_places == 2
    assert brunei_dollar.decimal_sign == '.'
    assert brunei_dollar.grouping_sign == ','
    assert not brunei_dollar.international
    assert brunei_dollar.symbol == '$'
    assert brunei_dollar.__hash__() == hash((decimal, 'BND', '096'))
    assert brunei_dollar.__repr__() == (
        'BruneiDollar(amount: -100, '
        'currency: "BND", '
        'symbol: "$", '
        'code: "096", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert brunei_dollar.__str__() == '$-100.00'


def test_brunei_dollar_custom():
    """test_brunei_dollar_custom."""
    amount = 1000
    brunei_dollar = BruneiDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert brunei_dollar.amount == decimal
    assert brunei_dollar.code == '096'
    assert brunei_dollar.currency == 'BND'
    assert brunei_dollar.decimal_places == 5
    assert brunei_dollar.decimal_sign == ','
    assert brunei_dollar.grouping_sign == '.'
    assert brunei_dollar.international
    assert brunei_dollar.symbol == '$'
    assert brunei_dollar.__hash__() == hash((decimal, 'BND', '096'))
    assert brunei_dollar.__repr__() == (
        'BruneiDollar(amount: 1000, '
        'currency: "BND", '
        'symbol: "$", '
        'code: "096", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert brunei_dollar.__str__() == 'BND 1.000,00000'


def test_brunei_dollar_changed():
    """test_cbrunei_dollar_changed."""
    brunei_dollar = BruneiDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brunei_dollar.international = True


def test_brunei_dollar_math_add():
    """test_brunei_dollar_math_add."""
    brunei_dollar_one = BruneiDollar(amount=1)
    brunei_dollar_two = BruneiDollar(amount=2)
    brunei_dollar_three = BruneiDollar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BND and OTHER.'):
        _ = brunei_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.BruneiDollar\'> '
                   'and <class \'str\'>.')):
        _ = brunei_dollar_one.__add__('1.00')
    assert (brunei_dollar_one + brunei_dollar_two) == brunei_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BruneiDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BruneiDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
