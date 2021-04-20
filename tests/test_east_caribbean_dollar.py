# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the East Caribbean Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EastCaribbeanDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_east_caribbean_dollar():
    """test_east_caribbean_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    east_caribbean_dollar = EastCaribbeanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert east_caribbean_dollar.amount == decimal
    assert east_caribbean_dollar.numeric_code == '951'
    assert east_caribbean_dollar.alpha_code == 'XCD'
    assert east_caribbean_dollar.decimal_places == 2
    assert east_caribbean_dollar.decimal_sign == '.'
    assert east_caribbean_dollar.grouping_sign == ','
    assert not east_caribbean_dollar.international
    assert east_caribbean_dollar.symbol == '$'
    assert east_caribbean_dollar.symbol_ahead
    assert east_caribbean_dollar.symbol_separator == ''
    assert east_caribbean_dollar.convertion == ''
    assert east_caribbean_dollar.__hash__() == hash((decimal, 'XCD', '951'))
    assert east_caribbean_dollar.__repr__() == (
        'EastCaribbeanDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XCD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "951", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert east_caribbean_dollar.__str__() == '$0.14'


def test_east_caribbean_dollar_negative():
    """test_east_caribbean_dollar_negative."""
    amount = -100
    east_caribbean_dollar = EastCaribbeanDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert east_caribbean_dollar.numeric_code == '951'
    assert east_caribbean_dollar.alpha_code == 'XCD'
    assert east_caribbean_dollar.decimal_places == 2
    assert east_caribbean_dollar.decimal_sign == '.'
    assert east_caribbean_dollar.grouping_sign == ','
    assert not east_caribbean_dollar.international
    assert east_caribbean_dollar.symbol == '$'
    assert east_caribbean_dollar.symbol_ahead
    assert east_caribbean_dollar.symbol_separator == ''
    assert east_caribbean_dollar.convertion == ''
    assert east_caribbean_dollar.__hash__() == hash((decimal, 'XCD', '951'))
    assert east_caribbean_dollar.__repr__() == (
        'EastCaribbeanDollar(amount: -100, '
        'alpha_code: "XCD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "951", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert east_caribbean_dollar.__str__() == '$-100.00'


def test_east_caribbean_dollar_custom():
    """test_east_caribbean_dollar_custom."""
    amount = 1000
    east_caribbean_dollar = EastCaribbeanDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert east_caribbean_dollar.amount == decimal
    assert east_caribbean_dollar.numeric_code == '951'
    assert east_caribbean_dollar.alpha_code == 'XCD'
    assert east_caribbean_dollar.decimal_places == 5
    assert east_caribbean_dollar.decimal_sign == ','
    assert east_caribbean_dollar.grouping_sign == '.'
    assert east_caribbean_dollar.international
    assert east_caribbean_dollar.symbol == '$'
    assert not east_caribbean_dollar.symbol_ahead
    assert east_caribbean_dollar.symbol_separator == '_'
    assert east_caribbean_dollar.convertion == ''
    assert east_caribbean_dollar.__hash__() == hash((decimal, 'XCD', '951'))
    assert east_caribbean_dollar.__repr__() == (
        'EastCaribbeanDollar(amount: 1000, '
        'alpha_code: "XCD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "951", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert east_caribbean_dollar.__str__() == 'XCD 1,000.00000'


def test_east_caribbean_dollar_changed():
    """test_ceast_caribbean_dollar_changed."""
    east_caribbean_dollar = EastCaribbeanDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        east_caribbean_dollar.international = True


def test_east_caribbean_dollar_math_add():
    """test_east_caribbean_dollar_math_add."""
    east_caribbean_dollar_one = EastCaribbeanDollar(amount=1)
    east_caribbean_dollar_two = EastCaribbeanDollar(amount=2)
    east_caribbean_dollar_three = EastCaribbeanDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XCD and OTHER.'):
        _ = east_caribbean_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.EastCaribbeanDollar\'> '
                   'and <class \'str\'>.')):
        _ = east_caribbean_dollar_one.__add__('1.00')
    assert (
        east_caribbean_dollar_one +
        east_caribbean_dollar_two) == east_caribbean_dollar_three


def test_east_caribbean_dollar_slots():
    """test_east_caribbean_dollar_slots."""
    east_caribbean_dollar = EastCaribbeanDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EastCaribbeanDollar\' '
                'object has no attribute \'new_variable\'')):
        east_caribbean_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
