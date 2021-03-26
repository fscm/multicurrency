# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Malaysian Ringgit representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MalaysianRinggit
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_malaysian_ringgit():
    """test_malaysian_ringgit."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    malaysian_ringgit = MalaysianRinggit(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malaysian_ringgit.amount == decimal
    assert malaysian_ringgit.code == '458'
    assert malaysian_ringgit.currency == 'MYR'
    assert malaysian_ringgit.decimal_places == 2
    assert malaysian_ringgit.decimal_sign == '.'
    assert malaysian_ringgit.grouping_sign == ','
    assert not malaysian_ringgit.international
    assert malaysian_ringgit.symbol == 'RM'
    assert malaysian_ringgit.__hash__() == hash((decimal, 'MYR', '458'))
    assert malaysian_ringgit.__repr__() == (
        'MalaysianRinggit(amount: 0.1428571428571428571428571429, '
        'currency: "MYR", '
        'symbol: "RM", '
        'code: "458", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert malaysian_ringgit.__str__() == 'RM0.14'


def test_malaysian_ringgit_negative():
    """test_malaysian_ringgit_negative."""
    amount = -100
    malaysian_ringgit = MalaysianRinggit(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malaysian_ringgit.code == '458'
    assert malaysian_ringgit.currency == 'MYR'
    assert malaysian_ringgit.decimal_places == 2
    assert malaysian_ringgit.decimal_sign == '.'
    assert malaysian_ringgit.grouping_sign == ','
    assert not malaysian_ringgit.international
    assert malaysian_ringgit.symbol == 'RM'
    assert malaysian_ringgit.__hash__() == hash((decimal, 'MYR', '458'))
    assert malaysian_ringgit.__repr__() == (
        'MalaysianRinggit(amount: -100, '
        'currency: "MYR", '
        'symbol: "RM", '
        'code: "458", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert malaysian_ringgit.__str__() == 'RM-100.00'


def test_malaysian_ringgit_custom():
    """test_malaysian_ringgit_custom."""
    amount = 1000
    malaysian_ringgit = MalaysianRinggit(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert malaysian_ringgit.amount == decimal
    assert malaysian_ringgit.code == '458'
    assert malaysian_ringgit.currency == 'MYR'
    assert malaysian_ringgit.decimal_places == 5
    assert malaysian_ringgit.decimal_sign == ','
    assert malaysian_ringgit.grouping_sign == '.'
    assert malaysian_ringgit.international
    assert malaysian_ringgit.symbol == 'RM'
    assert malaysian_ringgit.__hash__() == hash((decimal, 'MYR', '458'))
    assert malaysian_ringgit.__repr__() == (
        'MalaysianRinggit(amount: 1000, '
        'currency: "MYR", '
        'symbol: "RM", '
        'code: "458", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert malaysian_ringgit.__str__() == 'MYR 1.000,00000'


def test_malaysian_ringgit_changed():
    """test_cmalaysian_ringgit_changed."""
    malaysian_ringgit = MalaysianRinggit(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malaysian_ringgit.international = True


def test_malaysian_ringgit_math_add():
    """test_malaysian_ringgit_math_add."""
    malaysian_ringgit_one = MalaysianRinggit(amount=1)
    malaysian_ringgit_two = MalaysianRinggit(amount=2)
    malaysian_ringgit_three = MalaysianRinggit(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MYR and OTHER.'):
        _ = malaysian_ringgit_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'malaysian_ringgit.MalaysianRinggit\'> '
                   'and <class \'str\'>.')):
        _ = malaysian_ringgit_one.__add__('1.00')
    assert (
        malaysian_ringgit_one +
        malaysian_ringgit_two) == malaysian_ringgit_three


def test_currency_slots():
    """test_currency_slots."""
    euro = MalaysianRinggit(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MalaysianRinggit\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
