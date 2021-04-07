# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Malagasy Ariary representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MalagasyAriary
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_malagasy_ariary():
    """test_malagasy_ariary."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    malagasy_ariary = MalagasyAriary(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.amount == decimal
    assert malagasy_ariary.code == '969'
    assert malagasy_ariary.currency == 'MGA'
    assert malagasy_ariary.decimal_places == 0
    assert malagasy_ariary.decimal_sign == ','
    assert malagasy_ariary.grouping_sign == '.'
    assert not malagasy_ariary.international
    assert malagasy_ariary.symbol == ''
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: 0.1428571428571428571428571429, '
        'currency: "MGA", '
        'symbol: "", '
        'code: "969", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert malagasy_ariary.__str__() == '0'


def test_malagasy_ariary_negative():
    """test_malagasy_ariary_negative."""
    amount = -100
    malagasy_ariary = MalagasyAriary(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.code == '969'
    assert malagasy_ariary.currency == 'MGA'
    assert malagasy_ariary.decimal_places == 0
    assert malagasy_ariary.decimal_sign == ','
    assert malagasy_ariary.grouping_sign == '.'
    assert not malagasy_ariary.international
    assert malagasy_ariary.symbol == ''
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: -100, '
        'currency: "MGA", '
        'symbol: "", '
        'code: "969", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert malagasy_ariary.__str__() == '-100'


def test_malagasy_ariary_custom():
    """test_malagasy_ariary_custom."""
    amount = 1000
    malagasy_ariary = MalagasyAriary(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert malagasy_ariary.amount == decimal
    assert malagasy_ariary.code == '969'
    assert malagasy_ariary.currency == 'MGA'
    assert malagasy_ariary.decimal_places == 5
    assert malagasy_ariary.decimal_sign == '.'
    assert malagasy_ariary.grouping_sign == ','
    assert malagasy_ariary.international
    assert malagasy_ariary.symbol == ''
    assert malagasy_ariary.__hash__() == hash((decimal, 'MGA', '969'))
    assert malagasy_ariary.__repr__() == (
        'MalagasyAriary(amount: 1000, '
        'currency: "MGA", '
        'symbol: "", '
        'code: "969", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert malagasy_ariary.__str__() == 'MGA 1,000.00000'


def test_malagasy_ariary_changed():
    """test_cmalagasy_ariary_changed."""
    malagasy_ariary = MalagasyAriary(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        malagasy_ariary.international = True


def test_malagasy_ariary_math_add():
    """test_malagasy_ariary_math_add."""
    malagasy_ariary_one = MalagasyAriary(amount=1)
    malagasy_ariary_two = MalagasyAriary(amount=2)
    malagasy_ariary_three = MalagasyAriary(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MGA and OTHER.'):
        _ = malagasy_ariary_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'ariary.MalagasyAriary\'> '
                   'and <class \'str\'>.')):
        _ = malagasy_ariary_one.__add__('1.00')
    assert (malagasy_ariary_one + malagasy_ariary_two) == malagasy_ariary_three


def test_currency_slots():
    """test_currency_slots."""
    euro = MalagasyAriary(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MalagasyAriary\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
