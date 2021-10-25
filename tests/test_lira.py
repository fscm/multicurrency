# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lira currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Turkish Lira representation."""

from multicurrency import TurkishLira


class TestTurkishLira:

    def test_turkish_lira(self):
        """test_turkish_lira."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        turkish_lira = TurkishLira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira.amount == decimal
        assert turkish_lira.numeric_code == '949'
        assert turkish_lira.alpha_code == 'TRY'
        assert turkish_lira.decimal_places == 2
        assert turkish_lira.decimal_sign == ','
        assert turkish_lira.grouping_places == 3
        assert turkish_lira.grouping_sign == '.'
        assert not turkish_lira.international
        assert turkish_lira.symbol == '₤'
        assert turkish_lira.symbol_ahead
        assert turkish_lira.symbol_separator == ''
        assert turkish_lira.localized_symbol == '₤'
        assert turkish_lira.convertion == ''
        assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira.__repr__() == (
            'TurkishLira(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira.__str__() == '₤0,14'


    def test_turkish_lira_negative(self):
        """test_turkish_lira_negative."""
        amount = -100
        turkish_lira = TurkishLira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira.numeric_code == '949'
        assert turkish_lira.alpha_code == 'TRY'
        assert turkish_lira.decimal_places == 2
        assert turkish_lira.decimal_sign == ','
        assert turkish_lira.grouping_places == 3
        assert turkish_lira.grouping_sign == '.'
        assert not turkish_lira.international
        assert turkish_lira.symbol == '₤'
        assert turkish_lira.symbol_ahead
        assert turkish_lira.symbol_separator == ''
        assert turkish_lira.localized_symbol == '₤'
        assert turkish_lira.convertion == ''
        assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira.__repr__() == (
            'TurkishLira(amount: -100, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira.__str__() == '₤-100,00'


    def test_turkish_lira_custom(self):
        """test_turkish_lira_custom."""
        amount = 1000
        turkish_lira = TurkishLira(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira.amount == decimal
        assert turkish_lira.numeric_code == '949'
        assert turkish_lira.alpha_code == 'TRY'
        assert turkish_lira.decimal_places == 5
        assert turkish_lira.decimal_sign == '.'
        assert turkish_lira.grouping_places == 2
        assert turkish_lira.grouping_sign == ','
        assert turkish_lira.international
        assert turkish_lira.symbol == '₤'
        assert not turkish_lira.symbol_ahead
        assert turkish_lira.symbol_separator == '_'
        assert turkish_lira.localized_symbol == '₤'
        assert turkish_lira.convertion == ''
        assert turkish_lira.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira.__repr__() == (
            'TurkishLira(amount: 1000, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₤", '
            'numeric_code: "949", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert turkish_lira.__str__() == 'TRY 10,00.00000'


    def test_turkish_lira_changed(self):
        """test_cturkish_lira_changed."""
        turkish_lira = TurkishLira(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira.international = True


    def test_turkish_lira_math_add(self):
        """test_turkish_lira_math_add."""
        turkish_lira_one = TurkishLira(amount=1)
        turkish_lira_two = TurkishLira(amount=2)
        turkish_lira_three = TurkishLira(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TRY and OTHER.'):
            _ = turkish_lira_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'lira.TurkishLira\'> '
                    'and <class \'str\'>.')):
            _ = turkish_lira_one.__add__('1.00')
        assert (
            turkish_lira_one +
            turkish_lira_two) == turkish_lira_three


    def test_turkish_lira_slots(self):
        """test_turkish_lira_slots."""
        turkish_lira = TurkishLira(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TurkishLira\' '
                    'object has no attribute \'new_variable\'')):
            turkish_lira.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Turkish Lira CY representation."""

from multicurrency import TurkishLiraCY


class TestTurkishLiraCY:

    def test_turkish_lira_cy(self):
        """test_turkish_lira_cy."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        turkish_lira_cy = TurkishLiraCY(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_cy.amount == decimal
        assert turkish_lira_cy.numeric_code == '949'
        assert turkish_lira_cy.alpha_code == 'TRY'
        assert turkish_lira_cy.decimal_places == 2
        assert turkish_lira_cy.decimal_sign == ','
        assert turkish_lira_cy.grouping_places == 3
        assert turkish_lira_cy.grouping_sign == '.'
        assert not turkish_lira_cy.international
        assert turkish_lira_cy.symbol == '₤'
        assert turkish_lira_cy.symbol_ahead
        assert turkish_lira_cy.symbol_separator == ''
        assert turkish_lira_cy.localized_symbol == 'CY₤'
        assert turkish_lira_cy.convertion == ''
        assert turkish_lira_cy.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_cy.__repr__() == (
            'TurkishLiraCY(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CY₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira_cy.__str__() == '₤0,14'


    def test_turkish_lira_cy_negative(self):
        """test_turkish_lira_cy_negative."""
        amount = -100
        turkish_lira_cy = TurkishLiraCY(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_cy.numeric_code == '949'
        assert turkish_lira_cy.alpha_code == 'TRY'
        assert turkish_lira_cy.decimal_places == 2
        assert turkish_lira_cy.decimal_sign == ','
        assert turkish_lira_cy.grouping_places == 3
        assert turkish_lira_cy.grouping_sign == '.'
        assert not turkish_lira_cy.international
        assert turkish_lira_cy.symbol == '₤'
        assert turkish_lira_cy.symbol_ahead
        assert turkish_lira_cy.symbol_separator == ''
        assert turkish_lira_cy.localized_symbol == 'CY₤'
        assert turkish_lira_cy.convertion == ''
        assert turkish_lira_cy.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_cy.__repr__() == (
            'TurkishLiraCY(amount: -100, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CY₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira_cy.__str__() == '₤-100,00'


    def test_turkish_lira_cy_custom(self):
        """test_turkish_lira_cy_custom."""
        amount = 1000
        turkish_lira_cy = TurkishLiraCY(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_cy.amount == decimal
        assert turkish_lira_cy.numeric_code == '949'
        assert turkish_lira_cy.alpha_code == 'TRY'
        assert turkish_lira_cy.decimal_places == 5
        assert turkish_lira_cy.decimal_sign == '.'
        assert turkish_lira_cy.grouping_places == 2
        assert turkish_lira_cy.grouping_sign == ','
        assert turkish_lira_cy.international
        assert turkish_lira_cy.symbol == '₤'
        assert not turkish_lira_cy.symbol_ahead
        assert turkish_lira_cy.symbol_separator == '_'
        assert turkish_lira_cy.localized_symbol == 'CY₤'
        assert turkish_lira_cy.convertion == ''
        assert turkish_lira_cy.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_cy.__repr__() == (
            'TurkishLiraCY(amount: 1000, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CY₤", '
            'numeric_code: "949", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert turkish_lira_cy.__str__() == 'TRY 10,00.00000'


    def test_turkish_lira_cy_changed(self):
        """test_cturkish_lira_cy_changed."""
        turkish_lira_cy = TurkishLiraCY(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_cy.international = True


    def test_turkish_lira_cy_math_add(self):
        """test_turkish_lira_cy_math_add."""
        turkish_lira_cy_one = TurkishLiraCY(amount=1)
        turkish_lira_cy_two = TurkishLiraCY(amount=2)
        turkish_lira_cy_three = TurkishLiraCY(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TRY and OTHER.'):
            _ = turkish_lira_cy_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'lira.TurkishLiraCY\'> '
                    'and <class \'str\'>.')):
            _ = turkish_lira_cy_one.__add__('1.00')
        assert (
            turkish_lira_cy_one +
            turkish_lira_cy_two) == turkish_lira_cy_three


    def test_turkish_lira_cy_slots(self):
        """test_turkish_lira_cy_slots."""
        turkish_lira_cy = TurkishLiraCY(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TurkishLiraCY\' '
                    'object has no attribute \'new_variable\'')):
            turkish_lira_cy.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Turkish Lira TR representation."""

from multicurrency import TurkishLiraTR


class TestTurkishLiraTR:

    def test_turkish_lira_tr(self):
        """test_turkish_lira_tr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        turkish_lira_tr = TurkishLiraTR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_tr.amount == decimal
        assert turkish_lira_tr.numeric_code == '949'
        assert turkish_lira_tr.alpha_code == 'TRY'
        assert turkish_lira_tr.decimal_places == 2
        assert turkish_lira_tr.decimal_sign == ','
        assert turkish_lira_tr.grouping_places == 3
        assert turkish_lira_tr.grouping_sign == '.'
        assert not turkish_lira_tr.international
        assert turkish_lira_tr.symbol == '₤'
        assert turkish_lira_tr.symbol_ahead
        assert turkish_lira_tr.symbol_separator == ''
        assert turkish_lira_tr.localized_symbol == 'TR₤'
        assert turkish_lira_tr.convertion == ''
        assert turkish_lira_tr.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_tr.__repr__() == (
            'TurkishLiraTR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TR₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira_tr.__str__() == '₤0,14'


    def test_turkish_lira_tr_negative(self):
        """test_turkish_lira_tr_negative."""
        amount = -100
        turkish_lira_tr = TurkishLiraTR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_tr.numeric_code == '949'
        assert turkish_lira_tr.alpha_code == 'TRY'
        assert turkish_lira_tr.decimal_places == 2
        assert turkish_lira_tr.decimal_sign == ','
        assert turkish_lira_tr.grouping_places == 3
        assert turkish_lira_tr.grouping_sign == '.'
        assert not turkish_lira_tr.international
        assert turkish_lira_tr.symbol == '₤'
        assert turkish_lira_tr.symbol_ahead
        assert turkish_lira_tr.symbol_separator == ''
        assert turkish_lira_tr.localized_symbol == 'TR₤'
        assert turkish_lira_tr.convertion == ''
        assert turkish_lira_tr.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_tr.__repr__() == (
            'TurkishLiraTR(amount: -100, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TR₤", '
            'numeric_code: "949", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert turkish_lira_tr.__str__() == '₤-100,00'


    def test_turkish_lira_tr_custom(self):
        """test_turkish_lira_tr_custom."""
        amount = 1000
        turkish_lira_tr = TurkishLiraTR(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert turkish_lira_tr.amount == decimal
        assert turkish_lira_tr.numeric_code == '949'
        assert turkish_lira_tr.alpha_code == 'TRY'
        assert turkish_lira_tr.decimal_places == 5
        assert turkish_lira_tr.decimal_sign == '.'
        assert turkish_lira_tr.grouping_places == 2
        assert turkish_lira_tr.grouping_sign == ','
        assert turkish_lira_tr.international
        assert turkish_lira_tr.symbol == '₤'
        assert not turkish_lira_tr.symbol_ahead
        assert turkish_lira_tr.symbol_separator == '_'
        assert turkish_lira_tr.localized_symbol == 'TR₤'
        assert turkish_lira_tr.convertion == ''
        assert turkish_lira_tr.__hash__() == hash((decimal, 'TRY', '949'))
        assert turkish_lira_tr.__repr__() == (
            'TurkishLiraTR(amount: 1000, '
            'alpha_code: "TRY", '
            'symbol: "₤", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TR₤", '
            'numeric_code: "949", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert turkish_lira_tr.__str__() == 'TRY 10,00.00000'


    def test_turkish_lira_tr_changed(self):
        """test_cturkish_lira_tr_changed."""
        turkish_lira_tr = TurkishLiraTR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            turkish_lira_tr.international = True


    def test_turkish_lira_tr_math_add(self):
        """test_turkish_lira_tr_math_add."""
        turkish_lira_tr_one = TurkishLiraTR(amount=1)
        turkish_lira_tr_two = TurkishLiraTR(amount=2)
        turkish_lira_tr_three = TurkishLiraTR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TRY and OTHER.'):
            _ = turkish_lira_tr_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'lira.TurkishLiraTR\'> '
                    'and <class \'str\'>.')):
            _ = turkish_lira_tr_one.__add__('1.00')
        assert (
            turkish_lira_tr_one +
            turkish_lira_tr_two) == turkish_lira_tr_three


    def test_turkish_lira_tr_slots(self):
        """test_turkish_lira_tr_slots."""
        turkish_lira_tr = TurkishLiraTR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TurkishLiraTR\' '
                    'object has no attribute \'new_variable\'')):
            turkish_lira_tr.new_variable = 'fail'  # pylint: disable=assigning-non-slot
