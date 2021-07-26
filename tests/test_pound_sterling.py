# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pound Sterling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PoundSterling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pound_sterling():
    """test_pound_sterling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pound_sterling = PoundSterling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.amount == decimal
    assert pound_sterling.numeric_code == '826'
    assert pound_sterling.alpha_code == 'GBP'
    assert pound_sterling.decimal_places == 2
    assert pound_sterling.decimal_sign == '.'
    assert pound_sterling.grouping_places == 3
    assert pound_sterling.grouping_sign == ','
    assert not pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert pound_sterling.symbol_ahead
    assert pound_sterling.symbol_separator == ''
    assert pound_sterling.convertion == ''
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GBP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "826", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert pound_sterling.__str__() == '£0.14'


def test_pound_sterling_negative():
    """test_pound_sterling_negative."""
    amount = -100
    pound_sterling = PoundSterling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.numeric_code == '826'
    assert pound_sterling.alpha_code == 'GBP'
    assert pound_sterling.decimal_places == 2
    assert pound_sterling.decimal_sign == '.'
    assert pound_sterling.grouping_places == 3
    assert pound_sterling.grouping_sign == ','
    assert not pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert pound_sterling.symbol_ahead
    assert pound_sterling.symbol_separator == ''
    assert pound_sterling.convertion == ''
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: -100, '
        'alpha_code: "GBP", '
        'symbol: "£", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "826", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert pound_sterling.__str__() == '£-100.00'


def test_pound_sterling_custom():
    """test_pound_sterling_custom."""
    amount = 1000
    pound_sterling = PoundSterling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert pound_sterling.amount == decimal
    assert pound_sterling.numeric_code == '826'
    assert pound_sterling.alpha_code == 'GBP'
    assert pound_sterling.decimal_places == 5
    assert pound_sterling.decimal_sign == ','
    assert pound_sterling.grouping_places == 2
    assert pound_sterling.grouping_sign == '.'
    assert pound_sterling.international
    assert pound_sterling.symbol == '£'
    assert not pound_sterling.symbol_ahead
    assert pound_sterling.symbol_separator == '_'
    assert pound_sterling.convertion == ''
    assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
    assert pound_sterling.__repr__() == (
        'PoundSterling(amount: 1000, '
        'alpha_code: "GBP", '
        'symbol: "£", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "826", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert pound_sterling.__str__() == 'GBP 10,00.00000'


def test_pound_sterling_changed():
    """test_cpound_sterling_changed."""
    pound_sterling = PoundSterling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pound_sterling.international = True


def test_pound_sterling_math_add():
    """test_pound_sterling_math_add."""
    pound_sterling_one = PoundSterling(amount=1)
    pound_sterling_two = PoundSterling(amount=2)
    pound_sterling_three = PoundSterling(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GBP and OTHER.'):
        _ = pound_sterling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.PoundSterling\'> '
                   'and <class \'str\'>.')):
        _ = pound_sterling_one.__add__('1.00')
    assert (
        pound_sterling_one +
        pound_sterling_two) == pound_sterling_three


def test_pound_sterling_slots():
    """test_pound_sterling_slots."""
    pound_sterling = PoundSterling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PoundSterling\' '
                'object has no attribute \'new_variable\'')):
        pound_sterling.new_variable = 'fail'  # pylint: disable=assigning-non-slot
