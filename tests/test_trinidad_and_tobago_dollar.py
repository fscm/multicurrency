# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Trinidad and Tobago Dollar representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, TrinidadandTobagoDollar
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_trinidad_and_tobago_dollar():
    """test_trinidad_and_tobago_dollar."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert trinidad_and_tobago_dollar.amount == decimal
    assert trinidad_and_tobago_dollar.numeric_code == '780'
    assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
    assert trinidad_and_tobago_dollar.decimal_places == 2
    assert trinidad_and_tobago_dollar.decimal_sign == ','
    assert trinidad_and_tobago_dollar.grouping_sign == '.'
    assert not trinidad_and_tobago_dollar.international
    assert trinidad_and_tobago_dollar.symbol == '$'
    assert trinidad_and_tobago_dollar.__hash__() == hash((decimal, 'TTD', '780'))
    assert trinidad_and_tobago_dollar.__repr__() == (
        'TrinidadandTobagoDollar(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TTD", '
        'symbol: "$", '
        'numeric_code: "780", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert trinidad_and_tobago_dollar.__str__() == '$0,14'


def test_trinidad_and_tobago_dollar_negative():
    """test_trinidad_and_tobago_dollar_negative."""
    amount = -100
    trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert trinidad_and_tobago_dollar.numeric_code == '780'
    assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
    assert trinidad_and_tobago_dollar.decimal_places == 2
    assert trinidad_and_tobago_dollar.decimal_sign == ','
    assert trinidad_and_tobago_dollar.grouping_sign == '.'
    assert not trinidad_and_tobago_dollar.international
    assert trinidad_and_tobago_dollar.symbol == '$'
    assert trinidad_and_tobago_dollar.__hash__() == hash((decimal, 'TTD', '780'))
    assert trinidad_and_tobago_dollar.__repr__() == (
        'TrinidadandTobagoDollar(amount: -100, '
        'alpha_code: "TTD", '
        'symbol: "$", '
        'numeric_code: "780", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert trinidad_and_tobago_dollar.__str__() == '$-100,00'


def test_trinidad_and_tobago_dollar_custom():
    """test_trinidad_and_tobago_dollar_custom."""
    amount = 1000
    trinidad_and_tobago_dollar = TrinidadandTobagoDollar(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert trinidad_and_tobago_dollar.amount == decimal
    assert trinidad_and_tobago_dollar.numeric_code == '780'
    assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
    assert trinidad_and_tobago_dollar.decimal_places == 5
    assert trinidad_and_tobago_dollar.decimal_sign == '.'
    assert trinidad_and_tobago_dollar.grouping_sign == ','
    assert trinidad_and_tobago_dollar.international
    assert trinidad_and_tobago_dollar.symbol == '$'
    assert trinidad_and_tobago_dollar.__hash__() == hash((decimal, 'TTD', '780'))
    assert trinidad_and_tobago_dollar.__repr__() == (
        'TrinidadandTobagoDollar(amount: 1000, '
        'alpha_code: "TTD", '
        'symbol: "$", '
        'numeric_code: "780", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert trinidad_and_tobago_dollar.__str__() == 'TTD 1,000.00000'


def test_trinidad_and_tobago_dollar_changed():
    """test_ctrinidad_and_tobago_dollar_changed."""
    trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        trinidad_and_tobago_dollar.international = True


def test_trinidad_and_tobago_dollar_math_add():
    """test_trinidad_and_tobago_dollar_math_add."""
    trinidad_and_tobago_dollar_one = TrinidadandTobagoDollar(amount=1)
    trinidad_and_tobago_dollar_two = TrinidadandTobagoDollar(amount=2)
    trinidad_and_tobago_dollar_three = TrinidadandTobagoDollar(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TTD and OTHER.'):
        _ = trinidad_and_tobago_dollar_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dollar.TrinidadandTobagoDollar\'> '
                   'and <class \'str\'>.')):
        _ = trinidad_and_tobago_dollar_one.__add__('1.00')
    assert (trinidad_and_tobago_dollar_one + trinidad_and_tobago_dollar_two) == trinidad_and_tobago_dollar_three


def test_currency_slots():
    """test_currency_slots."""
    euro = TrinidadandTobagoDollar(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'TrinidadandTobagoDollar\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
