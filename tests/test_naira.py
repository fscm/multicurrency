# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Naira currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Naira representation."""

from multicurrency import Naira


class TestNaira:
    """Naira currency tests."""

    def test_naira(self):
        """test_naira."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        naira = Naira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert naira.amount == decimal
        assert naira.numeric_code == '566'
        assert naira.alpha_code == 'NGN'
        assert naira.decimal_places == 2
        assert naira.decimal_sign == '.'
        assert naira.grouping_places == 3
        assert naira.grouping_sign == ','
        assert not naira.international
        assert naira.symbol == '₦'
        assert naira.symbol_ahead
        assert naira.symbol_separator == ''
        assert naira.localized_symbol == '₦'
        assert naira.convertion == ''
        assert naira.__hash__() == hash(
            (naira.__class__, decimal, 'NGN', '566'))
        assert naira.__repr__() == (
            'Naira(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NGN", '
            'symbol: "₦", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₦", '
            'numeric_code: "566", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert naira.__str__() == '₦0.14'

    def test_naira_negative(self):
        """test_naira_negative."""
        amount = -100
        naira = Naira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert naira.numeric_code == '566'
        assert naira.alpha_code == 'NGN'
        assert naira.decimal_places == 2
        assert naira.decimal_sign == '.'
        assert naira.grouping_places == 3
        assert naira.grouping_sign == ','
        assert not naira.international
        assert naira.symbol == '₦'
        assert naira.symbol_ahead
        assert naira.symbol_separator == ''
        assert naira.localized_symbol == '₦'
        assert naira.convertion == ''
        assert naira.__hash__() == hash(
            (naira.__class__, decimal, 'NGN', '566'))
        assert naira.__repr__() == (
            'Naira(amount: -100, '
            'alpha_code: "NGN", '
            'symbol: "₦", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₦", '
            'numeric_code: "566", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert naira.__str__() == '₦-100.00'

    def test_naira_custom(self):
        """test_naira_custom."""
        amount = 1000
        naira = Naira(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert naira.amount == decimal
        assert naira.numeric_code == '566'
        assert naira.alpha_code == 'NGN'
        assert naira.decimal_places == 5
        assert naira.decimal_sign == ','
        assert naira.grouping_places == 2
        assert naira.grouping_sign == '.'
        assert naira.international
        assert naira.symbol == '₦'
        assert not naira.symbol_ahead
        assert naira.symbol_separator == '_'
        assert naira.localized_symbol == '₦'
        assert naira.convertion == ''
        assert naira.__hash__() == hash(
            (naira.__class__, decimal, 'NGN', '566'))
        assert naira.__repr__() == (
            'Naira(amount: 1000, '
            'alpha_code: "NGN", '
            'symbol: "₦", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₦", '
            'numeric_code: "566", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert naira.__str__() == 'NGN 10,00.00000'

    def test_naira_changed(self):
        """test_cnaira_changed."""
        naira = Naira(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            naira.international = True

    def test_naira_math_add(self):
        """test_naira_math_add."""
        naira_one = Naira(amount=1)
        naira_two = Naira(amount=2)
        naira_three = Naira(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NGN and OTHER.'):
            _ = naira_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'naira.Naira\'> '
                    'and <class \'str\'>.')):
            _ = naira_one.__add__('1.00')
        assert (
            naira_one +
            naira_two) == naira_three

    def test_naira_slots(self):
        """test_naira_slots."""
        naira = Naira(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Naira\' '
                    'object has no attribute \'new_variable\'')):
            naira.new_variable = 'fail'  # pylint: disable=assigning-non-slot
