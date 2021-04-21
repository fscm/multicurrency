# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Sudanese Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SudanesePound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_sudanese_pound():
    """test_sudanese_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    sudanese_pound = SudanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sudanese_pound.amount == decimal
    assert sudanese_pound.numeric_code == '938'
    assert sudanese_pound.alpha_code == 'SDG'
    assert sudanese_pound.decimal_places == 2
    assert sudanese_pound.decimal_sign == '\u066B'
    assert sudanese_pound.grouping_sign == '\u066C'
    assert not sudanese_pound.international
    assert sudanese_pound.symbol == 'ج.س'
    assert not sudanese_pound.symbol_ahead
    assert sudanese_pound.symbol_separator == '\u00A0'
    assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SDG", '
        'symbol: "ج.س", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "938", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert sudanese_pound.__str__() == '٠٫١٤ ج.س'


def test_sudanese_pound_negative():
    """test_sudanese_pound_negative."""
    amount = -100
    sudanese_pound = SudanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sudanese_pound.numeric_code == '938'
    assert sudanese_pound.alpha_code == 'SDG'
    assert sudanese_pound.decimal_places == 2
    assert sudanese_pound.decimal_sign == '\u066B'
    assert sudanese_pound.grouping_sign == '\u066C'
    assert not sudanese_pound.international
    assert sudanese_pound.symbol == 'ج.س'
    assert not sudanese_pound.symbol_ahead
    assert sudanese_pound.symbol_separator == '\u00A0'
    assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: -100, '
        'alpha_code: "SDG", '
        'symbol: "ج.س", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "938", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert sudanese_pound.__str__() == '-١٠٠٫٠٠ ج.س'


def test_sudanese_pound_custom():
    """test_sudanese_pound_custom."""
    amount = 1000
    sudanese_pound = SudanesePound(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert sudanese_pound.amount == decimal
    assert sudanese_pound.numeric_code == '938'
    assert sudanese_pound.alpha_code == 'SDG'
    assert sudanese_pound.decimal_places == 5
    assert sudanese_pound.decimal_sign == '\u066C'
    assert sudanese_pound.grouping_sign == '\u066B'
    assert sudanese_pound.international
    assert sudanese_pound.symbol == 'ج.س'
    assert not sudanese_pound.symbol_ahead
    assert sudanese_pound.symbol_separator == '_'
    assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: 1000, '
        'alpha_code: "SDG", '
        'symbol: "ج.س", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "938", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert sudanese_pound.__str__() == 'SDG 1,000.00000'


def test_sudanese_pound_changed():
    """test_csudanese_pound_changed."""
    sudanese_pound = SudanesePound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.international = True


def test_sudanese_pound_math_add():
    """test_sudanese_pound_math_add."""
    sudanese_pound_one = SudanesePound(amount=1)
    sudanese_pound_two = SudanesePound(amount=2)
    sudanese_pound_three = SudanesePound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SDG and OTHER.'):
        _ = sudanese_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.SudanesePound\'> '
                   'and <class \'str\'>.')):
        _ = sudanese_pound_one.__add__('1.00')
    assert (
        sudanese_pound_one +
        sudanese_pound_two) == sudanese_pound_three


def test_sudanese_pound_slots():
    """test_sudanese_pound_slots."""
    sudanese_pound = SudanesePound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SudanesePound\' '
                'object has no attribute \'new_variable\'')):
        sudanese_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
