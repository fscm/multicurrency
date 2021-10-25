# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kuna currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Croatian Kuna representation."""

from multicurrency import CroatianKuna


class TestCroatianKuna:

    def test_croatian_kuna(self):
        """test_croatian_kuna."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        croatian_kuna = CroatianKuna(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert croatian_kuna.amount == decimal
        assert croatian_kuna.numeric_code == '191'
        assert croatian_kuna.alpha_code == 'HRK'
        assert croatian_kuna.decimal_places == 2
        assert croatian_kuna.decimal_sign == ','
        assert croatian_kuna.grouping_places == 3
        assert croatian_kuna.grouping_sign == '.'
        assert not croatian_kuna.international
        assert croatian_kuna.symbol == 'Kn'
        assert not croatian_kuna.symbol_ahead
        assert croatian_kuna.symbol_separator == '\u00A0'
        assert croatian_kuna.localized_symbol == 'Kn'
        assert croatian_kuna.convertion == ''
        assert croatian_kuna.__hash__() == hash((decimal, 'HRK', '191'))
        assert croatian_kuna.__repr__() == (
            'CroatianKuna(amount: 0.1428571428571428571428571429, '
            'alpha_code: "HRK", '
            'symbol: "Kn", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kn", '
            'numeric_code: "191", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert croatian_kuna.__str__() == '0,14 Kn'


    def test_croatian_kuna_negative(self):
        """test_croatian_kuna_negative."""
        amount = -100
        croatian_kuna = CroatianKuna(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert croatian_kuna.numeric_code == '191'
        assert croatian_kuna.alpha_code == 'HRK'
        assert croatian_kuna.decimal_places == 2
        assert croatian_kuna.decimal_sign == ','
        assert croatian_kuna.grouping_places == 3
        assert croatian_kuna.grouping_sign == '.'
        assert not croatian_kuna.international
        assert croatian_kuna.symbol == 'Kn'
        assert not croatian_kuna.symbol_ahead
        assert croatian_kuna.symbol_separator == '\u00A0'
        assert croatian_kuna.localized_symbol == 'Kn'
        assert croatian_kuna.convertion == ''
        assert croatian_kuna.__hash__() == hash((decimal, 'HRK', '191'))
        assert croatian_kuna.__repr__() == (
            'CroatianKuna(amount: -100, '
            'alpha_code: "HRK", '
            'symbol: "Kn", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kn", '
            'numeric_code: "191", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert croatian_kuna.__str__() == '-100,00 Kn'


    def test_croatian_kuna_custom(self):
        """test_croatian_kuna_custom."""
        amount = 1000
        croatian_kuna = CroatianKuna(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert croatian_kuna.amount == decimal
        assert croatian_kuna.numeric_code == '191'
        assert croatian_kuna.alpha_code == 'HRK'
        assert croatian_kuna.decimal_places == 5
        assert croatian_kuna.decimal_sign == '.'
        assert croatian_kuna.grouping_places == 2
        assert croatian_kuna.grouping_sign == ','
        assert croatian_kuna.international
        assert croatian_kuna.symbol == 'Kn'
        assert not croatian_kuna.symbol_ahead
        assert croatian_kuna.symbol_separator == '_'
        assert croatian_kuna.localized_symbol == 'Kn'
        assert croatian_kuna.convertion == ''
        assert croatian_kuna.__hash__() == hash((decimal, 'HRK', '191'))
        assert croatian_kuna.__repr__() == (
            'CroatianKuna(amount: 1000, '
            'alpha_code: "HRK", '
            'symbol: "Kn", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Kn", '
            'numeric_code: "191", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert croatian_kuna.__str__() == 'HRK 10,00.00000'


    def test_croatian_kuna_changed(self):
        """test_ccroatian_kuna_changed."""
        croatian_kuna = CroatianKuna(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            croatian_kuna.international = True


    def test_croatian_kuna_math_add(self):
        """test_croatian_kuna_math_add."""
        croatian_kuna_one = CroatianKuna(amount=1)
        croatian_kuna_two = CroatianKuna(amount=2)
        croatian_kuna_three = CroatianKuna(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency HRK and OTHER.'):
            _ = croatian_kuna_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'kuna.CroatianKuna\'> '
                    'and <class \'str\'>.')):
            _ = croatian_kuna_one.__add__('1.00')
        assert (
            croatian_kuna_one +
            croatian_kuna_two) == croatian_kuna_three


    def test_croatian_kuna_slots(self):
        """test_croatian_kuna_slots."""
        croatian_kuna = CroatianKuna(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CroatianKuna\' '
                    'object has no attribute \'new_variable\'')):
            croatian_kuna.new_variable = 'fail'  # pylint: disable=assigning-non-slot
