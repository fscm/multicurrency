# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nepalese Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NepaleseRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_nepalese_rupee():
    """test_nepalese_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    nepalese_rupee = NepaleseRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nepalese_rupee.amount == decimal
    assert nepalese_rupee.code == '524'
    assert nepalese_rupee.currency == 'NPR'
    assert nepalese_rupee.decimal_places == 2
    assert nepalese_rupee.decimal_sign == '.'
    assert nepalese_rupee.grouping_sign == ','
    assert not nepalese_rupee.international
    assert nepalese_rupee.symbol == '₨'
    assert nepalese_rupee.__hash__() == hash((decimal, 'NPR', '524'))
    assert nepalese_rupee.__repr__() == (
        'NepaleseRupee(amount: 0.1428571428571428571428571429, '
        'currency: "NPR", '
        'symbol: "₨", '
        'code: "524", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nepalese_rupee.__str__() == '₨0.14'


def test_nepalese_rupee_negative():
    """test_nepalese_rupee_negative."""
    amount = -100
    nepalese_rupee = NepaleseRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nepalese_rupee.code == '524'
    assert nepalese_rupee.currency == 'NPR'
    assert nepalese_rupee.decimal_places == 2
    assert nepalese_rupee.decimal_sign == '.'
    assert nepalese_rupee.grouping_sign == ','
    assert not nepalese_rupee.international
    assert nepalese_rupee.symbol == '₨'
    assert nepalese_rupee.__hash__() == hash((decimal, 'NPR', '524'))
    assert nepalese_rupee.__repr__() == (
        'NepaleseRupee(amount: -100, '
        'currency: "NPR", '
        'symbol: "₨", '
        'code: "524", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nepalese_rupee.__str__() == '₨-100.00'


def test_nepalese_rupee_custom():
    """test_nepalese_rupee_custom."""
    amount = 1000
    nepalese_rupee = NepaleseRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert nepalese_rupee.amount == decimal
    assert nepalese_rupee.code == '524'
    assert nepalese_rupee.currency == 'NPR'
    assert nepalese_rupee.decimal_places == 5
    assert nepalese_rupee.decimal_sign == ','
    assert nepalese_rupee.grouping_sign == '.'
    assert nepalese_rupee.international
    assert nepalese_rupee.symbol == '₨'
    assert nepalese_rupee.__hash__() == hash((decimal, 'NPR', '524'))
    assert nepalese_rupee.__repr__() == (
        'NepaleseRupee(amount: 1000, '
        'currency: "NPR", '
        'symbol: "₨", '
        'code: "524", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert nepalese_rupee.__str__() == 'NPR 1.000,00000'


def test_nepalese_rupee_changed():
    """test_cnepalese_rupee_changed."""
    nepalese_rupee = NepaleseRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nepalese_rupee.international = True


def test_nepalese_rupee_math_add():
    """test_nepalese_rupee_math_add."""
    nepalese_rupee_one = NepaleseRupee(amount=1)
    nepalese_rupee_two = NepaleseRupee(amount=2)
    nepalese_rupee_three = NepaleseRupee(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NPR and OTHER.'):
        _ = nepalese_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'nepalese_rupee.NepaleseRupee\'> '
                   'and <class \'str\'>.')):
        _ = nepalese_rupee_one.__add__('1.00')
    assert (nepalese_rupee_one + nepalese_rupee_two) == nepalese_rupee_three


def test_currency_slots():
    """test_currency_slots."""
    euro = NepaleseRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NepaleseRupee\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
