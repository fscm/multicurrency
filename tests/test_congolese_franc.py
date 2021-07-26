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
    assert congolese_franc.numeric_code == '976'
    assert congolese_franc.alpha_code == 'CDF'
    assert congolese_franc.decimal_places == 2
    assert congolese_franc.decimal_sign == ','
    assert congolese_franc.grouping_places == 3
    assert congolese_franc.grouping_sign == '\u202F'
    assert not congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert not congolese_franc.symbol_ahead
    assert congolese_franc.symbol_separator == '\u00A0'
    assert congolese_franc.convertion == ''
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CDF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "976", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert congolese_franc.__str__() == '0,14 ₣'


def test_congolese_franc_negative():
    """test_congolese_franc_negative."""
    amount = -100
    congolese_franc = CongoleseFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert congolese_franc.numeric_code == '976'
    assert congolese_franc.alpha_code == 'CDF'
    assert congolese_franc.decimal_places == 2
    assert congolese_franc.decimal_sign == ','
    assert congolese_franc.grouping_places == 3
    assert congolese_franc.grouping_sign == '\u202F'
    assert not congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert not congolese_franc.symbol_ahead
    assert congolese_franc.symbol_separator == '\u00A0'
    assert congolese_franc.convertion == ''
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: -100, '
        'alpha_code: "CDF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "976", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert congolese_franc.__str__() == '-100,00 ₣'


def test_congolese_franc_custom():
    """test_congolese_franc_custom."""
    amount = 1000
    congolese_franc = CongoleseFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert congolese_franc.amount == decimal
    assert congolese_franc.numeric_code == '976'
    assert congolese_franc.alpha_code == 'CDF'
    assert congolese_franc.decimal_places == 5
    assert congolese_franc.decimal_sign == '\u202F'
    assert congolese_franc.grouping_places == 2
    assert congolese_franc.grouping_sign == ','
    assert congolese_franc.international
    assert congolese_franc.symbol == '₣'
    assert not congolese_franc.symbol_ahead
    assert congolese_franc.symbol_separator == '_'
    assert congolese_franc.convertion == ''
    assert congolese_franc.__hash__() == hash((decimal, 'CDF', '976'))
    assert congolese_franc.__repr__() == (
        'CongoleseFranc(amount: 1000, '
        'alpha_code: "CDF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "976", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert congolese_franc.__str__() == 'CDF 10,00.00000'


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
        congolese_franc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        congolese_franc.numeric_code = '978'
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
        congolese_franc.grouping_places = 4
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
    currency = Currency(amount=1, alpha_code='OTHER')
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
    assert (
        congolese_franc_one +
        congolese_franc_two) == congolese_franc_three


def test_congolese_franc_slots():
    """test_congolese_franc_slots."""
    congolese_franc = CongoleseFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CongoleseFranc\' '
                'object has no attribute \'new_variable\'')):
        congolese_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
