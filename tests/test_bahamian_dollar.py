# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bahamian Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BahamianDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bahamian_dollar():
    """test_bahamian_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bahamian_dollar = BahamianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bahamian_dollar.amount == decimal
    assert bahamian_dollar.numeric_code == '044'
    assert bahamian_dollar.alpha_code == 'BSD'
    assert bahamian_dollar.decimal_places == 2
    assert bahamian_dollar.decimal_sign == '.'
    assert bahamian_dollar.grouping_sign == ','
    assert not bahamian_dollar.international
    assert bahamian_dollar.symbol == '$'
    assert bahamian_dollar.symbol_ahead
    assert bahamian_dollar.symbol_separator == ''
    assert bahamian_dollar.__hash__() == hash((decimal, 'BSD', '044'))
    assert bahamian_dollar.__repr__() == (
        'BahamianDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BSD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "044", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert bahamian_dollar.__str__() == '$0.14'


def test_bahamian_dollar_negative():
    """test_bahamian_dollar_negative."""
    amount = -100
    bahamian_dollar = BahamianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bahamian_dollar.numeric_code == '044'
    assert bahamian_dollar.alpha_code == 'BSD'
    assert bahamian_dollar.decimal_places == 2
    assert bahamian_dollar.decimal_sign == '.'
    assert bahamian_dollar.grouping_sign == ','
    assert not bahamian_dollar.international
    assert bahamian_dollar.symbol == '$'
    assert bahamian_dollar.symbol_ahead
    assert bahamian_dollar.symbol_separator == ''
    assert bahamian_dollar.__hash__() == hash((decimal, 'BSD', '044'))
    assert bahamian_dollar.__repr__() == (
        'BahamianDollar(amount: -100, '
        'alpha_code: "BSD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "044", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert bahamian_dollar.__str__() == '$-100.00'


def test_bahamian_dollar_custom():
    """test_bahamian_dollar_custom."""
    amount = 1000
    bahamian_dollar = BahamianDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert bahamian_dollar.amount == decimal
    assert bahamian_dollar.numeric_code == '044'
    assert bahamian_dollar.alpha_code == 'BSD'
    assert bahamian_dollar.decimal_places == 5
    assert bahamian_dollar.decimal_sign == ','
    assert bahamian_dollar.grouping_sign == '.'
    assert bahamian_dollar.international
    assert bahamian_dollar.symbol == '$'
    assert not bahamian_dollar.symbol_ahead
    assert bahamian_dollar.symbol_separator == '_'
    assert bahamian_dollar.__hash__() == hash((decimal, 'BSD', '044'))
    assert bahamian_dollar.__repr__() == (
        'BahamianDollar(amount: 1000, '
        'alpha_code: "BSD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "044", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert bahamian_dollar.__str__() == 'BSD 1,000.00000'


def test_bahamian_dollar_changed():
    """test_cbahamian_dollar_changed."""
    bahamian_dollar = BahamianDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahamian_dollar.international = True


def test_bahamian_dollar_math_add():
    """test_bahamian_dollar_math_add."""
    bahamian_dollar_one = BahamianDollar(amount=1)
    bahamian_dollar_two = BahamianDollar(amount=2)
    bahamian_dollar_three = BahamianDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BSD and OTHER.'):
        _ = bahamian_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.BahamianDollar\'> '
                   'and <class \'str\'>.')):
        _ = bahamian_dollar_one.__add__('1.00')
    assert (
        bahamian_dollar_one +
        bahamian_dollar_two) == bahamian_dollar_three


def test_bahamian_dollar_slots():
    """test_bahamian_dollar_slots."""
    bahamian_dollar = BahamianDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BahamianDollar\' '
                'object has no attribute \'new_variable\'')):
        bahamian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
