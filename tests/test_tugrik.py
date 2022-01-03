# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tugrik currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Tugrik representation."""

from multicurrency import Tugrik


class TestTugrik:
    """Tugrik currency tests."""

    def test_tugrik(self):
        """test_tugrik."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        tugrik = Tugrik(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tugrik.amount == decimal
        assert tugrik.numeric_code == '496'
        assert tugrik.alpha_code == 'MNT'
        assert tugrik.decimal_places == 2
        assert tugrik.decimal_sign == '.'
        assert tugrik.grouping_places == 3
        assert tugrik.grouping_sign == ','
        assert not tugrik.international
        assert tugrik.symbol == '₮'
        assert tugrik.symbol_ahead
        assert tugrik.symbol_separator == '\u00A0'
        assert tugrik.localized_symbol == '₮'
        assert tugrik.convertion == ''
        assert tugrik.__hash__() == hash(
            (tugrik.__class__, decimal, 'MNT', '496'))
        assert tugrik.__repr__() == (
            'Tugrik(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MNT", '
            'symbol: "₮", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₮", '
            'numeric_code: "496", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tugrik.__str__() == '₮ 0.14'

    def test_tugrik_negative(self):
        """test_tugrik_negative."""
        amount = -100
        tugrik = Tugrik(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tugrik.numeric_code == '496'
        assert tugrik.alpha_code == 'MNT'
        assert tugrik.decimal_places == 2
        assert tugrik.decimal_sign == '.'
        assert tugrik.grouping_places == 3
        assert tugrik.grouping_sign == ','
        assert not tugrik.international
        assert tugrik.symbol == '₮'
        assert tugrik.symbol_ahead
        assert tugrik.symbol_separator == '\u00A0'
        assert tugrik.localized_symbol == '₮'
        assert tugrik.convertion == ''
        assert tugrik.__hash__() == hash(
            (tugrik.__class__, decimal, 'MNT', '496'))
        assert tugrik.__repr__() == (
            'Tugrik(amount: -100, '
            'alpha_code: "MNT", '
            'symbol: "₮", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₮", '
            'numeric_code: "496", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tugrik.__str__() == '₮ -100.00'

    def test_tugrik_custom(self):
        """test_tugrik_custom."""
        amount = 1000
        tugrik = Tugrik(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert tugrik.amount == decimal
        assert tugrik.numeric_code == '496'
        assert tugrik.alpha_code == 'MNT'
        assert tugrik.decimal_places == 5
        assert tugrik.decimal_sign == ','
        assert tugrik.grouping_places == 2
        assert tugrik.grouping_sign == '.'
        assert tugrik.international
        assert tugrik.symbol == '₮'
        assert not tugrik.symbol_ahead
        assert tugrik.symbol_separator == '_'
        assert tugrik.localized_symbol == '₮'
        assert tugrik.convertion == ''
        assert tugrik.__hash__() == hash(
            (tugrik.__class__, decimal, 'MNT', '496'))
        assert tugrik.__repr__() == (
            'Tugrik(amount: 1000, '
            'alpha_code: "MNT", '
            'symbol: "₮", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₮", '
            'numeric_code: "496", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert tugrik.__str__() == 'MNT 10,00.00000'

    def test_tugrik_changed(self):
        """test_ctugrik_changed."""
        tugrik = Tugrik(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tugrik.international = True

    def test_tugrik_math_add(self):
        """test_tugrik_math_add."""
        tugrik_one = Tugrik(amount=1)
        tugrik_two = Tugrik(amount=2)
        tugrik_three = Tugrik(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MNT and OTHER.'):
            _ = tugrik_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'tugrik.Tugrik\'> '
                    'and <class \'str\'>.')):
            _ = tugrik_one.__add__('1.00')
        assert (
            tugrik_one +
            tugrik_two) == tugrik_three

    def test_tugrik_slots(self):
        """test_tugrik_slots."""
        tugrik = Tugrik(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Tugrik\' '
                    'object has no attribute \'new_variable\'')):
            tugrik.new_variable = 'fail'  # pylint: disable=assigning-non-slot
