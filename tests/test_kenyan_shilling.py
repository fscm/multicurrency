# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kenyan Shilling representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, KenyanShilling
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_kenyan_shilling():
    """test_kenyan_shilling."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    kenyan_shilling = KenyanShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.amount == decimal
    assert kenyan_shilling.code == '404'
    assert kenyan_shilling.currency == 'KES'
    assert kenyan_shilling.decimal_places == 2
    assert kenyan_shilling.decimal_sign == '.'
    assert kenyan_shilling.grouping_sign == ','
    assert not kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Sh'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: 0.1428571428571428571428571429, '
        'currency: "KES", '
        'symbol: "Sh", '
        'code: "404", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kenyan_shilling.__str__() == 'Sh0.14'


def test_kenyan_shilling_negative():
    """test_kenyan_shilling_negative."""
    amount = -100
    kenyan_shilling = KenyanShilling(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.code == '404'
    assert kenyan_shilling.currency == 'KES'
    assert kenyan_shilling.decimal_places == 2
    assert kenyan_shilling.decimal_sign == '.'
    assert kenyan_shilling.grouping_sign == ','
    assert not kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Sh'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: -100, '
        'currency: "KES", '
        'symbol: "Sh", '
        'code: "404", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert kenyan_shilling.__str__() == 'Sh-100.00'


def test_kenyan_shilling_custom():
    """test_kenyan_shilling_custom."""
    amount = 1000
    kenyan_shilling = KenyanShilling(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert kenyan_shilling.amount == decimal
    assert kenyan_shilling.code == '404'
    assert kenyan_shilling.currency == 'KES'
    assert kenyan_shilling.decimal_places == 5
    assert kenyan_shilling.decimal_sign == ','
    assert kenyan_shilling.grouping_sign == '.'
    assert kenyan_shilling.international
    assert kenyan_shilling.symbol == 'Sh'
    assert kenyan_shilling.__hash__() == hash((decimal, 'KES', '404'))
    assert kenyan_shilling.__repr__() == (
        'KenyanShilling(amount: 1000, '
        'currency: "KES", '
        'symbol: "Sh", '
        'code: "404", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert kenyan_shilling.__str__() == 'KES 1.000,00000'


def test_kenyan_shilling_changed():
    """test_ckenyan_shilling_changed."""
    kenyan_shilling = KenyanShilling(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        kenyan_shilling.international = True


def test_kenyan_shilling_math_add():
    """test_kenyan_shilling_math_add."""
    kenyan_shilling_one = KenyanShilling(amount=1)
    kenyan_shilling_two = KenyanShilling(amount=2)
    kenyan_shilling_three = KenyanShilling(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency KES and OTHER.'):
        _ = kenyan_shilling_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'kenyan_shilling.KenyanShilling\'> '
                   'and <class \'str\'>.')):
        _ = kenyan_shilling_one.__add__('1.00')
    assert (kenyan_shilling_one + kenyan_shilling_two) == kenyan_shilling_three


def test_currency_slots():
    """test_currency_slots."""
    euro = KenyanShilling(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'KenyanShilling\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
