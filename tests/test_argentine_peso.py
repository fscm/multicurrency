# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Argentine Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ArgentinePeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_argentine_peso():
    """test_argentine_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    argentine_peso = ArgentinePeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert argentine_peso.amount == decimal
    assert argentine_peso.numeric_code == '032'
    assert argentine_peso.alpha_code == 'ARS'
    assert argentine_peso.decimal_places == 2
    assert argentine_peso.decimal_sign == ','
    assert argentine_peso.grouping_places == 3
    assert argentine_peso.grouping_sign == '.'
    assert not argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert argentine_peso.symbol_ahead
    assert argentine_peso.symbol_separator == '\u00A0'
    assert argentine_peso.convertion == ''
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ARS", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "032", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert argentine_peso.__str__() == '$ 0,14'


def test_argentine_peso_negative():
    """test_argentine_peso_negative."""
    amount = -100
    argentine_peso = ArgentinePeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert argentine_peso.numeric_code == '032'
    assert argentine_peso.alpha_code == 'ARS'
    assert argentine_peso.decimal_places == 2
    assert argentine_peso.decimal_sign == ','
    assert argentine_peso.grouping_places == 3
    assert argentine_peso.grouping_sign == '.'
    assert not argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert argentine_peso.symbol_ahead
    assert argentine_peso.symbol_separator == '\u00A0'
    assert argentine_peso.convertion == ''
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: -100, '
        'alpha_code: "ARS", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "032", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert argentine_peso.__str__() == '$ -100,00'


def test_argentine_peso_custom():
    """test_argentine_peso_custom."""
    amount = 1000
    argentine_peso = ArgentinePeso(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert argentine_peso.amount == decimal
    assert argentine_peso.numeric_code == '032'
    assert argentine_peso.alpha_code == 'ARS'
    assert argentine_peso.decimal_places == 5
    assert argentine_peso.decimal_sign == '.'
    assert argentine_peso.grouping_places == 2
    assert argentine_peso.grouping_sign == ','
    assert argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert not argentine_peso.symbol_ahead
    assert argentine_peso.symbol_separator == '_'
    assert argentine_peso.convertion == ''
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: 1000, '
        'alpha_code: "ARS", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "032", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert argentine_peso.__str__() == 'ARS 10,00.00000'


def test_argentine_peso_changed():
    """test_cargentine_peso_changed."""
    argentine_peso = ArgentinePeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.international = True


def test_argentine_peso_math_add():
    """test_argentine_peso_math_add."""
    argentine_peso_one = ArgentinePeso(amount=1)
    argentine_peso_two = ArgentinePeso(amount=2)
    argentine_peso_three = ArgentinePeso(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ARS and OTHER.'):
        _ = argentine_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.ArgentinePeso\'> '
                   'and <class \'str\'>.')):
        _ = argentine_peso_one.__add__('1.00')
    assert (
        argentine_peso_one +
        argentine_peso_two) == argentine_peso_three


def test_argentine_peso_slots():
    """test_argentine_peso_slots."""
    argentine_peso = ArgentinePeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ArgentinePeso\' '
                'object has no attribute \'new_variable\'')):
        argentine_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot
