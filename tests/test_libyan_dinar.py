# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Libyan Dinar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, LibyanDinar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_libyan_dinar():
    """test_libyan_dinar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    libyan_dinar = LibyanDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.amount == decimal
    assert libyan_dinar.numeric_code == '434'
    assert libyan_dinar.alpha_code == 'LYD'
    assert libyan_dinar.decimal_places == 3
    assert libyan_dinar.decimal_sign == ','
    assert libyan_dinar.grouping_places == 3
    assert libyan_dinar.grouping_sign == '.'
    assert not libyan_dinar.international
    assert libyan_dinar.symbol == 'د.ل.'
    assert libyan_dinar.symbol_ahead
    assert libyan_dinar.symbol_separator == '\u00A0'
    assert libyan_dinar.convertion == ''
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "LYD", '
        'symbol: "د.ل.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "434", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert libyan_dinar.__str__() == 'د.ل. 0,143'


def test_libyan_dinar_negative():
    """test_libyan_dinar_negative."""
    amount = -100
    libyan_dinar = LibyanDinar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.numeric_code == '434'
    assert libyan_dinar.alpha_code == 'LYD'
    assert libyan_dinar.decimal_places == 3
    assert libyan_dinar.decimal_sign == ','
    assert libyan_dinar.grouping_places == 3
    assert libyan_dinar.grouping_sign == '.'
    assert not libyan_dinar.international
    assert libyan_dinar.symbol == 'د.ل.'
    assert libyan_dinar.symbol_ahead
    assert libyan_dinar.symbol_separator == '\u00A0'
    assert libyan_dinar.convertion == ''
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: -100, '
        'alpha_code: "LYD", '
        'symbol: "د.ل.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "434", '
        'decimal_places: "3", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert libyan_dinar.__str__() == 'د.ل. -100,000'


def test_libyan_dinar_custom():
    """test_libyan_dinar_custom."""
    amount = 1000
    libyan_dinar = LibyanDinar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert libyan_dinar.amount == decimal
    assert libyan_dinar.numeric_code == '434'
    assert libyan_dinar.alpha_code == 'LYD'
    assert libyan_dinar.decimal_places == 5
    assert libyan_dinar.decimal_sign == '.'
    assert libyan_dinar.grouping_places == 2
    assert libyan_dinar.grouping_sign == ','
    assert libyan_dinar.international
    assert libyan_dinar.symbol == 'د.ل.'
    assert not libyan_dinar.symbol_ahead
    assert libyan_dinar.symbol_separator == '_'
    assert libyan_dinar.convertion == ''
    assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
    assert libyan_dinar.__repr__() == (
        'LibyanDinar(amount: 1000, '
        'alpha_code: "LYD", '
        'symbol: "د.ل.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "434", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert libyan_dinar.__str__() == 'LYD 10,00.00000'


def test_libyan_dinar_changed():
    """test_clibyan_dinar_changed."""
    libyan_dinar = LibyanDinar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        libyan_dinar.international = True


def test_libyan_dinar_math_add():
    """test_libyan_dinar_math_add."""
    libyan_dinar_one = LibyanDinar(amount=1)
    libyan_dinar_two = LibyanDinar(amount=2)
    libyan_dinar_three = LibyanDinar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LYD and OTHER.'):
        _ = libyan_dinar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.LibyanDinar\'> '
                   'and <class \'str\'>.')):
        _ = libyan_dinar_one.__add__('1.00')
    assert (
        libyan_dinar_one +
        libyan_dinar_two) == libyan_dinar_three


def test_libyan_dinar_slots():
    """test_libyan_dinar_slots."""
    libyan_dinar = LibyanDinar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'LibyanDinar\' '
                'object has no attribute \'new_variable\'')):
        libyan_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
