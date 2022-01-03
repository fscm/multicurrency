# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ringgit currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Malaysian Ringgit representation."""

from multicurrency import MalaysianRinggit


class TestMalaysianRinggit:
    """MalaysianRinggit currency tests."""

    def test_malaysian_ringgit(self):
        """test_malaysian_ringgit."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        malaysian_ringgit = MalaysianRinggit(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert malaysian_ringgit.amount == decimal
        assert malaysian_ringgit.numeric_code == '458'
        assert malaysian_ringgit.alpha_code == 'MYR'
        assert malaysian_ringgit.decimal_places == 2
        assert malaysian_ringgit.decimal_sign == '.'
        assert malaysian_ringgit.grouping_places == 3
        assert malaysian_ringgit.grouping_sign == ','
        assert not malaysian_ringgit.international
        assert malaysian_ringgit.symbol == 'RM'
        assert malaysian_ringgit.symbol_ahead
        assert malaysian_ringgit.symbol_separator == '\u00A0'
        assert malaysian_ringgit.localized_symbol == 'RM'
        assert malaysian_ringgit.convertion == ''
        assert malaysian_ringgit.__hash__() == hash(
            (malaysian_ringgit.__class__, decimal, 'MYR', '458'))
        assert malaysian_ringgit.__repr__() == (
            'MalaysianRinggit(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MYR", '
            'symbol: "RM", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RM", '
            'numeric_code: "458", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert malaysian_ringgit.__str__() == 'RM 0.14'

    def test_malaysian_ringgit_negative(self):
        """test_malaysian_ringgit_negative."""
        amount = -100
        malaysian_ringgit = MalaysianRinggit(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert malaysian_ringgit.numeric_code == '458'
        assert malaysian_ringgit.alpha_code == 'MYR'
        assert malaysian_ringgit.decimal_places == 2
        assert malaysian_ringgit.decimal_sign == '.'
        assert malaysian_ringgit.grouping_places == 3
        assert malaysian_ringgit.grouping_sign == ','
        assert not malaysian_ringgit.international
        assert malaysian_ringgit.symbol == 'RM'
        assert malaysian_ringgit.symbol_ahead
        assert malaysian_ringgit.symbol_separator == '\u00A0'
        assert malaysian_ringgit.localized_symbol == 'RM'
        assert malaysian_ringgit.convertion == ''
        assert malaysian_ringgit.__hash__() == hash(
            (malaysian_ringgit.__class__, decimal, 'MYR', '458'))
        assert malaysian_ringgit.__repr__() == (
            'MalaysianRinggit(amount: -100, '
            'alpha_code: "MYR", '
            'symbol: "RM", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RM", '
            'numeric_code: "458", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert malaysian_ringgit.__str__() == 'RM -100.00'

    def test_malaysian_ringgit_custom(self):
        """test_malaysian_ringgit_custom."""
        amount = 1000
        malaysian_ringgit = MalaysianRinggit(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert malaysian_ringgit.amount == decimal
        assert malaysian_ringgit.numeric_code == '458'
        assert malaysian_ringgit.alpha_code == 'MYR'
        assert malaysian_ringgit.decimal_places == 5
        assert malaysian_ringgit.decimal_sign == ','
        assert malaysian_ringgit.grouping_places == 2
        assert malaysian_ringgit.grouping_sign == '.'
        assert malaysian_ringgit.international
        assert malaysian_ringgit.symbol == 'RM'
        assert not malaysian_ringgit.symbol_ahead
        assert malaysian_ringgit.symbol_separator == '_'
        assert malaysian_ringgit.localized_symbol == 'RM'
        assert malaysian_ringgit.convertion == ''
        assert malaysian_ringgit.__hash__() == hash(
            (malaysian_ringgit.__class__, decimal, 'MYR', '458'))
        assert malaysian_ringgit.__repr__() == (
            'MalaysianRinggit(amount: 1000, '
            'alpha_code: "MYR", '
            'symbol: "RM", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "RM", '
            'numeric_code: "458", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert malaysian_ringgit.__str__() == 'MYR 10,00.00000'

    def test_malaysian_ringgit_changed(self):
        """test_cmalaysian_ringgit_changed."""
        malaysian_ringgit = MalaysianRinggit(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            malaysian_ringgit.international = True

    def test_malaysian_ringgit_math_add(self):
        """test_malaysian_ringgit_math_add."""
        malaysian_ringgit_one = MalaysianRinggit(amount=1)
        malaysian_ringgit_two = MalaysianRinggit(amount=2)
        malaysian_ringgit_three = MalaysianRinggit(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MYR and OTHER.'):
            _ = malaysian_ringgit_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ringgit.MalaysianRinggit\'> '
                    'and <class \'str\'>.')):
            _ = malaysian_ringgit_one.__add__('1.00')
        assert (
            malaysian_ringgit_one +
            malaysian_ringgit_two) == malaysian_ringgit_three

    def test_malaysian_ringgit_slots(self):
        """test_malaysian_ringgit_slots."""
        malaysian_ringgit = MalaysianRinggit(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'MalaysianRinggit\' '
                    'object has no attribute \'new_variable\'')):
            malaysian_ringgit.new_variable = 'fail'  # pylint: disable=assigning-non-slot
