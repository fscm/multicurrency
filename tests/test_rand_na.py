# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand NA representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RandNA
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rand_na():
    """test_rand_na."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rand_na = RandNA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_na.amount == decimal
    assert rand_na.numeric_code == '710'
    assert rand_na.alpha_code == 'ZAR'
    assert rand_na.decimal_places == 2
    assert rand_na.decimal_sign == '.'
    assert rand_na.grouping_sign == '\u202F'
    assert not rand_na.international
    assert rand_na.symbol == 'R'
    assert rand_na.symbol_ahead
    assert rand_na.symbol_separator == '\u00A0'
    assert rand_na.convertion == ''
    assert rand_na.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_na.__repr__() == (
        'RandNA(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert rand_na.__str__() == 'R 0.14'


def test_rand_na_negative():
    """test_rand_na_negative."""
    amount = -100
    rand_na = RandNA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_na.numeric_code == '710'
    assert rand_na.alpha_code == 'ZAR'
    assert rand_na.decimal_places == 2
    assert rand_na.decimal_sign == '.'
    assert rand_na.grouping_sign == '\u202F'
    assert not rand_na.international
    assert rand_na.symbol == 'R'
    assert rand_na.symbol_ahead
    assert rand_na.symbol_separator == '\u00A0'
    assert rand_na.convertion == ''
    assert rand_na.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_na.__repr__() == (
        'RandNA(amount: -100, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert rand_na.__str__() == 'R -100.00'


def test_rand_na_custom():
    """test_rand_na_custom."""
    amount = 1000
    rand_na = RandNA(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert rand_na.amount == decimal
    assert rand_na.numeric_code == '710'
    assert rand_na.alpha_code == 'ZAR'
    assert rand_na.decimal_places == 5
    assert rand_na.decimal_sign == '\u202F'
    assert rand_na.grouping_sign == '.'
    assert rand_na.international
    assert rand_na.symbol == 'R'
    assert not rand_na.symbol_ahead
    assert rand_na.symbol_separator == '_'
    assert rand_na.convertion == ''
    assert rand_na.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_na.__repr__() == (
        'RandNA(amount: 1000, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "710", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert rand_na.__str__() == 'ZAR 1,000.00000'


def test_rand_na_changed():
    """test_crand_na_changed."""
    rand_na = RandNA(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_na.international = True


def test_rand_na_math_add():
    """test_rand_na_math_add."""
    rand_na_one = RandNA(amount=1)
    rand_na_two = RandNA(amount=2)
    rand_na_three = RandNA(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZAR and OTHER.'):
        _ = rand_na_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rand.RandNA\'> '
                   'and <class \'str\'>.')):
        _ = rand_na_one.__add__('1.00')
    assert (
        rand_na_one +
        rand_na_two) == rand_na_three


def test_rand_na_slots():
    """test_rand_na_slots."""
    rand_na = RandNA(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RandNA\' '
                'object has no attribute \'new_variable\'')):
        rand_na.new_variable = 'fail'  # pylint: disable=assigning-non-slot
