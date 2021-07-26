# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroIT representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroIT
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_euroit():
    """test_euroit."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    euroit = EuroIT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroit.amount == decimal
    assert euroit.numeric_code == '978'
    assert euroit.alpha_code == 'EUR'
    assert euroit.decimal_places == 2
    assert euroit.decimal_sign == ','
    assert euroit.grouping_places == 3
    assert euroit.grouping_sign == '.'
    assert not euroit.international
    assert euroit.symbol == '€'
    assert not euroit.symbol_ahead
    assert euroit.symbol_separator == '\u00A0'
    assert euroit.convertion == ''
    assert euroit.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroit.__repr__() == (
        'EuroIT(amount: 0.1428571428571428571428571429, '
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
    assert euroit.__str__() == '0,14 €'


def test_euroit_negative():
    """test_euroit_negative."""
    amount = -100
    euroit = EuroIT(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert euroit.numeric_code == '978'
    assert euroit.alpha_code == 'EUR'
    assert euroit.decimal_places == 2
    assert euroit.decimal_sign == ','
    assert euroit.grouping_places == 3
    assert euroit.grouping_sign == '.'
    assert not euroit.international
    assert euroit.symbol == '€'
    assert not euroit.symbol_ahead
    assert euroit.symbol_separator == '\u00A0'
    assert euroit.convertion == ''
    assert euroit.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroit.__repr__() == (
        'EuroIT(amount: -100, '
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
    assert euroit.__str__() == '-100,00 €'


def test_euroit_custom():
    """test_euroit_custom."""
    amount = 1000
    euroit = EuroIT(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert euroit.amount == decimal
    assert euroit.numeric_code == '978'
    assert euroit.alpha_code == 'EUR'
    assert euroit.decimal_places == 5
    assert euroit.decimal_sign == '.'
    assert euroit.grouping_places == 2
    assert euroit.grouping_sign == ','
    assert euroit.international
    assert euroit.symbol == '€'
    assert not euroit.symbol_ahead
    assert euroit.symbol_separator == '_'
    assert euroit.convertion == ''
    assert euroit.__hash__() == hash((decimal, 'EUR', '978'))
    assert euroit.__repr__() == (
        'EuroIT(amount: 1000, '
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
    assert euroit.__str__() == 'EUR 10,00.00000'


def test_euroit_changed():
    """test_ceuroit_changed."""
    euroit = EuroIT(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euroit.international = True


def test_euroit_math_add():
    """test_euroit_math_add."""
    euroit_one = EuroIT(amount=1)
    euroit_two = EuroIT(amount=2)
    euroit_three = EuroIT(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = euroit_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroIT\'> '
                   'and <class \'str\'>.')):
        _ = euroit_one.__add__('1.00')
    assert (
        euroit_one +
        euroit_two) == euroit_three


def test_euroit_slots():
    """test_euroit_slots."""
    euroit = EuroIT(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroIT\' '
                'object has no attribute \'new_variable\'')):
        euroit.new_variable = 'fail'  # pylint: disable=assigning-non-slot
