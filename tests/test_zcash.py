# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Zcash representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Zcash
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_zcash():
    """test_zcash."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    zcash = Zcash(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zcash.amount == decimal
    assert zcash.numeric_code == '0'
    assert zcash.alpha_code == 'ZEC'
    assert zcash.decimal_places == 8
    assert zcash.decimal_sign == '.'
    assert zcash.grouping_sign == ','
    assert not zcash.international
    assert zcash.symbol == 'ⓩ'
    assert zcash.symbol_ahead
    assert zcash.symbol_separator == ''
    assert zcash.convertion == ''
    assert zcash.__hash__() == hash((decimal, 'ZEC', '0'))
    assert zcash.__repr__() == (
        'Zcash(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ZEC", '
        'symbol: "ⓩ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "8", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert zcash.__str__() == 'ⓩ0.14285714'


def test_zcash_negative():
    """test_zcash_negative."""
    amount = -100
    zcash = Zcash(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zcash.numeric_code == '0'
    assert zcash.alpha_code == 'ZEC'
    assert zcash.decimal_places == 8
    assert zcash.decimal_sign == '.'
    assert zcash.grouping_sign == ','
    assert not zcash.international
    assert zcash.symbol == 'ⓩ'
    assert zcash.symbol_ahead
    assert zcash.symbol_separator == ''
    assert zcash.convertion == ''
    assert zcash.__hash__() == hash((decimal, 'ZEC', '0'))
    assert zcash.__repr__() == (
        'Zcash(amount: -100, '
        'alpha_code: "ZEC", '
        'symbol: "ⓩ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "8", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert zcash.__str__() == 'ⓩ-100.00000000'


def test_zcash_custom():
    """test_zcash_custom."""
    amount = 1000
    zcash = Zcash(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert zcash.amount == decimal
    assert zcash.numeric_code == '0'
    assert zcash.alpha_code == 'ZEC'
    assert zcash.decimal_places == 5
    assert zcash.decimal_sign == ','
    assert zcash.grouping_sign == '.'
    assert zcash.international
    assert zcash.symbol == 'ⓩ'
    assert not zcash.symbol_ahead
    assert zcash.symbol_separator == '_'
    assert zcash.convertion == ''
    assert zcash.__hash__() == hash((decimal, 'ZEC', '0'))
    assert zcash.__repr__() == (
        'Zcash(amount: 1000, '
        'alpha_code: "ZEC", '
        'symbol: "ⓩ", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert zcash.__str__() == 'ZEC 1,000.00000'


def test_zcash_changed():
    """test_czcash_changed."""
    zcash = Zcash(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zcash.international = True


def test_zcash_math_add():
    """test_zcash_math_add."""
    zcash_one = Zcash(amount=1)
    zcash_two = Zcash(amount=2)
    zcash_three = Zcash(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZEC and OTHER.'):
        _ = zcash_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Zcash\'> '
                   'and <class \'str\'>.')):
        _ = zcash_one.__add__('1.00')
    assert (
        zcash_one +
        zcash_two) == zcash_three


def test_zcash_slots():
    """test_zcash_slots."""
    zcash = Zcash(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Zcash\' '
                'object has no attribute \'new_variable\'')):
        zcash.new_variable = 'fail'  # pylint: disable=assigning-non-slot
