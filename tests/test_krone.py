# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Krone currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Danish Krone representation."""

from multicurrency import DanishKrone


class TestDanishKrone:
    """DanishKrone currency tests."""

    def test_danish_krone(self):
        """test_danish_krone."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        danish_krone = DanishKrone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert danish_krone.amount == decimal
        assert danish_krone.numeric_code == '208'
        assert danish_krone.alpha_code == 'DKK'
        assert danish_krone.decimal_places == 2
        assert danish_krone.decimal_sign == ','
        assert danish_krone.grouping_places == 3
        assert danish_krone.grouping_sign == '.'
        assert not danish_krone.international
        assert danish_krone.symbol == 'kr'
        assert not danish_krone.symbol_ahead
        assert danish_krone.symbol_separator == '\u00A0'
        assert danish_krone.localized_symbol == 'kr'
        assert danish_krone.convertion == ''
        assert danish_krone.__hash__() == hash(
            (danish_krone.__class__, decimal, 'DKK', '208'))
        assert danish_krone.__repr__() == (
            'DanishKrone(amount: 0.1428571428571428571428571429, '
            'alpha_code: "DKK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "208", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert danish_krone.__str__() == '0,14 kr'

    def test_danish_krone_negative(self):
        """test_danish_krone_negative."""
        amount = -100
        danish_krone = DanishKrone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert danish_krone.numeric_code == '208'
        assert danish_krone.alpha_code == 'DKK'
        assert danish_krone.decimal_places == 2
        assert danish_krone.decimal_sign == ','
        assert danish_krone.grouping_places == 3
        assert danish_krone.grouping_sign == '.'
        assert not danish_krone.international
        assert danish_krone.symbol == 'kr'
        assert not danish_krone.symbol_ahead
        assert danish_krone.symbol_separator == '\u00A0'
        assert danish_krone.localized_symbol == 'kr'
        assert danish_krone.convertion == ''
        assert danish_krone.__hash__() == hash(
            (danish_krone.__class__, decimal, 'DKK', '208'))
        assert danish_krone.__repr__() == (
            'DanishKrone(amount: -100, '
            'alpha_code: "DKK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "208", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert danish_krone.__str__() == '-100,00 kr'

    def test_danish_krone_custom(self):
        """test_danish_krone_custom."""
        amount = 1000
        danish_krone = DanishKrone(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert danish_krone.amount == decimal
        assert danish_krone.numeric_code == '208'
        assert danish_krone.alpha_code == 'DKK'
        assert danish_krone.decimal_places == 5
        assert danish_krone.decimal_sign == '.'
        assert danish_krone.grouping_places == 2
        assert danish_krone.grouping_sign == ','
        assert danish_krone.international
        assert danish_krone.symbol == 'kr'
        assert not danish_krone.symbol_ahead
        assert danish_krone.symbol_separator == '_'
        assert danish_krone.localized_symbol == 'kr'
        assert danish_krone.convertion == ''
        assert danish_krone.__hash__() == hash(
            (danish_krone.__class__, decimal, 'DKK', '208'))
        assert danish_krone.__repr__() == (
            'DanishKrone(amount: 1000, '
            'alpha_code: "DKK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "kr", '
            'numeric_code: "208", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert danish_krone.__str__() == 'DKK 10,00.00000'

    def test_danish_krone_changed(self):
        """test_cdanish_krone_changed."""
        danish_krone = DanishKrone(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            danish_krone.international = True

    def test_danish_krone_math_add(self):
        """test_danish_krone_math_add."""
        danish_krone_one = DanishKrone(amount=1)
        danish_krone_two = DanishKrone(amount=2)
        danish_krone_three = DanishKrone(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency DKK and OTHER.'):
            _ = danish_krone_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'krone.DanishKrone\'> '
                    'and <class \'str\'>.')):
            _ = danish_krone_one.__add__('1.00')
        assert (
            danish_krone_one +
            danish_krone_two) == danish_krone_three

    def test_danish_krone_slots(self):
        """test_danish_krone_slots."""
        danish_krone = DanishKrone(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'DanishKrone\' '
                    'object has no attribute \'new_variable\'')):
            danish_krone.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Norwegian Krone representation."""

from multicurrency import NorwegianKrone


class TestNorwegianKrone:
    """NorwegianKrone currency tests."""

    def test_norwegian_krone(self):
        """test_norwegian_krone."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        norwegian_krone = NorwegianKrone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert norwegian_krone.amount == decimal
        assert norwegian_krone.numeric_code == '578'
        assert norwegian_krone.alpha_code == 'NOK'
        assert norwegian_krone.decimal_places == 2
        assert norwegian_krone.decimal_sign == ','
        assert norwegian_krone.grouping_places == 3
        assert norwegian_krone.grouping_sign == '\u202F'
        assert not norwegian_krone.international
        assert norwegian_krone.symbol == 'kr'
        assert norwegian_krone.symbol_ahead
        assert norwegian_krone.symbol_separator == '\u00A0'
        assert norwegian_krone.localized_symbol == 'kr'
        assert norwegian_krone.convertion == ''
        assert norwegian_krone.__hash__() == hash(
            (norwegian_krone.__class__, decimal, 'NOK', '578'))
        assert norwegian_krone.__repr__() == (
            'NorwegianKrone(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NOK", '
            'symbol: "kr", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "578", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert norwegian_krone.__str__() == 'kr 0,14'

    def test_norwegian_krone_negative(self):
        """test_norwegian_krone_negative."""
        amount = -100
        norwegian_krone = NorwegianKrone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert norwegian_krone.numeric_code == '578'
        assert norwegian_krone.alpha_code == 'NOK'
        assert norwegian_krone.decimal_places == 2
        assert norwegian_krone.decimal_sign == ','
        assert norwegian_krone.grouping_places == 3
        assert norwegian_krone.grouping_sign == '\u202F'
        assert not norwegian_krone.international
        assert norwegian_krone.symbol == 'kr'
        assert norwegian_krone.symbol_ahead
        assert norwegian_krone.symbol_separator == '\u00A0'
        assert norwegian_krone.localized_symbol == 'kr'
        assert norwegian_krone.convertion == ''
        assert norwegian_krone.__hash__() == hash(
            (norwegian_krone.__class__, decimal, 'NOK', '578'))
        assert norwegian_krone.__repr__() == (
            'NorwegianKrone(amount: -100, '
            'alpha_code: "NOK", '
            'symbol: "kr", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "578", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert norwegian_krone.__str__() == 'kr -100,00'

    def test_norwegian_krone_custom(self):
        """test_norwegian_krone_custom."""
        amount = 1000
        norwegian_krone = NorwegianKrone(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert norwegian_krone.amount == decimal
        assert norwegian_krone.numeric_code == '578'
        assert norwegian_krone.alpha_code == 'NOK'
        assert norwegian_krone.decimal_places == 5
        assert norwegian_krone.decimal_sign == '\u202F'
        assert norwegian_krone.grouping_places == 2
        assert norwegian_krone.grouping_sign == ','
        assert norwegian_krone.international
        assert norwegian_krone.symbol == 'kr'
        assert not norwegian_krone.symbol_ahead
        assert norwegian_krone.symbol_separator == '_'
        assert norwegian_krone.localized_symbol == 'kr'
        assert norwegian_krone.convertion == ''
        assert norwegian_krone.__hash__() == hash(
            (norwegian_krone.__class__, decimal, 'NOK', '578'))
        assert norwegian_krone.__repr__() == (
            'NorwegianKrone(amount: 1000, '
            'alpha_code: "NOK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "kr", '
            'numeric_code: "578", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert norwegian_krone.__str__() == 'NOK 10,00.00000'

    def test_norwegian_krone_changed(self):
        """test_cnorwegian_krone_changed."""
        norwegian_krone = NorwegianKrone(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            norwegian_krone.international = True

    def test_norwegian_krone_math_add(self):
        """test_norwegian_krone_math_add."""
        norwegian_krone_one = NorwegianKrone(amount=1)
        norwegian_krone_two = NorwegianKrone(amount=2)
        norwegian_krone_three = NorwegianKrone(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NOK and OTHER.'):
            _ = norwegian_krone_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'krone.NorwegianKrone\'> '
                    'and <class \'str\'>.')):
            _ = norwegian_krone_one.__add__('1.00')
        assert (
            norwegian_krone_one +
            norwegian_krone_two) == norwegian_krone_three

    def test_norwegian_krone_slots(self):
        """test_norwegian_krone_slots."""
        norwegian_krone = NorwegianKrone(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NorwegianKrone\' '
                    'object has no attribute \'new_variable\'')):
            norwegian_krone.new_variable = 'fail'  # pylint: disable=assigning-non-slot
