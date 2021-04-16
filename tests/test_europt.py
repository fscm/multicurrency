# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroPT representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroPT
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_europt():
    """test_europt."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    europt = EuroPT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert europt.amount == decimal
    assert europt.numeric_code == '978'
    assert europt.alpha_code == 'EUR'
    assert europt.decimal_places == 2
    assert europt.decimal_sign == ','
    assert europt.grouping_sign == '.'
    assert not europt.international
    assert europt.symbol == '€'
    assert europt.symbol_ahead
    assert europt.symbol_separator == '\u00A0'
    assert europt.__hash__() == hash((decimal, 'EUR', '978'))
    assert europt.__repr__() == (
        'EuroPT(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert europt.__str__() == '€ 0,14'


def test_europt_negative():
    """test_europt_negative."""
    amount = -100
    europt = EuroPT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert europt.numeric_code == '978'
    assert europt.alpha_code == 'EUR'
    assert europt.decimal_places == 2
    assert europt.decimal_sign == ','
    assert europt.grouping_sign == '.'
    assert not europt.international
    assert europt.symbol == '€'
    assert europt.symbol_ahead
    assert europt.symbol_separator == '\u00A0'
    assert europt.__hash__() == hash((decimal, 'EUR', '978'))
    assert europt.__repr__() == (
        'EuroPT(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert europt.__str__() == '€ -100,00'


def test_europt_custom():
    """test_europt_custom."""
    amount = 1000
    europt = EuroPT(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert europt.amount == decimal
    assert europt.numeric_code == '978'
    assert europt.alpha_code == 'EUR'
    assert europt.decimal_places == 5
    assert europt.decimal_sign == '.'
    assert europt.grouping_sign == ','
    assert europt.international
    assert europt.symbol == '€'
    assert not europt.symbol_ahead
    assert europt.symbol_separator == '_'
    assert europt.__hash__() == hash((decimal, 'EUR', '978'))
    assert europt.__repr__() == (
        'EuroPT(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert europt.__str__() == 'EUR 1,000.00000'


def test_europt_changed():
    """test_ceuropt_changed."""
    europt = EuroPT(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        europt.international = True


def test_europt_math_add():
    """test_europt_math_add."""
    europt_one = EuroPT(amount=1)
    europt_two = EuroPT(amount=2)
    europt_three = EuroPT(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = europt_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroPT\'> '
                   'and <class \'str\'>.')):
        _ = europt_one.__add__('1.00')
    assert (
        europt_one +
        europt_two) == europt_three


def test_europt_slots():
    """test_europt_slots."""
    europt = EuroPT(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroPT\' '
                'object has no attribute \'new_variable\'')):
        europt.new_variable = 'fail'  # pylint: disable=assigning-non-slot
