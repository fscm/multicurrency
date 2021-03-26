# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Iraqi Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, IraqiDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_iraqi_dinar():
    """test_iraqi_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    iraqi_dinar = IraqiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iraqi_dinar.amount == decimal
    assert iraqi_dinar.code == '368'
    assert iraqi_dinar.currency == 'IQD'
    assert iraqi_dinar.decimal_places == 3
    assert iraqi_dinar.decimal_sign == ','
    assert iraqi_dinar.grouping_sign == '.'
    assert not iraqi_dinar.international
    assert iraqi_dinar.symbol == 'ع.د'
    assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
    assert iraqi_dinar.__repr__() == (
        'IraqiDinar(amount: 0.1428571428571428571428571429, '
        'currency: "IQD", '
        'symbol: "ع.د", '
        'code: "368", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert iraqi_dinar.__str__() == 'ع.د0,143'


def test_iraqi_dinar_negative():
    """test_iraqi_dinar_negative."""
    amount = -100
    iraqi_dinar = IraqiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iraqi_dinar.code == '368'
    assert iraqi_dinar.currency == 'IQD'
    assert iraqi_dinar.decimal_places == 3
    assert iraqi_dinar.decimal_sign == ','
    assert iraqi_dinar.grouping_sign == '.'
    assert not iraqi_dinar.international
    assert iraqi_dinar.symbol == 'ع.د'
    assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
    assert iraqi_dinar.__repr__() == (
        'IraqiDinar(amount: -100, '
        'currency: "IQD", '
        'symbol: "ع.د", '
        'code: "368", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert iraqi_dinar.__str__() == 'ع.د-100,000'


def test_iraqi_dinar_custom():
    """test_iraqi_dinar_custom."""
    amount = 1000
    iraqi_dinar = IraqiDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert iraqi_dinar.amount == decimal
    assert iraqi_dinar.code == '368'
    assert iraqi_dinar.currency == 'IQD'
    assert iraqi_dinar.decimal_places == 5
    assert iraqi_dinar.decimal_sign == '.'
    assert iraqi_dinar.grouping_sign == ','
    assert iraqi_dinar.international
    assert iraqi_dinar.symbol == 'ع.د'
    assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
    assert iraqi_dinar.__repr__() == (
        'IraqiDinar(amount: 1000, '
        'currency: "IQD", '
        'symbol: "ع.د", '
        'code: "368", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert iraqi_dinar.__str__() == 'IQD 1,000.00000'


def test_iraqi_dinar_changed():
    """test_ciraqi_dinar_changed."""
    iraqi_dinar = IraqiDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iraqi_dinar.international = True


def test_iraqi_dinar_math_add():
    """test_iraqi_dinar_math_add."""
    iraqi_dinar_one = IraqiDinar(amount=1)
    iraqi_dinar_two = IraqiDinar(amount=2)
    iraqi_dinar_three = IraqiDinar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency IQD and OTHER.'):
        _ = iraqi_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'iraqi_dinar.IraqiDinar\'> '
                   'and <class \'str\'>.')):
        _ = iraqi_dinar_one.__add__('1.00')
    assert (iraqi_dinar_one + iraqi_dinar_two) == iraqi_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = IraqiDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'IraqiDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
