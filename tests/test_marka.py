# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Marka currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import KonvertibilnaMarka


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Konvertibilna Marka representation."""


class TestKonvertibilnaMarka:
    """KonvertibilnaMarka currency tests."""

    def test_konvertibilna_marka(self):
        """test_konvertibilna_marka."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        konvertibilna_marka = KonvertibilnaMarka(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert konvertibilna_marka.amount == decimal
        assert konvertibilna_marka.numeric_code == '977'
        assert konvertibilna_marka.alpha_code == 'BAM'
        assert konvertibilna_marka.decimal_places == 2
        assert konvertibilna_marka.decimal_sign == '.'
        assert konvertibilna_marka.grouping_places == 3
        assert konvertibilna_marka.grouping_sign == ','
        assert not konvertibilna_marka.international
        assert konvertibilna_marka.symbol == 'КМ'
        assert not konvertibilna_marka.symbol_ahead
        assert konvertibilna_marka.symbol_separator == '\u00A0'
        assert konvertibilna_marka.localized_symbol == 'КМ'
        assert konvertibilna_marka.convertion == ''
        assert konvertibilna_marka.__hash__() == hash(
            (konvertibilna_marka.__class__, decimal, 'BAM', '977'))
        assert konvertibilna_marka.__repr__() == (
            'KonvertibilnaMarka(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BAM", '
            'symbol: "КМ", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "КМ", '
            'numeric_code: "977", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert konvertibilna_marka.__str__() == '0.14 КМ'

    def test_konvertibilna_marka_negative(self):
        """test_konvertibilna_marka_negative."""
        amount = -100
        konvertibilna_marka = KonvertibilnaMarka(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert konvertibilna_marka.numeric_code == '977'
        assert konvertibilna_marka.alpha_code == 'BAM'
        assert konvertibilna_marka.decimal_places == 2
        assert konvertibilna_marka.decimal_sign == '.'
        assert konvertibilna_marka.grouping_places == 3
        assert konvertibilna_marka.grouping_sign == ','
        assert not konvertibilna_marka.international
        assert konvertibilna_marka.symbol == 'КМ'
        assert not konvertibilna_marka.symbol_ahead
        assert konvertibilna_marka.symbol_separator == '\u00A0'
        assert konvertibilna_marka.localized_symbol == 'КМ'
        assert konvertibilna_marka.convertion == ''
        assert konvertibilna_marka.__hash__() == hash(
            (konvertibilna_marka.__class__, decimal, 'BAM', '977'))
        assert konvertibilna_marka.__repr__() == (
            'KonvertibilnaMarka(amount: -100, '
            'alpha_code: "BAM", '
            'symbol: "КМ", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "КМ", '
            'numeric_code: "977", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert konvertibilna_marka.__str__() == '-100.00 КМ'

    def test_konvertibilna_marka_custom(self):
        """test_konvertibilna_marka_custom."""
        amount = 1000
        konvertibilna_marka = KonvertibilnaMarka(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert konvertibilna_marka.amount == decimal
        assert konvertibilna_marka.numeric_code == '977'
        assert konvertibilna_marka.alpha_code == 'BAM'
        assert konvertibilna_marka.decimal_places == 5
        assert konvertibilna_marka.decimal_sign == ','
        assert konvertibilna_marka.grouping_places == 2
        assert konvertibilna_marka.grouping_sign == '.'
        assert konvertibilna_marka.international
        assert konvertibilna_marka.symbol == 'КМ'
        assert not konvertibilna_marka.symbol_ahead
        assert konvertibilna_marka.symbol_separator == '_'
        assert konvertibilna_marka.localized_symbol == 'КМ'
        assert konvertibilna_marka.convertion == ''
        assert konvertibilna_marka.__hash__() == hash(
            (konvertibilna_marka.__class__, decimal, 'BAM', '977'))
        assert konvertibilna_marka.__repr__() == (
            'KonvertibilnaMarka(amount: 1000, '
            'alpha_code: "BAM", '
            'symbol: "КМ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "КМ", '
            'numeric_code: "977", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert konvertibilna_marka.__str__() == 'BAM 10,00.00000'

    def test_konvertibilna_marka_changed(self):
        """test_ckonvertibilna_marka_changed."""
        konvertibilna_marka = KonvertibilnaMarka(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            konvertibilna_marka.international = True

    def test_konvertibilna_marka_math_add(self):
        """test_konvertibilna_marka_math_add."""
        konvertibilna_marka_one = KonvertibilnaMarka(amount=1)
        konvertibilna_marka_two = KonvertibilnaMarka(amount=2)
        konvertibilna_marka_three = KonvertibilnaMarka(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BAM and OTHER.'):
            _ = konvertibilna_marka_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'marka.KonvertibilnaMarka\'> '
                    'and <class \'str\'>.')):
            _ = konvertibilna_marka_one.__add__('1.00')
        assert (
            konvertibilna_marka_one +
            konvertibilna_marka_two) == konvertibilna_marka_three

    def test_konvertibilna_marka_slots(self):
        """test_konvertibilna_marka_slots."""
        konvertibilna_marka = KonvertibilnaMarka(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'KonvertibilnaMarka\' '
                    'object has no attribute \'new_variable\'')):
            konvertibilna_marka.new_variable = 'fail'  # pylint: disable=assigning-non-slot
