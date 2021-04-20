# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwanza representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kwanza
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kwanza():
    """test_kwanza."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kwanza = Kwanza(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.amount == decimal
    assert kwanza.numeric_code == '973'
    assert kwanza.alpha_code == 'AOA'
    assert kwanza.decimal_places == 2
    assert kwanza.decimal_sign == ','
    assert kwanza.grouping_sign == '\u202F'
    assert not kwanza.international
    assert kwanza.symbol == 'Kz'
    assert not kwanza.symbol_ahead
    assert kwanza.symbol_separator == '\u00A0'
    assert kwanza.convertion == ''
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AOA", '
        'symbol: "Kz", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "973", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert kwanza.__str__() == '0,14 Kz'


def test_kwanza_negative():
    """test_kwanza_negative."""
    amount = -100
    kwanza = Kwanza(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.numeric_code == '973'
    assert kwanza.alpha_code == 'AOA'
    assert kwanza.decimal_places == 2
    assert kwanza.decimal_sign == ','
    assert kwanza.grouping_sign == '\u202F'
    assert not kwanza.international
    assert kwanza.symbol == 'Kz'
    assert not kwanza.symbol_ahead
    assert kwanza.symbol_separator == '\u00A0'
    assert kwanza.convertion == ''
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: -100, '
        'alpha_code: "AOA", '
        'symbol: "Kz", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "973", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert kwanza.__str__() == '-100,00 Kz'


def test_kwanza_custom():
    """test_kwanza_custom."""
    amount = 1000
    kwanza = Kwanza(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.amount == decimal
    assert kwanza.numeric_code == '973'
    assert kwanza.alpha_code == 'AOA'
    assert kwanza.decimal_places == 5
    assert kwanza.decimal_sign == '\u202F'
    assert kwanza.grouping_sign == ','
    assert kwanza.international
    assert kwanza.symbol == 'Kz'
    assert not kwanza.symbol_ahead
    assert kwanza.symbol_separator == '_'
    assert kwanza.convertion == ''
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: 1000, '
        'alpha_code: "AOA", '
        'symbol: "Kz", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "973", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert kwanza.__str__() == 'AOA 1,000.00000'


def test_kwanza_changed():
    """test_ckwanza_changed."""
    kwanza = Kwanza(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.international = True


def test_kwanza_math_add():
    """test_kwanza_math_add."""
    kwanza_one = Kwanza(amount=1)
    kwanza_two = Kwanza(amount=2)
    kwanza_three = Kwanza(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AOA and OTHER.'):
        _ = kwanza_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kwanza.Kwanza\'> '
                   'and <class \'str\'>.')):
        _ = kwanza_one.__add__('1.00')
    assert (
        kwanza_one +
        kwanza_two) == kwanza_three


def test_kwanza_slots():
    """test_kwanza_slots."""
    kwanza = Kwanza(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kwanza\' '
                'object has no attribute \'new_variable\'')):
        kwanza.new_variable = 'fail'  # pylint: disable=assigning-non-slot
