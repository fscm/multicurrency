# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Iceland Krona representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, IcelandKrona
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_iceland_krona():
    """test_iceland_krona."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    iceland_krona = IcelandKrona(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iceland_krona.amount == decimal
    assert iceland_krona.code == '352'
    assert iceland_krona.currency == 'ISK'
    assert iceland_krona.decimal_places == 0
    assert iceland_krona.decimal_sign == ','
    assert iceland_krona.grouping_sign == '.'
    assert not iceland_krona.international
    assert iceland_krona.symbol == 'Kr'
    assert iceland_krona.__hash__() == hash((decimal, 'ISK', '352'))
    assert iceland_krona.__repr__() == (
        'IcelandKrona(amount: 0.1428571428571428571428571429, '
        'currency: "ISK", '
        'symbol: "Kr", '
        'code: "352", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert iceland_krona.__str__() == 'Kr0'


def test_iceland_krona_negative():
    """test_iceland_krona_negative."""
    amount = -100
    iceland_krona = IcelandKrona(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iceland_krona.code == '352'
    assert iceland_krona.currency == 'ISK'
    assert iceland_krona.decimal_places == 0
    assert iceland_krona.decimal_sign == ','
    assert iceland_krona.grouping_sign == '.'
    assert not iceland_krona.international
    assert iceland_krona.symbol == 'Kr'
    assert iceland_krona.__hash__() == hash((decimal, 'ISK', '352'))
    assert iceland_krona.__repr__() == (
        'IcelandKrona(amount: -100, '
        'currency: "ISK", '
        'symbol: "Kr", '
        'code: "352", '
        'decimal_places: "0", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert iceland_krona.__str__() == 'Kr-100'


def test_iceland_krona_custom():
    """test_iceland_krona_custom."""
    amount = 1000
    iceland_krona = IcelandKrona(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert iceland_krona.amount == decimal
    assert iceland_krona.code == '352'
    assert iceland_krona.currency == 'ISK'
    assert iceland_krona.decimal_places == 5
    assert iceland_krona.decimal_sign == '.'
    assert iceland_krona.grouping_sign == ','
    assert iceland_krona.international
    assert iceland_krona.symbol == 'Kr'
    assert iceland_krona.__hash__() == hash((decimal, 'ISK', '352'))
    assert iceland_krona.__repr__() == (
        'IcelandKrona(amount: 1000, '
        'currency: "ISK", '
        'symbol: "Kr", '
        'code: "352", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert iceland_krona.__str__() == 'ISK 1,000.00000'


def test_iceland_krona_changed():
    """test_ciceland_krona_changed."""
    iceland_krona = IcelandKrona(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iceland_krona.international = True


def test_iceland_krona_math_add():
    """test_iceland_krona_math_add."""
    iceland_krona_one = IcelandKrona(amount=1)
    iceland_krona_two = IcelandKrona(amount=2)
    iceland_krona_three = IcelandKrona(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency ISK and OTHER.'):
        _ = iceland_krona_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'iceland_krona.IcelandKrona\'> '
                   'and <class \'str\'>.')):
        _ = iceland_krona_one.__add__('1.00')
    assert (iceland_krona_one + iceland_krona_two) == iceland_krona_three


def test_currency_slots():
    """test_currency_slots."""
    euro = IcelandKrona(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'IcelandKrona\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
