# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand ZA representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RandZA
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rand_za():
    """test_rand_za."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rand_za = RandZA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_za.amount == decimal
    assert rand_za.numeric_code == '710'
    assert rand_za.alpha_code == 'ZAR'
    assert rand_za.decimal_places == 2
    assert rand_za.decimal_sign == '.'
    assert rand_za.grouping_sign == '\u202F'
    assert not rand_za.international
    assert rand_za.symbol == 'R'
    assert rand_za.symbol_ahead
    assert rand_za.symbol_separator == '\u00A0'
    assert rand_za.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_za.__repr__() == (
        'RandZA(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert rand_za.__str__() == 'R 0.14'


def test_rand_za_negative():
    """test_rand_za_negative."""
    amount = -100
    rand_za = RandZA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_za.numeric_code == '710'
    assert rand_za.alpha_code == 'ZAR'
    assert rand_za.decimal_places == 2
    assert rand_za.decimal_sign == '.'
    assert rand_za.grouping_sign == '\u202F'
    assert not rand_za.international
    assert rand_za.symbol == 'R'
    assert rand_za.symbol_ahead
    assert rand_za.symbol_separator == '\u00A0'
    assert rand_za.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_za.__repr__() == (
        'RandZA(amount: -100, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert rand_za.__str__() == 'R -100.00'


def test_rand_za_custom():
    """test_rand_za_custom."""
    amount = 1000
    rand_za = RandZA(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert rand_za.amount == decimal
    assert rand_za.numeric_code == '710'
    assert rand_za.alpha_code == 'ZAR'
    assert rand_za.decimal_places == 5
    assert rand_za.decimal_sign == '\u202F'
    assert rand_za.grouping_sign == '.'
    assert rand_za.international
    assert rand_za.symbol == 'R'
    assert not rand_za.symbol_ahead
    assert rand_za.symbol_separator == '_'
    assert rand_za.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_za.__repr__() == (
        'RandZA(amount: 1000, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "710", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ".", '
        'international: True)')
    assert rand_za.__str__() == 'ZAR 1,000.00000'


def test_rand_za_changed():
    """test_crand_za_changed."""
    rand_za = RandZA(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_za.international = True


def test_rand_za_math_add():
    """test_rand_za_math_add."""
    rand_za_one = RandZA(amount=1)
    rand_za_two = RandZA(amount=2)
    rand_za_three = RandZA(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZAR and OTHER.'):
        _ = rand_za_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rand.RandZA\'> '
                   'and <class \'str\'>.')):
        _ = rand_za_one.__add__('1.00')
    assert (
        rand_za_one +
        rand_za_two) == rand_za_three


def test_rand_za_slots():
    """test_rand_za_slots."""
    rand_za = RandZA(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RandZA\' '
                'object has no attribute \'new_variable\'')):
        rand_za.new_variable = 'fail'  # pylint: disable=assigning-non-slot
