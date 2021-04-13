# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Serbian Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SerbianDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_serbian_dinar():
    """test_serbian_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    serbian_dinar = SerbianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar.amount == decimal
    assert serbian_dinar.numeric_code == '941'
    assert serbian_dinar.alpha_code == 'RSD'
    assert serbian_dinar.decimal_places == 2
    assert serbian_dinar.decimal_sign == ','
    assert serbian_dinar.grouping_sign == '.'
    assert not serbian_dinar.international
    assert serbian_dinar.symbol == 'din'
    assert serbian_dinar.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar.__repr__() == (
        'SerbianDinar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "RSD", '
        'symbol: "din", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert serbian_dinar.__str__() == 'din0,14'


def test_serbian_dinar_negative():
    """test_serbian_dinar_negative."""
    amount = -100
    serbian_dinar = SerbianDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar.numeric_code == '941'
    assert serbian_dinar.alpha_code == 'RSD'
    assert serbian_dinar.decimal_places == 2
    assert serbian_dinar.decimal_sign == ','
    assert serbian_dinar.grouping_sign == '.'
    assert not serbian_dinar.international
    assert serbian_dinar.symbol == 'din'
    assert serbian_dinar.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar.__repr__() == (
        'SerbianDinar(amount: -100, '
        'alpha_code: "RSD", '
        'symbol: "din", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert serbian_dinar.__str__() == 'din-100,00'


def test_serbian_dinar_custom():
    """test_serbian_dinar_custom."""
    amount = 1000
    serbian_dinar = SerbianDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar.amount == decimal
    assert serbian_dinar.numeric_code == '941'
    assert serbian_dinar.alpha_code == 'RSD'
    assert serbian_dinar.decimal_places == 5
    assert serbian_dinar.decimal_sign == '.'
    assert serbian_dinar.grouping_sign == ','
    assert serbian_dinar.international
    assert serbian_dinar.symbol == 'din'
    assert serbian_dinar.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar.__repr__() == (
        'SerbianDinar(amount: 1000, '
        'alpha_code: "RSD", '
        'symbol: "din", '
        'numeric_code: "941", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert serbian_dinar.__str__() == 'RSD 1,000.00000'


def test_serbian_dinar_changed():
    """test_cserbian_dinar_changed."""
    serbian_dinar = SerbianDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar.international = True


def test_serbian_dinar_math_add():
    """test_serbian_dinar_math_add."""
    serbian_dinar_one = SerbianDinar(amount=1)
    serbian_dinar_two = SerbianDinar(amount=2)
    serbian_dinar_three = SerbianDinar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RSD and OTHER.'):
        _ = serbian_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.SerbianDinar\'> '
                   'and <class \'str\'>.')):
        _ = serbian_dinar_one.__add__('1.00')
    assert (serbian_dinar_one + serbian_dinar_two) == serbian_dinar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SerbianDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SerbianDinar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
