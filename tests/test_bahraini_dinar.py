# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bahraini Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BahrainiDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bahraini_dinar():
    """test_bahraini_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bahraini_dinar = BahrainiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bahraini_dinar.amount == decimal
    assert bahraini_dinar.numeric_code == '048'
    assert bahraini_dinar.alpha_code == 'BHD'
    assert bahraini_dinar.decimal_places == 3
    assert bahraini_dinar.decimal_sign == '.'
    assert bahraini_dinar.grouping_sign == ','
    assert not bahraini_dinar.international
    assert bahraini_dinar.symbol == 'ب.د'
    assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
    assert bahraini_dinar.__repr__() == (
        'BahrainiDinar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BHD", '
        'symbol: "ب.د", '
        'numeric_code: "048", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert bahraini_dinar.__str__() == 'ب.د0.143'


def test_bahraini_dinar_negative():
    """test_bahraini_dinar_negative."""
    amount = -100
    bahraini_dinar = BahrainiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bahraini_dinar.numeric_code == '048'
    assert bahraini_dinar.alpha_code == 'BHD'
    assert bahraini_dinar.decimal_places == 3
    assert bahraini_dinar.decimal_sign == '.'
    assert bahraini_dinar.grouping_sign == ','
    assert not bahraini_dinar.international
    assert bahraini_dinar.symbol == 'ب.د'
    assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
    assert bahraini_dinar.__repr__() == (
        'BahrainiDinar(amount: -100, '
        'alpha_code: "BHD", '
        'symbol: "ب.د", '
        'numeric_code: "048", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert bahraini_dinar.__str__() == 'ب.د-100.000'


def test_bahraini_dinar_custom():
    """test_bahraini_dinar_custom."""
    amount = 1000
    bahraini_dinar = BahrainiDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert bahraini_dinar.amount == decimal
    assert bahraini_dinar.numeric_code == '048'
    assert bahraini_dinar.alpha_code == 'BHD'
    assert bahraini_dinar.decimal_places == 5
    assert bahraini_dinar.decimal_sign == ','
    assert bahraini_dinar.grouping_sign == '.'
    assert bahraini_dinar.international
    assert bahraini_dinar.symbol == 'ب.د'
    assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
    assert bahraini_dinar.__repr__() == (
        'BahrainiDinar(amount: 1000, '
        'alpha_code: "BHD", '
        'symbol: "ب.د", '
        'numeric_code: "048", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert bahraini_dinar.__str__() == 'BHD 1.000,00000'


def test_bahraini_dinar_changed():
    """test_cbahraini_dinar_changed."""
    bahraini_dinar = BahrainiDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bahraini_dinar.international = True


def test_bahraini_dinar_math_add():
    """test_bahraini_dinar_math_add."""
    bahraini_dinar_one = BahrainiDinar(amount=1)
    bahraini_dinar_two = BahrainiDinar(amount=2)
    bahraini_dinar_three = BahrainiDinar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BHD and OTHER.'):
        _ = bahraini_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.BahrainiDinar\'> '
                   'and <class \'str\'>.')):
        _ = bahraini_dinar_one.__add__('1.00')
    assert (bahraini_dinar_one + bahraini_dinar_two) == bahraini_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BahrainiDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BahrainiDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
