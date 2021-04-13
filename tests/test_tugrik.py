# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tugrik representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Tugrik
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_tugrik():
    """test_tugrik."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    tugrik = Tugrik(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tugrik.amount == decimal
    assert tugrik.numeric_code == '496'
    assert tugrik.alpha_code == 'MNT'
    assert tugrik.decimal_places == 2
    assert tugrik.decimal_sign == ','
    assert tugrik.grouping_sign == '.'
    assert not tugrik.international
    assert tugrik.symbol == '₮'
    assert tugrik.__hash__() == hash((decimal, 'MNT', '496'))
    assert tugrik.__repr__() == (
        'Tugrik(amount: 0.1428571428571428571428571429, '
        'alpha_code: "MNT", '
        'symbol: "₮", '
        'numeric_code: "496", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tugrik.__str__() == '₮0,14'


def test_tugrik_negative():
    """test_tugrik_negative."""
    amount = -100
    tugrik = Tugrik(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert tugrik.numeric_code == '496'
    assert tugrik.alpha_code == 'MNT'
    assert tugrik.decimal_places == 2
    assert tugrik.decimal_sign == ','
    assert tugrik.grouping_sign == '.'
    assert not tugrik.international
    assert tugrik.symbol == '₮'
    assert tugrik.__hash__() == hash((decimal, 'MNT', '496'))
    assert tugrik.__repr__() == (
        'Tugrik(amount: -100, '
        'alpha_code: "MNT", '
        'symbol: "₮", '
        'numeric_code: "496", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert tugrik.__str__() == '₮-100,00'


def test_tugrik_custom():
    """test_tugrik_custom."""
    amount = 1000
    tugrik = Tugrik(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert tugrik.amount == decimal
    assert tugrik.numeric_code == '496'
    assert tugrik.alpha_code == 'MNT'
    assert tugrik.decimal_places == 5
    assert tugrik.decimal_sign == '.'
    assert tugrik.grouping_sign == ','
    assert tugrik.international
    assert tugrik.symbol == '₮'
    assert tugrik.__hash__() == hash((decimal, 'MNT', '496'))
    assert tugrik.__repr__() == (
        'Tugrik(amount: 1000, '
        'alpha_code: "MNT", '
        'symbol: "₮", '
        'numeric_code: "496", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert tugrik.__str__() == 'MNT 1,000.00000'


def test_tugrik_changed():
    """test_ctugrik_changed."""
    tugrik = Tugrik(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        tugrik.international = True


def test_tugrik_math_add():
    """test_tugrik_math_add."""
    tugrik_one = Tugrik(amount=1)
    tugrik_two = Tugrik(amount=2)
    tugrik_three = Tugrik(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MNT and OTHER.'):
        _ = tugrik_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'tugrik.Tugrik\'> '
                   'and <class \'str\'>.')):
        _ = tugrik_one.__add__('1.00')
    assert (tugrik_one + tugrik_two) == tugrik_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Tugrik(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Tugrik\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
