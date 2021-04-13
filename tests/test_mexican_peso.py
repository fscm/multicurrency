# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Mexican Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MexicanPeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_mexican_peso():
    """test_mexican_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    mexican_peso = MexicanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert mexican_peso.amount == decimal
    assert mexican_peso.numeric_code == '484'
    assert mexican_peso.alpha_code == 'MXN'
    assert mexican_peso.decimal_places == 2
    assert mexican_peso.decimal_sign == '.'
    assert mexican_peso.grouping_sign == ','
    assert not mexican_peso.international
    assert mexican_peso.symbol == '$'
    assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
    assert mexican_peso.__repr__() == (
        'MexicanPeso(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MXN", '
        'symbol: "$", '
        'numeric_code: "484", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert mexican_peso.__str__() == '$0.14'


def test_mexican_peso_negative():
    """test_mexican_peso_negative."""
    amount = -100
    mexican_peso = MexicanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert mexican_peso.numeric_code == '484'
    assert mexican_peso.alpha_code == 'MXN'
    assert mexican_peso.decimal_places == 2
    assert mexican_peso.decimal_sign == '.'
    assert mexican_peso.grouping_sign == ','
    assert not mexican_peso.international
    assert mexican_peso.symbol == '$'
    assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
    assert mexican_peso.__repr__() == (
        'MexicanPeso(amount: -100, '
        'alpha_code: "MXN", '
        'symbol: "$", '
        'numeric_code: "484", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert mexican_peso.__str__() == '$-100.00'


def test_mexican_peso_custom():
    """test_mexican_peso_custom."""
    amount = 1000
    mexican_peso = MexicanPeso(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert mexican_peso.amount == decimal
    assert mexican_peso.numeric_code == '484'
    assert mexican_peso.alpha_code == 'MXN'
    assert mexican_peso.decimal_places == 5
    assert mexican_peso.decimal_sign == ','
    assert mexican_peso.grouping_sign == '.'
    assert mexican_peso.international
    assert mexican_peso.symbol == '$'
    assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
    assert mexican_peso.__repr__() == (
        'MexicanPeso(amount: 1000, '
        'alpha_code: "MXN", '
        'symbol: "$", '
        'numeric_code: "484", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert mexican_peso.__str__() == 'MXN 1.000,00000'


def test_mexican_peso_changed():
    """test_cmexican_peso_changed."""
    mexican_peso = MexicanPeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mexican_peso.international = True


def test_mexican_peso_math_add():
    """test_mexican_peso_math_add."""
    mexican_peso_one = MexicanPeso(amount=1)
    mexican_peso_two = MexicanPeso(amount=2)
    mexican_peso_three = MexicanPeso(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MXN and OTHER.'):
        _ = mexican_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.MexicanPeso\'> '
                   'and <class \'str\'>.')):
        _ = mexican_peso_one.__add__('1.00')
    assert (mexican_peso_one + mexican_peso_two) == mexican_peso_three


def test_currency_slots():
    """test_currency_slots."""
    euro = MexicanPeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MexicanPeso\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
