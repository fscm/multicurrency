# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Uzbekistan Sum representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, UzbekistanSum
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_uzbekistan_sum():
    """test_uzbekistan_sum."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    uzbekistan_sum = UzbekistanSum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.amount == decimal
    assert uzbekistan_sum.code == '860'
    assert uzbekistan_sum.currency == 'UZS'
    assert uzbekistan_sum.decimal_places == 2
    assert uzbekistan_sum.decimal_sign == ','
    assert uzbekistan_sum.grouping_sign == '.'
    assert not uzbekistan_sum.international
    assert uzbekistan_sum.symbol == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: 0.1428571428571428571428571429, '
        'currency: "UZS", '
        'symbol: "", '
        'code: "860", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert uzbekistan_sum.__str__() == '0,14'


def test_uzbekistan_sum_negative():
    """test_uzbekistan_sum_negative."""
    amount = -100
    uzbekistan_sum = UzbekistanSum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.code == '860'
    assert uzbekistan_sum.currency == 'UZS'
    assert uzbekistan_sum.decimal_places == 2
    assert uzbekistan_sum.decimal_sign == ','
    assert uzbekistan_sum.grouping_sign == '.'
    assert not uzbekistan_sum.international
    assert uzbekistan_sum.symbol == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: -100, '
        'currency: "UZS", '
        'symbol: "", '
        'code: "860", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert uzbekistan_sum.__str__() == '-100,00'


def test_uzbekistan_sum_custom():
    """test_uzbekistan_sum_custom."""
    amount = 1000
    uzbekistan_sum = UzbekistanSum(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert uzbekistan_sum.amount == decimal
    assert uzbekistan_sum.code == '860'
    assert uzbekistan_sum.currency == 'UZS'
    assert uzbekistan_sum.decimal_places == 5
    assert uzbekistan_sum.decimal_sign == '.'
    assert uzbekistan_sum.grouping_sign == ','
    assert uzbekistan_sum.international
    assert uzbekistan_sum.symbol == ''
    assert uzbekistan_sum.__hash__() == hash((decimal, 'UZS', '860'))
    assert uzbekistan_sum.__repr__() == (
        'UzbekistanSum(amount: 1000, '
        'currency: "UZS", '
        'symbol: "", '
        'code: "860", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert uzbekistan_sum.__str__() == 'UZS 1,000.00000'


def test_uzbekistan_sum_changed():
    """test_cuzbekistan_sum_changed."""
    uzbekistan_sum = UzbekistanSum(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        uzbekistan_sum.international = True


def test_uzbekistan_sum_math_add():
    """test_uzbekistan_sum_math_add."""
    uzbekistan_sum_one = UzbekistanSum(amount=1)
    uzbekistan_sum_two = UzbekistanSum(amount=2)
    uzbekistan_sum_three = UzbekistanSum(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency UZS and OTHER.'):
        _ = uzbekistan_sum_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'sum.UzbekistanSum\'> '
                   'and <class \'str\'>.')):
        _ = uzbekistan_sum_one.__add__('1.00')
    assert (uzbekistan_sum_one + uzbekistan_sum_two) == uzbekistan_sum_three


def test_currency_slots():
    """test_currency_slots."""
    euro = UzbekistanSum(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'UzbekistanSum\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
