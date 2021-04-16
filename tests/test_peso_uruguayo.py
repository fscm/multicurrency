# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Peso Uruguayo representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PesoUruguayo
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_peso_uruguayo():
    """test_peso_uruguayo."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    peso_uruguayo = PesoUruguayo(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert peso_uruguayo.amount == decimal
    assert peso_uruguayo.numeric_code == '858'
    assert peso_uruguayo.alpha_code == 'UYU'
    assert peso_uruguayo.decimal_places == 2
    assert peso_uruguayo.decimal_sign == ','
    assert peso_uruguayo.grouping_sign == '.'
    assert not peso_uruguayo.international
    assert peso_uruguayo.symbol == '$'
    assert peso_uruguayo.symbol_ahead
    assert peso_uruguayo.symbol_separator == '\u00A0'
    assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
    assert peso_uruguayo.__repr__() == (
        'PesoUruguayo(amount: 0.1428571428571428571428571429, '
        'alpha_code: "UYU", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "858", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert peso_uruguayo.__str__() == '$ 0,14'


def test_peso_uruguayo_negative():
    """test_peso_uruguayo_negative."""
    amount = -100
    peso_uruguayo = PesoUruguayo(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert peso_uruguayo.numeric_code == '858'
    assert peso_uruguayo.alpha_code == 'UYU'
    assert peso_uruguayo.decimal_places == 2
    assert peso_uruguayo.decimal_sign == ','
    assert peso_uruguayo.grouping_sign == '.'
    assert not peso_uruguayo.international
    assert peso_uruguayo.symbol == '$'
    assert peso_uruguayo.symbol_ahead
    assert peso_uruguayo.symbol_separator == '\u00A0'
    assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
    assert peso_uruguayo.__repr__() == (
        'PesoUruguayo(amount: -100, '
        'alpha_code: "UYU", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "858", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert peso_uruguayo.__str__() == '$ -100,00'


def test_peso_uruguayo_custom():
    """test_peso_uruguayo_custom."""
    amount = 1000
    peso_uruguayo = PesoUruguayo(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert peso_uruguayo.amount == decimal
    assert peso_uruguayo.numeric_code == '858'
    assert peso_uruguayo.alpha_code == 'UYU'
    assert peso_uruguayo.decimal_places == 5
    assert peso_uruguayo.decimal_sign == '.'
    assert peso_uruguayo.grouping_sign == ','
    assert peso_uruguayo.international
    assert peso_uruguayo.symbol == '$'
    assert not peso_uruguayo.symbol_ahead
    assert peso_uruguayo.symbol_separator == '_'
    assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
    assert peso_uruguayo.__repr__() == (
        'PesoUruguayo(amount: 1000, '
        'alpha_code: "UYU", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "858", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert peso_uruguayo.__str__() == 'UYU 1,000.00000'


def test_peso_uruguayo_changed():
    """test_cpeso_uruguayo_changed."""
    peso_uruguayo = PesoUruguayo(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        peso_uruguayo.international = True


def test_peso_uruguayo_math_add():
    """test_peso_uruguayo_math_add."""
    peso_uruguayo_one = PesoUruguayo(amount=1)
    peso_uruguayo_two = PesoUruguayo(amount=2)
    peso_uruguayo_three = PesoUruguayo(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency UYU and OTHER.'):
        _ = peso_uruguayo_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.PesoUruguayo\'> '
                   'and <class \'str\'>.')):
        _ = peso_uruguayo_one.__add__('1.00')
    assert (
        peso_uruguayo_one +
        peso_uruguayo_two) == peso_uruguayo_three


def test_peso_uruguayo_slots():
    """test_peso_uruguayo_slots."""
    peso_uruguayo = PesoUruguayo(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PesoUruguayo\' '
                'object has no attribute \'new_variable\'')):
        peso_uruguayo.new_variable = 'fail'  # pylint: disable=assigning-non-slot
