# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Stellar Lumens representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, StellarLumens
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_stellar_lumens():
    """test_stellar_lumens."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    stellar_lumens = StellarLumens(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert stellar_lumens.amount == decimal
    assert stellar_lumens.numeric_code == '0'
    assert stellar_lumens.alpha_code == 'XLM'
    assert stellar_lumens.decimal_places == 7
    assert stellar_lumens.decimal_sign == '.'
    assert stellar_lumens.grouping_places == 3
    assert stellar_lumens.grouping_sign == ','
    assert not stellar_lumens.international
    assert stellar_lumens.symbol == '*'
    assert stellar_lumens.symbol_ahead
    assert stellar_lumens.symbol_separator == ''
    assert stellar_lumens.convertion == ''
    assert stellar_lumens.__hash__() == hash((decimal, 'XLM', '0'))
    assert stellar_lumens.__repr__() == (
        'StellarLumens(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XLM", '
        'symbol: "*", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "7", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert stellar_lumens.__str__() == '*0.1428571'


def test_stellar_lumens_negative():
    """test_stellar_lumens_negative."""
    amount = -100
    stellar_lumens = StellarLumens(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert stellar_lumens.numeric_code == '0'
    assert stellar_lumens.alpha_code == 'XLM'
    assert stellar_lumens.decimal_places == 7
    assert stellar_lumens.decimal_sign == '.'
    assert stellar_lumens.grouping_places == 3
    assert stellar_lumens.grouping_sign == ','
    assert not stellar_lumens.international
    assert stellar_lumens.symbol == '*'
    assert stellar_lumens.symbol_ahead
    assert stellar_lumens.symbol_separator == ''
    assert stellar_lumens.convertion == ''
    assert stellar_lumens.__hash__() == hash((decimal, 'XLM', '0'))
    assert stellar_lumens.__repr__() == (
        'StellarLumens(amount: -100, '
        'alpha_code: "XLM", '
        'symbol: "*", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "7", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert stellar_lumens.__str__() == '*-100.0000000'


def test_stellar_lumens_custom():
    """test_stellar_lumens_custom."""
    amount = 1000
    stellar_lumens = StellarLumens(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert stellar_lumens.amount == decimal
    assert stellar_lumens.numeric_code == '0'
    assert stellar_lumens.alpha_code == 'XLM'
    assert stellar_lumens.decimal_places == 5
    assert stellar_lumens.decimal_sign == ','
    assert stellar_lumens.grouping_places == 2
    assert stellar_lumens.grouping_sign == '.'
    assert stellar_lumens.international
    assert stellar_lumens.symbol == '*'
    assert not stellar_lumens.symbol_ahead
    assert stellar_lumens.symbol_separator == '_'
    assert stellar_lumens.convertion == ''
    assert stellar_lumens.__hash__() == hash((decimal, 'XLM', '0'))
    assert stellar_lumens.__repr__() == (
        'StellarLumens(amount: 1000, '
        'alpha_code: "XLM", '
        'symbol: "*", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert stellar_lumens.__str__() == 'XLM 10,00.00000'


def test_stellar_lumens_changed():
    """test_cstellar_lumens_changed."""
    stellar_lumens = StellarLumens(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        stellar_lumens.international = True


def test_stellar_lumens_math_add():
    """test_stellar_lumens_math_add."""
    stellar_lumens_one = StellarLumens(amount=1)
    stellar_lumens_two = StellarLumens(amount=2)
    stellar_lumens_three = StellarLumens(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XLM and OTHER.'):
        _ = stellar_lumens_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.StellarLumens\'> '
                   'and <class \'str\'>.')):
        _ = stellar_lumens_one.__add__('1.00')
    assert (
        stellar_lumens_one +
        stellar_lumens_two) == stellar_lumens_three


def test_stellar_lumens_slots():
    """test_stellar_lumens_slots."""
    stellar_lumens = StellarLumens(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'StellarLumens\' '
                'object has no attribute \'new_variable\'')):
        stellar_lumens.new_variable = 'fail'  # pylint: disable=assigning-non-slot
