# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ruble currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Belarusian Ruble representation."""

from multicurrency import BelarusianRuble


class TestBelarusianRuble:
    """BelarusianRuble currency tests."""

    def test_belarusian_ruble(self):
        """test_belarusian_ruble."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        belarusian_ruble = BelarusianRuble(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert belarusian_ruble.amount == decimal
        assert belarusian_ruble.numeric_code == '933'
        assert belarusian_ruble.alpha_code == 'BYN'
        assert belarusian_ruble.decimal_places == 2
        assert belarusian_ruble.decimal_sign == ','
        assert belarusian_ruble.grouping_places == 3
        assert belarusian_ruble.grouping_sign == '\u202F'
        assert not belarusian_ruble.international
        assert belarusian_ruble.symbol == 'Br'
        assert not belarusian_ruble.symbol_ahead
        assert belarusian_ruble.symbol_separator == '\u00A0'
        assert belarusian_ruble.localized_symbol == 'Br'
        assert belarusian_ruble.convertion == ''
        assert belarusian_ruble.__hash__() == hash(
            (belarusian_ruble.__class__, decimal, 'BYN', '933'))
        assert belarusian_ruble.__repr__() == (
            'BelarusianRuble(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BYN", '
            'symbol: "Br", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Br", '
            'numeric_code: "933", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert belarusian_ruble.__str__() == '0,14 Br'

    def test_belarusian_ruble_negative(self):
        """test_belarusian_ruble_negative."""
        amount = -100
        belarusian_ruble = BelarusianRuble(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert belarusian_ruble.numeric_code == '933'
        assert belarusian_ruble.alpha_code == 'BYN'
        assert belarusian_ruble.decimal_places == 2
        assert belarusian_ruble.decimal_sign == ','
        assert belarusian_ruble.grouping_places == 3
        assert belarusian_ruble.grouping_sign == '\u202F'
        assert not belarusian_ruble.international
        assert belarusian_ruble.symbol == 'Br'
        assert not belarusian_ruble.symbol_ahead
        assert belarusian_ruble.symbol_separator == '\u00A0'
        assert belarusian_ruble.localized_symbol == 'Br'
        assert belarusian_ruble.convertion == ''
        assert belarusian_ruble.__hash__() == hash(
            (belarusian_ruble.__class__, decimal, 'BYN', '933'))
        assert belarusian_ruble.__repr__() == (
            'BelarusianRuble(amount: -100, '
            'alpha_code: "BYN", '
            'symbol: "Br", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Br", '
            'numeric_code: "933", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert belarusian_ruble.__str__() == '-100,00 Br'

    def test_belarusian_ruble_custom(self):
        """test_belarusian_ruble_custom."""
        amount = 1000
        belarusian_ruble = BelarusianRuble(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert belarusian_ruble.amount == decimal
        assert belarusian_ruble.numeric_code == '933'
        assert belarusian_ruble.alpha_code == 'BYN'
        assert belarusian_ruble.decimal_places == 5
        assert belarusian_ruble.decimal_sign == '\u202F'
        assert belarusian_ruble.grouping_places == 2
        assert belarusian_ruble.grouping_sign == ','
        assert belarusian_ruble.international
        assert belarusian_ruble.symbol == 'Br'
        assert not belarusian_ruble.symbol_ahead
        assert belarusian_ruble.symbol_separator == '_'
        assert belarusian_ruble.localized_symbol == 'Br'
        assert belarusian_ruble.convertion == ''
        assert belarusian_ruble.__hash__() == hash(
            (belarusian_ruble.__class__, decimal, 'BYN', '933'))
        assert belarusian_ruble.__repr__() == (
            'BelarusianRuble(amount: 1000, '
            'alpha_code: "BYN", '
            'symbol: "Br", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Br", '
            'numeric_code: "933", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert belarusian_ruble.__str__() == 'BYN 10,00.00000'

    def test_belarusian_ruble_changed(self):
        """test_cbelarusian_ruble_changed."""
        belarusian_ruble = BelarusianRuble(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belarusian_ruble.international = True

    def test_belarusian_ruble_math_add(self):
        """test_belarusian_ruble_math_add."""
        belarusian_ruble_one = BelarusianRuble(amount=1)
        belarusian_ruble_two = BelarusianRuble(amount=2)
        belarusian_ruble_three = BelarusianRuble(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BYN and OTHER.'):
            _ = belarusian_ruble_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ruble.BelarusianRuble\'> '
                    'and <class \'str\'>.')):
            _ = belarusian_ruble_one.__add__('1.00')
        assert (
            belarusian_ruble_one +
            belarusian_ruble_two) == belarusian_ruble_three

    def test_belarusian_ruble_slots(self):
        """test_belarusian_ruble_slots."""
        belarusian_ruble = BelarusianRuble(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BelarusianRuble\' '
                    'object has no attribute \'new_variable\'')):
            belarusian_ruble.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Russian Ruble representation."""

from multicurrency import RussianRuble


class TestRussianRuble:
    """RussianRuble currency tests."""

    def test_russian_ruble(self):
        """test_russian_ruble."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        russian_ruble = RussianRuble(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble.amount == decimal
        assert russian_ruble.numeric_code == '643'
        assert russian_ruble.alpha_code == 'RUB'
        assert russian_ruble.decimal_places == 2
        assert russian_ruble.decimal_sign == ','
        assert russian_ruble.grouping_places == 3
        assert russian_ruble.grouping_sign == '\u202F'
        assert not russian_ruble.international
        assert russian_ruble.symbol == '₽'
        assert not russian_ruble.symbol_ahead
        assert russian_ruble.symbol_separator == '\u00A0'
        assert russian_ruble.localized_symbol == '₽'
        assert russian_ruble.convertion == ''
        assert russian_ruble.__hash__() == hash(
            (russian_ruble.__class__, decimal, 'RUB', '643'))
        assert russian_ruble.__repr__() == (
            'RussianRuble(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble.__str__() == '0,14 ₽'

    def test_russian_ruble_negative(self):
        """test_russian_ruble_negative."""
        amount = -100
        russian_ruble = RussianRuble(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble.numeric_code == '643'
        assert russian_ruble.alpha_code == 'RUB'
        assert russian_ruble.decimal_places == 2
        assert russian_ruble.decimal_sign == ','
        assert russian_ruble.grouping_places == 3
        assert russian_ruble.grouping_sign == '\u202F'
        assert not russian_ruble.international
        assert russian_ruble.symbol == '₽'
        assert not russian_ruble.symbol_ahead
        assert russian_ruble.symbol_separator == '\u00A0'
        assert russian_ruble.localized_symbol == '₽'
        assert russian_ruble.convertion == ''
        assert russian_ruble.__hash__() == hash(
            (russian_ruble.__class__, decimal, 'RUB', '643'))
        assert russian_ruble.__repr__() == (
            'RussianRuble(amount: -100, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble.__str__() == '-100,00 ₽'

    def test_russian_ruble_custom(self):
        """test_russian_ruble_custom."""
        amount = 1000
        russian_ruble = RussianRuble(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble.amount == decimal
        assert russian_ruble.numeric_code == '643'
        assert russian_ruble.alpha_code == 'RUB'
        assert russian_ruble.decimal_places == 5
        assert russian_ruble.decimal_sign == '\u202F'
        assert russian_ruble.grouping_places == 2
        assert russian_ruble.grouping_sign == ','
        assert russian_ruble.international
        assert russian_ruble.symbol == '₽'
        assert not russian_ruble.symbol_ahead
        assert russian_ruble.symbol_separator == '_'
        assert russian_ruble.localized_symbol == '₽'
        assert russian_ruble.convertion == ''
        assert russian_ruble.__hash__() == hash(
            (russian_ruble.__class__, decimal, 'RUB', '643'))
        assert russian_ruble.__repr__() == (
            'RussianRuble(amount: 1000, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₽", '
            'numeric_code: "643", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert russian_ruble.__str__() == 'RUB 10,00.00000'

    def test_russian_ruble_changed(self):
        """test_crussian_ruble_changed."""
        russian_ruble = RussianRuble(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble.international = True

    def test_russian_ruble_math_add(self):
        """test_russian_ruble_math_add."""
        russian_ruble_one = RussianRuble(amount=1)
        russian_ruble_two = RussianRuble(amount=2)
        russian_ruble_three = RussianRuble(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RUB and OTHER.'):
            _ = russian_ruble_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ruble.RussianRuble\'> '
                    'and <class \'str\'>.')):
            _ = russian_ruble_one.__add__('1.00')
        assert (
            russian_ruble_one +
            russian_ruble_two) == russian_ruble_three

    def test_russian_ruble_slots(self):
        """test_russian_ruble_slots."""
        russian_ruble = RussianRuble(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RussianRuble\' '
                    'object has no attribute \'new_variable\'')):
            russian_ruble.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Russian Ruble RU representation."""

from multicurrency import RussianRubleRU


class TestRussianRubleRU:
    """RussianRubleRU currency tests."""

    def test_russian_ruble_ru(self):
        """test_russian_ruble_ru."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        russian_ruble_ru = RussianRubleRU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ru.amount == decimal
        assert russian_ruble_ru.numeric_code == '643'
        assert russian_ruble_ru.alpha_code == 'RUB'
        assert russian_ruble_ru.decimal_places == 2
        assert russian_ruble_ru.decimal_sign == ','
        assert russian_ruble_ru.grouping_places == 3
        assert russian_ruble_ru.grouping_sign == '\u202F'
        assert not russian_ruble_ru.international
        assert russian_ruble_ru.symbol == '₽'
        assert not russian_ruble_ru.symbol_ahead
        assert russian_ruble_ru.symbol_separator == '\u00A0'
        assert russian_ruble_ru.localized_symbol == 'RU₽'
        assert russian_ruble_ru.convertion == ''
        assert russian_ruble_ru.__hash__() == hash(
            (russian_ruble_ru.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ru.__repr__() == (
            'RussianRubleRU(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RU₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble_ru.__str__() == '0,14 ₽'

    def test_russian_ruble_ru_negative(self):
        """test_russian_ruble_ru_negative."""
        amount = -100
        russian_ruble_ru = RussianRubleRU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ru.numeric_code == '643'
        assert russian_ruble_ru.alpha_code == 'RUB'
        assert russian_ruble_ru.decimal_places == 2
        assert russian_ruble_ru.decimal_sign == ','
        assert russian_ruble_ru.grouping_places == 3
        assert russian_ruble_ru.grouping_sign == '\u202F'
        assert not russian_ruble_ru.international
        assert russian_ruble_ru.symbol == '₽'
        assert not russian_ruble_ru.symbol_ahead
        assert russian_ruble_ru.symbol_separator == '\u00A0'
        assert russian_ruble_ru.localized_symbol == 'RU₽'
        assert russian_ruble_ru.convertion == ''
        assert russian_ruble_ru.__hash__() == hash(
            (russian_ruble_ru.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ru.__repr__() == (
            'RussianRubleRU(amount: -100, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RU₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble_ru.__str__() == '-100,00 ₽'

    def test_russian_ruble_ru_custom(self):
        """test_russian_ruble_ru_custom."""
        amount = 1000
        russian_ruble_ru = RussianRubleRU(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ru.amount == decimal
        assert russian_ruble_ru.numeric_code == '643'
        assert russian_ruble_ru.alpha_code == 'RUB'
        assert russian_ruble_ru.decimal_places == 5
        assert russian_ruble_ru.decimal_sign == '\u202F'
        assert russian_ruble_ru.grouping_places == 2
        assert russian_ruble_ru.grouping_sign == ','
        assert russian_ruble_ru.international
        assert russian_ruble_ru.symbol == '₽'
        assert not russian_ruble_ru.symbol_ahead
        assert russian_ruble_ru.symbol_separator == '_'
        assert russian_ruble_ru.localized_symbol == 'RU₽'
        assert russian_ruble_ru.convertion == ''
        assert russian_ruble_ru.__hash__() == hash(
            (russian_ruble_ru.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ru.__repr__() == (
            'RussianRubleRU(amount: 1000, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "RU₽", '
            'numeric_code: "643", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert russian_ruble_ru.__str__() == 'RUB 10,00.00000'

    def test_russian_ruble_ru_changed(self):
        """test_crussian_ruble_ru_changed."""
        russian_ruble_ru = RussianRubleRU(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ru.international = True

    def test_russian_ruble_ru_math_add(self):
        """test_russian_ruble_ru_math_add."""
        russian_ruble_ru_one = RussianRubleRU(amount=1)
        russian_ruble_ru_two = RussianRubleRU(amount=2)
        russian_ruble_ru_three = RussianRubleRU(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RUB and OTHER.'):
            _ = russian_ruble_ru_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ruble.RussianRubleRU\'> '
                    'and <class \'str\'>.')):
            _ = russian_ruble_ru_one.__add__('1.00')
        assert (
            russian_ruble_ru_one +
            russian_ruble_ru_two) == russian_ruble_ru_three

    def test_russian_ruble_ru_slots(self):
        """test_russian_ruble_ru_slots."""
        russian_ruble_ru = RussianRubleRU(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RussianRubleRU\' '
                    'object has no attribute \'new_variable\'')):
            russian_ruble_ru.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Russian Ruble GE representation."""

from multicurrency import RussianRubleGE


class TestRussianRubleGE:
    """RussianRubleGE currency tests."""

    def test_russian_ruble_ge(self):
        """test_russian_ruble_ge."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        russian_ruble_ge = RussianRubleGE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ge.amount == decimal
        assert russian_ruble_ge.numeric_code == '643'
        assert russian_ruble_ge.alpha_code == 'RUB'
        assert russian_ruble_ge.decimal_places == 2
        assert russian_ruble_ge.decimal_sign == ','
        assert russian_ruble_ge.grouping_places == 3
        assert russian_ruble_ge.grouping_sign == '\u202F'
        assert not russian_ruble_ge.international
        assert russian_ruble_ge.symbol == '₽'
        assert not russian_ruble_ge.symbol_ahead
        assert russian_ruble_ge.symbol_separator == '\u00A0'
        assert russian_ruble_ge.localized_symbol == 'GE₽'
        assert russian_ruble_ge.convertion == ''
        assert russian_ruble_ge.__hash__() == hash(
            (russian_ruble_ge.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ge.__repr__() == (
            'RussianRubleGE(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GE₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble_ge.__str__() == '0,14 ₽'

    def test_russian_ruble_ge_negative(self):
        """test_russian_ruble_ge_negative."""
        amount = -100
        russian_ruble_ge = RussianRubleGE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ge.numeric_code == '643'
        assert russian_ruble_ge.alpha_code == 'RUB'
        assert russian_ruble_ge.decimal_places == 2
        assert russian_ruble_ge.decimal_sign == ','
        assert russian_ruble_ge.grouping_places == 3
        assert russian_ruble_ge.grouping_sign == '\u202F'
        assert not russian_ruble_ge.international
        assert russian_ruble_ge.symbol == '₽'
        assert not russian_ruble_ge.symbol_ahead
        assert russian_ruble_ge.symbol_separator == '\u00A0'
        assert russian_ruble_ge.localized_symbol == 'GE₽'
        assert russian_ruble_ge.convertion == ''
        assert russian_ruble_ge.__hash__() == hash(
            (russian_ruble_ge.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ge.__repr__() == (
            'RussianRubleGE(amount: -100, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GE₽", '
            'numeric_code: "643", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert russian_ruble_ge.__str__() == '-100,00 ₽'

    def test_russian_ruble_ge_custom(self):
        """test_russian_ruble_ge_custom."""
        amount = 1000
        russian_ruble_ge = RussianRubleGE(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert russian_ruble_ge.amount == decimal
        assert russian_ruble_ge.numeric_code == '643'
        assert russian_ruble_ge.alpha_code == 'RUB'
        assert russian_ruble_ge.decimal_places == 5
        assert russian_ruble_ge.decimal_sign == '\u202F'
        assert russian_ruble_ge.grouping_places == 2
        assert russian_ruble_ge.grouping_sign == ','
        assert russian_ruble_ge.international
        assert russian_ruble_ge.symbol == '₽'
        assert not russian_ruble_ge.symbol_ahead
        assert russian_ruble_ge.symbol_separator == '_'
        assert russian_ruble_ge.localized_symbol == 'GE₽'
        assert russian_ruble_ge.convertion == ''
        assert russian_ruble_ge.__hash__() == hash(
            (russian_ruble_ge.__class__, decimal, 'RUB', '643'))
        assert russian_ruble_ge.__repr__() == (
            'RussianRubleGE(amount: 1000, '
            'alpha_code: "RUB", '
            'symbol: "₽", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GE₽", '
            'numeric_code: "643", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert russian_ruble_ge.__str__() == 'RUB 10,00.00000'

    def test_russian_ruble_ge_changed(self):
        """test_crussian_ruble_ge_changed."""
        russian_ruble_ge = RussianRubleGE(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            russian_ruble_ge.international = True

    def test_russian_ruble_ge_math_add(self):
        """test_russian_ruble_ge_math_add."""
        russian_ruble_ge_one = RussianRubleGE(amount=1)
        russian_ruble_ge_two = RussianRubleGE(amount=2)
        russian_ruble_ge_three = RussianRubleGE(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RUB and OTHER.'):
            _ = russian_ruble_ge_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'ruble.RussianRubleGE\'> '
                    'and <class \'str\'>.')):
            _ = russian_ruble_ge_one.__add__('1.00')
        assert (
            russian_ruble_ge_one +
            russian_ruble_ge_two) == russian_ruble_ge_three

    def test_russian_ruble_ge_slots(self):
        """test_russian_ruble_ge_slots."""
        russian_ruble_ge = RussianRubleGE(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RussianRubleGE\' '
                    'object has no attribute \'new_variable\'')):
            russian_ruble_ge.new_variable = 'fail'  # pylint: disable=assigning-non-slot
