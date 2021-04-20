# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Moroccan Dirham representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MoroccanDirham
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_moroccan_dirham():
    """test_moroccan_dirham."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    moroccan_dirham = MoroccanDirham(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert moroccan_dirham.amount == decimal
    assert moroccan_dirham.numeric_code == '504'
    assert moroccan_dirham.alpha_code == 'MAD'
    assert moroccan_dirham.decimal_places == 2
    assert moroccan_dirham.decimal_sign == '\u066B'
    assert moroccan_dirham.grouping_sign == '\u066C'
    assert not moroccan_dirham.international
    assert moroccan_dirham.symbol == 'د.م.'
    assert not moroccan_dirham.symbol_ahead
    assert moroccan_dirham.symbol_separator == '\u00A0'
    assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert moroccan_dirham.__hash__() == hash((decimal, 'MAD', '504'))
    assert moroccan_dirham.__repr__() == (
        'MoroccanDirham(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MAD", '
        'symbol: "د.م.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "504", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert moroccan_dirham.__str__() == '٠٫١٤ د.م.'


def test_moroccan_dirham_negative():
    """test_moroccan_dirham_negative."""
    amount = -100
    moroccan_dirham = MoroccanDirham(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert moroccan_dirham.numeric_code == '504'
    assert moroccan_dirham.alpha_code == 'MAD'
    assert moroccan_dirham.decimal_places == 2
    assert moroccan_dirham.decimal_sign == '\u066B'
    assert moroccan_dirham.grouping_sign == '\u066C'
    assert not moroccan_dirham.international
    assert moroccan_dirham.symbol == 'د.م.'
    assert not moroccan_dirham.symbol_ahead
    assert moroccan_dirham.symbol_separator == '\u00A0'
    assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert moroccan_dirham.__hash__() == hash((decimal, 'MAD', '504'))
    assert moroccan_dirham.__repr__() == (
        'MoroccanDirham(amount: -100, '
        'alpha_code: "MAD", '
        'symbol: "د.م.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "504", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: False)')
    assert moroccan_dirham.__str__() == '-١٠٠٫٠٠ د.م.'


def test_moroccan_dirham_custom():
    """test_moroccan_dirham_custom."""
    amount = 1000
    moroccan_dirham = MoroccanDirham(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert moroccan_dirham.amount == decimal
    assert moroccan_dirham.numeric_code == '504'
    assert moroccan_dirham.alpha_code == 'MAD'
    assert moroccan_dirham.decimal_places == 5
    assert moroccan_dirham.decimal_sign == '\u066C'
    assert moroccan_dirham.grouping_sign == '\u066B'
    assert moroccan_dirham.international
    assert moroccan_dirham.symbol == 'د.م.'
    assert not moroccan_dirham.symbol_ahead
    assert moroccan_dirham.symbol_separator == '_'
    assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-\u066C\u066B'
    assert moroccan_dirham.__hash__() == hash((decimal, 'MAD', '504'))
    assert moroccan_dirham.__repr__() == (
        'MoroccanDirham(amount: 1000, '
        'alpha_code: "MAD", '
        'symbol: "د.م.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "504", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-\u066C\u066B", '
        'international: True)')
    assert moroccan_dirham.__str__() == 'MAD 1,000.00000'


def test_moroccan_dirham_changed():
    """test_cmoroccan_dirham_changed."""
    moroccan_dirham = MoroccanDirham(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moroccan_dirham.international = True


def test_moroccan_dirham_math_add():
    """test_moroccan_dirham_math_add."""
    moroccan_dirham_one = MoroccanDirham(amount=1)
    moroccan_dirham_two = MoroccanDirham(amount=2)
    moroccan_dirham_three = MoroccanDirham(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MAD and OTHER.'):
        _ = moroccan_dirham_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dirham.MoroccanDirham\'> '
                   'and <class \'str\'>.')):
        _ = moroccan_dirham_one.__add__('1.00')
    assert (
        moroccan_dirham_one +
        moroccan_dirham_two) == moroccan_dirham_three


def test_moroccan_dirham_slots():
    """test_moroccan_dirham_slots."""
    moroccan_dirham = MoroccanDirham(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MoroccanDirham\' '
                'object has no attribute \'new_variable\'')):
        moroccan_dirham.new_variable = 'fail'  # pylint: disable=assigning-non-slot
