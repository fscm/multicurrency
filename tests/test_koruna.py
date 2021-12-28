# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Koruna currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Czech Koruna representation."""

from multicurrency import CzechKoruna


class TestCzechKoruna:
    """CzechKoruna currency tests."""

    def test_czech_koruna(self):
        """test_czech_koruna."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        czech_koruna = CzechKoruna(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert czech_koruna.amount == decimal
        assert czech_koruna.numeric_code == '203'
        assert czech_koruna.alpha_code == 'CZK'
        assert czech_koruna.decimal_places == 2
        assert czech_koruna.decimal_sign == ','
        assert czech_koruna.grouping_places == 3
        assert czech_koruna.grouping_sign == '\u202F'
        assert not czech_koruna.international
        assert czech_koruna.symbol == 'Kč'
        assert not czech_koruna.symbol_ahead
        assert czech_koruna.symbol_separator == '\u00A0'
        assert czech_koruna.localized_symbol == 'Kč'
        assert czech_koruna.convertion == ''
        assert czech_koruna.__hash__() == hash(
            (czech_koruna.__class__, decimal, 'CZK', '203'))
        assert czech_koruna.__repr__() == (
            'CzechKoruna(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CZK", '
            'symbol: "Kč", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kč", '
            'numeric_code: "203", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert czech_koruna.__str__() == '0,14 Kč'

    def test_czech_koruna_negative(self):
        """test_czech_koruna_negative."""
        amount = -100
        czech_koruna = CzechKoruna(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert czech_koruna.numeric_code == '203'
        assert czech_koruna.alpha_code == 'CZK'
        assert czech_koruna.decimal_places == 2
        assert czech_koruna.decimal_sign == ','
        assert czech_koruna.grouping_places == 3
        assert czech_koruna.grouping_sign == '\u202F'
        assert not czech_koruna.international
        assert czech_koruna.symbol == 'Kč'
        assert not czech_koruna.symbol_ahead
        assert czech_koruna.symbol_separator == '\u00A0'
        assert czech_koruna.localized_symbol == 'Kč'
        assert czech_koruna.convertion == ''
        assert czech_koruna.__hash__() == hash(
            (czech_koruna.__class__, decimal, 'CZK', '203'))
        assert czech_koruna.__repr__() == (
            'CzechKoruna(amount: -100, '
            'alpha_code: "CZK", '
            'symbol: "Kč", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kč", '
            'numeric_code: "203", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert czech_koruna.__str__() == '-100,00 Kč'

    def test_czech_koruna_custom(self):
        """test_czech_koruna_custom."""
        amount = 1000
        czech_koruna = CzechKoruna(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert czech_koruna.amount == decimal
        assert czech_koruna.numeric_code == '203'
        assert czech_koruna.alpha_code == 'CZK'
        assert czech_koruna.decimal_places == 5
        assert czech_koruna.decimal_sign == '\u202F'
        assert czech_koruna.grouping_places == 2
        assert czech_koruna.grouping_sign == ','
        assert czech_koruna.international
        assert czech_koruna.symbol == 'Kč'
        assert not czech_koruna.symbol_ahead
        assert czech_koruna.symbol_separator == '_'
        assert czech_koruna.localized_symbol == 'Kč'
        assert czech_koruna.convertion == ''
        assert czech_koruna.__hash__() == hash(
            (czech_koruna.__class__, decimal, 'CZK', '203'))
        assert czech_koruna.__repr__() == (
            'CzechKoruna(amount: 1000, '
            'alpha_code: "CZK", '
            'symbol: "Kč", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Kč", '
            'numeric_code: "203", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert czech_koruna.__str__() == 'CZK 10,00.00000'

    def test_czech_koruna_changed(self):
        """test_cczech_koruna_changed."""
        czech_koruna = CzechKoruna(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            czech_koruna.international = True

    def test_czech_koruna_math_add(self):
        """test_czech_koruna_math_add."""
        czech_koruna_one = CzechKoruna(amount=1)
        czech_koruna_two = CzechKoruna(amount=2)
        czech_koruna_three = CzechKoruna(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CZK and OTHER.'):
            _ = czech_koruna_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'koruna.CzechKoruna\'> '
                    'and <class \'str\'>.')):
            _ = czech_koruna_one.__add__('1.00')
        assert (
            czech_koruna_one +
            czech_koruna_two) == czech_koruna_three

    def test_czech_koruna_slots(self):
        """test_czech_koruna_slots."""
        czech_koruna = CzechKoruna(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CzechKoruna\' '
                    'object has no attribute \'new_variable\'')):
            czech_koruna.new_variable = 'fail'  # pylint: disable=assigning-non-slot
