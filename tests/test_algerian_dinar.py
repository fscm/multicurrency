# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Algerian Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, AlgerianDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_algerian_dinar():
    """test_algerian_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    algerian_dinar = AlgerianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert algerian_dinar.amount == decimal
    assert algerian_dinar.code == '012'
    assert algerian_dinar.currency == 'DZD'
    assert algerian_dinar.decimal_places == 2
    assert algerian_dinar.decimal_sign == ','
    assert algerian_dinar.grouping_sign == '.'
    assert not algerian_dinar.international
    assert algerian_dinar.symbol == 'د.ج'
    assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
    assert algerian_dinar.__repr__() == (
        'AlgerianDinar(amount: 0.1428571428571428571428571429, '
        'currency: "DZD", '
        'symbol: "د.ج", '
        'code: "012", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert algerian_dinar.__str__() == 'د.ج0,14'


def test_algerian_dinar_negative():
    """test_algerian_dinar_negative."""
    amount = -100
    algerian_dinar = AlgerianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert algerian_dinar.code == '012'
    assert algerian_dinar.currency == 'DZD'
    assert algerian_dinar.decimal_places == 2
    assert algerian_dinar.decimal_sign == ','
    assert algerian_dinar.grouping_sign == '.'
    assert not algerian_dinar.international
    assert algerian_dinar.symbol == 'د.ج'
    assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
    assert algerian_dinar.__repr__() == (
        'AlgerianDinar(amount: -100, '
        'currency: "DZD", '
        'symbol: "د.ج", '
        'code: "012", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert algerian_dinar.__str__() == 'د.ج-100,00'


def test_algerian_dinar_custom():
    """test_algerian_dinar_custom."""
    amount = 1000
    algerian_dinar = AlgerianDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert algerian_dinar.amount == decimal
    assert algerian_dinar.code == '012'
    assert algerian_dinar.currency == 'DZD'
    assert algerian_dinar.decimal_places == 5
    assert algerian_dinar.decimal_sign == '.'
    assert algerian_dinar.grouping_sign == ','
    assert algerian_dinar.international
    assert algerian_dinar.symbol == 'د.ج'
    assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
    assert algerian_dinar.__repr__() == (
        'AlgerianDinar(amount: 1000, '
        'currency: "DZD", '
        'symbol: "د.ج", '
        'code: "012", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert algerian_dinar.__str__() == 'DZD 1,000.00000'


def test_algerian_dinar_changed():
    """test_calgerian_dinar_changed."""
    algerian_dinar = AlgerianDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        algerian_dinar.international = True


def test_algerian_dinar_math_add():
    """test_algerian_dinar_math_add."""
    algerian_dinar_one = AlgerianDinar(amount=1)
    algerian_dinar_two = AlgerianDinar(amount=2)
    algerian_dinar_three = AlgerianDinar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DZD and OTHER.'):
        _ = algerian_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.AlgerianDinar\'> '
                   'and <class \'str\'>.')):
        _ = algerian_dinar_one.__add__('1.00')
    assert (algerian_dinar_one + algerian_dinar_two) == algerian_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = AlgerianDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'AlgerianDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
