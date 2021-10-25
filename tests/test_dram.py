# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dram currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Armenian Dram representation."""

from multicurrency import ArmenianDram


class TestArmenianDram:

    def test_armenian_dram(self):
        """test_armenian_dram."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        armenian_dram = ArmenianDram(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert armenian_dram.amount == decimal
        assert armenian_dram.numeric_code == '051'
        assert armenian_dram.alpha_code == 'AMD'
        assert armenian_dram.decimal_places == 2
        assert armenian_dram.decimal_sign == ','
        assert armenian_dram.grouping_places == 3
        assert armenian_dram.grouping_sign == '\u202F'
        assert not armenian_dram.international
        assert armenian_dram.symbol == 'Դ'
        assert not armenian_dram.symbol_ahead
        assert armenian_dram.symbol_separator == '\u00A0'
        assert armenian_dram.localized_symbol == 'Դ'
        assert armenian_dram.convertion == ''
        assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
        assert armenian_dram.__repr__() == (
            'ArmenianDram(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AMD", '
            'symbol: "Դ", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Դ", '
            'numeric_code: "051", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert armenian_dram.__str__() == '0,14 Դ'


    def test_armenian_dram_negative(self):
        """test_armenian_dram_negative."""
        amount = -100
        armenian_dram = ArmenianDram(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert armenian_dram.numeric_code == '051'
        assert armenian_dram.alpha_code == 'AMD'
        assert armenian_dram.decimal_places == 2
        assert armenian_dram.decimal_sign == ','
        assert armenian_dram.grouping_places == 3
        assert armenian_dram.grouping_sign == '\u202F'
        assert not armenian_dram.international
        assert armenian_dram.symbol == 'Դ'
        assert not armenian_dram.symbol_ahead
        assert armenian_dram.symbol_separator == '\u00A0'
        assert armenian_dram.localized_symbol == 'Դ'
        assert armenian_dram.convertion == ''
        assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
        assert armenian_dram.__repr__() == (
            'ArmenianDram(amount: -100, '
            'alpha_code: "AMD", '
            'symbol: "Դ", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Դ", '
            'numeric_code: "051", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert armenian_dram.__str__() == '-100,00 Դ'


    def test_armenian_dram_custom(self):
        """test_armenian_dram_custom."""
        amount = 1000
        armenian_dram = ArmenianDram(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert armenian_dram.amount == decimal
        assert armenian_dram.numeric_code == '051'
        assert armenian_dram.alpha_code == 'AMD'
        assert armenian_dram.decimal_places == 5
        assert armenian_dram.decimal_sign == '\u202F'
        assert armenian_dram.grouping_places == 2
        assert armenian_dram.grouping_sign == ','
        assert armenian_dram.international
        assert armenian_dram.symbol == 'Դ'
        assert not armenian_dram.symbol_ahead
        assert armenian_dram.symbol_separator == '_'
        assert armenian_dram.localized_symbol == 'Դ'
        assert armenian_dram.convertion == ''
        assert armenian_dram.__hash__() == hash((decimal, 'AMD', '051'))
        assert armenian_dram.__repr__() == (
            'ArmenianDram(amount: 1000, '
            'alpha_code: "AMD", '
            'symbol: "Դ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Դ", '
            'numeric_code: "051", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert armenian_dram.__str__() == 'AMD 10,00.00000'


    def test_armenian_dram_changed(self):
        """test_carmenian_dram_changed."""
        armenian_dram = ArmenianDram(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            armenian_dram.international = True


    def test_armenian_dram_math_add(self):
        """test_armenian_dram_math_add."""
        armenian_dram_one = ArmenianDram(amount=1)
        armenian_dram_two = ArmenianDram(amount=2)
        armenian_dram_three = ArmenianDram(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AMD and OTHER.'):
            _ = armenian_dram_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dram.ArmenianDram\'> '
                    'and <class \'str\'>.')):
            _ = armenian_dram_one.__add__('1.00')
        assert (
            armenian_dram_one +
            armenian_dram_two) == armenian_dram_three


    def test_armenian_dram_slots(self):
        """test_armenian_dram_slots."""
        armenian_dram = ArmenianDram(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ArmenianDram\' '
                    'object has no attribute \'new_variable\'')):
            armenian_dram.new_variable = 'fail'  # pylint: disable=assigning-non-slot
