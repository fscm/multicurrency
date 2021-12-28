# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Krona currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Iceland Krona representation."""

from multicurrency import IcelandKrona


class TestIcelandKrona:
    """IcelandKrona currency tests."""

    def test_iceland_krona(self):
        """test_iceland_krona."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        iceland_krona = IcelandKrona(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iceland_krona.amount == decimal
        assert iceland_krona.numeric_code == '352'
        assert iceland_krona.alpha_code == 'ISK'
        assert iceland_krona.decimal_places == 0
        assert iceland_krona.decimal_sign == ','
        assert iceland_krona.grouping_places == 3
        assert iceland_krona.grouping_sign == '.'
        assert not iceland_krona.international
        assert iceland_krona.symbol == 'Kr'
        assert not iceland_krona.symbol_ahead
        assert iceland_krona.symbol_separator == '\u00A0'
        assert iceland_krona.localized_symbol == 'Kr'
        assert iceland_krona.convertion == ''
        assert iceland_krona.__hash__() == hash(
            (iceland_krona.__class__, decimal, 'ISK', '352'))
        assert iceland_krona.__repr__() == (
            'IcelandKrona(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ISK", '
            'symbol: "Kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kr", '
            'numeric_code: "352", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert iceland_krona.__str__() == '0 Kr'

    def test_iceland_krona_negative(self):
        """test_iceland_krona_negative."""
        amount = -100
        iceland_krona = IcelandKrona(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iceland_krona.numeric_code == '352'
        assert iceland_krona.alpha_code == 'ISK'
        assert iceland_krona.decimal_places == 0
        assert iceland_krona.decimal_sign == ','
        assert iceland_krona.grouping_places == 3
        assert iceland_krona.grouping_sign == '.'
        assert not iceland_krona.international
        assert iceland_krona.symbol == 'Kr'
        assert not iceland_krona.symbol_ahead
        assert iceland_krona.symbol_separator == '\u00A0'
        assert iceland_krona.localized_symbol == 'Kr'
        assert iceland_krona.convertion == ''
        assert iceland_krona.__hash__() == hash(
            (iceland_krona.__class__, decimal, 'ISK', '352'))
        assert iceland_krona.__repr__() == (
            'IcelandKrona(amount: -100, '
            'alpha_code: "ISK", '
            'symbol: "Kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Kr", '
            'numeric_code: "352", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert iceland_krona.__str__() == '-100 Kr'

    def test_iceland_krona_custom(self):
        """test_iceland_krona_custom."""
        amount = 1000
        iceland_krona = IcelandKrona(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert iceland_krona.amount == decimal
        assert iceland_krona.numeric_code == '352'
        assert iceland_krona.alpha_code == 'ISK'
        assert iceland_krona.decimal_places == 5
        assert iceland_krona.decimal_sign == '.'
        assert iceland_krona.grouping_places == 2
        assert iceland_krona.grouping_sign == ','
        assert iceland_krona.international
        assert iceland_krona.symbol == 'Kr'
        assert not iceland_krona.symbol_ahead
        assert iceland_krona.symbol_separator == '_'
        assert iceland_krona.localized_symbol == 'Kr'
        assert iceland_krona.convertion == ''
        assert iceland_krona.__hash__() == hash(
            (iceland_krona.__class__, decimal, 'ISK', '352'))
        assert iceland_krona.__repr__() == (
            'IcelandKrona(amount: 1000, '
            'alpha_code: "ISK", '
            'symbol: "Kr", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Kr", '
            'numeric_code: "352", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert iceland_krona.__str__() == 'ISK 10,00.00000'

    def test_iceland_krona_changed(self):
        """test_ciceland_krona_changed."""
        iceland_krona = IcelandKrona(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iceland_krona.international = True

    def test_iceland_krona_math_add(self):
        """test_iceland_krona_math_add."""
        iceland_krona_one = IcelandKrona(amount=1)
        iceland_krona_two = IcelandKrona(amount=2)
        iceland_krona_three = IcelandKrona(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ISK and OTHER.'):
            _ = iceland_krona_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'krona.IcelandKrona\'> '
                    'and <class \'str\'>.')):
            _ = iceland_krona_one.__add__('1.00')
        assert (
            iceland_krona_one +
            iceland_krona_two) == iceland_krona_three

    def test_iceland_krona_slots(self):
        """test_iceland_krona_slots."""
        iceland_krona = IcelandKrona(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IcelandKrona\' '
                    'object has no attribute \'new_variable\'')):
            iceland_krona.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Swedish Krona representation."""

from multicurrency import SwedishKrona


class TestSwedishKrona:
    """SwedishKrona currency tests."""

    def test_swedish_krona(self):
        """test_swedish_krona."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        swedish_krona = SwedishKrona(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swedish_krona.amount == decimal
        assert swedish_krona.numeric_code == '752'
        assert swedish_krona.alpha_code == 'SEK'
        assert swedish_krona.decimal_places == 2
        assert swedish_krona.decimal_sign == ','
        assert swedish_krona.grouping_places == 3
        assert swedish_krona.grouping_sign == '\u202F'
        assert not swedish_krona.international
        assert swedish_krona.symbol == 'kr'
        assert not swedish_krona.symbol_ahead
        assert swedish_krona.symbol_separator == '\u00A0'
        assert swedish_krona.localized_symbol == 'kr'
        assert swedish_krona.convertion == ''
        assert swedish_krona.__hash__() == hash(
            (swedish_krona.__class__, decimal, 'SEK', '752'))
        assert swedish_krona.__repr__() == (
            'SwedishKrona(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SEK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "752", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert swedish_krona.__str__() == '0,14 kr'

    def test_swedish_krona_negative(self):
        """test_swedish_krona_negative."""
        amount = -100
        swedish_krona = SwedishKrona(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swedish_krona.numeric_code == '752'
        assert swedish_krona.alpha_code == 'SEK'
        assert swedish_krona.decimal_places == 2
        assert swedish_krona.decimal_sign == ','
        assert swedish_krona.grouping_places == 3
        assert swedish_krona.grouping_sign == '\u202F'
        assert not swedish_krona.international
        assert swedish_krona.symbol == 'kr'
        assert not swedish_krona.symbol_ahead
        assert swedish_krona.symbol_separator == '\u00A0'
        assert swedish_krona.localized_symbol == 'kr'
        assert swedish_krona.convertion == ''
        assert swedish_krona.__hash__() == hash(
            (swedish_krona.__class__, decimal, 'SEK', '752'))
        assert swedish_krona.__repr__() == (
            'SwedishKrona(amount: -100, '
            'alpha_code: "SEK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "kr", '
            'numeric_code: "752", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert swedish_krona.__str__() == '-100,00 kr'

    def test_swedish_krona_custom(self):
        """test_swedish_krona_custom."""
        amount = 1000
        swedish_krona = SwedishKrona(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert swedish_krona.amount == decimal
        assert swedish_krona.numeric_code == '752'
        assert swedish_krona.alpha_code == 'SEK'
        assert swedish_krona.decimal_places == 5
        assert swedish_krona.decimal_sign == '\u202F'
        assert swedish_krona.grouping_places == 2
        assert swedish_krona.grouping_sign == ','
        assert swedish_krona.international
        assert swedish_krona.symbol == 'kr'
        assert not swedish_krona.symbol_ahead
        assert swedish_krona.symbol_separator == '_'
        assert swedish_krona.localized_symbol == 'kr'
        assert swedish_krona.convertion == ''
        assert swedish_krona.__hash__() == hash(
            (swedish_krona.__class__, decimal, 'SEK', '752'))
        assert swedish_krona.__repr__() == (
            'SwedishKrona(amount: 1000, '
            'alpha_code: "SEK", '
            'symbol: "kr", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "kr", '
            'numeric_code: "752", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert swedish_krona.__str__() == 'SEK 10,00.00000'

    def test_swedish_krona_changed(self):
        """test_cswedish_krona_changed."""
        swedish_krona = SwedishKrona(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swedish_krona.international = True

    def test_swedish_krona_math_add(self):
        """test_swedish_krona_math_add."""
        swedish_krona_one = SwedishKrona(amount=1)
        swedish_krona_two = SwedishKrona(amount=2)
        swedish_krona_three = SwedishKrona(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SEK and OTHER.'):
            _ = swedish_krona_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'krona.SwedishKrona\'> '
                    'and <class \'str\'>.')):
            _ = swedish_krona_one.__add__('1.00')
        assert (
            swedish_krona_one +
            swedish_krona_two) == swedish_krona_three

    def test_swedish_krona_slots(self):
        """test_swedish_krona_slots."""
        swedish_krona = SwedishKrona(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SwedishKrona\' '
                    'object has no attribute \'new_variable\'')):
            swedish_krona.new_variable = 'fail'  # pylint: disable=assigning-non-slot
