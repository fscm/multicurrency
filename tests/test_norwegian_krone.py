# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Norwegian Krone representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NorwegianKrone
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_norwegian_krone():
    """test_norwegian_krone."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    norwegian_krone = NorwegianKrone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert norwegian_krone.amount == decimal
    assert norwegian_krone.code == '578'
    assert norwegian_krone.currency == 'NOK'
    assert norwegian_krone.decimal_places == 2
    assert norwegian_krone.decimal_sign == ','
    assert norwegian_krone.grouping_sign == '.'
    assert not norwegian_krone.international
    assert norwegian_krone.symbol == 'kr'
    assert norwegian_krone.__hash__() == hash((decimal, 'NOK', '578'))
    assert norwegian_krone.__repr__() == (
        'NorwegianKrone(amount: 0.1428571428571428571428571429, '
        'currency: "NOK", '
        'symbol: "kr", '
        'code: "578", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert norwegian_krone.__str__() == 'kr0,14'


def test_norwegian_krone_negative():
    """test_norwegian_krone_negative."""
    amount = -100
    norwegian_krone = NorwegianKrone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert norwegian_krone.code == '578'
    assert norwegian_krone.currency == 'NOK'
    assert norwegian_krone.decimal_places == 2
    assert norwegian_krone.decimal_sign == ','
    assert norwegian_krone.grouping_sign == '.'
    assert not norwegian_krone.international
    assert norwegian_krone.symbol == 'kr'
    assert norwegian_krone.__hash__() == hash((decimal, 'NOK', '578'))
    assert norwegian_krone.__repr__() == (
        'NorwegianKrone(amount: -100, '
        'currency: "NOK", '
        'symbol: "kr", '
        'code: "578", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert norwegian_krone.__str__() == 'kr-100,00'


def test_norwegian_krone_custom():
    """test_norwegian_krone_custom."""
    amount = 1000
    norwegian_krone = NorwegianKrone(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert norwegian_krone.amount == decimal
    assert norwegian_krone.code == '578'
    assert norwegian_krone.currency == 'NOK'
    assert norwegian_krone.decimal_places == 5
    assert norwegian_krone.decimal_sign == '.'
    assert norwegian_krone.grouping_sign == ','
    assert norwegian_krone.international
    assert norwegian_krone.symbol == 'kr'
    assert norwegian_krone.__hash__() == hash((decimal, 'NOK', '578'))
    assert norwegian_krone.__repr__() == (
        'NorwegianKrone(amount: 1000, '
        'currency: "NOK", '
        'symbol: "kr", '
        'code: "578", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert norwegian_krone.__str__() == 'NOK 1,000.00000'


def test_norwegian_krone_changed():
    """test_cnorwegian_krone_changed."""
    norwegian_krone = NorwegianKrone(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        norwegian_krone.international = True


def test_norwegian_krone_math_add():
    """test_norwegian_krone_math_add."""
    norwegian_krone_one = NorwegianKrone(amount=1)
    norwegian_krone_two = NorwegianKrone(amount=2)
    norwegian_krone_three = NorwegianKrone(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency NOK and OTHER.'):
        _ = norwegian_krone_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'norwegian_krone.NorwegianKrone\'> '
                   'and <class \'str\'>.')):
        _ = norwegian_krone_one.__add__('1.00')
    assert (norwegian_krone_one + norwegian_krone_two) == norwegian_krone_three


def test_currency_slots():
    """test_currency_slots."""
    euro = NorwegianKrone(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NorwegianKrone\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
