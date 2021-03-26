# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tenge representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Tenge
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tenge():
    """test_tenge."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tenge = Tenge(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.amount == decimal
    assert tenge.code == '398'
    assert tenge.currency == 'KZT'
    assert tenge.decimal_places == 2
    assert tenge.decimal_sign == ','
    assert tenge.grouping_sign == '.'
    assert not tenge.international
    assert tenge.symbol == '〒'
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: 0.1428571428571428571428571429, '
        'currency: "KZT", '
        'symbol: "〒", '
        'code: "398", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tenge.__str__() == '〒0,14'


def test_tenge_negative():
    """test_tenge_negative."""
    amount = -100
    tenge = Tenge(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.code == '398'
    assert tenge.currency == 'KZT'
    assert tenge.decimal_places == 2
    assert tenge.decimal_sign == ','
    assert tenge.grouping_sign == '.'
    assert not tenge.international
    assert tenge.symbol == '〒'
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: -100, '
        'currency: "KZT", '
        'symbol: "〒", '
        'code: "398", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tenge.__str__() == '〒-100,00'


def test_tenge_custom():
    """test_tenge_custom."""
    amount = 1000
    tenge = Tenge(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.amount == decimal
    assert tenge.code == '398'
    assert tenge.currency == 'KZT'
    assert tenge.decimal_places == 5
    assert tenge.decimal_sign == '.'
    assert tenge.grouping_sign == ','
    assert tenge.international
    assert tenge.symbol == '〒'
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: 1000, '
        'currency: "KZT", '
        'symbol: "〒", '
        'code: "398", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert tenge.__str__() == 'KZT 1,000.00000'


def test_tenge_changed():
    """test_ctenge_changed."""
    tenge = Tenge(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.international = True


def test_tenge_math_add():
    """test_tenge_math_add."""
    tenge_one = Tenge(amount=1)
    tenge_two = Tenge(amount=2)
    tenge_three = Tenge(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KZT and OTHER.'):
        _ = tenge_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'tenge.Tenge\'> '
                   'and <class \'str\'>.')):
        _ = tenge_one.__add__('1.00')
    assert (tenge_one + tenge_two) == tenge_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Tenge(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Tenge\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
