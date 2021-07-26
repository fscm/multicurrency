# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Azerbaijanian Manat representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, AzerbaijanianManat
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_azerbaijanian_manat():
    """test_azerbaijanian_manat."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    azerbaijanian_manat = AzerbaijanianManat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert azerbaijanian_manat.amount == decimal
    assert azerbaijanian_manat.numeric_code == '944'
    assert azerbaijanian_manat.alpha_code == 'AZN'
    assert azerbaijanian_manat.decimal_places == 2
    assert azerbaijanian_manat.decimal_sign == ','
    assert azerbaijanian_manat.grouping_places == 3
    assert azerbaijanian_manat.grouping_sign == '.'
    assert not azerbaijanian_manat.international
    assert azerbaijanian_manat.symbol == '₼'
    assert not azerbaijanian_manat.symbol_ahead
    assert azerbaijanian_manat.symbol_separator == '\u00A0'
    assert azerbaijanian_manat.convertion == ''
    assert azerbaijanian_manat.__hash__() == hash((decimal, 'AZN', '944'))
    assert azerbaijanian_manat.__repr__() == (
        'AzerbaijanianManat(amount: 0.1428571428571428571428571429, '
        'alpha_code: "AZN", '
        'symbol: "₼", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "944", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert azerbaijanian_manat.__str__() == '0,14 ₼'


def test_azerbaijanian_manat_negative():
    """test_azerbaijanian_manat_negative."""
    amount = -100
    azerbaijanian_manat = AzerbaijanianManat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert azerbaijanian_manat.numeric_code == '944'
    assert azerbaijanian_manat.alpha_code == 'AZN'
    assert azerbaijanian_manat.decimal_places == 2
    assert azerbaijanian_manat.decimal_sign == ','
    assert azerbaijanian_manat.grouping_places == 3
    assert azerbaijanian_manat.grouping_sign == '.'
    assert not azerbaijanian_manat.international
    assert azerbaijanian_manat.symbol == '₼'
    assert not azerbaijanian_manat.symbol_ahead
    assert azerbaijanian_manat.symbol_separator == '\u00A0'
    assert azerbaijanian_manat.convertion == ''
    assert azerbaijanian_manat.__hash__() == hash((decimal, 'AZN', '944'))
    assert azerbaijanian_manat.__repr__() == (
        'AzerbaijanianManat(amount: -100, '
        'alpha_code: "AZN", '
        'symbol: "₼", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "944", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_places: "3", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert azerbaijanian_manat.__str__() == '-100,00 ₼'


def test_azerbaijanian_manat_custom():
    """test_azerbaijanian_manat_custom."""
    amount = 1000
    azerbaijanian_manat = AzerbaijanianManat(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_places=2,
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert azerbaijanian_manat.amount == decimal
    assert azerbaijanian_manat.numeric_code == '944'
    assert azerbaijanian_manat.alpha_code == 'AZN'
    assert azerbaijanian_manat.decimal_places == 5
    assert azerbaijanian_manat.decimal_sign == '.'
    assert azerbaijanian_manat.grouping_places == 2
    assert azerbaijanian_manat.grouping_sign == ','
    assert azerbaijanian_manat.international
    assert azerbaijanian_manat.symbol == '₼'
    assert not azerbaijanian_manat.symbol_ahead
    assert azerbaijanian_manat.symbol_separator == '_'
    assert azerbaijanian_manat.convertion == ''
    assert azerbaijanian_manat.__hash__() == hash((decimal, 'AZN', '944'))
    assert azerbaijanian_manat.__repr__() == (
        'AzerbaijanianManat(amount: 1000, '
        'alpha_code: "AZN", '
        'symbol: "₼", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "944", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_places: "2", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert azerbaijanian_manat.__str__() == 'AZN 10,00.00000'


def test_azerbaijanian_manat_changed():
    """test_cazerbaijanian_manat_changed."""
    azerbaijanian_manat = AzerbaijanianManat(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        azerbaijanian_manat.international = True


def test_azerbaijanian_manat_math_add():
    """test_azerbaijanian_manat_math_add."""
    azerbaijanian_manat_one = AzerbaijanianManat(amount=1)
    azerbaijanian_manat_two = AzerbaijanianManat(amount=2)
    azerbaijanian_manat_three = AzerbaijanianManat(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency AZN and OTHER.'):
        _ = azerbaijanian_manat_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'manat.AzerbaijanianManat\'> '
                   'and <class \'str\'>.')):
        _ = azerbaijanian_manat_one.__add__('1.00')
    assert (
        azerbaijanian_manat_one +
        azerbaijanian_manat_two) == azerbaijanian_manat_three


def test_azerbaijanian_manat_slots():
    """test_azerbaijanian_manat_slots."""
    azerbaijanian_manat = AzerbaijanianManat(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'AzerbaijanianManat\' '
                'object has no attribute \'new_variable\'')):
        azerbaijanian_manat.new_variable = 'fail'  # pylint: disable=assigning-non-slot
