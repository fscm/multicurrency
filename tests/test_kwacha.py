# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwacha currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Kwacha representation."""

from multicurrency import Kwacha


class TestKwacha:

    def test_kwacha(self):
        """test_kwacha."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        kwacha = Kwacha(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kwacha.amount == decimal
        assert kwacha.numeric_code == '454'
        assert kwacha.alpha_code == 'MWK'
        assert kwacha.decimal_places == 2
        assert kwacha.decimal_sign == '.'
        assert kwacha.grouping_places == 3
        assert kwacha.grouping_sign == ','
        assert not kwacha.international
        assert kwacha.symbol == 'MK'
        assert kwacha.symbol_ahead
        assert kwacha.symbol_separator == '\u00A0'
        assert kwacha.localized_symbol == 'MK'
        assert kwacha.convertion == ''
        assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
        assert kwacha.__repr__() == (
            'Kwacha(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MWK", '
            'symbol: "MK", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MK", '
            'numeric_code: "454", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert kwacha.__str__() == 'MK 0.14'


    def test_kwacha_negative(self):
        """test_kwacha_negative."""
        amount = -100
        kwacha = Kwacha(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kwacha.numeric_code == '454'
        assert kwacha.alpha_code == 'MWK'
        assert kwacha.decimal_places == 2
        assert kwacha.decimal_sign == '.'
        assert kwacha.grouping_places == 3
        assert kwacha.grouping_sign == ','
        assert not kwacha.international
        assert kwacha.symbol == 'MK'
        assert kwacha.symbol_ahead
        assert kwacha.symbol_separator == '\u00A0'
        assert kwacha.localized_symbol == 'MK'
        assert kwacha.convertion == ''
        assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
        assert kwacha.__repr__() == (
            'Kwacha(amount: -100, '
            'alpha_code: "MWK", '
            'symbol: "MK", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MK", '
            'numeric_code: "454", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert kwacha.__str__() == 'MK -100.00'


    def test_kwacha_custom(self):
        """test_kwacha_custom."""
        amount = 1000
        kwacha = Kwacha(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert kwacha.amount == decimal
        assert kwacha.numeric_code == '454'
        assert kwacha.alpha_code == 'MWK'
        assert kwacha.decimal_places == 5
        assert kwacha.decimal_sign == ','
        assert kwacha.grouping_places == 2
        assert kwacha.grouping_sign == '.'
        assert kwacha.international
        assert kwacha.symbol == 'MK'
        assert not kwacha.symbol_ahead
        assert kwacha.symbol_separator == '_'
        assert kwacha.localized_symbol == 'MK'
        assert kwacha.convertion == ''
        assert kwacha.__hash__() == hash((decimal, 'MWK', '454'))
        assert kwacha.__repr__() == (
            'Kwacha(amount: 1000, '
            'alpha_code: "MWK", '
            'symbol: "MK", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MK", '
            'numeric_code: "454", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert kwacha.__str__() == 'MWK 10,00.00000'


    def test_kwacha_changed(self):
        """test_ckwacha_changed."""
        kwacha = Kwacha(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kwacha.international = True


    def test_kwacha_math_add(self):
        """test_kwacha_math_add."""
        kwacha_one = Kwacha(amount=1)
        kwacha_two = Kwacha(amount=2)
        kwacha_three = Kwacha(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MWK and OTHER.'):
            _ = kwacha_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'kwacha.Kwacha\'> '
                    'and <class \'str\'>.')):
            _ = kwacha_one.__add__('1.00')
        assert (
            kwacha_one +
            kwacha_two) == kwacha_three


    def test_kwacha_slots(self):
        """test_kwacha_slots."""
        kwacha = Kwacha(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Kwacha\' '
                    'object has no attribute \'new_variable\'')):
            kwacha.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Zambian Kwacha representation."""

from multicurrency import ZambianKwacha


class TestZambianKwacha:

    def test_zambian_kwacha(self):
        """test_zambian_kwacha."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        zambian_kwacha = ZambianKwacha(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zambian_kwacha.amount == decimal
        assert zambian_kwacha.numeric_code == '967'
        assert zambian_kwacha.alpha_code == 'ZMW'
        assert zambian_kwacha.decimal_places == 2
        assert zambian_kwacha.decimal_sign == '.'
        assert zambian_kwacha.grouping_places == 3
        assert zambian_kwacha.grouping_sign == ','
        assert not zambian_kwacha.international
        assert zambian_kwacha.symbol == 'ZK'
        assert zambian_kwacha.symbol_ahead
        assert zambian_kwacha.symbol_separator == '\u00A0'
        assert zambian_kwacha.localized_symbol == 'ZK'
        assert zambian_kwacha.convertion == ''
        assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
        assert zambian_kwacha.__repr__() == (
            'ZambianKwacha(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZMW", '
            'symbol: "ZK", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZK", '
            'numeric_code: "967", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zambian_kwacha.__str__() == 'ZK 0.14'


    def test_zambian_kwacha_negative(self):
        """test_zambian_kwacha_negative."""
        amount = -100
        zambian_kwacha = ZambianKwacha(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zambian_kwacha.numeric_code == '967'
        assert zambian_kwacha.alpha_code == 'ZMW'
        assert zambian_kwacha.decimal_places == 2
        assert zambian_kwacha.decimal_sign == '.'
        assert zambian_kwacha.grouping_places == 3
        assert zambian_kwacha.grouping_sign == ','
        assert not zambian_kwacha.international
        assert zambian_kwacha.symbol == 'ZK'
        assert zambian_kwacha.symbol_ahead
        assert zambian_kwacha.symbol_separator == '\u00A0'
        assert zambian_kwacha.localized_symbol == 'ZK'
        assert zambian_kwacha.convertion == ''
        assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
        assert zambian_kwacha.__repr__() == (
            'ZambianKwacha(amount: -100, '
            'alpha_code: "ZMW", '
            'symbol: "ZK", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZK", '
            'numeric_code: "967", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zambian_kwacha.__str__() == 'ZK -100.00'


    def test_zambian_kwacha_custom(self):
        """test_zambian_kwacha_custom."""
        amount = 1000
        zambian_kwacha = ZambianKwacha(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert zambian_kwacha.amount == decimal
        assert zambian_kwacha.numeric_code == '967'
        assert zambian_kwacha.alpha_code == 'ZMW'
        assert zambian_kwacha.decimal_places == 5
        assert zambian_kwacha.decimal_sign == ','
        assert zambian_kwacha.grouping_places == 2
        assert zambian_kwacha.grouping_sign == '.'
        assert zambian_kwacha.international
        assert zambian_kwacha.symbol == 'ZK'
        assert not zambian_kwacha.symbol_ahead
        assert zambian_kwacha.symbol_separator == '_'
        assert zambian_kwacha.localized_symbol == 'ZK'
        assert zambian_kwacha.convertion == ''
        assert zambian_kwacha.__hash__() == hash((decimal, 'ZMW', '967'))
        assert zambian_kwacha.__repr__() == (
            'ZambianKwacha(amount: 1000, '
            'alpha_code: "ZMW", '
            'symbol: "ZK", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ZK", '
            'numeric_code: "967", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert zambian_kwacha.__str__() == 'ZMW 10,00.00000'


    def test_zambian_kwacha_changed(self):
        """test_czambian_kwacha_changed."""
        zambian_kwacha = ZambianKwacha(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zambian_kwacha.international = True


    def test_zambian_kwacha_math_add(self):
        """test_zambian_kwacha_math_add."""
        zambian_kwacha_one = ZambianKwacha(amount=1)
        zambian_kwacha_two = ZambianKwacha(amount=2)
        zambian_kwacha_three = ZambianKwacha(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZMW and OTHER.'):
            _ = zambian_kwacha_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'kwacha.ZambianKwacha\'> '
                    'and <class \'str\'>.')):
            _ = zambian_kwacha_one.__add__('1.00')
        assert (
            zambian_kwacha_one +
            zambian_kwacha_two) == zambian_kwacha_three


    def test_zambian_kwacha_slots(self):
        """test_zambian_kwacha_slots."""
        zambian_kwacha = ZambianKwacha(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ZambianKwacha\' '
                    'object has no attribute \'new_variable\'')):
            zambian_kwacha.new_variable = 'fail'  # pylint: disable=assigning-non-slot
