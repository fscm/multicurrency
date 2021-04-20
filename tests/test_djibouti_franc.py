# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Djibouti Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, DjiboutiFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_djibouti_franc():
    """test_djibouti_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    djibouti_franc = DjiboutiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.amount == decimal
    assert djibouti_franc.numeric_code == '262'
    assert djibouti_franc.alpha_code == 'DJF'
    assert djibouti_franc.decimal_places == 0
    assert djibouti_franc.decimal_sign == ','
    assert djibouti_franc.grouping_sign == '\u202F'
    assert not djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert not djibouti_franc.symbol_ahead
    assert djibouti_franc.symbol_separator == '\u00A0'
    assert djibouti_franc.convertion == ''
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: 0.1428571428571428571428571429, '
        'alpha_code: "DJF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "262", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert djibouti_franc.__str__() == '0 ₣'


def test_djibouti_franc_negative():
    """test_djibouti_franc_negative."""
    amount = -100
    djibouti_franc = DjiboutiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.numeric_code == '262'
    assert djibouti_franc.alpha_code == 'DJF'
    assert djibouti_franc.decimal_places == 0
    assert djibouti_franc.decimal_sign == ','
    assert djibouti_franc.grouping_sign == '\u202F'
    assert not djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert not djibouti_franc.symbol_ahead
    assert djibouti_franc.symbol_separator == '\u00A0'
    assert djibouti_franc.convertion == ''
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: -100, '
        'alpha_code: "DJF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "262", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert djibouti_franc.__str__() == '-100 ₣'


def test_djibouti_franc_custom():
    """test_djibouti_franc_custom."""
    amount = 1000
    djibouti_franc = DjiboutiFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert djibouti_franc.amount == decimal
    assert djibouti_franc.numeric_code == '262'
    assert djibouti_franc.alpha_code == 'DJF'
    assert djibouti_franc.decimal_places == 5
    assert djibouti_franc.decimal_sign == '\u202F'
    assert djibouti_franc.grouping_sign == ','
    assert djibouti_franc.international
    assert djibouti_franc.symbol == '₣'
    assert not djibouti_franc.symbol_ahead
    assert djibouti_franc.symbol_separator == '_'
    assert djibouti_franc.convertion == ''
    assert djibouti_franc.__hash__() == hash((decimal, 'DJF', '262'))
    assert djibouti_franc.__repr__() == (
        'DjiboutiFranc(amount: 1000, '
        'alpha_code: "DJF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "262", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert djibouti_franc.__str__() == 'DJF 1,000.00000'


def test_djibouti_franc_changed():
    """test_cdjibouti_franc_changed."""
    djibouti_franc = DjiboutiFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        djibouti_franc.international = True


def test_djibouti_franc_math_add():
    """test_djibouti_franc_math_add."""
    djibouti_franc_one = DjiboutiFranc(amount=1)
    djibouti_franc_two = DjiboutiFranc(amount=2)
    djibouti_franc_three = DjiboutiFranc(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DJF and OTHER.'):
        _ = djibouti_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.DjiboutiFranc\'> '
                   'and <class \'str\'>.')):
        _ = djibouti_franc_one.__add__('1.00')
    assert (
        djibouti_franc_one +
        djibouti_franc_two) == djibouti_franc_three


def test_djibouti_franc_slots():
    """test_djibouti_franc_slots."""
    djibouti_franc = DjiboutiFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'DjiboutiFranc\' '
                'object has no attribute \'new_variable\'')):
        djibouti_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
