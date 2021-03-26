# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Riel representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Riel
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_riel():
    """test_riel."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    riel = Riel(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert riel.amount == decimal
    assert riel.code == '116'
    assert riel.currency == 'KHR'
    assert riel.decimal_places == 2
    assert riel.decimal_sign == ','
    assert riel.grouping_sign == '.'
    assert not riel.international
    assert riel.symbol == '៛'
    assert riel.__hash__() == hash((decimal, 'KHR', '116'))
    assert riel.__repr__() == (
        'Riel(amount: 0.1428571428571428571428571429, '
        'currency: "KHR", '
        'symbol: "៛", '
        'code: "116", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert riel.__str__() == '៛0,14'


def test_riel_negative():
    """test_riel_negative."""
    amount = -100
    riel = Riel(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert riel.code == '116'
    assert riel.currency == 'KHR'
    assert riel.decimal_places == 2
    assert riel.decimal_sign == ','
    assert riel.grouping_sign == '.'
    assert not riel.international
    assert riel.symbol == '៛'
    assert riel.__hash__() == hash((decimal, 'KHR', '116'))
    assert riel.__repr__() == (
        'Riel(amount: -100, '
        'currency: "KHR", '
        'symbol: "៛", '
        'code: "116", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert riel.__str__() == '៛-100,00'


def test_riel_custom():
    """test_riel_custom."""
    amount = 1000
    riel = Riel(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert riel.amount == decimal
    assert riel.code == '116'
    assert riel.currency == 'KHR'
    assert riel.decimal_places == 5
    assert riel.decimal_sign == '.'
    assert riel.grouping_sign == ','
    assert riel.international
    assert riel.symbol == '៛'
    assert riel.__hash__() == hash((decimal, 'KHR', '116'))
    assert riel.__repr__() == (
        'Riel(amount: 1000, '
        'currency: "KHR", '
        'symbol: "៛", '
        'code: "116", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert riel.__str__() == 'KHR 1,000.00000'


def test_riel_changed():
    """test_criel_changed."""
    riel = Riel(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        riel.international = True


def test_riel_math_add():
    """test_riel_math_add."""
    riel_one = Riel(amount=1)
    riel_two = Riel(amount=2)
    riel_three = Riel(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KHR and OTHER.'):
        _ = riel_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'riel.Riel\'> '
                   'and <class \'str\'>.')):
        _ = riel_one.__add__('1.00')
    assert (riel_one + riel_two) == riel_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Riel(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Riel\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
