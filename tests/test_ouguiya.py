# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ouguiya representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Ouguiya
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ouguiya():
    """test_ouguiya."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ouguiya = Ouguiya(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.amount == decimal
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 2
    assert ouguiya.decimal_sign == ','
    assert ouguiya.grouping_sign == '.'
    assert not ouguiya.international
    assert ouguiya.symbol == 'UM'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MRU", '
        'symbol: "UM", '
        'numeric_code: "929", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ouguiya.__str__() == 'UM0,14'


def test_ouguiya_negative():
    """test_ouguiya_negative."""
    amount = -100
    ouguiya = Ouguiya(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 2
    assert ouguiya.decimal_sign == ','
    assert ouguiya.grouping_sign == '.'
    assert not ouguiya.international
    assert ouguiya.symbol == 'UM'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: -100, '
        'alpha_code: "MRU", '
        'symbol: "UM", '
        'numeric_code: "929", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ouguiya.__str__() == 'UM-100,00'


def test_ouguiya_custom():
    """test_ouguiya_custom."""
    amount = 1000
    ouguiya = Ouguiya(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.amount == decimal
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 5
    assert ouguiya.decimal_sign == '.'
    assert ouguiya.grouping_sign == ','
    assert ouguiya.international
    assert ouguiya.symbol == 'UM'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: 1000, '
        'alpha_code: "MRU", '
        'symbol: "UM", '
        'numeric_code: "929", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert ouguiya.__str__() == 'MRU 1,000.00000'


def test_ouguiya_changed():
    """test_couguiya_changed."""
    ouguiya = Ouguiya(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.international = True


def test_ouguiya_math_add():
    """test_ouguiya_math_add."""
    ouguiya_one = Ouguiya(amount=1)
    ouguiya_two = Ouguiya(amount=2)
    ouguiya_three = Ouguiya(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MRU and OTHER.'):
        _ = ouguiya_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ouguiya.Ouguiya\'> '
                   'and <class \'str\'>.')):
        _ = ouguiya_one.__add__('1.00')
    assert (ouguiya_one + ouguiya_two) == ouguiya_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Ouguiya(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Ouguiya\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
