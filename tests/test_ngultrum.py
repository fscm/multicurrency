# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ngultrum representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Ngultrum
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_ngultrum():
    """test_ngultrum."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    ngultrum = Ngultrum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ngultrum.amount == decimal
    assert ngultrum.code == '064'
    assert ngultrum.currency == 'BTN'
    assert ngultrum.decimal_places == 2
    assert ngultrum.decimal_sign == ','
    assert ngultrum.grouping_sign == '.'
    assert not ngultrum.international
    assert ngultrum.symbol == ''
    assert ngultrum.__hash__() == hash((decimal, 'BTN', '064'))
    assert ngultrum.__repr__() == (
        'Ngultrum(amount: 0.1428571428571428571428571429, '
        'currency: "BTN", '
        'symbol: "", '
        'code: "064", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ngultrum.__str__() == '0,14'


def test_ngultrum_negative():
    """test_ngultrum_negative."""
    amount = -100
    ngultrum = Ngultrum(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert ngultrum.code == '064'
    assert ngultrum.currency == 'BTN'
    assert ngultrum.decimal_places == 2
    assert ngultrum.decimal_sign == ','
    assert ngultrum.grouping_sign == '.'
    assert not ngultrum.international
    assert ngultrum.symbol == ''
    assert ngultrum.__hash__() == hash((decimal, 'BTN', '064'))
    assert ngultrum.__repr__() == (
        'Ngultrum(amount: -100, '
        'currency: "BTN", '
        'symbol: "", '
        'code: "064", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert ngultrum.__str__() == '-100,00'


def test_ngultrum_custom():
    """test_ngultrum_custom."""
    amount = 1000
    ngultrum = Ngultrum(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert ngultrum.amount == decimal
    assert ngultrum.code == '064'
    assert ngultrum.currency == 'BTN'
    assert ngultrum.decimal_places == 5
    assert ngultrum.decimal_sign == '.'
    assert ngultrum.grouping_sign == ','
    assert ngultrum.international
    assert ngultrum.symbol == ''
    assert ngultrum.__hash__() == hash((decimal, 'BTN', '064'))
    assert ngultrum.__repr__() == (
        'Ngultrum(amount: 1000, '
        'currency: "BTN", '
        'symbol: "", '
        'code: "064", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert ngultrum.__str__() == 'BTN 1,000.00000'


def test_ngultrum_changed():
    """test_cngultrum_changed."""
    ngultrum = Ngultrum(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        ngultrum.international = True


def test_ngultrum_math_add():
    """test_ngultrum_math_add."""
    ngultrum_one = Ngultrum(amount=1)
    ngultrum_two = Ngultrum(amount=2)
    ngultrum_three = Ngultrum(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BTN and OTHER.'):
        _ = ngultrum_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ngultrum.Ngultrum\'> '
                   'and <class \'str\'>.')):
        _ = ngultrum_one.__add__('1.00')
    assert (ngultrum_one + ngultrum_two) == ngultrum_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Ngultrum(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Ngultrum\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
