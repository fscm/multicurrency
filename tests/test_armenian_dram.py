# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Armenian Dram representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, ArmenianDram
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_armenian_dram():
    """test_armenian_dram."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    armenian_dram = ArmenianDram(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert armenian_dram.amount == decimal
    assert armenian_dram.numeric_code == '051'
    assert armenian_dram.alpha_code == 'AMD'
    assert armenian_dram.decimal_places == 2
    assert armenian_dram.decimal_sign == '.'
    assert armenian_dram.grouping_sign == ','
    assert not armenian_dram.international
    assert armenian_dram.symbol == 'Դ'
    assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
    assert armenian_dram.__repr__() == (
        'ArmenianDram(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AMD", '
        'symbol: "Դ", '
        'numeric_code: "051", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert armenian_dram.__str__() == 'Դ0.14'


def test_armenian_dram_negative():
    """test_armenian_dram_negative."""
    amount = -100
    armenian_dram = ArmenianDram(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert armenian_dram.numeric_code == '051'
    assert armenian_dram.alpha_code == 'AMD'
    assert armenian_dram.decimal_places == 2
    assert armenian_dram.decimal_sign == '.'
    assert armenian_dram.grouping_sign == ','
    assert not armenian_dram.international
    assert armenian_dram.symbol == 'Դ'
    assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
    assert armenian_dram.__repr__() == (
        'ArmenianDram(amount: -100, '
        'alpha_code: "AMD", '
        'symbol: "Դ", '
        'numeric_code: "051", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert armenian_dram.__str__() == 'Դ-100.00'


def test_armenian_dram_custom():
    """test_armenian_dram_custom."""
    amount = 1000
    armenian_dram = ArmenianDram(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert armenian_dram.amount == decimal
    assert armenian_dram.numeric_code == '051'
    assert armenian_dram.alpha_code == 'AMD'
    assert armenian_dram.decimal_places == 5
    assert armenian_dram.decimal_sign == ','
    assert armenian_dram.grouping_sign == '.'
    assert armenian_dram.international
    assert armenian_dram.symbol == 'Դ'
    assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
    assert armenian_dram.__repr__() == (
        'ArmenianDram(amount: 1000, '
        'alpha_code: "AMD", '
        'symbol: "Դ", '
        'numeric_code: "051", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert armenian_dram.__str__() == 'AMD 1.000,00000'


def test_armenian_dram_changed():
    """test_carmenian_dram_changed."""
    armenian_dram = ArmenianDram(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        armenian_dram.international = True


def test_armenian_dram_math_add():
    """test_armenian_dram_math_add."""
    armenian_dram_one = ArmenianDram(amount=1)
    armenian_dram_two = ArmenianDram(amount=2)
    armenian_dram_three = ArmenianDram(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AMD and OTHER.'):
        _ = armenian_dram_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dram.ArmenianDram\'> '
                   'and <class \'str\'>.')):
        _ = armenian_dram_one.__add__('1.00')
    assert (armenian_dram_one + armenian_dram_two) == armenian_dram_three


def test_currency_slots():
    """test_currency_slots."""
    euro = ArmenianDram(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'ArmenianDram\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
