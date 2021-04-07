# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Singapore Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SingaporeDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_singapore_dollar():
    """test_singapore_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    singapore_dollar = SingaporeDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert singapore_dollar.amount == decimal
    assert singapore_dollar.code == '702'
    assert singapore_dollar.currency == 'SGD'
    assert singapore_dollar.decimal_places == 2
    assert singapore_dollar.decimal_sign == '.'
    assert singapore_dollar.grouping_sign == ','
    assert not singapore_dollar.international
    assert singapore_dollar.symbol == '$'
    assert singapore_dollar.__hash__() == hash((decimal, 'SGD', '702'))
    assert singapore_dollar.__repr__() == (
        'SingaporeDollar(amount: 0.1428571428571428571428571429, '
        'currency: "SGD", '
        'symbol: "$", '
        'code: "702", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert singapore_dollar.__str__() == '$0.14'


def test_singapore_dollar_negative():
    """test_singapore_dollar_negative."""
    amount = -100
    singapore_dollar = SingaporeDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert singapore_dollar.code == '702'
    assert singapore_dollar.currency == 'SGD'
    assert singapore_dollar.decimal_places == 2
    assert singapore_dollar.decimal_sign == '.'
    assert singapore_dollar.grouping_sign == ','
    assert not singapore_dollar.international
    assert singapore_dollar.symbol == '$'
    assert singapore_dollar.__hash__() == hash((decimal, 'SGD', '702'))
    assert singapore_dollar.__repr__() == (
        'SingaporeDollar(amount: -100, '
        'currency: "SGD", '
        'symbol: "$", '
        'code: "702", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert singapore_dollar.__str__() == '$-100.00'


def test_singapore_dollar_custom():
    """test_singapore_dollar_custom."""
    amount = 1000
    singapore_dollar = SingaporeDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert singapore_dollar.amount == decimal
    assert singapore_dollar.code == '702'
    assert singapore_dollar.currency == 'SGD'
    assert singapore_dollar.decimal_places == 5
    assert singapore_dollar.decimal_sign == ','
    assert singapore_dollar.grouping_sign == '.'
    assert singapore_dollar.international
    assert singapore_dollar.symbol == '$'
    assert singapore_dollar.__hash__() == hash((decimal, 'SGD', '702'))
    assert singapore_dollar.__repr__() == (
        'SingaporeDollar(amount: 1000, '
        'currency: "SGD", '
        'symbol: "$", '
        'code: "702", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert singapore_dollar.__str__() == 'SGD 1.000,00000'


def test_singapore_dollar_changed():
    """test_csingapore_dollar_changed."""
    singapore_dollar = SingaporeDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        singapore_dollar.international = True


def test_singapore_dollar_math_add():
    """test_singapore_dollar_math_add."""
    singapore_dollar_one = SingaporeDollar(amount=1)
    singapore_dollar_two = SingaporeDollar(amount=2)
    singapore_dollar_three = SingaporeDollar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SGD and OTHER.'):
        _ = singapore_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.SingaporeDollar\'> '
                   'and <class \'str\'>.')):
        _ = singapore_dollar_one.__add__('1.00')
    assert (
        singapore_dollar_one +
        singapore_dollar_two) == singapore_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SingaporeDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SingaporeDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
