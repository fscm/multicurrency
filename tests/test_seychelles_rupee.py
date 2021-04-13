# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Seychelles Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SeychellesRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_seychelles_rupee():
    """test_seychelles_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    seychelles_rupee = SeychellesRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert seychelles_rupee.amount == decimal
    assert seychelles_rupee.numeric_code == '690'
    assert seychelles_rupee.alpha_code == 'SCR'
    assert seychelles_rupee.decimal_places == 2
    assert seychelles_rupee.decimal_sign == ','
    assert seychelles_rupee.grouping_sign == '.'
    assert not seychelles_rupee.international
    assert seychelles_rupee.symbol == '₨'
    assert seychelles_rupee.__hash__() == hash((decimal, 'SCR', '690'))
    assert seychelles_rupee.__repr__() == (
        'SeychellesRupee(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SCR", '
        'symbol: "₨", '
        'numeric_code: "690", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert seychelles_rupee.__str__() == '₨0,14'


def test_seychelles_rupee_negative():
    """test_seychelles_rupee_negative."""
    amount = -100
    seychelles_rupee = SeychellesRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert seychelles_rupee.numeric_code == '690'
    assert seychelles_rupee.alpha_code == 'SCR'
    assert seychelles_rupee.decimal_places == 2
    assert seychelles_rupee.decimal_sign == ','
    assert seychelles_rupee.grouping_sign == '.'
    assert not seychelles_rupee.international
    assert seychelles_rupee.symbol == '₨'
    assert seychelles_rupee.__hash__() == hash((decimal, 'SCR', '690'))
    assert seychelles_rupee.__repr__() == (
        'SeychellesRupee(amount: -100, '
        'alpha_code: "SCR", '
        'symbol: "₨", '
        'numeric_code: "690", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert seychelles_rupee.__str__() == '₨-100,00'


def test_seychelles_rupee_custom():
    """test_seychelles_rupee_custom."""
    amount = 1000
    seychelles_rupee = SeychellesRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert seychelles_rupee.amount == decimal
    assert seychelles_rupee.numeric_code == '690'
    assert seychelles_rupee.alpha_code == 'SCR'
    assert seychelles_rupee.decimal_places == 5
    assert seychelles_rupee.decimal_sign == '.'
    assert seychelles_rupee.grouping_sign == ','
    assert seychelles_rupee.international
    assert seychelles_rupee.symbol == '₨'
    assert seychelles_rupee.__hash__() == hash((decimal, 'SCR', '690'))
    assert seychelles_rupee.__repr__() == (
        'SeychellesRupee(amount: 1000, '
        'alpha_code: "SCR", '
        'symbol: "₨", '
        'numeric_code: "690", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert seychelles_rupee.__str__() == 'SCR 1,000.00000'


def test_seychelles_rupee_changed():
    """test_cseychelles_rupee_changed."""
    seychelles_rupee = SeychellesRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        seychelles_rupee.international = True


def test_seychelles_rupee_math_add():
    """test_seychelles_rupee_math_add."""
    seychelles_rupee_one = SeychellesRupee(amount=1)
    seychelles_rupee_two = SeychellesRupee(amount=2)
    seychelles_rupee_three = SeychellesRupee(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SCR and OTHER.'):
        _ = seychelles_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupee.SeychellesRupee\'> '
                   'and <class \'str\'>.')):
        _ = seychelles_rupee_one.__add__('1.00')
    assert (seychelles_rupee_one + seychelles_rupee_two) == seychelles_rupee_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SeychellesRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SeychellesRupee\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
