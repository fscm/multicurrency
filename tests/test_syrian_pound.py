# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Syrian Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SyrianPound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_syrian_pound():
    """test_syrian_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    syrian_pound = SyrianPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert syrian_pound.amount == decimal
    assert syrian_pound.numeric_code == '760'
    assert syrian_pound.alpha_code == 'SYP'
    assert syrian_pound.decimal_places == 2
    assert syrian_pound.decimal_sign == '\u066B'
    assert syrian_pound.grouping_sign == '\u066C'
    assert not syrian_pound.international
    assert syrian_pound.symbol == 'ل.س'
    assert not syrian_pound.symbol_ahead
    assert syrian_pound.symbol_separator == '\u00A0'
    assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
    assert syrian_pound.__repr__() == (
        'SyrianPound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SYP", '
        'symbol: "ل.س", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "760", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert syrian_pound.__str__() == '٠٫١٤ ل.س'


def test_syrian_pound_negative():
    """test_syrian_pound_negative."""
    amount = -100
    syrian_pound = SyrianPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert syrian_pound.numeric_code == '760'
    assert syrian_pound.alpha_code == 'SYP'
    assert syrian_pound.decimal_places == 2
    assert syrian_pound.decimal_sign == '\u066B'
    assert syrian_pound.grouping_sign == '\u066C'
    assert not syrian_pound.international
    assert syrian_pound.symbol == 'ل.س'
    assert not syrian_pound.symbol_ahead
    assert syrian_pound.symbol_separator == '\u00A0'
    assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
    assert syrian_pound.__repr__() == (
        'SyrianPound(amount: -100, '
        'alpha_code: "SYP", '
        'symbol: "ل.س", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "760", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert syrian_pound.__str__() == '-١٠٠٫٠٠ ل.س'


def test_syrian_pound_custom():
    """test_syrian_pound_custom."""
    amount = 1000
    syrian_pound = SyrianPound(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert syrian_pound.amount == decimal
    assert syrian_pound.numeric_code == '760'
    assert syrian_pound.alpha_code == 'SYP'
    assert syrian_pound.decimal_places == 5
    assert syrian_pound.decimal_sign == '\u066C'
    assert syrian_pound.grouping_sign == '\u066B'
    assert syrian_pound.international
    assert syrian_pound.symbol == 'ل.س'
    assert not syrian_pound.symbol_ahead
    assert syrian_pound.symbol_separator == '_'
    assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
    assert syrian_pound.__repr__() == (
        'SyrianPound(amount: 1000, '
        'alpha_code: "SYP", '
        'symbol: "ل.س", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "760", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: True)')
    assert syrian_pound.__str__() == 'SYP 1,000.00000'


def test_syrian_pound_changed():
    """test_csyrian_pound_changed."""
    syrian_pound = SyrianPound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        syrian_pound.international = True


def test_syrian_pound_math_add():
    """test_syrian_pound_math_add."""
    syrian_pound_one = SyrianPound(amount=1)
    syrian_pound_two = SyrianPound(amount=2)
    syrian_pound_three = SyrianPound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SYP and OTHER.'):
        _ = syrian_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.SyrianPound\'> '
                   'and <class \'str\'>.')):
        _ = syrian_pound_one.__add__('1.00')
    assert (
        syrian_pound_one +
        syrian_pound_two) == syrian_pound_three


def test_syrian_pound_slots():
    """test_syrian_pound_slots."""
    syrian_pound = SyrianPound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SyrianPound\' '
                'object has no attribute \'new_variable\'')):
        syrian_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
