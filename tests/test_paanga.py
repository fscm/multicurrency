# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pa’anga representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Paanga
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_paanga():
    """test_paanga."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    paanga = Paanga(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert paanga.amount == decimal
    assert paanga.numeric_code == '776'
    assert paanga.alpha_code == 'TOP'
    assert paanga.decimal_places == 2
    assert paanga.decimal_sign == '.'
    assert paanga.grouping_sign == ','
    assert not paanga.international
    assert paanga.symbol == 'T$'
    assert paanga.symbol_ahead
    assert paanga.symbol_separator == '\u00A0'
    assert paanga.__hash__() == hash((decimal, 'TOP', '776'))
    assert paanga.__repr__() == (
        'Paanga(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TOP", '
        'symbol: "T$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "776", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert paanga.__str__() == 'T$ 0.14'


def test_paanga_negative():
    """test_paanga_negative."""
    amount = -100
    paanga = Paanga(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert paanga.numeric_code == '776'
    assert paanga.alpha_code == 'TOP'
    assert paanga.decimal_places == 2
    assert paanga.decimal_sign == '.'
    assert paanga.grouping_sign == ','
    assert not paanga.international
    assert paanga.symbol == 'T$'
    assert paanga.symbol_ahead
    assert paanga.symbol_separator == '\u00A0'
    assert paanga.__hash__() == hash((decimal, 'TOP', '776'))
    assert paanga.__repr__() == (
        'Paanga(amount: -100, '
        'alpha_code: "TOP", '
        'symbol: "T$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "776", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert paanga.__str__() == 'T$ -100.00'


def test_paanga_custom():
    """test_paanga_custom."""
    amount = 1000
    paanga = Paanga(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert paanga.amount == decimal
    assert paanga.numeric_code == '776'
    assert paanga.alpha_code == 'TOP'
    assert paanga.decimal_places == 5
    assert paanga.decimal_sign == ','
    assert paanga.grouping_sign == '.'
    assert paanga.international
    assert paanga.symbol == 'T$'
    assert not paanga.symbol_ahead
    assert paanga.symbol_separator == '_'
    assert paanga.__hash__() == hash((decimal, 'TOP', '776'))
    assert paanga.__repr__() == (
        'Paanga(amount: 1000, '
        'alpha_code: "TOP", '
        'symbol: "T$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "776", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert paanga.__str__() == 'TOP 1,000.00000'


def test_paanga_changed():
    """test_cpaanga_changed."""
    paanga = Paanga(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        paanga.international = True


def test_paanga_math_add():
    """test_paanga_math_add."""
    paanga_one = Paanga(amount=1)
    paanga_two = Paanga(amount=2)
    paanga_three = Paanga(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TOP and OTHER.'):
        _ = paanga_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'paanga.Paanga\'> '
                   'and <class \'str\'>.')):
        _ = paanga_one.__add__('1.00')
    assert (
        paanga_one +
        paanga_two) == paanga_three


def test_paanga_slots():
    """test_paanga_slots."""
    paanga = Paanga(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Paanga\' '
                'object has no attribute \'new_variable\'')):
        paanga.new_variable = 'fail'  # pylint: disable=assigning-non-slot
