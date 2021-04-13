# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Manat representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, Manat
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_manat():
    """test_manat."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    manat = Manat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert manat.amount == decimal
    assert manat.numeric_code == '934'
    assert manat.alpha_code == 'TMT'
    assert manat.decimal_places == 2
    assert manat.decimal_sign == ','
    assert manat.grouping_sign == '.'
    assert not manat.international
    assert manat.symbol == 'm'
    assert manat.__hash__() == hash((decimal, 'TMT', '934'))
    assert manat.__repr__() == (
        'Manat(amount: 0.1428571428571428571428571429, '
        'alpha_code: "TMT", '
        'symbol: "m", '
        'numeric_code: "934", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert manat.__str__() == 'm0,14'


def test_manat_negative():
    """test_manat_negative."""
    amount = -100
    manat = Manat(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert manat.numeric_code == '934'
    assert manat.alpha_code == 'TMT'
    assert manat.decimal_places == 2
    assert manat.decimal_sign == ','
    assert manat.grouping_sign == '.'
    assert not manat.international
    assert manat.symbol == 'm'
    assert manat.__hash__() == hash((decimal, 'TMT', '934'))
    assert manat.__repr__() == (
        'Manat(amount: -100, '
        'alpha_code: "TMT", '
        'symbol: "m", '
        'numeric_code: "934", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert manat.__str__() == 'm-100,00'


def test_manat_custom():
    """test_manat_custom."""
    amount = 1000
    manat = Manat(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert manat.amount == decimal
    assert manat.numeric_code == '934'
    assert manat.alpha_code == 'TMT'
    assert manat.decimal_places == 5
    assert manat.decimal_sign == '.'
    assert manat.grouping_sign == ','
    assert manat.international
    assert manat.symbol == 'm'
    assert manat.__hash__() == hash((decimal, 'TMT', '934'))
    assert manat.__repr__() == (
        'Manat(amount: 1000, '
        'alpha_code: "TMT", '
        'symbol: "m", '
        'numeric_code: "934", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert manat.__str__() == 'TMT 1,000.00000'


def test_manat_changed():
    """test_cmanat_changed."""
    manat = Manat(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        manat.international = True


def test_manat_math_add():
    """test_manat_math_add."""
    manat_one = Manat(amount=1)
    manat_two = Manat(amount=2)
    manat_three = Manat(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency TMT and OTHER.'):
        _ = manat_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'manat.Manat\'> '
                   'and <class \'str\'>.')):
        _ = manat_one.__add__('1.00')
    assert (manat_one + manat_two) == manat_three


def test_currency_slots():
    """test_currency_slots."""
    euro = Manat(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Manat\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
