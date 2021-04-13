# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Turkish Lira representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, TurkishLira
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_turkish_lira():
    """test_turkish_lira."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    turkish_lira = TurkishLira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert turkish_lira.amount == decimal
    assert turkish_lira.numeric_code == '949'
    assert turkish_lira.alpha_code == 'TRY'
    assert turkish_lira.decimal_places == 2
    assert turkish_lira.decimal_sign == '.'
    assert turkish_lira.grouping_sign == ','
    assert not turkish_lira.international
    assert turkish_lira.symbol == '₤'
    assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
    assert turkish_lira.__repr__() == (
        'TurkishLira(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TRY", '
        'symbol: "₤", '
        'numeric_code: "949", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert turkish_lira.__str__() == '₤0.14'


def test_turkish_lira_negative():
    """test_turkish_lira_negative."""
    amount = -100
    turkish_lira = TurkishLira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert turkish_lira.numeric_code == '949'
    assert turkish_lira.alpha_code == 'TRY'
    assert turkish_lira.decimal_places == 2
    assert turkish_lira.decimal_sign == '.'
    assert turkish_lira.grouping_sign == ','
    assert not turkish_lira.international
    assert turkish_lira.symbol == '₤'
    assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
    assert turkish_lira.__repr__() == (
        'TurkishLira(amount: -100, '
        'alpha_code: "TRY", '
        'symbol: "₤", '
        'numeric_code: "949", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert turkish_lira.__str__() == '₤-100.00'


def test_turkish_lira_custom():
    """test_turkish_lira_custom."""
    amount = 1000
    turkish_lira = TurkishLira(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert turkish_lira.amount == decimal
    assert turkish_lira.numeric_code == '949'
    assert turkish_lira.alpha_code == 'TRY'
    assert turkish_lira.decimal_places == 5
    assert turkish_lira.decimal_sign == ','
    assert turkish_lira.grouping_sign == '.'
    assert turkish_lira.international
    assert turkish_lira.symbol == '₤'
    assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
    assert turkish_lira.__repr__() == (
        'TurkishLira(amount: 1000, '
        'alpha_code: "TRY", '
        'symbol: "₤", '
        'numeric_code: "949", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert turkish_lira.__str__() == 'TRY 1.000,00000'


def test_turkish_lira_changed():
    """test_cturkish_lira_changed."""
    turkish_lira = TurkishLira(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        turkish_lira.international = True


def test_turkish_lira_math_add():
    """test_turkish_lira_math_add."""
    turkish_lira_one = TurkishLira(amount=1)
    turkish_lira_two = TurkishLira(amount=2)
    turkish_lira_three = TurkishLira(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TRY and OTHER.'):
        _ = turkish_lira_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lira.TurkishLira\'> '
                   'and <class \'str\'>.')):
        _ = turkish_lira_one.__add__('1.00')
    assert (turkish_lira_one + turkish_lira_two) == turkish_lira_three


def test_currency_slots():
    """test_currency_slots."""
    euro = TurkishLira(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'TurkishLira\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
