# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ouguiya representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Ouguiya
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ouguiya():
    """test_ouguiya."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ouguiya = Ouguiya(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.amount == decimal
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 2
    assert ouguiya.decimal_sign == '\u066B'
    assert ouguiya.grouping_sign == '\u066C'
    assert not ouguiya.international
    assert ouguiya.symbol == 'أ.م'
    assert not ouguiya.symbol_ahead
    assert ouguiya.symbol_separator == '\u00A0'
    assert ouguiya.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MRU", '
        'symbol: "أ.م", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "929", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert ouguiya.__str__() == '٠٫١٤ أ.م'


def test_ouguiya_negative():
    """test_ouguiya_negative."""
    amount = -100
    ouguiya = Ouguiya(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 2
    assert ouguiya.decimal_sign == '\u066B'
    assert ouguiya.grouping_sign == '\u066C'
    assert not ouguiya.international
    assert ouguiya.symbol == 'أ.م'
    assert not ouguiya.symbol_ahead
    assert ouguiya.symbol_separator == '\u00A0'
    assert ouguiya.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: -100, '
        'alpha_code: "MRU", '
        'symbol: "أ.م", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "929", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert ouguiya.__str__() == '-١٠٠٫٠٠ أ.م'


def test_ouguiya_custom():
    """test_ouguiya_custom."""
    amount = 1000
    ouguiya = Ouguiya(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert ouguiya.amount == decimal
    assert ouguiya.numeric_code == '929'
    assert ouguiya.alpha_code == 'MRU'
    assert ouguiya.decimal_places == 5
    assert ouguiya.decimal_sign == '\u066C'
    assert ouguiya.grouping_sign == '\u066B'
    assert ouguiya.international
    assert ouguiya.symbol == 'أ.م'
    assert not ouguiya.symbol_ahead
    assert ouguiya.symbol_separator == '_'
    assert ouguiya.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert ouguiya.__hash__() == hash((decimal, 'MRU', '929'))
    assert ouguiya.__repr__() == (
        'Ouguiya(amount: 1000, '
        'alpha_code: "MRU", '
        'symbol: "أ.م", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "929", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: True)')
    assert ouguiya.__str__() == 'MRU 1,000.00000'


def test_ouguiya_changed():
    """test_couguiya_changed."""
    ouguiya = Ouguiya(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ouguiya.international = True


def test_ouguiya_math_add():
    """test_ouguiya_math_add."""
    ouguiya_one = Ouguiya(amount=1)
    ouguiya_two = Ouguiya(amount=2)
    ouguiya_three = Ouguiya(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MRU and OTHER.'):
        _ = ouguiya_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ouguiya.Ouguiya\'> '
                   'and <class \'str\'>.')):
        _ = ouguiya_one.__add__('1.00')
    assert (
        ouguiya_one +
        ouguiya_two) == ouguiya_three


def test_ouguiya_slots():
    """test_ouguiya_slots."""
    ouguiya = Ouguiya(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Ouguiya\' '
                'object has no attribute \'new_variable\'')):
        ouguiya.new_variable = 'fail'  # pylint: disable=assigning-non-slot
