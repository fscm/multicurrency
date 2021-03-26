# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Costa Rican Colon representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CostaRicanColon
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_costa_rican_colon():
    """test_costa_rican_colon."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    costa_rican_colon = CostaRicanColon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert costa_rican_colon.amount == decimal
    assert costa_rican_colon.code == '188'
    assert costa_rican_colon.currency == 'CRC'
    assert costa_rican_colon.decimal_places == 2
    assert costa_rican_colon.decimal_sign == ','
    assert costa_rican_colon.grouping_sign == '.'
    assert not costa_rican_colon.international
    assert costa_rican_colon.symbol == '₡'
    assert costa_rican_colon.__hash__() == hash((decimal, 'CRC', '188'))
    assert costa_rican_colon.__repr__() == (
        'CostaRicanColon(amount: 0.1428571428571428571428571429, '
        'currency: "CRC", '
        'symbol: "₡", '
        'code: "188", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert costa_rican_colon.__str__() == '₡0,14'


def test_costa_rican_colon_negative():
    """test_costa_rican_colon_negative."""
    amount = -100
    costa_rican_colon = CostaRicanColon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert costa_rican_colon.code == '188'
    assert costa_rican_colon.currency == 'CRC'
    assert costa_rican_colon.decimal_places == 2
    assert costa_rican_colon.decimal_sign == ','
    assert costa_rican_colon.grouping_sign == '.'
    assert not costa_rican_colon.international
    assert costa_rican_colon.symbol == '₡'
    assert costa_rican_colon.__hash__() == hash((decimal, 'CRC', '188'))
    assert costa_rican_colon.__repr__() == (
        'CostaRicanColon(amount: -100, '
        'currency: "CRC", '
        'symbol: "₡", '
        'code: "188", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert costa_rican_colon.__str__() == '₡-100,00'


def test_costa_rican_colon_custom():
    """test_costa_rican_colon_custom."""
    amount = 1000
    costa_rican_colon = CostaRicanColon(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert costa_rican_colon.amount == decimal
    assert costa_rican_colon.code == '188'
    assert costa_rican_colon.currency == 'CRC'
    assert costa_rican_colon.decimal_places == 5
    assert costa_rican_colon.decimal_sign == '.'
    assert costa_rican_colon.grouping_sign == ','
    assert costa_rican_colon.international
    assert costa_rican_colon.symbol == '₡'
    assert costa_rican_colon.__hash__() == hash((decimal, 'CRC', '188'))
    assert costa_rican_colon.__repr__() == (
        'CostaRicanColon(amount: 1000, '
        'currency: "CRC", '
        'symbol: "₡", '
        'code: "188", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert costa_rican_colon.__str__() == 'CRC 1,000.00000'


def test_costa_rican_colon_changed():
    """test_ccosta_rican_colon_changed."""
    costa_rican_colon = CostaRicanColon(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        costa_rican_colon.international = True


def test_costa_rican_colon_math_add():
    """test_costa_rican_colon_math_add."""
    costa_rican_colon_one = CostaRicanColon(amount=1)
    costa_rican_colon_two = CostaRicanColon(amount=2)
    costa_rican_colon_three = CostaRicanColon(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CRC and OTHER.'):
        _ = costa_rican_colon_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'costa_rican_colon.CostaRicanColon\'> '
                   'and <class \'str\'>.')):
        _ = costa_rican_colon_one.__add__('1.00')
    assert (
        costa_rican_colon_one +
        costa_rican_colon_two) == costa_rican_colon_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CostaRicanColon(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CostaRicanColon\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
