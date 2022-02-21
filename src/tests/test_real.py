# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Real currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import BrazilianReal


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Brazilian Real representation."""


class TestBrazilianReal:
    """BrazilianReal currency tests."""

    def test_brazilian_real(self):
        """test_brazilian_real."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        brazilian_real = BrazilianReal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brazilian_real.amount == decimal
        assert brazilian_real.numeric_code == '986'
        assert brazilian_real.alpha_code == 'BRL'
        assert brazilian_real.decimal_places == 2
        assert brazilian_real.decimal_sign == ','
        assert brazilian_real.grouping_places == 3
        assert brazilian_real.grouping_sign == '.'
        assert not brazilian_real.international
        assert brazilian_real.symbol == 'R$'
        assert brazilian_real.symbol_ahead
        assert brazilian_real.symbol_separator == '\u00A0'
        assert brazilian_real.localized_symbol == 'R$'
        assert brazilian_real.convertion == ''
        assert brazilian_real.__hash__() == hash(
            (brazilian_real.__class__, decimal, 'BRL', '986'))
        assert brazilian_real.__repr__() == (
            'BrazilianReal(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BRL", '
            'symbol: "R$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "R$", '
            'numeric_code: "986", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brazilian_real.__str__() == 'R$ 0,14'

    def test_brazilian_real_negative(self):
        """test_brazilian_real_negative."""
        amount = -100
        brazilian_real = BrazilianReal(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brazilian_real.numeric_code == '986'
        assert brazilian_real.alpha_code == 'BRL'
        assert brazilian_real.decimal_places == 2
        assert brazilian_real.decimal_sign == ','
        assert brazilian_real.grouping_places == 3
        assert brazilian_real.grouping_sign == '.'
        assert not brazilian_real.international
        assert brazilian_real.symbol == 'R$'
        assert brazilian_real.symbol_ahead
        assert brazilian_real.symbol_separator == '\u00A0'
        assert brazilian_real.localized_symbol == 'R$'
        assert brazilian_real.convertion == ''
        assert brazilian_real.__hash__() == hash(
            (brazilian_real.__class__, decimal, 'BRL', '986'))
        assert brazilian_real.__repr__() == (
            'BrazilianReal(amount: -100, '
            'alpha_code: "BRL", '
            'symbol: "R$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "R$", '
            'numeric_code: "986", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brazilian_real.__str__() == 'R$ -100,00'

    def test_brazilian_real_custom(self):
        """test_brazilian_real_custom."""
        amount = 1000
        brazilian_real = BrazilianReal(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert brazilian_real.amount == decimal
        assert brazilian_real.numeric_code == '986'
        assert brazilian_real.alpha_code == 'BRL'
        assert brazilian_real.decimal_places == 5
        assert brazilian_real.decimal_sign == '.'
        assert brazilian_real.grouping_places == 2
        assert brazilian_real.grouping_sign == ','
        assert brazilian_real.international
        assert brazilian_real.symbol == 'R$'
        assert not brazilian_real.symbol_ahead
        assert brazilian_real.symbol_separator == '_'
        assert brazilian_real.localized_symbol == 'R$'
        assert brazilian_real.convertion == ''
        assert brazilian_real.__hash__() == hash(
            (brazilian_real.__class__, decimal, 'BRL', '986'))
        assert brazilian_real.__repr__() == (
            'BrazilianReal(amount: 1000, '
            'alpha_code: "BRL", '
            'symbol: "R$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "R$", '
            'numeric_code: "986", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert brazilian_real.__str__() == 'BRL 10,00.00000'

    def test_brazilian_real_changed(self):
        """test_cbrazilian_real_changed."""
        brazilian_real = BrazilianReal(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brazilian_real.international = True

    def test_brazilian_real_math_add(self):
        """test_brazilian_real_math_add."""
        brazilian_real_one = BrazilianReal(amount=1)
        brazilian_real_two = BrazilianReal(amount=2)
        brazilian_real_three = BrazilianReal(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BRL and OTHER.'):
            _ = brazilian_real_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'real.BrazilianReal\'> '
                    'and <class \'str\'>.')):
            _ = brazilian_real_one.__add__('1.00')
        assert (
            brazilian_real_one +
            brazilian_real_two) == brazilian_real_three

    def test_brazilian_real_slots(self):
        """test_brazilian_real_slots."""
        brazilian_real = BrazilianReal(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BrazilianReal\' '
                    'object has no attribute \'new_variable\'')):
            brazilian_real.new_variable = 'fail'  # pylint: disable=assigning-non-slot
