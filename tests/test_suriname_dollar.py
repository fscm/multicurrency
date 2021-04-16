# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Suriname Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SurinameDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_suriname_dollar():
    """test_suriname_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    suriname_dollar = SurinameDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert suriname_dollar.amount == decimal
    assert suriname_dollar.numeric_code == '968'
    assert suriname_dollar.alpha_code == 'SRD'
    assert suriname_dollar.decimal_places == 2
    assert suriname_dollar.decimal_sign == ','
    assert suriname_dollar.grouping_sign == '.'
    assert not suriname_dollar.international
    assert suriname_dollar.symbol == '$'
    assert suriname_dollar.symbol_ahead
    assert suriname_dollar.symbol_separator == '\u00A0'
    assert suriname_dollar.__hash__() == hash((decimal, 'SRD', '968'))
    assert suriname_dollar.__repr__() == (
        'SurinameDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SRD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "968", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert suriname_dollar.__str__() == '$ 0,14'


def test_suriname_dollar_negative():
    """test_suriname_dollar_negative."""
    amount = -100
    suriname_dollar = SurinameDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert suriname_dollar.numeric_code == '968'
    assert suriname_dollar.alpha_code == 'SRD'
    assert suriname_dollar.decimal_places == 2
    assert suriname_dollar.decimal_sign == ','
    assert suriname_dollar.grouping_sign == '.'
    assert not suriname_dollar.international
    assert suriname_dollar.symbol == '$'
    assert suriname_dollar.symbol_ahead
    assert suriname_dollar.symbol_separator == '\u00A0'
    assert suriname_dollar.__hash__() == hash((decimal, 'SRD', '968'))
    assert suriname_dollar.__repr__() == (
        'SurinameDollar(amount: -100, '
        'alpha_code: "SRD", '
        'symbol: "$", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "968", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert suriname_dollar.__str__() == '$ -100,00'


def test_suriname_dollar_custom():
    """test_suriname_dollar_custom."""
    amount = 1000
    suriname_dollar = SurinameDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert suriname_dollar.amount == decimal
    assert suriname_dollar.numeric_code == '968'
    assert suriname_dollar.alpha_code == 'SRD'
    assert suriname_dollar.decimal_places == 5
    assert suriname_dollar.decimal_sign == '.'
    assert suriname_dollar.grouping_sign == ','
    assert suriname_dollar.international
    assert suriname_dollar.symbol == '$'
    assert not suriname_dollar.symbol_ahead
    assert suriname_dollar.symbol_separator == '_'
    assert suriname_dollar.__hash__() == hash((decimal, 'SRD', '968'))
    assert suriname_dollar.__repr__() == (
        'SurinameDollar(amount: 1000, '
        'alpha_code: "SRD", '
        'symbol: "$", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "968", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert suriname_dollar.__str__() == 'SRD 1,000.00000'


def test_suriname_dollar_changed():
    """test_csuriname_dollar_changed."""
    suriname_dollar = SurinameDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        suriname_dollar.international = True


def test_suriname_dollar_math_add():
    """test_suriname_dollar_math_add."""
    suriname_dollar_one = SurinameDollar(amount=1)
    suriname_dollar_two = SurinameDollar(amount=2)
    suriname_dollar_three = SurinameDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SRD and OTHER.'):
        _ = suriname_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.SurinameDollar\'> '
                   'and <class \'str\'>.')):
        _ = suriname_dollar_one.__add__('1.00')
    assert (
        suriname_dollar_one +
        suriname_dollar_two) == suriname_dollar_three


def test_suriname_dollar_slots():
    """test_suriname_dollar_slots."""
    suriname_dollar = SurinameDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SurinameDollar\' '
                'object has no attribute \'new_variable\'')):
        suriname_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
