# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yuan currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Yuan


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Yuan representation."""


class TestYuan:
    """Yuan currency tests."""

    def test_yuan(self):
        """test_yuan."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        yuan = Yuan(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yuan.amount == decimal
        assert yuan.numeric_code == '156'
        assert yuan.alpha_code == 'CNY'
        assert yuan.decimal_places == 2
        assert yuan.decimal_sign == '.'
        assert yuan.grouping_places == 3
        assert yuan.grouping_sign == ','
        assert not yuan.international
        assert yuan.symbol == '¥'
        assert yuan.symbol_ahead
        assert yuan.symbol_separator == ''
        assert yuan.localized_symbol == '¥'
        assert yuan.convertion == ''
        assert yuan.__hash__() == hash(
            (yuan.__class__, decimal, 'CNY', '156'))
        assert yuan.__repr__() == (
            'Yuan(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CNY", '
            'symbol: "¥", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "¥", '
            'numeric_code: "156", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert yuan.__str__() == '¥0.14'

    def test_yuan_negative(self):
        """test_yuan_negative."""
        amount = -100
        yuan = Yuan(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yuan.numeric_code == '156'
        assert yuan.alpha_code == 'CNY'
        assert yuan.decimal_places == 2
        assert yuan.decimal_sign == '.'
        assert yuan.grouping_places == 3
        assert yuan.grouping_sign == ','
        assert not yuan.international
        assert yuan.symbol == '¥'
        assert yuan.symbol_ahead
        assert yuan.symbol_separator == ''
        assert yuan.localized_symbol == '¥'
        assert yuan.convertion == ''
        assert yuan.__hash__() == hash(
            (yuan.__class__, decimal, 'CNY', '156'))
        assert yuan.__repr__() == (
            'Yuan(amount: -100, '
            'alpha_code: "CNY", '
            'symbol: "¥", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "¥", '
            'numeric_code: "156", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert yuan.__str__() == '¥-100.00'

    def test_yuan_custom(self):
        """test_yuan_custom."""
        amount = 1000
        yuan = Yuan(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert yuan.amount == decimal
        assert yuan.numeric_code == '156'
        assert yuan.alpha_code == 'CNY'
        assert yuan.decimal_places == 5
        assert yuan.decimal_sign == ','
        assert yuan.grouping_places == 2
        assert yuan.grouping_sign == '.'
        assert yuan.international
        assert yuan.symbol == '¥'
        assert not yuan.symbol_ahead
        assert yuan.symbol_separator == '_'
        assert yuan.localized_symbol == '¥'
        assert yuan.convertion == ''
        assert yuan.__hash__() == hash(
            (yuan.__class__, decimal, 'CNY', '156'))
        assert yuan.__repr__() == (
            'Yuan(amount: 1000, '
            'alpha_code: "CNY", '
            'symbol: "¥", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "¥", '
            'numeric_code: "156", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert yuan.__str__() == 'CNY 10,00.00000'

    def test_yuan_changed(self):
        """test_cyuan_changed."""
        yuan = Yuan(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yuan.international = True

    def test_yuan_math_add(self):
        """test_yuan_math_add."""
        yuan_one = Yuan(amount=1)
        yuan_two = Yuan(amount=2)
        yuan_three = Yuan(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CNY and OTHER.'):
            _ = yuan_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'yuan.Yuan\'> '
                    'and <class \'str\'>.')):
            _ = yuan_one.__add__('1.00')
        assert (
            yuan_one +
            yuan_two) == yuan_three

    def test_yuan_slots(self):
        """test_yuan_slots."""
        yuan = Yuan(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Yuan\' '
                    'object has no attribute \'new_variable\'')):
            yuan.new_variable = 'fail'  # pylint: disable=assigning-non-slot
