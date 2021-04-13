# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kuwaiti Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, KuwaitiDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kuwaiti_dinar():
    """test_kuwaiti_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kuwaiti_dinar = KuwaitiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kuwaiti_dinar.amount == decimal
    assert kuwaiti_dinar.numeric_code == '414'
    assert kuwaiti_dinar.alpha_code == 'KWD'
    assert kuwaiti_dinar.decimal_places == 3
    assert kuwaiti_dinar.decimal_sign == '.'
    assert kuwaiti_dinar.grouping_sign == ','
    assert not kuwaiti_dinar.international
    assert kuwaiti_dinar.symbol == 'د.ك'
    assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
    assert kuwaiti_dinar.__repr__() == (
        'KuwaitiDinar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KWD", '
        'symbol: "د.ك", '
        'numeric_code: "414", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kuwaiti_dinar.__str__() == 'د.ك0.143'


def test_kuwaiti_dinar_negative():
    """test_kuwaiti_dinar_negative."""
    amount = -100
    kuwaiti_dinar = KuwaitiDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kuwaiti_dinar.numeric_code == '414'
    assert kuwaiti_dinar.alpha_code == 'KWD'
    assert kuwaiti_dinar.decimal_places == 3
    assert kuwaiti_dinar.decimal_sign == '.'
    assert kuwaiti_dinar.grouping_sign == ','
    assert not kuwaiti_dinar.international
    assert kuwaiti_dinar.symbol == 'د.ك'
    assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
    assert kuwaiti_dinar.__repr__() == (
        'KuwaitiDinar(amount: -100, '
        'alpha_code: "KWD", '
        'symbol: "د.ك", '
        'numeric_code: "414", '
        'decimal_places: "3", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kuwaiti_dinar.__str__() == 'د.ك-100.000'


def test_kuwaiti_dinar_custom():
    """test_kuwaiti_dinar_custom."""
    amount = 1000
    kuwaiti_dinar = KuwaitiDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kuwaiti_dinar.amount == decimal
    assert kuwaiti_dinar.numeric_code == '414'
    assert kuwaiti_dinar.alpha_code == 'KWD'
    assert kuwaiti_dinar.decimal_places == 5
    assert kuwaiti_dinar.decimal_sign == ','
    assert kuwaiti_dinar.grouping_sign == '.'
    assert kuwaiti_dinar.international
    assert kuwaiti_dinar.symbol == 'د.ك'
    assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
    assert kuwaiti_dinar.__repr__() == (
        'KuwaitiDinar(amount: 1000, '
        'alpha_code: "KWD", '
        'symbol: "د.ك", '
        'numeric_code: "414", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert kuwaiti_dinar.__str__() == 'KWD 1.000,00000'


def test_kuwaiti_dinar_changed():
    """test_ckuwaiti_dinar_changed."""
    kuwaiti_dinar = KuwaitiDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kuwaiti_dinar.international = True


def test_kuwaiti_dinar_math_add():
    """test_kuwaiti_dinar_math_add."""
    kuwaiti_dinar_one = KuwaitiDinar(amount=1)
    kuwaiti_dinar_two = KuwaitiDinar(amount=2)
    kuwaiti_dinar_three = KuwaitiDinar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KWD and OTHER.'):
        _ = kuwaiti_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.KuwaitiDinar\'> '
                   'and <class \'str\'>.')):
        _ = kuwaiti_dinar_one.__add__('1.00')
    assert (kuwaiti_dinar_one + kuwaiti_dinar_two) == kuwaiti_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = KuwaitiDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'KuwaitiDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
