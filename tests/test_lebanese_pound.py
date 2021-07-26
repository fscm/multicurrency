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
    assert lebanese_pound.decimal_sign == '\u066B'
    assert lebanese_pound.grouping_places == 3
    assert lebanese_pound.grouping_sign == '\u066C'
    assert not lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل.'
    assert lebanese_pound.symbol_ahead
    assert lebanese_pound.symbol_separator == '\u00A0'
    assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "422", '
        'decimal_places: "0", '
        'decimal_sign: "\u066B", '
        'grouping_places: "3", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert lebanese_pound.__str__() == 'ل.ل. ٠'


def test_lebanese_pound_negative():
    """test_lebanese_pound_negative."""
    amount = -100
    lebanese_pound = LebanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lebanese_pound.numeric_code == '422'
    assert lebanese_pound.alpha_code == 'LBP'
    assert lebanese_pound.decimal_places == 0
    assert lebanese_pound.decimal_sign == '\u066B'
    assert lebanese_pound.grouping_places == 3
    assert lebanese_pound.grouping_sign == '\u066C'
    assert not lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل.'
    assert lebanese_pound.symbol_ahead
    assert lebanese_pound.symbol_separator == '\u00A0'
    assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: -100, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "422", '
        'decimal_places: "0", '
        'decimal_sign: "\u066B", '
        'grouping_places: "3", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert lebanese_pound.__str__() == 'ل.ل. -١٠٠'


def test_lebanese_pound_custom():
    """test_lebanese_pound_custom."""
    amount = 1000
    lebanese_pound = LebanesePound(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_places=2,
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert lebanese_pound.amount == decimal
    assert lebanese_pound.numeric_code == '422'
    assert lebanese_pound.alpha_code == 'LBP'
    assert lebanese_pound.decimal_places == 5
    assert lebanese_pound.decimal_sign == '\u066C'
    assert lebanese_pound.grouping_places == 2
    assert lebanese_pound.grouping_sign == '\u066B'
    assert lebanese_pound.international
    assert lebanese_pound.symbol == 'ل.ل.'
    assert not lebanese_pound.symbol_ahead
    assert lebanese_pound.symbol_separator == '_'
    assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
    assert lebanese_pound.__repr__() == (
        'LebanesePound(amount: 1000, '
        'alpha_code: "LBP", '
        'symbol: "ل.ل.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "422", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_places: "2", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert lebanese_pound.__str__() == 'LBP 10,00.00000'


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
        lebanese_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lebanese_pound.symbol_separator = '_'
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
        lebanese_pound.grouping_places = 4
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
    assert (
        lebanese_pound_one +
        lebanese_pound_two) == lebanese_pound_three


def test_lebanese_pound_slots():
    """test_lebanese_pound_slots."""
    lebanese_pound = LebanesePound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'LebanesePound\' '
                'object has no attribute \'new_variable\'')):
        lebanese_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
