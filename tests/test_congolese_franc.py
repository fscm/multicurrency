# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Congolese Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CongoleseFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_congolese_franc():
    """test_congolese_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    congolese_franc = CongoleseFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert congolese_franc.amount == decimal
    assert congolese_franc.code == '976'
    assert congolese_franc.currency == 'CDF'
    assert congolese_franc.decimal_places == 2
    assert congolese_franc.decimal_sign == ','
    assert congolese_franc.grouping_sign == '.'
    assert not congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: 0.1428571428571428571428571429, '
        'currency: "CDF", '
        'symbol: "₣", '
        'code: "976", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert congolese_franc.__str__() == '₣0,14'


def test_congolese_franc_negative():
    """test_congolese_franc_negative."""
    amount = -100
    congolese_franc = CongoleseFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert congolese_franc.code == '976'
    assert congolese_franc.currency == 'CDF'
    assert congolese_franc.decimal_places == 2
    assert congolese_franc.decimal_sign == ','
    assert congolese_franc.grouping_sign == '.'
    assert not congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: -100, '
        'currency: "CDF", '
        'symbol: "₣", '
        'code: "976", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert congolese_franc.__str__() == '₣-100,00'


def test_congolese_franc_custom():
    """test_congolese_franc_custom."""
    amount = 1000
    congolese_franc = CongoleseFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert congolese_franc.amount == decimal
    assert congolese_franc.code == '976'
    assert congolese_franc.currency == 'CDF'
    assert congolese_franc.decimal_places == 5
    assert congolese_franc.decimal_sign == '.'
    assert congolese_franc.grouping_sign == ','
    assert congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: 1000, '
        'currency: "CDF", '
        'symbol: "₣", '
        'code: "976", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert congolese_franc.__str__() == 'CDF 1,000.00000'


def test_congolese_franc_changed():
    """test_ccongolese_franc_changed."""
    congolese_franc = CongoleseFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.international = True


def test_congolese_franc_math_add():
    """test_congolese_franc_math_add."""
    congolese_franc_one = CongoleseFranc(amount=1)
    congolese_franc_two = CongoleseFranc(amount=2)
    congolese_franc_three = CongoleseFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CDF and OTHER.'):
        _ = congolese_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.CongoleseFranc\'> '
                   'and <class \'str\'>.')):
        _ = congolese_franc_one.__add__('1.00')
    assert (congolese_franc_one + congolese_franc_two) == congolese_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CongoleseFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CongoleseFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
