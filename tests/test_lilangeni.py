# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lilangeni representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Lilangeni
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lilangeni():
    """test_lilangeni."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lilangeni = Lilangeni(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lilangeni.amount == decimal
    assert lilangeni.numeric_code == '748'
    assert lilangeni.alpha_code == 'SZL'
    assert lilangeni.decimal_places == 2
    assert lilangeni.decimal_sign == '.'
    assert lilangeni.grouping_sign == ','
    assert not lilangeni.international
    assert lilangeni.symbol == 'L'
    assert lilangeni.__hash__() == hash((decimal, 'SZL', '748'))
    assert lilangeni.__repr__() == (
        'Lilangeni(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SZL", '
        'symbol: "L", '
        'numeric_code: "748", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert lilangeni.__str__() == 'L0.14'


def test_lilangeni_negative():
    """test_lilangeni_negative."""
    amount = -100
    lilangeni = Lilangeni(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lilangeni.numeric_code == '748'
    assert lilangeni.alpha_code == 'SZL'
    assert lilangeni.decimal_places == 2
    assert lilangeni.decimal_sign == '.'
    assert lilangeni.grouping_sign == ','
    assert not lilangeni.international
    assert lilangeni.symbol == 'L'
    assert lilangeni.__hash__() == hash((decimal, 'SZL', '748'))
    assert lilangeni.__repr__() == (
        'Lilangeni(amount: -100, '
        'alpha_code: "SZL", '
        'symbol: "L", '
        'numeric_code: "748", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert lilangeni.__str__() == 'L-100.00'


def test_lilangeni_custom():
    """test_lilangeni_custom."""
    amount = 1000
    lilangeni = Lilangeni(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert lilangeni.amount == decimal
    assert lilangeni.numeric_code == '748'
    assert lilangeni.alpha_code == 'SZL'
    assert lilangeni.decimal_places == 5
    assert lilangeni.decimal_sign == ','
    assert lilangeni.grouping_sign == '.'
    assert lilangeni.international
    assert lilangeni.symbol == 'L'
    assert lilangeni.__hash__() == hash((decimal, 'SZL', '748'))
    assert lilangeni.__repr__() == (
        'Lilangeni(amount: 1000, '
        'alpha_code: "SZL", '
        'symbol: "L", '
        'numeric_code: "748", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert lilangeni.__str__() == 'SZL 1.000,00000'


def test_lilangeni_changed():
    """test_clilangeni_changed."""
    lilangeni = Lilangeni(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lilangeni.international = True


def test_lilangeni_math_add():
    """test_lilangeni_math_add."""
    lilangeni_one = Lilangeni(amount=1)
    lilangeni_two = Lilangeni(amount=2)
    lilangeni_three = Lilangeni(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SZL and OTHER.'):
        _ = lilangeni_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lilangeni.Lilangeni\'> '
                   'and <class \'str\'>.')):
        _ = lilangeni_one.__add__('1.00')
    assert (lilangeni_one + lilangeni_two) == lilangeni_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Lilangeni(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Lilangeni\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
