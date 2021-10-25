# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Hryvnia currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Hryvnia representation."""

from multicurrency import Hryvnia


class TestHryvnia:

    def test_hryvnia(self):
        """test_hryvnia."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        hryvnia = Hryvnia(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert hryvnia.amount == decimal
        assert hryvnia.numeric_code == '980'
        assert hryvnia.alpha_code == 'UAH'
        assert hryvnia.decimal_places == 2
        assert hryvnia.decimal_sign == ','
        assert hryvnia.grouping_places == 3
        assert hryvnia.grouping_sign == '\u202F'
        assert not hryvnia.international
        assert hryvnia.symbol == '₴'
        assert not hryvnia.symbol_ahead
        assert hryvnia.symbol_separator == '\u00A0'
        assert hryvnia.localized_symbol == '₴'
        assert hryvnia.convertion == ''
        assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
        assert hryvnia.__repr__() == (
            'Hryvnia(amount: 0.1428571428571428571428571429, '
            'alpha_code: "UAH", '
            'symbol: "₴", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₴", '
            'numeric_code: "980", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert hryvnia.__str__() == '0,14 ₴'


    def test_hryvnia_negative(self):
        """test_hryvnia_negative."""
        amount = -100
        hryvnia = Hryvnia(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert hryvnia.numeric_code == '980'
        assert hryvnia.alpha_code == 'UAH'
        assert hryvnia.decimal_places == 2
        assert hryvnia.decimal_sign == ','
        assert hryvnia.grouping_places == 3
        assert hryvnia.grouping_sign == '\u202F'
        assert not hryvnia.international
        assert hryvnia.symbol == '₴'
        assert not hryvnia.symbol_ahead
        assert hryvnia.symbol_separator == '\u00A0'
        assert hryvnia.localized_symbol == '₴'
        assert hryvnia.convertion == ''
        assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
        assert hryvnia.__repr__() == (
            'Hryvnia(amount: -100, '
            'alpha_code: "UAH", '
            'symbol: "₴", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₴", '
            'numeric_code: "980", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert hryvnia.__str__() == '-100,00 ₴'


    def test_hryvnia_custom(self):
        """test_hryvnia_custom."""
        amount = 1000
        hryvnia = Hryvnia(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert hryvnia.amount == decimal
        assert hryvnia.numeric_code == '980'
        assert hryvnia.alpha_code == 'UAH'
        assert hryvnia.decimal_places == 5
        assert hryvnia.decimal_sign == '\u202F'
        assert hryvnia.grouping_places == 2
        assert hryvnia.grouping_sign == ','
        assert hryvnia.international
        assert hryvnia.symbol == '₴'
        assert not hryvnia.symbol_ahead
        assert hryvnia.symbol_separator == '_'
        assert hryvnia.localized_symbol == '₴'
        assert hryvnia.convertion == ''
        assert hryvnia.__hash__() == hash((decimal, 'UAH', '980'))
        assert hryvnia.__repr__() == (
            'Hryvnia(amount: 1000, '
            'alpha_code: "UAH", '
            'symbol: "₴", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₴", '
            'numeric_code: "980", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert hryvnia.__str__() == 'UAH 10,00.00000'


    def test_hryvnia_changed(self):
        """test_chryvnia_changed."""
        hryvnia = Hryvnia(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hryvnia.international = True


    def test_hryvnia_math_add(self):
        """test_hryvnia_math_add."""
        hryvnia_one = Hryvnia(amount=1)
        hryvnia_two = Hryvnia(amount=2)
        hryvnia_three = Hryvnia(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency UAH and OTHER.'):
            _ = hryvnia_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'hryvnia.Hryvnia\'> '
                    'and <class \'str\'>.')):
            _ = hryvnia_one.__add__('1.00')
        assert (
            hryvnia_one +
            hryvnia_two) == hryvnia_three


    def test_hryvnia_slots(self):
        """test_hryvnia_slots."""
        hryvnia = Hryvnia(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Hryvnia\' '
                    'object has no attribute \'new_variable\'')):
            hryvnia.new_variable = 'fail'  # pylint: disable=assigning-non-slot
