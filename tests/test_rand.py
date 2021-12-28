# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Rand representation."""

from multicurrency import Rand


class TestRand:
    """Rand currency tests."""

    def test_rand(self):
        """test_rand."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        rand = Rand(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand.amount == decimal
        assert rand.numeric_code == '710'
        assert rand.alpha_code == 'ZAR'
        assert rand.decimal_places == 2
        assert rand.decimal_sign == '.'
        assert rand.grouping_places == 3
        assert rand.grouping_sign == '\u202F'
        assert not rand.international
        assert rand.symbol == 'R'
        assert rand.symbol_ahead
        assert rand.symbol_separator == '\u00A0'
        assert rand.localized_symbol == 'R'
        assert rand.convertion == ''
        assert rand.__hash__() == hash(
            (rand.__class__, decimal, 'ZAR', '710'))
        assert rand.__repr__() == (
            'Rand(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "R", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand.__str__() == 'R 0.14'

    def test_rand_negative(self):
        """test_rand_negative."""
        amount = -100
        rand = Rand(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand.numeric_code == '710'
        assert rand.alpha_code == 'ZAR'
        assert rand.decimal_places == 2
        assert rand.decimal_sign == '.'
        assert rand.grouping_places == 3
        assert rand.grouping_sign == '\u202F'
        assert not rand.international
        assert rand.symbol == 'R'
        assert rand.symbol_ahead
        assert rand.symbol_separator == '\u00A0'
        assert rand.localized_symbol == 'R'
        assert rand.convertion == ''
        assert rand.__hash__() == hash(
            (rand.__class__, decimal, 'ZAR', '710'))
        assert rand.__repr__() == (
            'Rand(amount: -100, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "R", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand.__str__() == 'R -100.00'

    def test_rand_custom(self):
        """test_rand_custom."""
        amount = 1000
        rand = Rand(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert rand.amount == decimal
        assert rand.numeric_code == '710'
        assert rand.alpha_code == 'ZAR'
        assert rand.decimal_places == 5
        assert rand.decimal_sign == '\u202F'
        assert rand.grouping_places == 2
        assert rand.grouping_sign == '.'
        assert rand.international
        assert rand.symbol == 'R'
        assert not rand.symbol_ahead
        assert rand.symbol_separator == '_'
        assert rand.localized_symbol == 'R'
        assert rand.convertion == ''
        assert rand.__hash__() == hash(
            (rand.__class__, decimal, 'ZAR', '710'))
        assert rand.__repr__() == (
            'Rand(amount: 1000, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "R", '
            'numeric_code: "710", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert rand.__str__() == 'ZAR 10,00.00000'

    def test_rand_changed(self):
        """test_crand_changed."""
        rand = Rand(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand.international = True

    def test_rand_math_add(self):
        """test_rand_math_add."""
        rand_one = Rand(amount=1)
        rand_two = Rand(amount=2)
        rand_three = Rand(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZAR and OTHER.'):
            _ = rand_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rand.Rand\'> '
                    'and <class \'str\'>.')):
            _ = rand_one.__add__('1.00')
        assert (
            rand_one +
            rand_two) == rand_three

    def test_rand_slots(self):
        """test_rand_slots."""
        rand = Rand(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Rand\' '
                    'object has no attribute \'new_variable\'')):
            rand.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Rand LS representation."""

from multicurrency import RandLS


class TestRandLS:
    """RandLS currency tests."""

    def test_rand_ls(self):
        """test_rand_ls."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        rand_ls = RandLS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_ls.amount == decimal
        assert rand_ls.numeric_code == '710'
        assert rand_ls.alpha_code == 'ZAR'
        assert rand_ls.decimal_places == 2
        assert rand_ls.decimal_sign == '.'
        assert rand_ls.grouping_places == 3
        assert rand_ls.grouping_sign == ','
        assert not rand_ls.international
        assert rand_ls.symbol == 'R'
        assert rand_ls.symbol_ahead
        assert rand_ls.symbol_separator == '\u00A0'
        assert rand_ls.localized_symbol == 'LSR'
        assert rand_ls.convertion == ''
        assert rand_ls.__hash__() == hash(
            (rand_ls.__class__, decimal, 'ZAR', '710'))
        assert rand_ls.__repr__() == (
            'RandLS(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LSR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert rand_ls.__str__() == 'R 0.14'

    def test_rand_ls_negative(self):
        """test_rand_ls_negative."""
        amount = -100
        rand_ls = RandLS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_ls.numeric_code == '710'
        assert rand_ls.alpha_code == 'ZAR'
        assert rand_ls.decimal_places == 2
        assert rand_ls.decimal_sign == '.'
        assert rand_ls.grouping_places == 3
        assert rand_ls.grouping_sign == ','
        assert not rand_ls.international
        assert rand_ls.symbol == 'R'
        assert rand_ls.symbol_ahead
        assert rand_ls.symbol_separator == '\u00A0'
        assert rand_ls.localized_symbol == 'LSR'
        assert rand_ls.convertion == ''
        assert rand_ls.__hash__() == hash(
            (rand_ls.__class__, decimal, 'ZAR', '710'))
        assert rand_ls.__repr__() == (
            'RandLS(amount: -100, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LSR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert rand_ls.__str__() == 'R -100.00'

    def test_rand_ls_custom(self):
        """test_rand_ls_custom."""
        amount = 1000
        rand_ls = RandLS(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert rand_ls.amount == decimal
        assert rand_ls.numeric_code == '710'
        assert rand_ls.alpha_code == 'ZAR'
        assert rand_ls.decimal_places == 5
        assert rand_ls.decimal_sign == ','
        assert rand_ls.grouping_places == 2
        assert rand_ls.grouping_sign == '.'
        assert rand_ls.international
        assert rand_ls.symbol == 'R'
        assert not rand_ls.symbol_ahead
        assert rand_ls.symbol_separator == '_'
        assert rand_ls.localized_symbol == 'LSR'
        assert rand_ls.convertion == ''
        assert rand_ls.__hash__() == hash(
            (rand_ls.__class__, decimal, 'ZAR', '710'))
        assert rand_ls.__repr__() == (
            'RandLS(amount: 1000, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LSR", '
            'numeric_code: "710", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert rand_ls.__str__() == 'ZAR 10,00.00000'

    def test_rand_ls_changed(self):
        """test_crand_ls_changed."""
        rand_ls = RandLS(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_ls.international = True

    def test_rand_ls_math_add(self):
        """test_rand_ls_math_add."""
        rand_ls_one = RandLS(amount=1)
        rand_ls_two = RandLS(amount=2)
        rand_ls_three = RandLS(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZAR and OTHER.'):
            _ = rand_ls_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rand.RandLS\'> '
                    'and <class \'str\'>.')):
            _ = rand_ls_one.__add__('1.00')
        assert (
            rand_ls_one +
            rand_ls_two) == rand_ls_three

    def test_rand_ls_slots(self):
        """test_rand_ls_slots."""
        rand_ls = RandLS(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RandLS\' '
                    'object has no attribute \'new_variable\'')):
            rand_ls.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Rand NA representation."""

from multicurrency import RandNA


class TestRandNA:
    """RandNA currency tests."""

    def test_rand_na(self):
        """test_rand_na."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        rand_na = RandNA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_na.amount == decimal
        assert rand_na.numeric_code == '710'
        assert rand_na.alpha_code == 'ZAR'
        assert rand_na.decimal_places == 2
        assert rand_na.decimal_sign == '.'
        assert rand_na.grouping_places == 3
        assert rand_na.grouping_sign == '\u202F'
        assert not rand_na.international
        assert rand_na.symbol == 'R'
        assert rand_na.symbol_ahead
        assert rand_na.symbol_separator == '\u00A0'
        assert rand_na.localized_symbol == 'NAR'
        assert rand_na.convertion == ''
        assert rand_na.__hash__() == hash(
            (rand_na.__class__, decimal, 'ZAR', '710'))
        assert rand_na.__repr__() == (
            'RandNA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NAR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand_na.__str__() == 'R 0.14'

    def test_rand_na_negative(self):
        """test_rand_na_negative."""
        amount = -100
        rand_na = RandNA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_na.numeric_code == '710'
        assert rand_na.alpha_code == 'ZAR'
        assert rand_na.decimal_places == 2
        assert rand_na.decimal_sign == '.'
        assert rand_na.grouping_places == 3
        assert rand_na.grouping_sign == '\u202F'
        assert not rand_na.international
        assert rand_na.symbol == 'R'
        assert rand_na.symbol_ahead
        assert rand_na.symbol_separator == '\u00A0'
        assert rand_na.localized_symbol == 'NAR'
        assert rand_na.convertion == ''
        assert rand_na.__hash__() == hash(
            (rand_na.__class__, decimal, 'ZAR', '710'))
        assert rand_na.__repr__() == (
            'RandNA(amount: -100, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NAR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand_na.__str__() == 'R -100.00'

    def test_rand_na_custom(self):
        """test_rand_na_custom."""
        amount = 1000
        rand_na = RandNA(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert rand_na.amount == decimal
        assert rand_na.numeric_code == '710'
        assert rand_na.alpha_code == 'ZAR'
        assert rand_na.decimal_places == 5
        assert rand_na.decimal_sign == '\u202F'
        assert rand_na.grouping_places == 2
        assert rand_na.grouping_sign == '.'
        assert rand_na.international
        assert rand_na.symbol == 'R'
        assert not rand_na.symbol_ahead
        assert rand_na.symbol_separator == '_'
        assert rand_na.localized_symbol == 'NAR'
        assert rand_na.convertion == ''
        assert rand_na.__hash__() == hash(
            (rand_na.__class__, decimal, 'ZAR', '710'))
        assert rand_na.__repr__() == (
            'RandNA(amount: 1000, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NAR", '
            'numeric_code: "710", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert rand_na.__str__() == 'ZAR 10,00.00000'

    def test_rand_na_changed(self):
        """test_crand_na_changed."""
        rand_na = RandNA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_na.international = True

    def test_rand_na_math_add(self):
        """test_rand_na_math_add."""
        rand_na_one = RandNA(amount=1)
        rand_na_two = RandNA(amount=2)
        rand_na_three = RandNA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZAR and OTHER.'):
            _ = rand_na_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rand.RandNA\'> '
                    'and <class \'str\'>.')):
            _ = rand_na_one.__add__('1.00')
        assert (
            rand_na_one +
            rand_na_two) == rand_na_three

    def test_rand_na_slots(self):
        """test_rand_na_slots."""
        rand_na = RandNA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RandNA\' '
                    'object has no attribute \'new_variable\'')):
            rand_na.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Rand ZA representation."""

from multicurrency import RandZA


class TestRandZA:
    """RandZA currency tests."""

    def test_rand_za(self):
        """test_rand_za."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        rand_za = RandZA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_za.amount == decimal
        assert rand_za.numeric_code == '710'
        assert rand_za.alpha_code == 'ZAR'
        assert rand_za.decimal_places == 2
        assert rand_za.decimal_sign == '.'
        assert rand_za.grouping_places == 3
        assert rand_za.grouping_sign == '\u202F'
        assert not rand_za.international
        assert rand_za.symbol == 'R'
        assert rand_za.symbol_ahead
        assert rand_za.symbol_separator == '\u00A0'
        assert rand_za.localized_symbol == 'ZAR'
        assert rand_za.convertion == ''
        assert rand_za.__hash__() == hash(
            (rand_za.__class__, decimal, 'ZAR', '710'))
        assert rand_za.__repr__() == (
            'RandZA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZAR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand_za.__str__() == 'R 0.14'

    def test_rand_za_negative(self):
        """test_rand_za_negative."""
        amount = -100
        rand_za = RandZA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rand_za.numeric_code == '710'
        assert rand_za.alpha_code == 'ZAR'
        assert rand_za.decimal_places == 2
        assert rand_za.decimal_sign == '.'
        assert rand_za.grouping_places == 3
        assert rand_za.grouping_sign == '\u202F'
        assert not rand_za.international
        assert rand_za.symbol == 'R'
        assert rand_za.symbol_ahead
        assert rand_za.symbol_separator == '\u00A0'
        assert rand_za.localized_symbol == 'ZAR'
        assert rand_za.convertion == ''
        assert rand_za.__hash__() == hash(
            (rand_za.__class__, decimal, 'ZAR', '710'))
        assert rand_za.__repr__() == (
            'RandZA(amount: -100, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZAR", '
            'numeric_code: "710", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert rand_za.__str__() == 'R -100.00'

    def test_rand_za_custom(self):
        """test_rand_za_custom."""
        amount = 1000
        rand_za = RandZA(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert rand_za.amount == decimal
        assert rand_za.numeric_code == '710'
        assert rand_za.alpha_code == 'ZAR'
        assert rand_za.decimal_places == 5
        assert rand_za.decimal_sign == '\u202F'
        assert rand_za.grouping_places == 2
        assert rand_za.grouping_sign == '.'
        assert rand_za.international
        assert rand_za.symbol == 'R'
        assert not rand_za.symbol_ahead
        assert rand_za.symbol_separator == '_'
        assert rand_za.localized_symbol == 'ZAR'
        assert rand_za.convertion == ''
        assert rand_za.__hash__() == hash(
            (rand_za.__class__, decimal, 'ZAR', '710'))
        assert rand_za.__repr__() == (
            'RandZA(amount: 1000, '
            'alpha_code: "ZAR", '
            'symbol: "R", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ZAR", '
            'numeric_code: "710", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert rand_za.__str__() == 'ZAR 10,00.00000'

    def test_rand_za_changed(self):
        """test_crand_za_changed."""
        rand_za = RandZA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rand_za.international = True

    def test_rand_za_math_add(self):
        """test_rand_za_math_add."""
        rand_za_one = RandZA(amount=1)
        rand_za_two = RandZA(amount=2)
        rand_za_three = RandZA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZAR and OTHER.'):
            _ = rand_za_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rand.RandZA\'> '
                    'and <class \'str\'>.')):
            _ = rand_za_one.__add__('1.00')
        assert (
            rand_za_one +
            rand_za_two) == rand_za_three

    def test_rand_za_slots(self):
        """test_rand_za_slots."""
        rand_za = RandZA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RandZA\' '
                    'object has no attribute \'new_variable\'')):
            rand_za.new_variable = 'fail'  # pylint: disable=assigning-non-slot
