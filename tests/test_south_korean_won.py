# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the South Korean Won representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SouthKoreanWon
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_south_korean_won():
    """test_south_korean_won."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    south_korean_won = SouthKoreanWon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert south_korean_won.amount == decimal
    assert south_korean_won.code == '410'
    assert south_korean_won.currency == 'KRW'
    assert south_korean_won.decimal_places == 0
    assert south_korean_won.decimal_sign == '.'
    assert south_korean_won.grouping_sign == ','
    assert not south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: 0.1428571428571428571428571429, '
        'currency: "KRW", '
        'symbol: "₩", '
        'code: "410", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert south_korean_won.__str__() == '₩0'


def test_south_korean_won_negative():
    """test_south_korean_won_negative."""
    amount = -100
    south_korean_won = SouthKoreanWon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert south_korean_won.code == '410'
    assert south_korean_won.currency == 'KRW'
    assert south_korean_won.decimal_places == 0
    assert south_korean_won.decimal_sign == '.'
    assert south_korean_won.grouping_sign == ','
    assert not south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: -100, '
        'currency: "KRW", '
        'symbol: "₩", '
        'code: "410", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert south_korean_won.__str__() == '₩-100'


def test_south_korean_won_custom():
    """test_south_korean_won_custom."""
    amount = 1000
    south_korean_won = SouthKoreanWon(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert south_korean_won.amount == decimal
    assert south_korean_won.code == '410'
    assert south_korean_won.currency == 'KRW'
    assert south_korean_won.decimal_places == 5
    assert south_korean_won.decimal_sign == ','
    assert south_korean_won.grouping_sign == '.'
    assert south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: 1000, '
        'currency: "KRW", '
        'symbol: "₩", '
        'code: "410", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert south_korean_won.__str__() == 'KRW 1.000,00000'


def test_south_korean_won_changed():
    """test_csouth_korean_won_changed."""
    south_korean_won = SouthKoreanWon(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.international = True


def test_south_korean_won_math_add():
    """test_south_korean_won_math_add."""
    south_korean_won_one = SouthKoreanWon(amount=1)
    south_korean_won_two = SouthKoreanWon(amount=2)
    south_korean_won_three = SouthKoreanWon(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KRW and OTHER.'):
        _ = south_korean_won_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'won.SouthKoreanWon\'> '
                   'and <class \'str\'>.')):
        _ = south_korean_won_one.__add__('1.00')
    assert (
        south_korean_won_one +
        south_korean_won_two) == south_korean_won_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SouthKoreanWon(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SouthKoreanWon\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
