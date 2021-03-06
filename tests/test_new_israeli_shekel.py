# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the New Israeli Shekel representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, NewIsraeliShekel
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_new_israeli_shekel():
    """test_new_israeli_shekel."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    new_israeli_shekel = NewIsraeliShekel(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert new_israeli_shekel.amount == decimal
    assert new_israeli_shekel.numeric_code == '376'
    assert new_israeli_shekel.alpha_code == 'ILS'
    assert new_israeli_shekel.decimal_places == 2
    assert new_israeli_shekel.decimal_sign == '.'
    assert new_israeli_shekel.grouping_places == 3
    assert new_israeli_shekel.grouping_sign == ','
    assert not new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert not new_israeli_shekel.symbol_ahead
    assert new_israeli_shekel.symbol_separator == '\u00A0'
    assert new_israeli_shekel.convertion == ''
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ILS", '
        'symbol: "₪", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "376", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert new_israeli_shekel.__str__() == '0.14 ₪'


def test_new_israeli_shekel_negative():
    """test_new_israeli_shekel_negative."""
    amount = -100
    new_israeli_shekel = NewIsraeliShekel(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert new_israeli_shekel.numeric_code == '376'
    assert new_israeli_shekel.alpha_code == 'ILS'
    assert new_israeli_shekel.decimal_places == 2
    assert new_israeli_shekel.decimal_sign == '.'
    assert new_israeli_shekel.grouping_places == 3
    assert new_israeli_shekel.grouping_sign == ','
    assert not new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert not new_israeli_shekel.symbol_ahead
    assert new_israeli_shekel.symbol_separator == '\u00A0'
    assert new_israeli_shekel.convertion == ''
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: -100, '
        'alpha_code: "ILS", '
        'symbol: "₪", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "376", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert new_israeli_shekel.__str__() == '-100.00 ₪'


def test_new_israeli_shekel_custom():
    """test_new_israeli_shekel_custom."""
    amount = 1000
    new_israeli_shekel = NewIsraeliShekel(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert new_israeli_shekel.amount == decimal
    assert new_israeli_shekel.numeric_code == '376'
    assert new_israeli_shekel.alpha_code == 'ILS'
    assert new_israeli_shekel.decimal_places == 5
    assert new_israeli_shekel.decimal_sign == ','
    assert new_israeli_shekel.grouping_places == 2
    assert new_israeli_shekel.grouping_sign == '.'
    assert new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert not new_israeli_shekel.symbol_ahead
    assert new_israeli_shekel.symbol_separator == '_'
    assert new_israeli_shekel.convertion == ''
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: 1000, '
        'alpha_code: "ILS", '
        'symbol: "₪", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "376", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert new_israeli_shekel.__str__() == 'ILS 10,00.00000'


def test_new_israeli_shekel_changed():
    """test_cnew_israeli_shekel_changed."""
    new_israeli_shekel = NewIsraeliShekel(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.international = True


def test_new_israeli_shekel_math_add():
    """test_new_israeli_shekel_math_add."""
    new_israeli_shekel_one = NewIsraeliShekel(amount=1)
    new_israeli_shekel_two = NewIsraeliShekel(amount=2)
    new_israeli_shekel_three = NewIsraeliShekel(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ILS and OTHER.'):
        _ = new_israeli_shekel_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'shekel.NewIsraeliShekel\'> '
                   'and <class \'str\'>.')):
        _ = new_israeli_shekel_one.__add__('1.00')
    assert (
        new_israeli_shekel_one +
        new_israeli_shekel_two) == new_israeli_shekel_three


def test_new_israeli_shekel_slots():
    """test_new_israeli_shekel_slots."""
    new_israeli_shekel = NewIsraeliShekel(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NewIsraeliShekel\' '
                'object has no attribute \'new_variable\'')):
        new_israeli_shekel.new_variable = 'fail'  # pylint: disable=assigning-non-slot
