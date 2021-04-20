# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Chilean Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ChileanPeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_chilean_peso():
    """test_chilean_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    chilean_peso = ChileanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert chilean_peso.amount == decimal
    assert chilean_peso.numeric_code == '152'
    assert chilean_peso.alpha_code == 'CLP'
    assert chilean_peso.decimal_places == 0
    assert chilean_peso.decimal_sign == ','
    assert chilean_peso.grouping_sign == '.'
    assert not chilean_peso.international
    assert chilean_peso.symbol == '$'
    assert chilean_peso.symbol_ahead
    assert chilean_peso.symbol_separator == ''
    assert chilean_peso.convertion == ''
    assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
    assert chilean_peso.__repr__() == (
        'ChileanPeso(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CLP", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "152", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert chilean_peso.__str__() == '$0'


def test_chilean_peso_negative():
    """test_chilean_peso_negative."""
    amount = -100
    chilean_peso = ChileanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert chilean_peso.numeric_code == '152'
    assert chilean_peso.alpha_code == 'CLP'
    assert chilean_peso.decimal_places == 0
    assert chilean_peso.decimal_sign == ','
    assert chilean_peso.grouping_sign == '.'
    assert not chilean_peso.international
    assert chilean_peso.symbol == '$'
    assert chilean_peso.symbol_ahead
    assert chilean_peso.symbol_separator == ''
    assert chilean_peso.convertion == ''
    assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
    assert chilean_peso.__repr__() == (
        'ChileanPeso(amount: -100, '
        'alpha_code: "CLP", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "152", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert chilean_peso.__str__() == '$-100'


def test_chilean_peso_custom():
    """test_chilean_peso_custom."""
    amount = 1000
    chilean_peso = ChileanPeso(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert chilean_peso.amount == decimal
    assert chilean_peso.numeric_code == '152'
    assert chilean_peso.alpha_code == 'CLP'
    assert chilean_peso.decimal_places == 5
    assert chilean_peso.decimal_sign == '.'
    assert chilean_peso.grouping_sign == ','
    assert chilean_peso.international
    assert chilean_peso.symbol == '$'
    assert not chilean_peso.symbol_ahead
    assert chilean_peso.symbol_separator == '_'
    assert chilean_peso.convertion == ''
    assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
    assert chilean_peso.__repr__() == (
        'ChileanPeso(amount: 1000, '
        'alpha_code: "CLP", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "152", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert chilean_peso.__str__() == 'CLP 1,000.00000'


def test_chilean_peso_changed():
    """test_cchilean_peso_changed."""
    chilean_peso = ChileanPeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        chilean_peso.international = True


def test_chilean_peso_math_add():
    """test_chilean_peso_math_add."""
    chilean_peso_one = ChileanPeso(amount=1)
    chilean_peso_two = ChileanPeso(amount=2)
    chilean_peso_three = ChileanPeso(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CLP and OTHER.'):
        _ = chilean_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.ChileanPeso\'> '
                   'and <class \'str\'>.')):
        _ = chilean_peso_one.__add__('1.00')
    assert (
        chilean_peso_one +
        chilean_peso_two) == chilean_peso_three


def test_chilean_peso_slots():
    """test_chilean_peso_slots."""
    chilean_peso = ChileanPeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ChileanPeso\' '
                'object has no attribute \'new_variable\'')):
        chilean_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot
