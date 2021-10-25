# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yen currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Yen representation."""

from multicurrency import Yen


class TestYen:

    def test_yen(self):
        """test_yen."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        yen = Yen(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yen.amount == decimal
        assert yen.numeric_code == '392'
        assert yen.alpha_code == 'JPY'
        assert yen.decimal_places == 0
        assert yen.decimal_sign == '.'
        assert yen.grouping_places == 3
        assert yen.grouping_sign == ','
        assert not yen.international
        assert yen.symbol == '¥'
        assert yen.symbol_ahead
        assert yen.symbol_separator == ''
        assert yen.localized_symbol == '¥'
        assert yen.convertion == ''
        assert yen.__hash__() == hash((decimal, 'JPY', '392'))
        assert yen.__repr__() == (
            'Yen(amount: 0.1428571428571428571428571429, '
            'alpha_code: "JPY", '
            'symbol: "¥", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "¥", '
            'numeric_code: "392", '
            'decimal_places: "0", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert yen.__str__() == '¥0'


    def test_yen_negative(self):
        """test_yen_negative."""
        amount = -100
        yen = Yen(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yen.numeric_code == '392'
        assert yen.alpha_code == 'JPY'
        assert yen.decimal_places == 0
        assert yen.decimal_sign == '.'
        assert yen.grouping_places == 3
        assert yen.grouping_sign == ','
        assert not yen.international
        assert yen.symbol == '¥'
        assert yen.symbol_ahead
        assert yen.symbol_separator == ''
        assert yen.localized_symbol == '¥'
        assert yen.convertion == ''
        assert yen.__hash__() == hash((decimal, 'JPY', '392'))
        assert yen.__repr__() == (
            'Yen(amount: -100, '
            'alpha_code: "JPY", '
            'symbol: "¥", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "¥", '
            'numeric_code: "392", '
            'decimal_places: "0", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert yen.__str__() == '¥-100'


    def test_yen_custom(self):
        """test_yen_custom."""
        amount = 1000
        yen = Yen(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert yen.amount == decimal
        assert yen.numeric_code == '392'
        assert yen.alpha_code == 'JPY'
        assert yen.decimal_places == 5
        assert yen.decimal_sign == ','
        assert yen.grouping_places == 2
        assert yen.grouping_sign == '.'
        assert yen.international
        assert yen.symbol == '¥'
        assert not yen.symbol_ahead
        assert yen.symbol_separator == '_'
        assert yen.localized_symbol == '¥'
        assert yen.convertion == ''
        assert yen.__hash__() == hash((decimal, 'JPY', '392'))
        assert yen.__repr__() == (
            'Yen(amount: 1000, '
            'alpha_code: "JPY", '
            'symbol: "¥", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "¥", '
            'numeric_code: "392", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert yen.__str__() == 'JPY 10,00.00000'


    def test_yen_changed(self):
        """test_cyen_changed."""
        yen = Yen(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yen.international = True


    def test_yen_math_add(self):
        """test_yen_math_add."""
        yen_one = Yen(amount=1)
        yen_two = Yen(amount=2)
        yen_three = Yen(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency JPY and OTHER.'):
            _ = yen_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'yen.Yen\'> '
                    'and <class \'str\'>.')):
            _ = yen_one.__add__('1.00')
        assert (
            yen_one +
            yen_two) == yen_three


    def test_yen_slots(self):
        """test_yen_slots."""
        yen = Yen(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Yen\' '
                    'object has no attribute \'new_variable\'')):
            yen.new_variable = 'fail'  # pylint: disable=assigning-non-slot
