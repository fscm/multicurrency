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
    assert new_israeli_shekel.code == '376'
    assert new_israeli_shekel.currency == 'ILS'
    assert new_israeli_shekel.decimal_places == 2
    assert new_israeli_shekel.decimal_sign == '.'
    assert new_israeli_shekel.grouping_sign == ','
    assert not new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: 0.1428571428571428571428571429, '
        'currency: "ILS", '
        'symbol: "₪", '
        'code: "376", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert new_israeli_shekel.__str__() == '₪0.14'


def test_new_israeli_shekel_negative():
    """test_new_israeli_shekel_negative."""
    amount = -100
    new_israeli_shekel = NewIsraeliShekel(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert new_israeli_shekel.code == '376'
    assert new_israeli_shekel.currency == 'ILS'
    assert new_israeli_shekel.decimal_places == 2
    assert new_israeli_shekel.decimal_sign == '.'
    assert new_israeli_shekel.grouping_sign == ','
    assert not new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: -100, '
        'currency: "ILS", '
        'symbol: "₪", '
        'code: "376", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert new_israeli_shekel.__str__() == '₪-100.00'


def test_new_israeli_shekel_custom():
    """test_new_israeli_shekel_custom."""
    amount = 1000
    new_israeli_shekel = NewIsraeliShekel(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert new_israeli_shekel.amount == decimal
    assert new_israeli_shekel.code == '376'
    assert new_israeli_shekel.currency == 'ILS'
    assert new_israeli_shekel.decimal_places == 5
    assert new_israeli_shekel.decimal_sign == ','
    assert new_israeli_shekel.grouping_sign == '.'
    assert new_israeli_shekel.international
    assert new_israeli_shekel.symbol == '₪'
    assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
    assert new_israeli_shekel.__repr__() == (
        'NewIsraeliShekel(amount: 1000, '
        'currency: "ILS", '
        'symbol: "₪", '
        'code: "376", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert new_israeli_shekel.__str__() == 'ILS 1.000,00000'


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
        new_israeli_shekel.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        new_israeli_shekel.code = '978'
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
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ILS and OTHER.'):
        _ = new_israeli_shekel_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'new_israeli_shekel.NewIsraeliShekel\'> '
                   'and <class \'str\'>.')):
        _ = new_israeli_shekel_one.__add__('1.00')
    assert (
        new_israeli_shekel_one +
        new_israeli_shekel_two) == new_israeli_shekel_three


def test_currency_slots():
    """test_currency_slots."""
    euro = NewIsraeliShekel(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'NewIsraeliShekel\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
