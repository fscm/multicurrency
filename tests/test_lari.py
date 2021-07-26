# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lari representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Lari
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lari():
    """test_lari."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lari = Lari(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lari.amount == decimal
    assert lari.numeric_code == '981'
    assert lari.alpha_code == 'GEL'
    assert lari.decimal_places == 2
    assert lari.decimal_sign == ','
    assert lari.grouping_places == 3
    assert lari.grouping_sign == '\u202F'
    assert not lari.international
    assert lari.symbol == 'ლ'
    assert not lari.symbol_ahead
    assert lari.symbol_separator == '\u00A0'
    assert lari.convertion == ''
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GEL", '
        'symbol: "ლ", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "981", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert lari.__str__() == '0,14 ლ'


def test_lari_negative():
    """test_lari_negative."""
    amount = -100
    lari = Lari(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lari.numeric_code == '981'
    assert lari.alpha_code == 'GEL'
    assert lari.decimal_places == 2
    assert lari.decimal_sign == ','
    assert lari.grouping_places == 3
    assert lari.grouping_sign == '\u202F'
    assert not lari.international
    assert lari.symbol == 'ლ'
    assert not lari.symbol_ahead
    assert lari.symbol_separator == '\u00A0'
    assert lari.convertion == ''
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: -100, '
        'alpha_code: "GEL", '
        'symbol: "ლ", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "981", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert lari.__str__() == '-100,00 ლ'


def test_lari_custom():
    """test_lari_custom."""
    amount = 1000
    lari = Lari(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert lari.amount == decimal
    assert lari.numeric_code == '981'
    assert lari.alpha_code == 'GEL'
    assert lari.decimal_places == 5
    assert lari.decimal_sign == '\u202F'
    assert lari.grouping_places == 2
    assert lari.grouping_sign == ','
    assert lari.international
    assert lari.symbol == 'ლ'
    assert not lari.symbol_ahead
    assert lari.symbol_separator == '_'
    assert lari.convertion == ''
    assert lari.__hash__() == hash((decimal, 'GEL', '981'))
    assert lari.__repr__() == (
        'Lari(amount: 1000, '
        'alpha_code: "GEL", '
        'symbol: "ლ", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "981", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert lari.__str__() == 'GEL 10,00.00000'


def test_lari_changed():
    """test_clari_changed."""
    lari = Lari(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lari.international = True


def test_lari_math_add():
    """test_lari_math_add."""
    lari_one = Lari(amount=1)
    lari_two = Lari(amount=2)
    lari_three = Lari(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GEL and OTHER.'):
        _ = lari_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lari.Lari\'> '
                   'and <class \'str\'>.')):
        _ = lari_one.__add__('1.00')
    assert (
        lari_one +
        lari_two) == lari_three


def test_lari_slots():
    """test_lari_slots."""
    lari = Lari(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Lari\' '
                'object has no attribute \'new_variable\'')):
        lari.new_variable = 'fail'  # pylint: disable=assigning-non-slot
