# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dominican Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, DominicanPeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_dominican_peso():
    """test_dominican_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    dominican_peso = DominicanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dominican_peso.amount == decimal
    assert dominican_peso.numeric_code == '214'
    assert dominican_peso.alpha_code == 'DOP'
    assert dominican_peso.decimal_places == 2
    assert dominican_peso.decimal_sign == '.'
    assert dominican_peso.grouping_sign == ','
    assert not dominican_peso.international
    assert dominican_peso.symbol == '$'
    assert dominican_peso.symbol_ahead
    assert dominican_peso.symbol_separator == ''
    assert dominican_peso.convertion == ''
    assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
    assert dominican_peso.__repr__() == (
        'DominicanPeso(amount: 0.1428571428571428571428571429, '
        'alpha_code: "DOP", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "214", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert dominican_peso.__str__() == '$0.14'


def test_dominican_peso_negative():
    """test_dominican_peso_negative."""
    amount = -100
    dominican_peso = DominicanPeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dominican_peso.numeric_code == '214'
    assert dominican_peso.alpha_code == 'DOP'
    assert dominican_peso.decimal_places == 2
    assert dominican_peso.decimal_sign == '.'
    assert dominican_peso.grouping_sign == ','
    assert not dominican_peso.international
    assert dominican_peso.symbol == '$'
    assert dominican_peso.symbol_ahead
    assert dominican_peso.symbol_separator == ''
    assert dominican_peso.convertion == ''
    assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
    assert dominican_peso.__repr__() == (
        'DominicanPeso(amount: -100, '
        'alpha_code: "DOP", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "214", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert dominican_peso.__str__() == '$-100.00'


def test_dominican_peso_custom():
    """test_dominican_peso_custom."""
    amount = 1000
    dominican_peso = DominicanPeso(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert dominican_peso.amount == decimal
    assert dominican_peso.numeric_code == '214'
    assert dominican_peso.alpha_code == 'DOP'
    assert dominican_peso.decimal_places == 5
    assert dominican_peso.decimal_sign == ','
    assert dominican_peso.grouping_sign == '.'
    assert dominican_peso.international
    assert dominican_peso.symbol == '$'
    assert not dominican_peso.symbol_ahead
    assert dominican_peso.symbol_separator == '_'
    assert dominican_peso.convertion == ''
    assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
    assert dominican_peso.__repr__() == (
        'DominicanPeso(amount: 1000, '
        'alpha_code: "DOP", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "214", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert dominican_peso.__str__() == 'DOP 1,000.00000'


def test_dominican_peso_changed():
    """test_cdominican_peso_changed."""
    dominican_peso = DominicanPeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dominican_peso.international = True


def test_dominican_peso_math_add():
    """test_dominican_peso_math_add."""
    dominican_peso_one = DominicanPeso(amount=1)
    dominican_peso_two = DominicanPeso(amount=2)
    dominican_peso_three = DominicanPeso(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DOP and OTHER.'):
        _ = dominican_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.DominicanPeso\'> '
                   'and <class \'str\'>.')):
        _ = dominican_peso_one.__add__('1.00')
    assert (
        dominican_peso_one +
        dominican_peso_two) == dominican_peso_three


def test_dominican_peso_slots():
    """test_dominican_peso_slots."""
    dominican_peso = DominicanPeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'DominicanPeso\' '
                'object has no attribute \'new_variable\'')):
        dominican_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot
