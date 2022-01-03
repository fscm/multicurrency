# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pataca currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Pataca representation."""

from multicurrency import Pataca


class TestPataca:
    """Pataca currency tests."""

    def test_pataca(self):
        """test_pataca."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pataca = Pataca(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pataca.amount == decimal
        assert pataca.numeric_code == '446'
        assert pataca.alpha_code == 'MOP'
        assert pataca.decimal_places == 2
        assert pataca.decimal_sign == '.'
        assert pataca.grouping_places == 3
        assert pataca.grouping_sign == ','
        assert not pataca.international
        assert pataca.symbol == 'P'
        assert pataca.symbol_ahead
        assert pataca.symbol_separator == '\u00A0'
        assert pataca.localized_symbol == 'P'
        assert pataca.convertion == ''
        assert pataca.__hash__() == hash(
            (pataca.__class__, decimal, 'MOP', '446'))
        assert pataca.__repr__() == (
            'Pataca(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MOP", '
            'symbol: "P", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "P", '
            'numeric_code: "446", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pataca.__str__() == 'P 0.14'

    def test_pataca_negative(self):
        """test_pataca_negative."""
        amount = -100
        pataca = Pataca(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pataca.numeric_code == '446'
        assert pataca.alpha_code == 'MOP'
        assert pataca.decimal_places == 2
        assert pataca.decimal_sign == '.'
        assert pataca.grouping_places == 3
        assert pataca.grouping_sign == ','
        assert not pataca.international
        assert pataca.symbol == 'P'
        assert pataca.symbol_ahead
        assert pataca.symbol_separator == '\u00A0'
        assert pataca.localized_symbol == 'P'
        assert pataca.convertion == ''
        assert pataca.__hash__() == hash(
            (pataca.__class__, decimal, 'MOP', '446'))
        assert pataca.__repr__() == (
            'Pataca(amount: -100, '
            'alpha_code: "MOP", '
            'symbol: "P", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "P", '
            'numeric_code: "446", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pataca.__str__() == 'P -100.00'

    def test_pataca_custom(self):
        """test_pataca_custom."""
        amount = 1000
        pataca = Pataca(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pataca.amount == decimal
        assert pataca.numeric_code == '446'
        assert pataca.alpha_code == 'MOP'
        assert pataca.decimal_places == 5
        assert pataca.decimal_sign == ','
        assert pataca.grouping_places == 2
        assert pataca.grouping_sign == '.'
        assert pataca.international
        assert pataca.symbol == 'P'
        assert not pataca.symbol_ahead
        assert pataca.symbol_separator == '_'
        assert pataca.localized_symbol == 'P'
        assert pataca.convertion == ''
        assert pataca.__hash__() == hash(
            (pataca.__class__, decimal, 'MOP', '446'))
        assert pataca.__repr__() == (
            'Pataca(amount: 1000, '
            'alpha_code: "MOP", '
            'symbol: "P", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "P", '
            'numeric_code: "446", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pataca.__str__() == 'MOP 10,00.00000'

    def test_pataca_changed(self):
        """test_cpataca_changed."""
        pataca = Pataca(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pataca.international = True

    def test_pataca_math_add(self):
        """test_pataca_math_add."""
        pataca_one = Pataca(amount=1)
        pataca_two = Pataca(amount=2)
        pataca_three = Pataca(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MOP and OTHER.'):
            _ = pataca_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'pataca.Pataca\'> '
                    'and <class \'str\'>.')):
            _ = pataca_one.__add__('1.00')
        assert (
            pataca_one +
            pataca_two) == pataca_three

    def test_pataca_slots(self):
        """test_pataca_slots."""
        pataca = Pataca(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Pataca\' '
                    'object has no attribute \'new_variable\'')):
            pataca.new_variable = 'fail'  # pylint: disable=assigning-non-slot
