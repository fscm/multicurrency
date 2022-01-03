# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Riyal currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Saudi Riyal representation."""

from multicurrency import SaudiRiyal


class TestSaudiRiyal:
    """SaudiRiyal currency tests."""

    def test_saudi_riyal(self):
        """test_saudi_riyal."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        saudi_riyal = SaudiRiyal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert saudi_riyal.amount == decimal
        assert saudi_riyal.numeric_code == '682'
        assert saudi_riyal.alpha_code == 'SAR'
        assert saudi_riyal.decimal_places == 2
        assert saudi_riyal.decimal_sign == '\u066B'
        assert saudi_riyal.grouping_places == 3
        assert saudi_riyal.grouping_sign == '\u066C'
        assert not saudi_riyal.international
        assert saudi_riyal.symbol == 'ر.س.'
        assert saudi_riyal.symbol_ahead
        assert saudi_riyal.symbol_separator == '\u00A0'
        assert saudi_riyal.localized_symbol == 'ر.س.'
        assert saudi_riyal.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert saudi_riyal.__hash__() == hash(
            (saudi_riyal.__class__, decimal, 'SAR', '682'))
        assert saudi_riyal.__repr__() == (
            'SaudiRiyal(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SAR", '
            'symbol: "ر.س.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.س.", '
            'numeric_code: "682", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert saudi_riyal.__str__() == 'ر.س. ٠٫١٤'

    def test_saudi_riyal_negative(self):
        """test_saudi_riyal_negative."""
        amount = -100
        saudi_riyal = SaudiRiyal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert saudi_riyal.numeric_code == '682'
        assert saudi_riyal.alpha_code == 'SAR'
        assert saudi_riyal.decimal_places == 2
        assert saudi_riyal.decimal_sign == '\u066B'
        assert saudi_riyal.grouping_places == 3
        assert saudi_riyal.grouping_sign == '\u066C'
        assert not saudi_riyal.international
        assert saudi_riyal.symbol == 'ر.س.'
        assert saudi_riyal.symbol_ahead
        assert saudi_riyal.symbol_separator == '\u00A0'
        assert saudi_riyal.localized_symbol == 'ر.س.'
        assert saudi_riyal.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert saudi_riyal.__hash__() == hash(
            (saudi_riyal.__class__, decimal, 'SAR', '682'))
        assert saudi_riyal.__repr__() == (
            'SaudiRiyal(amount: -100, '
            'alpha_code: "SAR", '
            'symbol: "ر.س.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.س.", '
            'numeric_code: "682", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert saudi_riyal.__str__() == 'ر.س. -١٠٠٫٠٠'

    def test_saudi_riyal_custom(self):
        """test_saudi_riyal_custom."""
        amount = 1000
        saudi_riyal = SaudiRiyal(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert saudi_riyal.amount == decimal
        assert saudi_riyal.numeric_code == '682'
        assert saudi_riyal.alpha_code == 'SAR'
        assert saudi_riyal.decimal_places == 5
        assert saudi_riyal.decimal_sign == '\u066C'
        assert saudi_riyal.grouping_places == 2
        assert saudi_riyal.grouping_sign == '\u066B'
        assert saudi_riyal.international
        assert saudi_riyal.symbol == 'ر.س.'
        assert not saudi_riyal.symbol_ahead
        assert saudi_riyal.symbol_separator == '_'
        assert saudi_riyal.localized_symbol == 'ر.س.'
        assert saudi_riyal.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert saudi_riyal.__hash__() == hash(
            (saudi_riyal.__class__, decimal, 'SAR', '682'))
        assert saudi_riyal.__repr__() == (
            'SaudiRiyal(amount: 1000, '
            'alpha_code: "SAR", '
            'symbol: "ر.س.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ر.س.", '
            'numeric_code: "682", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert saudi_riyal.__str__() == 'SAR 10,00.00000'

    def test_saudi_riyal_changed(self):
        """test_csaudi_riyal_changed."""
        saudi_riyal = SaudiRiyal(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saudi_riyal.international = True

    def test_saudi_riyal_math_add(self):
        """test_saudi_riyal_math_add."""
        saudi_riyal_one = SaudiRiyal(amount=1)
        saudi_riyal_two = SaudiRiyal(amount=2)
        saudi_riyal_three = SaudiRiyal(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SAR and OTHER.'):
            _ = saudi_riyal_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'riyal.SaudiRiyal\'> '
                    'and <class \'str\'>.')):
            _ = saudi_riyal_one.__add__('1.00')
        assert (
            saudi_riyal_one +
            saudi_riyal_two) == saudi_riyal_three

    def test_saudi_riyal_slots(self):
        """test_saudi_riyal_slots."""
        saudi_riyal = SaudiRiyal(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SaudiRiyal\' '
                    'object has no attribute \'new_variable\'')):
            saudi_riyal.new_variable = 'fail'  # pylint: disable=assigning-non-slot
