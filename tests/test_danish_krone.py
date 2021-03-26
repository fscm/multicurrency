# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Danish Krone representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, DanishKrone
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_danish_krone():
    """test_danish_krone."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    danish_krone = DanishKrone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert danish_krone.amount == decimal
    assert danish_krone.code == '208'
    assert danish_krone.currency == 'DKK'
    assert danish_krone.decimal_places == 2
    assert danish_krone.decimal_sign == ','
    assert danish_krone.grouping_sign == '.'
    assert not danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: 0.1428571428571428571428571429, '
        'currency: "DKK", '
        'symbol: "kr", '
        'code: "208", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert danish_krone.__str__() == 'kr0,14'


def test_danish_krone_negative():
    """test_danish_krone_negative."""
    amount = -100
    danish_krone = DanishKrone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert danish_krone.code == '208'
    assert danish_krone.currency == 'DKK'
    assert danish_krone.decimal_places == 2
    assert danish_krone.decimal_sign == ','
    assert danish_krone.grouping_sign == '.'
    assert not danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: -100, '
        'currency: "DKK", '
        'symbol: "kr", '
        'code: "208", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert danish_krone.__str__() == 'kr-100,00'


def test_danish_krone_custom():
    """test_danish_krone_custom."""
    amount = 1000
    danish_krone = DanishKrone(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert danish_krone.amount == decimal
    assert danish_krone.code == '208'
    assert danish_krone.currency == 'DKK'
    assert danish_krone.decimal_places == 5
    assert danish_krone.decimal_sign == '.'
    assert danish_krone.grouping_sign == ','
    assert danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: 1000, '
        'currency: "DKK", '
        'symbol: "kr", '
        'code: "208", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert danish_krone.__str__() == 'DKK 1,000.00000'


def test_danish_krone_changed():
    """test_cdanish_krone_changed."""
    danish_krone = DanishKrone(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.international = True


def test_danish_krone_math_add():
    """test_danish_krone_math_add."""
    danish_krone_one = DanishKrone(amount=1)
    danish_krone_two = DanishKrone(amount=2)
    danish_krone_three = DanishKrone(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DKK and OTHER.'):
        _ = danish_krone_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'danish_krone.DanishKrone\'> '
                   'and <class \'str\'>.')):
        _ = danish_krone_one.__add__('1.00')
    assert (danish_krone_one + danish_krone_two) == danish_krone_three


def test_currency_slots():
    """test_currency_slots."""
    euro = DanishKrone(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'DanishKrone\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
