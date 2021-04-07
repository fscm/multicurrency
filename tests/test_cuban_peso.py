# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Cuban Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CubanPeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cuban_peso():
    """test_cuban_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cuban_peso = CubanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cuban_peso.amount == decimal
    assert cuban_peso.code == '192'
    assert cuban_peso.currency == 'CUP'
    assert cuban_peso.decimal_places == 2
    assert cuban_peso.decimal_sign == '.'
    assert cuban_peso.grouping_sign == ','
    assert not cuban_peso.international
    assert cuban_peso.symbol == '$'
    assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
    assert cuban_peso.__repr__() == (
        'CubanPeso(amount: 0.1428571428571428571428571429, '
        'currency: "CUP", '
        'symbol: "$", '
        'code: "192", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert cuban_peso.__str__() == '$0.14'


def test_cuban_peso_negative():
    """test_cuban_peso_negative."""
    amount = -100
    cuban_peso = CubanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cuban_peso.code == '192'
    assert cuban_peso.currency == 'CUP'
    assert cuban_peso.decimal_places == 2
    assert cuban_peso.decimal_sign == '.'
    assert cuban_peso.grouping_sign == ','
    assert not cuban_peso.international
    assert cuban_peso.symbol == '$'
    assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
    assert cuban_peso.__repr__() == (
        'CubanPeso(amount: -100, '
        'currency: "CUP", '
        'symbol: "$", '
        'code: "192", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert cuban_peso.__str__() == '$-100.00'


def test_cuban_peso_custom():
    """test_cuban_peso_custom."""
    amount = 1000
    cuban_peso = CubanPeso(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert cuban_peso.amount == decimal
    assert cuban_peso.code == '192'
    assert cuban_peso.currency == 'CUP'
    assert cuban_peso.decimal_places == 5
    assert cuban_peso.decimal_sign == ','
    assert cuban_peso.grouping_sign == '.'
    assert cuban_peso.international
    assert cuban_peso.symbol == '$'
    assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
    assert cuban_peso.__repr__() == (
        'CubanPeso(amount: 1000, '
        'currency: "CUP", '
        'symbol: "$", '
        'code: "192", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert cuban_peso.__str__() == 'CUP 1.000,00000'


def test_cuban_peso_changed():
    """test_ccuban_peso_changed."""
    cuban_peso = CubanPeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cuban_peso.international = True


def test_cuban_peso_math_add():
    """test_cuban_peso_math_add."""
    cuban_peso_one = CubanPeso(amount=1)
    cuban_peso_two = CubanPeso(amount=2)
    cuban_peso_three = CubanPeso(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CUP and OTHER.'):
        _ = cuban_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.CubanPeso\'> '
                   'and <class \'str\'>.')):
        _ = cuban_peso_one.__add__('1.00')
    assert (cuban_peso_one + cuban_peso_two) == cuban_peso_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CubanPeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CubanPeso\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
