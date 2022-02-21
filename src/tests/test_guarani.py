# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Guarani currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import Guarani


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Guarani representation."""


class TestGuarani:
    """Guarani currency tests."""

    def test_guarani(self):
        """test_guarani."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        guarani = Guarani(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guarani.amount == decimal
        assert guarani.numeric_code == '600'
        assert guarani.alpha_code == 'PYG'
        assert guarani.decimal_places == 0
        assert guarani.decimal_sign == ','
        assert guarani.grouping_places == 3
        assert guarani.grouping_sign == '.'
        assert not guarani.international
        assert guarani.symbol == '₲'
        assert guarani.symbol_ahead
        assert guarani.symbol_separator == '\u00A0'
        assert guarani.localized_symbol == '₲'
        assert guarani.convertion == ''
        assert guarani.__hash__() == hash(
            (guarani.__class__, decimal, 'PYG', '600'))
        assert guarani.__repr__() == (
            'Guarani(amount: 0.1428571428571428571428571429, '
            'alpha_code: "PYG", '
            'symbol: "₲", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₲", '
            'numeric_code: "600", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert guarani.__str__() == '₲ 0'

    def test_guarani_negative(self):
        """test_guarani_negative."""
        amount = -100
        guarani = Guarani(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guarani.numeric_code == '600'
        assert guarani.alpha_code == 'PYG'
        assert guarani.decimal_places == 0
        assert guarani.decimal_sign == ','
        assert guarani.grouping_places == 3
        assert guarani.grouping_sign == '.'
        assert not guarani.international
        assert guarani.symbol == '₲'
        assert guarani.symbol_ahead
        assert guarani.symbol_separator == '\u00A0'
        assert guarani.localized_symbol == '₲'
        assert guarani.convertion == ''
        assert guarani.__hash__() == hash(
            (guarani.__class__, decimal, 'PYG', '600'))
        assert guarani.__repr__() == (
            'Guarani(amount: -100, '
            'alpha_code: "PYG", '
            'symbol: "₲", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₲", '
            'numeric_code: "600", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert guarani.__str__() == '₲ -100'

    def test_guarani_custom(self):
        """test_guarani_custom."""
        amount = 1000
        guarani = Guarani(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert guarani.amount == decimal
        assert guarani.numeric_code == '600'
        assert guarani.alpha_code == 'PYG'
        assert guarani.decimal_places == 5
        assert guarani.decimal_sign == '.'
        assert guarani.grouping_places == 2
        assert guarani.grouping_sign == ','
        assert guarani.international
        assert guarani.symbol == '₲'
        assert not guarani.symbol_ahead
        assert guarani.symbol_separator == '_'
        assert guarani.localized_symbol == '₲'
        assert guarani.convertion == ''
        assert guarani.__hash__() == hash(
            (guarani.__class__, decimal, 'PYG', '600'))
        assert guarani.__repr__() == (
            'Guarani(amount: 1000, '
            'alpha_code: "PYG", '
            'symbol: "₲", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₲", '
            'numeric_code: "600", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert guarani.__str__() == 'PYG 10,00.00000'

    def test_guarani_changed(self):
        """test_cguarani_changed."""
        guarani = Guarani(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guarani.international = True

    def test_guarani_math_add(self):
        """test_guarani_math_add."""
        guarani_one = Guarani(amount=1)
        guarani_two = Guarani(amount=2)
        guarani_three = Guarani(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency PYG and OTHER.'):
            _ = guarani_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'guarani.Guarani\'> '
                    'and <class \'str\'>.')):
            _ = guarani_one.__add__('1.00')
        assert (
            guarani_one +
            guarani_two) == guarani_three

    def test_guarani_slots(self):
        """test_guarani_slots."""
        guarani = Guarani(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Guarani\' '
                    'object has no attribute \'new_variable\'')):
            guarani.new_variable = 'fail'  # pylint: disable=assigning-non-slot
