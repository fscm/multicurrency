# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Somoni currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Somoni representation."""

from multicurrency import Somoni


class TestSomoni:
    """Somoni currency tests."""

    def test_somoni(self):
        """test_somoni."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        somoni = Somoni(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert somoni.amount == decimal
        assert somoni.numeric_code == '972'
        assert somoni.alpha_code == 'TJS'
        assert somoni.decimal_places == 2
        assert somoni.decimal_sign == '.'
        assert somoni.grouping_places == 3
        assert somoni.grouping_sign == ','
        assert not somoni.international
        assert somoni.symbol == 'ЅМ'
        assert somoni.symbol_ahead
        assert somoni.symbol_separator == '\u00A0'
        assert somoni.localized_symbol == 'ЅМ'
        assert somoni.convertion == ''
        assert somoni.__hash__() == hash(
            (somoni.__class__, decimal, 'TJS', '972'))
        assert somoni.__repr__() == (
            'Somoni(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TJS", '
            'symbol: "ЅМ", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ЅМ", '
            'numeric_code: "972", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert somoni.__str__() == 'ЅМ 0.14'

    def test_somoni_negative(self):
        """test_somoni_negative."""
        amount = -100
        somoni = Somoni(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert somoni.numeric_code == '972'
        assert somoni.alpha_code == 'TJS'
        assert somoni.decimal_places == 2
        assert somoni.decimal_sign == '.'
        assert somoni.grouping_places == 3
        assert somoni.grouping_sign == ','
        assert not somoni.international
        assert somoni.symbol == 'ЅМ'
        assert somoni.symbol_ahead
        assert somoni.symbol_separator == '\u00A0'
        assert somoni.localized_symbol == 'ЅМ'
        assert somoni.convertion == ''
        assert somoni.__hash__() == hash(
            (somoni.__class__, decimal, 'TJS', '972'))
        assert somoni.__repr__() == (
            'Somoni(amount: -100, '
            'alpha_code: "TJS", '
            'symbol: "ЅМ", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ЅМ", '
            'numeric_code: "972", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert somoni.__str__() == 'ЅМ -100.00'

    def test_somoni_custom(self):
        """test_somoni_custom."""
        amount = 1000
        somoni = Somoni(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert somoni.amount == decimal
        assert somoni.numeric_code == '972'
        assert somoni.alpha_code == 'TJS'
        assert somoni.decimal_places == 5
        assert somoni.decimal_sign == ','
        assert somoni.grouping_places == 2
        assert somoni.grouping_sign == '.'
        assert somoni.international
        assert somoni.symbol == 'ЅМ'
        assert not somoni.symbol_ahead
        assert somoni.symbol_separator == '_'
        assert somoni.localized_symbol == 'ЅМ'
        assert somoni.convertion == ''
        assert somoni.__hash__() == hash(
            (somoni.__class__, decimal, 'TJS', '972'))
        assert somoni.__repr__() == (
            'Somoni(amount: 1000, '
            'alpha_code: "TJS", '
            'symbol: "ЅМ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ЅМ", '
            'numeric_code: "972", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert somoni.__str__() == 'TJS 10,00.00000'

    def test_somoni_changed(self):
        """test_csomoni_changed."""
        somoni = Somoni(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somoni.international = True

    def test_somoni_math_add(self):
        """test_somoni_math_add."""
        somoni_one = Somoni(amount=1)
        somoni_two = Somoni(amount=2)
        somoni_three = Somoni(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TJS and OTHER.'):
            _ = somoni_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'somoni.Somoni\'> '
                    'and <class \'str\'>.')):
            _ = somoni_one.__add__('1.00')
        assert (
            somoni_one +
            somoni_two) == somoni_three

    def test_somoni_slots(self):
        """test_somoni_slots."""
        somoni = Somoni(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Somoni\' '
                    'object has no attribute \'new_variable\'')):
            somoni.new_variable = 'fail'  # pylint: disable=assigning-non-slot
