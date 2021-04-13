# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Jordanian Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, JordanianDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_jordanian_dinar():
    """test_jordanian_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    jordanian_dinar = JordanianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert jordanian_dinar.amount == decimal
    assert jordanian_dinar.numeric_code == '400'
    assert jordanian_dinar.alpha_code == 'JOD'
    assert jordanian_dinar.decimal_places == 3
    assert jordanian_dinar.decimal_sign == '.'
    assert jordanian_dinar.grouping_sign == ','
    assert not jordanian_dinar.international
    assert jordanian_dinar.symbol == 'د.ا'
    assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
    assert jordanian_dinar.__repr__() == (
        'JordanianDinar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "JOD", '
        'symbol: "د.ا", '
        'numeric_code: "400", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert jordanian_dinar.__str__() == 'د.ا0.143'


def test_jordanian_dinar_negative():
    """test_jordanian_dinar_negative."""
    amount = -100
    jordanian_dinar = JordanianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert jordanian_dinar.numeric_code == '400'
    assert jordanian_dinar.alpha_code == 'JOD'
    assert jordanian_dinar.decimal_places == 3
    assert jordanian_dinar.decimal_sign == '.'
    assert jordanian_dinar.grouping_sign == ','
    assert not jordanian_dinar.international
    assert jordanian_dinar.symbol == 'د.ا'
    assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
    assert jordanian_dinar.__repr__() == (
        'JordanianDinar(amount: -100, '
        'alpha_code: "JOD", '
        'symbol: "د.ا", '
        'numeric_code: "400", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert jordanian_dinar.__str__() == 'د.ا-100.000'


def test_jordanian_dinar_custom():
    """test_jordanian_dinar_custom."""
    amount = 1000
    jordanian_dinar = JordanianDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert jordanian_dinar.amount == decimal
    assert jordanian_dinar.numeric_code == '400'
    assert jordanian_dinar.alpha_code == 'JOD'
    assert jordanian_dinar.decimal_places == 5
    assert jordanian_dinar.decimal_sign == ','
    assert jordanian_dinar.grouping_sign == '.'
    assert jordanian_dinar.international
    assert jordanian_dinar.symbol == 'د.ا'
    assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
    assert jordanian_dinar.__repr__() == (
        'JordanianDinar(amount: 1000, '
        'alpha_code: "JOD", '
        'symbol: "د.ا", '
        'numeric_code: "400", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert jordanian_dinar.__str__() == 'JOD 1.000,00000'


def test_jordanian_dinar_changed():
    """test_cjordanian_dinar_changed."""
    jordanian_dinar = JordanianDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        jordanian_dinar.international = True


def test_jordanian_dinar_math_add():
    """test_jordanian_dinar_math_add."""
    jordanian_dinar_one = JordanianDinar(amount=1)
    jordanian_dinar_two = JordanianDinar(amount=2)
    jordanian_dinar_three = JordanianDinar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency JOD and OTHER.'):
        _ = jordanian_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.JordanianDinar\'> '
                   'and <class \'str\'>.')):
        _ = jordanian_dinar_one.__add__('1.00')
    assert (jordanian_dinar_one + jordanian_dinar_two) == jordanian_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = JordanianDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'JordanianDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
