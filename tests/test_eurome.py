# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroME representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroME
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurome():
    """test_eurome."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurome = EuroME(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurome.amount == decimal
    assert eurome.numeric_code == '978'
    assert eurome.alpha_code == 'EUR'
    assert eurome.decimal_places == 2
    assert eurome.decimal_sign == ','
    assert eurome.grouping_sign == '.'
    assert not eurome.international
    assert eurome.symbol == '€'
    assert not eurome.symbol_ahead
    assert eurome.symbol_separator == '\u00A0'
    assert eurome.convertion == ''
    assert eurome.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurome.__repr__() == (
        'EuroME(amount: 0.1428571428571428571428571429, '
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
    assert eurome.__str__() == '0,14 €'


def test_eurome_negative():
    """test_eurome_negative."""
    amount = -100
    eurome = EuroME(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurome.numeric_code == '978'
    assert eurome.alpha_code == 'EUR'
    assert eurome.decimal_places == 2
    assert eurome.decimal_sign == ','
    assert eurome.grouping_sign == '.'
    assert not eurome.international
    assert eurome.symbol == '€'
    assert not eurome.symbol_ahead
    assert eurome.symbol_separator == '\u00A0'
    assert eurome.convertion == ''
    assert eurome.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurome.__repr__() == (
        'EuroME(amount: -100, '
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
    assert eurome.__str__() == '-100,00 €'


def test_eurome_custom():
    """test_eurome_custom."""
    amount = 1000
    eurome = EuroME(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurome.amount == decimal
    assert eurome.numeric_code == '978'
    assert eurome.alpha_code == 'EUR'
    assert eurome.decimal_places == 5
    assert eurome.decimal_sign == '.'
    assert eurome.grouping_sign == ','
    assert eurome.international
    assert eurome.symbol == '€'
    assert not eurome.symbol_ahead
    assert eurome.symbol_separator == '_'
    assert eurome.convertion == ''
    assert eurome.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurome.__repr__() == (
        'EuroME(amount: 1000, '
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
    assert eurome.__str__() == 'EUR 1,000.00000'


def test_eurome_changed():
    """test_ceurome_changed."""
    eurome = EuroME(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurome.international = True


def test_eurome_math_add():
    """test_eurome_math_add."""
    eurome_one = EuroME(amount=1)
    eurome_two = EuroME(amount=2)
    eurome_three = EuroME(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurome_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroME\'> '
                   'and <class \'str\'>.')):
        _ = eurome_one.__add__('1.00')
    assert (
        eurome_one +
        eurome_two) == eurome_three


def test_eurome_slots():
    """test_eurome_slots."""
    eurome = EuroME(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroME\' '
                'object has no attribute \'new_variable\'')):
        eurome.new_variable = 'fail'  # pylint: disable=assigning-non-slot
