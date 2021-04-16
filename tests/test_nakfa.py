# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nakfa representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Nakfa
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_nakfa():
    """test_nakfa."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    nakfa = Nakfa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.amount == decimal
    assert nakfa.numeric_code == '232'
    assert nakfa.alpha_code == 'ERN'
    assert nakfa.decimal_places == 2
    assert nakfa.decimal_sign == '.'
    assert nakfa.grouping_sign == ','
    assert not nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert nakfa.symbol_ahead
    assert nakfa.symbol_separator == '\u00A0'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ERN", '
        'symbol: "Nfk", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "232", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nakfa.__str__() == 'Nfk 0.14'


def test_nakfa_negative():
    """test_nakfa_negative."""
    amount = -100
    nakfa = Nakfa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.numeric_code == '232'
    assert nakfa.alpha_code == 'ERN'
    assert nakfa.decimal_places == 2
    assert nakfa.decimal_sign == '.'
    assert nakfa.grouping_sign == ','
    assert not nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert nakfa.symbol_ahead
    assert nakfa.symbol_separator == '\u00A0'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: -100, '
        'alpha_code: "ERN", '
        'symbol: "Nfk", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "232", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert nakfa.__str__() == 'Nfk -100.00'


def test_nakfa_custom():
    """test_nakfa_custom."""
    amount = 1000
    nakfa = Nakfa(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.amount == decimal
    assert nakfa.numeric_code == '232'
    assert nakfa.alpha_code == 'ERN'
    assert nakfa.decimal_places == 5
    assert nakfa.decimal_sign == ','
    assert nakfa.grouping_sign == '.'
    assert nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert not nakfa.symbol_ahead
    assert nakfa.symbol_separator == '_'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: 1000, '
        'alpha_code: "ERN", '
        'symbol: "Nfk", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "232", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert nakfa.__str__() == 'ERN 1,000.00000'


def test_nakfa_changed():
    """test_cnakfa_changed."""
    nakfa = Nakfa(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.international = True


def test_nakfa_math_add():
    """test_nakfa_math_add."""
    nakfa_one = Nakfa(amount=1)
    nakfa_two = Nakfa(amount=2)
    nakfa_three = Nakfa(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ERN and OTHER.'):
        _ = nakfa_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'nakfa.Nakfa\'> '
                   'and <class \'str\'>.')):
        _ = nakfa_one.__add__('1.00')
    assert (
        nakfa_one +
        nakfa_two) == nakfa_three


def test_nakfa_slots():
    """test_nakfa_slots."""
    nakfa = Nakfa(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Nakfa\' '
                'object has no attribute \'new_variable\'')):
        nakfa.new_variable = 'fail'  # pylint: disable=assigning-non-slot
