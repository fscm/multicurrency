# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pakistan Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PakistanRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_pakistan_rupee():
    """test_pakistan_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    pakistan_rupee = PakistanRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.amount == decimal
    assert pakistan_rupee.numeric_code == '586'
    assert pakistan_rupee.alpha_code == 'PKR'
    assert pakistan_rupee.decimal_places == 2
    assert pakistan_rupee.decimal_sign == '.'
    assert pakistan_rupee.grouping_places == 3
    assert pakistan_rupee.grouping_sign == ','
    assert not pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert pakistan_rupee.symbol_ahead
    assert pakistan_rupee.symbol_separator == '\u00A0'
    assert pakistan_rupee.convertion == ''
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: 0.1428571428571428571428571429, '
        'alpha_code: "PKR", '
        'symbol: "₨", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "586", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert pakistan_rupee.__str__() == '₨ 0.14'


def test_pakistan_rupee_negative():
    """test_pakistan_rupee_negative."""
    amount = -100
    pakistan_rupee = PakistanRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.numeric_code == '586'
    assert pakistan_rupee.alpha_code == 'PKR'
    assert pakistan_rupee.decimal_places == 2
    assert pakistan_rupee.decimal_sign == '.'
    assert pakistan_rupee.grouping_places == 3
    assert pakistan_rupee.grouping_sign == ','
    assert not pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert pakistan_rupee.symbol_ahead
    assert pakistan_rupee.symbol_separator == '\u00A0'
    assert pakistan_rupee.convertion == ''
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: -100, '
        'alpha_code: "PKR", '
        'symbol: "₨", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "586", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert pakistan_rupee.__str__() == '₨ -100.00'


def test_pakistan_rupee_custom():
    """test_pakistan_rupee_custom."""
    amount = 1000
    pakistan_rupee = PakistanRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert pakistan_rupee.amount == decimal
    assert pakistan_rupee.numeric_code == '586'
    assert pakistan_rupee.alpha_code == 'PKR'
    assert pakistan_rupee.decimal_places == 5
    assert pakistan_rupee.decimal_sign == ','
    assert pakistan_rupee.grouping_places == 2
    assert pakistan_rupee.grouping_sign == '.'
    assert pakistan_rupee.international
    assert pakistan_rupee.symbol == '₨'
    assert not pakistan_rupee.symbol_ahead
    assert pakistan_rupee.symbol_separator == '_'
    assert pakistan_rupee.convertion == ''
    assert pakistan_rupee.__hash__() == hash((decimal, 'PKR', '586'))
    assert pakistan_rupee.__repr__() == (
        'PakistanRupee(amount: 1000, '
        'alpha_code: "PKR", '
        'symbol: "₨", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "586", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert pakistan_rupee.__str__() == 'PKR 10,00.00000'


def test_pakistan_rupee_changed():
    """test_cpakistan_rupee_changed."""
    pakistan_rupee = PakistanRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        pakistan_rupee.international = True


def test_pakistan_rupee_math_add():
    """test_pakistan_rupee_math_add."""
    pakistan_rupee_one = PakistanRupee(amount=1)
    pakistan_rupee_two = PakistanRupee(amount=2)
    pakistan_rupee_three = PakistanRupee(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PKR and OTHER.'):
        _ = pakistan_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupee.PakistanRupee\'> '
                   'and <class \'str\'>.')):
        _ = pakistan_rupee_one.__add__('1.00')
    assert (
        pakistan_rupee_one +
        pakistan_rupee_two) == pakistan_rupee_three


def test_pakistan_rupee_slots():
    """test_pakistan_rupee_slots."""
    pakistan_rupee = PakistanRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PakistanRupee\' '
                'object has no attribute \'new_variable\'')):
        pakistan_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
