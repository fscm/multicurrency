# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Philippine Peso representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, PhilippinePeso
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_philippine_peso():
    """test_philippine_peso."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    philippine_peso = PhilippinePeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert philippine_peso.amount == decimal
    assert philippine_peso.numeric_code == '608'
    assert philippine_peso.alpha_code == 'PHP'
    assert philippine_peso.decimal_places == 2
    assert philippine_peso.decimal_sign == '.'
    assert philippine_peso.grouping_sign == ','
    assert not philippine_peso.international
    assert philippine_peso.symbol == '₱'
    assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
    assert philippine_peso.__repr__() == (
        'PhilippinePeso(amount: 0.1428571428571428571428571429, '
        'alpha_code: "PHP", '
        'symbol: "₱", '
        'numeric_code: "608", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert philippine_peso.__str__() == '₱0.14'


def test_philippine_peso_negative():
    """test_philippine_peso_negative."""
    amount = -100
    philippine_peso = PhilippinePeso(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert philippine_peso.numeric_code == '608'
    assert philippine_peso.alpha_code == 'PHP'
    assert philippine_peso.decimal_places == 2
    assert philippine_peso.decimal_sign == '.'
    assert philippine_peso.grouping_sign == ','
    assert not philippine_peso.international
    assert philippine_peso.symbol == '₱'
    assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
    assert philippine_peso.__repr__() == (
        'PhilippinePeso(amount: -100, '
        'alpha_code: "PHP", '
        'symbol: "₱", '
        'numeric_code: "608", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert philippine_peso.__str__() == '₱-100.00'


def test_philippine_peso_custom():
    """test_philippine_peso_custom."""
    amount = 1000
    philippine_peso = PhilippinePeso(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert philippine_peso.amount == decimal
    assert philippine_peso.numeric_code == '608'
    assert philippine_peso.alpha_code == 'PHP'
    assert philippine_peso.decimal_places == 5
    assert philippine_peso.decimal_sign == ','
    assert philippine_peso.grouping_sign == '.'
    assert philippine_peso.international
    assert philippine_peso.symbol == '₱'
    assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
    assert philippine_peso.__repr__() == (
        'PhilippinePeso(amount: 1000, '
        'alpha_code: "PHP", '
        'symbol: "₱", '
        'numeric_code: "608", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert philippine_peso.__str__() == 'PHP 1.000,00000'


def test_philippine_peso_changed():
    """test_cphilippine_peso_changed."""
    philippine_peso = PhilippinePeso(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        philippine_peso.international = True


def test_philippine_peso_math_add():
    """test_philippine_peso_math_add."""
    philippine_peso_one = PhilippinePeso(amount=1)
    philippine_peso_two = PhilippinePeso(amount=2)
    philippine_peso_three = PhilippinePeso(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency PHP and OTHER.'):
        _ = philippine_peso_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'peso.PhilippinePeso\'> '
                   'and <class \'str\'>.')):
        _ = philippine_peso_one.__add__('1.00')
    assert (philippine_peso_one + philippine_peso_two) == philippine_peso_three


def test_currency_slots():
    """test_currency_slots."""
    euro = PhilippinePeso(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'PhilippinePeso\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
