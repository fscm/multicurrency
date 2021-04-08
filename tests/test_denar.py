# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Denar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Denar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_denar():
    """test_denar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    denar = Denar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert denar.amount == decimal
    assert denar.code == '807'
    assert denar.currency == 'MKD'
    assert denar.decimal_places == 2
    assert denar.decimal_sign == '.'
    assert denar.grouping_sign == ','
    assert not denar.international
    assert denar.symbol == 'ден'
    assert denar.__hash__() == hash((decimal, 'MKD', '807'))
    assert denar.__repr__() == (
        'Denar(amount: 0.1428571428571428571428571429, '
        'currency: "MKD", '
        'symbol: "ден", '
        'code: "807", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert denar.__str__() == 'ден0.14'


def test_denar_negative():
    """test_denar_negative."""
    amount = -100
    denar = Denar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert denar.code == '807'
    assert denar.currency == 'MKD'
    assert denar.decimal_places == 2
    assert denar.decimal_sign == '.'
    assert denar.grouping_sign == ','
    assert not denar.international
    assert denar.symbol == 'ден'
    assert denar.__hash__() == hash((decimal, 'MKD', '807'))
    assert denar.__repr__() == (
        'Denar(amount: -100, '
        'currency: "MKD", '
        'symbol: "ден", '
        'code: "807", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert denar.__str__() == 'ден-100.00'


def test_denar_custom():
    """test_denar_custom."""
    amount = 1000
    denar = Denar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert denar.amount == decimal
    assert denar.code == '807'
    assert denar.currency == 'MKD'
    assert denar.decimal_places == 5
    assert denar.decimal_sign == ','
    assert denar.grouping_sign == '.'
    assert denar.international
    assert denar.symbol == 'ден'
    assert denar.__hash__() == hash((decimal, 'MKD', '807'))
    assert denar.__repr__() == (
        'Denar(amount: 1000, '
        'currency: "MKD", '
        'symbol: "ден", '
        'code: "807", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert denar.__str__() == 'MKD 1.000,00000'


def test_denar_changed():
    """test_cdenar_changed."""
    denar = Denar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        denar.international = True


def test_denar_math_add():
    """test_denar_math_add."""
    denar_one = Denar(amount=1)
    denar_two = Denar(amount=2)
    denar_three = Denar(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MKD and OTHER.'):
        _ = denar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'denar.Denar\'> '
                   'and <class \'str\'>.')):
        _ = denar_one.__add__('1.00')
    assert (denar_one + denar_two) == denar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Denar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Denar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot