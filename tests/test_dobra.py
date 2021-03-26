# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dobra representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Dobra
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_dobra():
    """test_dobra."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    dobra = Dobra(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dobra.amount == decimal
    assert dobra.code == '930'
    assert dobra.currency == 'STN'
    assert dobra.decimal_places == 2
    assert dobra.decimal_sign == ','
    assert dobra.grouping_sign == '.'
    assert not dobra.international
    assert dobra.symbol == 'Db'
    assert dobra.__hash__() == hash((decimal, 'STN', '930'))
    assert dobra.__repr__() == (
        'Dobra(amount: 0.1428571428571428571428571429, '
        'currency: "STN", '
        'symbol: "Db", '
        'code: "930", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert dobra.__str__() == 'Db0,14'


def test_dobra_negative():
    """test_dobra_negative."""
    amount = -100
    dobra = Dobra(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dobra.code == '930'
    assert dobra.currency == 'STN'
    assert dobra.decimal_places == 2
    assert dobra.decimal_sign == ','
    assert dobra.grouping_sign == '.'
    assert not dobra.international
    assert dobra.symbol == 'Db'
    assert dobra.__hash__() == hash((decimal, 'STN', '930'))
    assert dobra.__repr__() == (
        'Dobra(amount: -100, '
        'currency: "STN", '
        'symbol: "Db", '
        'code: "930", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert dobra.__str__() == 'Db-100,00'


def test_dobra_custom():
    """test_dobra_custom."""
    amount = 1000
    dobra = Dobra(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert dobra.amount == decimal
    assert dobra.code == '930'
    assert dobra.currency == 'STN'
    assert dobra.decimal_places == 5
    assert dobra.decimal_sign == '.'
    assert dobra.grouping_sign == ','
    assert dobra.international
    assert dobra.symbol == 'Db'
    assert dobra.__hash__() == hash((decimal, 'STN', '930'))
    assert dobra.__repr__() == (
        'Dobra(amount: 1000, '
        'currency: "STN", '
        'symbol: "Db", '
        'code: "930", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert dobra.__str__() == 'STN 1,000.00000'


def test_dobra_changed():
    """test_cdobra_changed."""
    dobra = Dobra(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dobra.international = True


def test_dobra_math_add():
    """test_dobra_math_add."""
    dobra_one = Dobra(amount=1)
    dobra_two = Dobra(amount=2)
    dobra_three = Dobra(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency STN and OTHER.'):
        _ = dobra_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dobra.Dobra\'> '
                   'and <class \'str\'>.')):
        _ = dobra_one.__add__('1.00')
    assert (dobra_one + dobra_two) == dobra_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Dobra(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Dobra\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
