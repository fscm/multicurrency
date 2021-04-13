# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leu representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Leu
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_leu():
    """test_leu."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    leu = Leu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert leu.amount == decimal
    assert leu.numeric_code == '946'
    assert leu.alpha_code == 'RON'
    assert leu.decimal_places == 2
    assert leu.decimal_sign == ','
    assert leu.grouping_sign == '.'
    assert not leu.international
    assert leu.symbol == 'L'
    assert leu.__hash__() == hash((decimal, 'RON', '946'))
    assert leu.__repr__() == (
        'Leu(amount: 0.1428571428571428571428571429, '
        'alpha_code: "RON", '
        'symbol: "L", '
        'numeric_code: "946", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert leu.__str__() == 'L0,14'


def test_leu_negative():
    """test_leu_negative."""
    amount = -100
    leu = Leu(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert leu.numeric_code == '946'
    assert leu.alpha_code == 'RON'
    assert leu.decimal_places == 2
    assert leu.decimal_sign == ','
    assert leu.grouping_sign == '.'
    assert not leu.international
    assert leu.symbol == 'L'
    assert leu.__hash__() == hash((decimal, 'RON', '946'))
    assert leu.__repr__() == (
        'Leu(amount: -100, '
        'alpha_code: "RON", '
        'symbol: "L", '
        'numeric_code: "946", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert leu.__str__() == 'L-100,00'


def test_leu_custom():
    """test_leu_custom."""
    amount = 1000
    leu = Leu(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert leu.amount == decimal
    assert leu.numeric_code == '946'
    assert leu.alpha_code == 'RON'
    assert leu.decimal_places == 5
    assert leu.decimal_sign == '.'
    assert leu.grouping_sign == ','
    assert leu.international
    assert leu.symbol == 'L'
    assert leu.__hash__() == hash((decimal, 'RON', '946'))
    assert leu.__repr__() == (
        'Leu(amount: 1000, '
        'alpha_code: "RON", '
        'symbol: "L", '
        'numeric_code: "946", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert leu.__str__() == 'RON 1,000.00000'


def test_leu_changed():
    """test_cleu_changed."""
    leu = Leu(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        leu.international = True


def test_leu_math_add():
    """test_leu_math_add."""
    leu_one = Leu(amount=1)
    leu_two = Leu(amount=2)
    leu_three = Leu(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency RON and OTHER.'):
        _ = leu_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'leu.Leu\'> '
                   'and <class \'str\'>.')):
        _ = leu_one.__add__('1.00')
    assert (leu_one + leu_two) == leu_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Leu(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Leu\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
