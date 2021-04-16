# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Liberian Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, LiberianDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_liberian_dollar():
    """test_liberian_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    liberian_dollar = LiberianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert liberian_dollar.amount == decimal
    assert liberian_dollar.numeric_code == '430'
    assert liberian_dollar.alpha_code == 'LRD'
    assert liberian_dollar.decimal_places == 2
    assert liberian_dollar.decimal_sign == '.'
    assert liberian_dollar.grouping_sign == ','
    assert not liberian_dollar.international
    assert liberian_dollar.symbol == '$'
    assert liberian_dollar.symbol_ahead
    assert liberian_dollar.symbol_separator == ''
    assert liberian_dollar.__hash__() == hash((decimal, 'LRD', '430'))
    assert liberian_dollar.__repr__() == (
        'LiberianDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "LRD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "430", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert liberian_dollar.__str__() == '$0.14'


def test_liberian_dollar_negative():
    """test_liberian_dollar_negative."""
    amount = -100
    liberian_dollar = LiberianDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert liberian_dollar.numeric_code == '430'
    assert liberian_dollar.alpha_code == 'LRD'
    assert liberian_dollar.decimal_places == 2
    assert liberian_dollar.decimal_sign == '.'
    assert liberian_dollar.grouping_sign == ','
    assert not liberian_dollar.international
    assert liberian_dollar.symbol == '$'
    assert liberian_dollar.symbol_ahead
    assert liberian_dollar.symbol_separator == ''
    assert liberian_dollar.__hash__() == hash((decimal, 'LRD', '430'))
    assert liberian_dollar.__repr__() == (
        'LiberianDollar(amount: -100, '
        'alpha_code: "LRD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "430", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert liberian_dollar.__str__() == '$-100.00'


def test_liberian_dollar_custom():
    """test_liberian_dollar_custom."""
    amount = 1000
    liberian_dollar = LiberianDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert liberian_dollar.amount == decimal
    assert liberian_dollar.numeric_code == '430'
    assert liberian_dollar.alpha_code == 'LRD'
    assert liberian_dollar.decimal_places == 5
    assert liberian_dollar.decimal_sign == ','
    assert liberian_dollar.grouping_sign == '.'
    assert liberian_dollar.international
    assert liberian_dollar.symbol == '$'
    assert not liberian_dollar.symbol_ahead
    assert liberian_dollar.symbol_separator == '_'
    assert liberian_dollar.__hash__() == hash((decimal, 'LRD', '430'))
    assert liberian_dollar.__repr__() == (
        'LiberianDollar(amount: 1000, '
        'alpha_code: "LRD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "430", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert liberian_dollar.__str__() == 'LRD 1,000.00000'


def test_liberian_dollar_changed():
    """test_cliberian_dollar_changed."""
    liberian_dollar = LiberianDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        liberian_dollar.international = True


def test_liberian_dollar_math_add():
    """test_liberian_dollar_math_add."""
    liberian_dollar_one = LiberianDollar(amount=1)
    liberian_dollar_two = LiberianDollar(amount=2)
    liberian_dollar_three = LiberianDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LRD and OTHER.'):
        _ = liberian_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.LiberianDollar\'> '
                   'and <class \'str\'>.')):
        _ = liberian_dollar_one.__add__('1.00')
    assert (
        liberian_dollar_one +
        liberian_dollar_two) == liberian_dollar_three


def test_liberian_dollar_slots():
    """test_liberian_dollar_slots."""
    liberian_dollar = LiberianDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'LiberianDollar\' '
                'object has no attribute \'new_variable\'')):
        liberian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
