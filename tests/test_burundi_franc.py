# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Burundi Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BurundiFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_burundi_franc():
    """test_burundi_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    burundi_franc = BurundiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.amount == decimal
    assert burundi_franc.code == '108'
    assert burundi_franc.currency == 'BIF'
    assert burundi_franc.decimal_places == 0
    assert burundi_franc.decimal_sign == ','
    assert burundi_franc.grouping_sign == '.'
    assert not burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: 0.1428571428571428571428571429, '
        'currency: "BIF", '
        'symbol: "₣", '
        'code: "108", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert burundi_franc.__str__() == '₣0'


def test_burundi_franc_negative():
    """test_burundi_franc_negative."""
    amount = -100
    burundi_franc = BurundiFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.code == '108'
    assert burundi_franc.currency == 'BIF'
    assert burundi_franc.decimal_places == 0
    assert burundi_franc.decimal_sign == ','
    assert burundi_franc.grouping_sign == '.'
    assert not burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: -100, '
        'currency: "BIF", '
        'symbol: "₣", '
        'code: "108", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert burundi_franc.__str__() == '₣-100'


def test_burundi_franc_custom():
    """test_burundi_franc_custom."""
    amount = 1000
    burundi_franc = BurundiFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert burundi_franc.amount == decimal
    assert burundi_franc.code == '108'
    assert burundi_franc.currency == 'BIF'
    assert burundi_franc.decimal_places == 5
    assert burundi_franc.decimal_sign == '.'
    assert burundi_franc.grouping_sign == ','
    assert burundi_franc.international
    assert burundi_franc.symbol == '₣'
    assert burundi_franc.__hash__() == hash((decimal, 'BIF', '108'))
    assert burundi_franc.__repr__() == (
        'BurundiFranc(amount: 1000, '
        'currency: "BIF", '
        'symbol: "₣", '
        'code: "108", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert burundi_franc.__str__() == 'BIF 1,000.00000'


def test_burundi_franc_changed():
    """test_cburundi_franc_changed."""
    burundi_franc = BurundiFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        burundi_franc.international = True


def test_burundi_franc_math_add():
    """test_burundi_franc_math_add."""
    burundi_franc_one = BurundiFranc(amount=1)
    burundi_franc_two = BurundiFranc(amount=2)
    burundi_franc_three = BurundiFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency BIF and OTHER.'):
        _ = burundi_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.BurundiFranc\'> '
                   'and <class \'str\'>.')):
        _ = burundi_franc_one.__add__('1.00')
    assert (burundi_franc_one + burundi_franc_two) == burundi_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = BurundiFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BurundiFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
