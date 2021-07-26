# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Monero representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Monero
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_monero():
    """test_monero."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    monero = Monero(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert monero.amount == decimal
    assert monero.numeric_code == '0'
    assert monero.alpha_code == 'XMR'
    assert monero.decimal_places == 12
    assert monero.decimal_sign == '.'
    assert monero.grouping_places == 3
    assert monero.grouping_sign == ','
    assert not monero.international
    assert monero.symbol == 'ɱ'
    assert monero.symbol_ahead
    assert monero.symbol_separator == ''
    assert monero.convertion == ''
    assert monero.__hash__() == hash((decimal, 'XMR', '0'))
    assert monero.__repr__() == (
        'Monero(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XMR", '
        'symbol: "ɱ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "12", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert monero.__str__() == 'ɱ0.142857142857'


def test_monero_negative():
    """test_monero_negative."""
    amount = -100
    monero = Monero(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert monero.numeric_code == '0'
    assert monero.alpha_code == 'XMR'
    assert monero.decimal_places == 12
    assert monero.decimal_sign == '.'
    assert monero.grouping_places == 3
    assert monero.grouping_sign == ','
    assert not monero.international
    assert monero.symbol == 'ɱ'
    assert monero.symbol_ahead
    assert monero.symbol_separator == ''
    assert monero.convertion == ''
    assert monero.__hash__() == hash((decimal, 'XMR', '0'))
    assert monero.__repr__() == (
        'Monero(amount: -100, '
        'alpha_code: "XMR", '
        'symbol: "ɱ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "12", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert monero.__str__() == 'ɱ-100.000000000000'


def test_monero_custom():
    """test_monero_custom."""
    amount = 1000
    monero = Monero(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert monero.amount == decimal
    assert monero.numeric_code == '0'
    assert monero.alpha_code == 'XMR'
    assert monero.decimal_places == 5
    assert monero.decimal_sign == ','
    assert monero.grouping_places == 2
    assert monero.grouping_sign == '.'
    assert monero.international
    assert monero.symbol == 'ɱ'
    assert not monero.symbol_ahead
    assert monero.symbol_separator == '_'
    assert monero.convertion == ''
    assert monero.__hash__() == hash((decimal, 'XMR', '0'))
    assert monero.__repr__() == (
        'Monero(amount: 1000, '
        'alpha_code: "XMR", '
        'symbol: "ɱ", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert monero.__str__() == 'XMR 10,00.00000'


def test_monero_changed():
    """test_cmonero_changed."""
    monero = Monero(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        monero.international = True


def test_monero_math_add():
    """test_monero_math_add."""
    monero_one = Monero(amount=1)
    monero_two = Monero(amount=2)
    monero_three = Monero(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XMR and OTHER.'):
        _ = monero_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Monero\'> '
                   'and <class \'str\'>.')):
        _ = monero_one.__add__('1.00')
    assert (
        monero_one +
        monero_two) == monero_three


def test_monero_slots():
    """test_monero_slots."""
    monero = Monero(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Monero\' '
                'object has no attribute \'new_variable\'')):
        monero.new_variable = 'fail'  # pylint: disable=assigning-non-slot
