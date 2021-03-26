# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Brazilian Real representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BrazilianReal
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_brazilian_real():
    """test_brazilian_real."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    brazilian_real = BrazilianReal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert brazilian_real.amount == decimal
    assert brazilian_real.code == '986'
    assert brazilian_real.currency == 'BRL'
    assert brazilian_real.decimal_places == 2
    assert brazilian_real.decimal_sign == ','
    assert brazilian_real.grouping_sign == '.'
    assert not brazilian_real.international
    assert brazilian_real.symbol == 'R$'
    assert brazilian_real.__hash__() == hash((decimal, 'BRL', '986'))
    assert brazilian_real.__repr__() == (
        'BrazilianReal(amount: 0.1428571428571428571428571429, '
        'currency: "BRL", '
        'symbol: "R$", '
        'code: "986", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert brazilian_real.__str__() == 'R$0,14'


def test_brazilian_real_negative():
    """test_brazilian_real_negative."""
    amount = -100
    brazilian_real = BrazilianReal(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert brazilian_real.code == '986'
    assert brazilian_real.currency == 'BRL'
    assert brazilian_real.decimal_places == 2
    assert brazilian_real.decimal_sign == ','
    assert brazilian_real.grouping_sign == '.'
    assert not brazilian_real.international
    assert brazilian_real.symbol == 'R$'
    assert brazilian_real.__hash__() == hash((decimal, 'BRL', '986'))
    assert brazilian_real.__repr__() == (
        'BrazilianReal(amount: -100, '
        'currency: "BRL", '
        'symbol: "R$", '
        'code: "986", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert brazilian_real.__str__() == 'R$-100,00'


def test_brazilian_real_custom():
    """test_brazilian_real_custom."""
    amount = 1000
    brazilian_real = BrazilianReal(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert brazilian_real.amount == decimal
    assert brazilian_real.code == '986'
    assert brazilian_real.currency == 'BRL'
    assert brazilian_real.decimal_places == 5
    assert brazilian_real.decimal_sign == '.'
    assert brazilian_real.grouping_sign == ','
    assert brazilian_real.international
    assert brazilian_real.symbol == 'R$'
    assert brazilian_real.__hash__() == hash((decimal, 'BRL', '986'))
    assert brazilian_real.__repr__() == (
        'BrazilianReal(amount: 1000, '
        'currency: "BRL", '
        'symbol: "R$", '
        'code: "986", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert brazilian_real.__str__() == 'BRL 1,000.00000'


def test_brazilian_real_changed():
    """test_cbrazilian_real_changed."""
    brazilian_real = BrazilianReal(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        brazilian_real.international = True


def test_brazilian_real_math_add():
    """test_brazilian_real_math_add."""
    brazilian_real_one = BrazilianReal(amount=1)
    brazilian_real_two = BrazilianReal(amount=2)
    brazilian_real_three = BrazilianReal(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BRL and OTHER.'):
        _ = brazilian_real_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'brazilian_real.BrazilianReal\'> '
                   'and <class \'str\'>.')):
        _ = brazilian_real_one.__add__('1.00')
    assert (brazilian_real_one + brazilian_real_two) == brazilian_real_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BrazilianReal(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BrazilianReal\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
