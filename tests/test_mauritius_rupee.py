# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Mauritius Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MauritiusRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_mauritius_rupee():
    """test_mauritius_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    mauritius_rupee = MauritiusRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert mauritius_rupee.amount == decimal
    assert mauritius_rupee.numeric_code == '480'
    assert mauritius_rupee.alpha_code == 'MUR'
    assert mauritius_rupee.decimal_places == 2
    assert mauritius_rupee.decimal_sign == '.'
    assert mauritius_rupee.grouping_sign == ','
    assert not mauritius_rupee.international
    assert mauritius_rupee.symbol == '₨'
    assert mauritius_rupee.symbol_ahead
    assert mauritius_rupee.symbol_separator == '\u00A0'
    assert mauritius_rupee.convertion == ''
    assert mauritius_rupee.__hash__() == hash((decimal, 'MUR', '480'))
    assert mauritius_rupee.__repr__() == (
        'MauritiusRupee(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MUR", '
        'symbol: "₨", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "480", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert mauritius_rupee.__str__() == '₨ 0.14'


def test_mauritius_rupee_negative():
    """test_mauritius_rupee_negative."""
    amount = -100
    mauritius_rupee = MauritiusRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert mauritius_rupee.numeric_code == '480'
    assert mauritius_rupee.alpha_code == 'MUR'
    assert mauritius_rupee.decimal_places == 2
    assert mauritius_rupee.decimal_sign == '.'
    assert mauritius_rupee.grouping_sign == ','
    assert not mauritius_rupee.international
    assert mauritius_rupee.symbol == '₨'
    assert mauritius_rupee.symbol_ahead
    assert mauritius_rupee.symbol_separator == '\u00A0'
    assert mauritius_rupee.convertion == ''
    assert mauritius_rupee.__hash__() == hash((decimal, 'MUR', '480'))
    assert mauritius_rupee.__repr__() == (
        'MauritiusRupee(amount: -100, '
        'alpha_code: "MUR", '
        'symbol: "₨", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "480", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert mauritius_rupee.__str__() == '₨ -100.00'


def test_mauritius_rupee_custom():
    """test_mauritius_rupee_custom."""
    amount = 1000
    mauritius_rupee = MauritiusRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert mauritius_rupee.amount == decimal
    assert mauritius_rupee.numeric_code == '480'
    assert mauritius_rupee.alpha_code == 'MUR'
    assert mauritius_rupee.decimal_places == 5
    assert mauritius_rupee.decimal_sign == ','
    assert mauritius_rupee.grouping_sign == '.'
    assert mauritius_rupee.international
    assert mauritius_rupee.symbol == '₨'
    assert not mauritius_rupee.symbol_ahead
    assert mauritius_rupee.symbol_separator == '_'
    assert mauritius_rupee.convertion == ''
    assert mauritius_rupee.__hash__() == hash((decimal, 'MUR', '480'))
    assert mauritius_rupee.__repr__() == (
        'MauritiusRupee(amount: 1000, '
        'alpha_code: "MUR", '
        'symbol: "₨", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "480", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert mauritius_rupee.__str__() == 'MUR 1,000.00000'


def test_mauritius_rupee_changed():
    """test_cmauritius_rupee_changed."""
    mauritius_rupee = MauritiusRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        mauritius_rupee.international = True


def test_mauritius_rupee_math_add():
    """test_mauritius_rupee_math_add."""
    mauritius_rupee_one = MauritiusRupee(amount=1)
    mauritius_rupee_two = MauritiusRupee(amount=2)
    mauritius_rupee_three = MauritiusRupee(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MUR and OTHER.'):
        _ = mauritius_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupee.MauritiusRupee\'> '
                   'and <class \'str\'>.')):
        _ = mauritius_rupee_one.__add__('1.00')
    assert (
        mauritius_rupee_one +
        mauritius_rupee_two) == mauritius_rupee_three


def test_mauritius_rupee_slots():
    """test_mauritius_rupee_slots."""
    mauritius_rupee = MauritiusRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MauritiusRupee\' '
                'object has no attribute \'new_variable\'')):
        mauritius_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
