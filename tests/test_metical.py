# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Metical currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Metical representation."""

from multicurrency import Metical


class TestMetical:
    """Metical currency tests."""

    def test_metical(self):
        """test_metical."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        metical = Metical(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert metical.amount == decimal
        assert metical.numeric_code == '943'
        assert metical.alpha_code == 'MZN'
        assert metical.decimal_places == 0
        assert metical.decimal_sign == ','
        assert metical.grouping_places == 3
        assert metical.grouping_sign == '.'
        assert not metical.international
        assert metical.symbol == 'MTn'
        assert not metical.symbol_ahead
        assert metical.symbol_separator == '\u00A0'
        assert metical.localized_symbol == 'MTn'
        assert metical.convertion == ''
        assert metical.__hash__() == hash(
            (metical.__class__, decimal, 'MZN', '943'))
        assert metical.__repr__() == (
            'Metical(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MZN", '
            'symbol: "MTn", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MTn", '
            'numeric_code: "943", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert metical.__str__() == '0 MTn'

    def test_metical_negative(self):
        """test_metical_negative."""
        amount = -100
        metical = Metical(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert metical.numeric_code == '943'
        assert metical.alpha_code == 'MZN'
        assert metical.decimal_places == 0
        assert metical.decimal_sign == ','
        assert metical.grouping_places == 3
        assert metical.grouping_sign == '.'
        assert not metical.international
        assert metical.symbol == 'MTn'
        assert not metical.symbol_ahead
        assert metical.symbol_separator == '\u00A0'
        assert metical.localized_symbol == 'MTn'
        assert metical.convertion == ''
        assert metical.__hash__() == hash(
            (metical.__class__, decimal, 'MZN', '943'))
        assert metical.__repr__() == (
            'Metical(amount: -100, '
            'alpha_code: "MZN", '
            'symbol: "MTn", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MTn", '
            'numeric_code: "943", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert metical.__str__() == '-100 MTn'

    def test_metical_custom(self):
        """test_metical_custom."""
        amount = 1000
        metical = Metical(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert metical.amount == decimal
        assert metical.numeric_code == '943'
        assert metical.alpha_code == 'MZN'
        assert metical.decimal_places == 5
        assert metical.decimal_sign == '.'
        assert metical.grouping_places == 2
        assert metical.grouping_sign == ','
        assert metical.international
        assert metical.symbol == 'MTn'
        assert not metical.symbol_ahead
        assert metical.symbol_separator == '_'
        assert metical.localized_symbol == 'MTn'
        assert metical.convertion == ''
        assert metical.__hash__() == hash(
            (metical.__class__, decimal, 'MZN', '943'))
        assert metical.__repr__() == (
            'Metical(amount: 1000, '
            'alpha_code: "MZN", '
            'symbol: "MTn", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MTn", '
            'numeric_code: "943", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert metical.__str__() == 'MZN 10,00.00000'

    def test_metical_changed(self):
        """test_cmetical_changed."""
        metical = Metical(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            metical.international = True

    def test_metical_math_add(self):
        """test_metical_math_add."""
        metical_one = Metical(amount=1)
        metical_two = Metical(amount=2)
        metical_three = Metical(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MZN and OTHER.'):
            _ = metical_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'metical.Metical\'> '
                    'and <class \'str\'>.')):
            _ = metical_one.__add__('1.00')
        assert (
            metical_one +
            metical_two) == metical_three

    def test_metical_slots(self):
        """test_metical_slots."""
        metical = Metical(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Metical\' '
                    'object has no attribute \'new_variable\'')):
            metical.new_variable = 'fail'  # pylint: disable=assigning-non-slot
