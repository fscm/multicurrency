# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwacha representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kwacha
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kwacha():
    """test_kwacha."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kwacha = Kwacha(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwacha.amount == decimal
    assert kwacha.code == '454'
    assert kwacha.currency == 'MWK'
    assert kwacha.decimal_places == 2
    assert kwacha.decimal_sign == ','
    assert kwacha.grouping_sign == '.'
    assert not kwacha.international
    assert kwacha.symbol == 'MK'
    assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
    assert kwacha.__repr__() == (
        'Kwacha(amount: 0.1428571428571428571428571429, '
        'currency: "MWK", '
        'symbol: "MK", '
        'code: "454", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kwacha.__str__() == 'MK0,14'


def test_kwacha_negative():
    """test_kwacha_negative."""
    amount = -100
    kwacha = Kwacha(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwacha.code == '454'
    assert kwacha.currency == 'MWK'
    assert kwacha.decimal_places == 2
    assert kwacha.decimal_sign == ','
    assert kwacha.grouping_sign == '.'
    assert not kwacha.international
    assert kwacha.symbol == 'MK'
    assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
    assert kwacha.__repr__() == (
        'Kwacha(amount: -100, '
        'currency: "MWK", '
        'symbol: "MK", '
        'code: "454", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kwacha.__str__() == 'MK-100,00'


def test_kwacha_custom():
    """test_kwacha_custom."""
    amount = 1000
    kwacha = Kwacha(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kwacha.amount == decimal
    assert kwacha.code == '454'
    assert kwacha.currency == 'MWK'
    assert kwacha.decimal_places == 5
    assert kwacha.decimal_sign == '.'
    assert kwacha.grouping_sign == ','
    assert kwacha.international
    assert kwacha.symbol == 'MK'
    assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
    assert kwacha.__repr__() == (
        'Kwacha(amount: 1000, '
        'currency: "MWK", '
        'symbol: "MK", '
        'code: "454", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert kwacha.__str__() == 'MWK 1,000.00000'


def test_kwacha_changed():
    """test_ckwacha_changed."""
    kwacha = Kwacha(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwacha.international = True


def test_kwacha_math_add():
    """test_kwacha_math_add."""
    kwacha_one = Kwacha(amount=1)
    kwacha_two = Kwacha(amount=2)
    kwacha_three = Kwacha(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MWK and OTHER.'):
        _ = kwacha_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kwacha.Kwacha\'> '
                   'and <class \'str\'>.')):
        _ = kwacha_one.__add__('1.00')
    assert (kwacha_one + kwacha_two) == kwacha_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Kwacha(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kwacha\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
