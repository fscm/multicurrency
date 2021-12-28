# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Baht currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Baht representation."""

from multicurrency import Baht


class TestBaht:
    """Baht currency tests."""

    def test_baht(self):
        """test_baht."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        baht = Baht(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert baht.amount == decimal
        assert baht.numeric_code == '764'
        assert baht.alpha_code == 'THB'
        assert baht.decimal_places == 2
        assert baht.decimal_sign == '.'
        assert baht.grouping_places == 3
        assert baht.grouping_sign == ','
        assert not baht.international
        assert baht.symbol == '฿'
        assert baht.symbol_ahead
        assert baht.symbol_separator == ''
        assert baht.localized_symbol == '฿'
        assert baht.convertion == ''
        assert baht.__hash__() == hash(
            (baht.__class__, decimal, 'THB', '764'))
        assert baht.__repr__() == (
            'Baht(amount: 0.1428571428571428571428571429, '
            'alpha_code: "THB", '
            'symbol: "฿", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "฿", '
            'numeric_code: "764", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert baht.__str__() == '฿0.14'

    def test_baht_negative(self):
        """test_baht_negative."""
        amount = -100
        baht = Baht(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert baht.numeric_code == '764'
        assert baht.alpha_code == 'THB'
        assert baht.decimal_places == 2
        assert baht.decimal_sign == '.'
        assert baht.grouping_places == 3
        assert baht.grouping_sign == ','
        assert not baht.international
        assert baht.symbol == '฿'
        assert baht.symbol_ahead
        assert baht.symbol_separator == ''
        assert baht.localized_symbol == '฿'
        assert baht.convertion == ''
        assert baht.__hash__() == hash(
            (baht.__class__, decimal, 'THB', '764'))
        assert baht.__repr__() == (
            'Baht(amount: -100, '
            'alpha_code: "THB", '
            'symbol: "฿", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "฿", '
            'numeric_code: "764", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert baht.__str__() == '฿-100.00'

    def test_baht_custom(self):
        """test_baht_custom."""
        amount = 1000
        baht = Baht(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert baht.amount == decimal
        assert baht.numeric_code == '764'
        assert baht.alpha_code == 'THB'
        assert baht.decimal_places == 5
        assert baht.decimal_sign == ','
        assert baht.grouping_places == 2
        assert baht.grouping_sign == '.'
        assert baht.international
        assert baht.symbol == '฿'
        assert not baht.symbol_ahead
        assert baht.symbol_separator == '_'
        assert baht.localized_symbol == '฿'
        assert baht.convertion == ''
        assert baht.__hash__() == hash(
            (baht.__class__, decimal, 'THB', '764'))
        assert baht.__repr__() == (
            'Baht(amount: 1000, '
            'alpha_code: "THB", '
            'symbol: "฿", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "฿", '
            'numeric_code: "764", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert baht.__str__() == 'THB 10,00.00000'

    def test_baht_changed(self):
        """test_cbaht_changed."""
        baht = Baht(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            baht.international = True

    def test_baht_math_add(self):
        """test_baht_math_add."""
        baht_one = Baht(amount=1)
        baht_two = Baht(amount=2)
        baht_three = Baht(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency THB and OTHER.'):
            _ = baht_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'baht.Baht\'> '
                    'and <class \'str\'>.')):
            _ = baht_one.__add__('1.00')
        assert (
            baht_one +
            baht_two) == baht_three

    def test_baht_slots(self):
        """test_baht_slots."""
        baht = Baht(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Baht\' '
                    'object has no attribute \'new_variable\'')):
            baht.new_variable = 'fail'  # pylint: disable=assigning-non-slot
