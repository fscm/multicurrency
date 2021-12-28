# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lempira currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Lempira representation."""

from multicurrency import Lempira


class TestLempira:
    """Lempira currency tests."""

    def test_lempira(self):
        """test_lempira."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        lempira = Lempira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lempira.amount == decimal
        assert lempira.numeric_code == '340'
        assert lempira.alpha_code == 'HNL'
        assert lempira.decimal_places == 2
        assert lempira.decimal_sign == '.'
        assert lempira.grouping_places == 3
        assert lempira.grouping_sign == ','
        assert not lempira.international
        assert lempira.symbol == 'L'
        assert lempira.symbol_ahead
        assert lempira.symbol_separator == '\u00A0'
        assert lempira.localized_symbol == 'L'
        assert lempira.convertion == ''
        assert lempira.__hash__() == hash(
            (lempira.__class__, decimal, 'HNL', '340'))
        assert lempira.__repr__() == (
            'Lempira(amount: 0.1428571428571428571428571429, '
            'alpha_code: "HNL", '
            'symbol: "L", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "340", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert lempira.__str__() == 'L 0.14'

    def test_lempira_negative(self):
        """test_lempira_negative."""
        amount = -100
        lempira = Lempira(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lempira.numeric_code == '340'
        assert lempira.alpha_code == 'HNL'
        assert lempira.decimal_places == 2
        assert lempira.decimal_sign == '.'
        assert lempira.grouping_places == 3
        assert lempira.grouping_sign == ','
        assert not lempira.international
        assert lempira.symbol == 'L'
        assert lempira.symbol_ahead
        assert lempira.symbol_separator == '\u00A0'
        assert lempira.localized_symbol == 'L'
        assert lempira.convertion == ''
        assert lempira.__hash__() == hash(
            (lempira.__class__, decimal, 'HNL', '340'))
        assert lempira.__repr__() == (
            'Lempira(amount: -100, '
            'alpha_code: "HNL", '
            'symbol: "L", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "340", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert lempira.__str__() == 'L -100.00'

    def test_lempira_custom(self):
        """test_lempira_custom."""
        amount = 1000
        lempira = Lempira(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert lempira.amount == decimal
        assert lempira.numeric_code == '340'
        assert lempira.alpha_code == 'HNL'
        assert lempira.decimal_places == 5
        assert lempira.decimal_sign == ','
        assert lempira.grouping_places == 2
        assert lempira.grouping_sign == '.'
        assert lempira.international
        assert lempira.symbol == 'L'
        assert not lempira.symbol_ahead
        assert lempira.symbol_separator == '_'
        assert lempira.localized_symbol == 'L'
        assert lempira.convertion == ''
        assert lempira.__hash__() == hash(
            (lempira.__class__, decimal, 'HNL', '340'))
        assert lempira.__repr__() == (
            'Lempira(amount: 1000, '
            'alpha_code: "HNL", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "L", '
            'numeric_code: "340", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert lempira.__str__() == 'HNL 10,00.00000'

    def test_lempira_changed(self):
        """test_clempira_changed."""
        lempira = Lempira(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lempira.international = True

    def test_lempira_math_add(self):
        """test_lempira_math_add."""
        lempira_one = Lempira(amount=1)
        lempira_two = Lempira(amount=2)
        lempira_three = Lempira(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency HNL and OTHER.'):
            _ = lempira_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'lempira.Lempira\'> '
                    'and <class \'str\'>.')):
            _ = lempira_one.__add__('1.00')
        assert (
            lempira_one +
            lempira_two) == lempira_three

    def test_lempira_slots(self):
        """test_lempira_slots."""
        lempira = Lempira(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Lempira\' '
                    'object has no attribute \'new_variable\'')):
            lempira.new_variable = 'fail'  # pylint: disable=assigning-non-slot
