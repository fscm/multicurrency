# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bitcoin representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Bitcoin
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bitcoin():
    """test_bitcoin."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bitcoin = Bitcoin(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bitcoin.amount == decimal
    assert bitcoin.numeric_code == '0'
    assert bitcoin.alpha_code == 'XBT'
    assert bitcoin.decimal_places == 8
    assert bitcoin.decimal_sign == '.'
    assert bitcoin.grouping_places == 3
    assert bitcoin.grouping_sign == ','
    assert not bitcoin.international
    assert bitcoin.symbol == '₿'
    assert bitcoin.symbol_ahead
    assert bitcoin.symbol_separator == ''
    assert bitcoin.convertion == ''
    assert bitcoin.__hash__() == hash((decimal, 'XBT', '0'))
    assert bitcoin.__repr__() == (
        'Bitcoin(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XBT", '
        'symbol: "₿", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "8", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert bitcoin.__str__() == '₿0.14285714'


def test_bitcoin_negative():
    """test_bitcoin_negative."""
    amount = -100
    bitcoin = Bitcoin(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bitcoin.numeric_code == '0'
    assert bitcoin.alpha_code == 'XBT'
    assert bitcoin.decimal_places == 8
    assert bitcoin.decimal_sign == '.'
    assert bitcoin.grouping_places == 3
    assert bitcoin.grouping_sign == ','
    assert not bitcoin.international
    assert bitcoin.symbol == '₿'
    assert bitcoin.symbol_ahead
    assert bitcoin.symbol_separator == ''
    assert bitcoin.convertion == ''
    assert bitcoin.__hash__() == hash((decimal, 'XBT', '0'))
    assert bitcoin.__repr__() == (
        'Bitcoin(amount: -100, '
        'alpha_code: "XBT", '
        'symbol: "₿", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "8", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert bitcoin.__str__() == '₿-100.00000000'


def test_bitcoin_custom():
    """test_bitcoin_custom."""
    amount = 1000
    bitcoin = Bitcoin(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert bitcoin.amount == decimal
    assert bitcoin.numeric_code == '0'
    assert bitcoin.alpha_code == 'XBT'
    assert bitcoin.decimal_places == 5
    assert bitcoin.decimal_sign == ','
    assert bitcoin.grouping_places == 2
    assert bitcoin.grouping_sign == '.'
    assert bitcoin.international
    assert bitcoin.symbol == '₿'
    assert not bitcoin.symbol_ahead
    assert bitcoin.symbol_separator == '_'
    assert bitcoin.convertion == ''
    assert bitcoin.__hash__() == hash((decimal, 'XBT', '0'))
    assert bitcoin.__repr__() == (
        'Bitcoin(amount: 1000, '
        'alpha_code: "XBT", '
        'symbol: "₿", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert bitcoin.__str__() == 'XBT 10,00.00000'


def test_bitcoin_changed():
    """test_cbitcoin_changed."""
    bitcoin = Bitcoin(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bitcoin.international = True


def test_bitcoin_math_add():
    """test_bitcoin_math_add."""
    bitcoin_one = Bitcoin(amount=1)
    bitcoin_two = Bitcoin(amount=2)
    bitcoin_three = Bitcoin(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XBT and OTHER.'):
        _ = bitcoin_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Bitcoin\'> '
                   'and <class \'str\'>.')):
        _ = bitcoin_one.__add__('1.00')
    assert (
        bitcoin_one +
        bitcoin_two) == bitcoin_three


def test_bitcoin_slots():
    """test_bitcoin_slots."""
    bitcoin = Bitcoin(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Bitcoin\' '
                'object has no attribute \'new_variable\'')):
        bitcoin.new_variable = 'fail'  # pylint: disable=assigning-non-slot
