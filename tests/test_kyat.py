# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kyat representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kyat
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kyat():
    """test_kyat."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kyat = Kyat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kyat.amount == decimal
    assert kyat.code == '104'
    assert kyat.currency == 'MMK'
    assert kyat.decimal_places == 2
    assert kyat.decimal_sign == ','
    assert kyat.grouping_sign == '.'
    assert not kyat.international
    assert kyat.symbol == 'K'
    assert kyat.__hash__() == hash((decimal, 'MMK', '104'))
    assert kyat.__repr__() == (
        'Kyat(amount: 0.1428571428571428571428571429, '
        'currency: "MMK", '
        'symbol: "K", '
        'code: "104", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kyat.__str__() == 'K0,14'


def test_kyat_negative():
    """test_kyat_negative."""
    amount = -100
    kyat = Kyat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kyat.code == '104'
    assert kyat.currency == 'MMK'
    assert kyat.decimal_places == 2
    assert kyat.decimal_sign == ','
    assert kyat.grouping_sign == '.'
    assert not kyat.international
    assert kyat.symbol == 'K'
    assert kyat.__hash__() == hash((decimal, 'MMK', '104'))
    assert kyat.__repr__() == (
        'Kyat(amount: -100, '
        'currency: "MMK", '
        'symbol: "K", '
        'code: "104", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kyat.__str__() == 'K-100,00'


def test_kyat_custom():
    """test_kyat_custom."""
    amount = 1000
    kyat = Kyat(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kyat.amount == decimal
    assert kyat.code == '104'
    assert kyat.currency == 'MMK'
    assert kyat.decimal_places == 5
    assert kyat.decimal_sign == '.'
    assert kyat.grouping_sign == ','
    assert kyat.international
    assert kyat.symbol == 'K'
    assert kyat.__hash__() == hash((decimal, 'MMK', '104'))
    assert kyat.__repr__() == (
        'Kyat(amount: 1000, '
        'currency: "MMK", '
        'symbol: "K", '
        'code: "104", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert kyat.__str__() == 'MMK 1,000.00000'


def test_kyat_changed():
    """test_ckyat_changed."""
    kyat = Kyat(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kyat.international = True


def test_kyat_math_add():
    """test_kyat_math_add."""
    kyat_one = Kyat(amount=1)
    kyat_two = Kyat(amount=2)
    kyat_three = Kyat(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MMK and OTHER.'):
        _ = kyat_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kyat.Kyat\'> '
                   'and <class \'str\'>.')):
        _ = kyat_one.__add__('1.00')
    assert (kyat_one + kyat_two) == kyat_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Kyat(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kyat\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
