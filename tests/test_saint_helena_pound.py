# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Saint Helena Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SaintHelenaPound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_saint_helena_pound():
    """test_saint_helena_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    saint_helena_pound = SaintHelenaPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert saint_helena_pound.amount == decimal
    assert saint_helena_pound.numeric_code == '654'
    assert saint_helena_pound.alpha_code == 'SHP'
    assert saint_helena_pound.decimal_places == 2
    assert saint_helena_pound.decimal_sign == '.'
    assert saint_helena_pound.grouping_places == 3
    assert saint_helena_pound.grouping_sign == ','
    assert not saint_helena_pound.international
    assert saint_helena_pound.symbol == '£'
    assert saint_helena_pound.symbol_ahead
    assert saint_helena_pound.symbol_separator == ''
    assert saint_helena_pound.convertion == ''
    assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
    assert saint_helena_pound.__repr__() == (
        'SaintHelenaPound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SHP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "654", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert saint_helena_pound.__str__() == '£0.14'


def test_saint_helena_pound_negative():
    """test_saint_helena_pound_negative."""
    amount = -100
    saint_helena_pound = SaintHelenaPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert saint_helena_pound.numeric_code == '654'
    assert saint_helena_pound.alpha_code == 'SHP'
    assert saint_helena_pound.decimal_places == 2
    assert saint_helena_pound.decimal_sign == '.'
    assert saint_helena_pound.grouping_places == 3
    assert saint_helena_pound.grouping_sign == ','
    assert not saint_helena_pound.international
    assert saint_helena_pound.symbol == '£'
    assert saint_helena_pound.symbol_ahead
    assert saint_helena_pound.symbol_separator == ''
    assert saint_helena_pound.convertion == ''
    assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
    assert saint_helena_pound.__repr__() == (
        'SaintHelenaPound(amount: -100, '
        'alpha_code: "SHP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "654", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert saint_helena_pound.__str__() == '£-100.00'


def test_saint_helena_pound_custom():
    """test_saint_helena_pound_custom."""
    amount = 1000
    saint_helena_pound = SaintHelenaPound(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert saint_helena_pound.amount == decimal
    assert saint_helena_pound.numeric_code == '654'
    assert saint_helena_pound.alpha_code == 'SHP'
    assert saint_helena_pound.decimal_places == 5
    assert saint_helena_pound.decimal_sign == ','
    assert saint_helena_pound.grouping_places == 2
    assert saint_helena_pound.grouping_sign == '.'
    assert saint_helena_pound.international
    assert saint_helena_pound.symbol == '£'
    assert not saint_helena_pound.symbol_ahead
    assert saint_helena_pound.symbol_separator == '_'
    assert saint_helena_pound.convertion == ''
    assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
    assert saint_helena_pound.__repr__() == (
        'SaintHelenaPound(amount: 1000, '
        'alpha_code: "SHP", '
        'symbol: "£", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "654", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert saint_helena_pound.__str__() == 'SHP 10,00.00000'


def test_saint_helena_pound_changed():
    """test_csaint_helena_pound_changed."""
    saint_helena_pound = SaintHelenaPound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        saint_helena_pound.international = True


def test_saint_helena_pound_math_add():
    """test_saint_helena_pound_math_add."""
    saint_helena_pound_one = SaintHelenaPound(amount=1)
    saint_helena_pound_two = SaintHelenaPound(amount=2)
    saint_helena_pound_three = SaintHelenaPound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SHP and OTHER.'):
        _ = saint_helena_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.SaintHelenaPound\'> '
                   'and <class \'str\'>.')):
        _ = saint_helena_pound_one.__add__('1.00')
    assert (
        saint_helena_pound_one +
        saint_helena_pound_two) == saint_helena_pound_three


def test_saint_helena_pound_slots():
    """test_saint_helena_pound_slots."""
    saint_helena_pound = SaintHelenaPound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SaintHelenaPound\' '
                'object has no attribute \'new_variable\'')):
        saint_helena_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
