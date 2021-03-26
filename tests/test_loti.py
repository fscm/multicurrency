# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Loti representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Loti
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_loti():
    """test_loti."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    loti = Loti(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert loti.amount == decimal
    assert loti.code == '426'
    assert loti.currency == 'LSL'
    assert loti.decimal_places == 2
    assert loti.decimal_sign == ','
    assert loti.grouping_sign == '.'
    assert not loti.international
    assert loti.symbol == 'L'
    assert loti.__hash__() == hash((decimal, 'LSL', '426'))
    assert loti.__repr__() == (
        'Loti(amount: 0.1428571428571428571428571429, '
        'currency: "LSL", '
        'symbol: "L", '
        'code: "426", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert loti.__str__() == 'L0,14'


def test_loti_negative():
    """test_loti_negative."""
    amount = -100
    loti = Loti(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert loti.code == '426'
    assert loti.currency == 'LSL'
    assert loti.decimal_places == 2
    assert loti.decimal_sign == ','
    assert loti.grouping_sign == '.'
    assert not loti.international
    assert loti.symbol == 'L'
    assert loti.__hash__() == hash((decimal, 'LSL', '426'))
    assert loti.__repr__() == (
        'Loti(amount: -100, '
        'currency: "LSL", '
        'symbol: "L", '
        'code: "426", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert loti.__str__() == 'L-100,00'


def test_loti_custom():
    """test_loti_custom."""
    amount = 1000
    loti = Loti(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert loti.amount == decimal
    assert loti.code == '426'
    assert loti.currency == 'LSL'
    assert loti.decimal_places == 5
    assert loti.decimal_sign == '.'
    assert loti.grouping_sign == ','
    assert loti.international
    assert loti.symbol == 'L'
    assert loti.__hash__() == hash((decimal, 'LSL', '426'))
    assert loti.__repr__() == (
        'Loti(amount: 1000, '
        'currency: "LSL", '
        'symbol: "L", '
        'code: "426", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert loti.__str__() == 'LSL 1,000.00000'


def test_loti_changed():
    """test_cloti_changed."""
    loti = Loti(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        loti.international = True


def test_loti_math_add():
    """test_loti_math_add."""
    loti_one = Loti(amount=1)
    loti_two = Loti(amount=2)
    loti_three = Loti(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LSL and OTHER.'):
        _ = loti_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'loti.Loti\'> '
                   'and <class \'str\'>.')):
        _ = loti_one.__add__('1.00')
    assert (loti_one + loti_two) == loti_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Loti(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Loti\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
