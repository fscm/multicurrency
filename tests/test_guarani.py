# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Guarani representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Guarani
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_guarani():
    """test_guarani."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    guarani = Guarani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guarani.amount == decimal
    assert guarani.code == '600'
    assert guarani.currency == 'PYG'
    assert guarani.decimal_places == 0
    assert guarani.decimal_sign == ','
    assert guarani.grouping_sign == '.'
    assert not guarani.international
    assert guarani.symbol == '₲'
    assert guarani.__hash__() == hash((decimal, 'PYG', '600'))
    assert guarani.__repr__() == (
        'Guarani(amount: 0.1428571428571428571428571429, '
        'currency: "PYG", '
        'symbol: "₲", '
        'code: "600", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert guarani.__str__() == '₲0'


def test_guarani_negative():
    """test_guarani_negative."""
    amount = -100
    guarani = Guarani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert guarani.code == '600'
    assert guarani.currency == 'PYG'
    assert guarani.decimal_places == 0
    assert guarani.decimal_sign == ','
    assert guarani.grouping_sign == '.'
    assert not guarani.international
    assert guarani.symbol == '₲'
    assert guarani.__hash__() == hash((decimal, 'PYG', '600'))
    assert guarani.__repr__() == (
        'Guarani(amount: -100, '
        'currency: "PYG", '
        'symbol: "₲", '
        'code: "600", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert guarani.__str__() == '₲-100'


def test_guarani_custom():
    """test_guarani_custom."""
    amount = 1000
    guarani = Guarani(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert guarani.amount == decimal
    assert guarani.code == '600'
    assert guarani.currency == 'PYG'
    assert guarani.decimal_places == 5
    assert guarani.decimal_sign == '.'
    assert guarani.grouping_sign == ','
    assert guarani.international
    assert guarani.symbol == '₲'
    assert guarani.__hash__() == hash((decimal, 'PYG', '600'))
    assert guarani.__repr__() == (
        'Guarani(amount: 1000, '
        'currency: "PYG", '
        'symbol: "₲", '
        'code: "600", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert guarani.__str__() == 'PYG 1,000.00000'


def test_guarani_changed():
    """test_cguarani_changed."""
    guarani = Guarani(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        guarani.international = True


def test_guarani_math_add():
    """test_guarani_math_add."""
    guarani_one = Guarani(amount=1)
    guarani_two = Guarani(amount=2)
    guarani_three = Guarani(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PYG and OTHER.'):
        _ = guarani_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'guarani.Guarani\'> '
                   'and <class \'str\'>.')):
        _ = guarani_one.__add__('1.00')
    assert (guarani_one + guarani_two) == guarani_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Guarani(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Guarani\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
