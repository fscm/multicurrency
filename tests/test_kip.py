# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kip currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Kip representation."""

from multicurrency import Kip


class TestKip:
    """Kip currency tests."""

    def test_kip(self):
        """test_kip."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        kip = Kip(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kip.amount == decimal
        assert kip.numeric_code == '418'
        assert kip.alpha_code == 'LAK'
        assert kip.decimal_places == 2
        assert kip.decimal_sign == ','
        assert kip.grouping_places == 3
        assert kip.grouping_sign == '.'
        assert not kip.international
        assert kip.symbol == '₭'
        assert kip.symbol_ahead
        assert kip.symbol_separator == ''
        assert kip.localized_symbol == '₭'
        assert kip.convertion == ''
        assert kip.__hash__() == hash(
            (kip.__class__, decimal, 'LAK', '418'))
        assert kip.__repr__() == (
            'Kip(amount: 0.1428571428571428571428571429, '
            'alpha_code: "LAK", '
            'symbol: "₭", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₭", '
            'numeric_code: "418", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert kip.__str__() == '₭0,14'

    def test_kip_negative(self):
        """test_kip_negative."""
        amount = -100
        kip = Kip(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kip.numeric_code == '418'
        assert kip.alpha_code == 'LAK'
        assert kip.decimal_places == 2
        assert kip.decimal_sign == ','
        assert kip.grouping_places == 3
        assert kip.grouping_sign == '.'
        assert not kip.international
        assert kip.symbol == '₭'
        assert kip.symbol_ahead
        assert kip.symbol_separator == ''
        assert kip.localized_symbol == '₭'
        assert kip.convertion == ''
        assert kip.__hash__() == hash(
            (kip.__class__, decimal, 'LAK', '418'))
        assert kip.__repr__() == (
            'Kip(amount: -100, '
            'alpha_code: "LAK", '
            'symbol: "₭", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₭", '
            'numeric_code: "418", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert kip.__str__() == '₭-100,00'

    def test_kip_custom(self):
        """test_kip_custom."""
        amount = 1000
        kip = Kip(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert kip.amount == decimal
        assert kip.numeric_code == '418'
        assert kip.alpha_code == 'LAK'
        assert kip.decimal_places == 5
        assert kip.decimal_sign == '.'
        assert kip.grouping_places == 2
        assert kip.grouping_sign == ','
        assert kip.international
        assert kip.symbol == '₭'
        assert not kip.symbol_ahead
        assert kip.symbol_separator == '_'
        assert kip.localized_symbol == '₭'
        assert kip.convertion == ''
        assert kip.__hash__() == hash(
            (kip.__class__, decimal, 'LAK', '418'))
        assert kip.__repr__() == (
            'Kip(amount: 1000, '
            'alpha_code: "LAK", '
            'symbol: "₭", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₭", '
            'numeric_code: "418", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert kip.__str__() == 'LAK 10,00.00000'

    def test_kip_changed(self):
        """test_ckip_changed."""
        kip = Kip(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kip.international = True

    def test_kip_math_add(self):
        """test_kip_math_add."""
        kip_one = Kip(amount=1)
        kip_two = Kip(amount=2)
        kip_three = Kip(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency LAK and OTHER.'):
            _ = kip_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'kip.Kip\'> '
                    'and <class \'str\'>.')):
            _ = kip_one.__add__('1.00')
        assert (
            kip_one +
            kip_two) == kip_three

    def test_kip_slots(self):
        """test_kip_slots."""
        kip = Kip(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Kip\' '
                    'object has no attribute \'new_variable\'')):
            kip.new_variable = 'fail'  # pylint: disable=assigning-non-slot
