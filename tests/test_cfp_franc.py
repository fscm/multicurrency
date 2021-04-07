# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the CFP Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CFPFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cfp_franc():
    """test_cfp_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cfp_franc = CFPFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfp_franc.amount == decimal
    assert cfp_franc.code == '953'
    assert cfp_franc.currency == 'XPF'
    assert cfp_franc.decimal_places == 0
    assert cfp_franc.decimal_sign == ','
    assert cfp_franc.grouping_sign == '.'
    assert not cfp_franc.international
    assert cfp_franc.symbol == '₣'
    assert cfp_franc.__hash__() == hash((decimal, 'XPF', '953'))
    assert cfp_franc.__repr__() == (
        'CFPFranc(amount: 0.1428571428571428571428571429, '
        'currency: "XPF", '
        'symbol: "₣", '
        'code: "953", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cfp_franc.__str__() == '₣0'


def test_cfp_franc_negative():
    """test_cfp_franc_negative."""
    amount = -100
    cfp_franc = CFPFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cfp_franc.code == '953'
    assert cfp_franc.currency == 'XPF'
    assert cfp_franc.decimal_places == 0
    assert cfp_franc.decimal_sign == ','
    assert cfp_franc.grouping_sign == '.'
    assert not cfp_franc.international
    assert cfp_franc.symbol == '₣'
    assert cfp_franc.__hash__() == hash((decimal, 'XPF', '953'))
    assert cfp_franc.__repr__() == (
        'CFPFranc(amount: -100, '
        'currency: "XPF", '
        'symbol: "₣", '
        'code: "953", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cfp_franc.__str__() == '₣-100'


def test_cfp_franc_custom():
    """test_cfp_franc_custom."""
    amount = 1000
    cfp_franc = CFPFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert cfp_franc.amount == decimal
    assert cfp_franc.code == '953'
    assert cfp_franc.currency == 'XPF'
    assert cfp_franc.decimal_places == 5
    assert cfp_franc.decimal_sign == '.'
    assert cfp_franc.grouping_sign == ','
    assert cfp_franc.international
    assert cfp_franc.symbol == '₣'
    assert cfp_franc.__hash__() == hash((decimal, 'XPF', '953'))
    assert cfp_franc.__repr__() == (
        'CFPFranc(amount: 1000, '
        'currency: "XPF", '
        'symbol: "₣", '
        'code: "953", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert cfp_franc.__str__() == 'XPF 1,000.00000'


def test_cfp_franc_changed():
    """test_ccfp_franc_changed."""
    cfp_franc = CFPFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cfp_franc.international = True


def test_cfp_franc_math_add():
    """test_cfp_franc_math_add."""
    cfp_franc_one = CFPFranc(amount=1)
    cfp_franc_two = CFPFranc(amount=2)
    cfp_franc_three = CFPFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency XPF and OTHER.'):
        _ = cfp_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.CFPFranc\'> '
                   'and <class \'str\'>.')):
        _ = cfp_franc_one.__add__('1.00')
    assert (cfp_franc_one + cfp_franc_two) == cfp_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CFPFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CFPFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
