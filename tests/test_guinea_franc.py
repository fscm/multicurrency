# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Guinea Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, GuineaFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_guinea_franc():
    """test_guinea_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    guinea_franc = GuineaFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guinea_franc.amount == decimal
    assert guinea_franc.numeric_code == '324'
    assert guinea_franc.alpha_code == 'GNF'
    assert guinea_franc.decimal_places == 0
    assert guinea_franc.decimal_sign == ','
    assert guinea_franc.grouping_places == 3
    assert guinea_franc.grouping_sign == '\u202F'
    assert not guinea_franc.international
    assert guinea_franc.symbol == '₣'
    assert not guinea_franc.symbol_ahead
    assert guinea_franc.symbol_separator == '\u00A0'
    assert guinea_franc.convertion == ''
    assert guinea_franc.__hash__() == hash((decimal, 'GNF', '324'))
    assert guinea_franc.__repr__() == (
        'GuineaFranc(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GNF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "324", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert guinea_franc.__str__() == '0 ₣'


def test_guinea_franc_negative():
    """test_guinea_franc_negative."""
    amount = -100
    guinea_franc = GuineaFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guinea_franc.numeric_code == '324'
    assert guinea_franc.alpha_code == 'GNF'
    assert guinea_franc.decimal_places == 0
    assert guinea_franc.decimal_sign == ','
    assert guinea_franc.grouping_places == 3
    assert guinea_franc.grouping_sign == '\u202F'
    assert not guinea_franc.international
    assert guinea_franc.symbol == '₣'
    assert not guinea_franc.symbol_ahead
    assert guinea_franc.symbol_separator == '\u00A0'
    assert guinea_franc.convertion == ''
    assert guinea_franc.__hash__() == hash((decimal, 'GNF', '324'))
    assert guinea_franc.__repr__() == (
        'GuineaFranc(amount: -100, '
        'alpha_code: "GNF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "324", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert guinea_franc.__str__() == '-100 ₣'


def test_guinea_franc_custom():
    """test_guinea_franc_custom."""
    amount = 1000
    guinea_franc = GuineaFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert guinea_franc.amount == decimal
    assert guinea_franc.numeric_code == '324'
    assert guinea_franc.alpha_code == 'GNF'
    assert guinea_franc.decimal_places == 5
    assert guinea_franc.decimal_sign == '\u202F'
    assert guinea_franc.grouping_places == 2
    assert guinea_franc.grouping_sign == ','
    assert guinea_franc.international
    assert guinea_franc.symbol == '₣'
    assert not guinea_franc.symbol_ahead
    assert guinea_franc.symbol_separator == '_'
    assert guinea_franc.convertion == ''
    assert guinea_franc.__hash__() == hash((decimal, 'GNF', '324'))
    assert guinea_franc.__repr__() == (
        'GuineaFranc(amount: 1000, '
        'alpha_code: "GNF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "324", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert guinea_franc.__str__() == 'GNF 10,00.00000'


def test_guinea_franc_changed():
    """test_cguinea_franc_changed."""
    guinea_franc = GuineaFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guinea_franc.international = True


def test_guinea_franc_math_add():
    """test_guinea_franc_math_add."""
    guinea_franc_one = GuineaFranc(amount=1)
    guinea_franc_two = GuineaFranc(amount=2)
    guinea_franc_three = GuineaFranc(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GNF and OTHER.'):
        _ = guinea_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.GuineaFranc\'> '
                   'and <class \'str\'>.')):
        _ = guinea_franc_one.__add__('1.00')
    assert (
        guinea_franc_one +
        guinea_franc_two) == guinea_franc_three


def test_guinea_franc_slots():
    """test_guinea_franc_slots."""
    guinea_franc = GuineaFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'GuineaFranc\' '
                'object has no attribute \'new_variable\'')):
        guinea_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
