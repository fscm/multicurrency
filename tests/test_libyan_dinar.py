# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Libyan Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, LibyanDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_libyan_dinar():
    """test_libyan_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    libyan_dinar = LibyanDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.amount == decimal
    assert libyan_dinar.code == '434'
    assert libyan_dinar.currency == 'LYD'
    assert libyan_dinar.decimal_places == 3
    assert libyan_dinar.decimal_sign == ','
    assert libyan_dinar.grouping_sign == '.'
    assert not libyan_dinar.international
    assert libyan_dinar.symbol == 'ل.د'
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: 0.1428571428571428571428571429, '
        'currency: "LYD", '
        'symbol: "ل.د", '
        'code: "434", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert libyan_dinar.__str__() == 'ل.د0,143'


def test_libyan_dinar_negative():
    """test_libyan_dinar_negative."""
    amount = -100
    libyan_dinar = LibyanDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.code == '434'
    assert libyan_dinar.currency == 'LYD'
    assert libyan_dinar.decimal_places == 3
    assert libyan_dinar.decimal_sign == ','
    assert libyan_dinar.grouping_sign == '.'
    assert not libyan_dinar.international
    assert libyan_dinar.symbol == 'ل.د'
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: -100, '
        'currency: "LYD", '
        'symbol: "ل.د", '
        'code: "434", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert libyan_dinar.__str__() == 'ل.د-100,000'


def test_libyan_dinar_custom():
    """test_libyan_dinar_custom."""
    amount = 1000
    libyan_dinar = LibyanDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.amount == decimal
    assert libyan_dinar.code == '434'
    assert libyan_dinar.currency == 'LYD'
    assert libyan_dinar.decimal_places == 5
    assert libyan_dinar.decimal_sign == '.'
    assert libyan_dinar.grouping_sign == ','
    assert libyan_dinar.international
    assert libyan_dinar.symbol == 'ل.د'
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: 1000, '
        'currency: "LYD", '
        'symbol: "ل.د", '
        'code: "434", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert libyan_dinar.__str__() == 'LYD 1,000.00000'


def test_libyan_dinar_changed():
    """test_clibyan_dinar_changed."""
    libyan_dinar = LibyanDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.international = True


def test_libyan_dinar_math_add():
    """test_libyan_dinar_math_add."""
    libyan_dinar_one = LibyanDinar(amount=1)
    libyan_dinar_two = LibyanDinar(amount=2)
    libyan_dinar_three = LibyanDinar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LYD and OTHER.'):
        _ = libyan_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.LibyanDinar\'> '
                   'and <class \'str\'>.')):
        _ = libyan_dinar_one.__add__('1.00')
    assert (libyan_dinar_one + libyan_dinar_two) == libyan_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = LibyanDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'LibyanDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
