# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dalasi representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Dalasi
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_dalasi():
    """test_dalasi."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    dalasi = Dalasi(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dalasi.amount == decimal
    assert dalasi.numeric_code == '270'
    assert dalasi.alpha_code == 'GMD'
    assert dalasi.decimal_places == 2
    assert dalasi.decimal_sign == ','
    assert dalasi.grouping_sign == '.'
    assert not dalasi.international
    assert dalasi.symbol == 'D'
    assert dalasi.__hash__() == hash((decimal, 'GMD', '270'))
    assert dalasi.__repr__() == (
        'Dalasi(amount: 0.1428571428571428571428571429, '
        'alpha_code: "GMD", '
        'symbol: "D", '
        'numeric_code: "270", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert dalasi.__str__() == 'D0,14'


def test_dalasi_negative():
    """test_dalasi_negative."""
    amount = -100
    dalasi = Dalasi(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert dalasi.numeric_code == '270'
    assert dalasi.alpha_code == 'GMD'
    assert dalasi.decimal_places == 2
    assert dalasi.decimal_sign == ','
    assert dalasi.grouping_sign == '.'
    assert not dalasi.international
    assert dalasi.symbol == 'D'
    assert dalasi.__hash__() == hash((decimal, 'GMD', '270'))
    assert dalasi.__repr__() == (
        'Dalasi(amount: -100, '
        'alpha_code: "GMD", '
        'symbol: "D", '
        'numeric_code: "270", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert dalasi.__str__() == 'D-100,00'


def test_dalasi_custom():
    """test_dalasi_custom."""
    amount = 1000
    dalasi = Dalasi(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert dalasi.amount == decimal
    assert dalasi.numeric_code == '270'
    assert dalasi.alpha_code == 'GMD'
    assert dalasi.decimal_places == 5
    assert dalasi.decimal_sign == '.'
    assert dalasi.grouping_sign == ','
    assert dalasi.international
    assert dalasi.symbol == 'D'
    assert dalasi.__hash__() == hash((decimal, 'GMD', '270'))
    assert dalasi.__repr__() == (
        'Dalasi(amount: 1000, '
        'alpha_code: "GMD", '
        'symbol: "D", '
        'numeric_code: "270", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert dalasi.__str__() == 'GMD 1,000.00000'


def test_dalasi_changed():
    """test_cdalasi_changed."""
    dalasi = Dalasi(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        dalasi.international = True


def test_dalasi_math_add():
    """test_dalasi_math_add."""
    dalasi_one = Dalasi(amount=1)
    dalasi_two = Dalasi(amount=2)
    dalasi_three = Dalasi(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency GMD and OTHER.'):
        _ = dalasi_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dalasi.Dalasi\'> '
                   'and <class \'str\'>.')):
        _ = dalasi_one.__add__('1.00')
    assert (dalasi_one + dalasi_two) == dalasi_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Dalasi(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Dalasi\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
