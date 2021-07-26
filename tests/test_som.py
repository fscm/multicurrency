# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Som representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Som
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_som():
    """test_som."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    som = Som(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert som.amount == decimal
    assert som.numeric_code == '417'
    assert som.alpha_code == 'KGS'
    assert som.decimal_places == 2
    assert som.decimal_sign == ','
    assert som.grouping_places == 3
    assert som.grouping_sign == '\u202F'
    assert not som.international
    assert som.symbol == 'Лв'
    assert not som.symbol_ahead
    assert som.symbol_separator == '\u00A0'
    assert som.convertion == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KGS", '
        'symbol: "Лв", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "417", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert som.__str__() == '0,14 Лв'


def test_som_negative():
    """test_som_negative."""
    amount = -100
    som = Som(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert som.numeric_code == '417'
    assert som.alpha_code == 'KGS'
    assert som.decimal_places == 2
    assert som.decimal_sign == ','
    assert som.grouping_places == 3
    assert som.grouping_sign == '\u202F'
    assert not som.international
    assert som.symbol == 'Лв'
    assert not som.symbol_ahead
    assert som.symbol_separator == '\u00A0'
    assert som.convertion == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: -100, '
        'alpha_code: "KGS", '
        'symbol: "Лв", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "417", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert som.__str__() == '-100,00 Лв'


def test_som_custom():
    """test_som_custom."""
    amount = 1000
    som = Som(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert som.amount == decimal
    assert som.numeric_code == '417'
    assert som.alpha_code == 'KGS'
    assert som.decimal_places == 5
    assert som.decimal_sign == '\u202F'
    assert som.grouping_places == 2
    assert som.grouping_sign == ','
    assert som.international
    assert som.symbol == 'Лв'
    assert not som.symbol_ahead
    assert som.symbol_separator == '_'
    assert som.convertion == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: 1000, '
        'alpha_code: "KGS", '
        'symbol: "Лв", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "417", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert som.__str__() == 'KGS 10,00.00000'


def test_som_changed():
    """test_csom_changed."""
    som = Som(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.international = True


def test_som_math_add():
    """test_som_math_add."""
    som_one = Som(amount=1)
    som_two = Som(amount=2)
    som_three = Som(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KGS and OTHER.'):
        _ = som_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'som.Som\'> '
                   'and <class \'str\'>.')):
        _ = som_one.__add__('1.00')
    assert (
        som_one +
        som_two) == som_three


def test_som_slots():
    """test_som_slots."""
    som = Som(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Som\' '
                'object has no attribute \'new_variable\'')):
        som.new_variable = 'fail'  # pylint: disable=assigning-non-slot
