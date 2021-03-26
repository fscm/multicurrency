# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pataca representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Pataca
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pataca():
    """test_pataca."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pataca = Pataca(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pataca.amount == decimal
    assert pataca.code == '446'
    assert pataca.currency == 'MOP'
    assert pataca.decimal_places == 2
    assert pataca.decimal_sign == ','
    assert pataca.grouping_sign == '.'
    assert not pataca.international
    assert pataca.symbol == 'P'
    assert pataca.__hash__() == hash((decimal, 'MOP', '446'))
    assert pataca.__repr__() == (
        'Pataca(amount: 0.1428571428571428571428571429, '
        'currency: "MOP", '
        'symbol: "P", '
        'code: "446", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pataca.__str__() == 'P0,14'


def test_pataca_negative():
    """test_pataca_negative."""
    amount = -100
    pataca = Pataca(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pataca.code == '446'
    assert pataca.currency == 'MOP'
    assert pataca.decimal_places == 2
    assert pataca.decimal_sign == ','
    assert pataca.grouping_sign == '.'
    assert not pataca.international
    assert pataca.symbol == 'P'
    assert pataca.__hash__() == hash((decimal, 'MOP', '446'))
    assert pataca.__repr__() == (
        'Pataca(amount: -100, '
        'currency: "MOP", '
        'symbol: "P", '
        'code: "446", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pataca.__str__() == 'P-100,00'


def test_pataca_custom():
    """test_pataca_custom."""
    amount = 1000
    pataca = Pataca(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert pataca.amount == decimal
    assert pataca.code == '446'
    assert pataca.currency == 'MOP'
    assert pataca.decimal_places == 5
    assert pataca.decimal_sign == '.'
    assert pataca.grouping_sign == ','
    assert pataca.international
    assert pataca.symbol == 'P'
    assert pataca.__hash__() == hash((decimal, 'MOP', '446'))
    assert pataca.__repr__() == (
        'Pataca(amount: 1000, '
        'currency: "MOP", '
        'symbol: "P", '
        'code: "446", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert pataca.__str__() == 'MOP 1,000.00000'


def test_pataca_changed():
    """test_cpataca_changed."""
    pataca = Pataca(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pataca.international = True


def test_pataca_math_add():
    """test_pataca_math_add."""
    pataca_one = Pataca(amount=1)
    pataca_two = Pataca(amount=2)
    pataca_three = Pataca(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MOP and OTHER.'):
        _ = pataca_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pataca.Pataca\'> '
                   'and <class \'str\'>.')):
        _ = pataca_one.__add__('1.00')
    assert (pataca_one + pataca_two) == pataca_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Pataca(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Pataca\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
