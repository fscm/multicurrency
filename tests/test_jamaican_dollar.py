# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Jamaican Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, JamaicanDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_jamaican_dollar():
    """test_jamaican_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    jamaican_dollar = JamaicanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert jamaican_dollar.amount == decimal
    assert jamaican_dollar.numeric_code == '388'
    assert jamaican_dollar.alpha_code == 'JMD'
    assert jamaican_dollar.decimal_places == 2
    assert jamaican_dollar.decimal_sign == '.'
    assert jamaican_dollar.grouping_sign == ','
    assert not jamaican_dollar.international
    assert jamaican_dollar.symbol == '$'
    assert jamaican_dollar.symbol_ahead
    assert jamaican_dollar.symbol_separator == ''
    assert jamaican_dollar.convertion == ''
    assert jamaican_dollar.__hash__() == hash((decimal, 'JMD', '388'))
    assert jamaican_dollar.__repr__() == (
        'JamaicanDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "JMD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "388", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert jamaican_dollar.__str__() == '$0.14'


def test_jamaican_dollar_negative():
    """test_jamaican_dollar_negative."""
    amount = -100
    jamaican_dollar = JamaicanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert jamaican_dollar.numeric_code == '388'
    assert jamaican_dollar.alpha_code == 'JMD'
    assert jamaican_dollar.decimal_places == 2
    assert jamaican_dollar.decimal_sign == '.'
    assert jamaican_dollar.grouping_sign == ','
    assert not jamaican_dollar.international
    assert jamaican_dollar.symbol == '$'
    assert jamaican_dollar.symbol_ahead
    assert jamaican_dollar.symbol_separator == ''
    assert jamaican_dollar.convertion == ''
    assert jamaican_dollar.__hash__() == hash((decimal, 'JMD', '388'))
    assert jamaican_dollar.__repr__() == (
        'JamaicanDollar(amount: -100, '
        'alpha_code: "JMD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "388", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert jamaican_dollar.__str__() == '$-100.00'


def test_jamaican_dollar_custom():
    """test_jamaican_dollar_custom."""
    amount = 1000
    jamaican_dollar = JamaicanDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert jamaican_dollar.amount == decimal
    assert jamaican_dollar.numeric_code == '388'
    assert jamaican_dollar.alpha_code == 'JMD'
    assert jamaican_dollar.decimal_places == 5
    assert jamaican_dollar.decimal_sign == ','
    assert jamaican_dollar.grouping_sign == '.'
    assert jamaican_dollar.international
    assert jamaican_dollar.symbol == '$'
    assert not jamaican_dollar.symbol_ahead
    assert jamaican_dollar.symbol_separator == '_'
    assert jamaican_dollar.convertion == ''
    assert jamaican_dollar.__hash__() == hash((decimal, 'JMD', '388'))
    assert jamaican_dollar.__repr__() == (
        'JamaicanDollar(amount: 1000, '
        'alpha_code: "JMD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "388", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert jamaican_dollar.__str__() == 'JMD 1,000.00000'


def test_jamaican_dollar_changed():
    """test_cjamaican_dollar_changed."""
    jamaican_dollar = JamaicanDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jamaican_dollar.international = True


def test_jamaican_dollar_math_add():
    """test_jamaican_dollar_math_add."""
    jamaican_dollar_one = JamaicanDollar(amount=1)
    jamaican_dollar_two = JamaicanDollar(amount=2)
    jamaican_dollar_three = JamaicanDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency JMD and OTHER.'):
        _ = jamaican_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.JamaicanDollar\'> '
                   'and <class \'str\'>.')):
        _ = jamaican_dollar_one.__add__('1.00')
    assert (
        jamaican_dollar_one +
        jamaican_dollar_two) == jamaican_dollar_three


def test_jamaican_dollar_slots():
    """test_jamaican_dollar_slots."""
    jamaican_dollar = JamaicanDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'JamaicanDollar\' '
                'object has no attribute \'new_variable\'')):
        jamaican_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
