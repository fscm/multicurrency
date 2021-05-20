# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bulgarian Lev representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BulgarianLev
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bulgarian_lev():
    """test_bulgarian_lev."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bulgarian_lev = BulgarianLev(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.amount == decimal
    assert bulgarian_lev.numeric_code == '975'
    assert bulgarian_lev.alpha_code == 'BGN'
    assert bulgarian_lev.decimal_places == 2
    assert bulgarian_lev.decimal_sign == ','
    assert bulgarian_lev.grouping_sign == ''
    assert not bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв.'
    assert not bulgarian_lev.symbol_ahead
    assert bulgarian_lev.symbol_separator == '\u00A0'
    assert bulgarian_lev.convertion == ''
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BGN", '
        'symbol: "лв.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "975", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "", '
        'convertion: "", '
        'international: False)')
    assert bulgarian_lev.__str__() == '0,14 лв.'


def test_bulgarian_lev_negative():
    """test_bulgarian_lev_negative."""
    amount = -100
    bulgarian_lev = BulgarianLev(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.numeric_code == '975'
    assert bulgarian_lev.alpha_code == 'BGN'
    assert bulgarian_lev.decimal_places == 2
    assert bulgarian_lev.decimal_sign == ','
    assert bulgarian_lev.grouping_sign == ''
    assert not bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв.'
    assert not bulgarian_lev.symbol_ahead
    assert bulgarian_lev.symbol_separator == '\u00A0'
    assert bulgarian_lev.convertion == ''
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: -100, '
        'alpha_code: "BGN", '
        'symbol: "лв.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "975", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "", '
        'convertion: "", '
        'international: False)')
    assert bulgarian_lev.__str__() == '-100,00 лв.'


def test_bulgarian_lev_custom():
    """test_bulgarian_lev_custom."""
    amount = 1000
    bulgarian_lev = BulgarianLev(
        amount=amount,
        decimal_places=5,
        decimal_sign='',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert bulgarian_lev.amount == decimal
    assert bulgarian_lev.numeric_code == '975'
    assert bulgarian_lev.alpha_code == 'BGN'
    assert bulgarian_lev.decimal_places == 5
    assert bulgarian_lev.decimal_sign == ''
    assert bulgarian_lev.grouping_sign == ','
    assert bulgarian_lev.international
    assert bulgarian_lev.symbol == 'лв.'
    assert not bulgarian_lev.symbol_ahead
    assert bulgarian_lev.symbol_separator == '_'
    assert bulgarian_lev.convertion == ''
    assert bulgarian_lev.__hash__() == hash((decimal, 'BGN', '975'))
    assert bulgarian_lev.__repr__() == (
        'BulgarianLev(amount: 1000, '
        'alpha_code: "BGN", '
        'symbol: "лв.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "975", '
        'decimal_places: "5", '
        'decimal_sign: "", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert bulgarian_lev.__str__() == 'BGN 1,000.00000'


def test_bulgarian_lev_changed():
    """test_cbulgarian_lev_changed."""
    bulgarian_lev = BulgarianLev(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bulgarian_lev.international = True


def test_bulgarian_lev_math_add():
    """test_bulgarian_lev_math_add."""
    bulgarian_lev_one = BulgarianLev(amount=1)
    bulgarian_lev_two = BulgarianLev(amount=2)
    bulgarian_lev_three = BulgarianLev(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BGN and OTHER.'):
        _ = bulgarian_lev_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lev.BulgarianLev\'> '
                   'and <class \'str\'>.')):
        _ = bulgarian_lev_one.__add__('1.00')
    assert (
        bulgarian_lev_one +
        bulgarian_lev_two) == bulgarian_lev_three


def test_bulgarian_lev_slots():
    """test_bulgarian_lev_slots."""
    bulgarian_lev = BulgarianLev(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BulgarianLev\' '
                'object has no attribute \'new_variable\'')):
        bulgarian_lev.new_variable = 'fail'  # pylint: disable=assigning-non-slot
