# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ethereum representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Ethereum
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ethereum():
    """test_ethereum."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ethereum = Ethereum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ethereum.amount == decimal
    assert ethereum.numeric_code == '0'
    assert ethereum.alpha_code == 'ETH'
    assert ethereum.decimal_places == 18
    assert ethereum.decimal_sign == '.'
    assert ethereum.grouping_places == 3
    assert ethereum.grouping_sign == ','
    assert not ethereum.international
    assert ethereum.symbol == 'Ξ'
    assert ethereum.symbol_ahead
    assert ethereum.symbol_separator == ''
    assert ethereum.convertion == ''
    assert ethereum.__hash__() == hash((decimal, 'ETH', '0'))
    assert ethereum.__repr__() == (
        'Ethereum(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ETH", '
        'symbol: "Ξ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "18", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert ethereum.__str__() == 'Ξ0.142857142857142857'


def test_ethereum_negative():
    """test_ethereum_negative."""
    amount = -100
    ethereum = Ethereum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ethereum.numeric_code == '0'
    assert ethereum.alpha_code == 'ETH'
    assert ethereum.decimal_places == 18
    assert ethereum.decimal_sign == '.'
    assert ethereum.grouping_places == 3
    assert ethereum.grouping_sign == ','
    assert not ethereum.international
    assert ethereum.symbol == 'Ξ'
    assert ethereum.symbol_ahead
    assert ethereum.symbol_separator == ''
    assert ethereum.convertion == ''
    assert ethereum.__hash__() == hash((decimal, 'ETH', '0'))
    assert ethereum.__repr__() == (
        'Ethereum(amount: -100, '
        'alpha_code: "ETH", '
        'symbol: "Ξ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "18", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert ethereum.__str__() == 'Ξ-100.000000000000000000'


def test_ethereum_custom():
    """test_ethereum_custom."""
    amount = 1000
    ethereum = Ethereum(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert ethereum.amount == decimal
    assert ethereum.numeric_code == '0'
    assert ethereum.alpha_code == 'ETH'
    assert ethereum.decimal_places == 5
    assert ethereum.decimal_sign == ','
    assert ethereum.grouping_places == 2
    assert ethereum.grouping_sign == '.'
    assert ethereum.international
    assert ethereum.symbol == 'Ξ'
    assert not ethereum.symbol_ahead
    assert ethereum.symbol_separator == '_'
    assert ethereum.convertion == ''
    assert ethereum.__hash__() == hash((decimal, 'ETH', '0'))
    assert ethereum.__repr__() == (
        'Ethereum(amount: 1000, '
        'alpha_code: "ETH", '
        'symbol: "Ξ", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert ethereum.__str__() == 'ETH 10,00.00000'


def test_ethereum_changed():
    """test_cethereum_changed."""
    ethereum = Ethereum(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ethereum.international = True


def test_ethereum_math_add():
    """test_ethereum_math_add."""
    ethereum_one = Ethereum(amount=1)
    ethereum_two = Ethereum(amount=2)
    ethereum_three = Ethereum(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ETH and OTHER.'):
        _ = ethereum_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Ethereum\'> '
                   'and <class \'str\'>.')):
        _ = ethereum_one.__add__('1.00')
    assert (
        ethereum_one +
        ethereum_two) == ethereum_three


def test_ethereum_slots():
    """test_ethereum_slots."""
    ethereum = Ethereum(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Ethereum\' '
                'object has no attribute \'new_variable\'')):
        ethereum.new_variable = 'fail'  # pylint: disable=assigning-non-slot
