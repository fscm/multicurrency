# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nakfa representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Nakfa
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_nakfa():
    """test_nakfa."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    nakfa = Nakfa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.amount == decimal
    assert nakfa.code == '232'
    assert nakfa.currency == 'ERN'
    assert nakfa.decimal_places == 2
    assert nakfa.decimal_sign == ','
    assert nakfa.grouping_sign == '.'
    assert not nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: 0.1428571428571428571428571429, '
        'currency: "ERN", '
        'symbol: "Nfk", '
        'code: "232", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert nakfa.__str__() == 'Nfk0,14'


def test_nakfa_negative():
    """test_nakfa_negative."""
    amount = -100
    nakfa = Nakfa(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.code == '232'
    assert nakfa.currency == 'ERN'
    assert nakfa.decimal_places == 2
    assert nakfa.decimal_sign == ','
    assert nakfa.grouping_sign == '.'
    assert not nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: -100, '
        'currency: "ERN", '
        'symbol: "Nfk", '
        'code: "232", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert nakfa.__str__() == 'Nfk-100,00'


def test_nakfa_custom():
    """test_nakfa_custom."""
    amount = 1000
    nakfa = Nakfa(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert nakfa.amount == decimal
    assert nakfa.code == '232'
    assert nakfa.currency == 'ERN'
    assert nakfa.decimal_places == 5
    assert nakfa.decimal_sign == '.'
    assert nakfa.grouping_sign == ','
    assert nakfa.international
    assert nakfa.symbol == 'Nfk'
    assert nakfa.__hash__() == hash((decimal, 'ERN', '232'))
    assert nakfa.__repr__() == (
        'Nakfa(amount: 1000, '
        'currency: "ERN", '
        'symbol: "Nfk", '
        'code: "232", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert nakfa.__str__() == 'ERN 1,000.00000'


def test_nakfa_changed():
    """test_cnakfa_changed."""
    nakfa = Nakfa(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        nakfa.international = True


def test_nakfa_math_add():
    """test_nakfa_math_add."""
    nakfa_one = Nakfa(amount=1)
    nakfa_two = Nakfa(amount=2)
    nakfa_three = Nakfa(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ERN and OTHER.'):
        _ = nakfa_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'nakfa.Nakfa\'> '
                   'and <class \'str\'>.')):
        _ = nakfa_one.__add__('1.00')
    assert (nakfa_one + nakfa_two) == nakfa_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Nakfa(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Nakfa\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
