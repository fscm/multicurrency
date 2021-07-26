# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Serbian Dinar XK representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SerbianDinarXK
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_serbian_dinar_xk():
    """test_serbian_dinar_xk."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    serbian_dinar_xk = SerbianDinarXK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_xk.amount == decimal
    assert serbian_dinar_xk.numeric_code == '941'
    assert serbian_dinar_xk.alpha_code == 'RSD'
    assert serbian_dinar_xk.decimal_places == 2
    assert serbian_dinar_xk.decimal_sign == ','
    assert serbian_dinar_xk.grouping_places == 3
    assert serbian_dinar_xk.grouping_sign == '.'
    assert not serbian_dinar_xk.international
    assert serbian_dinar_xk.symbol == 'дин.'
    assert not serbian_dinar_xk.symbol_ahead
    assert serbian_dinar_xk.symbol_separator == '\u00A0'
    assert serbian_dinar_xk.convertion == ''
    assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_xk.__repr__() == (
        'SerbianDinarXK(amount: 0.1428571428571428571428571429, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert serbian_dinar_xk.__str__() == '0,14 дин.'


def test_serbian_dinar_xk_negative():
    """test_serbian_dinar_xk_negative."""
    amount = -100
    serbian_dinar_xk = SerbianDinarXK(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_xk.numeric_code == '941'
    assert serbian_dinar_xk.alpha_code == 'RSD'
    assert serbian_dinar_xk.decimal_places == 2
    assert serbian_dinar_xk.decimal_sign == ','
    assert serbian_dinar_xk.grouping_places == 3
    assert serbian_dinar_xk.grouping_sign == '.'
    assert not serbian_dinar_xk.international
    assert serbian_dinar_xk.symbol == 'дин.'
    assert not serbian_dinar_xk.symbol_ahead
    assert serbian_dinar_xk.symbol_separator == '\u00A0'
    assert serbian_dinar_xk.convertion == ''
    assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_xk.__repr__() == (
        'SerbianDinarXK(amount: -100, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "941", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert serbian_dinar_xk.__str__() == '-100,00 дин.'


def test_serbian_dinar_xk_custom():
    """test_serbian_dinar_xk_custom."""
    amount = 1000
    serbian_dinar_xk = SerbianDinarXK(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert serbian_dinar_xk.amount == decimal
    assert serbian_dinar_xk.numeric_code == '941'
    assert serbian_dinar_xk.alpha_code == 'RSD'
    assert serbian_dinar_xk.decimal_places == 5
    assert serbian_dinar_xk.decimal_sign == '.'
    assert serbian_dinar_xk.grouping_places == 2
    assert serbian_dinar_xk.grouping_sign == ','
    assert serbian_dinar_xk.international
    assert serbian_dinar_xk.symbol == 'дин.'
    assert not serbian_dinar_xk.symbol_ahead
    assert serbian_dinar_xk.symbol_separator == '_'
    assert serbian_dinar_xk.convertion == ''
    assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
    assert serbian_dinar_xk.__repr__() == (
        'SerbianDinarXK(amount: 1000, '
        'alpha_code: "RSD", '
        'symbol: "дин.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "941", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert serbian_dinar_xk.__str__() == 'RSD 10,00.00000'


def test_serbian_dinar_xk_changed():
    """test_cserbian_dinar_xk_changed."""
    serbian_dinar_xk = SerbianDinarXK(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        serbian_dinar_xk.international = True


def test_serbian_dinar_xk_math_add():
    """test_serbian_dinar_xk_math_add."""
    serbian_dinar_xk_one = SerbianDinarXK(amount=1)
    serbian_dinar_xk_two = SerbianDinarXK(amount=2)
    serbian_dinar_xk_three = SerbianDinarXK(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RSD and OTHER.'):
        _ = serbian_dinar_xk_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'dinar.SerbianDinarXK\'> '
                   'and <class \'str\'>.')):
        _ = serbian_dinar_xk_one.__add__('1.00')
    assert (
        serbian_dinar_xk_one +
        serbian_dinar_xk_two) == serbian_dinar_xk_three


def test_serbian_dinar_xk_slots():
    """test_serbian_dinar_xk_slots."""
    serbian_dinar_xk = SerbianDinarXK(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SerbianDinarXK\' '
                'object has no attribute \'new_variable\'')):
        serbian_dinar_xk.new_variable = 'fail'  # pylint: disable=assigning-non-slot
