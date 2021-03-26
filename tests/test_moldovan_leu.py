# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Moldovan Leu representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, MoldovanLeu
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_moldovan_leu():
    """test_moldovan_leu."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    moldovan_leu = MoldovanLeu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert moldovan_leu.amount == decimal
    assert moldovan_leu.code == '498'
    assert moldovan_leu.currency == 'MDL'
    assert moldovan_leu.decimal_places == 2
    assert moldovan_leu.decimal_sign == ','
    assert moldovan_leu.grouping_sign == '.'
    assert not moldovan_leu.international
    assert moldovan_leu.symbol == 'L'
    assert moldovan_leu.__hash__() == hash((decimal, 'MDL', '498'))
    assert moldovan_leu.__repr__() == (
        'MoldovanLeu(amount: 0.1428571428571428571428571429, '
        'currency: "MDL", '
        'symbol: "L", '
        'code: "498", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert moldovan_leu.__str__() == 'L0,14'


def test_moldovan_leu_negative():
    """test_moldovan_leu_negative."""
    amount = -100
    moldovan_leu = MoldovanLeu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert moldovan_leu.code == '498'
    assert moldovan_leu.currency == 'MDL'
    assert moldovan_leu.decimal_places == 2
    assert moldovan_leu.decimal_sign == ','
    assert moldovan_leu.grouping_sign == '.'
    assert not moldovan_leu.international
    assert moldovan_leu.symbol == 'L'
    assert moldovan_leu.__hash__() == hash((decimal, 'MDL', '498'))
    assert moldovan_leu.__repr__() == (
        'MoldovanLeu(amount: -100, '
        'currency: "MDL", '
        'symbol: "L", '
        'code: "498", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert moldovan_leu.__str__() == 'L-100,00'


def test_moldovan_leu_custom():
    """test_moldovan_leu_custom."""
    amount = 1000
    moldovan_leu = MoldovanLeu(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert moldovan_leu.amount == decimal
    assert moldovan_leu.code == '498'
    assert moldovan_leu.currency == 'MDL'
    assert moldovan_leu.decimal_places == 5
    assert moldovan_leu.decimal_sign == '.'
    assert moldovan_leu.grouping_sign == ','
    assert moldovan_leu.international
    assert moldovan_leu.symbol == 'L'
    assert moldovan_leu.__hash__() == hash((decimal, 'MDL', '498'))
    assert moldovan_leu.__repr__() == (
        'MoldovanLeu(amount: 1000, '
        'currency: "MDL", '
        'symbol: "L", '
        'code: "498", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert moldovan_leu.__str__() == 'MDL 1,000.00000'


def test_moldovan_leu_changed():
    """test_cmoldovan_leu_changed."""
    moldovan_leu = MoldovanLeu(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        moldovan_leu.international = True


def test_moldovan_leu_math_add():
    """test_moldovan_leu_math_add."""
    moldovan_leu_one = MoldovanLeu(amount=1)
    moldovan_leu_two = MoldovanLeu(amount=2)
    moldovan_leu_three = MoldovanLeu(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency MDL and OTHER.'):
        _ = moldovan_leu_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'moldovan_leu.MoldovanLeu\'> '
                   'and <class \'str\'>.')):
        _ = moldovan_leu_one.__add__('1.00')
    assert (moldovan_leu_one + moldovan_leu_two) == moldovan_leu_three


def test_currency_slots():
    """test_currency_slots."""
    euro = MoldovanLeu(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'MoldovanLeu\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
