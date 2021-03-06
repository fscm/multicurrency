# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the New Zealand Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NewZealandDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_new_zealand_dollar():
    """test_new_zealand_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    new_zealand_dollar = NewZealandDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert new_zealand_dollar.amount == decimal
    assert new_zealand_dollar.numeric_code == '554'
    assert new_zealand_dollar.alpha_code == 'NZD'
    assert new_zealand_dollar.decimal_places == 2
    assert new_zealand_dollar.decimal_sign == '.'
    assert new_zealand_dollar.grouping_places == 3
    assert new_zealand_dollar.grouping_sign == ','
    assert not new_zealand_dollar.international
    assert new_zealand_dollar.symbol == '$'
    assert new_zealand_dollar.symbol_ahead
    assert new_zealand_dollar.symbol_separator == ''
    assert new_zealand_dollar.convertion == ''
    assert new_zealand_dollar.__hash__() == hash((decimal, 'NZD', '554'))
    assert new_zealand_dollar.__repr__() == (
        'NewZealandDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "NZD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "554", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert new_zealand_dollar.__str__() == '$0.14'


def test_new_zealand_dollar_negative():
    """test_new_zealand_dollar_negative."""
    amount = -100
    new_zealand_dollar = NewZealandDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert new_zealand_dollar.numeric_code == '554'
    assert new_zealand_dollar.alpha_code == 'NZD'
    assert new_zealand_dollar.decimal_places == 2
    assert new_zealand_dollar.decimal_sign == '.'
    assert new_zealand_dollar.grouping_places == 3
    assert new_zealand_dollar.grouping_sign == ','
    assert not new_zealand_dollar.international
    assert new_zealand_dollar.symbol == '$'
    assert new_zealand_dollar.symbol_ahead
    assert new_zealand_dollar.symbol_separator == ''
    assert new_zealand_dollar.convertion == ''
    assert new_zealand_dollar.__hash__() == hash((decimal, 'NZD', '554'))
    assert new_zealand_dollar.__repr__() == (
        'NewZealandDollar(amount: -100, '
        'alpha_code: "NZD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "554", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert new_zealand_dollar.__str__() == '$-100.00'


def test_new_zealand_dollar_custom():
    """test_new_zealand_dollar_custom."""
    amount = 1000
    new_zealand_dollar = NewZealandDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert new_zealand_dollar.amount == decimal
    assert new_zealand_dollar.numeric_code == '554'
    assert new_zealand_dollar.alpha_code == 'NZD'
    assert new_zealand_dollar.decimal_places == 5
    assert new_zealand_dollar.decimal_sign == ','
    assert new_zealand_dollar.grouping_places == 2
    assert new_zealand_dollar.grouping_sign == '.'
    assert new_zealand_dollar.international
    assert new_zealand_dollar.symbol == '$'
    assert not new_zealand_dollar.symbol_ahead
    assert new_zealand_dollar.symbol_separator == '_'
    assert new_zealand_dollar.convertion == ''
    assert new_zealand_dollar.__hash__() == hash((decimal, 'NZD', '554'))
    assert new_zealand_dollar.__repr__() == (
        'NewZealandDollar(amount: 1000, '
        'alpha_code: "NZD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "554", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert new_zealand_dollar.__str__() == 'NZD 10,00.00000'


def test_new_zealand_dollar_changed():
    """test_cnew_zealand_dollar_changed."""
    new_zealand_dollar = NewZealandDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.symbol = '???'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_zealand_dollar.international = True


def test_new_zealand_dollar_math_add():
    """test_new_zealand_dollar_math_add."""
    new_zealand_dollar_one = NewZealandDollar(amount=1)
    new_zealand_dollar_two = NewZealandDollar(amount=2)
    new_zealand_dollar_three = NewZealandDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NZD and OTHER.'):
        _ = new_zealand_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.NewZealandDollar\'> '
                   'and <class \'str\'>.')):
        _ = new_zealand_dollar_one.__add__('1.00')
    assert (
        new_zealand_dollar_one +
        new_zealand_dollar_two) == new_zealand_dollar_three


def test_new_zealand_dollar_slots():
    """test_new_zealand_dollar_slots."""
    new_zealand_dollar = NewZealandDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NewZealandDollar\' '
                'object has no attribute \'new_variable\'')):
        new_zealand_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
