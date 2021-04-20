# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroVA representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroVA
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurova():
    """test_eurova."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurova = EuroVA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurova.amount == decimal
    assert eurova.numeric_code == '978'
    assert eurova.alpha_code == 'EUR'
    assert eurova.decimal_places == 2
    assert eurova.decimal_sign == '.'
    assert eurova.grouping_sign == ','
    assert not eurova.international
    assert eurova.symbol == '€'
    assert eurova.symbol_ahead
    assert eurova.symbol_separator == ''
    assert eurova.convertion == ''
    assert eurova.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurova.__repr__() == (
        'EuroVA(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert eurova.__str__() == '€0.14'


def test_eurova_negative():
    """test_eurova_negative."""
    amount = -100
    eurova = EuroVA(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurova.numeric_code == '978'
    assert eurova.alpha_code == 'EUR'
    assert eurova.decimal_places == 2
    assert eurova.decimal_sign == '.'
    assert eurova.grouping_sign == ','
    assert not eurova.international
    assert eurova.symbol == '€'
    assert eurova.symbol_ahead
    assert eurova.symbol_separator == ''
    assert eurova.convertion == ''
    assert eurova.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurova.__repr__() == (
        'EuroVA(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert eurova.__str__() == '€-100.00'


def test_eurova_custom():
    """test_eurova_custom."""
    amount = 1000
    eurova = EuroVA(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurova.amount == decimal
    assert eurova.numeric_code == '978'
    assert eurova.alpha_code == 'EUR'
    assert eurova.decimal_places == 5
    assert eurova.decimal_sign == ','
    assert eurova.grouping_sign == '.'
    assert eurova.international
    assert eurova.symbol == '€'
    assert not eurova.symbol_ahead
    assert eurova.symbol_separator == '_'
    assert eurova.convertion == ''
    assert eurova.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurova.__repr__() == (
        'EuroVA(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert eurova.__str__() == 'EUR 1,000.00000'


def test_eurova_changed():
    """test_ceurova_changed."""
    eurova = EuroVA(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurova.international = True


def test_eurova_math_add():
    """test_eurova_math_add."""
    eurova_one = EuroVA(amount=1)
    eurova_two = EuroVA(amount=2)
    eurova_three = EuroVA(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurova_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroVA\'> '
                   'and <class \'str\'>.')):
        _ = eurova_one.__add__('1.00')
    assert (
        eurova_one +
        eurova_two) == eurova_three


def test_eurova_slots():
    """test_eurova_slots."""
    eurova = EuroVA(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroVA\' '
                'object has no attribute \'new_variable\'')):
        eurova.new_variable = 'fail'  # pylint: disable=assigning-non-slot
