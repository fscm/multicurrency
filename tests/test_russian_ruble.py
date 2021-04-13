# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Russian Ruble representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RussianRuble
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_russian_ruble():
    """test_russian_ruble."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    russian_ruble = RussianRuble(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert russian_ruble.amount == decimal
    assert russian_ruble.numeric_code == '643'
    assert russian_ruble.alpha_code == 'RUB'
    assert russian_ruble.decimal_places == 2
    assert russian_ruble.decimal_sign == ','
    assert russian_ruble.grouping_sign == '.'
    assert not russian_ruble.international
    assert russian_ruble.symbol == 'р.'
    assert russian_ruble.__hash__() == hash((decimal, 'RUB', '643'))
    assert russian_ruble.__repr__() == (
        'RussianRuble(amount: 0.1428571428571428571428571429, '
        'alpha_code: "RUB", '
        'symbol: "р.", '
        'numeric_code: "643", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert russian_ruble.__str__() == 'р.0,14'


def test_russian_ruble_negative():
    """test_russian_ruble_negative."""
    amount = -100
    russian_ruble = RussianRuble(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert russian_ruble.numeric_code == '643'
    assert russian_ruble.alpha_code == 'RUB'
    assert russian_ruble.decimal_places == 2
    assert russian_ruble.decimal_sign == ','
    assert russian_ruble.grouping_sign == '.'
    assert not russian_ruble.international
    assert russian_ruble.symbol == 'р.'
    assert russian_ruble.__hash__() == hash((decimal, 'RUB', '643'))
    assert russian_ruble.__repr__() == (
        'RussianRuble(amount: -100, '
        'alpha_code: "RUB", '
        'symbol: "р.", '
        'numeric_code: "643", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert russian_ruble.__str__() == 'р.-100,00'


def test_russian_ruble_custom():
    """test_russian_ruble_custom."""
    amount = 1000
    russian_ruble = RussianRuble(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert russian_ruble.amount == decimal
    assert russian_ruble.numeric_code == '643'
    assert russian_ruble.alpha_code == 'RUB'
    assert russian_ruble.decimal_places == 5
    assert russian_ruble.decimal_sign == '.'
    assert russian_ruble.grouping_sign == ','
    assert russian_ruble.international
    assert russian_ruble.symbol == 'р.'
    assert russian_ruble.__hash__() == hash((decimal, 'RUB', '643'))
    assert russian_ruble.__repr__() == (
        'RussianRuble(amount: 1000, '
        'alpha_code: "RUB", '
        'symbol: "р.", '
        'numeric_code: "643", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert russian_ruble.__str__() == 'RUB 1,000.00000'


def test_russian_ruble_changed():
    """test_crussian_ruble_changed."""
    russian_ruble = RussianRuble(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        russian_ruble.international = True


def test_russian_ruble_math_add():
    """test_russian_ruble_math_add."""
    russian_ruble_one = RussianRuble(amount=1)
    russian_ruble_two = RussianRuble(amount=2)
    russian_ruble_three = RussianRuble(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RUB and OTHER.'):
        _ = russian_ruble_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ruble.RussianRuble\'> '
                   'and <class \'str\'>.')):
        _ = russian_ruble_one.__add__('1.00')
    assert (russian_ruble_one + russian_ruble_two) == russian_ruble_three


def test_currency_slots():
    """test_currency_slots."""
    euro = RussianRuble(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RussianRuble\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
