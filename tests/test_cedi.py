# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Cedi representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Cedi
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cedi():
    """test_cedi."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cedi = Cedi(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cedi.amount == decimal
    assert cedi.numeric_code == '936'
    assert cedi.alpha_code == 'GHS'
    assert cedi.decimal_places == 2
    assert cedi.decimal_sign == '.'
    assert cedi.grouping_sign == ','
    assert not cedi.international
    assert cedi.symbol == '₵'
    assert cedi.symbol_ahead
    assert cedi.symbol_separator == ''
    assert cedi.__hash__() == hash((decimal, 'GHS', '936'))
    assert cedi.__repr__() == (
        'Cedi(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GHS", '
        'symbol: "₵", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "936", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert cedi.__str__() == '₵0.14'


def test_cedi_negative():
    """test_cedi_negative."""
    amount = -100
    cedi = Cedi(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cedi.numeric_code == '936'
    assert cedi.alpha_code == 'GHS'
    assert cedi.decimal_places == 2
    assert cedi.decimal_sign == '.'
    assert cedi.grouping_sign == ','
    assert not cedi.international
    assert cedi.symbol == '₵'
    assert cedi.symbol_ahead
    assert cedi.symbol_separator == ''
    assert cedi.__hash__() == hash((decimal, 'GHS', '936'))
    assert cedi.__repr__() == (
        'Cedi(amount: -100, '
        'alpha_code: "GHS", '
        'symbol: "₵", '
        'symbol_ahead: True, '
        'symbol_separator: "", '
        'numeric_code: "936", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert cedi.__str__() == '₵-100.00'


def test_cedi_custom():
    """test_cedi_custom."""
    amount = 1000
    cedi = Cedi(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert cedi.amount == decimal
    assert cedi.numeric_code == '936'
    assert cedi.alpha_code == 'GHS'
    assert cedi.decimal_places == 5
    assert cedi.decimal_sign == ','
    assert cedi.grouping_sign == '.'
    assert cedi.international
    assert cedi.symbol == '₵'
    assert not cedi.symbol_ahead
    assert cedi.symbol_separator == '_'
    assert cedi.__hash__() == hash((decimal, 'GHS', '936'))
    assert cedi.__repr__() == (
        'Cedi(amount: 1000, '
        'alpha_code: "GHS", '
        'symbol: "₵", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "936", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert cedi.__str__() == 'GHS 1,000.00000'


def test_cedi_changed():
    """test_ccedi_changed."""
    cedi = Cedi(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cedi.international = True


def test_cedi_math_add():
    """test_cedi_math_add."""
    cedi_one = Cedi(amount=1)
    cedi_two = Cedi(amount=2)
    cedi_three = Cedi(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GHS and OTHER.'):
        _ = cedi_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'cedi.Cedi\'> '
                   'and <class \'str\'>.')):
        _ = cedi_one.__add__('1.00')
    assert (
        cedi_one +
        cedi_two) == cedi_three


def test_cedi_slots():
    """test_cedi_slots."""
    cedi = Cedi(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Cedi\' '
                'object has no attribute \'new_variable\'')):
        cedi.new_variable = 'fail'  # pylint: disable=assigning-non-slot
