# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Konvertibilna Marka representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, KonvertibilnaMarka
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_konvertibilna_marka():
    """test_konvertibilna_marka."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    konvertibilna_marka = KonvertibilnaMarka(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert konvertibilna_marka.amount == decimal
    assert konvertibilna_marka.code == '977'
    assert konvertibilna_marka.currency == 'BAM'
    assert konvertibilna_marka.decimal_places == 2
    assert konvertibilna_marka.decimal_sign == '.'
    assert konvertibilna_marka.grouping_sign == ','
    assert not konvertibilna_marka.international
    assert konvertibilna_marka.symbol == 'КМ'
    assert konvertibilna_marka.__hash__() == hash((decimal, 'BAM', '977'))
    assert konvertibilna_marka.__repr__() == (
        'KonvertibilnaMarka(amount: 0.1428571428571428571428571429, '
        'currency: "BAM", '
        'symbol: "КМ", '
        'code: "977", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert konvertibilna_marka.__str__() == 'КМ0.14'


def test_konvertibilna_marka_negative():
    """test_konvertibilna_marka_negative."""
    amount = -100
    konvertibilna_marka = KonvertibilnaMarka(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert konvertibilna_marka.code == '977'
    assert konvertibilna_marka.currency == 'BAM'
    assert konvertibilna_marka.decimal_places == 2
    assert konvertibilna_marka.decimal_sign == '.'
    assert konvertibilna_marka.grouping_sign == ','
    assert not konvertibilna_marka.international
    assert konvertibilna_marka.symbol == 'КМ'
    assert konvertibilna_marka.__hash__() == hash((decimal, 'BAM', '977'))
    assert konvertibilna_marka.__repr__() == (
        'KonvertibilnaMarka(amount: -100, '
        'currency: "BAM", '
        'symbol: "КМ", '
        'code: "977", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert konvertibilna_marka.__str__() == 'КМ-100.00'


def test_konvertibilna_marka_custom():
    """test_konvertibilna_marka_custom."""
    amount = 1000
    konvertibilna_marka = KonvertibilnaMarka(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert konvertibilna_marka.amount == decimal
    assert konvertibilna_marka.code == '977'
    assert konvertibilna_marka.currency == 'BAM'
    assert konvertibilna_marka.decimal_places == 5
    assert konvertibilna_marka.decimal_sign == ','
    assert konvertibilna_marka.grouping_sign == '.'
    assert konvertibilna_marka.international
    assert konvertibilna_marka.symbol == 'КМ'
    assert konvertibilna_marka.__hash__() == hash((decimal, 'BAM', '977'))
    assert konvertibilna_marka.__repr__() == (
        'KonvertibilnaMarka(amount: 1000, '
        'currency: "BAM", '
        'symbol: "КМ", '
        'code: "977", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert konvertibilna_marka.__str__() == 'BAM 1.000,00000'


def test_konvertibilna_marka_changed():
    """test_ckonvertibilna_marka_changed."""
    konvertibilna_marka = KonvertibilnaMarka(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        konvertibilna_marka.international = True


def test_konvertibilna_marka_math_add():
    """test_konvertibilna_marka_math_add."""
    konvertibilna_marka_one = KonvertibilnaMarka(amount=1)
    konvertibilna_marka_two = KonvertibilnaMarka(amount=2)
    konvertibilna_marka_three = KonvertibilnaMarka(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BAM and OTHER.'):
        _ = konvertibilna_marka_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'marka.KonvertibilnaMarka\'> '
                   'and <class \'str\'>.')):
        _ = konvertibilna_marka_one.__add__('1.00')
    assert (
        konvertibilna_marka_one +
        konvertibilna_marka_two) == konvertibilna_marka_three


def test_currency_slots():
    """test_currency_slots."""
    euro = KonvertibilnaMarka(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'KonvertibilnaMarka\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
