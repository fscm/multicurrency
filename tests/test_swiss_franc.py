# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Swiss Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SwissFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_swiss_franc():
    """test_swiss_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    swiss_franc = SwissFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.amount == decimal
    assert swiss_franc.code == '756'
    assert swiss_franc.currency == 'CHF'
    assert swiss_franc.decimal_places == 2
    assert swiss_franc.decimal_sign == '.'
    assert swiss_franc.grouping_sign == '\''
    assert not swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: 0.1428571428571428571428571429, '
        'currency: "CHF", '
        'symbol: "₣", '
        'code: "756", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\'", '
        'international: False)')
    assert swiss_franc.__str__() == '₣0.14'


def test_swiss_franc_negative():
    """test_swiss_franc_negative."""
    amount = -100
    swiss_franc = SwissFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.code == '756'
    assert swiss_franc.currency == 'CHF'
    assert swiss_franc.decimal_places == 2
    assert swiss_franc.decimal_sign == '.'
    assert swiss_franc.grouping_sign == '\''
    assert not swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: -100, '
        'currency: "CHF", '
        'symbol: "₣", '
        'code: "756", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: "\'", '
        'international: False)')
    assert swiss_franc.__str__() == '₣-100.00'


def test_swiss_franc_custom():
    """test_swiss_franc_custom."""
    amount = 1000
    swiss_franc = SwissFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\'',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.amount == decimal
    assert swiss_franc.code == '756'
    assert swiss_franc.currency == 'CHF'
    assert swiss_franc.decimal_places == 5
    assert swiss_franc.decimal_sign == '\''
    assert swiss_franc.grouping_sign == '.'
    assert swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: 1000, '
        'currency: "CHF", '
        'symbol: "₣", '
        'code: "756", '
        'decimal_places: "5", '
        'decimal_sign: "\'", '
        'grouping_sign: ".", '
        'international: True)')
    assert swiss_franc.__str__() == 'CHF 1.000\'00000'


def test_swiss_franc_changed():
    """test_cswiss_franc_changed."""
    swiss_franc = SwissFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.international = True


def test_swiss_franc_math_add():
    """test_swiss_franc_math_add."""
    swiss_franc_one = SwissFranc(amount=1)
    swiss_franc_two = SwissFranc(amount=2)
    swiss_franc_three = SwissFranc(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CHF and OTHER.'):
        _ = swiss_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'swiss_franc.SwissFranc\'> '
                   'and <class \'str\'>.')):
        _ = swiss_franc_one.__add__('1.00')
    assert (swiss_franc_one + swiss_franc_two) == swiss_franc_three


def test_currency_slots():
    """test_currency_slots."""
    euro = SwissFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SwissFranc\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
