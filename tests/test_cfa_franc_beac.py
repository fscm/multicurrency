# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the CFA Franc BEAC representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CFAFrancBEAC
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cfa_franc_beac():
    """test_cfa_franc_beac."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cfa_franc_beac = CFAFrancBEAC(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_beac.amount == decimal
    assert cfa_franc_beac.numeric_code == '950'
    assert cfa_franc_beac.alpha_code == 'XAF'
    assert cfa_franc_beac.decimal_places == 0
    assert cfa_franc_beac.decimal_sign == ','
    assert cfa_franc_beac.grouping_sign == '.'
    assert not cfa_franc_beac.international
    assert cfa_franc_beac.symbol == '₣'
    assert cfa_franc_beac.__hash__() == hash((decimal, 'XAF', '950'))
    assert cfa_franc_beac.__repr__() == (
        'CFAFrancBEAC(amount: 0.1428571428571428571428571429, '
        'alpha_code: "XAF", '
        'symbol: "₣", '
        'numeric_code: "950", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cfa_franc_beac.__str__() == '₣0'


def test_cfa_franc_beac_negative():
    """test_cfa_franc_beac_negative."""
    amount = -100
    cfa_franc_beac = CFAFrancBEAC(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_beac.numeric_code == '950'
    assert cfa_franc_beac.alpha_code == 'XAF'
    assert cfa_franc_beac.decimal_places == 0
    assert cfa_franc_beac.decimal_sign == ','
    assert cfa_franc_beac.grouping_sign == '.'
    assert not cfa_franc_beac.international
    assert cfa_franc_beac.symbol == '₣'
    assert cfa_franc_beac.__hash__() == hash((decimal, 'XAF', '950'))
    assert cfa_franc_beac.__repr__() == (
        'CFAFrancBEAC(amount: -100, '
        'alpha_code: "XAF", '
        'symbol: "₣", '
        'numeric_code: "950", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cfa_franc_beac.__str__() == '₣-100'


def test_cfa_franc_beac_custom():
    """test_cfa_franc_beac_custom."""
    amount = 1000
    cfa_franc_beac = CFAFrancBEAC(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert cfa_franc_beac.amount == decimal
    assert cfa_franc_beac.numeric_code == '950'
    assert cfa_franc_beac.alpha_code == 'XAF'
    assert cfa_franc_beac.decimal_places == 5
    assert cfa_franc_beac.decimal_sign == '.'
    assert cfa_franc_beac.grouping_sign == ','
    assert cfa_franc_beac.international
    assert cfa_franc_beac.symbol == '₣'
    assert cfa_franc_beac.__hash__() == hash((decimal, 'XAF', '950'))
    assert cfa_franc_beac.__repr__() == (
        'CFAFrancBEAC(amount: 1000, '
        'alpha_code: "XAF", '
        'symbol: "₣", '
        'numeric_code: "950", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert cfa_franc_beac.__str__() == 'XAF 1,000.00000'


def test_cfa_franc_beac_changed():
    """test_ccfa_franc_beac_changed."""
    cfa_franc_beac = CFAFrancBEAC(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfa_franc_beac.international = True


def test_cfa_franc_beac_math_add():
    """test_cfa_franc_beac_math_add."""
    cfa_franc_beac_one = CFAFrancBEAC(amount=1)
    cfa_franc_beac_two = CFAFrancBEAC(amount=2)
    cfa_franc_beac_three = CFAFrancBEAC(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XAF and OTHER.'):
        _ = cfa_franc_beac_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.CFAFrancBEAC\'> '
                   'and <class \'str\'>.')):
        _ = cfa_franc_beac_one.__add__('1.00')
    assert (cfa_franc_beac_one + cfa_franc_beac_two) == cfa_franc_beac_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CFAFrancBEAC(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CFAFrancBEAC\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
