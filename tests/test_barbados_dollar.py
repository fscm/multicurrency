# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Barbados Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BarbadosDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_barbados_dollar():
    """test_barbados_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    barbados_dollar = BarbadosDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert barbados_dollar.amount == decimal
    assert barbados_dollar.numeric_code == '052'
    assert barbados_dollar.alpha_code == 'BBD'
    assert barbados_dollar.decimal_places == 2
    assert barbados_dollar.decimal_sign == '.'
    assert barbados_dollar.grouping_places == 3
    assert barbados_dollar.grouping_sign == ','
    assert not barbados_dollar.international
    assert barbados_dollar.symbol == '$'
    assert barbados_dollar.symbol_ahead
    assert barbados_dollar.symbol_separator == ''
    assert barbados_dollar.convertion == ''
    assert barbados_dollar.__hash__() == hash((decimal, 'BBD', '052'))
    assert barbados_dollar.__repr__() == (
        'BarbadosDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BBD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "052", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert barbados_dollar.__str__() == '$0.14'


def test_barbados_dollar_negative():
    """test_barbados_dollar_negative."""
    amount = -100
    barbados_dollar = BarbadosDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert barbados_dollar.numeric_code == '052'
    assert barbados_dollar.alpha_code == 'BBD'
    assert barbados_dollar.decimal_places == 2
    assert barbados_dollar.decimal_sign == '.'
    assert barbados_dollar.grouping_places == 3
    assert barbados_dollar.grouping_sign == ','
    assert not barbados_dollar.international
    assert barbados_dollar.symbol == '$'
    assert barbados_dollar.symbol_ahead
    assert barbados_dollar.symbol_separator == ''
    assert barbados_dollar.convertion == ''
    assert barbados_dollar.__hash__() == hash((decimal, 'BBD', '052'))
    assert barbados_dollar.__repr__() == (
        'BarbadosDollar(amount: -100, '
        'alpha_code: "BBD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "052", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert barbados_dollar.__str__() == '$-100.00'


def test_barbados_dollar_custom():
    """test_barbados_dollar_custom."""
    amount = 1000
    barbados_dollar = BarbadosDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert barbados_dollar.amount == decimal
    assert barbados_dollar.numeric_code == '052'
    assert barbados_dollar.alpha_code == 'BBD'
    assert barbados_dollar.decimal_places == 5
    assert barbados_dollar.decimal_sign == ','
    assert barbados_dollar.grouping_places == 2
    assert barbados_dollar.grouping_sign == '.'
    assert barbados_dollar.international
    assert barbados_dollar.symbol == '$'
    assert not barbados_dollar.symbol_ahead
    assert barbados_dollar.symbol_separator == '_'
    assert barbados_dollar.convertion == ''
    assert barbados_dollar.__hash__() == hash((decimal, 'BBD', '052'))
    assert barbados_dollar.__repr__() == (
        'BarbadosDollar(amount: 1000, '
        'alpha_code: "BBD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "052", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert barbados_dollar.__str__() == 'BBD 10,00.00000'


def test_barbados_dollar_changed():
    """test_cbarbados_dollar_changed."""
    barbados_dollar = BarbadosDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        barbados_dollar.international = True


def test_barbados_dollar_math_add():
    """test_barbados_dollar_math_add."""
    barbados_dollar_one = BarbadosDollar(amount=1)
    barbados_dollar_two = BarbadosDollar(amount=2)
    barbados_dollar_three = BarbadosDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BBD and OTHER.'):
        _ = barbados_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.BarbadosDollar\'> '
                   'and <class \'str\'>.')):
        _ = barbados_dollar_one.__add__('1.00')
    assert (
        barbados_dollar_one +
        barbados_dollar_two) == barbados_dollar_three


def test_barbados_dollar_slots():
    """test_barbados_dollar_slots."""
    barbados_dollar = BarbadosDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BarbadosDollar\' '
                'object has no attribute \'new_variable\'')):
        barbados_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
