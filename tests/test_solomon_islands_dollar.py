# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Solomon Islands Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SolomonIslandsDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_solomon_islands_dollar():
    """test_solomon_islands_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    solomon_islands_dollar = SolomonIslandsDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert solomon_islands_dollar.amount == decimal
    assert solomon_islands_dollar.numeric_code == '090'
    assert solomon_islands_dollar.alpha_code == 'SBD'
    assert solomon_islands_dollar.decimal_places == 2
    assert solomon_islands_dollar.decimal_sign == '.'
    assert solomon_islands_dollar.grouping_places == 3
    assert solomon_islands_dollar.grouping_sign == ','
    assert not solomon_islands_dollar.international
    assert solomon_islands_dollar.symbol == '$'
    assert solomon_islands_dollar.symbol_ahead
    assert solomon_islands_dollar.symbol_separator == ''
    assert solomon_islands_dollar.convertion == ''
    assert solomon_islands_dollar.__hash__() == hash((decimal, 'SBD', '090'))
    assert solomon_islands_dollar.__repr__() == (
        'SolomonIslandsDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SBD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "090", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert solomon_islands_dollar.__str__() == '$0.14'


def test_solomon_islands_dollar_negative():
    """test_solomon_islands_dollar_negative."""
    amount = -100
    solomon_islands_dollar = SolomonIslandsDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert solomon_islands_dollar.numeric_code == '090'
    assert solomon_islands_dollar.alpha_code == 'SBD'
    assert solomon_islands_dollar.decimal_places == 2
    assert solomon_islands_dollar.decimal_sign == '.'
    assert solomon_islands_dollar.grouping_places == 3
    assert solomon_islands_dollar.grouping_sign == ','
    assert not solomon_islands_dollar.international
    assert solomon_islands_dollar.symbol == '$'
    assert solomon_islands_dollar.symbol_ahead
    assert solomon_islands_dollar.symbol_separator == ''
    assert solomon_islands_dollar.convertion == ''
    assert solomon_islands_dollar.__hash__() == hash((decimal, 'SBD', '090'))
    assert solomon_islands_dollar.__repr__() == (
        'SolomonIslandsDollar(amount: -100, '
        'alpha_code: "SBD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "090", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert solomon_islands_dollar.__str__() == '$-100.00'


def test_solomon_islands_dollar_custom():
    """test_solomon_islands_dollar_custom."""
    amount = 1000
    solomon_islands_dollar = SolomonIslandsDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert solomon_islands_dollar.amount == decimal
    assert solomon_islands_dollar.numeric_code == '090'
    assert solomon_islands_dollar.alpha_code == 'SBD'
    assert solomon_islands_dollar.decimal_places == 5
    assert solomon_islands_dollar.decimal_sign == ','
    assert solomon_islands_dollar.grouping_places == 2
    assert solomon_islands_dollar.grouping_sign == '.'
    assert solomon_islands_dollar.international
    assert solomon_islands_dollar.symbol == '$'
    assert not solomon_islands_dollar.symbol_ahead
    assert solomon_islands_dollar.symbol_separator == '_'
    assert solomon_islands_dollar.convertion == ''
    assert solomon_islands_dollar.__hash__() == hash((decimal, 'SBD', '090'))
    assert solomon_islands_dollar.__repr__() == (
        'SolomonIslandsDollar(amount: 1000, '
        'alpha_code: "SBD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "090", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert solomon_islands_dollar.__str__() == 'SBD 10,00.00000'


def test_solomon_islands_dollar_changed():
    """test_csolomon_islands_dollar_changed."""
    solomon_islands_dollar = SolomonIslandsDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.symbol = '???'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        solomon_islands_dollar.international = True


def test_solomon_islands_dollar_math_add():
    """test_solomon_islands_dollar_math_add."""
    solomon_islands_dollar_one = SolomonIslandsDollar(amount=1)
    solomon_islands_dollar_two = SolomonIslandsDollar(amount=2)
    solomon_islands_dollar_three = SolomonIslandsDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SBD and OTHER.'):
        _ = solomon_islands_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.SolomonIslandsDollar\'> '
                   'and <class \'str\'>.')):
        _ = solomon_islands_dollar_one.__add__('1.00')
    assert (
        solomon_islands_dollar_one +
        solomon_islands_dollar_two) == solomon_islands_dollar_three


def test_solomon_islands_dollar_slots():
    """test_solomon_islands_dollar_slots."""
    solomon_islands_dollar = SolomonIslandsDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SolomonIslandsDollar\' '
                'object has no attribute \'new_variable\'')):
        solomon_islands_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
