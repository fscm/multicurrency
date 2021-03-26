# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lari representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Lari
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lari():
    """test_lari."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lari = Lari(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lari.amount == decimal
    assert lari.code == '981'
    assert lari.currency == 'GEL'
    assert lari.decimal_places == 2
    assert lari.decimal_sign == ','
    assert lari.grouping_sign == '.'
    assert not lari.international
    assert lari.symbol == 'ლ'
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: 0.1428571428571428571428571429, '
        'currency: "GEL", '
        'symbol: "ლ", '
        'code: "981", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert lari.__str__() == 'ლ0,14'


def test_lari_negative():
    """test_lari_negative."""
    amount = -100
    lari = Lari(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lari.code == '981'
    assert lari.currency == 'GEL'
    assert lari.decimal_places == 2
    assert lari.decimal_sign == ','
    assert lari.grouping_sign == '.'
    assert not lari.international
    assert lari.symbol == 'ლ'
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: -100, '
        'currency: "GEL", '
        'symbol: "ლ", '
        'code: "981", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert lari.__str__() == 'ლ-100,00'


def test_lari_custom():
    """test_lari_custom."""
    amount = 1000
    lari = Lari(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert lari.amount == decimal
    assert lari.code == '981'
    assert lari.currency == 'GEL'
    assert lari.decimal_places == 5
    assert lari.decimal_sign == '.'
    assert lari.grouping_sign == ','
    assert lari.international
    assert lari.symbol == 'ლ'
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: 1000, '
        'currency: "GEL", '
        'symbol: "ლ", '
        'code: "981", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert lari.__str__() == 'GEL 1,000.00000'


def test_lari_changed():
    """test_clari_changed."""
    lari = Lari(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.international = True


def test_lari_math_add():
    """test_lari_math_add."""
    lari_one = Lari(amount=1)
    lari_two = Lari(amount=2)
    lari_three = Lari(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GEL and OTHER.'):
        _ = lari_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lari.Lari\'> '
                   'and <class \'str\'>.')):
        _ = lari_one.__add__('1.00')
    assert (lari_one + lari_two) == lari_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Lari(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Lari\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
