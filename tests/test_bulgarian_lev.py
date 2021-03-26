# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bulgarian Lev representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BulgarianLev
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bulgarian_lev():
    """test_bulgarian_lev."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bulgarian_lev = BulgarianLev(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.amount == decimal
    assert bulgarian_lev.code == '975'
    assert bulgarian_lev.currency == 'BGN'
    assert bulgarian_lev.decimal_places == 2
    assert bulgarian_lev.decimal_sign == ','
    assert bulgarian_lev.grouping_sign == '.'
    assert not bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв'
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: 0.1428571428571428571428571429, '
        'currency: "BGN", '
        'symbol: "лв", '
        'code: "975", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert bulgarian_lev.__str__() == 'лв0,14'


def test_bulgarian_lev_negative():
    """test_bulgarian_lev_negative."""
    amount = -100
    bulgarian_lev = BulgarianLev(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.code == '975'
    assert bulgarian_lev.currency == 'BGN'
    assert bulgarian_lev.decimal_places == 2
    assert bulgarian_lev.decimal_sign == ','
    assert bulgarian_lev.grouping_sign == '.'
    assert not bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв'
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: -100, '
        'currency: "BGN", '
        'symbol: "лв", '
        'code: "975", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert bulgarian_lev.__str__() == 'лв-100,00'


def test_bulgarian_lev_custom():
    """test_bulgarian_lev_custom."""
    amount = 1000
    bulgarian_lev = BulgarianLev(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.amount == decimal
    assert bulgarian_lev.code == '975'
    assert bulgarian_lev.currency == 'BGN'
    assert bulgarian_lev.decimal_places == 5
    assert bulgarian_lev.decimal_sign == '.'
    assert bulgarian_lev.grouping_sign == ','
    assert bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв'
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: 1000, '
        'currency: "BGN", '
        'symbol: "лв", '
        'code: "975", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert bulgarian_lev.__str__() == 'BGN 1,000.00000'


def test_bulgarian_lev_changed():
    """test_cbulgarian_lev_changed."""
    bulgarian_lev = BulgarianLev(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.international = True


def test_bulgarian_lev_math_add():
    """test_bulgarian_lev_math_add."""
    bulgarian_lev_one = BulgarianLev(amount=1)
    bulgarian_lev_two = BulgarianLev(amount=2)
    bulgarian_lev_three = BulgarianLev(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BGN and OTHER.'):
        _ = bulgarian_lev_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'bulgarian_lev.BulgarianLev\'> '
                   'and <class \'str\'>.')):
        _ = bulgarian_lev_one.__add__('1.00')
    assert (bulgarian_lev_one + bulgarian_lev_two) == bulgarian_lev_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BulgarianLev(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BulgarianLev\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
