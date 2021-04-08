# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Hryvnia representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Hryvnia
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_hryvnia():
    """test_hryvnia."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    hryvnia = Hryvnia(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert hryvnia.amount == decimal
    assert hryvnia.code == '980'
    assert hryvnia.currency == 'UAH'
    assert hryvnia.decimal_places == 2
    assert hryvnia.decimal_sign == ','
    assert hryvnia.grouping_sign == '.'
    assert not hryvnia.international
    assert hryvnia.symbol == '₴'
    assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
    assert hryvnia.__repr__() == (
        'Hryvnia(amount: 0.1428571428571428571428571429, '
        'currency: "UAH", '
        'symbol: "₴", '
        'code: "980", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert hryvnia.__str__() == '₴0,14'


def test_hryvnia_negative():
    """test_hryvnia_negative."""
    amount = -100
    hryvnia = Hryvnia(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert hryvnia.code == '980'
    assert hryvnia.currency == 'UAH'
    assert hryvnia.decimal_places == 2
    assert hryvnia.decimal_sign == ','
    assert hryvnia.grouping_sign == '.'
    assert not hryvnia.international
    assert hryvnia.symbol == '₴'
    assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
    assert hryvnia.__repr__() == (
        'Hryvnia(amount: -100, '
        'currency: "UAH", '
        'symbol: "₴", '
        'code: "980", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert hryvnia.__str__() == '₴-100,00'


def test_hryvnia_custom():
    """test_hryvnia_custom."""
    amount = 1000
    hryvnia = Hryvnia(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert hryvnia.amount == decimal
    assert hryvnia.code == '980'
    assert hryvnia.currency == 'UAH'
    assert hryvnia.decimal_places == 5
    assert hryvnia.decimal_sign == '.'
    assert hryvnia.grouping_sign == ','
    assert hryvnia.international
    assert hryvnia.symbol == '₴'
    assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
    assert hryvnia.__repr__() == (
        'Hryvnia(amount: 1000, '
        'currency: "UAH", '
        'symbol: "₴", '
        'code: "980", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert hryvnia.__str__() == 'UAH 1,000.00000'


def test_hryvnia_changed():
    """test_chryvnia_changed."""
    hryvnia = Hryvnia(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        hryvnia.international = True


def test_hryvnia_math_add():
    """test_hryvnia_math_add."""
    hryvnia_one = Hryvnia(amount=1)
    hryvnia_two = Hryvnia(amount=2)
    hryvnia_three = Hryvnia(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency UAH and OTHER.'):
        _ = hryvnia_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'hryvnia.Hryvnia\'> '
                   'and <class \'str\'>.')):
        _ = hryvnia_one.__add__('1.00')
    assert (hryvnia_one + hryvnia_two) == hryvnia_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Hryvnia(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Hryvnia\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot