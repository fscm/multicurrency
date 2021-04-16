# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Indian Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, IndianRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_indian_rupee():
    """test_indian_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    indian_rupee = IndianRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert indian_rupee.amount == decimal
    assert indian_rupee.numeric_code == '356'
    assert indian_rupee.alpha_code == 'INR'
    assert indian_rupee.decimal_places == 2
    assert indian_rupee.decimal_sign == '.'
    assert indian_rupee.grouping_sign == ','
    assert not indian_rupee.international
    assert indian_rupee.symbol == '₹'
    assert indian_rupee.symbol_ahead
    assert indian_rupee.symbol_separator == ''
    assert indian_rupee.__hash__() == hash((decimal, 'INR', '356'))
    assert indian_rupee.__repr__() == (
        'IndianRupee(amount: 0.1428571428571428571428571429, '
        'alpha_code: "INR", '
        'symbol: "₹", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "356", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert indian_rupee.__str__() == '₹0.14'


def test_indian_rupee_negative():
    """test_indian_rupee_negative."""
    amount = -100
    indian_rupee = IndianRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert indian_rupee.numeric_code == '356'
    assert indian_rupee.alpha_code == 'INR'
    assert indian_rupee.decimal_places == 2
    assert indian_rupee.decimal_sign == '.'
    assert indian_rupee.grouping_sign == ','
    assert not indian_rupee.international
    assert indian_rupee.symbol == '₹'
    assert indian_rupee.symbol_ahead
    assert indian_rupee.symbol_separator == ''
    assert indian_rupee.__hash__() == hash((decimal, 'INR', '356'))
    assert indian_rupee.__repr__() == (
        'IndianRupee(amount: -100, '
        'alpha_code: "INR", '
        'symbol: "₹", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "356", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert indian_rupee.__str__() == '₹-100.00'


def test_indian_rupee_custom():
    """test_indian_rupee_custom."""
    amount = 1000
    indian_rupee = IndianRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert indian_rupee.amount == decimal
    assert indian_rupee.numeric_code == '356'
    assert indian_rupee.alpha_code == 'INR'
    assert indian_rupee.decimal_places == 5
    assert indian_rupee.decimal_sign == ','
    assert indian_rupee.grouping_sign == '.'
    assert indian_rupee.international
    assert indian_rupee.symbol == '₹'
    assert not indian_rupee.symbol_ahead
    assert indian_rupee.symbol_separator == '_'
    assert indian_rupee.__hash__() == hash((decimal, 'INR', '356'))
    assert indian_rupee.__repr__() == (
        'IndianRupee(amount: 1000, '
        'alpha_code: "INR", '
        'symbol: "₹", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "356", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert indian_rupee.__str__() == 'INR 1,000.00000'


def test_indian_rupee_changed():
    """test_cindian_rupee_changed."""
    indian_rupee = IndianRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        indian_rupee.international = True


def test_indian_rupee_math_add():
    """test_indian_rupee_math_add."""
    indian_rupee_one = IndianRupee(amount=1)
    indian_rupee_two = IndianRupee(amount=2)
    indian_rupee_three = IndianRupee(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency INR and OTHER.'):
        _ = indian_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupee.IndianRupee\'> '
                   'and <class \'str\'>.')):
        _ = indian_rupee_one.__add__('1.00')
    assert (
        indian_rupee_one +
        indian_rupee_two) == indian_rupee_three


def test_indian_rupee_slots():
    """test_indian_rupee_slots."""
    indian_rupee = IndianRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'IndianRupee\' '
                'object has no attribute \'new_variable\'')):
        indian_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
