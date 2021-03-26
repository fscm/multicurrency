# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leone representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Leone
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_leone():
    """test_leone."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    leone = Leone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert leone.amount == decimal
    assert leone.code == '694'
    assert leone.currency == 'SLL'
    assert leone.decimal_places == 2
    assert leone.decimal_sign == ','
    assert leone.grouping_sign == '.'
    assert not leone.international
    assert leone.symbol == 'Le'
    assert leone.__hash__() == hash((decimal, 'SLL', '694'))
    assert leone.__repr__() == (
        'Leone(amount: 0.1428571428571428571428571429, '
        'currency: "SLL", '
        'symbol: "Le", '
        'code: "694", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert leone.__str__() == 'Le0,14'


def test_leone_negative():
    """test_leone_negative."""
    amount = -100
    leone = Leone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert leone.code == '694'
    assert leone.currency == 'SLL'
    assert leone.decimal_places == 2
    assert leone.decimal_sign == ','
    assert leone.grouping_sign == '.'
    assert not leone.international
    assert leone.symbol == 'Le'
    assert leone.__hash__() == hash((decimal, 'SLL', '694'))
    assert leone.__repr__() == (
        'Leone(amount: -100, '
        'currency: "SLL", '
        'symbol: "Le", '
        'code: "694", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert leone.__str__() == 'Le-100,00'


def test_leone_custom():
    """test_leone_custom."""
    amount = 1000
    leone = Leone(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert leone.amount == decimal
    assert leone.code == '694'
    assert leone.currency == 'SLL'
    assert leone.decimal_places == 5
    assert leone.decimal_sign == '.'
    assert leone.grouping_sign == ','
    assert leone.international
    assert leone.symbol == 'Le'
    assert leone.__hash__() == hash((decimal, 'SLL', '694'))
    assert leone.__repr__() == (
        'Leone(amount: 1000, '
        'currency: "SLL", '
        'symbol: "Le", '
        'code: "694", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert leone.__str__() == 'SLL 1,000.00000'


def test_leone_changed():
    """test_cleone_changed."""
    leone = Leone(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leone.international = True


def test_leone_math_add():
    """test_leone_math_add."""
    leone_one = Leone(amount=1)
    leone_two = Leone(amount=2)
    leone_three = Leone(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SLL and OTHER.'):
        _ = leone_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'leone.Leone\'> '
                   'and <class \'str\'>.')):
        _ = leone_one.__add__('1.00')
    assert (leone_one + leone_two) == leone_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Leone(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Leone\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
