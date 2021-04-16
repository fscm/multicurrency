# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroES representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroES
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroes():
    """test_euroes."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroes = EuroES(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroes.amount == decimal
    assert euroes.numeric_code == '978'
    assert euroes.alpha_code == 'EUR'
    assert euroes.decimal_places == 2
    assert euroes.decimal_sign == ','
    assert euroes.grouping_sign == '.'
    assert not euroes.international
    assert euroes.symbol == '€'
    assert not euroes.symbol_ahead
    assert euroes.symbol_separator == '\u00A0'
    assert euroes.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroes.__repr__() == (
        'EuroES(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euroes.__str__() == '0,14 €'


def test_euroes_negative():
    """test_euroes_negative."""
    amount = -100
    euroes = EuroES(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroes.numeric_code == '978'
    assert euroes.alpha_code == 'EUR'
    assert euroes.decimal_places == 2
    assert euroes.decimal_sign == ','
    assert euroes.grouping_sign == '.'
    assert not euroes.international
    assert euroes.symbol == '€'
    assert not euroes.symbol_ahead
    assert euroes.symbol_separator == '\u00A0'
    assert euroes.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroes.__repr__() == (
        'EuroES(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert euroes.__str__() == '-100,00 €'


def test_euroes_custom():
    """test_euroes_custom."""
    amount = 1000
    euroes = EuroES(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroes.amount == decimal
    assert euroes.numeric_code == '978'
    assert euroes.alpha_code == 'EUR'
    assert euroes.decimal_places == 5
    assert euroes.decimal_sign == '.'
    assert euroes.grouping_sign == ','
    assert euroes.international
    assert euroes.symbol == '€'
    assert not euroes.symbol_ahead
    assert euroes.symbol_separator == '_'
    assert euroes.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroes.__repr__() == (
        'EuroES(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert euroes.__str__() == 'EUR 1,000.00000'


def test_euroes_changed():
    """test_ceuroes_changed."""
    euroes = EuroES(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroes.international = True


def test_euroes_math_add():
    """test_euroes_math_add."""
    euroes_one = EuroES(amount=1)
    euroes_two = EuroES(amount=2)
    euroes_three = EuroES(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroes_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroES\'> '
                   'and <class \'str\'>.')):
        _ = euroes_one.__add__('1.00')
    assert (
        euroes_one +
        euroes_two) == euroes_three


def test_euroes_slots():
    """test_euroes_slots."""
    euroes = EuroES(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroES\' '
                'object has no attribute \'new_variable\'')):
        euroes.new_variable = 'fail'  # pylint: disable=assigning-non-slot
