# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroGR representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroGR
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurogr():
    """test_eurogr."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurogr = EuroGR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurogr.amount == decimal
    assert eurogr.numeric_code == '978'
    assert eurogr.alpha_code == 'EUR'
    assert eurogr.decimal_places == 2
    assert eurogr.decimal_sign == ','
    assert eurogr.grouping_sign == '.'
    assert not eurogr.international
    assert eurogr.symbol == '€'
    assert not eurogr.symbol_ahead
    assert eurogr.symbol_separator == '\u00A0'
    assert eurogr.convertion == ''
    assert eurogr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurogr.__repr__() == (
        'EuroGR(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurogr.__str__() == '0,14 €'


def test_eurogr_negative():
    """test_eurogr_negative."""
    amount = -100
    eurogr = EuroGR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurogr.numeric_code == '978'
    assert eurogr.alpha_code == 'EUR'
    assert eurogr.decimal_places == 2
    assert eurogr.decimal_sign == ','
    assert eurogr.grouping_sign == '.'
    assert not eurogr.international
    assert eurogr.symbol == '€'
    assert not eurogr.symbol_ahead
    assert eurogr.symbol_separator == '\u00A0'
    assert eurogr.convertion == ''
    assert eurogr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurogr.__repr__() == (
        'EuroGR(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert eurogr.__str__() == '-100,00 €'


def test_eurogr_custom():
    """test_eurogr_custom."""
    amount = 1000
    eurogr = EuroGR(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurogr.amount == decimal
    assert eurogr.numeric_code == '978'
    assert eurogr.alpha_code == 'EUR'
    assert eurogr.decimal_places == 5
    assert eurogr.decimal_sign == '.'
    assert eurogr.grouping_sign == ','
    assert eurogr.international
    assert eurogr.symbol == '€'
    assert not eurogr.symbol_ahead
    assert eurogr.symbol_separator == '_'
    assert eurogr.convertion == ''
    assert eurogr.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurogr.__repr__() == (
        'EuroGR(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert eurogr.__str__() == 'EUR 1,000.00000'


def test_eurogr_changed():
    """test_ceurogr_changed."""
    eurogr = EuroGR(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurogr.international = True


def test_eurogr_math_add():
    """test_eurogr_math_add."""
    eurogr_one = EuroGR(amount=1)
    eurogr_two = EuroGR(amount=2)
    eurogr_three = EuroGR(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurogr_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroGR\'> '
                   'and <class \'str\'>.')):
        _ = eurogr_one.__add__('1.00')
    assert (
        eurogr_one +
        eurogr_two) == eurogr_three


def test_eurogr_slots():
    """test_eurogr_slots."""
    eurogr = EuroGR(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroGR\' '
                'object has no attribute \'new_variable\'')):
        eurogr.new_variable = 'fail'  # pylint: disable=assigning-non-slot
