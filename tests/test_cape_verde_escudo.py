# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Cape Verde Escudo representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, CapeVerdeEscudo
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_cape_verde_escudo():
    """test_cape_verde_escudo."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    cape_verde_escudo = CapeVerdeEscudo(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cape_verde_escudo.amount == decimal
    assert cape_verde_escudo.code == '132'
    assert cape_verde_escudo.currency == 'CVE'
    assert cape_verde_escudo.decimal_places == 2
    assert cape_verde_escudo.decimal_sign == ','
    assert cape_verde_escudo.grouping_sign == '.'
    assert not cape_verde_escudo.international
    assert cape_verde_escudo.symbol == '$'
    assert cape_verde_escudo.__hash__() == hash((decimal, 'CVE', '132'))
    assert cape_verde_escudo.__repr__() == (
        'CapeVerdeEscudo(amount: 0.1428571428571428571428571429, '
        'currency: "CVE", '
        'symbol: "$", '
        'code: "132", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cape_verde_escudo.__str__() == '$0,14'


def test_cape_verde_escudo_negative():
    """test_cape_verde_escudo_negative."""
    amount = -100
    cape_verde_escudo = CapeVerdeEscudo(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert cape_verde_escudo.code == '132'
    assert cape_verde_escudo.currency == 'CVE'
    assert cape_verde_escudo.decimal_places == 2
    assert cape_verde_escudo.decimal_sign == ','
    assert cape_verde_escudo.grouping_sign == '.'
    assert not cape_verde_escudo.international
    assert cape_verde_escudo.symbol == '$'
    assert cape_verde_escudo.__hash__() == hash((decimal, 'CVE', '132'))
    assert cape_verde_escudo.__repr__() == (
        'CapeVerdeEscudo(amount: -100, '
        'currency: "CVE", '
        'symbol: "$", '
        'code: "132", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert cape_verde_escudo.__str__() == '$-100,00'


def test_cape_verde_escudo_custom():
    """test_cape_verde_escudo_custom."""
    amount = 1000
    cape_verde_escudo = CapeVerdeEscudo(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert cape_verde_escudo.amount == decimal
    assert cape_verde_escudo.code == '132'
    assert cape_verde_escudo.currency == 'CVE'
    assert cape_verde_escudo.decimal_places == 5
    assert cape_verde_escudo.decimal_sign == '.'
    assert cape_verde_escudo.grouping_sign == ','
    assert cape_verde_escudo.international
    assert cape_verde_escudo.symbol == '$'
    assert cape_verde_escudo.__hash__() == hash((decimal, 'CVE', '132'))
    assert cape_verde_escudo.__repr__() == (
        'CapeVerdeEscudo(amount: 1000, '
        'currency: "CVE", '
        'symbol: "$", '
        'code: "132", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert cape_verde_escudo.__str__() == 'CVE 1,000.00000'


def test_cape_verde_escudo_changed():
    """test_ccape_verde_escudo_changed."""
    cape_verde_escudo = CapeVerdeEscudo(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        cape_verde_escudo.international = True


def test_cape_verde_escudo_math_add():
    """test_cape_verde_escudo_math_add."""
    cape_verde_escudo_one = CapeVerdeEscudo(amount=1)
    cape_verde_escudo_two = CapeVerdeEscudo(amount=2)
    cape_verde_escudo_three = CapeVerdeEscudo(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CVE and OTHER.'):
        _ = cape_verde_escudo_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'cape_verde_escudo.CapeVerdeEscudo\'> '
                   'and <class \'str\'>.')):
        _ = cape_verde_escudo_one.__add__('1.00')
    assert (
        cape_verde_escudo_one +
        cape_verde_escudo_two) == cape_verde_escudo_three


def test_currency_slots():
    """test_currency_slots."""
    euro = CapeVerdeEscudo(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'CapeVerdeEscudo\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
