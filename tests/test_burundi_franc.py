# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Burundi Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BurundiFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_burundi_franc():
    """test_burundi_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    burundi_franc = BurundiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.amount == decimal
    assert burundi_franc.numeric_code == '108'
    assert burundi_franc.alpha_code == 'BIF'
    assert burundi_franc.decimal_places == 0
    assert burundi_franc.decimal_sign == ','
    assert burundi_franc.grouping_sign == '\u202F'
    assert not burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert not burundi_franc.symbol_ahead
    assert burundi_franc.symbol_separator == '\u00A0'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BIF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "108", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert burundi_franc.__str__() == '0 ₣'


def test_burundi_franc_negative():
    """test_burundi_franc_negative."""
    amount = -100
    burundi_franc = BurundiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.numeric_code == '108'
    assert burundi_franc.alpha_code == 'BIF'
    assert burundi_franc.decimal_places == 0
    assert burundi_franc.decimal_sign == ','
    assert burundi_franc.grouping_sign == '\u202F'
    assert not burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert not burundi_franc.symbol_ahead
    assert burundi_franc.symbol_separator == '\u00A0'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: -100, '
        'alpha_code: "BIF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "108", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert burundi_franc.__str__() == '-100 ₣'


def test_burundi_franc_custom():
    """test_burundi_franc_custom."""
    amount = 1000
    burundi_franc = BurundiFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.amount == decimal
    assert burundi_franc.numeric_code == '108'
    assert burundi_franc.alpha_code == 'BIF'
    assert burundi_franc.decimal_places == 5
    assert burundi_franc.decimal_sign == '\u202F'
    assert burundi_franc.grouping_sign == ','
    assert burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert not burundi_franc.symbol_ahead
    assert burundi_franc.symbol_separator == '_'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: 1000, '
        'alpha_code: "BIF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "108", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert burundi_franc.__str__() == 'BIF 1,000.00000'


def test_burundi_franc_changed():
    """test_cburundi_franc_changed."""
    burundi_franc = BurundiFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.international = True


def test_burundi_franc_math_add():
    """test_burundi_franc_math_add."""
    burundi_franc_one = BurundiFranc(amount=1)
    burundi_franc_two = BurundiFranc(amount=2)
    burundi_franc_three = BurundiFranc(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BIF and OTHER.'):
        _ = burundi_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.BurundiFranc\'> '
                   'and <class \'str\'>.')):
        _ = burundi_franc_one.__add__('1.00')
    assert (
        burundi_franc_one +
        burundi_franc_two) == burundi_franc_three


def test_burundi_franc_slots():
    """test_burundi_franc_slots."""
    burundi_franc = BurundiFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BurundiFranc\' '
                'object has no attribute \'new_variable\'')):
        burundi_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
