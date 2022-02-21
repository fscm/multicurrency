# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Riel currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Riel


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Riel representation."""


class TestRiel:
    """Riel currency tests."""

    def test_riel(self):
        """test_riel."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        riel = Riel(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert riel.amount == decimal
        assert riel.numeric_code == '116'
        assert riel.alpha_code == 'KHR'
        assert riel.decimal_places == 2
        assert riel.decimal_sign == ','
        assert riel.grouping_places == 3
        assert riel.grouping_sign == '.'
        assert not riel.international
        assert riel.symbol == '៛'
        assert not riel.symbol_ahead
        assert riel.symbol_separator == ''
        assert riel.localized_symbol == '៛'
        assert riel.convertion == ''
        assert riel.__hash__() == hash(
            (riel.__class__, decimal, 'KHR', '116'))
        assert riel.__repr__() == (
            'Riel(amount: 0.1428571428571428571428571429, '
            'alpha_code: "KHR", '
            'symbol: "៛", '
            'symbol_ahead: False, '
            'symbol_separator: "", '
            'localized_symbol: "៛", '
            'numeric_code: "116", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert riel.__str__() == '0,14៛'

    def test_riel_negative(self):
        """test_riel_negative."""
        amount = -100
        riel = Riel(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert riel.numeric_code == '116'
        assert riel.alpha_code == 'KHR'
        assert riel.decimal_places == 2
        assert riel.decimal_sign == ','
        assert riel.grouping_places == 3
        assert riel.grouping_sign == '.'
        assert not riel.international
        assert riel.symbol == '៛'
        assert not riel.symbol_ahead
        assert riel.symbol_separator == ''
        assert riel.localized_symbol == '៛'
        assert riel.convertion == ''
        assert riel.__hash__() == hash(
            (riel.__class__, decimal, 'KHR', '116'))
        assert riel.__repr__() == (
            'Riel(amount: -100, '
            'alpha_code: "KHR", '
            'symbol: "៛", '
            'symbol_ahead: False, '
            'symbol_separator: "", '
            'localized_symbol: "៛", '
            'numeric_code: "116", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert riel.__str__() == '-100,00៛'

    def test_riel_custom(self):
        """test_riel_custom."""
        amount = 1000
        riel = Riel(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert riel.amount == decimal
        assert riel.numeric_code == '116'
        assert riel.alpha_code == 'KHR'
        assert riel.decimal_places == 5
        assert riel.decimal_sign == '.'
        assert riel.grouping_places == 2
        assert riel.grouping_sign == ','
        assert riel.international
        assert riel.symbol == '៛'
        assert not riel.symbol_ahead
        assert riel.symbol_separator == '_'
        assert riel.localized_symbol == '៛'
        assert riel.convertion == ''
        assert riel.__hash__() == hash(
            (riel.__class__, decimal, 'KHR', '116'))
        assert riel.__repr__() == (
            'Riel(amount: 1000, '
            'alpha_code: "KHR", '
            'symbol: "៛", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "៛", '
            'numeric_code: "116", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert riel.__str__() == 'KHR 10,00.00000'

    def test_riel_changed(self):
        """test_criel_changed."""
        riel = Riel(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            riel.international = True

    def test_riel_math_add(self):
        """test_riel_math_add."""
        riel_one = Riel(amount=1)
        riel_two = Riel(amount=2)
        riel_three = Riel(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency KHR and OTHER.'):
            _ = riel_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'riel.Riel\'> '
                    'and <class \'str\'>.')):
            _ = riel_one.__add__('1.00')
        assert (
            riel_one +
            riel_two) == riel_three

    def test_riel_slots(self):
        """test_riel_slots."""
        riel = Riel(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Riel\' '
                    'object has no attribute \'new_variable\'')):
            riel.new_variable = 'fail'  # pylint: disable=assigning-non-slot
