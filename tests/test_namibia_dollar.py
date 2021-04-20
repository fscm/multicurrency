# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Namibia Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NamibiaDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_namibia_dollar():
    """test_namibia_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    namibia_dollar = NamibiaDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert namibia_dollar.amount == decimal
    assert namibia_dollar.numeric_code == '516'
    assert namibia_dollar.alpha_code == 'NAD'
    assert namibia_dollar.decimal_places == 2
    assert namibia_dollar.decimal_sign == '.'
    assert namibia_dollar.grouping_sign == ','
    assert not namibia_dollar.international
    assert namibia_dollar.symbol == '$'
    assert namibia_dollar.symbol_ahead
    assert namibia_dollar.symbol_separator == ''
    assert namibia_dollar.convertion == ''
    assert namibia_dollar.__hash__() == hash((decimal, 'NAD', '516'))
    assert namibia_dollar.__repr__() == (
        'NamibiaDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "NAD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "516", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert namibia_dollar.__str__() == '$0.14'


def test_namibia_dollar_negative():
    """test_namibia_dollar_negative."""
    amount = -100
    namibia_dollar = NamibiaDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert namibia_dollar.numeric_code == '516'
    assert namibia_dollar.alpha_code == 'NAD'
    assert namibia_dollar.decimal_places == 2
    assert namibia_dollar.decimal_sign == '.'
    assert namibia_dollar.grouping_sign == ','
    assert not namibia_dollar.international
    assert namibia_dollar.symbol == '$'
    assert namibia_dollar.symbol_ahead
    assert namibia_dollar.symbol_separator == ''
    assert namibia_dollar.convertion == ''
    assert namibia_dollar.__hash__() == hash((decimal, 'NAD', '516'))
    assert namibia_dollar.__repr__() == (
        'NamibiaDollar(amount: -100, '
        'alpha_code: "NAD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "516", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert namibia_dollar.__str__() == '$-100.00'


def test_namibia_dollar_custom():
    """test_namibia_dollar_custom."""
    amount = 1000
    namibia_dollar = NamibiaDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert namibia_dollar.amount == decimal
    assert namibia_dollar.numeric_code == '516'
    assert namibia_dollar.alpha_code == 'NAD'
    assert namibia_dollar.decimal_places == 5
    assert namibia_dollar.decimal_sign == ','
    assert namibia_dollar.grouping_sign == '.'
    assert namibia_dollar.international
    assert namibia_dollar.symbol == '$'
    assert not namibia_dollar.symbol_ahead
    assert namibia_dollar.symbol_separator == '_'
    assert namibia_dollar.convertion == ''
    assert namibia_dollar.__hash__() == hash((decimal, 'NAD', '516'))
    assert namibia_dollar.__repr__() == (
        'NamibiaDollar(amount: 1000, '
        'alpha_code: "NAD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "516", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert namibia_dollar.__str__() == 'NAD 1,000.00000'


def test_namibia_dollar_changed():
    """test_cnamibia_dollar_changed."""
    namibia_dollar = NamibiaDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        namibia_dollar.international = True


def test_namibia_dollar_math_add():
    """test_namibia_dollar_math_add."""
    namibia_dollar_one = NamibiaDollar(amount=1)
    namibia_dollar_two = NamibiaDollar(amount=2)
    namibia_dollar_three = NamibiaDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NAD and OTHER.'):
        _ = namibia_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.NamibiaDollar\'> '
                   'and <class \'str\'>.')):
        _ = namibia_dollar_one.__add__('1.00')
    assert (
        namibia_dollar_one +
        namibia_dollar_two) == namibia_dollar_three


def test_namibia_dollar_slots():
    """test_namibia_dollar_slots."""
    namibia_dollar = NamibiaDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NamibiaDollar\' '
                'object has no attribute \'new_variable\'')):
        namibia_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
