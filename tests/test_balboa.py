# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Balboa representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Balboa
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_balboa():
    """test_balboa."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    balboa = Balboa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert balboa.amount == decimal
    assert balboa.code == '590'
    assert balboa.currency == 'PAB'
    assert balboa.decimal_places == 2
    assert balboa.decimal_sign == ','
    assert balboa.grouping_sign == '.'
    assert not balboa.international
    assert balboa.symbol == 'B/.'
    assert balboa.__hash__() == hash((decimal, 'PAB', '590'))
    assert balboa.__repr__() == (
        'Balboa(amount: 0.1428571428571428571428571429, '
        'currency: "PAB", '
        'symbol: "B/.", '
        'code: "590", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert balboa.__str__() == 'B/.0,14'


def test_balboa_negative():
    """test_balboa_negative."""
    amount = -100
    balboa = Balboa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert balboa.code == '590'
    assert balboa.currency == 'PAB'
    assert balboa.decimal_places == 2
    assert balboa.decimal_sign == ','
    assert balboa.grouping_sign == '.'
    assert not balboa.international
    assert balboa.symbol == 'B/.'
    assert balboa.__hash__() == hash((decimal, 'PAB', '590'))
    assert balboa.__repr__() == (
        'Balboa(amount: -100, '
        'currency: "PAB", '
        'symbol: "B/.", '
        'code: "590", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert balboa.__str__() == 'B/.-100,00'


def test_balboa_custom():
    """test_balboa_custom."""
    amount = 1000
    balboa = Balboa(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert balboa.amount == decimal
    assert balboa.code == '590'
    assert balboa.currency == 'PAB'
    assert balboa.decimal_places == 5
    assert balboa.decimal_sign == '.'
    assert balboa.grouping_sign == ','
    assert balboa.international
    assert balboa.symbol == 'B/.'
    assert balboa.__hash__() == hash((decimal, 'PAB', '590'))
    assert balboa.__repr__() == (
        'Balboa(amount: 1000, '
        'currency: "PAB", '
        'symbol: "B/.", '
        'code: "590", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert balboa.__str__() == 'PAB 1,000.00000'


def test_balboa_changed():
    """test_cbalboa_changed."""
    balboa = Balboa(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        balboa.international = True


def test_balboa_math_add():
    """test_balboa_math_add."""
    balboa_one = Balboa(amount=1)
    balboa_two = Balboa(amount=2)
    balboa_three = Balboa(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PAB and OTHER.'):
        _ = balboa_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'balboa.Balboa\'> '
                   'and <class \'str\'>.')):
        _ = balboa_one.__add__('1.00')
    assert (balboa_one + balboa_two) == balboa_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Balboa(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Balboa\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
