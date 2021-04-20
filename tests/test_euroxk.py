# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroXK representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroXK
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroxk():
    """test_euroxk."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroxk = EuroXK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroxk.amount == decimal
    assert euroxk.numeric_code == '978'
    assert euroxk.alpha_code == 'EUR'
    assert euroxk.decimal_places == 2
    assert euroxk.decimal_sign == ','
    assert euroxk.grouping_sign == '\u202F'
    assert not euroxk.international
    assert euroxk.symbol == '€'
    assert not euroxk.symbol_ahead
    assert euroxk.symbol_separator == '\u00A0'
    assert euroxk.convertion == ''
    assert euroxk.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroxk.__repr__() == (
        'EuroXK(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert euroxk.__str__() == '0,14 €'


def test_euroxk_negative():
    """test_euroxk_negative."""
    amount = -100
    euroxk = EuroXK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroxk.numeric_code == '978'
    assert euroxk.alpha_code == 'EUR'
    assert euroxk.decimal_places == 2
    assert euroxk.decimal_sign == ','
    assert euroxk.grouping_sign == '\u202F'
    assert not euroxk.international
    assert euroxk.symbol == '€'
    assert not euroxk.symbol_ahead
    assert euroxk.symbol_separator == '\u00A0'
    assert euroxk.convertion == ''
    assert euroxk.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroxk.__repr__() == (
        'EuroXK(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert euroxk.__str__() == '-100,00 €'


def test_euroxk_custom():
    """test_euroxk_custom."""
    amount = 1000
    euroxk = EuroXK(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroxk.amount == decimal
    assert euroxk.numeric_code == '978'
    assert euroxk.alpha_code == 'EUR'
    assert euroxk.decimal_places == 5
    assert euroxk.decimal_sign == '\u202F'
    assert euroxk.grouping_sign == ','
    assert euroxk.international
    assert euroxk.symbol == '€'
    assert not euroxk.symbol_ahead
    assert euroxk.symbol_separator == '_'
    assert euroxk.convertion == ''
    assert euroxk.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroxk.__repr__() == (
        'EuroXK(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert euroxk.__str__() == 'EUR 1,000.00000'


def test_euroxk_changed():
    """test_ceuroxk_changed."""
    euroxk = EuroXK(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroxk.international = True


def test_euroxk_math_add():
    """test_euroxk_math_add."""
    euroxk_one = EuroXK(amount=1)
    euroxk_two = EuroXK(amount=2)
    euroxk_three = EuroXK(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroxk_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroXK\'> '
                   'and <class \'str\'>.')):
        _ = euroxk_one.__add__('1.00')
    assert (
        euroxk_one +
        euroxk_two) == euroxk_three


def test_euroxk_slots():
    """test_euroxk_slots."""
    euroxk = EuroXK(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroXK\' '
                'object has no attribute \'new_variable\'')):
        euroxk.new_variable = 'fail'  # pylint: disable=assigning-non-slot
