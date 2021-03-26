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
    assert argentine_peso.code == '032'
    assert argentine_peso.currency == 'ARS'
    assert argentine_peso.decimal_places == 2
    assert argentine_peso.decimal_sign == ','
    assert argentine_peso.grouping_sign == '.'
    assert not argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: 0.1428571428571428571428571429, '
        'currency: "ARS", '
        'symbol: "$", '
        'code: "032", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert argentine_peso.__str__() == '$0,14'


def test_argentine_peso_negative():
    """test_argentine_peso_negative."""
    amount = -100
    argentine_peso = ArgentinePeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert argentine_peso.code == '032'
    assert argentine_peso.currency == 'ARS'
    assert argentine_peso.decimal_places == 2
    assert argentine_peso.decimal_sign == ','
    assert argentine_peso.grouping_sign == '.'
    assert not argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: -100, '
        'currency: "ARS", '
        'symbol: "$", '
        'code: "032", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert argentine_peso.__str__() == '$-100,00'


def test_argentine_peso_custom():
    """test_argentine_peso_custom."""
    amount = 1000
    argentine_peso = ArgentinePeso(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert argentine_peso.amount == decimal
    assert argentine_peso.code == '032'
    assert argentine_peso.currency == 'ARS'
    assert argentine_peso.decimal_places == 5
    assert argentine_peso.decimal_sign == '.'
    assert argentine_peso.grouping_sign == ','
    assert argentine_peso.international
    assert argentine_peso.symbol == '$'
    assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
    assert argentine_peso.__repr__() == (
        'ArgentinePeso(amount: 1000, '
        'currency: "ARS", '
        'symbol: "$", '
        'code: "032", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert argentine_peso.__str__() == 'ARS 1,000.00000'


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
        argentine_peso.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        argentine_peso.code = '978'
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
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ARS and OTHER.'):
        _ = argentine_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'argentine_peso.ArgentinePeso\'> '
                   'and <class \'str\'>.')):
        _ = argentine_peso_one.__add__('1.00')
    assert (argentine_peso_one + argentine_peso_two) == argentine_peso_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ArgentinePeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ArgentinePeso\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
