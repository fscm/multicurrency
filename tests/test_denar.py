# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Denar currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Denar representation."""

from multicurrency import Denar


class TestDenar:
    """Denar currency tests."""

    def test_denar(self):
        """test_denar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        denar = Denar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert denar.amount == decimal
        assert denar.numeric_code == '807'
        assert denar.alpha_code == 'MKD'
        assert denar.decimal_places == 2
        assert denar.decimal_sign == ','
        assert denar.grouping_places == 3
        assert denar.grouping_sign == '.'
        assert not denar.international
        assert denar.symbol == 'ден.'
        assert not denar.symbol_ahead
        assert denar.symbol_separator == '\u00A0'
        assert denar.localized_symbol == 'ден.'
        assert denar.convertion == ''
        assert denar.__hash__() == hash(
            (denar.__class__, decimal, 'MKD', '807'))
        assert denar.__repr__() == (
            'Denar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MKD", '
            'symbol: "ден.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ден.", '
            'numeric_code: "807", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert denar.__str__() == '0,14 ден.'

    def test_denar_negative(self):
        """test_denar_negative."""
        amount = -100
        denar = Denar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert denar.numeric_code == '807'
        assert denar.alpha_code == 'MKD'
        assert denar.decimal_places == 2
        assert denar.decimal_sign == ','
        assert denar.grouping_places == 3
        assert denar.grouping_sign == '.'
        assert not denar.international
        assert denar.symbol == 'ден.'
        assert not denar.symbol_ahead
        assert denar.symbol_separator == '\u00A0'
        assert denar.localized_symbol == 'ден.'
        assert denar.convertion == ''
        assert denar.__hash__() == hash(
            (denar.__class__, decimal, 'MKD', '807'))
        assert denar.__repr__() == (
            'Denar(amount: -100, '
            'alpha_code: "MKD", '
            'symbol: "ден.", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ден.", '
            'numeric_code: "807", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert denar.__str__() == '-100,00 ден.'

    def test_denar_custom(self):
        """test_denar_custom."""
        amount = 1000
        denar = Denar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert denar.amount == decimal
        assert denar.numeric_code == '807'
        assert denar.alpha_code == 'MKD'
        assert denar.decimal_places == 5
        assert denar.decimal_sign == '.'
        assert denar.grouping_places == 2
        assert denar.grouping_sign == ','
        assert denar.international
        assert denar.symbol == 'ден.'
        assert not denar.symbol_ahead
        assert denar.symbol_separator == '_'
        assert denar.localized_symbol == 'ден.'
        assert denar.convertion == ''
        assert denar.__hash__() == hash(
            (denar.__class__, decimal, 'MKD', '807'))
        assert denar.__repr__() == (
            'Denar(amount: 1000, '
            'alpha_code: "MKD", '
            'symbol: "ден.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ден.", '
            'numeric_code: "807", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert denar.__str__() == 'MKD 10,00.00000'

    def test_denar_changed(self):
        """test_cdenar_changed."""
        denar = Denar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            denar.international = True

    def test_denar_math_add(self):
        """test_denar_math_add."""
        denar_one = Denar(amount=1)
        denar_two = Denar(amount=2)
        denar_three = Denar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MKD and OTHER.'):
            _ = denar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'denar.Denar\'> '
                    'and <class \'str\'>.')):
            _ = denar_one.__add__('1.00')
        assert (
            denar_one +
            denar_two) == denar_three

    def test_denar_slots(self):
        """test_denar_slots."""
        denar = Denar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Denar\' '
                    'object has no attribute \'new_variable\'')):
            denar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
