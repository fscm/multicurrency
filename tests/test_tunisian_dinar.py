# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tunisian Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, TunisianDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tunisian_dinar():
    """test_tunisian_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tunisian_dinar = TunisianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tunisian_dinar.amount == decimal
    assert tunisian_dinar.code == '788'
    assert tunisian_dinar.currency == 'TND'
    assert tunisian_dinar.decimal_places == 3
    assert tunisian_dinar.decimal_sign == ','
    assert tunisian_dinar.grouping_sign == '.'
    assert not tunisian_dinar.international
    assert tunisian_dinar.symbol == 'د.ت'
    assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
    assert tunisian_dinar.__repr__() == (
        'TunisianDinar(amount: 0.1428571428571428571428571429, '
        'currency: "TND", '
        'symbol: "د.ت", '
        'code: "788", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tunisian_dinar.__str__() == 'د.ت0,143'


def test_tunisian_dinar_negative():
    """test_tunisian_dinar_negative."""
    amount = -100
    tunisian_dinar = TunisianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tunisian_dinar.code == '788'
    assert tunisian_dinar.currency == 'TND'
    assert tunisian_dinar.decimal_places == 3
    assert tunisian_dinar.decimal_sign == ','
    assert tunisian_dinar.grouping_sign == '.'
    assert not tunisian_dinar.international
    assert tunisian_dinar.symbol == 'د.ت'
    assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
    assert tunisian_dinar.__repr__() == (
        'TunisianDinar(amount: -100, '
        'currency: "TND", '
        'symbol: "د.ت", '
        'code: "788", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tunisian_dinar.__str__() == 'د.ت-100,000'


def test_tunisian_dinar_custom():
    """test_tunisian_dinar_custom."""
    amount = 1000
    tunisian_dinar = TunisianDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert tunisian_dinar.amount == decimal
    assert tunisian_dinar.code == '788'
    assert tunisian_dinar.currency == 'TND'
    assert tunisian_dinar.decimal_places == 5
    assert tunisian_dinar.decimal_sign == '.'
    assert tunisian_dinar.grouping_sign == ','
    assert tunisian_dinar.international
    assert tunisian_dinar.symbol == 'د.ت'
    assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
    assert tunisian_dinar.__repr__() == (
        'TunisianDinar(amount: 1000, '
        'currency: "TND", '
        'symbol: "د.ت", '
        'code: "788", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert tunisian_dinar.__str__() == 'TND 1,000.00000'


def test_tunisian_dinar_changed():
    """test_ctunisian_dinar_changed."""
    tunisian_dinar = TunisianDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tunisian_dinar.international = True


def test_tunisian_dinar_math_add():
    """test_tunisian_dinar_math_add."""
    tunisian_dinar_one = TunisianDinar(amount=1)
    tunisian_dinar_two = TunisianDinar(amount=2)
    tunisian_dinar_three = TunisianDinar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TND and OTHER.'):
        _ = tunisian_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.TunisianDinar\'> '
                   'and <class \'str\'>.')):
        _ = tunisian_dinar_one.__add__('1.00')
    assert (tunisian_dinar_one + tunisian_dinar_two) == tunisian_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = TunisianDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'TunisianDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot