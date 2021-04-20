# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dong representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Dong
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_dong():
    """test_dong."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    dong = Dong(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dong.amount == decimal
    assert dong.numeric_code == '704'
    assert dong.alpha_code == 'VND'
    assert dong.decimal_places == 0
    assert dong.decimal_sign == ','
    assert dong.grouping_sign == '.'
    assert not dong.international
    assert dong.symbol == '₫'
    assert not dong.symbol_ahead
    assert dong.symbol_separator == '\u00A0'
    assert dong.convertion == ''
    assert dong.__hash__() == hash((decimal, 'VND', '704'))
    assert dong.__repr__() == (
        'Dong(amount: 0.1428571428571428571428571429, '
        'alpha_code: "VND", '
        'symbol: "₫", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "704", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert dong.__str__() == '0 ₫'


def test_dong_negative():
    """test_dong_negative."""
    amount = -100
    dong = Dong(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dong.numeric_code == '704'
    assert dong.alpha_code == 'VND'
    assert dong.decimal_places == 0
    assert dong.decimal_sign == ','
    assert dong.grouping_sign == '.'
    assert not dong.international
    assert dong.symbol == '₫'
    assert not dong.symbol_ahead
    assert dong.symbol_separator == '\u00A0'
    assert dong.convertion == ''
    assert dong.__hash__() == hash((decimal, 'VND', '704'))
    assert dong.__repr__() == (
        'Dong(amount: -100, '
        'alpha_code: "VND", '
        'symbol: "₫", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "704", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert dong.__str__() == '-100 ₫'


def test_dong_custom():
    """test_dong_custom."""
    amount = 1000
    dong = Dong(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert dong.amount == decimal
    assert dong.numeric_code == '704'
    assert dong.alpha_code == 'VND'
    assert dong.decimal_places == 5
    assert dong.decimal_sign == '.'
    assert dong.grouping_sign == ','
    assert dong.international
    assert dong.symbol == '₫'
    assert not dong.symbol_ahead
    assert dong.symbol_separator == '_'
    assert dong.convertion == ''
    assert dong.__hash__() == hash((decimal, 'VND', '704'))
    assert dong.__repr__() == (
        'Dong(amount: 1000, '
        'alpha_code: "VND", '
        'symbol: "₫", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "704", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert dong.__str__() == 'VND 1,000.00000'


def test_dong_changed():
    """test_cdong_changed."""
    dong = Dong(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dong.international = True


def test_dong_math_add():
    """test_dong_math_add."""
    dong_one = Dong(amount=1)
    dong_two = Dong(amount=2)
    dong_three = Dong(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency VND and OTHER.'):
        _ = dong_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dong.Dong\'> '
                   'and <class \'str\'>.')):
        _ = dong_one.__add__('1.00')
    assert (
        dong_one +
        dong_two) == dong_three


def test_dong_slots():
    """test_dong_slots."""
    dong = Dong(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Dong\' '
                'object has no attribute \'new_variable\'')):
        dong.new_variable = 'fail'  # pylint: disable=assigning-non-slot
