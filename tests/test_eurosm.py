# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroSM representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroSM
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurosm():
    """test_eurosm."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurosm = EuroSM(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosm.amount == decimal
    assert eurosm.numeric_code == '978'
    assert eurosm.alpha_code == 'EUR'
    assert eurosm.decimal_places == 2
    assert eurosm.decimal_sign == ','
    assert eurosm.grouping_places == 3
    assert eurosm.grouping_sign == '.'
    assert not eurosm.international
    assert eurosm.symbol == '€'
    assert not eurosm.symbol_ahead
    assert eurosm.symbol_separator == '\u00A0'
    assert eurosm.convertion == ''
    assert eurosm.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosm.__repr__() == (
        'EuroSM(amount: 0.1428571428571428571428571429, '
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
    assert eurosm.__str__() == '0,14 €'


def test_eurosm_negative():
    """test_eurosm_negative."""
    amount = -100
    eurosm = EuroSM(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurosm.numeric_code == '978'
    assert eurosm.alpha_code == 'EUR'
    assert eurosm.decimal_places == 2
    assert eurosm.decimal_sign == ','
    assert eurosm.grouping_places == 3
    assert eurosm.grouping_sign == '.'
    assert not eurosm.international
    assert eurosm.symbol == '€'
    assert not eurosm.symbol_ahead
    assert eurosm.symbol_separator == '\u00A0'
    assert eurosm.convertion == ''
    assert eurosm.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosm.__repr__() == (
        'EuroSM(amount: -100, '
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
    assert eurosm.__str__() == '-100,00 €'


def test_eurosm_custom():
    """test_eurosm_custom."""
    amount = 1000
    eurosm = EuroSM(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurosm.amount == decimal
    assert eurosm.numeric_code == '978'
    assert eurosm.alpha_code == 'EUR'
    assert eurosm.decimal_places == 5
    assert eurosm.decimal_sign == '.'
    assert eurosm.grouping_places == 2
    assert eurosm.grouping_sign == ','
    assert eurosm.international
    assert eurosm.symbol == '€'
    assert not eurosm.symbol_ahead
    assert eurosm.symbol_separator == '_'
    assert eurosm.convertion == ''
    assert eurosm.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurosm.__repr__() == (
        'EuroSM(amount: 1000, '
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
    assert eurosm.__str__() == 'EUR 10,00.00000'


def test_eurosm_changed():
    """test_ceurosm_changed."""
    eurosm = EuroSM(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurosm.international = True


def test_eurosm_math_add():
    """test_eurosm_math_add."""
    eurosm_one = EuroSM(amount=1)
    eurosm_two = EuroSM(amount=2)
    eurosm_three = EuroSM(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurosm_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroSM\'> '
                   'and <class \'str\'>.')):
        _ = eurosm_one.__add__('1.00')
    assert (
        eurosm_one +
        eurosm_two) == eurosm_three


def test_eurosm_slots():
    """test_eurosm_slots."""
    eurosm = EuroSM(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroSM\' '
                'object has no attribute \'new_variable\'')):
        eurosm.new_variable = 'fail'  # pylint: disable=assigning-non-slot
