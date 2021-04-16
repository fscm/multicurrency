# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kenyan Shilling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, KenyanShilling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kenyan_shilling():
    """test_kenyan_shilling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kenyan_shilling = KenyanShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.amount == decimal
    assert kenyan_shilling.numeric_code == '404'
    assert kenyan_shilling.alpha_code == 'KES'
    assert kenyan_shilling.decimal_places == 2
    assert kenyan_shilling.decimal_sign == '.'
    assert kenyan_shilling.grouping_sign == ','
    assert not kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Ksh'
    assert kenyan_shilling.symbol_ahead
    assert kenyan_shilling.symbol_separator == '\u00A0'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: 0.1428571428571428571428571429, '
        'alpha_code: "KES", '
        'symbol: "Ksh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "404", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kenyan_shilling.__str__() == 'Ksh 0.14'


def test_kenyan_shilling_negative():
    """test_kenyan_shilling_negative."""
    amount = -100
    kenyan_shilling = KenyanShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.numeric_code == '404'
    assert kenyan_shilling.alpha_code == 'KES'
    assert kenyan_shilling.decimal_places == 2
    assert kenyan_shilling.decimal_sign == '.'
    assert kenyan_shilling.grouping_sign == ','
    assert not kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Ksh'
    assert kenyan_shilling.symbol_ahead
    assert kenyan_shilling.symbol_separator == '\u00A0'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: -100, '
        'alpha_code: "KES", '
        'symbol: "Ksh", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "404", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kenyan_shilling.__str__() == 'Ksh -100.00'


def test_kenyan_shilling_custom():
    """test_kenyan_shilling_custom."""
    amount = 1000
    kenyan_shilling = KenyanShilling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.amount == decimal
    assert kenyan_shilling.numeric_code == '404'
    assert kenyan_shilling.alpha_code == 'KES'
    assert kenyan_shilling.decimal_places == 5
    assert kenyan_shilling.decimal_sign == ','
    assert kenyan_shilling.grouping_sign == '.'
    assert kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Ksh'
    assert not kenyan_shilling.symbol_ahead
    assert kenyan_shilling.symbol_separator == '_'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: 1000, '
        'alpha_code: "KES", '
        'symbol: "Ksh", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "404", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert kenyan_shilling.__str__() == 'KES 1,000.00000'


def test_kenyan_shilling_changed():
    """test_ckenyan_shilling_changed."""
    kenyan_shilling = KenyanShilling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.international = True


def test_kenyan_shilling_math_add():
    """test_kenyan_shilling_math_add."""
    kenyan_shilling_one = KenyanShilling(amount=1)
    kenyan_shilling_two = KenyanShilling(amount=2)
    kenyan_shilling_three = KenyanShilling(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KES and OTHER.'):
        _ = kenyan_shilling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'shilling.KenyanShilling\'> '
                   'and <class \'str\'>.')):
        _ = kenyan_shilling_one.__add__('1.00')
    assert (
        kenyan_shilling_one +
        kenyan_shilling_two) == kenyan_shilling_three


def test_kenyan_shilling_slots():
    """test_kenyan_shilling_slots."""
    kenyan_shilling = KenyanShilling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'KenyanShilling\' '
                'object has no attribute \'new_variable\'')):
        kenyan_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot
