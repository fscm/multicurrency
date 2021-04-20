# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroLU representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroLU
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurolu():
    """test_eurolu."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurolu = EuroLU(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolu.amount == decimal
    assert eurolu.numeric_code == '978'
    assert eurolu.alpha_code == 'EUR'
    assert eurolu.decimal_places == 2
    assert eurolu.decimal_sign == ','
    assert eurolu.grouping_sign == '.'
    assert not eurolu.international
    assert eurolu.symbol == '€'
    assert not eurolu.symbol_ahead
    assert eurolu.symbol_separator == '\u00A0'
    assert eurolu.convertion == ''
    assert eurolu.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolu.__repr__() == (
        'EuroLU(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurolu.__str__() == '0,14 €'


def test_eurolu_negative():
    """test_eurolu_negative."""
    amount = -100
    eurolu = EuroLU(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurolu.numeric_code == '978'
    assert eurolu.alpha_code == 'EUR'
    assert eurolu.decimal_places == 2
    assert eurolu.decimal_sign == ','
    assert eurolu.grouping_sign == '.'
    assert not eurolu.international
    assert eurolu.symbol == '€'
    assert not eurolu.symbol_ahead
    assert eurolu.symbol_separator == '\u00A0'
    assert eurolu.convertion == ''
    assert eurolu.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolu.__repr__() == (
        'EuroLU(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurolu.__str__() == '-100,00 €'


def test_eurolu_custom():
    """test_eurolu_custom."""
    amount = 1000
    eurolu = EuroLU(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurolu.amount == decimal
    assert eurolu.numeric_code == '978'
    assert eurolu.alpha_code == 'EUR'
    assert eurolu.decimal_places == 5
    assert eurolu.decimal_sign == '.'
    assert eurolu.grouping_sign == ','
    assert eurolu.international
    assert eurolu.symbol == '€'
    assert not eurolu.symbol_ahead
    assert eurolu.symbol_separator == '_'
    assert eurolu.convertion == ''
    assert eurolu.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurolu.__repr__() == (
        'EuroLU(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurolu.__str__() == 'EUR 1,000.00000'


def test_eurolu_changed():
    """test_ceurolu_changed."""
    eurolu = EuroLU(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurolu.international = True


def test_eurolu_math_add():
    """test_eurolu_math_add."""
    eurolu_one = EuroLU(amount=1)
    eurolu_two = EuroLU(amount=2)
    eurolu_three = EuroLU(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurolu_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroLU\'> '
                   'and <class \'str\'>.')):
        _ = eurolu_one.__add__('1.00')
    assert (
        eurolu_one +
        eurolu_two) == eurolu_three


def test_eurolu_slots():
    """test_eurolu_slots."""
    eurolu = EuroLU(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroLU\' '
                'object has no attribute \'new_variable\'')):
        eurolu.new_variable = 'fail'  # pylint: disable=assigning-non-slot
