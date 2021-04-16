# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Saudi Riyal representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SaudiRiyal
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_saudi_riyal():
    """test_saudi_riyal."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    saudi_riyal = SaudiRiyal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert saudi_riyal.amount == decimal
    assert saudi_riyal.numeric_code == '682'
    assert saudi_riyal.alpha_code == 'SAR'
    assert saudi_riyal.decimal_places == 2
    assert saudi_riyal.decimal_sign == '.'
    assert saudi_riyal.grouping_sign == ','
    assert not saudi_riyal.international
    assert saudi_riyal.symbol == 'ر.س.'
    assert not saudi_riyal.symbol_ahead
    assert saudi_riyal.symbol_separator == '\u00A0'
    assert saudi_riyal.__hash__() == hash((decimal, 'SAR', '682'))
    assert saudi_riyal.__repr__() == (
        'SaudiRiyal(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SAR", '
        'symbol: "ر.س.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "682", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert saudi_riyal.__str__() == '0.14 ر.س.'


def test_saudi_riyal_negative():
    """test_saudi_riyal_negative."""
    amount = -100
    saudi_riyal = SaudiRiyal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert saudi_riyal.numeric_code == '682'
    assert saudi_riyal.alpha_code == 'SAR'
    assert saudi_riyal.decimal_places == 2
    assert saudi_riyal.decimal_sign == '.'
    assert saudi_riyal.grouping_sign == ','
    assert not saudi_riyal.international
    assert saudi_riyal.symbol == 'ر.س.'
    assert not saudi_riyal.symbol_ahead
    assert saudi_riyal.symbol_separator == '\u00A0'
    assert saudi_riyal.__hash__() == hash((decimal, 'SAR', '682'))
    assert saudi_riyal.__repr__() == (
        'SaudiRiyal(amount: -100, '
        'alpha_code: "SAR", '
        'symbol: "ر.س.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "682", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert saudi_riyal.__str__() == '-100.00 ر.س.'


def test_saudi_riyal_custom():
    """test_saudi_riyal_custom."""
    amount = 1000
    saudi_riyal = SaudiRiyal(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert saudi_riyal.amount == decimal
    assert saudi_riyal.numeric_code == '682'
    assert saudi_riyal.alpha_code == 'SAR'
    assert saudi_riyal.decimal_places == 5
    assert saudi_riyal.decimal_sign == ','
    assert saudi_riyal.grouping_sign == '.'
    assert saudi_riyal.international
    assert saudi_riyal.symbol == 'ر.س.'
    assert not saudi_riyal.symbol_ahead
    assert saudi_riyal.symbol_separator == '_'
    assert saudi_riyal.__hash__() == hash((decimal, 'SAR', '682'))
    assert saudi_riyal.__repr__() == (
        'SaudiRiyal(amount: 1000, '
        'alpha_code: "SAR", '
        'symbol: "ر.س.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "682", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert saudi_riyal.__str__() == 'SAR 1,000.00000'


def test_saudi_riyal_changed():
    """test_csaudi_riyal_changed."""
    saudi_riyal = SaudiRiyal(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saudi_riyal.international = True


def test_saudi_riyal_math_add():
    """test_saudi_riyal_math_add."""
    saudi_riyal_one = SaudiRiyal(amount=1)
    saudi_riyal_two = SaudiRiyal(amount=2)
    saudi_riyal_three = SaudiRiyal(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SAR and OTHER.'):
        _ = saudi_riyal_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'riyal.SaudiRiyal\'> '
                   'and <class \'str\'>.')):
        _ = saudi_riyal_one.__add__('1.00')
    assert (
        saudi_riyal_one +
        saudi_riyal_two) == saudi_riyal_three


def test_saudi_riyal_slots():
    """test_saudi_riyal_slots."""
    saudi_riyal = SaudiRiyal(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SaudiRiyal\' '
                'object has no attribute \'new_variable\'')):
        saudi_riyal.new_variable = 'fail'  # pylint: disable=assigning-non-slot
