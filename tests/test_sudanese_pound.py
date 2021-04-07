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
    assert sudanese_pound.code == '938'
    assert sudanese_pound.currency == 'SDG'
    assert sudanese_pound.decimal_places == 2
    assert sudanese_pound.decimal_sign == ','
    assert sudanese_pound.grouping_sign == '.'
    assert not sudanese_pound.international
    assert sudanese_pound.symbol == '£'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: 0.1428571428571428571428571429, '
        'currency: "SDG", '
        'symbol: "£", '
        'code: "938", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert sudanese_pound.__str__() == '£0,14'


def test_sudanese_pound_negative():
    """test_sudanese_pound_negative."""
    amount = -100
    sudanese_pound = SudanesePound(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sudanese_pound.code == '938'
    assert sudanese_pound.currency == 'SDG'
    assert sudanese_pound.decimal_places == 2
    assert sudanese_pound.decimal_sign == ','
    assert sudanese_pound.grouping_sign == '.'
    assert not sudanese_pound.international
    assert sudanese_pound.symbol == '£'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: -100, '
        'currency: "SDG", '
        'symbol: "£", '
        'code: "938", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert sudanese_pound.__str__() == '£-100,00'


def test_sudanese_pound_custom():
    """test_sudanese_pound_custom."""
    amount = 1000
    sudanese_pound = SudanesePound(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert sudanese_pound.amount == decimal
    assert sudanese_pound.code == '938'
    assert sudanese_pound.currency == 'SDG'
    assert sudanese_pound.decimal_places == 5
    assert sudanese_pound.decimal_sign == '.'
    assert sudanese_pound.grouping_sign == ','
    assert sudanese_pound.international
    assert sudanese_pound.symbol == '£'
    assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
    assert sudanese_pound.__repr__() == (
        'SudanesePound(amount: 1000, '
        'currency: "SDG", '
        'symbol: "£", '
        'code: "938", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
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
        sudanese_pound.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sudanese_pound.code = '978'
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
    currency = Currency(amount=1, currency='OTHER')
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
    assert (sudanese_pound_one + sudanese_pound_two) == sudanese_pound_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SudanesePound(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SudanesePound\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
