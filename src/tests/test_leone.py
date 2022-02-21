# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leone currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Leone


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Leone representation."""


class TestLeone:
    """Leone currency tests."""

    def test_leone(self):
        """test_leone."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        leone = Leone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert leone.amount == decimal
        assert leone.numeric_code == '694'
        assert leone.alpha_code == 'SLL'
        assert leone.decimal_places == 2
        assert leone.decimal_sign == '.'
        assert leone.grouping_places == 3
        assert leone.grouping_sign == ','
        assert not leone.international
        assert leone.symbol == 'Le'
        assert leone.symbol_ahead
        assert leone.symbol_separator == '\u00A0'
        assert leone.localized_symbol == 'Le'
        assert leone.convertion == ''
        assert leone.__hash__() == hash(
            (leone.__class__, decimal, 'SLL', '694'))
        assert leone.__repr__() == (
            'Leone(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SLL", '
            'symbol: "Le", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Le", '
            'numeric_code: "694", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert leone.__str__() == 'Le 0.14'

    def test_leone_negative(self):
        """test_leone_negative."""
        amount = -100
        leone = Leone(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert leone.numeric_code == '694'
        assert leone.alpha_code == 'SLL'
        assert leone.decimal_places == 2
        assert leone.decimal_sign == '.'
        assert leone.grouping_places == 3
        assert leone.grouping_sign == ','
        assert not leone.international
        assert leone.symbol == 'Le'
        assert leone.symbol_ahead
        assert leone.symbol_separator == '\u00A0'
        assert leone.localized_symbol == 'Le'
        assert leone.convertion == ''
        assert leone.__hash__() == hash(
            (leone.__class__, decimal, 'SLL', '694'))
        assert leone.__repr__() == (
            'Leone(amount: -100, '
            'alpha_code: "SLL", '
            'symbol: "Le", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Le", '
            'numeric_code: "694", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert leone.__str__() == 'Le -100.00'

    def test_leone_custom(self):
        """test_leone_custom."""
        amount = 1000
        leone = Leone(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert leone.amount == decimal
        assert leone.numeric_code == '694'
        assert leone.alpha_code == 'SLL'
        assert leone.decimal_places == 5
        assert leone.decimal_sign == ','
        assert leone.grouping_places == 2
        assert leone.grouping_sign == '.'
        assert leone.international
        assert leone.symbol == 'Le'
        assert not leone.symbol_ahead
        assert leone.symbol_separator == '_'
        assert leone.localized_symbol == 'Le'
        assert leone.convertion == ''
        assert leone.__hash__() == hash(
            (leone.__class__, decimal, 'SLL', '694'))
        assert leone.__repr__() == (
            'Leone(amount: 1000, '
            'alpha_code: "SLL", '
            'symbol: "Le", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Le", '
            'numeric_code: "694", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert leone.__str__() == 'SLL 10,00.00000'

    def test_leone_changed(self):
        """test_cleone_changed."""
        leone = Leone(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leone.international = True

    def test_leone_math_add(self):
        """test_leone_math_add."""
        leone_one = Leone(amount=1)
        leone_two = Leone(amount=2)
        leone_three = Leone(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SLL and OTHER.'):
            _ = leone_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'leone.Leone\'> '
                    'and <class \'str\'>.')):
            _ = leone_one.__add__('1.00')
        assert (
            leone_one +
            leone_two) == leone_three

    def test_leone_slots(self):
        """test_leone_slots."""
        leone = Leone(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Leone\' '
                    'object has no attribute \'new_variable\'')):
            leone.new_variable = 'fail'  # pylint: disable=assigning-non-slot
