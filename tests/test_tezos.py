# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tezos representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Tezos
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tezos():
    """test_tezos."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tezos = Tezos(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tezos.amount == decimal
    assert tezos.numeric_code == '0'
    assert tezos.alpha_code == 'XTZ'
    assert tezos.decimal_places == 6
    assert tezos.decimal_sign == '.'
    assert tezos.grouping_places == 3
    assert tezos.grouping_sign == ','
    assert not tezos.international
    assert tezos.symbol == 'ꜩ'
    assert tezos.symbol_ahead
    assert tezos.symbol_separator == ''
    assert tezos.convertion == ''
    assert tezos.__hash__() == hash((decimal, 'XTZ', '0'))
    assert tezos.__repr__() == (
        'Tezos(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XTZ", '
        'symbol: "ꜩ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "6", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert tezos.__str__() == 'ꜩ0.142857'


def test_tezos_negative():
    """test_tezos_negative."""
    amount = -100
    tezos = Tezos(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tezos.numeric_code == '0'
    assert tezos.alpha_code == 'XTZ'
    assert tezos.decimal_places == 6
    assert tezos.decimal_sign == '.'
    assert tezos.grouping_places == 3
    assert tezos.grouping_sign == ','
    assert not tezos.international
    assert tezos.symbol == 'ꜩ'
    assert tezos.symbol_ahead
    assert tezos.symbol_separator == ''
    assert tezos.convertion == ''
    assert tezos.__hash__() == hash((decimal, 'XTZ', '0'))
    assert tezos.__repr__() == (
        'Tezos(amount: -100, '
        'alpha_code: "XTZ", '
        'symbol: "ꜩ", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "6", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert tezos.__str__() == 'ꜩ-100.000000'


def test_tezos_custom():
    """test_tezos_custom."""
    amount = 1000
    tezos = Tezos(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert tezos.amount == decimal
    assert tezos.numeric_code == '0'
    assert tezos.alpha_code == 'XTZ'
    assert tezos.decimal_places == 5
    assert tezos.decimal_sign == ','
    assert tezos.grouping_places == 2
    assert tezos.grouping_sign == '.'
    assert tezos.international
    assert tezos.symbol == 'ꜩ'
    assert not tezos.symbol_ahead
    assert tezos.symbol_separator == '_'
    assert tezos.convertion == ''
    assert tezos.__hash__() == hash((decimal, 'XTZ', '0'))
    assert tezos.__repr__() == (
        'Tezos(amount: 1000, '
        'alpha_code: "XTZ", '
        'symbol: "ꜩ", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert tezos.__str__() == 'XTZ 10,00.00000'


def test_tezos_changed():
    """test_ctezos_changed."""
    tezos = Tezos(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tezos.international = True


def test_tezos_math_add():
    """test_tezos_math_add."""
    tezos_one = Tezos(amount=1)
    tezos_two = Tezos(amount=2)
    tezos_three = Tezos(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XTZ and OTHER.'):
        _ = tezos_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.Tezos\'> '
                   'and <class \'str\'>.')):
        _ = tezos_one.__add__('1.00')
    assert (
        tezos_one +
        tezos_two) == tezos_three


def test_tezos_slots():
    """test_tezos_slots."""
    tezos = Tezos(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Tezos\' '
                'object has no attribute \'new_variable\'')):
        tezos.new_variable = 'fail'  # pylint: disable=assigning-non-slot
