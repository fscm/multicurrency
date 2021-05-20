# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Serbian Dinar SR representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SerbianDinarSR
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_serbian_dinar_sr():
    """test_serbian_dinar_sr."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    serbian_dinar_sr = SerbianDinarSR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_sr.amount == decimal
    assert serbian_dinar_sr.numeric_code == '941'
    assert serbian_dinar_sr.alpha_code == 'RSD'
    assert serbian_dinar_sr.decimal_places == 2
    assert serbian_dinar_sr.decimal_sign == ','
    assert serbian_dinar_sr.grouping_sign == '\u202F'
    assert not serbian_dinar_sr.international
    assert serbian_dinar_sr.symbol == 'дин.'
    assert not serbian_dinar_sr.symbol_ahead
    assert serbian_dinar_sr.symbol_separator == '\u00A0'
    assert serbian_dinar_sr.convertion == ''
    assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_sr.__repr__() == (
        'SerbianDinarSR(amount: 0.1428571428571428571428571429, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert serbian_dinar_sr.__str__() == '0,14 дин.'


def test_serbian_dinar_sr_negative():
    """test_serbian_dinar_sr_negative."""
    amount = -100
    serbian_dinar_sr = SerbianDinarSR(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_sr.numeric_code == '941'
    assert serbian_dinar_sr.alpha_code == 'RSD'
    assert serbian_dinar_sr.decimal_places == 2
    assert serbian_dinar_sr.decimal_sign == ','
    assert serbian_dinar_sr.grouping_sign == '\u202F'
    assert not serbian_dinar_sr.international
    assert serbian_dinar_sr.symbol == 'дин.'
    assert not serbian_dinar_sr.symbol_ahead
    assert serbian_dinar_sr.symbol_separator == '\u00A0'
    assert serbian_dinar_sr.convertion == ''
    assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_sr.__repr__() == (
        'SerbianDinarSR(amount: -100, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert serbian_dinar_sr.__str__() == '-100,00 дин.'


def test_serbian_dinar_sr_custom():
    """test_serbian_dinar_sr_custom."""
    amount = 1000
    serbian_dinar_sr = SerbianDinarSR(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_sr.amount == decimal
    assert serbian_dinar_sr.numeric_code == '941'
    assert serbian_dinar_sr.alpha_code == 'RSD'
    assert serbian_dinar_sr.decimal_places == 5
    assert serbian_dinar_sr.decimal_sign == '\u202F'
    assert serbian_dinar_sr.grouping_sign == ','
    assert serbian_dinar_sr.international
    assert serbian_dinar_sr.symbol == 'дин.'
    assert not serbian_dinar_sr.symbol_ahead
    assert serbian_dinar_sr.symbol_separator == '_'
    assert serbian_dinar_sr.convertion == ''
    assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_sr.__repr__() == (
        'SerbianDinarSR(amount: 1000, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "941", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert serbian_dinar_sr.__str__() == 'RSD 1,000.00000'


def test_serbian_dinar_sr_changed():
    """test_cserbian_dinar_sr_changed."""
    serbian_dinar_sr = SerbianDinarSR(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_sr.international = True


def test_serbian_dinar_sr_math_add():
    """test_serbian_dinar_sr_math_add."""
    serbian_dinar_sr_one = SerbianDinarSR(amount=1)
    serbian_dinar_sr_two = SerbianDinarSR(amount=2)
    serbian_dinar_sr_three = SerbianDinarSR(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RSD and OTHER.'):
        _ = serbian_dinar_sr_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.SerbianDinarSR\'> '
                   'and <class \'str\'>.')):
        _ = serbian_dinar_sr_one.__add__('1.00')
    assert (
        serbian_dinar_sr_one +
        serbian_dinar_sr_two) == serbian_dinar_sr_three


def test_serbian_dinar_sr_slots():
    """test_serbian_dinar_sr_slots."""
    serbian_dinar_sr = SerbianDinarSR(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SerbianDinarSR\' '
                'object has no attribute \'new_variable\'')):
        serbian_dinar_sr.new_variable = 'fail'  # pylint: disable=assigning-non-slot
