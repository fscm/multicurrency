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
    assert danish_krone.numeric_code == '208'
    assert danish_krone.alpha_code == 'DKK'
    assert danish_krone.decimal_places == 2
    assert danish_krone.decimal_sign == ','
    assert danish_krone.grouping_places == 3
    assert danish_krone.grouping_sign == '.'
    assert not danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert not danish_krone.symbol_ahead
    assert danish_krone.symbol_separator == '\u00A0'
    assert danish_krone.convertion == ''
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: 0.1428571428571428571428571429, '
        'alpha_code: "DKK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "208", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert danish_krone.__str__() == '0,14 kr'


def test_danish_krone_negative():
    """test_danish_krone_negative."""
    amount = -100
    danish_krone = DanishKrone(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert danish_krone.numeric_code == '208'
    assert danish_krone.alpha_code == 'DKK'
    assert danish_krone.decimal_places == 2
    assert danish_krone.decimal_sign == ','
    assert danish_krone.grouping_places == 3
    assert danish_krone.grouping_sign == '.'
    assert not danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert not danish_krone.symbol_ahead
    assert danish_krone.symbol_separator == '\u00A0'
    assert danish_krone.convertion == ''
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: -100, '
        'alpha_code: "DKK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "208", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert danish_krone.__str__() == '-100,00 kr'


def test_danish_krone_custom():
    """test_danish_krone_custom."""
    amount = 1000
    danish_krone = DanishKrone(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert danish_krone.amount == decimal
    assert danish_krone.numeric_code == '208'
    assert danish_krone.alpha_code == 'DKK'
    assert danish_krone.decimal_places == 5
    assert danish_krone.decimal_sign == '.'
    assert danish_krone.grouping_places == 2
    assert danish_krone.grouping_sign == ','
    assert danish_krone.international
    assert danish_krone.symbol == 'kr'
    assert not danish_krone.symbol_ahead
    assert danish_krone.symbol_separator == '_'
    assert danish_krone.convertion == ''
    assert danish_krone.__hash__() == hash((decimal, 'DKK', '208'))
    assert danish_krone.__repr__() == (
        'DanishKrone(amount: 1000, '
        'alpha_code: "DKK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "208", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert danish_krone.__str__() == 'DKK 10,00.00000'


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
        danish_krone.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        danish_krone.numeric_code = '978'
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
        danish_krone.grouping_places = 4
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
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency DKK and OTHER.'):
        _ = danish_krone_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'krone.DanishKrone\'> '
                   'and <class \'str\'>.')):
        _ = danish_krone_one.__add__('1.00')
    assert (
        danish_krone_one +
        danish_krone_two) == danish_krone_three


def test_danish_krone_slots():
    """test_danish_krone_slots."""
    danish_krone = DanishKrone(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'DanishKrone\' '
                'object has no attribute \'new_variable\'')):
        danish_krone.new_variable = 'fail'  # pylint: disable=assigning-non-slot
