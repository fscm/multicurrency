# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroBE representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroBE
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurobe():
    """test_eurobe."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurobe = EuroBE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurobe.amount == decimal
    assert eurobe.numeric_code == '978'
    assert eurobe.alpha_code == 'EUR'
    assert eurobe.decimal_places == 2
    assert eurobe.decimal_sign == ','
    assert eurobe.grouping_places == 3
    assert eurobe.grouping_sign == '.'
    assert not eurobe.international
    assert eurobe.symbol == '€'
    assert eurobe.symbol_ahead
    assert eurobe.symbol_separator == '\u00A0'
    assert eurobe.convertion == ''
    assert eurobe.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurobe.__repr__() == (
        'EuroBE(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurobe.__str__() == '€ 0,14'


def test_eurobe_negative():
    """test_eurobe_negative."""
    amount = -100
    eurobe = EuroBE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurobe.numeric_code == '978'
    assert eurobe.alpha_code == 'EUR'
    assert eurobe.decimal_places == 2
    assert eurobe.decimal_sign == ','
    assert eurobe.grouping_places == 3
    assert eurobe.grouping_sign == '.'
    assert not eurobe.international
    assert eurobe.symbol == '€'
    assert eurobe.symbol_ahead
    assert eurobe.symbol_separator == '\u00A0'
    assert eurobe.convertion == ''
    assert eurobe.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurobe.__repr__() == (
        'EuroBE(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurobe.__str__() == '€ -100,00'


def test_eurobe_custom():
    """test_eurobe_custom."""
    amount = 1000
    eurobe = EuroBE(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurobe.amount == decimal
    assert eurobe.numeric_code == '978'
    assert eurobe.alpha_code == 'EUR'
    assert eurobe.decimal_places == 5
    assert eurobe.decimal_sign == '.'
    assert eurobe.grouping_places == 2
    assert eurobe.grouping_sign == ','
    assert eurobe.international
    assert eurobe.symbol == '€'
    assert not eurobe.symbol_ahead
    assert eurobe.symbol_separator == '_'
    assert eurobe.convertion == ''
    assert eurobe.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurobe.__repr__() == (
        'EuroBE(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurobe.__str__() == 'EUR 10,00.00000'


def test_eurobe_changed():
    """test_ceurobe_changed."""
    eurobe = EuroBE(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurobe.international = True


def test_eurobe_math_add():
    """test_eurobe_math_add."""
    eurobe_one = EuroBE(amount=1)
    eurobe_two = EuroBE(amount=2)
    eurobe_three = EuroBE(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurobe_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroBE\'> '
                   'and <class \'str\'>.')):
        _ = eurobe_one.__add__('1.00')
    assert (
        eurobe_one +
        eurobe_two) == eurobe_three


def test_eurobe_slots():
    """test_eurobe_slots."""
    eurobe = EuroBE(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroBE\' '
                'object has no attribute \'new_variable\'')):
        eurobe.new_variable = 'fail'  # pylint: disable=assigning-non-slot
