# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Czech Koruna representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CzechKoruna
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_czech_koruna():
    """test_czech_koruna."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    czech_koruna = CzechKoruna(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert czech_koruna.amount == decimal
    assert czech_koruna.code == '203'
    assert czech_koruna.currency == 'CZK'
    assert czech_koruna.decimal_places == 2
    assert czech_koruna.decimal_sign == ','
    assert czech_koruna.grouping_sign == '.'
    assert not czech_koruna.international
    assert czech_koruna.symbol == 'Kč'
    assert czech_koruna.__hash__() == hash((decimal, 'CZK', '203'))
    assert czech_koruna.__repr__() == (
        'CzechKoruna(amount: 0.1428571428571428571428571429, '
        'currency: "CZK", '
        'symbol: "Kč", '
        'code: "203", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert czech_koruna.__str__() == 'Kč0,14'


def test_czech_koruna_negative():
    """test_czech_koruna_negative."""
    amount = -100
    czech_koruna = CzechKoruna(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert czech_koruna.code == '203'
    assert czech_koruna.currency == 'CZK'
    assert czech_koruna.decimal_places == 2
    assert czech_koruna.decimal_sign == ','
    assert czech_koruna.grouping_sign == '.'
    assert not czech_koruna.international
    assert czech_koruna.symbol == 'Kč'
    assert czech_koruna.__hash__() == hash((decimal, 'CZK', '203'))
    assert czech_koruna.__repr__() == (
        'CzechKoruna(amount: -100, '
        'currency: "CZK", '
        'symbol: "Kč", '
        'code: "203", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert czech_koruna.__str__() == 'Kč-100,00'


def test_czech_koruna_custom():
    """test_czech_koruna_custom."""
    amount = 1000
    czech_koruna = CzechKoruna(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert czech_koruna.amount == decimal
    assert czech_koruna.code == '203'
    assert czech_koruna.currency == 'CZK'
    assert czech_koruna.decimal_places == 5
    assert czech_koruna.decimal_sign == '.'
    assert czech_koruna.grouping_sign == ','
    assert czech_koruna.international
    assert czech_koruna.symbol == 'Kč'
    assert czech_koruna.__hash__() == hash((decimal, 'CZK', '203'))
    assert czech_koruna.__repr__() == (
        'CzechKoruna(amount: 1000, '
        'currency: "CZK", '
        'symbol: "Kč", '
        'code: "203", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert czech_koruna.__str__() == 'CZK 1,000.00000'


def test_czech_koruna_changed():
    """test_cczech_koruna_changed."""
    czech_koruna = CzechKoruna(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        czech_koruna.international = True


def test_czech_koruna_math_add():
    """test_czech_koruna_math_add."""
    czech_koruna_one = CzechKoruna(amount=1)
    czech_koruna_two = CzechKoruna(amount=2)
    czech_koruna_three = CzechKoruna(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CZK and OTHER.'):
        _ = czech_koruna_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'czech_koruna.CzechKoruna\'> '
                   'and <class \'str\'>.')):
        _ = czech_koruna_one.__add__('1.00')
    assert (czech_koruna_one + czech_koruna_two) == czech_koruna_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CzechKoruna(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CzechKoruna\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
