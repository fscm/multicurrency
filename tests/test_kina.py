# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kina representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Kina
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kina():
    """test_kina."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kina = Kina(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kina.amount == decimal
    assert kina.numeric_code == '598'
    assert kina.alpha_code == 'PGK'
    assert kina.decimal_places == 2
    assert kina.decimal_sign == '.'
    assert kina.grouping_sign == ','
    assert not kina.international
    assert kina.symbol == 'K'
    assert kina.symbol_ahead
    assert kina.symbol_separator == '\u00A0'
    assert kina.convertion == ''
    assert kina.__hash__() == hash((decimal, 'PGK', '598'))
    assert kina.__repr__() == (
        'Kina(amount: 0.1428571428571428571428571429, '
        'alpha_code: "PGK", '
        'symbol: "K", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "598", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert kina.__str__() == 'K 0.14'


def test_kina_negative():
    """test_kina_negative."""
    amount = -100
    kina = Kina(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kina.numeric_code == '598'
    assert kina.alpha_code == 'PGK'
    assert kina.decimal_places == 2
    assert kina.decimal_sign == '.'
    assert kina.grouping_sign == ','
    assert not kina.international
    assert kina.symbol == 'K'
    assert kina.symbol_ahead
    assert kina.symbol_separator == '\u00A0'
    assert kina.convertion == ''
    assert kina.__hash__() == hash((decimal, 'PGK', '598'))
    assert kina.__repr__() == (
        'Kina(amount: -100, '
        'alpha_code: "PGK", '
        'symbol: "K", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "598", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert kina.__str__() == 'K -100.00'


def test_kina_custom():
    """test_kina_custom."""
    amount = 1000
    kina = Kina(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert kina.amount == decimal
    assert kina.numeric_code == '598'
    assert kina.alpha_code == 'PGK'
    assert kina.decimal_places == 5
    assert kina.decimal_sign == ','
    assert kina.grouping_sign == '.'
    assert kina.international
    assert kina.symbol == 'K'
    assert not kina.symbol_ahead
    assert kina.symbol_separator == '_'
    assert kina.convertion == ''
    assert kina.__hash__() == hash((decimal, 'PGK', '598'))
    assert kina.__repr__() == (
        'Kina(amount: 1000, '
        'alpha_code: "PGK", '
        'symbol: "K", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "598", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert kina.__str__() == 'PGK 1,000.00000'


def test_kina_changed():
    """test_ckina_changed."""
    kina = Kina(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kina.international = True


def test_kina_math_add():
    """test_kina_math_add."""
    kina_one = Kina(amount=1)
    kina_two = Kina(amount=2)
    kina_three = Kina(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PGK and OTHER.'):
        _ = kina_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kina.Kina\'> '
                   'and <class \'str\'>.')):
        _ = kina_one.__add__('1.00')
    assert (
        kina_one +
        kina_two) == kina_three


def test_kina_slots():
    """test_kina_slots."""
    kina = Kina(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Kina\' '
                'object has no attribute \'new_variable\'')):
        kina.new_variable = 'fail'  # pylint: disable=assigning-non-slot
