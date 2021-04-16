# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Afghani representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Afghani
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_afghani():
    """test_afghani."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    afghani = Afghani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert afghani.amount == decimal
    assert afghani.numeric_code == '971'
    assert afghani.alpha_code == 'AFN'
    assert afghani.decimal_places == 2
    assert afghani.decimal_sign == ','
    assert afghani.grouping_sign == '.'
    assert not afghani.international
    assert afghani.symbol == 'Af'
    assert afghani.symbol_ahead
    assert afghani.symbol_separator == '\u00A0'
    assert afghani.__hash__() == hash((decimal, 'AFN', '971'))
    assert afghani.__repr__() == (
        'Afghani(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AFN", '
        'symbol: "Af", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "971", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert afghani.__str__() == 'Af 0,14'


def test_afghani_negative():
    """test_afghani_negative."""
    amount = -100
    afghani = Afghani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert afghani.numeric_code == '971'
    assert afghani.alpha_code == 'AFN'
    assert afghani.decimal_places == 2
    assert afghani.decimal_sign == ','
    assert afghani.grouping_sign == '.'
    assert not afghani.international
    assert afghani.symbol == 'Af'
    assert afghani.symbol_ahead
    assert afghani.symbol_separator == '\u00A0'
    assert afghani.__hash__() == hash((decimal, 'AFN', '971'))
    assert afghani.__repr__() == (
        'Afghani(amount: -100, '
        'alpha_code: "AFN", '
        'symbol: "Af", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "971", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert afghani.__str__() == 'Af -100,00'


def test_afghani_custom():
    """test_afghani_custom."""
    amount = 1000
    afghani = Afghani(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert afghani.amount == decimal
    assert afghani.numeric_code == '971'
    assert afghani.alpha_code == 'AFN'
    assert afghani.decimal_places == 5
    assert afghani.decimal_sign == '.'
    assert afghani.grouping_sign == ','
    assert afghani.international
    assert afghani.symbol == 'Af'
    assert not afghani.symbol_ahead
    assert afghani.symbol_separator == '_'
    assert afghani.__hash__() == hash((decimal, 'AFN', '971'))
    assert afghani.__repr__() == (
        'Afghani(amount: 1000, '
        'alpha_code: "AFN", '
        'symbol: "Af", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "971", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert afghani.__str__() == 'AFN 1,000.00000'


def test_afghani_changed():
    """test_cafghani_changed."""
    afghani = Afghani(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        afghani.international = True


def test_afghani_math_add():
    """test_afghani_math_add."""
    afghani_one = Afghani(amount=1)
    afghani_two = Afghani(amount=2)
    afghani_three = Afghani(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AFN and OTHER.'):
        _ = afghani_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'afghani.Afghani\'> '
                   'and <class \'str\'>.')):
        _ = afghani_one.__add__('1.00')
    assert (
        afghani_one +
        afghani_two) == afghani_three


def test_afghani_slots():
    """test_afghani_slots."""
    afghani = Afghani(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Afghani\' '
                'object has no attribute \'new_variable\'')):
        afghani.new_variable = 'fail'  # pylint: disable=assigning-non-slot
