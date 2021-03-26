# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rufiyaa representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Rufiyaa
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rufiyaa():
    """test_rufiyaa."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rufiyaa = Rufiyaa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.amount == decimal
    assert rufiyaa.code == '462'
    assert rufiyaa.currency == 'MVR'
    assert rufiyaa.decimal_places == 2
    assert rufiyaa.decimal_sign == ','
    assert rufiyaa.grouping_sign == '.'
    assert not rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: 0.1428571428571428571428571429, '
        'currency: "MVR", '
        'symbol: "ރ.", '
        'code: "462", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rufiyaa.__str__() == 'ރ.0,14'


def test_rufiyaa_negative():
    """test_rufiyaa_negative."""
    amount = -100
    rufiyaa = Rufiyaa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.code == '462'
    assert rufiyaa.currency == 'MVR'
    assert rufiyaa.decimal_places == 2
    assert rufiyaa.decimal_sign == ','
    assert rufiyaa.grouping_sign == '.'
    assert not rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: -100, '
        'currency: "MVR", '
        'symbol: "ރ.", '
        'code: "462", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rufiyaa.__str__() == 'ރ.-100,00'


def test_rufiyaa_custom():
    """test_rufiyaa_custom."""
    amount = 1000
    rufiyaa = Rufiyaa(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert rufiyaa.amount == decimal
    assert rufiyaa.code == '462'
    assert rufiyaa.currency == 'MVR'
    assert rufiyaa.decimal_places == 5
    assert rufiyaa.decimal_sign == '.'
    assert rufiyaa.grouping_sign == ','
    assert rufiyaa.international
    assert rufiyaa.symbol == 'ރ.'
    assert rufiyaa.__hash__() == hash((decimal, 'MVR', '462'))
    assert rufiyaa.__repr__() == (
        'Rufiyaa(amount: 1000, '
        'currency: "MVR", '
        'symbol: "ރ.", '
        'code: "462", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert rufiyaa.__str__() == 'MVR 1,000.00000'


def test_rufiyaa_changed():
    """test_crufiyaa_changed."""
    rufiyaa = Rufiyaa(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rufiyaa.international = True


def test_rufiyaa_math_add():
    """test_rufiyaa_math_add."""
    rufiyaa_one = Rufiyaa(amount=1)
    rufiyaa_two = Rufiyaa(amount=2)
    rufiyaa_three = Rufiyaa(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MVR and OTHER.'):
        _ = rufiyaa_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rufiyaa.Rufiyaa\'> '
                   'and <class \'str\'>.')):
        _ = rufiyaa_one.__add__('1.00')
    assert (rufiyaa_one + rufiyaa_two) == rufiyaa_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Rufiyaa(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Rufiyaa\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
