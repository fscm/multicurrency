# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroFI representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroFI
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurofi():
    """test_eurofi."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurofi = EuroFI(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurofi.amount == decimal
    assert eurofi.numeric_code == '978'
    assert eurofi.alpha_code == 'EUR'
    assert eurofi.decimal_places == 2
    assert eurofi.decimal_sign == ','
    assert eurofi.grouping_sign == '\u202F'
    assert not eurofi.international
    assert eurofi.symbol == '€'
    assert not eurofi.symbol_ahead
    assert eurofi.symbol_separator == '\u00A0'
    assert eurofi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofi.__repr__() == (
        'EuroFI(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurofi.__str__() == '0,14 €'


def test_eurofi_negative():
    """test_eurofi_negative."""
    amount = -100
    eurofi = EuroFI(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurofi.numeric_code == '978'
    assert eurofi.alpha_code == 'EUR'
    assert eurofi.decimal_places == 2
    assert eurofi.decimal_sign == ','
    assert eurofi.grouping_sign == '\u202F'
    assert not eurofi.international
    assert eurofi.symbol == '€'
    assert not eurofi.symbol_ahead
    assert eurofi.symbol_separator == '\u00A0'
    assert eurofi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofi.__repr__() == (
        'EuroFI(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert eurofi.__str__() == '-100,00 €'


def test_eurofi_custom():
    """test_eurofi_custom."""
    amount = 1000
    eurofi = EuroFI(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurofi.amount == decimal
    assert eurofi.numeric_code == '978'
    assert eurofi.alpha_code == 'EUR'
    assert eurofi.decimal_places == 5
    assert eurofi.decimal_sign == '\u202F'
    assert eurofi.grouping_sign == ','
    assert eurofi.international
    assert eurofi.symbol == '€'
    assert not eurofi.symbol_ahead
    assert eurofi.symbol_separator == '_'
    assert eurofi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurofi.__repr__() == (
        'EuroFI(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert eurofi.__str__() == 'EUR 1,000.00000'


def test_eurofi_changed():
    """test_ceurofi_changed."""
    eurofi = EuroFI(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurofi.international = True


def test_eurofi_math_add():
    """test_eurofi_math_add."""
    eurofi_one = EuroFI(amount=1)
    eurofi_two = EuroFI(amount=2)
    eurofi_three = EuroFI(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurofi_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroFI\'> '
                   'and <class \'str\'>.')):
        _ = eurofi_one.__add__('1.00')
    assert (
        eurofi_one +
        eurofi_two) == eurofi_three


def test_eurofi_slots():
    """test_eurofi_slots."""
    eurofi = EuroFI(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroFI\' '
                'object has no attribute \'new_variable\'')):
        eurofi.new_variable = 'fail'  # pylint: disable=assigning-non-slot
