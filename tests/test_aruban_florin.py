# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Aruban Florin representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ArubanFlorin
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_aruban_florin():
    """test_aruban_florin."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    aruban_florin = ArubanFlorin(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert aruban_florin.amount == decimal
    assert aruban_florin.numeric_code == '533'
    assert aruban_florin.alpha_code == 'AWG'
    assert aruban_florin.decimal_places == 2
    assert aruban_florin.decimal_sign == '.'
    assert aruban_florin.grouping_sign == ','
    assert not aruban_florin.international
    assert aruban_florin.symbol == 'ƒ'
    assert aruban_florin.__hash__() == hash((decimal, 'AWG', '533'))
    assert aruban_florin.__repr__() == (
        'ArubanFlorin(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AWG", '
        'symbol: "ƒ", '
        'numeric_code: "533", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert aruban_florin.__str__() == 'ƒ0.14'


def test_aruban_florin_negative():
    """test_aruban_florin_negative."""
    amount = -100
    aruban_florin = ArubanFlorin(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert aruban_florin.numeric_code == '533'
    assert aruban_florin.alpha_code == 'AWG'
    assert aruban_florin.decimal_places == 2
    assert aruban_florin.decimal_sign == '.'
    assert aruban_florin.grouping_sign == ','
    assert not aruban_florin.international
    assert aruban_florin.symbol == 'ƒ'
    assert aruban_florin.__hash__() == hash((decimal, 'AWG', '533'))
    assert aruban_florin.__repr__() == (
        'ArubanFlorin(amount: -100, '
        'alpha_code: "AWG", '
        'symbol: "ƒ", '
        'numeric_code: "533", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert aruban_florin.__str__() == 'ƒ-100.00'


def test_aruban_florin_custom():
    """test_aruban_florin_custom."""
    amount = 1000
    aruban_florin = ArubanFlorin(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert aruban_florin.amount == decimal
    assert aruban_florin.numeric_code == '533'
    assert aruban_florin.alpha_code == 'AWG'
    assert aruban_florin.decimal_places == 5
    assert aruban_florin.decimal_sign == ','
    assert aruban_florin.grouping_sign == '.'
    assert aruban_florin.international
    assert aruban_florin.symbol == 'ƒ'
    assert aruban_florin.__hash__() == hash((decimal, 'AWG', '533'))
    assert aruban_florin.__repr__() == (
        'ArubanFlorin(amount: 1000, '
        'alpha_code: "AWG", '
        'symbol: "ƒ", '
        'numeric_code: "533", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert aruban_florin.__str__() == 'AWG 1.000,00000'


def test_aruban_florin_changed():
    """test_caruban_florin_changed."""
    aruban_florin = ArubanFlorin(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        aruban_florin.international = True


def test_aruban_florin_math_add():
    """test_aruban_florin_math_add."""
    aruban_florin_one = ArubanFlorin(amount=1)
    aruban_florin_two = ArubanFlorin(amount=2)
    aruban_florin_three = ArubanFlorin(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AWG and OTHER.'):
        _ = aruban_florin_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'florin.ArubanFlorin\'> '
                   'and <class \'str\'>.')):
        _ = aruban_florin_one.__add__('1.00')
    assert (aruban_florin_one + aruban_florin_two) == aruban_florin_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ArubanFlorin(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ArubanFlorin\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
