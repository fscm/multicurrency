# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tenge representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Tenge
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tenge():
    """test_tenge."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tenge = Tenge(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.amount == decimal
    assert tenge.numeric_code == '398'
    assert tenge.alpha_code == 'KZT'
    assert tenge.decimal_places == 2
    assert tenge.decimal_sign == ','
    assert tenge.grouping_places == 3
    assert tenge.grouping_sign == '\u202F'
    assert not tenge.international
    assert tenge.symbol == '〒'
    assert not tenge.symbol_ahead
    assert tenge.symbol_separator == '\u00A0'
    assert tenge.convertion == ''
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KZT", '
        'symbol: "〒", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "398", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert tenge.__str__() == '0,14 〒'


def test_tenge_negative():
    """test_tenge_negative."""
    amount = -100
    tenge = Tenge(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.numeric_code == '398'
    assert tenge.alpha_code == 'KZT'
    assert tenge.decimal_places == 2
    assert tenge.decimal_sign == ','
    assert tenge.grouping_places == 3
    assert tenge.grouping_sign == '\u202F'
    assert not tenge.international
    assert tenge.symbol == '〒'
    assert not tenge.symbol_ahead
    assert tenge.symbol_separator == '\u00A0'
    assert tenge.convertion == ''
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: -100, '
        'alpha_code: "KZT", '
        'symbol: "〒", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "398", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert tenge.__str__() == '-100,00 〒'


def test_tenge_custom():
    """test_tenge_custom."""
    amount = 1000
    tenge = Tenge(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert tenge.amount == decimal
    assert tenge.numeric_code == '398'
    assert tenge.alpha_code == 'KZT'
    assert tenge.decimal_places == 5
    assert tenge.decimal_sign == '\u202F'
    assert tenge.grouping_places == 2
    assert tenge.grouping_sign == ','
    assert tenge.international
    assert tenge.symbol == '〒'
    assert not tenge.symbol_ahead
    assert tenge.symbol_separator == '_'
    assert tenge.convertion == ''
    assert tenge.__hash__() == hash((decimal, 'KZT', '398'))
    assert tenge.__repr__() == (
        'Tenge(amount: 1000, '
        'alpha_code: "KZT", '
        'symbol: "〒", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "398", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert tenge.__str__() == 'KZT 10,00.00000'


def test_tenge_changed():
    """test_ctenge_changed."""
    tenge = Tenge(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tenge.international = True


def test_tenge_math_add():
    """test_tenge_math_add."""
    tenge_one = Tenge(amount=1)
    tenge_two = Tenge(amount=2)
    tenge_three = Tenge(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KZT and OTHER.'):
        _ = tenge_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'tenge.Tenge\'> '
                   'and <class \'str\'>.')):
        _ = tenge_one.__add__('1.00')
    assert (
        tenge_one +
        tenge_two) == tenge_three


def test_tenge_slots():
    """test_tenge_slots."""
    tenge = Tenge(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Tenge\' '
                'object has no attribute \'new_variable\'')):
        tenge.new_variable = 'fail'  # pylint: disable=assigning-non-slot
