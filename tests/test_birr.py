# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Birr currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Ethiopian Birr representation."""

from multicurrency import EthiopianBirr


class TestEthiopianBirr:

    def test_ethiopian_birr(self):
        """test_ethiopian_birr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        ethiopian_birr = EthiopianBirr(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ethiopian_birr.amount == decimal
        assert ethiopian_birr.numeric_code == '230'
        assert ethiopian_birr.alpha_code == 'ETB'
        assert ethiopian_birr.decimal_places == 2
        assert ethiopian_birr.decimal_sign == '.'
        assert ethiopian_birr.grouping_places == 3
        assert ethiopian_birr.grouping_sign == ','
        assert not ethiopian_birr.international
        assert ethiopian_birr.symbol == 'ብር'
        assert ethiopian_birr.symbol_ahead
        assert ethiopian_birr.symbol_separator == '\u00A0'
        assert ethiopian_birr.localized_symbol == 'ብር'
        assert ethiopian_birr.convertion == ''
        assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
        assert ethiopian_birr.__repr__() == (
            'EthiopianBirr(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ETB", '
            'symbol: "ብር", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ብር", '
            'numeric_code: "230", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ethiopian_birr.__str__() == 'ብር 0.14'


    def test_ethiopian_birr_negative(self):
        """test_ethiopian_birr_negative."""
        amount = -100
        ethiopian_birr = EthiopianBirr(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ethiopian_birr.numeric_code == '230'
        assert ethiopian_birr.alpha_code == 'ETB'
        assert ethiopian_birr.decimal_places == 2
        assert ethiopian_birr.decimal_sign == '.'
        assert ethiopian_birr.grouping_places == 3
        assert ethiopian_birr.grouping_sign == ','
        assert not ethiopian_birr.international
        assert ethiopian_birr.symbol == 'ብር'
        assert ethiopian_birr.symbol_ahead
        assert ethiopian_birr.symbol_separator == '\u00A0'
        assert ethiopian_birr.localized_symbol == 'ብር'
        assert ethiopian_birr.convertion == ''
        assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
        assert ethiopian_birr.__repr__() == (
            'EthiopianBirr(amount: -100, '
            'alpha_code: "ETB", '
            'symbol: "ብር", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ብር", '
            'numeric_code: "230", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ethiopian_birr.__str__() == 'ብር -100.00'


    def test_ethiopian_birr_custom(self):
        """test_ethiopian_birr_custom."""
        amount = 1000
        ethiopian_birr = EthiopianBirr(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert ethiopian_birr.amount == decimal
        assert ethiopian_birr.numeric_code == '230'
        assert ethiopian_birr.alpha_code == 'ETB'
        assert ethiopian_birr.decimal_places == 5
        assert ethiopian_birr.decimal_sign == ','
        assert ethiopian_birr.grouping_places == 2
        assert ethiopian_birr.grouping_sign == '.'
        assert ethiopian_birr.international
        assert ethiopian_birr.symbol == 'ብር'
        assert not ethiopian_birr.symbol_ahead
        assert ethiopian_birr.symbol_separator == '_'
        assert ethiopian_birr.localized_symbol == 'ብር'
        assert ethiopian_birr.convertion == ''
        assert ethiopian_birr.__hash__() == hash((decimal, 'ETB', '230'))
        assert ethiopian_birr.__repr__() == (
            'EthiopianBirr(amount: 1000, '
            'alpha_code: "ETB", '
            'symbol: "ብር", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ብር", '
            'numeric_code: "230", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert ethiopian_birr.__str__() == 'ETB 10,00.00000'


    def test_ethiopian_birr_changed(self):
        """test_cethiopian_birr_changed."""
        ethiopian_birr = EthiopianBirr(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethiopian_birr.international = True


    def test_ethiopian_birr_math_add(self):
        """test_ethiopian_birr_math_add."""
        ethiopian_birr_one = EthiopianBirr(amount=1)
        ethiopian_birr_two = EthiopianBirr(amount=2)
        ethiopian_birr_three = EthiopianBirr(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ETB and OTHER.'):
            _ = ethiopian_birr_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'birr.EthiopianBirr\'> '
                    'and <class \'str\'>.')):
            _ = ethiopian_birr_one.__add__('1.00')
        assert (
            ethiopian_birr_one +
            ethiopian_birr_two) == ethiopian_birr_three


    def test_ethiopian_birr_slots(self):
        """test_ethiopian_birr_slots."""
        ethiopian_birr = EthiopianBirr(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EthiopianBirr\' '
                    'object has no attribute \'new_variable\'')):
            ethiopian_birr.new_variable = 'fail'  # pylint: disable=assigning-non-slot
