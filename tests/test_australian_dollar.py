# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Australian Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, AustralianDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_australian_dollar():
    """test_australian_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    australian_dollar = AustralianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert australian_dollar.amount == decimal
    assert australian_dollar.numeric_code == '036'
    assert australian_dollar.alpha_code == 'AUD'
    assert australian_dollar.decimal_places == 2
    assert australian_dollar.decimal_sign == '.'
    assert australian_dollar.grouping_places == 3
    assert australian_dollar.grouping_sign == ','
    assert not australian_dollar.international
    assert australian_dollar.symbol == '$'
    assert australian_dollar.symbol_ahead
    assert australian_dollar.symbol_separator == ''
    assert australian_dollar.convertion == ''
    assert australian_dollar.__hash__() == hash((decimal, 'AUD', '036'))
    assert australian_dollar.__repr__() == (
        'AustralianDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AUD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "036", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert australian_dollar.__str__() == '$0.14'


def test_australian_dollar_negative():
    """test_australian_dollar_negative."""
    amount = -100
    australian_dollar = AustralianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert australian_dollar.numeric_code == '036'
    assert australian_dollar.alpha_code == 'AUD'
    assert australian_dollar.decimal_places == 2
    assert australian_dollar.decimal_sign == '.'
    assert australian_dollar.grouping_places == 3
    assert australian_dollar.grouping_sign == ','
    assert not australian_dollar.international
    assert australian_dollar.symbol == '$'
    assert australian_dollar.symbol_ahead
    assert australian_dollar.symbol_separator == ''
    assert australian_dollar.convertion == ''
    assert australian_dollar.__hash__() == hash((decimal, 'AUD', '036'))
    assert australian_dollar.__repr__() == (
        'AustralianDollar(amount: -100, '
        'alpha_code: "AUD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "036", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert australian_dollar.__str__() == '$-100.00'


def test_australian_dollar_custom():
    """test_australian_dollar_custom."""
    amount = 1000
    australian_dollar = AustralianDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert australian_dollar.amount == decimal
    assert australian_dollar.numeric_code == '036'
    assert australian_dollar.alpha_code == 'AUD'
    assert australian_dollar.decimal_places == 5
    assert australian_dollar.decimal_sign == ','
    assert australian_dollar.grouping_places == 2
    assert australian_dollar.grouping_sign == '.'
    assert australian_dollar.international
    assert australian_dollar.symbol == '$'
    assert not australian_dollar.symbol_ahead
    assert australian_dollar.symbol_separator == '_'
    assert australian_dollar.convertion == ''
    assert australian_dollar.__hash__() == hash((decimal, 'AUD', '036'))
    assert australian_dollar.__repr__() == (
        'AustralianDollar(amount: 1000, '
        'alpha_code: "AUD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "036", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert australian_dollar.__str__() == 'AUD 10,00.00000'


def test_australian_dollar_changed():
    """test_caustralian_dollar_changed."""
    australian_dollar = AustralianDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.symbol = '???'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        australian_dollar.international = True


def test_australian_dollar_math_add():
    """test_australian_dollar_math_add."""
    australian_dollar_one = AustralianDollar(amount=1)
    australian_dollar_two = AustralianDollar(amount=2)
    australian_dollar_three = AustralianDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AUD and OTHER.'):
        _ = australian_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.AustralianDollar\'> '
                   'and <class \'str\'>.')):
        _ = australian_dollar_one.__add__('1.00')
    assert (
        australian_dollar_one +
        australian_dollar_two) == australian_dollar_three


def test_australian_dollar_slots():
    """test_australian_dollar_slots."""
    australian_dollar = AustralianDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'AustralianDollar\' '
                'object has no attribute \'new_variable\'')):
        australian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
