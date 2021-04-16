# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Gourde representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Gourde
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_gourde():
    """test_gourde."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    gourde = Gourde(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert gourde.amount == decimal
    assert gourde.numeric_code == '332'
    assert gourde.alpha_code == 'HTG'
    assert gourde.decimal_places == 2
    assert gourde.decimal_sign == '.'
    assert gourde.grouping_sign == ','
    assert not gourde.international
    assert gourde.symbol == 'G'
    assert gourde.symbol_ahead
    assert gourde.symbol_separator == '\u00A0'
    assert gourde.__hash__() == hash((decimal, 'HTG', '332'))
    assert gourde.__repr__() == (
        'Gourde(amount: 0.1428571428571428571428571429, '
        'alpha_code: "HTG", '
        'symbol: "G", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "332", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert gourde.__str__() == 'G 0.14'


def test_gourde_negative():
    """test_gourde_negative."""
    amount = -100
    gourde = Gourde(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert gourde.numeric_code == '332'
    assert gourde.alpha_code == 'HTG'
    assert gourde.decimal_places == 2
    assert gourde.decimal_sign == '.'
    assert gourde.grouping_sign == ','
    assert not gourde.international
    assert gourde.symbol == 'G'
    assert gourde.symbol_ahead
    assert gourde.symbol_separator == '\u00A0'
    assert gourde.__hash__() == hash((decimal, 'HTG', '332'))
    assert gourde.__repr__() == (
        'Gourde(amount: -100, '
        'alpha_code: "HTG", '
        'symbol: "G", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "332", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert gourde.__str__() == 'G -100.00'


def test_gourde_custom():
    """test_gourde_custom."""
    amount = 1000
    gourde = Gourde(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert gourde.amount == decimal
    assert gourde.numeric_code == '332'
    assert gourde.alpha_code == 'HTG'
    assert gourde.decimal_places == 5
    assert gourde.decimal_sign == ','
    assert gourde.grouping_sign == '.'
    assert gourde.international
    assert gourde.symbol == 'G'
    assert not gourde.symbol_ahead
    assert gourde.symbol_separator == '_'
    assert gourde.__hash__() == hash((decimal, 'HTG', '332'))
    assert gourde.__repr__() == (
        'Gourde(amount: 1000, '
        'alpha_code: "HTG", '
        'symbol: "G", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "332", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert gourde.__str__() == 'HTG 1,000.00000'


def test_gourde_changed():
    """test_cgourde_changed."""
    gourde = Gourde(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        gourde.international = True


def test_gourde_math_add():
    """test_gourde_math_add."""
    gourde_one = Gourde(amount=1)
    gourde_two = Gourde(amount=2)
    gourde_three = Gourde(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency HTG and OTHER.'):
        _ = gourde_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'gourde.Gourde\'> '
                   'and <class \'str\'>.')):
        _ = gourde_one.__add__('1.00')
    assert (
        gourde_one +
        gourde_two) == gourde_three


def test_gourde_slots():
    """test_gourde_slots."""
    gourde = Gourde(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Gourde\' '
                'object has no attribute \'new_variable\'')):
        gourde.new_variable = 'fail'  # pylint: disable=assigning-non-slot
