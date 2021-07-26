# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rufiyaa representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Rufiyaa
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rufiyaa():
    """test_rufiyaa."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rufiyaa = Rufiyaa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.amount == decimal
    assert rufiyaa.numeric_code == '462'
    assert rufiyaa.alpha_code == 'MVR'
    assert rufiyaa.decimal_places == 2
    assert rufiyaa.decimal_sign == '.'
    assert rufiyaa.grouping_places == 3
    assert rufiyaa.grouping_sign == ','
    assert not rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert rufiyaa.symbol_ahead
    assert rufiyaa.symbol_separator == '\u00A0'
    assert rufiyaa.convertion == ''
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MVR", '
        'symbol: "ރ.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "462", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert rufiyaa.__str__() == 'ރ. 0.14'


def test_rufiyaa_negative():
    """test_rufiyaa_negative."""
    amount = -100
    rufiyaa = Rufiyaa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.numeric_code == '462'
    assert rufiyaa.alpha_code == 'MVR'
    assert rufiyaa.decimal_places == 2
    assert rufiyaa.decimal_sign == '.'
    assert rufiyaa.grouping_places == 3
    assert rufiyaa.grouping_sign == ','
    assert not rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert rufiyaa.symbol_ahead
    assert rufiyaa.symbol_separator == '\u00A0'
    assert rufiyaa.convertion == ''
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: -100, '
        'alpha_code: "MVR", '
        'symbol: "ރ.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "462", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert rufiyaa.__str__() == 'ރ. -100.00'


def test_rufiyaa_custom():
    """test_rufiyaa_custom."""
    amount = 1000
    rufiyaa = Rufiyaa(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.amount == decimal
    assert rufiyaa.numeric_code == '462'
    assert rufiyaa.alpha_code == 'MVR'
    assert rufiyaa.decimal_places == 5
    assert rufiyaa.decimal_sign == ','
    assert rufiyaa.grouping_places == 2
    assert rufiyaa.grouping_sign == '.'
    assert rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert not rufiyaa.symbol_ahead
    assert rufiyaa.symbol_separator == '_'
    assert rufiyaa.convertion == ''
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: 1000, '
        'alpha_code: "MVR", '
        'symbol: "ރ.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "462", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert rufiyaa.__str__() == 'MVR 10,00.00000'


def test_rufiyaa_changed():
    """test_crufiyaa_changed."""
    rufiyaa = Rufiyaa(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.international = True


def test_rufiyaa_math_add():
    """test_rufiyaa_math_add."""
    rufiyaa_one = Rufiyaa(amount=1)
    rufiyaa_two = Rufiyaa(amount=2)
    rufiyaa_three = Rufiyaa(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MVR and OTHER.'):
        _ = rufiyaa_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rufiyaa.Rufiyaa\'> '
                   'and <class \'str\'>.')):
        _ = rufiyaa_one.__add__('1.00')
    assert (
        rufiyaa_one +
        rufiyaa_two) == rufiyaa_three


def test_rufiyaa_slots():
    """test_rufiyaa_slots."""
    rufiyaa = Rufiyaa(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Rufiyaa\' '
                'object has no attribute \'new_variable\'')):
        rufiyaa.new_variable = 'fail'  # pylint: disable=assigning-non-slot
