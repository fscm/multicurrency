# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Escudo currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Cape Verde Escudo representation."""

from multicurrency import CapeVerdeEscudo


class TestCapeVerdeEscudo:
    """CapeVerdeEscudo currency tests."""

    def test_cape_verde_escudo(self):
        """test_cape_verde_escudo."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cape_verde_escudo = CapeVerdeEscudo(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cape_verde_escudo.amount == decimal
        assert cape_verde_escudo.numeric_code == '132'
        assert cape_verde_escudo.alpha_code == 'CVE'
        assert cape_verde_escudo.decimal_places == 2
        assert cape_verde_escudo.decimal_sign == '$'
        assert cape_verde_escudo.grouping_places == 3
        assert cape_verde_escudo.grouping_sign == '\u202F'
        assert not cape_verde_escudo.international
        assert cape_verde_escudo.symbol == ''
        assert not cape_verde_escudo.symbol_ahead
        assert cape_verde_escudo.symbol_separator == ''
        assert cape_verde_escudo.localized_symbol == ''
        assert cape_verde_escudo.convertion == ''
        assert cape_verde_escudo.__hash__() == hash(
            (cape_verde_escudo.__class__, decimal, 'CVE', '132'))
        assert cape_verde_escudo.__repr__() == (
            'CapeVerdeEscudo(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CVE", '
            'symbol: "", '
            'symbol_ahead: False, '
            'symbol_separator: "", '
            'localized_symbol: "", '
            'numeric_code: "132", '
            'decimal_places: "2", '
            'decimal_sign: "$", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cape_verde_escudo.__str__() == '0$14'

    def test_cape_verde_escudo_negative(self):
        """test_cape_verde_escudo_negative."""
        amount = -100
        cape_verde_escudo = CapeVerdeEscudo(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cape_verde_escudo.numeric_code == '132'
        assert cape_verde_escudo.alpha_code == 'CVE'
        assert cape_verde_escudo.decimal_places == 2
        assert cape_verde_escudo.decimal_sign == '$'
        assert cape_verde_escudo.grouping_places == 3
        assert cape_verde_escudo.grouping_sign == '\u202F'
        assert not cape_verde_escudo.international
        assert cape_verde_escudo.symbol == ''
        assert not cape_verde_escudo.symbol_ahead
        assert cape_verde_escudo.symbol_separator == ''
        assert cape_verde_escudo.localized_symbol == ''
        assert cape_verde_escudo.convertion == ''
        assert cape_verde_escudo.__hash__() == hash(
            (cape_verde_escudo.__class__, decimal, 'CVE', '132'))
        assert cape_verde_escudo.__repr__() == (
            'CapeVerdeEscudo(amount: -100, '
            'alpha_code: "CVE", '
            'symbol: "", '
            'symbol_ahead: False, '
            'symbol_separator: "", '
            'localized_symbol: "", '
            'numeric_code: "132", '
            'decimal_places: "2", '
            'decimal_sign: "$", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cape_verde_escudo.__str__() == '-100$00'

    def test_cape_verde_escudo_custom(self):
        """test_cape_verde_escudo_custom."""
        amount = 1000
        cape_verde_escudo = CapeVerdeEscudo(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign='$',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cape_verde_escudo.amount == decimal
        assert cape_verde_escudo.numeric_code == '132'
        assert cape_verde_escudo.alpha_code == 'CVE'
        assert cape_verde_escudo.decimal_places == 5
        assert cape_verde_escudo.decimal_sign == '\u202F'
        assert cape_verde_escudo.grouping_places == 2
        assert cape_verde_escudo.grouping_sign == '$'
        assert cape_verde_escudo.international
        assert cape_verde_escudo.symbol == ''
        assert not cape_verde_escudo.symbol_ahead
        assert cape_verde_escudo.symbol_separator == '_'
        assert cape_verde_escudo.localized_symbol == ''
        assert cape_verde_escudo.convertion == ''
        assert cape_verde_escudo.__hash__() == hash(
            (cape_verde_escudo.__class__, decimal, 'CVE', '132'))
        assert cape_verde_escudo.__repr__() == (
            'CapeVerdeEscudo(amount: 1000, '
            'alpha_code: "CVE", '
            'symbol: "", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "", '
            'numeric_code: "132", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: "$", '
            'convertion: "", '
            'international: True)')
        assert cape_verde_escudo.__str__() == 'CVE 10,00.00000'

    def test_cape_verde_escudo_changed(self):
        """test_ccape_verde_escudo_changed."""
        cape_verde_escudo = CapeVerdeEscudo(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cape_verde_escudo.international = True

    def test_cape_verde_escudo_math_add(self):
        """test_cape_verde_escudo_math_add."""
        cape_verde_escudo_one = CapeVerdeEscudo(amount=1)
        cape_verde_escudo_two = CapeVerdeEscudo(amount=2)
        cape_verde_escudo_three = CapeVerdeEscudo(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CVE and OTHER.'):
            _ = cape_verde_escudo_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'escudo.CapeVerdeEscudo\'> '
                    'and <class \'str\'>.')):
            _ = cape_verde_escudo_one.__add__('1.00')
        assert (
            cape_verde_escudo_one +
            cape_verde_escudo_two) == cape_verde_escudo_three

    def test_cape_verde_escudo_slots(self):
        """test_cape_verde_escudo_slots."""
        cape_verde_escudo = CapeVerdeEscudo(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CapeVerdeEscudo\' '
                    'object has no attribute \'new_variable\'')):
            cape_verde_escudo.new_variable = 'fail'  # pylint: disable=assigning-non-slot
