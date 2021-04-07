# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rwanda Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RwandaFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rwanda_franc():
    """test_rwanda_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rwanda_franc = RwandaFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rwanda_franc.amount == decimal
    assert rwanda_franc.code == '646'
    assert rwanda_franc.currency == 'RWF'
    assert rwanda_franc.decimal_places == 0
    assert rwanda_franc.decimal_sign == ','
    assert rwanda_franc.grouping_sign == '.'
    assert not rwanda_franc.international
    assert rwanda_franc.symbol == '₣'
    assert rwanda_franc.__hash__() == hash((decimal, 'RWF', '646'))
    assert rwanda_franc.__repr__() == (
        'RwandaFranc(amount: 0.1428571428571428571428571429, '
        'currency: "RWF", '
        'symbol: "₣", '
        'code: "646", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rwanda_franc.__str__() == '₣0'


def test_rwanda_franc_negative():
    """test_rwanda_franc_negative."""
    amount = -100
    rwanda_franc = RwandaFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rwanda_franc.code == '646'
    assert rwanda_franc.currency == 'RWF'
    assert rwanda_franc.decimal_places == 0
    assert rwanda_franc.decimal_sign == ','
    assert rwanda_franc.grouping_sign == '.'
    assert not rwanda_franc.international
    assert rwanda_franc.symbol == '₣'
    assert rwanda_franc.__hash__() == hash((decimal, 'RWF', '646'))
    assert rwanda_franc.__repr__() == (
        'RwandaFranc(amount: -100, '
        'currency: "RWF", '
        'symbol: "₣", '
        'code: "646", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rwanda_franc.__str__() == '₣-100'


def test_rwanda_franc_custom():
    """test_rwanda_franc_custom."""
    amount = 1000
    rwanda_franc = RwandaFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert rwanda_franc.amount == decimal
    assert rwanda_franc.code == '646'
    assert rwanda_franc.currency == 'RWF'
    assert rwanda_franc.decimal_places == 5
    assert rwanda_franc.decimal_sign == '.'
    assert rwanda_franc.grouping_sign == ','
    assert rwanda_franc.international
    assert rwanda_franc.symbol == '₣'
    assert rwanda_franc.__hash__() == hash((decimal, 'RWF', '646'))
    assert rwanda_franc.__repr__() == (
        'RwandaFranc(amount: 1000, '
        'currency: "RWF", '
        'symbol: "₣", '
        'code: "646", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert rwanda_franc.__str__() == 'RWF 1,000.00000'


def test_rwanda_franc_changed():
    """test_crwanda_franc_changed."""
    rwanda_franc = RwandaFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rwanda_franc.international = True


def test_rwanda_franc_math_add():
    """test_rwanda_franc_math_add."""
    rwanda_franc_one = RwandaFranc(amount=1)
    rwanda_franc_two = RwandaFranc(amount=2)
    rwanda_franc_three = RwandaFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RWF and OTHER.'):
        _ = rwanda_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.RwandaFranc\'> '
                   'and <class \'str\'>.')):
        _ = rwanda_franc_one.__add__('1.00')
    assert (rwanda_franc_one + rwanda_franc_two) == rwanda_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = RwandaFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RwandaFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
