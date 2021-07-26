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
    assert south_korean_won.numeric_code == '410'
    assert south_korean_won.alpha_code == 'KRW'
    assert south_korean_won.decimal_places == 0
    assert south_korean_won.decimal_sign == '.'
    assert south_korean_won.grouping_places == 3
    assert south_korean_won.grouping_sign == ','
    assert not south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert south_korean_won.symbol_ahead
    assert south_korean_won.symbol_separator == ''
    assert south_korean_won.convertion == ''
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KRW", '
        'symbol: "₩", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "410", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert south_korean_won.__str__() == '₩0'


def test_south_korean_won_negative():
    """test_south_korean_won_negative."""
    amount = -100
    south_korean_won = SouthKoreanWon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert south_korean_won.numeric_code == '410'
    assert south_korean_won.alpha_code == 'KRW'
    assert south_korean_won.decimal_places == 0
    assert south_korean_won.decimal_sign == '.'
    assert south_korean_won.grouping_places == 3
    assert south_korean_won.grouping_sign == ','
    assert not south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert south_korean_won.symbol_ahead
    assert south_korean_won.symbol_separator == ''
    assert south_korean_won.convertion == ''
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: -100, '
        'alpha_code: "KRW", '
        'symbol: "₩", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "410", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert south_korean_won.__str__() == '₩-100'


def test_south_korean_won_custom():
    """test_south_korean_won_custom."""
    amount = 1000
    south_korean_won = SouthKoreanWon(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert south_korean_won.amount == decimal
    assert south_korean_won.numeric_code == '410'
    assert south_korean_won.alpha_code == 'KRW'
    assert south_korean_won.decimal_places == 5
    assert south_korean_won.decimal_sign == ','
    assert south_korean_won.grouping_places == 2
    assert south_korean_won.grouping_sign == '.'
    assert south_korean_won.international
    assert south_korean_won.symbol == '₩'
    assert not south_korean_won.symbol_ahead
    assert south_korean_won.symbol_separator == '_'
    assert south_korean_won.convertion == ''
    assert south_korean_won.__hash__() == hash((decimal, 'KRW', '410'))
    assert south_korean_won.__repr__() == (
        'SouthKoreanWon(amount: 1000, '
        'alpha_code: "KRW", '
        'symbol: "₩", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "410", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert south_korean_won.__str__() == 'KRW 10,00.00000'


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
        south_korean_won.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        south_korean_won.numeric_code = '978'
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
        south_korean_won.grouping_places = 4
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
    currency = Currency(amount=1, alpha_code='OTHER')
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


def test_south_korean_won_slots():
    """test_south_korean_won_slots."""
    south_korean_won = SouthKoreanWon(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SouthKoreanWon\' '
                'object has no attribute \'new_variable\'')):
        south_korean_won.new_variable = 'fail'  # pylint: disable=assigning-non-slot
