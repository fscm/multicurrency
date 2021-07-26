# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroSI representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroSI
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurosi():
    """test_eurosi."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurosi = EuroSI(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosi.amount == decimal
    assert eurosi.numeric_code == '978'
    assert eurosi.alpha_code == 'EUR'
    assert eurosi.decimal_places == 2
    assert eurosi.decimal_sign == ','
    assert eurosi.grouping_places == 3
    assert eurosi.grouping_sign == '.'
    assert not eurosi.international
    assert eurosi.symbol == '€'
    assert not eurosi.symbol_ahead
    assert eurosi.symbol_separator == '\u00A0'
    assert eurosi.convertion == ''
    assert eurosi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosi.__repr__() == (
        'EuroSI(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurosi.__str__() == '0,14 €'


def test_eurosi_negative():
    """test_eurosi_negative."""
    amount = -100
    eurosi = EuroSI(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosi.numeric_code == '978'
    assert eurosi.alpha_code == 'EUR'
    assert eurosi.decimal_places == 2
    assert eurosi.decimal_sign == ','
    assert eurosi.grouping_places == 3
    assert eurosi.grouping_sign == '.'
    assert not eurosi.international
    assert eurosi.symbol == '€'
    assert not eurosi.symbol_ahead
    assert eurosi.symbol_separator == '\u00A0'
    assert eurosi.convertion == ''
    assert eurosi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosi.__repr__() == (
        'EuroSI(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurosi.__str__() == '-100,00 €'


def test_eurosi_custom():
    """test_eurosi_custom."""
    amount = 1000
    eurosi = EuroSI(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurosi.amount == decimal
    assert eurosi.numeric_code == '978'
    assert eurosi.alpha_code == 'EUR'
    assert eurosi.decimal_places == 5
    assert eurosi.decimal_sign == '.'
    assert eurosi.grouping_places == 2
    assert eurosi.grouping_sign == ','
    assert eurosi.international
    assert eurosi.symbol == '€'
    assert not eurosi.symbol_ahead
    assert eurosi.symbol_separator == '_'
    assert eurosi.convertion == ''
    assert eurosi.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosi.__repr__() == (
        'EuroSI(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurosi.__str__() == 'EUR 10,00.00000'


def test_eurosi_changed():
    """test_ceurosi_changed."""
    eurosi = EuroSI(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosi.international = True


def test_eurosi_math_add():
    """test_eurosi_math_add."""
    eurosi_one = EuroSI(amount=1)
    eurosi_two = EuroSI(amount=2)
    eurosi_three = EuroSI(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurosi_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroSI\'> '
                   'and <class \'str\'>.')):
        _ = eurosi_one.__add__('1.00')
    assert (
        eurosi_one +
        eurosi_two) == eurosi_three


def test_eurosi_slots():
    """test_eurosi_slots."""
    eurosi = EuroSI(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroSI\' '
                'object has no attribute \'new_variable\'')):
        eurosi.new_variable = 'fail'  # pylint: disable=assigning-non-slot
