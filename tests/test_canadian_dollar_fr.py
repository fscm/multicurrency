# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Canadian Dollar FR representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CanadianDollarFR
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_canadian_dollar_fr():
    """test_canadian_dollar_fr."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    canadian_dollar_fr = CanadianDollarFR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_fr.amount == decimal
    assert canadian_dollar_fr.numeric_code == '124'
    assert canadian_dollar_fr.alpha_code == 'CAD'
    assert canadian_dollar_fr.decimal_places == 2
    assert canadian_dollar_fr.decimal_sign == ','
    assert canadian_dollar_fr.grouping_sign == '.'
    assert not canadian_dollar_fr.international
    assert canadian_dollar_fr.symbol == '$'
    assert canadian_dollar_fr.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_fr.__repr__() == (
        'CanadianDollarFR(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert canadian_dollar_fr.__str__() == '$0,14'


def test_canadian_dollar_fr_negative():
    """test_canadian_dollar_fr_negative."""
    amount = -100
    canadian_dollar_fr = CanadianDollarFR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_fr.numeric_code == '124'
    assert canadian_dollar_fr.alpha_code == 'CAD'
    assert canadian_dollar_fr.decimal_places == 2
    assert canadian_dollar_fr.decimal_sign == ','
    assert canadian_dollar_fr.grouping_sign == '.'
    assert not canadian_dollar_fr.international
    assert canadian_dollar_fr.symbol == '$'
    assert canadian_dollar_fr.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_fr.__repr__() == (
        'CanadianDollarFR(amount: -100, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert canadian_dollar_fr.__str__() == '$-100,00'


def test_canadian_dollar_fr_custom():
    """test_canadian_dollar_fr_custom."""
    amount = 1000
    canadian_dollar_fr = CanadianDollarFR(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert canadian_dollar_fr.amount == decimal
    assert canadian_dollar_fr.numeric_code == '124'
    assert canadian_dollar_fr.alpha_code == 'CAD'
    assert canadian_dollar_fr.decimal_places == 5
    assert canadian_dollar_fr.decimal_sign == '.'
    assert canadian_dollar_fr.grouping_sign == ','
    assert canadian_dollar_fr.international
    assert canadian_dollar_fr.symbol == '$'
    assert canadian_dollar_fr.__hash__() == hash((decimal, 'CAD', '124'))
    assert canadian_dollar_fr.__repr__() == (
        'CanadianDollarFR(amount: 1000, '
        'alpha_code: "CAD", '
        'symbol: "$", '
        'numeric_code: "124", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert canadian_dollar_fr.__str__() == 'CAD 1,000.00000'


def test_canadian_dollar_fr_changed():
    """test_ccanadian_dollar_fr_changed."""
    canadian_dollar_fr = CanadianDollarFR(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        canadian_dollar_fr.international = True


def test_canadian_dollar_fr_math_add():
    """test_canadian_dollar_fr_math_add."""
    canadian_dollar_fr_one = CanadianDollarFR(amount=1)
    canadian_dollar_fr_two = CanadianDollarFR(amount=2)
    canadian_dollar_fr_three = CanadianDollarFR(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CAD and OTHER.'):
        _ = canadian_dollar_fr_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.CanadianDollarFR\'> '
                   'and <class \'str\'>.')):
        _ = canadian_dollar_fr_one.__add__('1.00')
    assert (canadian_dollar_fr_one + canadian_dollar_fr_two) == canadian_dollar_fr_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CanadianDollarFR(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CanadianDollarFR\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
