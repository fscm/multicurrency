# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Sri Lanka Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SriLankaRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_sri_lanka_rupee():
    """test_sri_lanka_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    sri_lanka_rupee = SriLankaRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.amount == decimal
    assert sri_lanka_rupee.code == '144'
    assert sri_lanka_rupee.currency == 'LKR'
    assert sri_lanka_rupee.decimal_places == 2
    assert sri_lanka_rupee.decimal_sign == ','
    assert sri_lanka_rupee.grouping_sign == '.'
    assert not sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'Rs'
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: 0.1428571428571428571428571429, '
        'currency: "LKR", '
        'symbol: "Rs", '
        'code: "144", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert sri_lanka_rupee.__str__() == 'Rs0,14'


def test_sri_lanka_rupee_negative():
    """test_sri_lanka_rupee_negative."""
    amount = -100
    sri_lanka_rupee = SriLankaRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.code == '144'
    assert sri_lanka_rupee.currency == 'LKR'
    assert sri_lanka_rupee.decimal_places == 2
    assert sri_lanka_rupee.decimal_sign == ','
    assert sri_lanka_rupee.grouping_sign == '.'
    assert not sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'Rs'
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: -100, '
        'currency: "LKR", '
        'symbol: "Rs", '
        'code: "144", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert sri_lanka_rupee.__str__() == 'Rs-100,00'


def test_sri_lanka_rupee_custom():
    """test_sri_lanka_rupee_custom."""
    amount = 1000
    sri_lanka_rupee = SriLankaRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.amount == decimal
    assert sri_lanka_rupee.code == '144'
    assert sri_lanka_rupee.currency == 'LKR'
    assert sri_lanka_rupee.decimal_places == 5
    assert sri_lanka_rupee.decimal_sign == '.'
    assert sri_lanka_rupee.grouping_sign == ','
    assert sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'Rs'
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: 1000, '
        'currency: "LKR", '
        'symbol: "Rs", '
        'code: "144", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert sri_lanka_rupee.__str__() == 'LKR 1,000.00000'


def test_sri_lanka_rupee_changed():
    """test_csri_lanka_rupee_changed."""
    sri_lanka_rupee = SriLankaRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.international = True


def test_sri_lanka_rupee_math_add():
    """test_sri_lanka_rupee_math_add."""
    sri_lanka_rupee_one = SriLankaRupee(amount=1)
    sri_lanka_rupee_two = SriLankaRupee(amount=2)
    sri_lanka_rupee_three = SriLankaRupee(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LKR and OTHER.'):
        _ = sri_lanka_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'sri_lanka_rupee.SriLankaRupee\'> '
                   'and <class \'str\'>.')):
        _ = sri_lanka_rupee_one.__add__('1.00')
    assert (sri_lanka_rupee_one + sri_lanka_rupee_two) == sri_lanka_rupee_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SriLankaRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SriLankaRupee\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
