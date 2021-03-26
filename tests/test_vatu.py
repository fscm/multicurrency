# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Vatu representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Vatu
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_vatu():
    """test_vatu."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    vatu = Vatu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.amount == decimal
    assert vatu.code == '548'
    assert vatu.currency == 'VUV'
    assert vatu.decimal_places == 0
    assert vatu.decimal_sign == '.'
    assert vatu.grouping_sign == ','
    assert not vatu.international
    assert vatu.symbol == 'Vt'
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: 0.1428571428571428571428571429, '
        'currency: "VUV", '
        'symbol: "Vt", '
        'code: "548", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert vatu.__str__() == 'Vt0'


def test_vatu_negative():
    """test_vatu_negative."""
    amount = -100
    vatu = Vatu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.code == '548'
    assert vatu.currency == 'VUV'
    assert vatu.decimal_places == 0
    assert vatu.decimal_sign == '.'
    assert vatu.grouping_sign == ','
    assert not vatu.international
    assert vatu.symbol == 'Vt'
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: -100, '
        'currency: "VUV", '
        'symbol: "Vt", '
        'code: "548", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert vatu.__str__() == 'Vt-100'


def test_vatu_custom():
    """test_vatu_custom."""
    amount = 1000
    vatu = Vatu(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.amount == decimal
    assert vatu.code == '548'
    assert vatu.currency == 'VUV'
    assert vatu.decimal_places == 5
    assert vatu.decimal_sign == ','
    assert vatu.grouping_sign == '.'
    assert vatu.international
    assert vatu.symbol == 'Vt'
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: 1000, '
        'currency: "VUV", '
        'symbol: "Vt", '
        'code: "548", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert vatu.__str__() == 'VUV 1.000,00000'


def test_vatu_changed():
    """test_cvatu_changed."""
    vatu = Vatu(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.international = True


def test_vatu_math_add():
    """test_vatu_math_add."""
    vatu_one = Vatu(amount=1)
    vatu_two = Vatu(amount=2)
    vatu_three = Vatu(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency VUV and OTHER.'):
        _ = vatu_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'vatu.Vatu\'> '
                   'and <class \'str\'>.')):
        _ = vatu_one.__add__('1.00')
    assert (vatu_one + vatu_two) == vatu_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Vatu(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Vatu\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
