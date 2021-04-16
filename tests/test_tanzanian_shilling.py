# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tanzanian Shilling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, TanzanianShilling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tanzanian_shilling():
    """test_tanzanian_shilling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tanzanian_shilling = TanzanianShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tanzanian_shilling.amount == decimal
    assert tanzanian_shilling.numeric_code == '834'
    assert tanzanian_shilling.alpha_code == 'TZS'
    assert tanzanian_shilling.decimal_places == 2
    assert tanzanian_shilling.decimal_sign == '.'
    assert tanzanian_shilling.grouping_sign == ','
    assert not tanzanian_shilling.international
    assert tanzanian_shilling.symbol == 'TSh'
    assert tanzanian_shilling.symbol_ahead
    assert tanzanian_shilling.symbol_separator == '\u00A0'
    assert tanzanian_shilling.__hash__() == hash((decimal, 'TZS', '834'))
    assert tanzanian_shilling.__repr__() == (
        'TanzanianShilling(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TZS", '
        'symbol: "TSh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "834", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert tanzanian_shilling.__str__() == 'TSh 0.14'


def test_tanzanian_shilling_negative():
    """test_tanzanian_shilling_negative."""
    amount = -100
    tanzanian_shilling = TanzanianShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tanzanian_shilling.numeric_code == '834'
    assert tanzanian_shilling.alpha_code == 'TZS'
    assert tanzanian_shilling.decimal_places == 2
    assert tanzanian_shilling.decimal_sign == '.'
    assert tanzanian_shilling.grouping_sign == ','
    assert not tanzanian_shilling.international
    assert tanzanian_shilling.symbol == 'TSh'
    assert tanzanian_shilling.symbol_ahead
    assert tanzanian_shilling.symbol_separator == '\u00A0'
    assert tanzanian_shilling.__hash__() == hash((decimal, 'TZS', '834'))
    assert tanzanian_shilling.__repr__() == (
        'TanzanianShilling(amount: -100, '
        'alpha_code: "TZS", '
        'symbol: "TSh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "834", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert tanzanian_shilling.__str__() == 'TSh -100.00'


def test_tanzanian_shilling_custom():
    """test_tanzanian_shilling_custom."""
    amount = 1000
    tanzanian_shilling = TanzanianShilling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert tanzanian_shilling.amount == decimal
    assert tanzanian_shilling.numeric_code == '834'
    assert tanzanian_shilling.alpha_code == 'TZS'
    assert tanzanian_shilling.decimal_places == 5
    assert tanzanian_shilling.decimal_sign == ','
    assert tanzanian_shilling.grouping_sign == '.'
    assert tanzanian_shilling.international
    assert tanzanian_shilling.symbol == 'TSh'
    assert not tanzanian_shilling.symbol_ahead
    assert tanzanian_shilling.symbol_separator == '_'
    assert tanzanian_shilling.__hash__() == hash((decimal, 'TZS', '834'))
    assert tanzanian_shilling.__repr__() == (
        'TanzanianShilling(amount: 1000, '
        'alpha_code: "TZS", '
        'symbol: "TSh", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "834", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert tanzanian_shilling.__str__() == 'TZS 1,000.00000'


def test_tanzanian_shilling_changed():
    """test_ctanzanian_shilling_changed."""
    tanzanian_shilling = TanzanianShilling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tanzanian_shilling.international = True


def test_tanzanian_shilling_math_add():
    """test_tanzanian_shilling_math_add."""
    tanzanian_shilling_one = TanzanianShilling(amount=1)
    tanzanian_shilling_two = TanzanianShilling(amount=2)
    tanzanian_shilling_three = TanzanianShilling(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TZS and OTHER.'):
        _ = tanzanian_shilling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'shilling.TanzanianShilling\'> '
                   'and <class \'str\'>.')):
        _ = tanzanian_shilling_one.__add__('1.00')
    assert (
        tanzanian_shilling_one +
        tanzanian_shilling_two) == tanzanian_shilling_three


def test_tanzanian_shilling_slots():
    """test_tanzanian_shilling_slots."""
    tanzanian_shilling = TanzanianShilling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'TanzanianShilling\' '
                'object has no attribute \'new_variable\'')):
        tanzanian_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot
