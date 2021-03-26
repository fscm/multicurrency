# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Somali Shilling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SomaliShilling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_somali_shilling():
    """test_somali_shilling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    somali_shilling = SomaliShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert somali_shilling.amount == decimal
    assert somali_shilling.code == '706'
    assert somali_shilling.currency == 'SOS'
    assert somali_shilling.decimal_places == 2
    assert somali_shilling.decimal_sign == ','
    assert somali_shilling.grouping_sign == '.'
    assert not somali_shilling.international
    assert somali_shilling.symbol == 'Sh'
    assert somali_shilling.__hash__() == hash((decimal, 'SOS', '706'))
    assert somali_shilling.__repr__() == (
        'SomaliShilling(amount: 0.1428571428571428571428571429, '
        'currency: "SOS", '
        'symbol: "Sh", '
        'code: "706", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert somali_shilling.__str__() == 'Sh0,14'


def test_somali_shilling_negative():
    """test_somali_shilling_negative."""
    amount = -100
    somali_shilling = SomaliShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert somali_shilling.code == '706'
    assert somali_shilling.currency == 'SOS'
    assert somali_shilling.decimal_places == 2
    assert somali_shilling.decimal_sign == ','
    assert somali_shilling.grouping_sign == '.'
    assert not somali_shilling.international
    assert somali_shilling.symbol == 'Sh'
    assert somali_shilling.__hash__() == hash((decimal, 'SOS', '706'))
    assert somali_shilling.__repr__() == (
        'SomaliShilling(amount: -100, '
        'currency: "SOS", '
        'symbol: "Sh", '
        'code: "706", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert somali_shilling.__str__() == 'Sh-100,00'


def test_somali_shilling_custom():
    """test_somali_shilling_custom."""
    amount = 1000
    somali_shilling = SomaliShilling(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert somali_shilling.amount == decimal
    assert somali_shilling.code == '706'
    assert somali_shilling.currency == 'SOS'
    assert somali_shilling.decimal_places == 5
    assert somali_shilling.decimal_sign == '.'
    assert somali_shilling.grouping_sign == ','
    assert somali_shilling.international
    assert somali_shilling.symbol == 'Sh'
    assert somali_shilling.__hash__() == hash((decimal, 'SOS', '706'))
    assert somali_shilling.__repr__() == (
        'SomaliShilling(amount: 1000, '
        'currency: "SOS", '
        'symbol: "Sh", '
        'code: "706", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert somali_shilling.__str__() == 'SOS 1,000.00000'


def test_somali_shilling_changed():
    """test_csomali_shilling_changed."""
    somali_shilling = SomaliShilling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        somali_shilling.international = True


def test_somali_shilling_math_add():
    """test_somali_shilling_math_add."""
    somali_shilling_one = SomaliShilling(amount=1)
    somali_shilling_two = SomaliShilling(amount=2)
    somali_shilling_three = SomaliShilling(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency SOS and OTHER.'):
        _ = somali_shilling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'somali_shilling.SomaliShilling\'> '
                   'and <class \'str\'>.')):
        _ = somali_shilling_one.__add__('1.00')
    assert (somali_shilling_one + somali_shilling_two) == somali_shilling_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SomaliShilling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SomaliShilling\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
