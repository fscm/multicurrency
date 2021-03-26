# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Colombian Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ColombianPeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_colombian_peso():
    """test_colombian_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    colombian_peso = ColombianPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert colombian_peso.amount == decimal
    assert colombian_peso.code == '170'
    assert colombian_peso.currency == 'COP'
    assert colombian_peso.decimal_places == 2
    assert colombian_peso.decimal_sign == ','
    assert colombian_peso.grouping_sign == '.'
    assert not colombian_peso.international
    assert colombian_peso.symbol == '$'
    assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
    assert colombian_peso.__repr__() == (
        'ColombianPeso(amount: 0.1428571428571428571428571429, '
        'currency: "COP", '
        'symbol: "$", '
        'code: "170", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert colombian_peso.__str__() == '$0,14'


def test_colombian_peso_negative():
    """test_colombian_peso_negative."""
    amount = -100
    colombian_peso = ColombianPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert colombian_peso.code == '170'
    assert colombian_peso.currency == 'COP'
    assert colombian_peso.decimal_places == 2
    assert colombian_peso.decimal_sign == ','
    assert colombian_peso.grouping_sign == '.'
    assert not colombian_peso.international
    assert colombian_peso.symbol == '$'
    assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
    assert colombian_peso.__repr__() == (
        'ColombianPeso(amount: -100, '
        'currency: "COP", '
        'symbol: "$", '
        'code: "170", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert colombian_peso.__str__() == '$-100,00'


def test_colombian_peso_custom():
    """test_colombian_peso_custom."""
    amount = 1000
    colombian_peso = ColombianPeso(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert colombian_peso.amount == decimal
    assert colombian_peso.code == '170'
    assert colombian_peso.currency == 'COP'
    assert colombian_peso.decimal_places == 5
    assert colombian_peso.decimal_sign == '.'
    assert colombian_peso.grouping_sign == ','
    assert colombian_peso.international
    assert colombian_peso.symbol == '$'
    assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
    assert colombian_peso.__repr__() == (
        'ColombianPeso(amount: 1000, '
        'currency: "COP", '
        'symbol: "$", '
        'code: "170", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert colombian_peso.__str__() == 'COP 1,000.00000'


def test_colombian_peso_changed():
    """test_ccolombian_peso_changed."""
    colombian_peso = ColombianPeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        colombian_peso.international = True


def test_colombian_peso_math_add():
    """test_colombian_peso_math_add."""
    colombian_peso_one = ColombianPeso(amount=1)
    colombian_peso_two = ColombianPeso(amount=2)
    colombian_peso_three = ColombianPeso(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency COP and OTHER.'):
        _ = colombian_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'colombian_peso.ColombianPeso\'> '
                   'and <class \'str\'>.')):
        _ = colombian_peso_one.__add__('1.00')
    assert (colombian_peso_one + colombian_peso_two) == colombian_peso_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ColombianPeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ColombianPeso\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
