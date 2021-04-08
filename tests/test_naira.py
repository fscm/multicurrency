# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Naira representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Naira
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_naira():
    """test_naira."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    naira = Naira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert naira.amount == decimal
    assert naira.code == '566'
    assert naira.currency == 'NGN'
    assert naira.decimal_places == 2
    assert naira.decimal_sign == ','
    assert naira.grouping_sign == '.'
    assert not naira.international
    assert naira.symbol == '₦'
    assert naira.__hash__() == hash((decimal, 'NGN', '566'))
    assert naira.__repr__() == (
        'Naira(amount: 0.1428571428571428571428571429, '
        'currency: "NGN", '
        'symbol: "₦", '
        'code: "566", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert naira.__str__() == '₦0,14'


def test_naira_negative():
    """test_naira_negative."""
    amount = -100
    naira = Naira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert naira.code == '566'
    assert naira.currency == 'NGN'
    assert naira.decimal_places == 2
    assert naira.decimal_sign == ','
    assert naira.grouping_sign == '.'
    assert not naira.international
    assert naira.symbol == '₦'
    assert naira.__hash__() == hash((decimal, 'NGN', '566'))
    assert naira.__repr__() == (
        'Naira(amount: -100, '
        'currency: "NGN", '
        'symbol: "₦", '
        'code: "566", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert naira.__str__() == '₦-100,00'


def test_naira_custom():
    """test_naira_custom."""
    amount = 1000
    naira = Naira(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert naira.amount == decimal
    assert naira.code == '566'
    assert naira.currency == 'NGN'
    assert naira.decimal_places == 5
    assert naira.decimal_sign == '.'
    assert naira.grouping_sign == ','
    assert naira.international
    assert naira.symbol == '₦'
    assert naira.__hash__() == hash((decimal, 'NGN', '566'))
    assert naira.__repr__() == (
        'Naira(amount: 1000, '
        'currency: "NGN", '
        'symbol: "₦", '
        'code: "566", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert naira.__str__() == 'NGN 1,000.00000'


def test_naira_changed():
    """test_cnaira_changed."""
    naira = Naira(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        naira.international = True


def test_naira_math_add():
    """test_naira_math_add."""
    naira_one = Naira(amount=1)
    naira_two = Naira(amount=2)
    naira_three = Naira(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NGN and OTHER.'):
        _ = naira_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'naira.Naira\'> '
                   'and <class \'str\'>.')):
        _ = naira_one.__add__('1.00')
    assert (naira_one + naira_two) == naira_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Naira(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Naira\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot