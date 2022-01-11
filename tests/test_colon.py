# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Colon currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import CostaRicanColon


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Costa Rican Colon representation."""


class TestCostaRicanColon:
    """CostaRicanColon currency tests."""

    def test_costa_rican_colon(self):
        """test_costa_rican_colon."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        costa_rican_colon = CostaRicanColon(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert costa_rican_colon.amount == decimal
        assert costa_rican_colon.numeric_code == '188'
        assert costa_rican_colon.alpha_code == 'CRC'
        assert costa_rican_colon.decimal_places == 2
        assert costa_rican_colon.decimal_sign == ','
        assert costa_rican_colon.grouping_places == 3
        assert costa_rican_colon.grouping_sign == '\u202F'
        assert not costa_rican_colon.international
        assert costa_rican_colon.symbol == '₡'
        assert costa_rican_colon.symbol_ahead
        assert costa_rican_colon.symbol_separator == ''
        assert costa_rican_colon.localized_symbol == '₡'
        assert costa_rican_colon.convertion == ''
        assert costa_rican_colon.__hash__() == hash(
            (costa_rican_colon.__class__, decimal, 'CRC', '188'))
        assert costa_rican_colon.__repr__() == (
            'CostaRicanColon(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CRC", '
            'symbol: "₡", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₡", '
            'numeric_code: "188", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert costa_rican_colon.__str__() == '₡0,14'

    def test_costa_rican_colon_negative(self):
        """test_costa_rican_colon_negative."""
        amount = -100
        costa_rican_colon = CostaRicanColon(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert costa_rican_colon.numeric_code == '188'
        assert costa_rican_colon.alpha_code == 'CRC'
        assert costa_rican_colon.decimal_places == 2
        assert costa_rican_colon.decimal_sign == ','
        assert costa_rican_colon.grouping_places == 3
        assert costa_rican_colon.grouping_sign == '\u202F'
        assert not costa_rican_colon.international
        assert costa_rican_colon.symbol == '₡'
        assert costa_rican_colon.symbol_ahead
        assert costa_rican_colon.symbol_separator == ''
        assert costa_rican_colon.localized_symbol == '₡'
        assert costa_rican_colon.convertion == ''
        assert costa_rican_colon.__hash__() == hash(
            (costa_rican_colon.__class__, decimal, 'CRC', '188'))
        assert costa_rican_colon.__repr__() == (
            'CostaRicanColon(amount: -100, '
            'alpha_code: "CRC", '
            'symbol: "₡", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₡", '
            'numeric_code: "188", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert costa_rican_colon.__str__() == '₡-100,00'

    def test_costa_rican_colon_custom(self):
        """test_costa_rican_colon_custom."""
        amount = 1000
        costa_rican_colon = CostaRicanColon(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert costa_rican_colon.amount == decimal
        assert costa_rican_colon.numeric_code == '188'
        assert costa_rican_colon.alpha_code == 'CRC'
        assert costa_rican_colon.decimal_places == 5
        assert costa_rican_colon.decimal_sign == '\u202F'
        assert costa_rican_colon.grouping_places == 2
        assert costa_rican_colon.grouping_sign == ','
        assert costa_rican_colon.international
        assert costa_rican_colon.symbol == '₡'
        assert not costa_rican_colon.symbol_ahead
        assert costa_rican_colon.symbol_separator == '_'
        assert costa_rican_colon.localized_symbol == '₡'
        assert costa_rican_colon.convertion == ''
        assert costa_rican_colon.__hash__() == hash(
            (costa_rican_colon.__class__, decimal, 'CRC', '188'))
        assert costa_rican_colon.__repr__() == (
            'CostaRicanColon(amount: 1000, '
            'alpha_code: "CRC", '
            'symbol: "₡", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₡", '
            'numeric_code: "188", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert costa_rican_colon.__str__() == 'CRC 10,00.00000'

    def test_costa_rican_colon_changed(self):
        """test_ccosta_rican_colon_changed."""
        costa_rican_colon = CostaRicanColon(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            costa_rican_colon.international = True

    def test_costa_rican_colon_math_add(self):
        """test_costa_rican_colon_math_add."""
        costa_rican_colon_one = CostaRicanColon(amount=1)
        costa_rican_colon_two = CostaRicanColon(amount=2)
        costa_rican_colon_three = CostaRicanColon(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CRC and OTHER.'):
            _ = costa_rican_colon_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'colon.CostaRicanColon\'> '
                    'and <class \'str\'>.')):
            _ = costa_rican_colon_one.__add__('1.00')
        assert (
            costa_rican_colon_one +
            costa_rican_colon_two) == costa_rican_colon_three

    def test_costa_rican_colon_slots(self):
        """test_costa_rican_colon_slots."""
        costa_rican_colon = CostaRicanColon(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CostaRicanColon\' '
                    'object has no attribute \'new_variable\'')):
            costa_rican_colon.new_variable = 'fail'  # pylint: disable=assigning-non-slot
