# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the UAE Dirham representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, UAEDirham
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_uae_dirham():
    """test_uae_dirham."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    uae_dirham = UAEDirham(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uae_dirham.amount == decimal
    assert uae_dirham.numeric_code == '784'
    assert uae_dirham.alpha_code == 'AED'
    assert uae_dirham.decimal_places == 2
    assert uae_dirham.decimal_sign == '\u066B'
    assert uae_dirham.grouping_sign == '\u066C'
    assert not uae_dirham.international
    assert uae_dirham.symbol == 'د.إ.'
    assert uae_dirham.symbol_ahead
    assert uae_dirham.symbol_separator == '\u00A0'
    assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert uae_dirham.__hash__() == hash((decimal, 'AED', '784'))
    assert uae_dirham.__repr__() == (
        'UAEDirham(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AED", '
        'symbol: "د.إ.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "784", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert uae_dirham.__str__() == 'د.إ. ٠٫١٤'


def test_uae_dirham_negative():
    """test_uae_dirham_negative."""
    amount = -100
    uae_dirham = UAEDirham(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uae_dirham.numeric_code == '784'
    assert uae_dirham.alpha_code == 'AED'
    assert uae_dirham.decimal_places == 2
    assert uae_dirham.decimal_sign == '\u066B'
    assert uae_dirham.grouping_sign == '\u066C'
    assert not uae_dirham.international
    assert uae_dirham.symbol == 'د.إ.'
    assert uae_dirham.symbol_ahead
    assert uae_dirham.symbol_separator == '\u00A0'
    assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert uae_dirham.__hash__() == hash((decimal, 'AED', '784'))
    assert uae_dirham.__repr__() == (
        'UAEDirham(amount: -100, '
        'alpha_code: "AED", '
        'symbol: "د.إ.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "784", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert uae_dirham.__str__() == 'د.إ. -١٠٠٫٠٠'


def test_uae_dirham_custom():
    """test_uae_dirham_custom."""
    amount = 1000
    uae_dirham = UAEDirham(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert uae_dirham.amount == decimal
    assert uae_dirham.numeric_code == '784'
    assert uae_dirham.alpha_code == 'AED'
    assert uae_dirham.decimal_places == 5
    assert uae_dirham.decimal_sign == '\u066C'
    assert uae_dirham.grouping_sign == '\u066B'
    assert uae_dirham.international
    assert uae_dirham.symbol == 'د.إ.'
    assert not uae_dirham.symbol_ahead
    assert uae_dirham.symbol_separator == '_'
    assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert uae_dirham.__hash__() == hash((decimal, 'AED', '784'))
    assert uae_dirham.__repr__() == (
        'UAEDirham(amount: 1000, '
        'alpha_code: "AED", '
        'symbol: "د.إ.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "784", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert uae_dirham.__str__() == 'AED 1,000.00000'


def test_uae_dirham_changed():
    """test_cuae_dirham_changed."""
    uae_dirham = UAEDirham(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uae_dirham.international = True


def test_uae_dirham_math_add():
    """test_uae_dirham_math_add."""
    uae_dirham_one = UAEDirham(amount=1)
    uae_dirham_two = UAEDirham(amount=2)
    uae_dirham_three = UAEDirham(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AED and OTHER.'):
        _ = uae_dirham_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dirham.UAEDirham\'> '
                   'and <class \'str\'>.')):
        _ = uae_dirham_one.__add__('1.00')
    assert (
        uae_dirham_one +
        uae_dirham_two) == uae_dirham_three


def test_uae_dirham_slots():
    """test_uae_dirham_slots."""
    uae_dirham = UAEDirham(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'UAEDirham\' '
                'object has no attribute \'new_variable\'')):
        uae_dirham.new_variable = 'fail'  # pylint: disable=assigning-non-slot
