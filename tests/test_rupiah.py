# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rupiah representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Rupiah
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rupiah():
    """test_rupiah."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rupiah = Rupiah(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rupiah.amount == decimal
    assert rupiah.code == '360'
    assert rupiah.currency == 'IDR'
    assert rupiah.decimal_places == 2
    assert rupiah.decimal_sign == ','
    assert rupiah.grouping_sign == '.'
    assert not rupiah.international
    assert rupiah.symbol == 'Rp'
    assert rupiah.__hash__() == hash((decimal, 'IDR', '360'))
    assert rupiah.__repr__() == (
        'Rupiah(amount: 0.1428571428571428571428571429, '
        'currency: "IDR", '
        'symbol: "Rp", '
        'code: "360", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rupiah.__str__() == 'Rp0,14'


def test_rupiah_negative():
    """test_rupiah_negative."""
    amount = -100
    rupiah = Rupiah(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rupiah.code == '360'
    assert rupiah.currency == 'IDR'
    assert rupiah.decimal_places == 2
    assert rupiah.decimal_sign == ','
    assert rupiah.grouping_sign == '.'
    assert not rupiah.international
    assert rupiah.symbol == 'Rp'
    assert rupiah.__hash__() == hash((decimal, 'IDR', '360'))
    assert rupiah.__repr__() == (
        'Rupiah(amount: -100, '
        'currency: "IDR", '
        'symbol: "Rp", '
        'code: "360", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert rupiah.__str__() == 'Rp-100,00'


def test_rupiah_custom():
    """test_rupiah_custom."""
    amount = 1000
    rupiah = Rupiah(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert rupiah.amount == decimal
    assert rupiah.code == '360'
    assert rupiah.currency == 'IDR'
    assert rupiah.decimal_places == 5
    assert rupiah.decimal_sign == '.'
    assert rupiah.grouping_sign == ','
    assert rupiah.international
    assert rupiah.symbol == 'Rp'
    assert rupiah.__hash__() == hash((decimal, 'IDR', '360'))
    assert rupiah.__repr__() == (
        'Rupiah(amount: 1000, '
        'currency: "IDR", '
        'symbol: "Rp", '
        'code: "360", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert rupiah.__str__() == 'IDR 1,000.00000'


def test_rupiah_changed():
    """test_crupiah_changed."""
    rupiah = Rupiah(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rupiah.international = True


def test_rupiah_math_add():
    """test_rupiah_math_add."""
    rupiah_one = Rupiah(amount=1)
    rupiah_two = Rupiah(amount=2)
    rupiah_three = Rupiah(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency IDR and OTHER.'):
        _ = rupiah_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupiah.Rupiah\'> '
                   'and <class \'str\'>.')):
        _ = rupiah_one.__add__('1.00')
    assert (rupiah_one + rupiah_two) == rupiah_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Rupiah(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Rupiah\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
