# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EOS representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EOS
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eos():
    """test_eos."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eos = EOS(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eos.amount == decimal
    assert eos.numeric_code == '0'
    assert eos.alpha_code == 'EOS'
    assert eos.decimal_places == 4
    assert eos.decimal_sign == '.'
    assert eos.grouping_sign == ','
    assert not eos.international
    assert eos.symbol == 'ε'
    assert eos.symbol_ahead
    assert eos.symbol_separator == ''
    assert eos.convertion == ''
    assert eos.__hash__() == hash((decimal, 'EOS', '0'))
    assert eos.__repr__() == (
        'EOS(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EOS", '
        'symbol: "ε", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "4", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert eos.__str__() == 'ε0.1429'


def test_eos_negative():
    """test_eos_negative."""
    amount = -100
    eos = EOS(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eos.numeric_code == '0'
    assert eos.alpha_code == 'EOS'
    assert eos.decimal_places == 4
    assert eos.decimal_sign == '.'
    assert eos.grouping_sign == ','
    assert not eos.international
    assert eos.symbol == 'ε'
    assert eos.symbol_ahead
    assert eos.symbol_separator == ''
    assert eos.convertion == ''
    assert eos.__hash__() == hash((decimal, 'EOS', '0'))
    assert eos.__repr__() == (
        'EOS(amount: -100, '
        'alpha_code: "EOS", '
        'symbol: "ε", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "0", '
        'decimal_places: "4", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert eos.__str__() == 'ε-100.0000'


def test_eos_custom():
    """test_eos_custom."""
    amount = 1000
    eos = EOS(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eos.amount == decimal
    assert eos.numeric_code == '0'
    assert eos.alpha_code == 'EOS'
    assert eos.decimal_places == 5
    assert eos.decimal_sign == ','
    assert eos.grouping_sign == '.'
    assert eos.international
    assert eos.symbol == 'ε'
    assert not eos.symbol_ahead
    assert eos.symbol_separator == '_'
    assert eos.convertion == ''
    assert eos.__hash__() == hash((decimal, 'EOS', '0'))
    assert eos.__repr__() == (
        'EOS(amount: 1000, '
        'alpha_code: "EOS", '
        'symbol: "ε", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "0", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert eos.__str__() == 'EOS 1,000.00000'


def test_eos_changed():
    """test_ceos_changed."""
    eos = EOS(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eos.international = True


def test_eos_math_add():
    """test_eos_math_add."""
    eos_one = EOS(amount=1)
    eos_two = EOS(amount=2)
    eos_three = EOS(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EOS and OTHER.'):
        _ = eos_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'crypto.EOS\'> '
                   'and <class \'str\'>.')):
        _ = eos_one.__add__('1.00')
    assert (
        eos_one +
        eos_two) == eos_three


def test_eos_slots():
    """test_eos_slots."""
    eos = EOS(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EOS\' '
                'object has no attribute \'new_variable\'')):
        eos.new_variable = 'fail'  # pylint: disable=assigning-non-slot
