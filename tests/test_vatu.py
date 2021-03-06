# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Vatu representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Vatu
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_vatu():
    """test_vatu."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    vatu = Vatu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.amount == decimal
    assert vatu.numeric_code == '548'
    assert vatu.alpha_code == 'VUV'
    assert vatu.decimal_places == 0
    assert vatu.decimal_sign == '.'
    assert vatu.grouping_places == 3
    assert vatu.grouping_sign == ','
    assert not vatu.international
    assert vatu.symbol == 'Vt'
    assert vatu.symbol_ahead
    assert vatu.symbol_separator == '\u00A0'
    assert vatu.convertion == ''
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: 0.1428571428571428571428571429, '
        'alpha_code: "VUV", '
        'symbol: "Vt", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "548", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert vatu.__str__() == 'Vt 0'


def test_vatu_negative():
    """test_vatu_negative."""
    amount = -100
    vatu = Vatu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.numeric_code == '548'
    assert vatu.alpha_code == 'VUV'
    assert vatu.decimal_places == 0
    assert vatu.decimal_sign == '.'
    assert vatu.grouping_places == 3
    assert vatu.grouping_sign == ','
    assert not vatu.international
    assert vatu.symbol == 'Vt'
    assert vatu.symbol_ahead
    assert vatu.symbol_separator == '\u00A0'
    assert vatu.convertion == ''
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: -100, '
        'alpha_code: "VUV", '
        'symbol: "Vt", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "548", '
        'decimal_places: "0", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: False)')
    assert vatu.__str__() == 'Vt -100'


def test_vatu_custom():
    """test_vatu_custom."""
    amount = 1000
    vatu = Vatu(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert vatu.amount == decimal
    assert vatu.numeric_code == '548'
    assert vatu.alpha_code == 'VUV'
    assert vatu.decimal_places == 5
    assert vatu.decimal_sign == ','
    assert vatu.grouping_places == 2
    assert vatu.grouping_sign == '.'
    assert vatu.international
    assert vatu.symbol == 'Vt'
    assert not vatu.symbol_ahead
    assert vatu.symbol_separator == '_'
    assert vatu.convertion == ''
    assert vatu.__hash__() == hash((decimal, 'VUV', '548'))
    assert vatu.__repr__() == (
        'Vatu(amount: 1000, '
        'alpha_code: "VUV", '
        'symbol: "Vt", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "548", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert vatu.__str__() == 'VUV 10,00.00000'


def test_vatu_changed():
    """test_cvatu_changed."""
    vatu = Vatu(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        vatu.international = True


def test_vatu_math_add():
    """test_vatu_math_add."""
    vatu_one = Vatu(amount=1)
    vatu_two = Vatu(amount=2)
    vatu_three = Vatu(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency VUV and OTHER.'):
        _ = vatu_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'vatu.Vatu\'> '
                   'and <class \'str\'>.')):
        _ = vatu_one.__add__('1.00')
    assert (
        vatu_one +
        vatu_two) == vatu_three


def test_vatu_slots():
    """test_vatu_slots."""
    vatu = Vatu(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Vatu\' '
                'object has no attribute \'new_variable\'')):
        vatu.new_variable = 'fail'  # pylint: disable=assigning-non-slot
