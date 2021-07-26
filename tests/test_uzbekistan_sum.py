# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Uzbekistan Sum representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, UzbekistanSum
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_uzbekistan_sum():
    """test_uzbekistan_sum."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    uzbekistan_sum = UzbekistanSum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.amount == decimal
    assert uzbekistan_sum.numeric_code == '860'
    assert uzbekistan_sum.alpha_code == 'UZS'
    assert uzbekistan_sum.decimal_places == 2
    assert uzbekistan_sum.decimal_sign == ','
    assert uzbekistan_sum.grouping_places == 3
    assert uzbekistan_sum.grouping_sign == '\u202F'
    assert not uzbekistan_sum.international
    assert uzbekistan_sum.symbol == 'сўм'
    assert not uzbekistan_sum.symbol_ahead
    assert uzbekistan_sum.symbol_separator == '\u00A0'
    assert uzbekistan_sum.convertion == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: 0.1428571428571428571428571429, '
        'alpha_code: "UZS", '
        'symbol: "сўм", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "860", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert uzbekistan_sum.__str__() == '0,14 сўм'


def test_uzbekistan_sum_negative():
    """test_uzbekistan_sum_negative."""
    amount = -100
    uzbekistan_sum = UzbekistanSum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.numeric_code == '860'
    assert uzbekistan_sum.alpha_code == 'UZS'
    assert uzbekistan_sum.decimal_places == 2
    assert uzbekistan_sum.decimal_sign == ','
    assert uzbekistan_sum.grouping_places == 3
    assert uzbekistan_sum.grouping_sign == '\u202F'
    assert not uzbekistan_sum.international
    assert uzbekistan_sum.symbol == 'сўм'
    assert not uzbekistan_sum.symbol_ahead
    assert uzbekistan_sum.symbol_separator == '\u00A0'
    assert uzbekistan_sum.convertion == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: -100, '
        'alpha_code: "UZS", '
        'symbol: "сўм", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "860", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert uzbekistan_sum.__str__() == '-100,00 сўм'


def test_uzbekistan_sum_custom():
    """test_uzbekistan_sum_custom."""
    amount = 1000
    uzbekistan_sum = UzbekistanSum(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.amount == decimal
    assert uzbekistan_sum.numeric_code == '860'
    assert uzbekistan_sum.alpha_code == 'UZS'
    assert uzbekistan_sum.decimal_places == 5
    assert uzbekistan_sum.decimal_sign == '\u202F'
    assert uzbekistan_sum.grouping_places == 2
    assert uzbekistan_sum.grouping_sign == ','
    assert uzbekistan_sum.international
    assert uzbekistan_sum.symbol == 'сўм'
    assert not uzbekistan_sum.symbol_ahead
    assert uzbekistan_sum.symbol_separator == '_'
    assert uzbekistan_sum.convertion == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: 1000, '
        'alpha_code: "UZS", '
        'symbol: "сўм", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "860", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert uzbekistan_sum.__str__() == 'UZS 10,00.00000'


def test_uzbekistan_sum_changed():
    """test_cuzbekistan_sum_changed."""
    uzbekistan_sum = UzbekistanSum(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.international = True


def test_uzbekistan_sum_math_add():
    """test_uzbekistan_sum_math_add."""
    uzbekistan_sum_one = UzbekistanSum(amount=1)
    uzbekistan_sum_two = UzbekistanSum(amount=2)
    uzbekistan_sum_three = UzbekistanSum(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency UZS and OTHER.'):
        _ = uzbekistan_sum_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'sum.UzbekistanSum\'> '
                   'and <class \'str\'>.')):
        _ = uzbekistan_sum_one.__add__('1.00')
    assert (
        uzbekistan_sum_one +
        uzbekistan_sum_two) == uzbekistan_sum_three


def test_uzbekistan_sum_slots():
    """test_uzbekistan_sum_slots."""
    uzbekistan_sum = UzbekistanSum(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'UzbekistanSum\' '
                'object has no attribute \'new_variable\'')):
        uzbekistan_sum.new_variable = 'fail'  # pylint: disable=assigning-non-slot
