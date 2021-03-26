# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Gibraltar Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, GibraltarPound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_gibraltar_pound():
    """test_gibraltar_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    gibraltar_pound = GibraltarPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert gibraltar_pound.amount == decimal
    assert gibraltar_pound.code == '292'
    assert gibraltar_pound.currency == 'GIP'
    assert gibraltar_pound.decimal_places == 2
    assert gibraltar_pound.decimal_sign == ','
    assert gibraltar_pound.grouping_sign == '.'
    assert not gibraltar_pound.international
    assert gibraltar_pound.symbol == '£'
    assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
    assert gibraltar_pound.__repr__() == (
        'GibraltarPound(amount: 0.1428571428571428571428571429, '
        'currency: "GIP", '
        'symbol: "£", '
        'code: "292", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert gibraltar_pound.__str__() == '£0,14'


def test_gibraltar_pound_negative():
    """test_gibraltar_pound_negative."""
    amount = -100
    gibraltar_pound = GibraltarPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert gibraltar_pound.code == '292'
    assert gibraltar_pound.currency == 'GIP'
    assert gibraltar_pound.decimal_places == 2
    assert gibraltar_pound.decimal_sign == ','
    assert gibraltar_pound.grouping_sign == '.'
    assert not gibraltar_pound.international
    assert gibraltar_pound.symbol == '£'
    assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
    assert gibraltar_pound.__repr__() == (
        'GibraltarPound(amount: -100, '
        'currency: "GIP", '
        'symbol: "£", '
        'code: "292", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert gibraltar_pound.__str__() == '£-100,00'


def test_gibraltar_pound_custom():
    """test_gibraltar_pound_custom."""
    amount = 1000
    gibraltar_pound = GibraltarPound(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert gibraltar_pound.amount == decimal
    assert gibraltar_pound.code == '292'
    assert gibraltar_pound.currency == 'GIP'
    assert gibraltar_pound.decimal_places == 5
    assert gibraltar_pound.decimal_sign == '.'
    assert gibraltar_pound.grouping_sign == ','
    assert gibraltar_pound.international
    assert gibraltar_pound.symbol == '£'
    assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
    assert gibraltar_pound.__repr__() == (
        'GibraltarPound(amount: 1000, '
        'currency: "GIP", '
        'symbol: "£", '
        'code: "292", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert gibraltar_pound.__str__() == 'GIP 1,000.00000'


def test_gibraltar_pound_changed():
    """test_cgibraltar_pound_changed."""
    gibraltar_pound = GibraltarPound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gibraltar_pound.international = True


def test_gibraltar_pound_math_add():
    """test_gibraltar_pound_math_add."""
    gibraltar_pound_one = GibraltarPound(amount=1)
    gibraltar_pound_two = GibraltarPound(amount=2)
    gibraltar_pound_three = GibraltarPound(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GIP and OTHER.'):
        _ = gibraltar_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'gibraltar_pound.GibraltarPound\'> '
                   'and <class \'str\'>.')):
        _ = gibraltar_pound_one.__add__('1.00')
    assert (gibraltar_pound_one + gibraltar_pound_two) == gibraltar_pound_three


def test_currency_slots():
    """test_currency_slots."""
    euro = GibraltarPound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'GibraltarPound\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
