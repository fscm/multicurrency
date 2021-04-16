# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Swedish Krona representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SwedishKrona
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_swedish_krona():
    """test_swedish_krona."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    swedish_krona = SwedishKrona(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swedish_krona.amount == decimal
    assert swedish_krona.numeric_code == '752'
    assert swedish_krona.alpha_code == 'SEK'
    assert swedish_krona.decimal_places == 2
    assert swedish_krona.decimal_sign == ','
    assert swedish_krona.grouping_sign == '\u202F'
    assert not swedish_krona.international
    assert swedish_krona.symbol == 'kr'
    assert not swedish_krona.symbol_ahead
    assert swedish_krona.symbol_separator == '\u00A0'
    assert swedish_krona.__hash__() == hash((decimal, 'SEK', '752'))
    assert swedish_krona.__repr__() == (
        'SwedishKrona(amount: 0.1428571428571428571428571429, '
        'alpha_code: "SEK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "752", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert swedish_krona.__str__() == '0,14 kr'


def test_swedish_krona_negative():
    """test_swedish_krona_negative."""
    amount = -100
    swedish_krona = SwedishKrona(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swedish_krona.numeric_code == '752'
    assert swedish_krona.alpha_code == 'SEK'
    assert swedish_krona.decimal_places == 2
    assert swedish_krona.decimal_sign == ','
    assert swedish_krona.grouping_sign == '\u202F'
    assert not swedish_krona.international
    assert swedish_krona.symbol == 'kr'
    assert not swedish_krona.symbol_ahead
    assert swedish_krona.symbol_separator == '\u00A0'
    assert swedish_krona.__hash__() == hash((decimal, 'SEK', '752'))
    assert swedish_krona.__repr__() == (
        'SwedishKrona(amount: -100, '
        'alpha_code: "SEK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "752", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'international: False)')
    assert swedish_krona.__str__() == '-100,00 kr'


def test_swedish_krona_custom():
    """test_swedish_krona_custom."""
    amount = 1000
    swedish_krona = SwedishKrona(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert swedish_krona.amount == decimal
    assert swedish_krona.numeric_code == '752'
    assert swedish_krona.alpha_code == 'SEK'
    assert swedish_krona.decimal_places == 5
    assert swedish_krona.decimal_sign == '\u202F'
    assert swedish_krona.grouping_sign == ','
    assert swedish_krona.international
    assert swedish_krona.symbol == 'kr'
    assert not swedish_krona.symbol_ahead
    assert swedish_krona.symbol_separator == '_'
    assert swedish_krona.__hash__() == hash((decimal, 'SEK', '752'))
    assert swedish_krona.__repr__() == (
        'SwedishKrona(amount: 1000, '
        'alpha_code: "SEK", '
        'symbol: "kr", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "752", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'international: True)')
    assert swedish_krona.__str__() == 'SEK 1,000.00000'


def test_swedish_krona_changed():
    """test_cswedish_krona_changed."""
    swedish_krona = SwedishKrona(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swedish_krona.international = True


def test_swedish_krona_math_add():
    """test_swedish_krona_math_add."""
    swedish_krona_one = SwedishKrona(amount=1)
    swedish_krona_two = SwedishKrona(amount=2)
    swedish_krona_three = SwedishKrona(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SEK and OTHER.'):
        _ = swedish_krona_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'krona.SwedishKrona\'> '
                   'and <class \'str\'>.')):
        _ = swedish_krona_one.__add__('1.00')
    assert (
        swedish_krona_one +
        swedish_krona_two) == swedish_krona_three


def test_swedish_krona_slots():
    """test_swedish_krona_slots."""
    swedish_krona = SwedishKrona(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SwedishKrona\' '
                'object has no attribute \'new_variable\'')):
        swedish_krona.new_variable = 'fail'  # pylint: disable=assigning-non-slot
