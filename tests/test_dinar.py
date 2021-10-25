# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dinar currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Bahraini Dinar representation."""

from multicurrency import BahrainiDinar


class TestBahrainiDinar:

    def test_bahraini_dinar(self):
        """test_bahraini_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        bahraini_dinar = BahrainiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bahraini_dinar.amount == decimal
        assert bahraini_dinar.numeric_code == '048'
        assert bahraini_dinar.alpha_code == 'BHD'
        assert bahraini_dinar.decimal_places == 3
        assert bahraini_dinar.decimal_sign == '\u066B'
        assert bahraini_dinar.grouping_places == 3
        assert bahraini_dinar.grouping_sign == '\u066C'
        assert not bahraini_dinar.international
        assert bahraini_dinar.symbol == 'د.ب.'
        assert bahraini_dinar.symbol_ahead
        assert bahraini_dinar.symbol_separator == '\u00A0'
        assert bahraini_dinar.localized_symbol == 'د.ب.'
        assert bahraini_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
        assert bahraini_dinar.__repr__() == (
            'BahrainiDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BHD", '
            'symbol: "د.ب.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ب.", '
            'numeric_code: "048", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert bahraini_dinar.__str__() == 'د.ب. ٠٫١٤٣'


    def test_bahraini_dinar_negative(self):
        """test_bahraini_dinar_negative."""
        amount = -100
        bahraini_dinar = BahrainiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bahraini_dinar.numeric_code == '048'
        assert bahraini_dinar.alpha_code == 'BHD'
        assert bahraini_dinar.decimal_places == 3
        assert bahraini_dinar.decimal_sign == '\u066B'
        assert bahraini_dinar.grouping_places == 3
        assert bahraini_dinar.grouping_sign == '\u066C'
        assert not bahraini_dinar.international
        assert bahraini_dinar.symbol == 'د.ب.'
        assert bahraini_dinar.symbol_ahead
        assert bahraini_dinar.symbol_separator == '\u00A0'
        assert bahraini_dinar.localized_symbol == 'د.ب.'
        assert bahraini_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
        assert bahraini_dinar.__repr__() == (
            'BahrainiDinar(amount: -100, '
            'alpha_code: "BHD", '
            'symbol: "د.ب.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ب.", '
            'numeric_code: "048", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert bahraini_dinar.__str__() == 'د.ب. -١٠٠٫٠٠٠'


    def test_bahraini_dinar_custom(self):
        """test_bahraini_dinar_custom."""
        amount = 1000
        bahraini_dinar = BahrainiDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert bahraini_dinar.amount == decimal
        assert bahraini_dinar.numeric_code == '048'
        assert bahraini_dinar.alpha_code == 'BHD'
        assert bahraini_dinar.decimal_places == 5
        assert bahraini_dinar.decimal_sign == '\u066C'
        assert bahraini_dinar.grouping_places == 2
        assert bahraini_dinar.grouping_sign == '\u066B'
        assert bahraini_dinar.international
        assert bahraini_dinar.symbol == 'د.ب.'
        assert not bahraini_dinar.symbol_ahead
        assert bahraini_dinar.symbol_separator == '_'
        assert bahraini_dinar.localized_symbol == 'د.ب.'
        assert bahraini_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert bahraini_dinar.__hash__() == hash((decimal, 'BHD', '048'))
        assert bahraini_dinar.__repr__() == (
            'BahrainiDinar(amount: 1000, '
            'alpha_code: "BHD", '
            'symbol: "د.ب.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ب.", '
            'numeric_code: "048", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert bahraini_dinar.__str__() == 'BHD 10,00.00000'


    def test_bahraini_dinar_changed(self):
        """test_cbahraini_dinar_changed."""
        bahraini_dinar = BahrainiDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahraini_dinar.international = True


    def test_bahraini_dinar_math_add(self):
        """test_bahraini_dinar_math_add."""
        bahraini_dinar_one = BahrainiDinar(amount=1)
        bahraini_dinar_two = BahrainiDinar(amount=2)
        bahraini_dinar_three = BahrainiDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BHD and OTHER.'):
            _ = bahraini_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.BahrainiDinar\'> '
                    'and <class \'str\'>.')):
            _ = bahraini_dinar_one.__add__('1.00')
        assert (
            bahraini_dinar_one +
            bahraini_dinar_two) == bahraini_dinar_three


    def test_bahraini_dinar_slots(self):
        """test_bahraini_dinar_slots."""
        bahraini_dinar = BahrainiDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BahrainiDinar\' '
                    'object has no attribute \'new_variable\'')):
            bahraini_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Algerian Dinar representation."""

from multicurrency import AlgerianDinar


class TestAlgerianDinar:

    def test_algerian_dinar(self):
        """test_algerian_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        algerian_dinar = AlgerianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert algerian_dinar.amount == decimal
        assert algerian_dinar.numeric_code == '012'
        assert algerian_dinar.alpha_code == 'DZD'
        assert algerian_dinar.decimal_places == 2
        assert algerian_dinar.decimal_sign == ','
        assert algerian_dinar.grouping_places == 3
        assert algerian_dinar.grouping_sign == '.'
        assert not algerian_dinar.international
        assert algerian_dinar.symbol == 'د.ج.'
        assert not algerian_dinar.symbol_ahead
        assert algerian_dinar.symbol_separator == '\u00A0'
        assert algerian_dinar.localized_symbol == 'د.ج.'
        assert algerian_dinar.convertion == ''
        assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
        assert algerian_dinar.__repr__() == (
            'AlgerianDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "DZD", '
            'symbol: "د.ج.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ج.", '
            'numeric_code: "012", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert algerian_dinar.__str__() == '0,14 د.ج.'


    def test_algerian_dinar_negative(self):
        """test_algerian_dinar_negative."""
        amount = -100
        algerian_dinar = AlgerianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert algerian_dinar.numeric_code == '012'
        assert algerian_dinar.alpha_code == 'DZD'
        assert algerian_dinar.decimal_places == 2
        assert algerian_dinar.decimal_sign == ','
        assert algerian_dinar.grouping_places == 3
        assert algerian_dinar.grouping_sign == '.'
        assert not algerian_dinar.international
        assert algerian_dinar.symbol == 'د.ج.'
        assert not algerian_dinar.symbol_ahead
        assert algerian_dinar.symbol_separator == '\u00A0'
        assert algerian_dinar.localized_symbol == 'د.ج.'
        assert algerian_dinar.convertion == ''
        assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
        assert algerian_dinar.__repr__() == (
            'AlgerianDinar(amount: -100, '
            'alpha_code: "DZD", '
            'symbol: "د.ج.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ج.", '
            'numeric_code: "012", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert algerian_dinar.__str__() == '-100,00 د.ج.'


    def test_algerian_dinar_custom(self):
        """test_algerian_dinar_custom."""
        amount = 1000
        algerian_dinar = AlgerianDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert algerian_dinar.amount == decimal
        assert algerian_dinar.numeric_code == '012'
        assert algerian_dinar.alpha_code == 'DZD'
        assert algerian_dinar.decimal_places == 5
        assert algerian_dinar.decimal_sign == '.'
        assert algerian_dinar.grouping_places == 2
        assert algerian_dinar.grouping_sign == ','
        assert algerian_dinar.international
        assert algerian_dinar.symbol == 'د.ج.'
        assert not algerian_dinar.symbol_ahead
        assert algerian_dinar.symbol_separator == '_'
        assert algerian_dinar.localized_symbol == 'د.ج.'
        assert algerian_dinar.convertion == ''
        assert algerian_dinar.__hash__() == hash((decimal, 'DZD', '012'))
        assert algerian_dinar.__repr__() == (
            'AlgerianDinar(amount: 1000, '
            'alpha_code: "DZD", '
            'symbol: "د.ج.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ج.", '
            'numeric_code: "012", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert algerian_dinar.__str__() == 'DZD 10,00.00000'


    def test_algerian_dinar_changed(self):
        """test_calgerian_dinar_changed."""
        algerian_dinar = AlgerianDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            algerian_dinar.international = True


    def test_algerian_dinar_math_add(self):
        """test_algerian_dinar_math_add."""
        algerian_dinar_one = AlgerianDinar(amount=1)
        algerian_dinar_two = AlgerianDinar(amount=2)
        algerian_dinar_three = AlgerianDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency DZD and OTHER.'):
            _ = algerian_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.AlgerianDinar\'> '
                    'and <class \'str\'>.')):
            _ = algerian_dinar_one.__add__('1.00')
        assert (
            algerian_dinar_one +
            algerian_dinar_two) == algerian_dinar_three


    def test_algerian_dinar_slots(self):
        """test_algerian_dinar_slots."""
        algerian_dinar = AlgerianDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AlgerianDinar\' '
                    'object has no attribute \'new_variable\'')):
            algerian_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Iraqi Dinar representation."""

from multicurrency import IraqiDinar


class TestIraqiDinar:

    def test_iraqi_dinar(self):
        """test_iraqi_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        iraqi_dinar = IraqiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iraqi_dinar.amount == decimal
        assert iraqi_dinar.numeric_code == '368'
        assert iraqi_dinar.alpha_code == 'IQD'
        assert iraqi_dinar.decimal_places == 3
        assert iraqi_dinar.decimal_sign == '\u066B'
        assert iraqi_dinar.grouping_places == 3
        assert iraqi_dinar.grouping_sign == '\u066C'
        assert not iraqi_dinar.international
        assert iraqi_dinar.symbol == 'د.ع.'
        assert iraqi_dinar.symbol_ahead
        assert iraqi_dinar.symbol_separator == '\u00A0'
        assert iraqi_dinar.localized_symbol == 'د.ع.'
        assert iraqi_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
        assert iraqi_dinar.__repr__() == (
            'IraqiDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "IQD", '
            'symbol: "د.ع.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ع.", '
            'numeric_code: "368", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert iraqi_dinar.__str__() == 'د.ع. ٠٫١٤٣'


    def test_iraqi_dinar_negative(self):
        """test_iraqi_dinar_negative."""
        amount = -100
        iraqi_dinar = IraqiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iraqi_dinar.numeric_code == '368'
        assert iraqi_dinar.alpha_code == 'IQD'
        assert iraqi_dinar.decimal_places == 3
        assert iraqi_dinar.decimal_sign == '\u066B'
        assert iraqi_dinar.grouping_places == 3
        assert iraqi_dinar.grouping_sign == '\u066C'
        assert not iraqi_dinar.international
        assert iraqi_dinar.symbol == 'د.ع.'
        assert iraqi_dinar.symbol_ahead
        assert iraqi_dinar.symbol_separator == '\u00A0'
        assert iraqi_dinar.localized_symbol == 'د.ع.'
        assert iraqi_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
        assert iraqi_dinar.__repr__() == (
            'IraqiDinar(amount: -100, '
            'alpha_code: "IQD", '
            'symbol: "د.ع.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ع.", '
            'numeric_code: "368", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert iraqi_dinar.__str__() == 'د.ع. -١٠٠٫٠٠٠'


    def test_iraqi_dinar_custom(self):
        """test_iraqi_dinar_custom."""
        amount = 1000
        iraqi_dinar = IraqiDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert iraqi_dinar.amount == decimal
        assert iraqi_dinar.numeric_code == '368'
        assert iraqi_dinar.alpha_code == 'IQD'
        assert iraqi_dinar.decimal_places == 5
        assert iraqi_dinar.decimal_sign == '\u066C'
        assert iraqi_dinar.grouping_places == 2
        assert iraqi_dinar.grouping_sign == '\u066B'
        assert iraqi_dinar.international
        assert iraqi_dinar.symbol == 'د.ع.'
        assert not iraqi_dinar.symbol_ahead
        assert iraqi_dinar.symbol_separator == '_'
        assert iraqi_dinar.localized_symbol == 'د.ع.'
        assert iraqi_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert iraqi_dinar.__hash__() == hash((decimal, 'IQD', '368'))
        assert iraqi_dinar.__repr__() == (
            'IraqiDinar(amount: 1000, '
            'alpha_code: "IQD", '
            'symbol: "د.ع.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ع.", '
            'numeric_code: "368", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert iraqi_dinar.__str__() == 'IQD 10,00.00000'


    def test_iraqi_dinar_changed(self):
        """test_ciraqi_dinar_changed."""
        iraqi_dinar = IraqiDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iraqi_dinar.international = True


    def test_iraqi_dinar_math_add(self):
        """test_iraqi_dinar_math_add."""
        iraqi_dinar_one = IraqiDinar(amount=1)
        iraqi_dinar_two = IraqiDinar(amount=2)
        iraqi_dinar_three = IraqiDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency IQD and OTHER.'):
            _ = iraqi_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.IraqiDinar\'> '
                    'and <class \'str\'>.')):
            _ = iraqi_dinar_one.__add__('1.00')
        assert (
            iraqi_dinar_one +
            iraqi_dinar_two) == iraqi_dinar_three


    def test_iraqi_dinar_slots(self):
        """test_iraqi_dinar_slots."""
        iraqi_dinar = IraqiDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IraqiDinar\' '
                    'object has no attribute \'new_variable\'')):
            iraqi_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Jordanian Dinar representation."""

from multicurrency import JordanianDinar


class TestJordanianDinar:

    def test_jordanian_dinar(self):
        """test_jordanian_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        jordanian_dinar = JordanianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert jordanian_dinar.amount == decimal
        assert jordanian_dinar.numeric_code == '400'
        assert jordanian_dinar.alpha_code == 'JOD'
        assert jordanian_dinar.decimal_places == 3
        assert jordanian_dinar.decimal_sign == '\u066B'
        assert jordanian_dinar.grouping_places == 3
        assert jordanian_dinar.grouping_sign == '\u066C'
        assert not jordanian_dinar.international
        assert jordanian_dinar.symbol == 'د.أ.'
        assert jordanian_dinar.symbol_ahead
        assert jordanian_dinar.symbol_separator == '\u00A0'
        assert jordanian_dinar.localized_symbol == 'د.أ.'
        assert jordanian_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
        assert jordanian_dinar.__repr__() == (
            'JordanianDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "JOD", '
            'symbol: "د.أ.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.أ.", '
            'numeric_code: "400", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert jordanian_dinar.__str__() == 'د.أ. ٠٫١٤٣'


    def test_jordanian_dinar_negative(self):
        """test_jordanian_dinar_negative."""
        amount = -100
        jordanian_dinar = JordanianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert jordanian_dinar.numeric_code == '400'
        assert jordanian_dinar.alpha_code == 'JOD'
        assert jordanian_dinar.decimal_places == 3
        assert jordanian_dinar.decimal_sign == '\u066B'
        assert jordanian_dinar.grouping_places == 3
        assert jordanian_dinar.grouping_sign == '\u066C'
        assert not jordanian_dinar.international
        assert jordanian_dinar.symbol == 'د.أ.'
        assert jordanian_dinar.symbol_ahead
        assert jordanian_dinar.symbol_separator == '\u00A0'
        assert jordanian_dinar.localized_symbol == 'د.أ.'
        assert jordanian_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
        assert jordanian_dinar.__repr__() == (
            'JordanianDinar(amount: -100, '
            'alpha_code: "JOD", '
            'symbol: "د.أ.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.أ.", '
            'numeric_code: "400", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert jordanian_dinar.__str__() == 'د.أ. -١٠٠٫٠٠٠'


    def test_jordanian_dinar_custom(self):
        """test_jordanian_dinar_custom."""
        amount = 1000
        jordanian_dinar = JordanianDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert jordanian_dinar.amount == decimal
        assert jordanian_dinar.numeric_code == '400'
        assert jordanian_dinar.alpha_code == 'JOD'
        assert jordanian_dinar.decimal_places == 5
        assert jordanian_dinar.decimal_sign == '\u066C'
        assert jordanian_dinar.grouping_places == 2
        assert jordanian_dinar.grouping_sign == '\u066B'
        assert jordanian_dinar.international
        assert jordanian_dinar.symbol == 'د.أ.'
        assert not jordanian_dinar.symbol_ahead
        assert jordanian_dinar.symbol_separator == '_'
        assert jordanian_dinar.localized_symbol == 'د.أ.'
        assert jordanian_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert jordanian_dinar.__hash__() == hash((decimal, 'JOD', '400'))
        assert jordanian_dinar.__repr__() == (
            'JordanianDinar(amount: 1000, '
            'alpha_code: "JOD", '
            'symbol: "د.أ.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.أ.", '
            'numeric_code: "400", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert jordanian_dinar.__str__() == 'JOD 10,00.00000'


    def test_jordanian_dinar_changed(self):
        """test_cjordanian_dinar_changed."""
        jordanian_dinar = JordanianDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jordanian_dinar.international = True


    def test_jordanian_dinar_math_add(self):
        """test_jordanian_dinar_math_add."""
        jordanian_dinar_one = JordanianDinar(amount=1)
        jordanian_dinar_two = JordanianDinar(amount=2)
        jordanian_dinar_three = JordanianDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency JOD and OTHER.'):
            _ = jordanian_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.JordanianDinar\'> '
                    'and <class \'str\'>.')):
            _ = jordanian_dinar_one.__add__('1.00')
        assert (
            jordanian_dinar_one +
            jordanian_dinar_two) == jordanian_dinar_three


    def test_jordanian_dinar_slots(self):
        """test_jordanian_dinar_slots."""
        jordanian_dinar = JordanianDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'JordanianDinar\' '
                    'object has no attribute \'new_variable\'')):
            jordanian_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Kuwaiti Dinar representation."""

from multicurrency import KuwaitiDinar


class TestKuwaitiDinar:

    def test_kuwaiti_dinar(self):
        """test_kuwaiti_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        kuwaiti_dinar = KuwaitiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kuwaiti_dinar.amount == decimal
        assert kuwaiti_dinar.numeric_code == '414'
        assert kuwaiti_dinar.alpha_code == 'KWD'
        assert kuwaiti_dinar.decimal_places == 3
        assert kuwaiti_dinar.decimal_sign == '\u066B'
        assert kuwaiti_dinar.grouping_places == 3
        assert kuwaiti_dinar.grouping_sign == '\u066C'
        assert not kuwaiti_dinar.international
        assert kuwaiti_dinar.symbol == 'د.ك.'
        assert kuwaiti_dinar.symbol_ahead
        assert kuwaiti_dinar.symbol_separator == '\u00A0'
        assert kuwaiti_dinar.localized_symbol == 'د.ك.'
        assert kuwaiti_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
        assert kuwaiti_dinar.__repr__() == (
            'KuwaitiDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "KWD", '
            'symbol: "د.ك.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ك.", '
            'numeric_code: "414", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert kuwaiti_dinar.__str__() == 'د.ك. ٠٫١٤٣'


    def test_kuwaiti_dinar_negative(self):
        """test_kuwaiti_dinar_negative."""
        amount = -100
        kuwaiti_dinar = KuwaitiDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kuwaiti_dinar.numeric_code == '414'
        assert kuwaiti_dinar.alpha_code == 'KWD'
        assert kuwaiti_dinar.decimal_places == 3
        assert kuwaiti_dinar.decimal_sign == '\u066B'
        assert kuwaiti_dinar.grouping_places == 3
        assert kuwaiti_dinar.grouping_sign == '\u066C'
        assert not kuwaiti_dinar.international
        assert kuwaiti_dinar.symbol == 'د.ك.'
        assert kuwaiti_dinar.symbol_ahead
        assert kuwaiti_dinar.symbol_separator == '\u00A0'
        assert kuwaiti_dinar.localized_symbol == 'د.ك.'
        assert kuwaiti_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
        assert kuwaiti_dinar.__repr__() == (
            'KuwaitiDinar(amount: -100, '
            'alpha_code: "KWD", '
            'symbol: "د.ك.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ك.", '
            'numeric_code: "414", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert kuwaiti_dinar.__str__() == 'د.ك. -١٠٠٫٠٠٠'


    def test_kuwaiti_dinar_custom(self):
        """test_kuwaiti_dinar_custom."""
        amount = 1000
        kuwaiti_dinar = KuwaitiDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert kuwaiti_dinar.amount == decimal
        assert kuwaiti_dinar.numeric_code == '414'
        assert kuwaiti_dinar.alpha_code == 'KWD'
        assert kuwaiti_dinar.decimal_places == 5
        assert kuwaiti_dinar.decimal_sign == '\u066C'
        assert kuwaiti_dinar.grouping_places == 2
        assert kuwaiti_dinar.grouping_sign == '\u066B'
        assert kuwaiti_dinar.international
        assert kuwaiti_dinar.symbol == 'د.ك.'
        assert not kuwaiti_dinar.symbol_ahead
        assert kuwaiti_dinar.symbol_separator == '_'
        assert kuwaiti_dinar.localized_symbol == 'د.ك.'
        assert kuwaiti_dinar.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert kuwaiti_dinar.__hash__() == hash((decimal, 'KWD', '414'))
        assert kuwaiti_dinar.__repr__() == (
            'KuwaitiDinar(amount: 1000, '
            'alpha_code: "KWD", '
            'symbol: "د.ك.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ك.", '
            'numeric_code: "414", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert kuwaiti_dinar.__str__() == 'KWD 10,00.00000'


    def test_kuwaiti_dinar_changed(self):
        """test_ckuwaiti_dinar_changed."""
        kuwaiti_dinar = KuwaitiDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kuwaiti_dinar.international = True


    def test_kuwaiti_dinar_math_add(self):
        """test_kuwaiti_dinar_math_add."""
        kuwaiti_dinar_one = KuwaitiDinar(amount=1)
        kuwaiti_dinar_two = KuwaitiDinar(amount=2)
        kuwaiti_dinar_three = KuwaitiDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency KWD and OTHER.'):
            _ = kuwaiti_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.KuwaitiDinar\'> '
                    'and <class \'str\'>.')):
            _ = kuwaiti_dinar_one.__add__('1.00')
        assert (
            kuwaiti_dinar_one +
            kuwaiti_dinar_two) == kuwaiti_dinar_three


    def test_kuwaiti_dinar_slots(self):
        """test_kuwaiti_dinar_slots."""
        kuwaiti_dinar = KuwaitiDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'KuwaitiDinar\' '
                    'object has no attribute \'new_variable\'')):
            kuwaiti_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Libyan Dinar representation."""

from multicurrency import LibyanDinar


class TestLibyanDinar:

    def test_libyan_dinar(self):
        """test_libyan_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        libyan_dinar = LibyanDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert libyan_dinar.amount == decimal
        assert libyan_dinar.numeric_code == '434'
        assert libyan_dinar.alpha_code == 'LYD'
        assert libyan_dinar.decimal_places == 3
        assert libyan_dinar.decimal_sign == ','
        assert libyan_dinar.grouping_places == 3
        assert libyan_dinar.grouping_sign == '.'
        assert not libyan_dinar.international
        assert libyan_dinar.symbol == 'د.ل.'
        assert libyan_dinar.symbol_ahead
        assert libyan_dinar.symbol_separator == '\u00A0'
        assert libyan_dinar.localized_symbol == 'د.ل.'
        assert libyan_dinar.convertion == ''
        assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
        assert libyan_dinar.__repr__() == (
            'LibyanDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "LYD", '
            'symbol: "د.ل.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ل.", '
            'numeric_code: "434", '
            'decimal_places: "3", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert libyan_dinar.__str__() == 'د.ل. 0,143'


    def test_libyan_dinar_negative(self):
        """test_libyan_dinar_negative."""
        amount = -100
        libyan_dinar = LibyanDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert libyan_dinar.numeric_code == '434'
        assert libyan_dinar.alpha_code == 'LYD'
        assert libyan_dinar.decimal_places == 3
        assert libyan_dinar.decimal_sign == ','
        assert libyan_dinar.grouping_places == 3
        assert libyan_dinar.grouping_sign == '.'
        assert not libyan_dinar.international
        assert libyan_dinar.symbol == 'د.ل.'
        assert libyan_dinar.symbol_ahead
        assert libyan_dinar.symbol_separator == '\u00A0'
        assert libyan_dinar.localized_symbol == 'د.ل.'
        assert libyan_dinar.convertion == ''
        assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
        assert libyan_dinar.__repr__() == (
            'LibyanDinar(amount: -100, '
            'alpha_code: "LYD", '
            'symbol: "د.ل.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ل.", '
            'numeric_code: "434", '
            'decimal_places: "3", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert libyan_dinar.__str__() == 'د.ل. -100,000'


    def test_libyan_dinar_custom(self):
        """test_libyan_dinar_custom."""
        amount = 1000
        libyan_dinar = LibyanDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert libyan_dinar.amount == decimal
        assert libyan_dinar.numeric_code == '434'
        assert libyan_dinar.alpha_code == 'LYD'
        assert libyan_dinar.decimal_places == 5
        assert libyan_dinar.decimal_sign == '.'
        assert libyan_dinar.grouping_places == 2
        assert libyan_dinar.grouping_sign == ','
        assert libyan_dinar.international
        assert libyan_dinar.symbol == 'د.ل.'
        assert not libyan_dinar.symbol_ahead
        assert libyan_dinar.symbol_separator == '_'
        assert libyan_dinar.localized_symbol == 'د.ل.'
        assert libyan_dinar.convertion == ''
        assert libyan_dinar.__hash__() == hash((decimal, 'LYD', '434'))
        assert libyan_dinar.__repr__() == (
            'LibyanDinar(amount: 1000, '
            'alpha_code: "LYD", '
            'symbol: "د.ل.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ل.", '
            'numeric_code: "434", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert libyan_dinar.__str__() == 'LYD 10,00.00000'


    def test_libyan_dinar_changed(self):
        """test_clibyan_dinar_changed."""
        libyan_dinar = LibyanDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            libyan_dinar.international = True


    def test_libyan_dinar_math_add(self):
        """test_libyan_dinar_math_add."""
        libyan_dinar_one = LibyanDinar(amount=1)
        libyan_dinar_two = LibyanDinar(amount=2)
        libyan_dinar_three = LibyanDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency LYD and OTHER.'):
            _ = libyan_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.LibyanDinar\'> '
                    'and <class \'str\'>.')):
            _ = libyan_dinar_one.__add__('1.00')
        assert (
            libyan_dinar_one +
            libyan_dinar_two) == libyan_dinar_three


    def test_libyan_dinar_slots(self):
        """test_libyan_dinar_slots."""
        libyan_dinar = LibyanDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'LibyanDinar\' '
                    'object has no attribute \'new_variable\'')):
            libyan_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Serbian Dinar XK representation."""

from multicurrency import SerbianDinarXK


class TestSerbianDinarXK:

    def test_serbian_dinar_xk(self):
        """test_serbian_dinar_xk."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        serbian_dinar_xk = SerbianDinarXK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_xk.amount == decimal
        assert serbian_dinar_xk.numeric_code == '941'
        assert serbian_dinar_xk.alpha_code == 'RSD'
        assert serbian_dinar_xk.decimal_places == 2
        assert serbian_dinar_xk.decimal_sign == ','
        assert serbian_dinar_xk.grouping_places == 3
        assert serbian_dinar_xk.grouping_sign == '.'
        assert not serbian_dinar_xk.international
        assert serbian_dinar_xk.symbol == 'дин.'
        assert not serbian_dinar_xk.symbol_ahead
        assert serbian_dinar_xk.symbol_separator == '\u00A0'
        assert serbian_dinar_xk.localized_symbol == 'дин.'
        assert serbian_dinar_xk.convertion == ''
        assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_xk.__repr__() == (
            'SerbianDinarXK(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert serbian_dinar_xk.__str__() == '0,14 дин.'


    def test_serbian_dinar_xk_negative(self):
        """test_serbian_dinar_xk_negative."""
        amount = -100
        serbian_dinar_xk = SerbianDinarXK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_xk.numeric_code == '941'
        assert serbian_dinar_xk.alpha_code == 'RSD'
        assert serbian_dinar_xk.decimal_places == 2
        assert serbian_dinar_xk.decimal_sign == ','
        assert serbian_dinar_xk.grouping_places == 3
        assert serbian_dinar_xk.grouping_sign == '.'
        assert not serbian_dinar_xk.international
        assert serbian_dinar_xk.symbol == 'дин.'
        assert not serbian_dinar_xk.symbol_ahead
        assert serbian_dinar_xk.symbol_separator == '\u00A0'
        assert serbian_dinar_xk.localized_symbol == 'дин.'
        assert serbian_dinar_xk.convertion == ''
        assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_xk.__repr__() == (
            'SerbianDinarXK(amount: -100, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert serbian_dinar_xk.__str__() == '-100,00 дин.'


    def test_serbian_dinar_xk_custom(self):
        """test_serbian_dinar_xk_custom."""
        amount = 1000
        serbian_dinar_xk = SerbianDinarXK(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_xk.amount == decimal
        assert serbian_dinar_xk.numeric_code == '941'
        assert serbian_dinar_xk.alpha_code == 'RSD'
        assert serbian_dinar_xk.decimal_places == 5
        assert serbian_dinar_xk.decimal_sign == '.'
        assert serbian_dinar_xk.grouping_places == 2
        assert serbian_dinar_xk.grouping_sign == ','
        assert serbian_dinar_xk.international
        assert serbian_dinar_xk.symbol == 'дин.'
        assert not serbian_dinar_xk.symbol_ahead
        assert serbian_dinar_xk.symbol_separator == '_'
        assert serbian_dinar_xk.localized_symbol == 'дин.'
        assert serbian_dinar_xk.convertion == ''
        assert serbian_dinar_xk.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_xk.__repr__() == (
            'SerbianDinarXK(amount: 1000, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert serbian_dinar_xk.__str__() == 'RSD 10,00.00000'


    def test_serbian_dinar_xk_changed(self):
        """test_cserbian_dinar_xk_changed."""
        serbian_dinar_xk = SerbianDinarXK(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_xk.international = True


    def test_serbian_dinar_xk_math_add(self):
        """test_serbian_dinar_xk_math_add."""
        serbian_dinar_xk_one = SerbianDinarXK(amount=1)
        serbian_dinar_xk_two = SerbianDinarXK(amount=2)
        serbian_dinar_xk_three = SerbianDinarXK(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RSD and OTHER.'):
            _ = serbian_dinar_xk_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.SerbianDinarXK\'> '
                    'and <class \'str\'>.')):
            _ = serbian_dinar_xk_one.__add__('1.00')
        assert (
            serbian_dinar_xk_one +
            serbian_dinar_xk_two) == serbian_dinar_xk_three


    def test_serbian_dinar_xk_slots(self):
        """test_serbian_dinar_xk_slots."""
        serbian_dinar_xk = SerbianDinarXK(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SerbianDinarXK\' '
                    'object has no attribute \'new_variable\'')):
            serbian_dinar_xk.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Serbian Dinar SR representation."""

from multicurrency import SerbianDinarSR


class TestSerbianDinarSR:

    def test_serbian_dinar_sr(self):
        """test_serbian_dinar_sr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        serbian_dinar_sr = SerbianDinarSR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_sr.amount == decimal
        assert serbian_dinar_sr.numeric_code == '941'
        assert serbian_dinar_sr.alpha_code == 'RSD'
        assert serbian_dinar_sr.decimal_places == 2
        assert serbian_dinar_sr.decimal_sign == ','
        assert serbian_dinar_sr.grouping_places == 3
        assert serbian_dinar_sr.grouping_sign == '\u202F'
        assert not serbian_dinar_sr.international
        assert serbian_dinar_sr.symbol == 'дин.'
        assert not serbian_dinar_sr.symbol_ahead
        assert serbian_dinar_sr.symbol_separator == '\u00A0'
        assert serbian_dinar_sr.localized_symbol == 'дин.'
        assert serbian_dinar_sr.convertion == ''
        assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_sr.__repr__() == (
            'SerbianDinarSR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert serbian_dinar_sr.__str__() == '0,14 дин.'


    def test_serbian_dinar_sr_negative(self):
        """test_serbian_dinar_sr_negative."""
        amount = -100
        serbian_dinar_sr = SerbianDinarSR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_sr.numeric_code == '941'
        assert serbian_dinar_sr.alpha_code == 'RSD'
        assert serbian_dinar_sr.decimal_places == 2
        assert serbian_dinar_sr.decimal_sign == ','
        assert serbian_dinar_sr.grouping_places == 3
        assert serbian_dinar_sr.grouping_sign == '\u202F'
        assert not serbian_dinar_sr.international
        assert serbian_dinar_sr.symbol == 'дин.'
        assert not serbian_dinar_sr.symbol_ahead
        assert serbian_dinar_sr.symbol_separator == '\u00A0'
        assert serbian_dinar_sr.localized_symbol == 'дин.'
        assert serbian_dinar_sr.convertion == ''
        assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_sr.__repr__() == (
            'SerbianDinarSR(amount: -100, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert serbian_dinar_sr.__str__() == '-100,00 дин.'


    def test_serbian_dinar_sr_custom(self):
        """test_serbian_dinar_sr_custom."""
        amount = 1000
        serbian_dinar_sr = SerbianDinarSR(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert serbian_dinar_sr.amount == decimal
        assert serbian_dinar_sr.numeric_code == '941'
        assert serbian_dinar_sr.alpha_code == 'RSD'
        assert serbian_dinar_sr.decimal_places == 5
        assert serbian_dinar_sr.decimal_sign == '\u202F'
        assert serbian_dinar_sr.grouping_places == 2
        assert serbian_dinar_sr.grouping_sign == ','
        assert serbian_dinar_sr.international
        assert serbian_dinar_sr.symbol == 'дин.'
        assert not serbian_dinar_sr.symbol_ahead
        assert serbian_dinar_sr.symbol_separator == '_'
        assert serbian_dinar_sr.localized_symbol == 'дин.'
        assert serbian_dinar_sr.convertion == ''
        assert serbian_dinar_sr.__hash__() == hash((decimal, 'RSD', '941'))
        assert serbian_dinar_sr.__repr__() == (
            'SerbianDinarSR(amount: 1000, '
            'alpha_code: "RSD", '
            'symbol: "дин.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "дин.", '
            'numeric_code: "941", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert serbian_dinar_sr.__str__() == 'RSD 10,00.00000'


    def test_serbian_dinar_sr_changed(self):
        """test_cserbian_dinar_sr_changed."""
        serbian_dinar_sr = SerbianDinarSR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            serbian_dinar_sr.international = True


    def test_serbian_dinar_sr_math_add(self):
        """test_serbian_dinar_sr_math_add."""
        serbian_dinar_sr_one = SerbianDinarSR(amount=1)
        serbian_dinar_sr_two = SerbianDinarSR(amount=2)
        serbian_dinar_sr_three = SerbianDinarSR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RSD and OTHER.'):
            _ = serbian_dinar_sr_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.SerbianDinarSR\'> '
                    'and <class \'str\'>.')):
            _ = serbian_dinar_sr_one.__add__('1.00')
        assert (
            serbian_dinar_sr_one +
            serbian_dinar_sr_two) == serbian_dinar_sr_three


    def test_serbian_dinar_sr_slots(self):
        """test_serbian_dinar_sr_slots."""
        serbian_dinar_sr = SerbianDinarSR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SerbianDinarSR\' '
                    'object has no attribute \'new_variable\'')):
            serbian_dinar_sr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Tunisian Dinar representation."""

from multicurrency import TunisianDinar


class TestTunisianDinar:

    def test_tunisian_dinar(self):
        """test_tunisian_dinar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        tunisian_dinar = TunisianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tunisian_dinar.amount == decimal
        assert tunisian_dinar.numeric_code == '788'
        assert tunisian_dinar.alpha_code == 'TND'
        assert tunisian_dinar.decimal_places == 3
        assert tunisian_dinar.decimal_sign == ','
        assert tunisian_dinar.grouping_places == 3
        assert tunisian_dinar.grouping_sign == '.'
        assert not tunisian_dinar.international
        assert tunisian_dinar.symbol == 'د.ت.'
        assert tunisian_dinar.symbol_ahead
        assert tunisian_dinar.symbol_separator == '\u00A0'
        assert tunisian_dinar.localized_symbol == 'د.ت.'
        assert tunisian_dinar.convertion == ''
        assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
        assert tunisian_dinar.__repr__() == (
            'TunisianDinar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TND", '
            'symbol: "د.ت.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ت.", '
            'numeric_code: "788", '
            'decimal_places: "3", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert tunisian_dinar.__str__() == 'د.ت. 0,143'


    def test_tunisian_dinar_negative(self):
        """test_tunisian_dinar_negative."""
        amount = -100
        tunisian_dinar = TunisianDinar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tunisian_dinar.numeric_code == '788'
        assert tunisian_dinar.alpha_code == 'TND'
        assert tunisian_dinar.decimal_places == 3
        assert tunisian_dinar.decimal_sign == ','
        assert tunisian_dinar.grouping_places == 3
        assert tunisian_dinar.grouping_sign == '.'
        assert not tunisian_dinar.international
        assert tunisian_dinar.symbol == 'د.ت.'
        assert tunisian_dinar.symbol_ahead
        assert tunisian_dinar.symbol_separator == '\u00A0'
        assert tunisian_dinar.localized_symbol == 'د.ت.'
        assert tunisian_dinar.convertion == ''
        assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
        assert tunisian_dinar.__repr__() == (
            'TunisianDinar(amount: -100, '
            'alpha_code: "TND", '
            'symbol: "د.ت.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.ت.", '
            'numeric_code: "788", '
            'decimal_places: "3", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert tunisian_dinar.__str__() == 'د.ت. -100,000'


    def test_tunisian_dinar_custom(self):
        """test_tunisian_dinar_custom."""
        amount = 1000
        tunisian_dinar = TunisianDinar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert tunisian_dinar.amount == decimal
        assert tunisian_dinar.numeric_code == '788'
        assert tunisian_dinar.alpha_code == 'TND'
        assert tunisian_dinar.decimal_places == 5
        assert tunisian_dinar.decimal_sign == '.'
        assert tunisian_dinar.grouping_places == 2
        assert tunisian_dinar.grouping_sign == ','
        assert tunisian_dinar.international
        assert tunisian_dinar.symbol == 'د.ت.'
        assert not tunisian_dinar.symbol_ahead
        assert tunisian_dinar.symbol_separator == '_'
        assert tunisian_dinar.localized_symbol == 'د.ت.'
        assert tunisian_dinar.convertion == ''
        assert tunisian_dinar.__hash__() == hash((decimal, 'TND', '788'))
        assert tunisian_dinar.__repr__() == (
            'TunisianDinar(amount: 1000, '
            'alpha_code: "TND", '
            'symbol: "د.ت.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.ت.", '
            'numeric_code: "788", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert tunisian_dinar.__str__() == 'TND 10,00.00000'


    def test_tunisian_dinar_changed(self):
        """test_ctunisian_dinar_changed."""
        tunisian_dinar = TunisianDinar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tunisian_dinar.international = True


    def test_tunisian_dinar_math_add(self):
        """test_tunisian_dinar_math_add."""
        tunisian_dinar_one = TunisianDinar(amount=1)
        tunisian_dinar_two = TunisianDinar(amount=2)
        tunisian_dinar_three = TunisianDinar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TND and OTHER.'):
            _ = tunisian_dinar_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'dinar.TunisianDinar\'> '
                    'and <class \'str\'>.')):
            _ = tunisian_dinar_one.__add__('1.00')
        assert (
            tunisian_dinar_one +
            tunisian_dinar_two) == tunisian_dinar_three


    def test_tunisian_dinar_slots(self):
        """test_tunisian_dinar_slots."""
        tunisian_dinar = TunisianDinar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TunisianDinar\' '
                    'object has no attribute \'new_variable\'')):
            tunisian_dinar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
