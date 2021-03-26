# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwanza representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kwanza
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kwanza():
    """test_kwanza."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kwanza = Kwanza(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.amount == decimal
    assert kwanza.code == '973'
    assert kwanza.currency == 'AOA'
    assert kwanza.decimal_places == 2
    assert kwanza.decimal_sign == ','
    assert kwanza.grouping_sign == '.'
    assert not kwanza.international
    assert kwanza.symbol == 'Kz'
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: 0.1428571428571428571428571429, '
        'currency: "AOA", '
        'symbol: "Kz", '
        'code: "973", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kwanza.__str__() == 'Kz0,14'


def test_kwanza_negative():
    """test_kwanza_negative."""
    amount = -100
    kwanza = Kwanza(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.code == '973'
    assert kwanza.currency == 'AOA'
    assert kwanza.decimal_places == 2
    assert kwanza.decimal_sign == ','
    assert kwanza.grouping_sign == '.'
    assert not kwanza.international
    assert kwanza.symbol == 'Kz'
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: -100, '
        'currency: "AOA", '
        'symbol: "Kz", '
        'code: "973", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert kwanza.__str__() == 'Kz-100,00'


def test_kwanza_custom():
    """test_kwanza_custom."""
    amount = 1000
    kwanza = Kwanza(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kwanza.amount == decimal
    assert kwanza.code == '973'
    assert kwanza.currency == 'AOA'
    assert kwanza.decimal_places == 5
    assert kwanza.decimal_sign == '.'
    assert kwanza.grouping_sign == ','
    assert kwanza.international
    assert kwanza.symbol == 'Kz'
    assert kwanza.__hash__() == hash((decimal, 'AOA', '973'))
    assert kwanza.__repr__() == (
        'Kwanza(amount: 1000, '
        'currency: "AOA", '
        'symbol: "Kz", '
        'code: "973", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert kwanza.__str__() == 'AOA 1,000.00000'


def test_kwanza_changed():
    """test_ckwanza_changed."""
    kwanza = Kwanza(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kwanza.international = True


def test_kwanza_math_add():
    """test_kwanza_math_add."""
    kwanza_one = Kwanza(amount=1)
    kwanza_two = Kwanza(amount=2)
    kwanza_three = Kwanza(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AOA and OTHER.'):
        _ = kwanza_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kwanza.Kwanza\'> '
                   'and <class \'str\'>.')):
        _ = kwanza_one.__add__('1.00')
    assert (kwanza_one + kwanza_two) == kwanza_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Kwanza(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kwanza\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
