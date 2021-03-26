# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Som representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Som
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_som():
    """test_som."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    som = Som(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert som.amount == decimal
    assert som.code == '417'
    assert som.currency == 'KGS'
    assert som.decimal_places == 2
    assert som.decimal_sign == ','
    assert som.grouping_sign == '.'
    assert not som.international
    assert som.symbol == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: 0.1428571428571428571428571429, '
        'currency: "KGS", '
        'symbol: "", '
        'code: "417", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert som.__str__() == '0,14'


def test_som_negative():
    """test_som_negative."""
    amount = -100
    som = Som(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert som.code == '417'
    assert som.currency == 'KGS'
    assert som.decimal_places == 2
    assert som.decimal_sign == ','
    assert som.grouping_sign == '.'
    assert not som.international
    assert som.symbol == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: -100, '
        'currency: "KGS", '
        'symbol: "", '
        'code: "417", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert som.__str__() == '-100,00'


def test_som_custom():
    """test_som_custom."""
    amount = 1000
    som = Som(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert som.amount == decimal
    assert som.code == '417'
    assert som.currency == 'KGS'
    assert som.decimal_places == 5
    assert som.decimal_sign == '.'
    assert som.grouping_sign == ','
    assert som.international
    assert som.symbol == ''
    assert som.__hash__() == hash((decimal, 'KGS', '417'))
    assert som.__repr__() == (
        'Som(amount: 1000, '
        'currency: "KGS", '
        'symbol: "", '
        'code: "417", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert som.__str__() == 'KGS 1,000.00000'


def test_som_changed():
    """test_csom_changed."""
    som = Som(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        som.international = True


def test_som_math_add():
    """test_som_math_add."""
    som_one = Som(amount=1)
    som_two = Som(amount=2)
    som_three = Som(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KGS and OTHER.'):
        _ = som_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'som.Som\'> '
                   'and <class \'str\'>.')):
        _ = som_one.__add__('1.00')
    assert (som_one + som_two) == som_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Som(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Som\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
