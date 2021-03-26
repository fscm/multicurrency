# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pakistan Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PakistanRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pakistan_rupee():
    """test_pakistan_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pakistan_rupee = PakistanRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.amount == decimal
    assert pakistan_rupee.code == '586'
    assert pakistan_rupee.currency == 'PKR'
    assert pakistan_rupee.decimal_places == 2
    assert pakistan_rupee.decimal_sign == '.'
    assert pakistan_rupee.grouping_sign == ','
    assert not pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: 0.1428571428571428571428571429, '
        'currency: "PKR", '
        'symbol: "₨", '
        'code: "586", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert pakistan_rupee.__str__() == '₨0.14'


def test_pakistan_rupee_negative():
    """test_pakistan_rupee_negative."""
    amount = -100
    pakistan_rupee = PakistanRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.code == '586'
    assert pakistan_rupee.currency == 'PKR'
    assert pakistan_rupee.decimal_places == 2
    assert pakistan_rupee.decimal_sign == '.'
    assert pakistan_rupee.grouping_sign == ','
    assert not pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: -100, '
        'currency: "PKR", '
        'symbol: "₨", '
        'code: "586", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert pakistan_rupee.__str__() == '₨-100.00'


def test_pakistan_rupee_custom():
    """test_pakistan_rupee_custom."""
    amount = 1000
    pakistan_rupee = PakistanRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.amount == decimal
    assert pakistan_rupee.code == '586'
    assert pakistan_rupee.currency == 'PKR'
    assert pakistan_rupee.decimal_places == 5
    assert pakistan_rupee.decimal_sign == ','
    assert pakistan_rupee.grouping_sign == '.'
    assert pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: 1000, '
        'currency: "PKR", '
        'symbol: "₨", '
        'code: "586", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert pakistan_rupee.__str__() == 'PKR 1.000,00000'


def test_pakistan_rupee_changed():
    """test_cpakistan_rupee_changed."""
    pakistan_rupee = PakistanRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.international = True


def test_pakistan_rupee_math_add():
    """test_pakistan_rupee_math_add."""
    pakistan_rupee_one = PakistanRupee(amount=1)
    pakistan_rupee_two = PakistanRupee(amount=2)
    pakistan_rupee_three = PakistanRupee(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PKR and OTHER.'):
        _ = pakistan_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pakistan_rupee.PakistanRupee\'> '
                   'and <class \'str\'>.')):
        _ = pakistan_rupee_one.__add__('1.00')
    assert (pakistan_rupee_one + pakistan_rupee_two) == pakistan_rupee_three


def test_currency_slots():
    """test_currency_slots."""
    euro = PakistanRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PakistanRupee\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
