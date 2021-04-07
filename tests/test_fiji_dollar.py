# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Fiji Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, FijiDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_fiji_dollar():
    """test_fiji_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    fiji_dollar = FijiDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert fiji_dollar.amount == decimal
    assert fiji_dollar.code == '242'
    assert fiji_dollar.currency == 'FJD'
    assert fiji_dollar.decimal_places == 2
    assert fiji_dollar.decimal_sign == ','
    assert fiji_dollar.grouping_sign == '.'
    assert not fiji_dollar.international
    assert fiji_dollar.symbol == '$'
    assert fiji_dollar.__hash__() == hash((decimal, 'FJD', '242'))
    assert fiji_dollar.__repr__() == (
        'FijiDollar(amount: 0.1428571428571428571428571429, '
        'currency: "FJD", '
        'symbol: "$", '
        'code: "242", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert fiji_dollar.__str__() == '$0,14'


def test_fiji_dollar_negative():
    """test_fiji_dollar_negative."""
    amount = -100
    fiji_dollar = FijiDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert fiji_dollar.code == '242'
    assert fiji_dollar.currency == 'FJD'
    assert fiji_dollar.decimal_places == 2
    assert fiji_dollar.decimal_sign == ','
    assert fiji_dollar.grouping_sign == '.'
    assert not fiji_dollar.international
    assert fiji_dollar.symbol == '$'
    assert fiji_dollar.__hash__() == hash((decimal, 'FJD', '242'))
    assert fiji_dollar.__repr__() == (
        'FijiDollar(amount: -100, '
        'currency: "FJD", '
        'symbol: "$", '
        'code: "242", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert fiji_dollar.__str__() == '$-100,00'


def test_fiji_dollar_custom():
    """test_fiji_dollar_custom."""
    amount = 1000
    fiji_dollar = FijiDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert fiji_dollar.amount == decimal
    assert fiji_dollar.code == '242'
    assert fiji_dollar.currency == 'FJD'
    assert fiji_dollar.decimal_places == 5
    assert fiji_dollar.decimal_sign == '.'
    assert fiji_dollar.grouping_sign == ','
    assert fiji_dollar.international
    assert fiji_dollar.symbol == '$'
    assert fiji_dollar.__hash__() == hash((decimal, 'FJD', '242'))
    assert fiji_dollar.__repr__() == (
        'FijiDollar(amount: 1000, '
        'currency: "FJD", '
        'symbol: "$", '
        'code: "242", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert fiji_dollar.__str__() == 'FJD 1,000.00000'


def test_fiji_dollar_changed():
    """test_cfiji_dollar_changed."""
    fiji_dollar = FijiDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        fiji_dollar.international = True


def test_fiji_dollar_math_add():
    """test_fiji_dollar_math_add."""
    fiji_dollar_one = FijiDollar(amount=1)
    fiji_dollar_two = FijiDollar(amount=2)
    fiji_dollar_three = FijiDollar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency FJD and OTHER.'):
        _ = fiji_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.FijiDollar\'> '
                   'and <class \'str\'>.')):
        _ = fiji_dollar_one.__add__('1.00')
    assert (fiji_dollar_one + fiji_dollar_two) == fiji_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = FijiDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'FijiDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
