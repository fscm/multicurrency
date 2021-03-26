# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pound Sterling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PoundSterling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pound_sterling():
    """test_pound_sterling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pound_sterling = PoundSterling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.amount == decimal
    assert pound_sterling.code == '826'
    assert pound_sterling.currency == 'GBP'
    assert pound_sterling.decimal_places == 2
    assert pound_sterling.decimal_sign == '.'
    assert pound_sterling.grouping_sign == ','
    assert not pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: 0.1428571428571428571428571429, '
        'currency: "GBP", '
        'symbol: "£", '
        'code: "826", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert pound_sterling.__str__() == '£0.14'


def test_pound_sterling_negative():
    """test_pound_sterling_negative."""
    amount = -100
    pound_sterling = PoundSterling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.code == '826'
    assert pound_sterling.currency == 'GBP'
    assert pound_sterling.decimal_places == 2
    assert pound_sterling.decimal_sign == '.'
    assert pound_sterling.grouping_sign == ','
    assert not pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: -100, '
        'currency: "GBP", '
        'symbol: "£", '
        'code: "826", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert pound_sterling.__str__() == '£-100.00'


def test_pound_sterling_custom():
    """test_pound_sterling_custom."""
    amount = 1000
    pound_sterling = PoundSterling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.amount == decimal
    assert pound_sterling.code == '826'
    assert pound_sterling.currency == 'GBP'
    assert pound_sterling.decimal_places == 5
    assert pound_sterling.decimal_sign == ','
    assert pound_sterling.grouping_sign == '.'
    assert pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: 1000, '
        'currency: "GBP", '
        'symbol: "£", '
        'code: "826", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert pound_sterling.__str__() == 'GBP 1.000,00000'


def test_pound_sterling_changed():
    """test_cpound_sterling_changed."""
    pound_sterling = PoundSterling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.international = True


def test_pound_sterling_math_add():
    """test_pound_sterling_math_add."""
    pound_sterling_one = PoundSterling(amount=1)
    pound_sterling_two = PoundSterling(amount=2)
    pound_sterling_three = PoundSterling(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GBP and OTHER.'):
        _ = pound_sterling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound_sterling.PoundSterling\'> '
                   'and <class \'str\'>.')):
        _ = pound_sterling_one.__add__('1.00')
    assert (pound_sterling_one + pound_sterling_two) == pound_sterling_three


def test_currency_slots():
    """test_currency_slots."""
    euro = PoundSterling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PoundSterling\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
