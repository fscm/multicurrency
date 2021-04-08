# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the PZloty representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PZloty
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pzloty():
    """test_pzloty."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pzloty = PZloty(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pzloty.amount == decimal
    assert pzloty.code == '985'
    assert pzloty.currency == 'PLN'
    assert pzloty.decimal_places == 2
    assert pzloty.decimal_sign == ','
    assert pzloty.grouping_sign == '.'
    assert not pzloty.international
    assert pzloty.symbol == 'zł'
    assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
    assert pzloty.__repr__() == (
        'PZloty(amount: 0.1428571428571428571428571429, '
        'currency: "PLN", '
        'symbol: "zł", '
        'code: "985", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pzloty.__str__() == 'zł0,14'


def test_pzloty_negative():
    """test_pzloty_negative."""
    amount = -100
    pzloty = PZloty(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pzloty.code == '985'
    assert pzloty.currency == 'PLN'
    assert pzloty.decimal_places == 2
    assert pzloty.decimal_sign == ','
    assert pzloty.grouping_sign == '.'
    assert not pzloty.international
    assert pzloty.symbol == 'zł'
    assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
    assert pzloty.__repr__() == (
        'PZloty(amount: -100, '
        'currency: "PLN", '
        'symbol: "zł", '
        'code: "985", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pzloty.__str__() == 'zł-100,00'


def test_pzloty_custom():
    """test_pzloty_custom."""
    amount = 1000
    pzloty = PZloty(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert pzloty.amount == decimal
    assert pzloty.code == '985'
    assert pzloty.currency == 'PLN'
    assert pzloty.decimal_places == 5
    assert pzloty.decimal_sign == '.'
    assert pzloty.grouping_sign == ','
    assert pzloty.international
    assert pzloty.symbol == 'zł'
    assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
    assert pzloty.__repr__() == (
        'PZloty(amount: 1000, '
        'currency: "PLN", '
        'symbol: "zł", '
        'code: "985", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert pzloty.__str__() == 'PLN 1,000.00000'


def test_pzloty_changed():
    """test_cpzloty_changed."""
    pzloty = PZloty(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pzloty.international = True


def test_pzloty_math_add():
    """test_pzloty_math_add."""
    pzloty_one = PZloty(amount=1)
    pzloty_two = PZloty(amount=2)
    pzloty_three = PZloty(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PLN and OTHER.'):
        _ = pzloty_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pzloty.PZloty\'> '
                   'and <class \'str\'>.')):
        _ = pzloty_one.__add__('1.00')
    assert (pzloty_one + pzloty_two) == pzloty_three


def test_currency_slots():
    """test_currency_slots."""
    euro = PZloty(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PZloty\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot