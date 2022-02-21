# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ngultrum currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Ngultrum


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Ngultrum representation."""


class TestNgultrum:
    """Ngultrum currency tests."""

    def test_ngultrum(self):
        """test_ngultrum."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        ngultrum = Ngultrum(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ngultrum.amount == decimal
        assert ngultrum.numeric_code == '064'
        assert ngultrum.alpha_code == 'BTN'
        assert ngultrum.decimal_places == 2
        assert ngultrum.decimal_sign == '.'
        assert ngultrum.grouping_places == 3
        assert ngultrum.grouping_sign == ','
        assert not ngultrum.international
        assert ngultrum.symbol == 'Nu.'
        assert ngultrum.symbol_ahead
        assert ngultrum.symbol_separator == '\u00A0'
        assert ngultrum.localized_symbol == 'Nu.'
        assert ngultrum.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert ngultrum.__hash__() == hash(
            (ngultrum.__class__, decimal, 'BTN', '064'))
        assert ngultrum.__repr__() == (
            'Ngultrum(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BTN", '
            'symbol: "Nu.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Nu.", '
            'numeric_code: "064", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "༠༡༢༣༤༥༦༧༨༩-", '
            'international: False)')
        assert ngultrum.__str__() == 'Nu. ༠.༡༤'

    def test_ngultrum_negative(self):
        """test_ngultrum_negative."""
        amount = -100
        ngultrum = Ngultrum(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ngultrum.numeric_code == '064'
        assert ngultrum.alpha_code == 'BTN'
        assert ngultrum.decimal_places == 2
        assert ngultrum.decimal_sign == '.'
        assert ngultrum.grouping_places == 3
        assert ngultrum.grouping_sign == ','
        assert not ngultrum.international
        assert ngultrum.symbol == 'Nu.'
        assert ngultrum.symbol_ahead
        assert ngultrum.symbol_separator == '\u00A0'
        assert ngultrum.localized_symbol == 'Nu.'
        assert ngultrum.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert ngultrum.__hash__() == hash(
            (ngultrum.__class__, decimal, 'BTN', '064'))
        assert ngultrum.__repr__() == (
            'Ngultrum(amount: -100, '
            'alpha_code: "BTN", '
            'symbol: "Nu.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Nu.", '
            'numeric_code: "064", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "༠༡༢༣༤༥༦༧༨༩-", '
            'international: False)')
        assert ngultrum.__str__() == 'Nu. -༡༠༠.༠༠'

    def test_ngultrum_custom(self):
        """test_ngultrum_custom."""
        amount = 1000
        ngultrum = Ngultrum(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert ngultrum.amount == decimal
        assert ngultrum.numeric_code == '064'
        assert ngultrum.alpha_code == 'BTN'
        assert ngultrum.decimal_places == 5
        assert ngultrum.decimal_sign == ','
        assert ngultrum.grouping_places == 2
        assert ngultrum.grouping_sign == '.'
        assert ngultrum.international
        assert ngultrum.symbol == 'Nu.'
        assert not ngultrum.symbol_ahead
        assert ngultrum.symbol_separator == '_'
        assert ngultrum.localized_symbol == 'Nu.'
        assert ngultrum.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert ngultrum.__hash__() == hash(
            (ngultrum.__class__, decimal, 'BTN', '064'))
        assert ngultrum.__repr__() == (
            'Ngultrum(amount: 1000, '
            'alpha_code: "BTN", '
            'symbol: "Nu.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Nu.", '
            'numeric_code: "064", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "༠༡༢༣༤༥༦༧༨༩-", '
            'international: True)')
        assert ngultrum.__str__() == 'BTN 10,00.00000'

    def test_ngultrum_changed(self):
        """test_cngultrum_changed."""
        ngultrum = Ngultrum(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ngultrum.international = True

    def test_ngultrum_math_add(self):
        """test_ngultrum_math_add."""
        ngultrum_one = Ngultrum(amount=1)
        ngultrum_two = Ngultrum(amount=2)
        ngultrum_three = Ngultrum(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BTN and OTHER.'):
            _ = ngultrum_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ngultrum.Ngultrum\'> '
                    'and <class \'str\'>.')):
            _ = ngultrum_one.__add__('1.00')
        assert (
            ngultrum_one +
            ngultrum_two) == ngultrum_three

    def test_ngultrum_slots(self):
        """test_ngultrum_slots."""
        ngultrum = Ngultrum(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Ngultrum\' '
                    'object has no attribute \'new_variable\'')):
            ngultrum.new_variable = 'fail'  # pylint: disable=assigning-non-slot
