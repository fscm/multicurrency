# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroAD representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroAD
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroad():
    """test_euroad."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroad = EuroAD(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroad.amount == decimal
    assert euroad.numeric_code == '978'
    assert euroad.alpha_code == 'EUR'
    assert euroad.decimal_places == 2
    assert euroad.decimal_sign == ','
    assert euroad.grouping_places == 3
    assert euroad.grouping_sign == '.'
    assert not euroad.international
    assert euroad.symbol == '€'
    assert not euroad.symbol_ahead
    assert euroad.symbol_separator == '\u00A0'
    assert euroad.convertion == ''
    assert euroad.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroad.__repr__() == (
        'EuroAD(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert euroad.__str__() == '0,14 €'


def test_euroad_negative():
    """test_euroad_negative."""
    amount = -100
    euroad = EuroAD(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroad.numeric_code == '978'
    assert euroad.alpha_code == 'EUR'
    assert euroad.decimal_places == 2
    assert euroad.decimal_sign == ','
    assert euroad.grouping_places == 3
    assert euroad.grouping_sign == '.'
    assert not euroad.international
    assert euroad.symbol == '€'
    assert not euroad.symbol_ahead
    assert euroad.symbol_separator == '\u00A0'
    assert euroad.convertion == ''
    assert euroad.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroad.__repr__() == (
        'EuroAD(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert euroad.__str__() == '-100,00 €'


def test_euroad_custom():
    """test_euroad_custom."""
    amount = 1000
    euroad = EuroAD(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroad.amount == decimal
    assert euroad.numeric_code == '978'
    assert euroad.alpha_code == 'EUR'
    assert euroad.decimal_places == 5
    assert euroad.decimal_sign == '.'
    assert euroad.grouping_places == 2
    assert euroad.grouping_sign == ','
    assert euroad.international
    assert euroad.symbol == '€'
    assert not euroad.symbol_ahead
    assert euroad.symbol_separator == '_'
    assert euroad.convertion == ''
    assert euroad.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroad.__repr__() == (
        'EuroAD(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert euroad.__str__() == 'EUR 10,00.00000'


def test_euroad_changed():
    """test_ceuroad_changed."""
    euroad = EuroAD(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroad.international = True


def test_euroad_math_add():
    """test_euroad_math_add."""
    euroad_one = EuroAD(amount=1)
    euroad_two = EuroAD(amount=2)
    euroad_three = EuroAD(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroad_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroAD\'> '
                   'and <class \'str\'>.')):
        _ = euroad_one.__add__('1.00')
    assert (
        euroad_one +
        euroad_two) == euroad_three


def test_euroad_slots():
    """test_euroad_slots."""
    euroad = EuroAD(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroAD\' '
                'object has no attribute \'new_variable\'')):
        euroad.new_variable = 'fail'  # pylint: disable=assigning-non-slot
