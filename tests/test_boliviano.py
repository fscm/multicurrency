# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Boliviano representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Boliviano
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_boliviano():
    """test_boliviano."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    boliviano = Boliviano(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert boliviano.amount == decimal
    assert boliviano.code == '068'
    assert boliviano.currency == 'BOB'
    assert boliviano.decimal_places == 2
    assert boliviano.decimal_sign == '.'
    assert boliviano.grouping_sign == ','
    assert not boliviano.international
    assert boliviano.symbol == 'Bs.'
    assert boliviano.__hash__() == hash((decimal, 'BOB', '068'))
    assert boliviano.__repr__() == (
        'Boliviano(amount: 0.1428571428571428571428571429, '
        'currency: "BOB", '
        'symbol: "Bs.", '
        'code: "068", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert boliviano.__str__() == 'Bs.0.14'


def test_boliviano_negative():
    """test_boliviano_negative."""
    amount = -100
    boliviano = Boliviano(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert boliviano.code == '068'
    assert boliviano.currency == 'BOB'
    assert boliviano.decimal_places == 2
    assert boliviano.decimal_sign == '.'
    assert boliviano.grouping_sign == ','
    assert not boliviano.international
    assert boliviano.symbol == 'Bs.'
    assert boliviano.__hash__() == hash((decimal, 'BOB', '068'))
    assert boliviano.__repr__() == (
        'Boliviano(amount: -100, '
        'currency: "BOB", '
        'symbol: "Bs.", '
        'code: "068", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert boliviano.__str__() == 'Bs.-100.00'


def test_boliviano_custom():
    """test_boliviano_custom."""
    amount = 1000
    boliviano = Boliviano(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert boliviano.amount == decimal
    assert boliviano.code == '068'
    assert boliviano.currency == 'BOB'
    assert boliviano.decimal_places == 5
    assert boliviano.decimal_sign == ','
    assert boliviano.grouping_sign == '.'
    assert boliviano.international
    assert boliviano.symbol == 'Bs.'
    assert boliviano.__hash__() == hash((decimal, 'BOB', '068'))
    assert boliviano.__repr__() == (
        'Boliviano(amount: 1000, '
        'currency: "BOB", '
        'symbol: "Bs.", '
        'code: "068", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert boliviano.__str__() == 'BOB 1.000,00000'


def test_boliviano_changed():
    """test_cboliviano_changed."""
    boliviano = Boliviano(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        boliviano.international = True


def test_boliviano_math_add():
    """test_boliviano_math_add."""
    boliviano_one = Boliviano(amount=1)
    boliviano_two = Boliviano(amount=2)
    boliviano_three = Boliviano(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BOB and OTHER.'):
        _ = boliviano_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'boliviano.Boliviano\'> '
                   'and <class \'str\'>.')):
        _ = boliviano_one.__add__('1.00')
    assert (boliviano_one + boliviano_two) == boliviano_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Boliviano(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Boliviano\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot