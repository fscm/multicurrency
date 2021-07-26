# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Taiwan Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, TaiwanDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_taiwan_dollar():
    """test_taiwan_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    taiwan_dollar = TaiwanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert taiwan_dollar.amount == decimal
    assert taiwan_dollar.numeric_code == '901'
    assert taiwan_dollar.alpha_code == 'TWD'
    assert taiwan_dollar.decimal_places == 2
    assert taiwan_dollar.decimal_sign == '.'
    assert taiwan_dollar.grouping_places == 3
    assert taiwan_dollar.grouping_sign == ','
    assert not taiwan_dollar.international
    assert taiwan_dollar.symbol == '$'
    assert taiwan_dollar.symbol_ahead
    assert taiwan_dollar.symbol_separator == ''
    assert taiwan_dollar.convertion == ''
    assert taiwan_dollar.__hash__() == hash((decimal, 'TWD', '901'))
    assert taiwan_dollar.__repr__() == (
        'TaiwanDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TWD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "901", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert taiwan_dollar.__str__() == '$0.14'


def test_taiwan_dollar_negative():
    """test_taiwan_dollar_negative."""
    amount = -100
    taiwan_dollar = TaiwanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert taiwan_dollar.numeric_code == '901'
    assert taiwan_dollar.alpha_code == 'TWD'
    assert taiwan_dollar.decimal_places == 2
    assert taiwan_dollar.decimal_sign == '.'
    assert taiwan_dollar.grouping_places == 3
    assert taiwan_dollar.grouping_sign == ','
    assert not taiwan_dollar.international
    assert taiwan_dollar.symbol == '$'
    assert taiwan_dollar.symbol_ahead
    assert taiwan_dollar.symbol_separator == ''
    assert taiwan_dollar.convertion == ''
    assert taiwan_dollar.__hash__() == hash((decimal, 'TWD', '901'))
    assert taiwan_dollar.__repr__() == (
        'TaiwanDollar(amount: -100, '
        'alpha_code: "TWD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "901", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert taiwan_dollar.__str__() == '$-100.00'


def test_taiwan_dollar_custom():
    """test_taiwan_dollar_custom."""
    amount = 1000
    taiwan_dollar = TaiwanDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert taiwan_dollar.amount == decimal
    assert taiwan_dollar.numeric_code == '901'
    assert taiwan_dollar.alpha_code == 'TWD'
    assert taiwan_dollar.decimal_places == 5
    assert taiwan_dollar.decimal_sign == ','
    assert taiwan_dollar.grouping_places == 2
    assert taiwan_dollar.grouping_sign == '.'
    assert taiwan_dollar.international
    assert taiwan_dollar.symbol == '$'
    assert not taiwan_dollar.symbol_ahead
    assert taiwan_dollar.symbol_separator == '_'
    assert taiwan_dollar.convertion == ''
    assert taiwan_dollar.__hash__() == hash((decimal, 'TWD', '901'))
    assert taiwan_dollar.__repr__() == (
        'TaiwanDollar(amount: 1000, '
        'alpha_code: "TWD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "901", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert taiwan_dollar.__str__() == 'TWD 10,00.00000'


def test_taiwan_dollar_changed():
    """test_ctaiwan_dollar_changed."""
    taiwan_dollar = TaiwanDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taiwan_dollar.international = True


def test_taiwan_dollar_math_add():
    """test_taiwan_dollar_math_add."""
    taiwan_dollar_one = TaiwanDollar(amount=1)
    taiwan_dollar_two = TaiwanDollar(amount=2)
    taiwan_dollar_three = TaiwanDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TWD and OTHER.'):
        _ = taiwan_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.TaiwanDollar\'> '
                   'and <class \'str\'>.')):
        _ = taiwan_dollar_one.__add__('1.00')
    assert (
        taiwan_dollar_one +
        taiwan_dollar_two) == taiwan_dollar_three


def test_taiwan_dollar_slots():
    """test_taiwan_dollar_slots."""
    taiwan_dollar = TaiwanDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'TaiwanDollar\' '
                'object has no attribute \'new_variable\'')):
        taiwan_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
