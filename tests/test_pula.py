# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pula representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Pula
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pula():
    """test_pula."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pula = Pula(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pula.amount == decimal
    assert pula.code == '072'
    assert pula.currency == 'BWP'
    assert pula.decimal_places == 2
    assert pula.decimal_sign == ','
    assert pula.grouping_sign == '.'
    assert not pula.international
    assert pula.symbol == 'P'
    assert pula.__hash__() == hash((decimal, 'BWP', '072'))
    assert pula.__repr__() == (
        'Pula(amount: 0.1428571428571428571428571429, '
        'currency: "BWP", '
        'symbol: "P", '
        'code: "072", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pula.__str__() == 'P0,14'


def test_pula_negative():
    """test_pula_negative."""
    amount = -100
    pula = Pula(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pula.code == '072'
    assert pula.currency == 'BWP'
    assert pula.decimal_places == 2
    assert pula.decimal_sign == ','
    assert pula.grouping_sign == '.'
    assert not pula.international
    assert pula.symbol == 'P'
    assert pula.__hash__() == hash((decimal, 'BWP', '072'))
    assert pula.__repr__() == (
        'Pula(amount: -100, '
        'currency: "BWP", '
        'symbol: "P", '
        'code: "072", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert pula.__str__() == 'P-100,00'


def test_pula_custom():
    """test_pula_custom."""
    amount = 1000
    pula = Pula(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert pula.amount == decimal
    assert pula.code == '072'
    assert pula.currency == 'BWP'
    assert pula.decimal_places == 5
    assert pula.decimal_sign == '.'
    assert pula.grouping_sign == ','
    assert pula.international
    assert pula.symbol == 'P'
    assert pula.__hash__() == hash((decimal, 'BWP', '072'))
    assert pula.__repr__() == (
        'Pula(amount: 1000, '
        'currency: "BWP", '
        'symbol: "P", '
        'code: "072", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert pula.__str__() == 'BWP 1,000.00000'


def test_pula_changed():
    """test_cpula_changed."""
    pula = Pula(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pula.international = True


def test_pula_math_add():
    """test_pula_math_add."""
    pula_one = Pula(amount=1)
    pula_two = Pula(amount=2)
    pula_three = Pula(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BWP and OTHER.'):
        _ = pula_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'pula.Pula\'> '
                   'and <class \'str\'>.')):
        _ = pula_one.__add__('1.00')
    assert (pula_one + pula_two) == pula_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Pula(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Pula\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
