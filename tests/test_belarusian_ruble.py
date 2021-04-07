# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Belarusian Ruble representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BelarusianRuble
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_belarusian_ruble():
    """test_belarusian_ruble."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    belarusian_ruble = BelarusianRuble(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert belarusian_ruble.amount == decimal
    assert belarusian_ruble.code == '933'
    assert belarusian_ruble.currency == 'BYN'
    assert belarusian_ruble.decimal_places == 2
    assert belarusian_ruble.decimal_sign == ','
    assert belarusian_ruble.grouping_sign == '.'
    assert not belarusian_ruble.international
    assert belarusian_ruble.symbol == 'Br'
    assert belarusian_ruble.__hash__() == hash((decimal, 'BYN', '933'))
    assert belarusian_ruble.__repr__() == (
        'BelarusianRuble(amount: 0.1428571428571428571428571429, '
        'currency: "BYN", '
        'symbol: "Br", '
        'code: "933", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert belarusian_ruble.__str__() == 'Br0,14'


def test_belarusian_ruble_negative():
    """test_belarusian_ruble_negative."""
    amount = -100
    belarusian_ruble = BelarusianRuble(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert belarusian_ruble.code == '933'
    assert belarusian_ruble.currency == 'BYN'
    assert belarusian_ruble.decimal_places == 2
    assert belarusian_ruble.decimal_sign == ','
    assert belarusian_ruble.grouping_sign == '.'
    assert not belarusian_ruble.international
    assert belarusian_ruble.symbol == 'Br'
    assert belarusian_ruble.__hash__() == hash((decimal, 'BYN', '933'))
    assert belarusian_ruble.__repr__() == (
        'BelarusianRuble(amount: -100, '
        'currency: "BYN", '
        'symbol: "Br", '
        'code: "933", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert belarusian_ruble.__str__() == 'Br-100,00'


def test_belarusian_ruble_custom():
    """test_belarusian_ruble_custom."""
    amount = 1000
    belarusian_ruble = BelarusianRuble(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert belarusian_ruble.amount == decimal
    assert belarusian_ruble.code == '933'
    assert belarusian_ruble.currency == 'BYN'
    assert belarusian_ruble.decimal_places == 5
    assert belarusian_ruble.decimal_sign == '.'
    assert belarusian_ruble.grouping_sign == ','
    assert belarusian_ruble.international
    assert belarusian_ruble.symbol == 'Br'
    assert belarusian_ruble.__hash__() == hash((decimal, 'BYN', '933'))
    assert belarusian_ruble.__repr__() == (
        'BelarusianRuble(amount: 1000, '
        'currency: "BYN", '
        'symbol: "Br", '
        'code: "933", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert belarusian_ruble.__str__() == 'BYN 1,000.00000'


def test_belarusian_ruble_changed():
    """test_cbelarusian_ruble_changed."""
    belarusian_ruble = BelarusianRuble(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        belarusian_ruble.international = True


def test_belarusian_ruble_math_add():
    """test_belarusian_ruble_math_add."""
    belarusian_ruble_one = BelarusianRuble(amount=1)
    belarusian_ruble_two = BelarusianRuble(amount=2)
    belarusian_ruble_three = BelarusianRuble(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BYN and OTHER.'):
        _ = belarusian_ruble_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ruble.BelarusianRuble\'> '
                   'and <class \'str\'>.')):
        _ = belarusian_ruble_one.__add__('1.00')
    assert (
        belarusian_ruble_one +
        belarusian_ruble_two) == belarusian_ruble_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BelarusianRuble(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BelarusianRuble\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
