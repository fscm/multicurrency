# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Malagasy Ariary representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MalagasyAriary
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_malagasy_ariary():
    """test_malagasy_ariary."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    malagasy_ariary = MalagasyAriary(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.amount == decimal
    assert malagasy_ariary.numeric_code == '969'
    assert malagasy_ariary.alpha_code == 'MGA'
    assert malagasy_ariary.decimal_places == 0
    assert malagasy_ariary.decimal_sign == ','
    assert malagasy_ariary.grouping_sign == '\u202F'
    assert not malagasy_ariary.international
    assert malagasy_ariary.symbol == 'Ar'
    assert not malagasy_ariary.symbol_ahead
    assert malagasy_ariary.symbol_separator == '\u00A0'
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MGA", '
        'symbol: "Ar", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "969", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert malagasy_ariary.__str__() == '0 Ar'


def test_malagasy_ariary_negative():
    """test_malagasy_ariary_negative."""
    amount = -100
    malagasy_ariary = MalagasyAriary(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.numeric_code == '969'
    assert malagasy_ariary.alpha_code == 'MGA'
    assert malagasy_ariary.decimal_places == 0
    assert malagasy_ariary.decimal_sign == ','
    assert malagasy_ariary.grouping_sign == '\u202F'
    assert not malagasy_ariary.international
    assert malagasy_ariary.symbol == 'Ar'
    assert not malagasy_ariary.symbol_ahead
    assert malagasy_ariary.symbol_separator == '\u00A0'
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: -100, '
        'alpha_code: "MGA", '
        'symbol: "Ar", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "969", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert malagasy_ariary.__str__() == '-100 Ar'


def test_malagasy_ariary_custom():
    """test_malagasy_ariary_custom."""
    amount = 1000
    malagasy_ariary = MalagasyAriary(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.amount == decimal
    assert malagasy_ariary.numeric_code == '969'
    assert malagasy_ariary.alpha_code == 'MGA'
    assert malagasy_ariary.decimal_places == 5
    assert malagasy_ariary.decimal_sign == '\u202F'
    assert malagasy_ariary.grouping_sign == ','
    assert malagasy_ariary.international
    assert malagasy_ariary.symbol == 'Ar'
    assert not malagasy_ariary.symbol_ahead
    assert malagasy_ariary.symbol_separator == '_'
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: 1000, '
        'alpha_code: "MGA", '
        'symbol: "Ar", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "969", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert malagasy_ariary.__str__() == 'MGA 1,000.00000'


def test_malagasy_ariary_changed():
    """test_cmalagasy_ariary_changed."""
    malagasy_ariary = MalagasyAriary(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.international = True


def test_malagasy_ariary_math_add():
    """test_malagasy_ariary_math_add."""
    malagasy_ariary_one = MalagasyAriary(amount=1)
    malagasy_ariary_two = MalagasyAriary(amount=2)
    malagasy_ariary_three = MalagasyAriary(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MGA and OTHER.'):
        _ = malagasy_ariary_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ariary.MalagasyAriary\'> '
                   'and <class \'str\'>.')):
        _ = malagasy_ariary_one.__add__('1.00')
    assert (
        malagasy_ariary_one +
        malagasy_ariary_two) == malagasy_ariary_three


def test_malagasy_ariary_slots():
    """test_malagasy_ariary_slots."""
    malagasy_ariary = MalagasyAriary(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MalagasyAriary\' '
                'object has no attribute \'new_variable\'')):
        malagasy_ariary.new_variable = 'fail'  # pylint: disable=assigning-non-slot
