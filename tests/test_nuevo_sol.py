# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nuevo Sol representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NuevoSol
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_nuevo_sol():
    """test_nuevo_sol."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    nuevo_sol = NuevoSol(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nuevo_sol.amount == decimal
    assert nuevo_sol.numeric_code == '604'
    assert nuevo_sol.alpha_code == 'PEN'
    assert nuevo_sol.decimal_places == 2
    assert nuevo_sol.decimal_sign == '.'
    assert nuevo_sol.grouping_sign == ','
    assert not nuevo_sol.international
    assert nuevo_sol.symbol == 'S/.'
    assert nuevo_sol.symbol_ahead
    assert nuevo_sol.symbol_separator == '\u00A0'
    assert nuevo_sol.__hash__() == hash((decimal, 'PEN', '604'))
    assert nuevo_sol.__repr__() == (
        'NuevoSol(amount: 0.1428571428571428571428571429, '
        'alpha_code: "PEN", '
        'symbol: "S/.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "604", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nuevo_sol.__str__() == 'S/. 0.14'


def test_nuevo_sol_negative():
    """test_nuevo_sol_negative."""
    amount = -100
    nuevo_sol = NuevoSol(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nuevo_sol.numeric_code == '604'
    assert nuevo_sol.alpha_code == 'PEN'
    assert nuevo_sol.decimal_places == 2
    assert nuevo_sol.decimal_sign == '.'
    assert nuevo_sol.grouping_sign == ','
    assert not nuevo_sol.international
    assert nuevo_sol.symbol == 'S/.'
    assert nuevo_sol.symbol_ahead
    assert nuevo_sol.symbol_separator == '\u00A0'
    assert nuevo_sol.__hash__() == hash((decimal, 'PEN', '604'))
    assert nuevo_sol.__repr__() == (
        'NuevoSol(amount: -100, '
        'alpha_code: "PEN", '
        'symbol: "S/.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "604", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nuevo_sol.__str__() == 'S/. -100.00'


def test_nuevo_sol_custom():
    """test_nuevo_sol_custom."""
    amount = 1000
    nuevo_sol = NuevoSol(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert nuevo_sol.amount == decimal
    assert nuevo_sol.numeric_code == '604'
    assert nuevo_sol.alpha_code == 'PEN'
    assert nuevo_sol.decimal_places == 5
    assert nuevo_sol.decimal_sign == ','
    assert nuevo_sol.grouping_sign == '.'
    assert nuevo_sol.international
    assert nuevo_sol.symbol == 'S/.'
    assert not nuevo_sol.symbol_ahead
    assert nuevo_sol.symbol_separator == '_'
    assert nuevo_sol.__hash__() == hash((decimal, 'PEN', '604'))
    assert nuevo_sol.__repr__() == (
        'NuevoSol(amount: 1000, '
        'alpha_code: "PEN", '
        'symbol: "S/.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "604", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert nuevo_sol.__str__() == 'PEN 1,000.00000'


def test_nuevo_sol_changed():
    """test_cnuevo_sol_changed."""
    nuevo_sol = NuevoSol(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nuevo_sol.international = True


def test_nuevo_sol_math_add():
    """test_nuevo_sol_math_add."""
    nuevo_sol_one = NuevoSol(amount=1)
    nuevo_sol_two = NuevoSol(amount=2)
    nuevo_sol_three = NuevoSol(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PEN and OTHER.'):
        _ = nuevo_sol_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'nuevo_sol.NuevoSol\'> '
                   'and <class \'str\'>.')):
        _ = nuevo_sol_one.__add__('1.00')
    assert (
        nuevo_sol_one +
        nuevo_sol_two) == nuevo_sol_three


def test_nuevo_sol_slots():
    """test_nuevo_sol_slots."""
    nuevo_sol = NuevoSol(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NuevoSol\' '
                'object has no attribute \'new_variable\'')):
        nuevo_sol.new_variable = 'fail'  # pylint: disable=assigning-non-slot
