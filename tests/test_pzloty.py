# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the PZloty currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the PZloty representation."""

from multicurrency import PZloty


class TestPZloty:

    def test_pzloty(self):
        """test_pzloty."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pzloty = PZloty(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pzloty.amount == decimal
        assert pzloty.numeric_code == '985'
        assert pzloty.alpha_code == 'PLN'
        assert pzloty.decimal_places == 2
        assert pzloty.decimal_sign == ','
        assert pzloty.grouping_places == 3
        assert pzloty.grouping_sign == '\u202F'
        assert not pzloty.international
        assert pzloty.symbol == 'zł'
        assert not pzloty.symbol_ahead
        assert pzloty.symbol_separator == '\u00A0'
        assert pzloty.localized_symbol == 'zł'
        assert pzloty.convertion == ''
        assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
        assert pzloty.__repr__() == (
            'PZloty(amount: 0.1428571428571428571428571429, '
            'alpha_code: "PLN", '
            'symbol: "zł", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "zł", '
            'numeric_code: "985", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert pzloty.__str__() == '0,14 zł'


    def test_pzloty_negative(self):
        """test_pzloty_negative."""
        amount = -100
        pzloty = PZloty(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pzloty.numeric_code == '985'
        assert pzloty.alpha_code == 'PLN'
        assert pzloty.decimal_places == 2
        assert pzloty.decimal_sign == ','
        assert pzloty.grouping_places == 3
        assert pzloty.grouping_sign == '\u202F'
        assert not pzloty.international
        assert pzloty.symbol == 'zł'
        assert not pzloty.symbol_ahead
        assert pzloty.symbol_separator == '\u00A0'
        assert pzloty.localized_symbol == 'zł'
        assert pzloty.convertion == ''
        assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
        assert pzloty.__repr__() == (
            'PZloty(amount: -100, '
            'alpha_code: "PLN", '
            'symbol: "zł", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "zł", '
            'numeric_code: "985", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert pzloty.__str__() == '-100,00 zł'


    def test_pzloty_custom(self):
        """test_pzloty_custom."""
        amount = 1000
        pzloty = PZloty(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pzloty.amount == decimal
        assert pzloty.numeric_code == '985'
        assert pzloty.alpha_code == 'PLN'
        assert pzloty.decimal_places == 5
        assert pzloty.decimal_sign == '\u202F'
        assert pzloty.grouping_places == 2
        assert pzloty.grouping_sign == ','
        assert pzloty.international
        assert pzloty.symbol == 'zł'
        assert not pzloty.symbol_ahead
        assert pzloty.symbol_separator == '_'
        assert pzloty.localized_symbol == 'zł'
        assert pzloty.convertion == ''
        assert pzloty.__hash__() == hash((decimal, 'PLN', '985'))
        assert pzloty.__repr__() == (
            'PZloty(amount: 1000, '
            'alpha_code: "PLN", '
            'symbol: "zł", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "zł", '
            'numeric_code: "985", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert pzloty.__str__() == 'PLN 10,00.00000'


    def test_pzloty_changed(self):
        """test_cpzloty_changed."""
        pzloty = PZloty(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pzloty.international = True


    def test_pzloty_math_add(self):
        """test_pzloty_math_add."""
        pzloty_one = PZloty(amount=1)
        pzloty_two = PZloty(amount=2)
        pzloty_three = PZloty(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency PLN and OTHER.'):
            _ = pzloty_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pzloty.PZloty\'> '
                    'and <class \'str\'>.')):
            _ = pzloty_one.__add__('1.00')
        assert (
            pzloty_one +
            pzloty_two) == pzloty_three


    def test_pzloty_slots(self):
        """test_pzloty_slots."""
        pzloty = PZloty(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PZloty\' '
                    'object has no attribute \'new_variable\'')):
            pzloty.new_variable = 'fail'  # pylint: disable=assigning-non-slot
