# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Manat currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Azerbaijanian Manat representation."""

from multicurrency import AzerbaijanianManat


class TestAzerbaijanianManat:
    """AzerbaijanianManat currency tests."""

    def test_azerbaijanian_manat(self):
        """test_azerbaijanian_manat."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        azerbaijanian_manat = AzerbaijanianManat(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert azerbaijanian_manat.amount == decimal
        assert azerbaijanian_manat.numeric_code == '944'
        assert azerbaijanian_manat.alpha_code == 'AZN'
        assert azerbaijanian_manat.decimal_places == 2
        assert azerbaijanian_manat.decimal_sign == ','
        assert azerbaijanian_manat.grouping_places == 3
        assert azerbaijanian_manat.grouping_sign == '.'
        assert not azerbaijanian_manat.international
        assert azerbaijanian_manat.symbol == '₼'
        assert not azerbaijanian_manat.symbol_ahead
        assert azerbaijanian_manat.symbol_separator == '\u00A0'
        assert azerbaijanian_manat.localized_symbol == '₼'
        assert azerbaijanian_manat.convertion == ''
        assert azerbaijanian_manat.__hash__() == hash(
            (azerbaijanian_manat.__class__, decimal, 'AZN', '944'))
        assert azerbaijanian_manat.__repr__() == (
            'AzerbaijanianManat(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AZN", '
            'symbol: "₼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₼", '
            'numeric_code: "944", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert azerbaijanian_manat.__str__() == '0,14 ₼'

    def test_azerbaijanian_manat_negative(self):
        """test_azerbaijanian_manat_negative."""
        amount = -100
        azerbaijanian_manat = AzerbaijanianManat(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert azerbaijanian_manat.numeric_code == '944'
        assert azerbaijanian_manat.alpha_code == 'AZN'
        assert azerbaijanian_manat.decimal_places == 2
        assert azerbaijanian_manat.decimal_sign == ','
        assert azerbaijanian_manat.grouping_places == 3
        assert azerbaijanian_manat.grouping_sign == '.'
        assert not azerbaijanian_manat.international
        assert azerbaijanian_manat.symbol == '₼'
        assert not azerbaijanian_manat.symbol_ahead
        assert azerbaijanian_manat.symbol_separator == '\u00A0'
        assert azerbaijanian_manat.localized_symbol == '₼'
        assert azerbaijanian_manat.convertion == ''
        assert azerbaijanian_manat.__hash__() == hash(
            (azerbaijanian_manat.__class__, decimal, 'AZN', '944'))
        assert azerbaijanian_manat.__repr__() == (
            'AzerbaijanianManat(amount: -100, '
            'alpha_code: "AZN", '
            'symbol: "₼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₼", '
            'numeric_code: "944", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert azerbaijanian_manat.__str__() == '-100,00 ₼'

    def test_azerbaijanian_manat_custom(self):
        """test_azerbaijanian_manat_custom."""
        amount = 1000
        azerbaijanian_manat = AzerbaijanianManat(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert azerbaijanian_manat.amount == decimal
        assert azerbaijanian_manat.numeric_code == '944'
        assert azerbaijanian_manat.alpha_code == 'AZN'
        assert azerbaijanian_manat.decimal_places == 5
        assert azerbaijanian_manat.decimal_sign == '.'
        assert azerbaijanian_manat.grouping_places == 2
        assert azerbaijanian_manat.grouping_sign == ','
        assert azerbaijanian_manat.international
        assert azerbaijanian_manat.symbol == '₼'
        assert not azerbaijanian_manat.symbol_ahead
        assert azerbaijanian_manat.symbol_separator == '_'
        assert azerbaijanian_manat.localized_symbol == '₼'
        assert azerbaijanian_manat.convertion == ''
        assert azerbaijanian_manat.__hash__() == hash(
            (azerbaijanian_manat.__class__, decimal, 'AZN', '944'))
        assert azerbaijanian_manat.__repr__() == (
            'AzerbaijanianManat(amount: 1000, '
            'alpha_code: "AZN", '
            'symbol: "₼", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₼", '
            'numeric_code: "944", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert azerbaijanian_manat.__str__() == 'AZN 10,00.00000'

    def test_azerbaijanian_manat_changed(self):
        """test_cazerbaijanian_manat_changed."""
        azerbaijanian_manat = AzerbaijanianManat(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            azerbaijanian_manat.international = True

    def test_azerbaijanian_manat_math_add(self):
        """test_azerbaijanian_manat_math_add."""
        azerbaijanian_manat_one = AzerbaijanianManat(amount=1)
        azerbaijanian_manat_two = AzerbaijanianManat(amount=2)
        azerbaijanian_manat_three = AzerbaijanianManat(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AZN and OTHER.'):
            _ = azerbaijanian_manat_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'manat.AzerbaijanianManat\'> '
                    'and <class \'str\'>.')):
            _ = azerbaijanian_manat_one.__add__('1.00')
        assert (
            azerbaijanian_manat_one +
            azerbaijanian_manat_two) == azerbaijanian_manat_three

    def test_azerbaijanian_manat_slots(self):
        """test_azerbaijanian_manat_slots."""
        azerbaijanian_manat = AzerbaijanianManat(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AzerbaijanianManat\' '
                    'object has no attribute \'new_variable\'')):
            azerbaijanian_manat.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Manat representation."""

from multicurrency import Manat


class TestManat:
    """Manat currency tests."""

    def test_manat(self):
        """test_manat."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        manat = Manat(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert manat.amount == decimal
        assert manat.numeric_code == '934'
        assert manat.alpha_code == 'TMT'
        assert manat.decimal_places == 2
        assert manat.decimal_sign == ','
        assert manat.grouping_places == 3
        assert manat.grouping_sign == '\u202F'
        assert not manat.international
        assert manat.symbol == 'm'
        assert not manat.symbol_ahead
        assert manat.symbol_separator == '\u00A0'
        assert manat.localized_symbol == 'm'
        assert manat.convertion == ''
        assert manat.__hash__() == hash(
            (manat.__class__, decimal, 'TMT', '934'))
        assert manat.__repr__() == (
            'Manat(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TMT", '
            'symbol: "m", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "m", '
            'numeric_code: "934", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert manat.__str__() == '0,14 m'

    def test_manat_negative(self):
        """test_manat_negative."""
        amount = -100
        manat = Manat(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert manat.numeric_code == '934'
        assert manat.alpha_code == 'TMT'
        assert manat.decimal_places == 2
        assert manat.decimal_sign == ','
        assert manat.grouping_places == 3
        assert manat.grouping_sign == '\u202F'
        assert not manat.international
        assert manat.symbol == 'm'
        assert not manat.symbol_ahead
        assert manat.symbol_separator == '\u00A0'
        assert manat.localized_symbol == 'm'
        assert manat.convertion == ''
        assert manat.__hash__() == hash(
            (manat.__class__, decimal, 'TMT', '934'))
        assert manat.__repr__() == (
            'Manat(amount: -100, '
            'alpha_code: "TMT", '
            'symbol: "m", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "m", '
            'numeric_code: "934", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert manat.__str__() == '-100,00 m'

    def test_manat_custom(self):
        """test_manat_custom."""
        amount = 1000
        manat = Manat(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert manat.amount == decimal
        assert manat.numeric_code == '934'
        assert manat.alpha_code == 'TMT'
        assert manat.decimal_places == 5
        assert manat.decimal_sign == '\u202F'
        assert manat.grouping_places == 2
        assert manat.grouping_sign == ','
        assert manat.international
        assert manat.symbol == 'm'
        assert not manat.symbol_ahead
        assert manat.symbol_separator == '_'
        assert manat.localized_symbol == 'm'
        assert manat.convertion == ''
        assert manat.__hash__() == hash(
            (manat.__class__, decimal, 'TMT', '934'))
        assert manat.__repr__() == (
            'Manat(amount: 1000, '
            'alpha_code: "TMT", '
            'symbol: "m", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "m", '
            'numeric_code: "934", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert manat.__str__() == 'TMT 10,00.00000'

    def test_manat_changed(self):
        """test_cmanat_changed."""
        manat = Manat(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            manat.international = True

    def test_manat_math_add(self):
        """test_manat_math_add."""
        manat_one = Manat(amount=1)
        manat_two = Manat(amount=2)
        manat_three = Manat(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TMT and OTHER.'):
            _ = manat_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'manat.Manat\'> '
                    'and <class \'str\'>.')):
            _ = manat_one.__add__('1.00')
        assert (
            manat_one +
            manat_two) == manat_three

    def test_manat_slots(self):
        """test_manat_slots."""
        manat = Manat(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Manat\' '
                    'object has no attribute \'new_variable\'')):
            manat.new_variable = 'fail'  # pylint: disable=assigning-non-slot
