# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Baht representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Baht
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_baht():
    """test_baht."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    baht = Baht(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert baht.amount == decimal
    assert baht.code == '764'
    assert baht.currency == 'THB'
    assert baht.decimal_places == 2
    assert baht.decimal_sign == '.'
    assert baht.grouping_sign == ','
    assert not baht.international
    assert baht.symbol == '฿'
    assert baht.__hash__() == hash((decimal, 'THB', '764'))
    assert baht.__repr__() == (
        'Baht(amount: 0.1428571428571428571428571429, '
        'currency: "THB", '
        'symbol: "฿", '
        'code: "764", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert baht.__str__() == '฿0.14'


def test_baht_negative():
    """test_baht_negative."""
    amount = -100
    baht = Baht(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert baht.code == '764'
    assert baht.currency == 'THB'
    assert baht.decimal_places == 2
    assert baht.decimal_sign == '.'
    assert baht.grouping_sign == ','
    assert not baht.international
    assert baht.symbol == '฿'
    assert baht.__hash__() == hash((decimal, 'THB', '764'))
    assert baht.__repr__() == (
        'Baht(amount: -100, '
        'currency: "THB", '
        'symbol: "฿", '
        'code: "764", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert baht.__str__() == '฿-100.00'


def test_baht_custom():
    """test_baht_custom."""
    amount = 1000
    baht = Baht(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert baht.amount == decimal
    assert baht.code == '764'
    assert baht.currency == 'THB'
    assert baht.decimal_places == 5
    assert baht.decimal_sign == ','
    assert baht.grouping_sign == '.'
    assert baht.international
    assert baht.symbol == '฿'
    assert baht.__hash__() == hash((decimal, 'THB', '764'))
    assert baht.__repr__() == (
        'Baht(amount: 1000, '
        'currency: "THB", '
        'symbol: "฿", '
        'code: "764", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert baht.__str__() == 'THB 1.000,00000'


def test_baht_changed():
    """test_cbaht_changed."""
    baht = Baht(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        baht.international = True


def test_baht_math_add():
    """test_baht_math_add."""
    baht_one = Baht(amount=1)
    baht_two = Baht(amount=2)
    baht_three = Baht(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency THB and OTHER.'):
        _ = baht_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'baht.Baht\'> '
                   'and <class \'str\'>.')):
        _ = baht_one.__add__('1.00')
    assert (baht_one + baht_two) == baht_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Baht(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Baht\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
