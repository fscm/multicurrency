# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand LS representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RandLS
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rand_ls():
    """test_rand_ls."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rand_ls = RandLS(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_ls.amount == decimal
    assert rand_ls.numeric_code == '710'
    assert rand_ls.alpha_code == 'ZAR'
    assert rand_ls.decimal_places == 2
    assert rand_ls.decimal_sign == '.'
    assert rand_ls.grouping_sign == ','
    assert not rand_ls.international
    assert rand_ls.symbol == 'R'
    assert rand_ls.symbol_ahead
    assert rand_ls.symbol_separator == '\u00A0'
    assert rand_ls.convertion == ''
    assert rand_ls.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_ls.__repr__() == (
        'RandLS(amount: 0.1428571428571428571428571429, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert rand_ls.__str__() == 'R 0.14'


def test_rand_ls_negative():
    """test_rand_ls_negative."""
    amount = -100
    rand_ls = RandLS(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rand_ls.numeric_code == '710'
    assert rand_ls.alpha_code == 'ZAR'
    assert rand_ls.decimal_places == 2
    assert rand_ls.decimal_sign == '.'
    assert rand_ls.grouping_sign == ','
    assert not rand_ls.international
    assert rand_ls.symbol == 'R'
    assert rand_ls.symbol_ahead
    assert rand_ls.symbol_separator == '\u00A0'
    assert rand_ls.convertion == ''
    assert rand_ls.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_ls.__repr__() == (
        'RandLS(amount: -100, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "710", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert rand_ls.__str__() == 'R -100.00'


def test_rand_ls_custom():
    """test_rand_ls_custom."""
    amount = 1000
    rand_ls = RandLS(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert rand_ls.amount == decimal
    assert rand_ls.numeric_code == '710'
    assert rand_ls.alpha_code == 'ZAR'
    assert rand_ls.decimal_places == 5
    assert rand_ls.decimal_sign == ','
    assert rand_ls.grouping_sign == '.'
    assert rand_ls.international
    assert rand_ls.symbol == 'R'
    assert not rand_ls.symbol_ahead
    assert rand_ls.symbol_separator == '_'
    assert rand_ls.convertion == ''
    assert rand_ls.__hash__() == hash((decimal, 'ZAR', '710'))
    assert rand_ls.__repr__() == (
        'RandLS(amount: 1000, '
        'alpha_code: "ZAR", '
        'symbol: "R", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "710", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert rand_ls.__str__() == 'ZAR 1,000.00000'


def test_rand_ls_changed():
    """test_crand_ls_changed."""
    rand_ls = RandLS(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rand_ls.international = True


def test_rand_ls_math_add():
    """test_rand_ls_math_add."""
    rand_ls_one = RandLS(amount=1)
    rand_ls_two = RandLS(amount=2)
    rand_ls_three = RandLS(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ZAR and OTHER.'):
        _ = rand_ls_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rand.RandLS\'> '
                   'and <class \'str\'>.')):
        _ = rand_ls_one.__add__('1.00')
    assert (
        rand_ls_one +
        rand_ls_two) == rand_ls_three


def test_rand_ls_slots():
    """test_rand_ls_slots."""
    rand_ls = RandLS(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RandLS\' '
                'object has no attribute \'new_variable\'')):
        rand_ls.new_variable = 'fail'  # pylint: disable=assigning-non-slot
