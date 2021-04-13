# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lebanese Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, LebanesePound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lebanese_pound():
    """test_lebanese_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lebanese_pound = LebanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lebanese_pound.amount == decimal
    assert lebanese_pound.numeric_code == '422'
    assert lebanese_pound.alpha_code == 'LBP'
    assert lebanese_pound.decimal_places == 0
    assert lebanese_pound.decimal_sign == '.'
    assert lebanese_pound.grouping_sign == ' '
    assert not lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل", '
        'numeric_code: "422", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: " ", '
        'international: False)')
    assert lebanese_pound.__str__() == 'ل.ل0'


def test_lebanese_pound_negative():
    """test_lebanese_pound_negative."""
    amount = -100
    lebanese_pound = LebanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lebanese_pound.numeric_code == '422'
    assert lebanese_pound.alpha_code == 'LBP'
    assert lebanese_pound.decimal_places == 0
    assert lebanese_pound.decimal_sign == '.'
    assert lebanese_pound.grouping_sign == ' '
    assert not lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: -100, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل", '
        'numeric_code: "422", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: " ", '
        'international: False)')
    assert lebanese_pound.__str__() == 'ل.ل-100'


def test_lebanese_pound_custom():
    """test_lebanese_pound_custom."""
    amount = 1000
    lebanese_pound = LebanesePound(
        amount=amount,
        decimal_places=5,
        decimal_sign=' ',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert lebanese_pound.amount == decimal
    assert lebanese_pound.numeric_code == '422'
    assert lebanese_pound.alpha_code == 'LBP'
    assert lebanese_pound.decimal_places == 5
    assert lebanese_pound.decimal_sign == ' '
    assert lebanese_pound.grouping_sign == '.'
    assert lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: 1000, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل", '
        'numeric_code: "422", '
        'decimal_places: "5", '
        'decimal_sign: " ", '
        'grouping_sign: ".", '
        'international: True)')
    assert lebanese_pound.__str__() == 'LBP 1.000 00000'


def test_lebanese_pound_changed():
    """test_clebanese_pound_changed."""
    lebanese_pound = LebanesePound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.international = True


def test_lebanese_pound_math_add():
    """test_lebanese_pound_math_add."""
    lebanese_pound_one = LebanesePound(amount=1)
    lebanese_pound_two = LebanesePound(amount=2)
    lebanese_pound_three = LebanesePound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LBP and OTHER.'):
        _ = lebanese_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.LebanesePound\'> '
                   'and <class \'str\'>.')):
        _ = lebanese_pound_one.__add__('1.00')
    assert (lebanese_pound_one + lebanese_pound_two) == lebanese_pound_three


def test_currency_slots():
    """test_currency_slots."""
    euro = LebanesePound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'LebanesePound\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
