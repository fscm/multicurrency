# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the North Korean Won representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NorthKoreanWon
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_north_korean_won():
    """test_north_korean_won."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    north_korean_won = NorthKoreanWon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert north_korean_won.amount == decimal
    assert north_korean_won.numeric_code == '408'
    assert north_korean_won.alpha_code == 'KPW'
    assert north_korean_won.decimal_places == 2
    assert north_korean_won.decimal_sign == '.'
    assert north_korean_won.grouping_places == 3
    assert north_korean_won.grouping_sign == ','
    assert not north_korean_won.international
    assert north_korean_won.symbol == '₩'
    assert north_korean_won.symbol_ahead
    assert north_korean_won.symbol_separator == '\u00A0'
    assert north_korean_won.convertion == ''
    assert north_korean_won.__hash__() == hash((decimal, 'KPW', '408'))
    assert north_korean_won.__repr__() == (
        'NorthKoreanWon(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KPW", '
        'symbol: "₩", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "408", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert north_korean_won.__str__() == '₩ 0.14'


def test_north_korean_won_negative():
    """test_north_korean_won_negative."""
    amount = -100
    north_korean_won = NorthKoreanWon(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert north_korean_won.numeric_code == '408'
    assert north_korean_won.alpha_code == 'KPW'
    assert north_korean_won.decimal_places == 2
    assert north_korean_won.decimal_sign == '.'
    assert north_korean_won.grouping_places == 3
    assert north_korean_won.grouping_sign == ','
    assert not north_korean_won.international
    assert north_korean_won.symbol == '₩'
    assert north_korean_won.symbol_ahead
    assert north_korean_won.symbol_separator == '\u00A0'
    assert north_korean_won.convertion == ''
    assert north_korean_won.__hash__() == hash((decimal, 'KPW', '408'))
    assert north_korean_won.__repr__() == (
        'NorthKoreanWon(amount: -100, '
        'alpha_code: "KPW", '
        'symbol: "₩", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "408", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert north_korean_won.__str__() == '₩ -100.00'


def test_north_korean_won_custom():
    """test_north_korean_won_custom."""
    amount = 1000
    north_korean_won = NorthKoreanWon(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert north_korean_won.amount == decimal
    assert north_korean_won.numeric_code == '408'
    assert north_korean_won.alpha_code == 'KPW'
    assert north_korean_won.decimal_places == 5
    assert north_korean_won.decimal_sign == ','
    assert north_korean_won.grouping_places == 2
    assert north_korean_won.grouping_sign == '.'
    assert north_korean_won.international
    assert north_korean_won.symbol == '₩'
    assert not north_korean_won.symbol_ahead
    assert north_korean_won.symbol_separator == '_'
    assert north_korean_won.convertion == ''
    assert north_korean_won.__hash__() == hash((decimal, 'KPW', '408'))
    assert north_korean_won.__repr__() == (
        'NorthKoreanWon(amount: 1000, '
        'alpha_code: "KPW", '
        'symbol: "₩", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "408", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert north_korean_won.__str__() == 'KPW 10,00.00000'


def test_north_korean_won_changed():
    """test_cnorth_korean_won_changed."""
    north_korean_won = NorthKoreanWon(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        north_korean_won.international = True


def test_north_korean_won_math_add():
    """test_north_korean_won_math_add."""
    north_korean_won_one = NorthKoreanWon(amount=1)
    north_korean_won_two = NorthKoreanWon(amount=2)
    north_korean_won_three = NorthKoreanWon(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KPW and OTHER.'):
        _ = north_korean_won_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'won.NorthKoreanWon\'> '
                   'and <class \'str\'>.')):
        _ = north_korean_won_one.__add__('1.00')
    assert (
        north_korean_won_one +
        north_korean_won_two) == north_korean_won_three


def test_north_korean_won_slots():
    """test_north_korean_won_slots."""
    north_korean_won = NorthKoreanWon(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NorthKoreanWon\' '
                'object has no attribute \'new_variable\'')):
        north_korean_won.new_variable = 'fail'  # pylint: disable=assigning-non-slot
