# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Rand
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rand():
    """test_rand."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rand = Rand(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand.amount == decimal
    assert rand.code == '710'
    assert rand.currency == 'ZAR'
    assert rand.decimal_places == 2
    assert rand.decimal_sign == '.'
    assert rand.grouping_sign == ' '
    assert not rand.international
    assert rand.symbol == 'R'
    assert rand.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand.__repr__() == (
        'Rand(amount: 0.1428571428571428571428571429, '
        'currency: "ZAR", '
        'symbol: "R", '
        'code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: " ", '
        'international: False)')
    assert rand.__str__() == 'R0.14'


def test_rand_negative():
    """test_rand_negative."""
    amount = -100
    rand = Rand(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand.code == '710'
    assert rand.currency == 'ZAR'
    assert rand.decimal_places == 2
    assert rand.decimal_sign == '.'
    assert rand.grouping_sign == ' '
    assert not rand.international
    assert rand.symbol == 'R'
    assert rand.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand.__repr__() == (
        'Rand(amount: -100, '
        'currency: "ZAR", '
        'symbol: "R", '
        'code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: " ", '
        'international: False)')
    assert rand.__str__() == 'R-100.00'


def test_rand_custom():
    """test_rand_custom."""
    amount = 1000
    rand = Rand(
        amount=amount,
        decimal_places=5,
        decimal_sign=' ',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert rand.amount == decimal
    assert rand.code == '710'
    assert rand.currency == 'ZAR'
    assert rand.decimal_places == 5
    assert rand.decimal_sign == ' '
    assert rand.grouping_sign == '.'
    assert rand.international
    assert rand.symbol == 'R'
    assert rand.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand.__repr__() == (
        'Rand(amount: 1000, '
        'currency: "ZAR", '
        'symbol: "R", '
        'code: "710", '
        'decimal_places: "5", '
        'decimal_sign: " ", '
        'grouping_sign: ".", '
        'international: True)')
    assert rand.__str__() == 'ZAR 1.000 00000'


def test_rand_changed():
    """test_crand_changed."""
    rand = Rand(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand.international = True


def test_rand_math_add():
    """test_rand_math_add."""
    rand_one = Rand(amount=1)
    rand_two = Rand(amount=2)
    rand_three = Rand(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZAR and OTHER.'):
        _ = rand_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rand.Rand\'> '
                   'and <class \'str\'>.')):
        _ = rand_one.__add__('1.00')
    assert (rand_one + rand_two) == rand_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Rand(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Rand\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
