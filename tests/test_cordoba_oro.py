# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Cordoba Oro representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CordobaOro
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cordoba_oro():
    """test_cordoba_oro."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cordoba_oro = CordobaOro(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cordoba_oro.amount == decimal
    assert cordoba_oro.code == '558'
    assert cordoba_oro.currency == 'NIO'
    assert cordoba_oro.decimal_places == 2
    assert cordoba_oro.decimal_sign == ','
    assert cordoba_oro.grouping_sign == '.'
    assert not cordoba_oro.international
    assert cordoba_oro.symbol == 'C$'
    assert cordoba_oro.__hash__() == hash((decimal, 'NIO', '558'))
    assert cordoba_oro.__repr__() == (
        'CordobaOro(amount: 0.1428571428571428571428571429, '
        'currency: "NIO", '
        'symbol: "C$", '
        'code: "558", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cordoba_oro.__str__() == 'C$0,14'


def test_cordoba_oro_negative():
    """test_cordoba_oro_negative."""
    amount = -100
    cordoba_oro = CordobaOro(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cordoba_oro.code == '558'
    assert cordoba_oro.currency == 'NIO'
    assert cordoba_oro.decimal_places == 2
    assert cordoba_oro.decimal_sign == ','
    assert cordoba_oro.grouping_sign == '.'
    assert not cordoba_oro.international
    assert cordoba_oro.symbol == 'C$'
    assert cordoba_oro.__hash__() == hash((decimal, 'NIO', '558'))
    assert cordoba_oro.__repr__() == (
        'CordobaOro(amount: -100, '
        'currency: "NIO", '
        'symbol: "C$", '
        'code: "558", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cordoba_oro.__str__() == 'C$-100,00'


def test_cordoba_oro_custom():
    """test_cordoba_oro_custom."""
    amount = 1000
    cordoba_oro = CordobaOro(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert cordoba_oro.amount == decimal
    assert cordoba_oro.code == '558'
    assert cordoba_oro.currency == 'NIO'
    assert cordoba_oro.decimal_places == 5
    assert cordoba_oro.decimal_sign == '.'
    assert cordoba_oro.grouping_sign == ','
    assert cordoba_oro.international
    assert cordoba_oro.symbol == 'C$'
    assert cordoba_oro.__hash__() == hash((decimal, 'NIO', '558'))
    assert cordoba_oro.__repr__() == (
        'CordobaOro(amount: 1000, '
        'currency: "NIO", '
        'symbol: "C$", '
        'code: "558", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert cordoba_oro.__str__() == 'NIO 1,000.00000'


def test_cordoba_oro_changed():
    """test_ccordoba_oro_changed."""
    cordoba_oro = CordobaOro(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cordoba_oro.international = True


def test_cordoba_oro_math_add():
    """test_cordoba_oro_math_add."""
    cordoba_oro_one = CordobaOro(amount=1)
    cordoba_oro_two = CordobaOro(amount=2)
    cordoba_oro_three = CordobaOro(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NIO and OTHER.'):
        _ = cordoba_oro_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'cordoba_oro.CordobaOro\'> '
                   'and <class \'str\'>.')):
        _ = cordoba_oro_one.__add__('1.00')
    assert (cordoba_oro_one + cordoba_oro_two) == cordoba_oro_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CordobaOro(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CordobaOro\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
