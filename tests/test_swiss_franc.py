# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Swiss Franc representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, SwissFranc
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_swiss_franc():
    """test_swiss_franc."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    swiss_franc = SwissFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.amount == decimal
    assert swiss_franc.numeric_code == '756'
    assert swiss_franc.alpha_code == 'CHF'
    assert swiss_franc.decimal_places == 2
    assert swiss_franc.decimal_sign == '.'
    assert swiss_franc.grouping_places == 3
    assert swiss_franc.grouping_sign == '\''
    assert not swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert swiss_franc.symbol_ahead
    assert swiss_franc.symbol_separator == '\u00A0'
    assert swiss_franc.convertion == ''
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: 0.1428571428571428571428571429, '
        'alpha_code: "CHF", '
        'symbol: "₣", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "756", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: "\'", '
        'convertion: "", '
        'international: False)')
    assert swiss_franc.__str__() == '₣ 0.14'


def test_swiss_franc_negative():
    """test_swiss_franc_negative."""
    amount = -100
    swiss_franc = SwissFranc(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.numeric_code == '756'
    assert swiss_franc.alpha_code == 'CHF'
    assert swiss_franc.decimal_places == 2
    assert swiss_franc.decimal_sign == '.'
    assert swiss_franc.grouping_places == 3
    assert swiss_franc.grouping_sign == '\''
    assert not swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert swiss_franc.symbol_ahead
    assert swiss_franc.symbol_separator == '\u00A0'
    assert swiss_franc.convertion == ''
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: -100, '
        'alpha_code: "CHF", '
        'symbol: "₣", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "756", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_places: "3", '
        'grouping_sign: "\'", '
        'convertion: "", '
        'international: False)')
    assert swiss_franc.__str__() == '₣ -100.00'


def test_swiss_franc_custom():
    """test_swiss_franc_custom."""
    amount = 1000
    swiss_franc = SwissFranc(
        amount=amount,
        decimal_places=5,
        decimal_sign='\'',
        grouping_places=2,
        grouping_sign='.',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert swiss_franc.amount == decimal
    assert swiss_franc.numeric_code == '756'
    assert swiss_franc.alpha_code == 'CHF'
    assert swiss_franc.decimal_places == 5
    assert swiss_franc.decimal_sign == '\''
    assert swiss_franc.grouping_places == 2
    assert swiss_franc.grouping_sign == '.'
    assert swiss_franc.international
    assert swiss_franc.symbol == '₣'
    assert not swiss_franc.symbol_ahead
    assert swiss_franc.symbol_separator == '_'
    assert swiss_franc.convertion == ''
    assert swiss_franc.__hash__() == hash((decimal, 'CHF', '756'))
    assert swiss_franc.__repr__() == (
        'SwissFranc(amount: 1000, '
        'alpha_code: "CHF", '
        'symbol: "₣", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "756", '
        'decimal_places: "5", '
        'decimal_sign: "\'", '
        'grouping_places: "2", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: True)')
    assert swiss_franc.__str__() == 'CHF 10,00.00000'


def test_swiss_franc_changed():
    """test_cswiss_franc_changed."""
    swiss_franc = SwissFranc(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        swiss_franc.international = True


def test_swiss_franc_math_add():
    """test_swiss_franc_math_add."""
    swiss_franc_one = SwissFranc(amount=1)
    swiss_franc_two = SwissFranc(amount=2)
    swiss_franc_three = SwissFranc(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency CHF and OTHER.'):
        _ = swiss_franc_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'franc.SwissFranc\'> '
                   'and <class \'str\'>.')):
        _ = swiss_franc_one.__add__('1.00')
    assert (
        swiss_franc_one +
        swiss_franc_two) == swiss_franc_three


def test_swiss_franc_slots():
    """test_swiss_franc_slots."""
    swiss_franc = SwissFranc(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'SwissFranc\' '
                'object has no attribute \'new_variable\'')):
        swiss_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot
