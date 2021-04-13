# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Canadian Dollar EN representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CanadianDollarEN
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_canadian_dollar_en():
    """test_canadian_dollar_en."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    canadian_dollar_en = CanadianDollarEN(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_en.amount == decimal
    assert canadian_dollar_en.numeric_code == '124'
    assert canadian_dollar_en.alpha_code == 'CAD'
    assert canadian_dollar_en.decimal_places == 2
    assert canadian_dollar_en.decimal_sign == '.'
    assert canadian_dollar_en.grouping_sign == ','
    assert not canadian_dollar_en.international
    assert canadian_dollar_en.symbol == '$'
    assert canadian_dollar_en.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_en.__repr__() == (
        'CanadianDollarEN(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert canadian_dollar_en.__str__() == '$0.14'


def test_canadian_dollar_en_negative():
    """test_canadian_dollar_en_negative."""
    amount = -100
    canadian_dollar_en = CanadianDollarEN(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_en.numeric_code == '124'
    assert canadian_dollar_en.alpha_code == 'CAD'
    assert canadian_dollar_en.decimal_places == 2
    assert canadian_dollar_en.decimal_sign == '.'
    assert canadian_dollar_en.grouping_sign == ','
    assert not canadian_dollar_en.international
    assert canadian_dollar_en.symbol == '$'
    assert canadian_dollar_en.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_en.__repr__() == (
        'CanadianDollarEN(amount: -100, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert canadian_dollar_en.__str__() == '$-100.00'


def test_canadian_dollar_en_custom():
    """test_canadian_dollar_en_custom."""
    amount = 1000
    canadian_dollar_en = CanadianDollarEN(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_en.amount == decimal
    assert canadian_dollar_en.numeric_code == '124'
    assert canadian_dollar_en.alpha_code == 'CAD'
    assert canadian_dollar_en.decimal_places == 5
    assert canadian_dollar_en.decimal_sign == ','
    assert canadian_dollar_en.grouping_sign == '.'
    assert canadian_dollar_en.international
    assert canadian_dollar_en.symbol == '$'
    assert canadian_dollar_en.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_en.__repr__() == (
        'CanadianDollarEN(amount: 1000, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert canadian_dollar_en.__str__() == 'CAD 1.000,00000'


def test_canadian_dollar_en_changed():
    """test_ccanadian_dollar_en_changed."""
    canadian_dollar_en = CanadianDollarEN(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_en.international = True


def test_canadian_dollar_en_math_add():
    """test_canadian_dollar_en_math_add."""
    canadian_dollar_en_one = CanadianDollarEN(amount=1)
    canadian_dollar_en_two = CanadianDollarEN(amount=2)
    canadian_dollar_en_three = CanadianDollarEN(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CAD and OTHER.'):
        _ = canadian_dollar_en_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.CanadianDollarEN\'> '
                   'and <class \'str\'>.')):
        _ = canadian_dollar_en_one.__add__('1.00')
    assert (canadian_dollar_en_one + canadian_dollar_en_two) == canadian_dollar_en_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CanadianDollarEN(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CanadianDollarEN\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
