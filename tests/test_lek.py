# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lek representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Lek
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_lek():
    """test_lek."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    lek = Lek(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lek.amount == decimal
    assert lek.numeric_code == '008'
    assert lek.alpha_code == 'ALL'
    assert lek.decimal_places == 2
    assert lek.decimal_sign == ','
    assert lek.grouping_sign == '.'
    assert not lek.international
    assert lek.symbol == 'L'
    assert lek.__hash__() == hash((decimal, 'ALL', '008'))
    assert lek.__repr__() == (
        'Lek(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ALL", '
        'symbol: "L", '
        'numeric_code: "008", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert lek.__str__() == 'L0,14'


def test_lek_negative():
    """test_lek_negative."""
    amount = -100
    lek = Lek(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert lek.numeric_code == '008'
    assert lek.alpha_code == 'ALL'
    assert lek.decimal_places == 2
    assert lek.decimal_sign == ','
    assert lek.grouping_sign == '.'
    assert not lek.international
    assert lek.symbol == 'L'
    assert lek.__hash__() == hash((decimal, 'ALL', '008'))
    assert lek.__repr__() == (
        'Lek(amount: -100, '
        'alpha_code: "ALL", '
        'symbol: "L", '
        'numeric_code: "008", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert lek.__str__() == 'L-100,00'


def test_lek_custom():
    """test_lek_custom."""
    amount = 1000
    lek = Lek(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert lek.amount == decimal
    assert lek.numeric_code == '008'
    assert lek.alpha_code == 'ALL'
    assert lek.decimal_places == 5
    assert lek.decimal_sign == '.'
    assert lek.grouping_sign == ','
    assert lek.international
    assert lek.symbol == 'L'
    assert lek.__hash__() == hash((decimal, 'ALL', '008'))
    assert lek.__repr__() == (
        'Lek(amount: 1000, '
        'alpha_code: "ALL", '
        'symbol: "L", '
        'numeric_code: "008", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert lek.__str__() == 'ALL 1,000.00000'


def test_lek_changed():
    """test_clek_changed."""
    lek = Lek(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        lek.international = True


def test_lek_math_add():
    """test_lek_math_add."""
    lek_one = Lek(amount=1)
    lek_two = Lek(amount=2)
    lek_three = Lek(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ALL and OTHER.'):
        _ = lek_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'lek.Lek\'> '
                   'and <class \'str\'>.')):
        _ = lek_one.__add__('1.00')
    assert (lek_one + lek_two) == lek_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Lek(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Lek\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
