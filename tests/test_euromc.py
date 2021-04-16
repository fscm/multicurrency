# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroMC representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroMC
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euromc():
    """test_euromc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euromc = EuroMC(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euromc.amount == decimal
    assert euromc.numeric_code == '978'
    assert euromc.alpha_code == 'EUR'
    assert euromc.decimal_places == 2
    assert euromc.decimal_sign == ','
    assert euromc.grouping_sign == '\u202F'
    assert not euromc.international
    assert euromc.symbol == '€'
    assert not euromc.symbol_ahead
    assert euromc.symbol_separator == '\u00A0'
    assert euromc.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromc.__repr__() == (
        'EuroMC(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert euromc.__str__() == '0,14 €'


def test_euromc_negative():
    """test_euromc_negative."""
    amount = -100
    euromc = EuroMC(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euromc.numeric_code == '978'
    assert euromc.alpha_code == 'EUR'
    assert euromc.decimal_places == 2
    assert euromc.decimal_sign == ','
    assert euromc.grouping_sign == '\u202F'
    assert not euromc.international
    assert euromc.symbol == '€'
    assert not euromc.symbol_ahead
    assert euromc.symbol_separator == '\u00A0'
    assert euromc.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromc.__repr__() == (
        'EuroMC(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert euromc.__str__() == '-100,00 €'


def test_euromc_custom():
    """test_euromc_custom."""
    amount = 1000
    euromc = EuroMC(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euromc.amount == decimal
    assert euromc.numeric_code == '978'
    assert euromc.alpha_code == 'EUR'
    assert euromc.decimal_places == 5
    assert euromc.decimal_sign == '\u202F'
    assert euromc.grouping_sign == ','
    assert euromc.international
    assert euromc.symbol == '€'
    assert not euromc.symbol_ahead
    assert euromc.symbol_separator == '_'
    assert euromc.__hash__() == hash((decimal, 'EUR', '978'))
    assert euromc.__repr__() == (
        'EuroMC(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert euromc.__str__() == 'EUR 1,000.00000'


def test_euromc_changed():
    """test_ceuromc_changed."""
    euromc = EuroMC(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euromc.international = True


def test_euromc_math_add():
    """test_euromc_math_add."""
    euromc_one = EuroMC(amount=1)
    euromc_two = EuroMC(amount=2)
    euromc_three = EuroMC(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euromc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroMC\'> '
                   'and <class \'str\'>.')):
        _ = euromc_one.__add__('1.00')
    assert (
        euromc_one +
        euromc_two) == euromc_three


def test_euromc_slots():
    """test_euromc_slots."""
    euromc = EuroMC(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroMC\' '
                'object has no attribute \'new_variable\'')):
        euromc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
