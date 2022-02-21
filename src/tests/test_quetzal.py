# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Quetzal currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Quetzal


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Quetzal representation."""


class TestQuetzal:
    """Quetzal currency tests."""

    def test_quetzal(self):
        """test_quetzal."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        quetzal = Quetzal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert quetzal.amount == decimal
        assert quetzal.numeric_code == '320'
        assert quetzal.alpha_code == 'GTQ'
        assert quetzal.decimal_places == 2
        assert quetzal.decimal_sign == '.'
        assert quetzal.grouping_places == 3
        assert quetzal.grouping_sign == ','
        assert not quetzal.international
        assert quetzal.symbol == 'Q'
        assert quetzal.symbol_ahead
        assert quetzal.symbol_separator == '\u00A0'
        assert quetzal.localized_symbol == 'Q'
        assert quetzal.convertion == ''
        assert quetzal.__hash__() == hash(
            (quetzal.__class__, decimal, 'GTQ', '320'))
        assert quetzal.__repr__() == (
            'Quetzal(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GTQ", '
            'symbol: "Q", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Q", '
            'numeric_code: "320", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert quetzal.__str__() == 'Q 0.14'

    def test_quetzal_negative(self):
        """test_quetzal_negative."""
        amount = -100
        quetzal = Quetzal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert quetzal.numeric_code == '320'
        assert quetzal.alpha_code == 'GTQ'
        assert quetzal.decimal_places == 2
        assert quetzal.decimal_sign == '.'
        assert quetzal.grouping_places == 3
        assert quetzal.grouping_sign == ','
        assert not quetzal.international
        assert quetzal.symbol == 'Q'
        assert quetzal.symbol_ahead
        assert quetzal.symbol_separator == '\u00A0'
        assert quetzal.localized_symbol == 'Q'
        assert quetzal.convertion == ''
        assert quetzal.__hash__() == hash(
            (quetzal.__class__, decimal, 'GTQ', '320'))
        assert quetzal.__repr__() == (
            'Quetzal(amount: -100, '
            'alpha_code: "GTQ", '
            'symbol: "Q", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Q", '
            'numeric_code: "320", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert quetzal.__str__() == 'Q -100.00'

    def test_quetzal_custom(self):
        """test_quetzal_custom."""
        amount = 1000
        quetzal = Quetzal(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert quetzal.amount == decimal
        assert quetzal.numeric_code == '320'
        assert quetzal.alpha_code == 'GTQ'
        assert quetzal.decimal_places == 5
        assert quetzal.decimal_sign == ','
        assert quetzal.grouping_places == 2
        assert quetzal.grouping_sign == '.'
        assert quetzal.international
        assert quetzal.symbol == 'Q'
        assert not quetzal.symbol_ahead
        assert quetzal.symbol_separator == '_'
        assert quetzal.localized_symbol == 'Q'
        assert quetzal.convertion == ''
        assert quetzal.__hash__() == hash(
            (quetzal.__class__, decimal, 'GTQ', '320'))
        assert quetzal.__repr__() == (
            'Quetzal(amount: 1000, '
            'alpha_code: "GTQ", '
            'symbol: "Q", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Q", '
            'numeric_code: "320", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert quetzal.__str__() == 'GTQ 10,00.00000'

    def test_quetzal_changed(self):
        """test_cquetzal_changed."""
        quetzal = Quetzal(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            quetzal.international = True

    def test_quetzal_math_add(self):
        """test_quetzal_math_add."""
        quetzal_one = Quetzal(amount=1)
        quetzal_two = Quetzal(amount=2)
        quetzal_three = Quetzal(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GTQ and OTHER.'):
            _ = quetzal_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'quetzal.Quetzal\'> '
                    'and <class \'str\'>.')):
            _ = quetzal_one.__add__('1.00')
        assert (
            quetzal_one +
            quetzal_two) == quetzal_three

    def test_quetzal_slots(self):
        """test_quetzal_slots."""
        quetzal = Quetzal(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Quetzal\' '
                    'object has no attribute \'new_variable\'')):
            quetzal.new_variable = 'fail'  # pylint: disable=assigning-non-slot
