# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Taka representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Taka
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_taka():
    """test_taka."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    taka = Taka(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert taka.amount == decimal
    assert taka.numeric_code == '050'
    assert taka.alpha_code == 'BDT'
    assert taka.decimal_places == 2
    assert taka.decimal_sign == '.'
    assert taka.grouping_sign == ','
    assert not taka.international
    assert taka.symbol == '৳'
    assert taka.__hash__() == hash((decimal, 'BDT', '050'))
    assert taka.__repr__() == (
        'Taka(amount: 0.1428571428571428571428571429, '
        'alpha_code: "BDT", '
        'symbol: "৳", '
        'numeric_code: "050", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert taka.__str__() == '৳0.14'


def test_taka_negative():
    """test_taka_negative."""
    amount = -100
    taka = Taka(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert taka.numeric_code == '050'
    assert taka.alpha_code == 'BDT'
    assert taka.decimal_places == 2
    assert taka.decimal_sign == '.'
    assert taka.grouping_sign == ','
    assert not taka.international
    assert taka.symbol == '৳'
    assert taka.__hash__() == hash((decimal, 'BDT', '050'))
    assert taka.__repr__() == (
        'Taka(amount: -100, '
        'alpha_code: "BDT", '
        'symbol: "৳", '
        'numeric_code: "050", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert taka.__str__() == '৳-100.00'


def test_taka_custom():
    """test_taka_custom."""
    amount = 1000
    taka = Taka(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert taka.amount == decimal
    assert taka.numeric_code == '050'
    assert taka.alpha_code == 'BDT'
    assert taka.decimal_places == 5
    assert taka.decimal_sign == ','
    assert taka.grouping_sign == '.'
    assert taka.international
    assert taka.symbol == '৳'
    assert taka.__hash__() == hash((decimal, 'BDT', '050'))
    assert taka.__repr__() == (
        'Taka(amount: 1000, '
        'alpha_code: "BDT", '
        'symbol: "৳", '
        'numeric_code: "050", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert taka.__str__() == 'BDT 1.000,00000'


def test_taka_changed():
    """test_ctaka_changed."""
    taka = Taka(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        taka.international = True


def test_taka_math_add():
    """test_taka_math_add."""
    taka_one = Taka(amount=1)
    taka_two = Taka(amount=2)
    taka_three = Taka(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BDT and OTHER.'):
        _ = taka_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'taka.Taka\'> '
                   'and <class \'str\'>.')):
        _ = taka_one.__add__('1.00')
    assert (taka_one + taka_two) == taka_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Taka(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Taka\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
