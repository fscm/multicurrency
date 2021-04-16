# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the EuroDE representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, EuroDE
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_eurode():
    """test_eurode."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    eurode = EuroDE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurode.amount == decimal
    assert eurode.numeric_code == '978'
    assert eurode.alpha_code == 'EUR'
    assert eurode.decimal_places == 2
    assert eurode.decimal_sign == ','
    assert eurode.grouping_sign == '.'
    assert not eurode.international
    assert eurode.symbol == '€'
    assert not eurode.symbol_ahead
    assert eurode.symbol_separator == '\u00A0'
    assert eurode.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurode.__repr__() == (
        'EuroDE(amount: 0.1428571428571428571428571429, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert eurode.__str__() == '0,14 €'


def test_eurode_negative():
    """test_eurode_negative."""
    amount = -100
    eurode = EuroDE(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert eurode.numeric_code == '978'
    assert eurode.alpha_code == 'EUR'
    assert eurode.decimal_places == 2
    assert eurode.decimal_sign == ','
    assert eurode.grouping_sign == '.'
    assert not eurode.international
    assert eurode.symbol == '€'
    assert not eurode.symbol_ahead
    assert eurode.symbol_separator == '\u00A0'
    assert eurode.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurode.__repr__() == (
        'EuroDE(amount: -100, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "978", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert eurode.__str__() == '-100,00 €'


def test_eurode_custom():
    """test_eurode_custom."""
    amount = 1000
    eurode = EuroDE(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert eurode.amount == decimal
    assert eurode.numeric_code == '978'
    assert eurode.alpha_code == 'EUR'
    assert eurode.decimal_places == 5
    assert eurode.decimal_sign == '.'
    assert eurode.grouping_sign == ','
    assert eurode.international
    assert eurode.symbol == '€'
    assert not eurode.symbol_ahead
    assert eurode.symbol_separator == '_'
    assert eurode.__hash__() == hash((decimal, 'EUR', '978'))
    assert eurode.__repr__() == (
        'EuroDE(amount: 1000, '
        'alpha_code: "EUR", '
        'symbol: "€", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "978", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert eurode.__str__() == 'EUR 1,000.00000'


def test_eurode_changed():
    """test_ceurode_changed."""
    eurode = EuroDE(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        eurode.international = True


def test_eurode_math_add():
    """test_eurode_math_add."""
    eurode_one = EuroDE(amount=1)
    eurode_two = EuroDE(amount=2)
    eurode_three = EuroDE(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and OTHER.'):
        _ = eurode_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'euro.EuroDE\'> '
                   'and <class \'str\'>.')):
        _ = eurode_one.__add__('1.00')
    assert (
        eurode_one +
        eurode_two) == eurode_three


def test_eurode_slots():
    """test_eurode_slots."""
    eurode = EuroDE(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'EuroDE\' '
                'object has no attribute \'new_variable\'')):
        eurode.new_variable = 'fail'  # pylint: disable=assigning-non-slot
