# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ethiopian Birr representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EthiopianBirr
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ethiopian_birr():
    """test_ethiopian_birr."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ethiopian_birr = EthiopianBirr(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ethiopian_birr.amount == decimal
    assert ethiopian_birr.code == '230'
    assert ethiopian_birr.currency == 'ETB'
    assert ethiopian_birr.decimal_places == 2
    assert ethiopian_birr.decimal_sign == ','
    assert ethiopian_birr.grouping_sign == '.'
    assert not ethiopian_birr.international
    assert ethiopian_birr.symbol == ''
    assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
    assert ethiopian_birr.__repr__() == (
        'EthiopianBirr(amount: 0.1428571428571428571428571429, '
        'currency: "ETB", '
        'symbol: "", '
        'code: "230", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ethiopian_birr.__str__() == '0,14'


def test_ethiopian_birr_negative():
    """test_ethiopian_birr_negative."""
    amount = -100
    ethiopian_birr = EthiopianBirr(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ethiopian_birr.code == '230'
    assert ethiopian_birr.currency == 'ETB'
    assert ethiopian_birr.decimal_places == 2
    assert ethiopian_birr.decimal_sign == ','
    assert ethiopian_birr.grouping_sign == '.'
    assert not ethiopian_birr.international
    assert ethiopian_birr.symbol == ''
    assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
    assert ethiopian_birr.__repr__() == (
        'EthiopianBirr(amount: -100, '
        'currency: "ETB", '
        'symbol: "", '
        'code: "230", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ethiopian_birr.__str__() == '-100,00'


def test_ethiopian_birr_custom():
    """test_ethiopian_birr_custom."""
    amount = 1000
    ethiopian_birr = EthiopianBirr(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert ethiopian_birr.amount == decimal
    assert ethiopian_birr.code == '230'
    assert ethiopian_birr.currency == 'ETB'
    assert ethiopian_birr.decimal_places == 5
    assert ethiopian_birr.decimal_sign == '.'
    assert ethiopian_birr.grouping_sign == ','
    assert ethiopian_birr.international
    assert ethiopian_birr.symbol == ''
    assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
    assert ethiopian_birr.__repr__() == (
        'EthiopianBirr(amount: 1000, '
        'currency: "ETB", '
        'symbol: "", '
        'code: "230", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert ethiopian_birr.__str__() == 'ETB 1,000.00000'


def test_ethiopian_birr_changed():
    """test_cethiopian_birr_changed."""
    ethiopian_birr = EthiopianBirr(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethiopian_birr.international = True


def test_ethiopian_birr_math_add():
    """test_ethiopian_birr_math_add."""
    ethiopian_birr_one = EthiopianBirr(amount=1)
    ethiopian_birr_two = EthiopianBirr(amount=2)
    ethiopian_birr_three = EthiopianBirr(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ETB and OTHER.'):
        _ = ethiopian_birr_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'birr.EthiopianBirr\'> '
                   'and <class \'str\'>.')):
        _ = ethiopian_birr_one.__add__('1.00')
    assert (ethiopian_birr_one + ethiopian_birr_two) == ethiopian_birr_three


def test_currency_slots():
    """test_currency_slots."""
    euro = EthiopianBirr(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EthiopianBirr\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
