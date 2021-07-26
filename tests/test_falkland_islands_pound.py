# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Falkland Islands Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, FalklandIslandsPound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_falkland_islands_pound():
    """test_falkland_islands_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    falkland_islands_pound = FalklandIslandsPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert falkland_islands_pound.amount == decimal
    assert falkland_islands_pound.numeric_code == '238'
    assert falkland_islands_pound.alpha_code == 'FKP'
    assert falkland_islands_pound.decimal_places == 2
    assert falkland_islands_pound.decimal_sign == '.'
    assert falkland_islands_pound.grouping_places == 3
    assert falkland_islands_pound.grouping_sign == ','
    assert not falkland_islands_pound.international
    assert falkland_islands_pound.symbol == '£'
    assert falkland_islands_pound.symbol_ahead
    assert falkland_islands_pound.symbol_separator == ''
    assert falkland_islands_pound.convertion == ''
    assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
    assert falkland_islands_pound.__repr__() == (
        'FalklandIslandsPound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "FKP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "238", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert falkland_islands_pound.__str__() == '£0.14'


def test_falkland_islands_pound_negative():
    """test_falkland_islands_pound_negative."""
    amount = -100
    falkland_islands_pound = FalklandIslandsPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert falkland_islands_pound.numeric_code == '238'
    assert falkland_islands_pound.alpha_code == 'FKP'
    assert falkland_islands_pound.decimal_places == 2
    assert falkland_islands_pound.decimal_sign == '.'
    assert falkland_islands_pound.grouping_places == 3
    assert falkland_islands_pound.grouping_sign == ','
    assert not falkland_islands_pound.international
    assert falkland_islands_pound.symbol == '£'
    assert falkland_islands_pound.symbol_ahead
    assert falkland_islands_pound.symbol_separator == ''
    assert falkland_islands_pound.convertion == ''
    assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
    assert falkland_islands_pound.__repr__() == (
        'FalklandIslandsPound(amount: -100, '
        'alpha_code: "FKP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "238", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert falkland_islands_pound.__str__() == '£-100.00'


def test_falkland_islands_pound_custom():
    """test_falkland_islands_pound_custom."""
    amount = 1000
    falkland_islands_pound = FalklandIslandsPound(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert falkland_islands_pound.amount == decimal
    assert falkland_islands_pound.numeric_code == '238'
    assert falkland_islands_pound.alpha_code == 'FKP'
    assert falkland_islands_pound.decimal_places == 5
    assert falkland_islands_pound.decimal_sign == ','
    assert falkland_islands_pound.grouping_places == 2
    assert falkland_islands_pound.grouping_sign == '.'
    assert falkland_islands_pound.international
    assert falkland_islands_pound.symbol == '£'
    assert not falkland_islands_pound.symbol_ahead
    assert falkland_islands_pound.symbol_separator == '_'
    assert falkland_islands_pound.convertion == ''
    assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
    assert falkland_islands_pound.__repr__() == (
        'FalklandIslandsPound(amount: 1000, '
        'alpha_code: "FKP", '
        'symbol: "£", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "238", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert falkland_islands_pound.__str__() == 'FKP 10,00.00000'


def test_falkland_islands_pound_changed():
    """test_cfalkland_islands_pound_changed."""
    falkland_islands_pound = FalklandIslandsPound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        falkland_islands_pound.international = True


def test_falkland_islands_pound_math_add():
    """test_falkland_islands_pound_math_add."""
    falkland_islands_pound_one = FalklandIslandsPound(amount=1)
    falkland_islands_pound_two = FalklandIslandsPound(amount=2)
    falkland_islands_pound_three = FalklandIslandsPound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency FKP and OTHER.'):
        _ = falkland_islands_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.FalklandIslandsPound\'> '
                   'and <class \'str\'>.')):
        _ = falkland_islands_pound_one.__add__('1.00')
    assert (
        falkland_islands_pound_one +
        falkland_islands_pound_two) == falkland_islands_pound_three


def test_falkland_islands_pound_slots():
    """test_falkland_islands_pound_slots."""
    falkland_islands_pound = FalklandIslandsPound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'FalklandIslandsPound\' '
                'object has no attribute \'new_variable\'')):
        falkland_islands_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
