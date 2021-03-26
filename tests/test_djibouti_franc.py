# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Djibouti Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, DjiboutiFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_djibouti_franc():
    """test_djibouti_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    djibouti_franc = DjiboutiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.amount == decimal
    assert djibouti_franc.code == '262'
    assert djibouti_franc.currency == 'DJF'
    assert djibouti_franc.decimal_places == 0
    assert djibouti_franc.decimal_sign == ','
    assert djibouti_franc.grouping_sign == '.'
    assert not djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: 0.1428571428571428571428571429, '
        'currency: "DJF", '
        'symbol: "₣", '
        'code: "262", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert djibouti_franc.__str__() == '₣0'


def test_djibouti_franc_negative():
    """test_djibouti_franc_negative."""
    amount = -100
    djibouti_franc = DjiboutiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.code == '262'
    assert djibouti_franc.currency == 'DJF'
    assert djibouti_franc.decimal_places == 0
    assert djibouti_franc.decimal_sign == ','
    assert djibouti_franc.grouping_sign == '.'
    assert not djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: -100, '
        'currency: "DJF", '
        'symbol: "₣", '
        'code: "262", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert djibouti_franc.__str__() == '₣-100'


def test_djibouti_franc_custom():
    """test_djibouti_franc_custom."""
    amount = 1000
    djibouti_franc = DjiboutiFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.amount == decimal
    assert djibouti_franc.code == '262'
    assert djibouti_franc.currency == 'DJF'
    assert djibouti_franc.decimal_places == 5
    assert djibouti_franc.decimal_sign == '.'
    assert djibouti_franc.grouping_sign == ','
    assert djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: 1000, '
        'currency: "DJF", '
        'symbol: "₣", '
        'code: "262", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert djibouti_franc.__str__() == 'DJF 1,000.00000'


def test_djibouti_franc_changed():
    """test_cdjibouti_franc_changed."""
    djibouti_franc = DjiboutiFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.international = True


def test_djibouti_franc_math_add():
    """test_djibouti_franc_math_add."""
    djibouti_franc_one = DjiboutiFranc(amount=1)
    djibouti_franc_two = DjiboutiFranc(amount=2)
    djibouti_franc_three = DjiboutiFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DJF and OTHER.'):
        _ = djibouti_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'djibouti_franc.DjiboutiFranc\'> '
                   'and <class \'str\'>.')):
        _ = djibouti_franc_one.__add__('1.00')
    assert (djibouti_franc_one + djibouti_franc_two) == djibouti_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = DjiboutiFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'DjiboutiFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
