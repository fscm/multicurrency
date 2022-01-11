# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dirham currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import (
    UAEDirham,
    MoroccanDirham)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the UAE Dirham representation."""


class TestUAEDirham:
    """UAEDirham currency tests."""

    def test_uae_dirham(self):
        """test_uae_dirham."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        uae_dirham = UAEDirham(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert uae_dirham.amount == decimal
        assert uae_dirham.numeric_code == '784'
        assert uae_dirham.alpha_code == 'AED'
        assert uae_dirham.decimal_places == 2
        assert uae_dirham.decimal_sign == '\u066B'
        assert uae_dirham.grouping_places == 3
        assert uae_dirham.grouping_sign == '\u066C'
        assert not uae_dirham.international
        assert uae_dirham.symbol == 'د.إ.'
        assert uae_dirham.symbol_ahead
        assert uae_dirham.symbol_separator == '\u00A0'
        assert uae_dirham.localized_symbol == 'د.إ.'
        assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert uae_dirham.__hash__() == hash(
            (uae_dirham.__class__, decimal, 'AED', '784'))
        assert uae_dirham.__repr__() == (
            'UAEDirham(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AED", '
            'symbol: "د.إ.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.إ.", '
            'numeric_code: "784", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert uae_dirham.__str__() == 'د.إ. ٠٫١٤'

    def test_uae_dirham_negative(self):
        """test_uae_dirham_negative."""
        amount = -100
        uae_dirham = UAEDirham(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert uae_dirham.numeric_code == '784'
        assert uae_dirham.alpha_code == 'AED'
        assert uae_dirham.decimal_places == 2
        assert uae_dirham.decimal_sign == '\u066B'
        assert uae_dirham.grouping_places == 3
        assert uae_dirham.grouping_sign == '\u066C'
        assert not uae_dirham.international
        assert uae_dirham.symbol == 'د.إ.'
        assert uae_dirham.symbol_ahead
        assert uae_dirham.symbol_separator == '\u00A0'
        assert uae_dirham.localized_symbol == 'د.إ.'
        assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert uae_dirham.__hash__() == hash(
            (uae_dirham.__class__, decimal, 'AED', '784'))
        assert uae_dirham.__repr__() == (
            'UAEDirham(amount: -100, '
            'alpha_code: "AED", '
            'symbol: "د.إ.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.إ.", '
            'numeric_code: "784", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert uae_dirham.__str__() == 'د.إ. -١٠٠٫٠٠'

    def test_uae_dirham_custom(self):
        """test_uae_dirham_custom."""
        amount = 1000
        uae_dirham = UAEDirham(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert uae_dirham.amount == decimal
        assert uae_dirham.numeric_code == '784'
        assert uae_dirham.alpha_code == 'AED'
        assert uae_dirham.decimal_places == 5
        assert uae_dirham.decimal_sign == '\u066C'
        assert uae_dirham.grouping_places == 2
        assert uae_dirham.grouping_sign == '\u066B'
        assert uae_dirham.international
        assert uae_dirham.symbol == 'د.إ.'
        assert not uae_dirham.symbol_ahead
        assert uae_dirham.symbol_separator == '_'
        assert uae_dirham.localized_symbol == 'د.إ.'
        assert uae_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert uae_dirham.__hash__() == hash(
            (uae_dirham.__class__, decimal, 'AED', '784'))
        assert uae_dirham.__repr__() == (
            'UAEDirham(amount: 1000, '
            'alpha_code: "AED", '
            'symbol: "د.إ.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.إ.", '
            'numeric_code: "784", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert uae_dirham.__str__() == 'AED 10,00.00000'

    def test_uae_dirham_changed(self):
        """test_cuae_dirham_changed."""
        uae_dirham = UAEDirham(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uae_dirham.international = True

    def test_uae_dirham_math_add(self):
        """test_uae_dirham_math_add."""
        uae_dirham_one = UAEDirham(amount=1)
        uae_dirham_two = UAEDirham(amount=2)
        uae_dirham_three = UAEDirham(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AED and OTHER.'):
            _ = uae_dirham_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dirham.UAEDirham\'> '
                    'and <class \'str\'>.')):
            _ = uae_dirham_one.__add__('1.00')
        assert (
            uae_dirham_one +
            uae_dirham_two) == uae_dirham_three

    def test_uae_dirham_slots(self):
        """test_uae_dirham_slots."""
        uae_dirham = UAEDirham(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'UAEDirham\' '
                    'object has no attribute \'new_variable\'')):
            uae_dirham.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Moroccan Dirham representation."""


class TestMoroccanDirham:
    """MoroccanDirham currency tests."""

    def test_moroccan_dirham(self):
        """test_moroccan_dirham."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        moroccan_dirham = MoroccanDirham(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert moroccan_dirham.amount == decimal
        assert moroccan_dirham.numeric_code == '504'
        assert moroccan_dirham.alpha_code == 'MAD'
        assert moroccan_dirham.decimal_places == 2
        assert moroccan_dirham.decimal_sign == '\u066B'
        assert moroccan_dirham.grouping_places == 3
        assert moroccan_dirham.grouping_sign == '\u066C'
        assert not moroccan_dirham.international
        assert moroccan_dirham.symbol == 'د.م.'
        assert moroccan_dirham.symbol_ahead
        assert moroccan_dirham.symbol_separator == '\u00A0'
        assert moroccan_dirham.localized_symbol == 'د.م.'
        assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert moroccan_dirham.__hash__() == hash(
            (moroccan_dirham.__class__, decimal, 'MAD', '504'))
        assert moroccan_dirham.__repr__() == (
            'MoroccanDirham(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MAD", '
            'symbol: "د.م.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.م.", '
            'numeric_code: "504", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert moroccan_dirham.__str__() == 'د.م. ٠٫١٤'

    def test_moroccan_dirham_negative(self):
        """test_moroccan_dirham_negative."""
        amount = -100
        moroccan_dirham = MoroccanDirham(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert moroccan_dirham.numeric_code == '504'
        assert moroccan_dirham.alpha_code == 'MAD'
        assert moroccan_dirham.decimal_places == 2
        assert moroccan_dirham.decimal_sign == '\u066B'
        assert moroccan_dirham.grouping_places == 3
        assert moroccan_dirham.grouping_sign == '\u066C'
        assert not moroccan_dirham.international
        assert moroccan_dirham.symbol == 'د.م.'
        assert moroccan_dirham.symbol_ahead
        assert moroccan_dirham.symbol_separator == '\u00A0'
        assert moroccan_dirham.localized_symbol == 'د.م.'
        assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert moroccan_dirham.__hash__() == hash(
            (moroccan_dirham.__class__, decimal, 'MAD', '504'))
        assert moroccan_dirham.__repr__() == (
            'MoroccanDirham(amount: -100, '
            'alpha_code: "MAD", '
            'symbol: "د.م.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "د.م.", '
            'numeric_code: "504", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert moroccan_dirham.__str__() == 'د.م. -١٠٠٫٠٠'

    def test_moroccan_dirham_custom(self):
        """test_moroccan_dirham_custom."""
        amount = 1000
        moroccan_dirham = MoroccanDirham(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert moroccan_dirham.amount == decimal
        assert moroccan_dirham.numeric_code == '504'
        assert moroccan_dirham.alpha_code == 'MAD'
        assert moroccan_dirham.decimal_places == 5
        assert moroccan_dirham.decimal_sign == '\u066C'
        assert moroccan_dirham.grouping_places == 2
        assert moroccan_dirham.grouping_sign == '\u066B'
        assert moroccan_dirham.international
        assert moroccan_dirham.symbol == 'د.م.'
        assert not moroccan_dirham.symbol_ahead
        assert moroccan_dirham.symbol_separator == '_'
        assert moroccan_dirham.localized_symbol == 'د.م.'
        assert moroccan_dirham.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert moroccan_dirham.__hash__() == hash(
            (moroccan_dirham.__class__, decimal, 'MAD', '504'))
        assert moroccan_dirham.__repr__() == (
            'MoroccanDirham(amount: 1000, '
            'alpha_code: "MAD", '
            'symbol: "د.م.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "د.م.", '
            'numeric_code: "504", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert moroccan_dirham.__str__() == 'MAD 10,00.00000'

    def test_moroccan_dirham_changed(self):
        """test_cmoroccan_dirham_changed."""
        moroccan_dirham = MoroccanDirham(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moroccan_dirham.international = True

    def test_moroccan_dirham_math_add(self):
        """test_moroccan_dirham_math_add."""
        moroccan_dirham_one = MoroccanDirham(amount=1)
        moroccan_dirham_two = MoroccanDirham(amount=2)
        moroccan_dirham_three = MoroccanDirham(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MAD and OTHER.'):
            _ = moroccan_dirham_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dirham.MoroccanDirham\'> '
                    'and <class \'str\'>.')):
            _ = moroccan_dirham_one.__add__('1.00')
        assert (
            moroccan_dirham_one +
            moroccan_dirham_two) == moroccan_dirham_three

    def test_moroccan_dirham_slots(self):
        """test_moroccan_dirham_slots."""
        moroccan_dirham = MoroccanDirham(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'MoroccanDirham\' '
                    'object has no attribute \'new_variable\'')):
            moroccan_dirham.new_variable = 'fail'  # pylint: disable=assigning-non-slot
