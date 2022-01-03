# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lek currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Lek representation."""

from multicurrency import Lek


class TestLek:
    """Lek currency tests."""

    def test_lek(self):
        """test_lek."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        lek = Lek(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lek.amount == decimal
        assert lek.numeric_code == '008'
        assert lek.alpha_code == 'ALL'
        assert lek.decimal_places == 2
        assert lek.decimal_sign == ','
        assert lek.grouping_places == 3
        assert lek.grouping_sign == '\u202F'
        assert not lek.international
        assert lek.symbol == 'Lek'
        assert not lek.symbol_ahead
        assert lek.symbol_separator == '\u00A0'
        assert lek.localized_symbol == 'Lek'
        assert lek.convertion == ''
        assert lek.__hash__() == hash(
            (lek.__class__, decimal, 'ALL', '008'))
        assert lek.__repr__() == (
            'Lek(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ALL", '
            'symbol: "Lek", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Lek", '
            'numeric_code: "008", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert lek.__str__() == '0,14 Lek'

    def test_lek_negative(self):
        """test_lek_negative."""
        amount = -100
        lek = Lek(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lek.numeric_code == '008'
        assert lek.alpha_code == 'ALL'
        assert lek.decimal_places == 2
        assert lek.decimal_sign == ','
        assert lek.grouping_places == 3
        assert lek.grouping_sign == '\u202F'
        assert not lek.international
        assert lek.symbol == 'Lek'
        assert not lek.symbol_ahead
        assert lek.symbol_separator == '\u00A0'
        assert lek.localized_symbol == 'Lek'
        assert lek.convertion == ''
        assert lek.__hash__() == hash(
            (lek.__class__, decimal, 'ALL', '008'))
        assert lek.__repr__() == (
            'Lek(amount: -100, '
            'alpha_code: "ALL", '
            'symbol: "Lek", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Lek", '
            'numeric_code: "008", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert lek.__str__() == '-100,00 Lek'

    def test_lek_custom(self):
        """test_lek_custom."""
        amount = 1000
        lek = Lek(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert lek.amount == decimal
        assert lek.numeric_code == '008'
        assert lek.alpha_code == 'ALL'
        assert lek.decimal_places == 5
        assert lek.decimal_sign == '\u202F'
        assert lek.grouping_places == 2
        assert lek.grouping_sign == ','
        assert lek.international
        assert lek.symbol == 'Lek'
        assert not lek.symbol_ahead
        assert lek.symbol_separator == '_'
        assert lek.localized_symbol == 'Lek'
        assert lek.convertion == ''
        assert lek.__hash__() == hash(
            (lek.__class__, decimal, 'ALL', '008'))
        assert lek.__repr__() == (
            'Lek(amount: 1000, '
            'alpha_code: "ALL", '
            'symbol: "Lek", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Lek", '
            'numeric_code: "008", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert lek.__str__() == 'ALL 10,00.00000'

    def test_lek_changed(self):
        """test_clek_changed."""
        lek = Lek(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lek.international = True

    def test_lek_math_add(self):
        """test_lek_math_add."""
        lek_one = Lek(amount=1)
        lek_two = Lek(amount=2)
        lek_three = Lek(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ALL and OTHER.'):
            _ = lek_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'lek.Lek\'> '
                    'and <class \'str\'>.')):
            _ = lek_one.__add__('1.00')
        assert (
            lek_one +
            lek_two) == lek_three

    def test_lek_slots(self):
        """test_lek_slots."""
        lek = Lek(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Lek\' '
                    'object has no attribute \'new_variable\'')):
            lek.new_variable = 'fail'  # pylint: disable=assigning-non-slot
