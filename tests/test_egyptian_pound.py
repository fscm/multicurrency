# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Egyptian Pound representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EgyptianPound
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_egyptian_pound():
    """test_egyptian_pound."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    egyptian_pound = EgyptianPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert egyptian_pound.amount == decimal
    assert egyptian_pound.numeric_code == '818'
    assert egyptian_pound.alpha_code == 'EGP'
    assert egyptian_pound.decimal_places == 2
    assert egyptian_pound.decimal_sign == '\u066B'
    assert egyptian_pound.grouping_sign == '\u066C'
    assert not egyptian_pound.international
    assert egyptian_pound.symbol == 'ج.م.'
    assert egyptian_pound.symbol_ahead
    assert egyptian_pound.symbol_separator == '\u00A0'
    assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
    assert egyptian_pound.__repr__() == (
        'EgyptianPound(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EGP", '
        'symbol: "ج.م.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "818", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert egyptian_pound.__str__() == 'ج.م. ٠٫١٤'


def test_egyptian_pound_negative():
    """test_egyptian_pound_negative."""
    amount = -100
    egyptian_pound = EgyptianPound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert egyptian_pound.numeric_code == '818'
    assert egyptian_pound.alpha_code == 'EGP'
    assert egyptian_pound.decimal_places == 2
    assert egyptian_pound.decimal_sign == '\u066B'
    assert egyptian_pound.grouping_sign == '\u066C'
    assert not egyptian_pound.international
    assert egyptian_pound.symbol == 'ج.م.'
    assert egyptian_pound.symbol_ahead
    assert egyptian_pound.symbol_separator == '\u00A0'
    assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
    assert egyptian_pound.__repr__() == (
        'EgyptianPound(amount: -100, '
        'alpha_code: "EGP", '
        'symbol: "ج.م.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "818", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert egyptian_pound.__str__() == 'ج.م. -١٠٠٫٠٠'


def test_egyptian_pound_custom():
    """test_egyptian_pound_custom."""
    amount = 1000
    egyptian_pound = EgyptianPound(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert egyptian_pound.amount == decimal
    assert egyptian_pound.numeric_code == '818'
    assert egyptian_pound.alpha_code == 'EGP'
    assert egyptian_pound.decimal_places == 5
    assert egyptian_pound.decimal_sign == '\u066C'
    assert egyptian_pound.grouping_sign == '\u066B'
    assert egyptian_pound.international
    assert egyptian_pound.symbol == 'ج.م.'
    assert not egyptian_pound.symbol_ahead
    assert egyptian_pound.symbol_separator == '_'
    assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
    assert egyptian_pound.__repr__() == (
        'EgyptianPound(amount: 1000, '
        'alpha_code: "EGP", '
        'symbol: "ج.م.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "818", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert egyptian_pound.__str__() == 'EGP 1,000.00000'


def test_egyptian_pound_changed():
    """test_cegyptian_pound_changed."""
    egyptian_pound = EgyptianPound(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        egyptian_pound.international = True


def test_egyptian_pound_math_add():
    """test_egyptian_pound_math_add."""
    egyptian_pound_one = EgyptianPound(amount=1)
    egyptian_pound_two = EgyptianPound(amount=2)
    egyptian_pound_three = EgyptianPound(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EGP and OTHER.'):
        _ = egyptian_pound_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pound.EgyptianPound\'> '
                   'and <class \'str\'>.')):
        _ = egyptian_pound_one.__add__('1.00')
    assert (
        egyptian_pound_one +
        egyptian_pound_two) == egyptian_pound_three


def test_egyptian_pound_slots():
    """test_egyptian_pound_slots."""
    egyptian_pound = EgyptianPound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EgyptianPound\' '
                'object has no attribute \'new_variable\'')):
        egyptian_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
