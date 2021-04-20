# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the CFA Franc BCEAO representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CFAFrancBCEAO
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cfa_franc_bceao():
    """test_cfa_franc_bceao."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cfa_franc_bceao = CFAFrancBCEAO(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_bceao.amount == decimal
    assert cfa_franc_bceao.numeric_code == '952'
    assert cfa_franc_bceao.alpha_code == 'XOF'
    assert cfa_franc_bceao.decimal_places == 0
    assert cfa_franc_bceao.decimal_sign == ','
    assert cfa_franc_bceao.grouping_sign == '\u202F'
    assert not cfa_franc_bceao.international
    assert cfa_franc_bceao.symbol == '₣'
    assert not cfa_franc_bceao.symbol_ahead
    assert cfa_franc_bceao.symbol_separator == '\u00A0'
    assert cfa_franc_bceao.convertion == ''
    assert cfa_franc_bceao.__hash__() == hash((decimal, 'XOF', '952'))
    assert cfa_franc_bceao.__repr__() == (
        'CFAFrancBCEAO(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XOF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "952", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert cfa_franc_bceao.__str__() == '0 ₣'


def test_cfa_franc_bceao_negative():
    """test_cfa_franc_bceao_negative."""
    amount = -100
    cfa_franc_bceao = CFAFrancBCEAO(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_bceao.numeric_code == '952'
    assert cfa_franc_bceao.alpha_code == 'XOF'
    assert cfa_franc_bceao.decimal_places == 0
    assert cfa_franc_bceao.decimal_sign == ','
    assert cfa_franc_bceao.grouping_sign == '\u202F'
    assert not cfa_franc_bceao.international
    assert cfa_franc_bceao.symbol == '₣'
    assert not cfa_franc_bceao.symbol_ahead
    assert cfa_franc_bceao.symbol_separator == '\u00A0'
    assert cfa_franc_bceao.convertion == ''
    assert cfa_franc_bceao.__hash__() == hash((decimal, 'XOF', '952'))
    assert cfa_franc_bceao.__repr__() == (
        'CFAFrancBCEAO(amount: -100, '
        'alpha_code: "XOF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "952", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: "\u202F", '
        'convertion: "", '
        'international: False)')
    assert cfa_franc_bceao.__str__() == '-100 ₣'


def test_cfa_franc_bceao_custom():
    """test_cfa_franc_bceao_custom."""
    amount = 1000
    cfa_franc_bceao = CFAFrancBCEAO(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u202F',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_bceao.amount == decimal
    assert cfa_franc_bceao.numeric_code == '952'
    assert cfa_franc_bceao.alpha_code == 'XOF'
    assert cfa_franc_bceao.decimal_places == 5
    assert cfa_franc_bceao.decimal_sign == '\u202F'
    assert cfa_franc_bceao.grouping_sign == ','
    assert cfa_franc_bceao.international
    assert cfa_franc_bceao.symbol == '₣'
    assert not cfa_franc_bceao.symbol_ahead
    assert cfa_franc_bceao.symbol_separator == '_'
    assert cfa_franc_bceao.convertion == ''
    assert cfa_franc_bceao.__hash__() == hash((decimal, 'XOF', '952'))
    assert cfa_franc_bceao.__repr__() == (
        'CFAFrancBCEAO(amount: 1000, '
        'alpha_code: "XOF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "952", '
        'decimal_places: "5", '
        'decimal_sign: "\u202F", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert cfa_franc_bceao.__str__() == 'XOF 1,000.00000'


def test_cfa_franc_bceao_changed():
    """test_ccfa_franc_bceao_changed."""
    cfa_franc_bceao = CFAFrancBCEAO(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_bceao.international = True


def test_cfa_franc_bceao_math_add():
    """test_cfa_franc_bceao_math_add."""
    cfa_franc_bceao_one = CFAFrancBCEAO(amount=1)
    cfa_franc_bceao_two = CFAFrancBCEAO(amount=2)
    cfa_franc_bceao_three = CFAFrancBCEAO(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XOF and OTHER.'):
        _ = cfa_franc_bceao_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.CFAFrancBCEAO\'> '
                   'and <class \'str\'>.')):
        _ = cfa_franc_bceao_one.__add__('1.00')
    assert (
        cfa_franc_bceao_one +
        cfa_franc_bceao_two) == cfa_franc_bceao_three


def test_cfa_franc_bceao_slots():
    """test_cfa_franc_bceao_slots."""
    cfa_franc_bceao = CFAFrancBCEAO(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CFAFrancBCEAO\' '
                'object has no attribute \'new_variable\'')):
        cfa_franc_bceao.new_variable = 'fail'  # pylint: disable=assigning-non-slot
