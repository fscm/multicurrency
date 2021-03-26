# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lempira representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Lempira
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lempira():
    """test_lempira."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lempira = Lempira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lempira.amount == decimal
    assert lempira.code == '340'
    assert lempira.currency == 'HNL'
    assert lempira.decimal_places == 2
    assert lempira.decimal_sign == '.'
    assert lempira.grouping_sign == ','
    assert not lempira.international
    assert lempira.symbol == 'L'
    assert lempira.__hash__() == hash((decimal, 'HNL', '340'))
    assert lempira.__repr__() == (
        'Lempira(amount: 0.1428571428571428571428571429, '
        'currency: "HNL", '
        'symbol: "L", '
        'code: "340", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert lempira.__str__() == 'L0.14'


def test_lempira_negative():
    """test_lempira_negative."""
    amount = -100
    lempira = Lempira(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lempira.code == '340'
    assert lempira.currency == 'HNL'
    assert lempira.decimal_places == 2
    assert lempira.decimal_sign == '.'
    assert lempira.grouping_sign == ','
    assert not lempira.international
    assert lempira.symbol == 'L'
    assert lempira.__hash__() == hash((decimal, 'HNL', '340'))
    assert lempira.__repr__() == (
        'Lempira(amount: -100, '
        'currency: "HNL", '
        'symbol: "L", '
        'code: "340", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert lempira.__str__() == 'L-100.00'


def test_lempira_custom():
    """test_lempira_custom."""
    amount = 1000
    lempira = Lempira(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert lempira.amount == decimal
    assert lempira.code == '340'
    assert lempira.currency == 'HNL'
    assert lempira.decimal_places == 5
    assert lempira.decimal_sign == ','
    assert lempira.grouping_sign == '.'
    assert lempira.international
    assert lempira.symbol == 'L'
    assert lempira.__hash__() == hash((decimal, 'HNL', '340'))
    assert lempira.__repr__() == (
        'Lempira(amount: 1000, '
        'currency: "HNL", '
        'symbol: "L", '
        'code: "340", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert lempira.__str__() == 'HNL 1.000,00000'


def test_lempira_changed():
    """test_clempira_changed."""
    lempira = Lempira(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lempira.international = True


def test_lempira_math_add():
    """test_lempira_math_add."""
    lempira_one = Lempira(amount=1)
    lempira_two = Lempira(amount=2)
    lempira_three = Lempira(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency HNL and OTHER.'):
        _ = lempira_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lempira.Lempira\'> '
                   'and <class \'str\'>.')):
        _ = lempira_one.__add__('1.00')
    assert (lempira_one + lempira_two) == lempira_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Lempira(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Lempira\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
