# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kip representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kip
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kip():
    """test_kip."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kip = Kip(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kip.amount == decimal
    assert kip.code == '418'
    assert kip.currency == 'LAK'
    assert kip.decimal_places == 2
    assert kip.decimal_sign == ','
    assert kip.grouping_sign == '.'
    assert not kip.international
    assert kip.symbol == '₭'
    assert kip.__hash__() == hash((decimal, 'LAK', '418'))
    assert kip.__repr__() == (
        'Kip(amount: 0.1428571428571428571428571429, '
        'currency: "LAK", '
        'symbol: "₭", '
        'code: "418", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kip.__str__() == '₭0,14'


def test_kip_negative():
    """test_kip_negative."""
    amount = -100
    kip = Kip(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kip.code == '418'
    assert kip.currency == 'LAK'
    assert kip.decimal_places == 2
    assert kip.decimal_sign == ','
    assert kip.grouping_sign == '.'
    assert not kip.international
    assert kip.symbol == '₭'
    assert kip.__hash__() == hash((decimal, 'LAK', '418'))
    assert kip.__repr__() == (
        'Kip(amount: -100, '
        'currency: "LAK", '
        'symbol: "₭", '
        'code: "418", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kip.__str__() == '₭-100,00'


def test_kip_custom():
    """test_kip_custom."""
    amount = 1000
    kip = Kip(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kip.amount == decimal
    assert kip.code == '418'
    assert kip.currency == 'LAK'
    assert kip.decimal_places == 5
    assert kip.decimal_sign == '.'
    assert kip.grouping_sign == ','
    assert kip.international
    assert kip.symbol == '₭'
    assert kip.__hash__() == hash((decimal, 'LAK', '418'))
    assert kip.__repr__() == (
        'Kip(amount: 1000, '
        'currency: "LAK", '
        'symbol: "₭", '
        'code: "418", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert kip.__str__() == 'LAK 1,000.00000'


def test_kip_changed():
    """test_ckip_changed."""
    kip = Kip(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kip.international = True


def test_kip_math_add():
    """test_kip_math_add."""
    kip_one = Kip(amount=1)
    kip_two = Kip(amount=2)
    kip_three = Kip(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LAK and OTHER.'):
        _ = kip_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kip.Kip\'> '
                   'and <class \'str\'>.')):
        _ = kip_one.__add__('1.00')
    assert (kip_one + kip_two) == kip_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Kip(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kip\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
