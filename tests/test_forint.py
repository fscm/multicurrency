# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Forint representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Forint
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_forint():
    """test_forint."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    forint = Forint(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert forint.amount == decimal
    assert forint.code == '348'
    assert forint.currency == 'HUF'
    assert forint.decimal_places == 0
    assert forint.decimal_sign == ','
    assert forint.grouping_sign == '.'
    assert not forint.international
    assert forint.symbol == 'Ft'
    assert forint.__hash__() == hash((decimal, 'HUF', '348'))
    assert forint.__repr__() == (
        'Forint(amount: 0.1428571428571428571428571429, '
        'currency: "HUF", '
        'symbol: "Ft", '
        'code: "348", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert forint.__str__() == 'Ft0'


def test_forint_negative():
    """test_forint_negative."""
    amount = -100
    forint = Forint(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert forint.code == '348'
    assert forint.currency == 'HUF'
    assert forint.decimal_places == 0
    assert forint.decimal_sign == ','
    assert forint.grouping_sign == '.'
    assert not forint.international
    assert forint.symbol == 'Ft'
    assert forint.__hash__() == hash((decimal, 'HUF', '348'))
    assert forint.__repr__() == (
        'Forint(amount: -100, '
        'currency: "HUF", '
        'symbol: "Ft", '
        'code: "348", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert forint.__str__() == 'Ft-100'


def test_forint_custom():
    """test_forint_custom."""
    amount = 1000
    forint = Forint(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert forint.amount == decimal
    assert forint.code == '348'
    assert forint.currency == 'HUF'
    assert forint.decimal_places == 5
    assert forint.decimal_sign == '.'
    assert forint.grouping_sign == ','
    assert forint.international
    assert forint.symbol == 'Ft'
    assert forint.__hash__() == hash((decimal, 'HUF', '348'))
    assert forint.__repr__() == (
        'Forint(amount: 1000, '
        'currency: "HUF", '
        'symbol: "Ft", '
        'code: "348", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert forint.__str__() == 'HUF 1,000.00000'


def test_forint_changed():
    """test_cforint_changed."""
    forint = Forint(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        forint.international = True


def test_forint_math_add():
    """test_forint_math_add."""
    forint_one = Forint(amount=1)
    forint_two = Forint(amount=2)
    forint_three = Forint(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency HUF and OTHER.'):
        _ = forint_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'forint.Forint\'> '
                   'and <class \'str\'>.')):
        _ = forint_one.__add__('1.00')
    assert (forint_one + forint_two) == forint_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Forint(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Forint\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
