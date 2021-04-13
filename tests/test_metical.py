# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Metical representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Metical
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_metical():
    """test_metical."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    metical = Metical(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert metical.amount == decimal
    assert metical.numeric_code == '943'
    assert metical.alpha_code == 'MZN'
    assert metical.decimal_places == 0
    assert metical.decimal_sign == ','
    assert metical.grouping_sign == '.'
    assert not metical.international
    assert metical.symbol == 'MTn'
    assert metical.__hash__() == hash((decimal, 'MZN', '943'))
    assert metical.__repr__() == (
        'Metical(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MZN", '
        'symbol: "MTn", '
        'numeric_code: "943", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert metical.__str__() == 'MTn0'


def test_metical_negative():
    """test_metical_negative."""
    amount = -100
    metical = Metical(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert metical.numeric_code == '943'
    assert metical.alpha_code == 'MZN'
    assert metical.decimal_places == 0
    assert metical.decimal_sign == ','
    assert metical.grouping_sign == '.'
    assert not metical.international
    assert metical.symbol == 'MTn'
    assert metical.__hash__() == hash((decimal, 'MZN', '943'))
    assert metical.__repr__() == (
        'Metical(amount: -100, '
        'alpha_code: "MZN", '
        'symbol: "MTn", '
        'numeric_code: "943", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert metical.__str__() == 'MTn-100'


def test_metical_custom():
    """test_metical_custom."""
    amount = 1000
    metical = Metical(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert metical.amount == decimal
    assert metical.numeric_code == '943'
    assert metical.alpha_code == 'MZN'
    assert metical.decimal_places == 5
    assert metical.decimal_sign == '.'
    assert metical.grouping_sign == ','
    assert metical.international
    assert metical.symbol == 'MTn'
    assert metical.__hash__() == hash((decimal, 'MZN', '943'))
    assert metical.__repr__() == (
        'Metical(amount: 1000, '
        'alpha_code: "MZN", '
        'symbol: "MTn", '
        'numeric_code: "943", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert metical.__str__() == 'MZN 1,000.00000'


def test_metical_changed():
    """test_cmetical_changed."""
    metical = Metical(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        metical.international = True


def test_metical_math_add():
    """test_metical_math_add."""
    metical_one = Metical(amount=1)
    metical_two = Metical(amount=2)
    metical_three = Metical(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MZN and OTHER.'):
        _ = metical_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'metical.Metical\'> '
                   'and <class \'str\'>.')):
        _ = metical_one.__add__('1.00')
    assert (metical_one + metical_two) == metical_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Metical(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Metical\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
