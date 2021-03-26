# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Zambian Kwacha representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ZambianKwacha
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_zambian_kwacha():
    """test_zambian_kwacha."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    zambian_kwacha = ZambianKwacha(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zambian_kwacha.amount == decimal
    assert zambian_kwacha.code == '967'
    assert zambian_kwacha.currency == 'ZMW'
    assert zambian_kwacha.decimal_places == 2
    assert zambian_kwacha.decimal_sign == ','
    assert zambian_kwacha.grouping_sign == '.'
    assert not zambian_kwacha.international
    assert zambian_kwacha.symbol == 'ZK'
    assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
    assert zambian_kwacha.__repr__() == (
        'ZambianKwacha(amount: 0.1428571428571428571428571429, '
        'currency: "ZMW", '
        'symbol: "ZK", '
        'code: "967", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert zambian_kwacha.__str__() == 'ZK0,14'


def test_zambian_kwacha_negative():
    """test_zambian_kwacha_negative."""
    amount = -100
    zambian_kwacha = ZambianKwacha(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert zambian_kwacha.code == '967'
    assert zambian_kwacha.currency == 'ZMW'
    assert zambian_kwacha.decimal_places == 2
    assert zambian_kwacha.decimal_sign == ','
    assert zambian_kwacha.grouping_sign == '.'
    assert not zambian_kwacha.international
    assert zambian_kwacha.symbol == 'ZK'
    assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
    assert zambian_kwacha.__repr__() == (
        'ZambianKwacha(amount: -100, '
        'currency: "ZMW", '
        'symbol: "ZK", '
        'code: "967", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert zambian_kwacha.__str__() == 'ZK-100,00'


def test_zambian_kwacha_custom():
    """test_zambian_kwacha_custom."""
    amount = 1000
    zambian_kwacha = ZambianKwacha(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert zambian_kwacha.amount == decimal
    assert zambian_kwacha.code == '967'
    assert zambian_kwacha.currency == 'ZMW'
    assert zambian_kwacha.decimal_places == 5
    assert zambian_kwacha.decimal_sign == '.'
    assert zambian_kwacha.grouping_sign == ','
    assert zambian_kwacha.international
    assert zambian_kwacha.symbol == 'ZK'
    assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
    assert zambian_kwacha.__repr__() == (
        'ZambianKwacha(amount: 1000, '
        'currency: "ZMW", '
        'symbol: "ZK", '
        'code: "967", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert zambian_kwacha.__str__() == 'ZMW 1,000.00000'


def test_zambian_kwacha_changed():
    """test_czambian_kwacha_changed."""
    zambian_kwacha = ZambianKwacha(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        zambian_kwacha.international = True


def test_zambian_kwacha_math_add():
    """test_zambian_kwacha_math_add."""
    zambian_kwacha_one = ZambianKwacha(amount=1)
    zambian_kwacha_two = ZambianKwacha(amount=2)
    zambian_kwacha_three = ZambianKwacha(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZMW and OTHER.'):
        _ = zambian_kwacha_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'zambian_kwacha.ZambianKwacha\'> '
                   'and <class \'str\'>.')):
        _ = zambian_kwacha_one.__add__('1.00')
    assert (zambian_kwacha_one + zambian_kwacha_two) == zambian_kwacha_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ZambianKwacha(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ZambianKwacha\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
