# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Quetzal representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Quetzal
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_quetzal():
    """test_quetzal."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    quetzal = Quetzal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert quetzal.amount == decimal
    assert quetzal.code == '320'
    assert quetzal.currency == 'GTQ'
    assert quetzal.decimal_places == 2
    assert quetzal.decimal_sign == ','
    assert quetzal.grouping_sign == '.'
    assert not quetzal.international
    assert quetzal.symbol == 'Q'
    assert quetzal.__hash__() == hash((decimal, 'GTQ', '320'))
    assert quetzal.__repr__() == (
        'Quetzal(amount: 0.1428571428571428571428571429, '
        'currency: "GTQ", '
        'symbol: "Q", '
        'code: "320", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert quetzal.__str__() == 'Q0,14'


def test_quetzal_negative():
    """test_quetzal_negative."""
    amount = -100
    quetzal = Quetzal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert quetzal.code == '320'
    assert quetzal.currency == 'GTQ'
    assert quetzal.decimal_places == 2
    assert quetzal.decimal_sign == ','
    assert quetzal.grouping_sign == '.'
    assert not quetzal.international
    assert quetzal.symbol == 'Q'
    assert quetzal.__hash__() == hash((decimal, 'GTQ', '320'))
    assert quetzal.__repr__() == (
        'Quetzal(amount: -100, '
        'currency: "GTQ", '
        'symbol: "Q", '
        'code: "320", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert quetzal.__str__() == 'Q-100,00'


def test_quetzal_custom():
    """test_quetzal_custom."""
    amount = 1000
    quetzal = Quetzal(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert quetzal.amount == decimal
    assert quetzal.code == '320'
    assert quetzal.currency == 'GTQ'
    assert quetzal.decimal_places == 5
    assert quetzal.decimal_sign == '.'
    assert quetzal.grouping_sign == ','
    assert quetzal.international
    assert quetzal.symbol == 'Q'
    assert quetzal.__hash__() == hash((decimal, 'GTQ', '320'))
    assert quetzal.__repr__() == (
        'Quetzal(amount: 1000, '
        'currency: "GTQ", '
        'symbol: "Q", '
        'code: "320", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert quetzal.__str__() == 'GTQ 1,000.00000'


def test_quetzal_changed():
    """test_cquetzal_changed."""
    quetzal = Quetzal(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        quetzal.international = True


def test_quetzal_math_add():
    """test_quetzal_math_add."""
    quetzal_one = Quetzal(amount=1)
    quetzal_two = Quetzal(amount=2)
    quetzal_three = Quetzal(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GTQ and OTHER.'):
        _ = quetzal_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'quetzal.Quetzal\'> '
                   'and <class \'str\'>.')):
        _ = quetzal_one.__add__('1.00')
    assert (quetzal_one + quetzal_two) == quetzal_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Quetzal(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Quetzal\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot