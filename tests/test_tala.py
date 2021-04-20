# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tala representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Tala
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tala():
    """test_tala."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tala = Tala(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tala.amount == decimal
    assert tala.numeric_code == '882'
    assert tala.alpha_code == 'WST'
    assert tala.decimal_places == 2
    assert tala.decimal_sign == '.'
    assert tala.grouping_sign == ','
    assert not tala.international
    assert tala.symbol == 'T'
    assert tala.symbol_ahead
    assert tala.symbol_separator == '\u00A0'
    assert tala.convertion == ''
    assert tala.__hash__() == hash((decimal, 'WST', '882'))
    assert tala.__repr__() == (
        'Tala(amount: 0.1428571428571428571428571429, '
        'alpha_code: "WST", '
        'symbol: "T", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "882", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert tala.__str__() == 'T 0.14'


def test_tala_negative():
    """test_tala_negative."""
    amount = -100
    tala = Tala(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tala.numeric_code == '882'
    assert tala.alpha_code == 'WST'
    assert tala.decimal_places == 2
    assert tala.decimal_sign == '.'
    assert tala.grouping_sign == ','
    assert not tala.international
    assert tala.symbol == 'T'
    assert tala.symbol_ahead
    assert tala.symbol_separator == '\u00A0'
    assert tala.convertion == ''
    assert tala.__hash__() == hash((decimal, 'WST', '882'))
    assert tala.__repr__() == (
        'Tala(amount: -100, '
        'alpha_code: "WST", '
        'symbol: "T", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "882", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert tala.__str__() == 'T -100.00'


def test_tala_custom():
    """test_tala_custom."""
    amount = 1000
    tala = Tala(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert tala.amount == decimal
    assert tala.numeric_code == '882'
    assert tala.alpha_code == 'WST'
    assert tala.decimal_places == 5
    assert tala.decimal_sign == ','
    assert tala.grouping_sign == '.'
    assert tala.international
    assert tala.symbol == 'T'
    assert not tala.symbol_ahead
    assert tala.symbol_separator == '_'
    assert tala.convertion == ''
    assert tala.__hash__() == hash((decimal, 'WST', '882'))
    assert tala.__repr__() == (
        'Tala(amount: 1000, '
        'alpha_code: "WST", '
        'symbol: "T", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "882", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert tala.__str__() == 'WST 1,000.00000'


def test_tala_changed():
    """test_ctala_changed."""
    tala = Tala(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tala.international = True


def test_tala_math_add():
    """test_tala_math_add."""
    tala_one = Tala(amount=1)
    tala_two = Tala(amount=2)
    tala_three = Tala(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency WST and OTHER.'):
        _ = tala_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'tala.Tala\'> '
                   'and <class \'str\'>.')):
        _ = tala_one.__add__('1.00')
    assert (
        tala_one +
        tala_two) == tala_three


def test_tala_slots():
    """test_tala_slots."""
    tala = Tala(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Tala\' '
                'object has no attribute \'new_variable\'')):
        tala.new_variable = 'fail'  # pylint: disable=assigning-non-slot
