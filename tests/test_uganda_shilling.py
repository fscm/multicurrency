# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Uganda Shilling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, UgandaShilling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_uganda_shilling():
    """test_uganda_shilling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    uganda_shilling = UgandaShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uganda_shilling.amount == decimal
    assert uganda_shilling.numeric_code == '800'
    assert uganda_shilling.alpha_code == 'UGX'
    assert uganda_shilling.decimal_places == 0
    assert uganda_shilling.decimal_sign == '.'
    assert uganda_shilling.grouping_places == 3
    assert uganda_shilling.grouping_sign == ','
    assert not uganda_shilling.international
    assert uganda_shilling.symbol == 'USh'
    assert uganda_shilling.symbol_ahead
    assert uganda_shilling.symbol_separator == '\u00A0'
    assert uganda_shilling.convertion == ''
    assert uganda_shilling.__hash__() == hash((decimal, 'UGX', '800'))
    assert uganda_shilling.__repr__() == (
        'UgandaShilling(amount: 0.1428571428571428571428571429, '
        'alpha_code: "UGX", '
        'symbol: "USh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "800", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert uganda_shilling.__str__() == 'USh 0'


def test_uganda_shilling_negative():
    """test_uganda_shilling_negative."""
    amount = -100
    uganda_shilling = UgandaShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uganda_shilling.numeric_code == '800'
    assert uganda_shilling.alpha_code == 'UGX'
    assert uganda_shilling.decimal_places == 0
    assert uganda_shilling.decimal_sign == '.'
    assert uganda_shilling.grouping_places == 3
    assert uganda_shilling.grouping_sign == ','
    assert not uganda_shilling.international
    assert uganda_shilling.symbol == 'USh'
    assert uganda_shilling.symbol_ahead
    assert uganda_shilling.symbol_separator == '\u00A0'
    assert uganda_shilling.convertion == ''
    assert uganda_shilling.__hash__() == hash((decimal, 'UGX', '800'))
    assert uganda_shilling.__repr__() == (
        'UgandaShilling(amount: -100, '
        'alpha_code: "UGX", '
        'symbol: "USh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "800", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert uganda_shilling.__str__() == 'USh -100'


def test_uganda_shilling_custom():
    """test_uganda_shilling_custom."""
    amount = 1000
    uganda_shilling = UgandaShilling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert uganda_shilling.amount == decimal
    assert uganda_shilling.numeric_code == '800'
    assert uganda_shilling.alpha_code == 'UGX'
    assert uganda_shilling.decimal_places == 5
    assert uganda_shilling.decimal_sign == ','
    assert uganda_shilling.grouping_places == 2
    assert uganda_shilling.grouping_sign == '.'
    assert uganda_shilling.international
    assert uganda_shilling.symbol == 'USh'
    assert not uganda_shilling.symbol_ahead
    assert uganda_shilling.symbol_separator == '_'
    assert uganda_shilling.convertion == ''
    assert uganda_shilling.__hash__() == hash((decimal, 'UGX', '800'))
    assert uganda_shilling.__repr__() == (
        'UgandaShilling(amount: 1000, '
        'alpha_code: "UGX", '
        'symbol: "USh", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "800", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert uganda_shilling.__str__() == 'UGX 10,00.00000'


def test_uganda_shilling_changed():
    """test_cuganda_shilling_changed."""
    uganda_shilling = UgandaShilling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uganda_shilling.international = True


def test_uganda_shilling_math_add():
    """test_uganda_shilling_math_add."""
    uganda_shilling_one = UgandaShilling(amount=1)
    uganda_shilling_two = UgandaShilling(amount=2)
    uganda_shilling_three = UgandaShilling(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency UGX and OTHER.'):
        _ = uganda_shilling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'shilling.UgandaShilling\'> '
                   'and <class \'str\'>.')):
        _ = uganda_shilling_one.__add__('1.00')
    assert (
        uganda_shilling_one +
        uganda_shilling_two) == uganda_shilling_three


def test_uganda_shilling_slots():
    """test_uganda_shilling_slots."""
    uganda_shilling = UgandaShilling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'UgandaShilling\' '
                'object has no attribute \'new_variable\'')):
        uganda_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot
