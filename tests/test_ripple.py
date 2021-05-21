# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ripple representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Ripple
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ripple():
    """test_ripple."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ripple = Ripple(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ripple.amount == decimal
    assert ripple.numeric_code == '0'
    assert ripple.alpha_code == 'XRP'
    assert ripple.decimal_places == 6
    assert ripple.decimal_sign == '.'
    assert ripple.grouping_sign == ','
    assert not ripple.international
    assert ripple.symbol == '✕'
    assert ripple.symbol_ahead
    assert ripple.symbol_separator == ''
    assert ripple.convertion == ''
    assert ripple.__hash__() == hash((decimal, 'XRP', '0'))
    assert ripple.__repr__() == (
        'Ripple(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XRP", '
        'symbol: "✕", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "6", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert ripple.__str__() == '✕0.142857'


def test_ripple_negative():
    """test_ripple_negative."""
    amount = -100
    ripple = Ripple(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ripple.numeric_code == '0'
    assert ripple.alpha_code == 'XRP'
    assert ripple.decimal_places == 6
    assert ripple.decimal_sign == '.'
    assert ripple.grouping_sign == ','
    assert not ripple.international
    assert ripple.symbol == '✕'
    assert ripple.symbol_ahead
    assert ripple.symbol_separator == ''
    assert ripple.convertion == ''
    assert ripple.__hash__() == hash((decimal, 'XRP', '0'))
    assert ripple.__repr__() == (
        'Ripple(amount: -100, '
        'alpha_code: "XRP", '
        'symbol: "✕", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "6", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert ripple.__str__() == '✕-100.000000'


def test_ripple_custom():
    """test_ripple_custom."""
    amount = 1000
    ripple = Ripple(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert ripple.amount == decimal
    assert ripple.numeric_code == '0'
    assert ripple.alpha_code == 'XRP'
    assert ripple.decimal_places == 5
    assert ripple.decimal_sign == ','
    assert ripple.grouping_sign == '.'
    assert ripple.international
    assert ripple.symbol == '✕'
    assert not ripple.symbol_ahead
    assert ripple.symbol_separator == '_'
    assert ripple.convertion == ''
    assert ripple.__hash__() == hash((decimal, 'XRP', '0'))
    assert ripple.__repr__() == (
        'Ripple(amount: 1000, '
        'alpha_code: "XRP", '
        'symbol: "✕", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert ripple.__str__() == 'XRP 1,000.00000'


def test_ripple_changed():
    """test_cripple_changed."""
    ripple = Ripple(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ripple.international = True


def test_ripple_math_add():
    """test_ripple_math_add."""
    ripple_one = Ripple(amount=1)
    ripple_two = Ripple(amount=2)
    ripple_three = Ripple(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XRP and OTHER.'):
        _ = ripple_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Ripple\'> '
                   'and <class \'str\'>.')):
        _ = ripple_one.__add__('1.00')
    assert (
        ripple_one +
        ripple_two) == ripple_three


def test_ripple_slots():
    """test_ripple_slots."""
    ripple = Ripple(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Ripple\' '
                'object has no attribute \'new_variable\'')):
        ripple.new_variable = 'fail'  # pylint: disable=assigning-non-slot
