# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Euro representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Euro
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euro():
    """test_euro."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euro = Euro(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euro.amount == decimal
    assert euro.code == '978'
    assert euro.currency == 'EUR'
    assert euro.decimal_places == 2
    assert euro.decimal_sign == ','
    assert euro.grouping_sign == '.'
    assert not euro.international
    assert euro.symbol == '€'
    assert euro.__hash__() == hash((decimal, 'EUR', '978'))
    assert euro.__repr__() == (
        'Euro(amount: 0.1428571428571428571428571429, '
        'currency: "EUR", '
        'symbol: "€", '
        'code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euro.__str__() == '€0,14'


def test_euro_negative():
    """test_euro_negative."""
    amount = -100
    euro = Euro(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euro.code == '978'
    assert euro.currency == 'EUR'
    assert euro.decimal_places == 2
    assert euro.decimal_sign == ','
    assert euro.grouping_sign == '.'
    assert not euro.international
    assert euro.symbol == '€'
    assert euro.__hash__() == hash((decimal, 'EUR', '978'))
    assert euro.__repr__() == (
        'Euro(amount: -100, '
        'currency: "EUR", '
        'symbol: "€", '
        'code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euro.__str__() == '€-100,00'


def test_euro_custom():
    """test_euro_custom."""
    amount = 1000
    euro = Euro(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert euro.amount == decimal
    assert euro.code == '978'
    assert euro.currency == 'EUR'
    assert euro.decimal_places == 5
    assert euro.decimal_sign == '.'
    assert euro.grouping_sign == ','
    assert euro.international
    assert euro.symbol == '€'
    assert euro.__hash__() == hash((decimal, 'EUR', '978'))
    assert euro.__repr__() == (
        'Euro(amount: 1000, '
        'currency: "EUR", '
        'symbol: "€", '
        'code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert euro.__str__() == 'EUR 1,000.00000'


def test_euro_changed():
    """test_ceuro_changed."""
    euro = Euro(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.international = True


def test_euro_math_add():
    """test_euro_math_add."""
    euro_one = Euro(amount=1)
    euro_two = Euro(amount=2)
    euro_three = Euro(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euro_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.Euro\'> '
                   'and <class \'str\'>.')):
        _ = euro_one.__add__('1.00')
    assert (euro_one + euro_two) == euro_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Euro(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Euro\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
