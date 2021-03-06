# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Sri Lanka Rupee representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SriLankaRupee
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_sri_lanka_rupee():
    """test_sri_lanka_rupee."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    sri_lanka_rupee = SriLankaRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.amount == decimal
    assert sri_lanka_rupee.numeric_code == '144'
    assert sri_lanka_rupee.alpha_code == 'LKR'
    assert sri_lanka_rupee.decimal_places == 2
    assert sri_lanka_rupee.decimal_sign == '.'
    assert sri_lanka_rupee.grouping_places == 3
    assert sri_lanka_rupee.grouping_sign == ','
    assert not sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'රු.'
    assert sri_lanka_rupee.symbol_ahead
    assert sri_lanka_rupee.symbol_separator == '\u00A0'
    assert sri_lanka_rupee.convertion == ''
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: 0.1428571428571428571428571429, '
        'alpha_code: "LKR", '
        'symbol: "රු.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "144", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert sri_lanka_rupee.__str__() == 'රු. 0.14'


def test_sri_lanka_rupee_negative():
    """test_sri_lanka_rupee_negative."""
    amount = -100
    sri_lanka_rupee = SriLankaRupee(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.numeric_code == '144'
    assert sri_lanka_rupee.alpha_code == 'LKR'
    assert sri_lanka_rupee.decimal_places == 2
    assert sri_lanka_rupee.decimal_sign == '.'
    assert sri_lanka_rupee.grouping_places == 3
    assert sri_lanka_rupee.grouping_sign == ','
    assert not sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'රු.'
    assert sri_lanka_rupee.symbol_ahead
    assert sri_lanka_rupee.symbol_separator == '\u00A0'
    assert sri_lanka_rupee.convertion == ''
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: -100, '
        'alpha_code: "LKR", '
        'symbol: "රු.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "144", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert sri_lanka_rupee.__str__() == 'රු. -100.00'


def test_sri_lanka_rupee_custom():
    """test_sri_lanka_rupee_custom."""
    amount = 1000
    sri_lanka_rupee = SriLankaRupee(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert sri_lanka_rupee.amount == decimal
    assert sri_lanka_rupee.numeric_code == '144'
    assert sri_lanka_rupee.alpha_code == 'LKR'
    assert sri_lanka_rupee.decimal_places == 5
    assert sri_lanka_rupee.decimal_sign == ','
    assert sri_lanka_rupee.grouping_places == 2
    assert sri_lanka_rupee.grouping_sign == '.'
    assert sri_lanka_rupee.international
    assert sri_lanka_rupee.symbol == 'රු.'
    assert not sri_lanka_rupee.symbol_ahead
    assert sri_lanka_rupee.symbol_separator == '_'
    assert sri_lanka_rupee.convertion == ''
    assert sri_lanka_rupee.__hash__() == hash((decimal, 'LKR', '144'))
    assert sri_lanka_rupee.__repr__() == (
        'SriLankaRupee(amount: 1000, '
        'alpha_code: "LKR", '
        'symbol: "රු.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "144", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert sri_lanka_rupee.__str__() == 'LKR 10,00.00000'


def test_sri_lanka_rupee_changed():
    """test_csri_lanka_rupee_changed."""
    sri_lanka_rupee = SriLankaRupee(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        sri_lanka_rupee.international = True


def test_sri_lanka_rupee_math_add():
    """test_sri_lanka_rupee_math_add."""
    sri_lanka_rupee_one = SriLankaRupee(amount=1)
    sri_lanka_rupee_two = SriLankaRupee(amount=2)
    sri_lanka_rupee_three = SriLankaRupee(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency LKR and OTHER.'):
        _ = sri_lanka_rupee_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rupee.SriLankaRupee\'> '
                   'and <class \'str\'>.')):
        _ = sri_lanka_rupee_one.__add__('1.00')
    assert (
        sri_lanka_rupee_one +
        sri_lanka_rupee_two) == sri_lanka_rupee_three


def test_sri_lanka_rupee_slots():
    """test_sri_lanka_rupee_slots."""
    sri_lanka_rupee = SriLankaRupee(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SriLankaRupee\' '
                'object has no attribute \'new_variable\'')):
        sri_lanka_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
