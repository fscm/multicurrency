# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Florin currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import ArubanFlorin


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Aruban Florin representation."""


class TestArubanFlorin:
    """ArubanFlorin currency tests."""

    def test_aruban_florin(self):
        """test_aruban_florin."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        aruban_florin = ArubanFlorin(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert aruban_florin.amount == decimal
        assert aruban_florin.numeric_code == '533'
        assert aruban_florin.alpha_code == 'AWG'
        assert aruban_florin.decimal_places == 2
        assert aruban_florin.decimal_sign == '.'
        assert aruban_florin.grouping_places == 3
        assert aruban_florin.grouping_sign == ','
        assert not aruban_florin.international
        assert aruban_florin.symbol == 'ƒ'
        assert aruban_florin.symbol_ahead
        assert aruban_florin.symbol_separator == ''
        assert aruban_florin.localized_symbol == 'ƒ'
        assert aruban_florin.convertion == ''
        assert aruban_florin.__hash__() == hash(
            (aruban_florin.__class__, decimal, 'AWG', '533'))
        assert aruban_florin.__repr__() == (
            'ArubanFlorin(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AWG", '
            'symbol: "ƒ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ƒ", '
            'numeric_code: "533", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert aruban_florin.__str__() == 'ƒ0.14'

    def test_aruban_florin_negative(self):
        """test_aruban_florin_negative."""
        amount = -100
        aruban_florin = ArubanFlorin(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert aruban_florin.numeric_code == '533'
        assert aruban_florin.alpha_code == 'AWG'
        assert aruban_florin.decimal_places == 2
        assert aruban_florin.decimal_sign == '.'
        assert aruban_florin.grouping_places == 3
        assert aruban_florin.grouping_sign == ','
        assert not aruban_florin.international
        assert aruban_florin.symbol == 'ƒ'
        assert aruban_florin.symbol_ahead
        assert aruban_florin.symbol_separator == ''
        assert aruban_florin.localized_symbol == 'ƒ'
        assert aruban_florin.convertion == ''
        assert aruban_florin.__hash__() == hash(
            (aruban_florin.__class__, decimal, 'AWG', '533'))
        assert aruban_florin.__repr__() == (
            'ArubanFlorin(amount: -100, '
            'alpha_code: "AWG", '
            'symbol: "ƒ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ƒ", '
            'numeric_code: "533", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert aruban_florin.__str__() == 'ƒ-100.00'

    def test_aruban_florin_custom(self):
        """test_aruban_florin_custom."""
        amount = 1000
        aruban_florin = ArubanFlorin(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert aruban_florin.amount == decimal
        assert aruban_florin.numeric_code == '533'
        assert aruban_florin.alpha_code == 'AWG'
        assert aruban_florin.decimal_places == 5
        assert aruban_florin.decimal_sign == ','
        assert aruban_florin.grouping_places == 2
        assert aruban_florin.grouping_sign == '.'
        assert aruban_florin.international
        assert aruban_florin.symbol == 'ƒ'
        assert not aruban_florin.symbol_ahead
        assert aruban_florin.symbol_separator == '_'
        assert aruban_florin.localized_symbol == 'ƒ'
        assert aruban_florin.convertion == ''
        assert aruban_florin.__hash__() == hash(
            (aruban_florin.__class__, decimal, 'AWG', '533'))
        assert aruban_florin.__repr__() == (
            'ArubanFlorin(amount: 1000, '
            'alpha_code: "AWG", '
            'symbol: "ƒ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ƒ", '
            'numeric_code: "533", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert aruban_florin.__str__() == 'AWG 10,00.00000'

    def test_aruban_florin_changed(self):
        """test_caruban_florin_changed."""
        aruban_florin = ArubanFlorin(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            aruban_florin.international = True

    def test_aruban_florin_math_add(self):
        """test_aruban_florin_math_add."""
        aruban_florin_one = ArubanFlorin(amount=1)
        aruban_florin_two = ArubanFlorin(amount=2)
        aruban_florin_three = ArubanFlorin(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AWG and OTHER.'):
            _ = aruban_florin_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'florin.ArubanFlorin\'> '
                    'and <class \'str\'>.')):
            _ = aruban_florin_one.__add__('1.00')
        assert (
            aruban_florin_one +
            aruban_florin_two) == aruban_florin_three

    def test_aruban_florin_slots(self):
        """test_aruban_florin_slots."""
        aruban_florin = ArubanFlorin(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ArubanFlorin\' '
                    'object has no attribute \'new_variable\'')):
            aruban_florin.new_variable = 'fail'  # pylint: disable=assigning-non-slot
