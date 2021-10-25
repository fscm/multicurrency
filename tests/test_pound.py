# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pound currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Egyptian Pound representation."""

from multicurrency import EgyptianPound


class TestEgyptianPound:

    def test_egyptian_pound(self):
        """test_egyptian_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        egyptian_pound = EgyptianPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert egyptian_pound.amount == decimal
        assert egyptian_pound.numeric_code == '818'
        assert egyptian_pound.alpha_code == 'EGP'
        assert egyptian_pound.decimal_places == 2
        assert egyptian_pound.decimal_sign == '\u066B'
        assert egyptian_pound.grouping_places == 3
        assert egyptian_pound.grouping_sign == '\u066C'
        assert not egyptian_pound.international
        assert egyptian_pound.symbol == 'ج.م.'
        assert egyptian_pound.symbol_ahead
        assert egyptian_pound.symbol_separator == '\u00A0'
        assert egyptian_pound.localized_symbol == 'ج.م.'
        assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
        assert egyptian_pound.__repr__() == (
            'EgyptianPound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EGP", '
            'symbol: "ج.م.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ج.م.", '
            'numeric_code: "818", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert egyptian_pound.__str__() == 'ج.م. ٠٫١٤'


    def test_egyptian_pound_negative(self):
        """test_egyptian_pound_negative."""
        amount = -100
        egyptian_pound = EgyptianPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert egyptian_pound.numeric_code == '818'
        assert egyptian_pound.alpha_code == 'EGP'
        assert egyptian_pound.decimal_places == 2
        assert egyptian_pound.decimal_sign == '\u066B'
        assert egyptian_pound.grouping_places == 3
        assert egyptian_pound.grouping_sign == '\u066C'
        assert not egyptian_pound.international
        assert egyptian_pound.symbol == 'ج.م.'
        assert egyptian_pound.symbol_ahead
        assert egyptian_pound.symbol_separator == '\u00A0'
        assert egyptian_pound.localized_symbol == 'ج.م.'
        assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
        assert egyptian_pound.__repr__() == (
            'EgyptianPound(amount: -100, '
            'alpha_code: "EGP", '
            'symbol: "ج.م.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ج.م.", '
            'numeric_code: "818", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert egyptian_pound.__str__() == 'ج.م. -١٠٠٫٠٠'


    def test_egyptian_pound_custom(self):
        """test_egyptian_pound_custom."""
        amount = 1000
        egyptian_pound = EgyptianPound(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert egyptian_pound.amount == decimal
        assert egyptian_pound.numeric_code == '818'
        assert egyptian_pound.alpha_code == 'EGP'
        assert egyptian_pound.decimal_places == 5
        assert egyptian_pound.decimal_sign == '\u066C'
        assert egyptian_pound.grouping_places == 2
        assert egyptian_pound.grouping_sign == '\u066B'
        assert egyptian_pound.international
        assert egyptian_pound.symbol == 'ج.م.'
        assert not egyptian_pound.symbol_ahead
        assert egyptian_pound.symbol_separator == '_'
        assert egyptian_pound.localized_symbol == 'ج.م.'
        assert egyptian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert egyptian_pound.__hash__() == hash((decimal, 'EGP', '818'))
        assert egyptian_pound.__repr__() == (
            'EgyptianPound(amount: 1000, '
            'alpha_code: "EGP", '
            'symbol: "ج.م.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ج.م.", '
            'numeric_code: "818", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert egyptian_pound.__str__() == 'EGP 10,00.00000'


    def test_egyptian_pound_changed(self):
        """test_cegyptian_pound_changed."""
        egyptian_pound = EgyptianPound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            egyptian_pound.international = True


    def test_egyptian_pound_math_add(self):
        """test_egyptian_pound_math_add."""
        egyptian_pound_one = EgyptianPound(amount=1)
        egyptian_pound_two = EgyptianPound(amount=2)
        egyptian_pound_three = EgyptianPound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EGP and OTHER.'):
            _ = egyptian_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.EgyptianPound\'> '
                    'and <class \'str\'>.')):
            _ = egyptian_pound_one.__add__('1.00')
        assert (
            egyptian_pound_one +
            egyptian_pound_two) == egyptian_pound_three


    def test_egyptian_pound_slots(self):
        """test_egyptian_pound_slots."""
        egyptian_pound = EgyptianPound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EgyptianPound\' '
                    'object has no attribute \'new_variable\'')):
            egyptian_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Falkland Islands Pound representation."""

from multicurrency import FalklandIslandsPound


class TestFalklandIslandsPound:

    def test_falkland_islands_pound(self):
        """test_falkland_islands_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        falkland_islands_pound = FalklandIslandsPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert falkland_islands_pound.amount == decimal
        assert falkland_islands_pound.numeric_code == '238'
        assert falkland_islands_pound.alpha_code == 'FKP'
        assert falkland_islands_pound.decimal_places == 2
        assert falkland_islands_pound.decimal_sign == '.'
        assert falkland_islands_pound.grouping_places == 3
        assert falkland_islands_pound.grouping_sign == ','
        assert not falkland_islands_pound.international
        assert falkland_islands_pound.symbol == '£'
        assert falkland_islands_pound.symbol_ahead
        assert falkland_islands_pound.symbol_separator == ''
        assert falkland_islands_pound.localized_symbol == 'FK£'
        assert falkland_islands_pound.convertion == ''
        assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
        assert falkland_islands_pound.__repr__() == (
            'FalklandIslandsPound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "FKP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FK£", '
            'numeric_code: "238", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert falkland_islands_pound.__str__() == '£0.14'


    def test_falkland_islands_pound_negative(self):
        """test_falkland_islands_pound_negative."""
        amount = -100
        falkland_islands_pound = FalklandIslandsPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert falkland_islands_pound.numeric_code == '238'
        assert falkland_islands_pound.alpha_code == 'FKP'
        assert falkland_islands_pound.decimal_places == 2
        assert falkland_islands_pound.decimal_sign == '.'
        assert falkland_islands_pound.grouping_places == 3
        assert falkland_islands_pound.grouping_sign == ','
        assert not falkland_islands_pound.international
        assert falkland_islands_pound.symbol == '£'
        assert falkland_islands_pound.symbol_ahead
        assert falkland_islands_pound.symbol_separator == ''
        assert falkland_islands_pound.localized_symbol == 'FK£'
        assert falkland_islands_pound.convertion == ''
        assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
        assert falkland_islands_pound.__repr__() == (
            'FalklandIslandsPound(amount: -100, '
            'alpha_code: "FKP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FK£", '
            'numeric_code: "238", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert falkland_islands_pound.__str__() == '£-100.00'


    def test_falkland_islands_pound_custom(self):
        """test_falkland_islands_pound_custom."""
        amount = 1000
        falkland_islands_pound = FalklandIslandsPound(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert falkland_islands_pound.amount == decimal
        assert falkland_islands_pound.numeric_code == '238'
        assert falkland_islands_pound.alpha_code == 'FKP'
        assert falkland_islands_pound.decimal_places == 5
        assert falkland_islands_pound.decimal_sign == ','
        assert falkland_islands_pound.grouping_places == 2
        assert falkland_islands_pound.grouping_sign == '.'
        assert falkland_islands_pound.international
        assert falkland_islands_pound.symbol == '£'
        assert not falkland_islands_pound.symbol_ahead
        assert falkland_islands_pound.symbol_separator == '_'
        assert falkland_islands_pound.localized_symbol == 'FK£'
        assert falkland_islands_pound.convertion == ''
        assert falkland_islands_pound.__hash__() == hash((decimal, 'FKP', '238'))
        assert falkland_islands_pound.__repr__() == (
            'FalklandIslandsPound(amount: 1000, '
            'alpha_code: "FKP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "FK£", '
            'numeric_code: "238", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert falkland_islands_pound.__str__() == 'FKP 10,00.00000'


    def test_falkland_islands_pound_changed(self):
        """test_cfalkland_islands_pound_changed."""
        falkland_islands_pound = FalklandIslandsPound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            falkland_islands_pound.international = True


    def test_falkland_islands_pound_math_add(self):
        """test_falkland_islands_pound_math_add."""
        falkland_islands_pound_one = FalklandIslandsPound(amount=1)
        falkland_islands_pound_two = FalklandIslandsPound(amount=2)
        falkland_islands_pound_three = FalklandIslandsPound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency FKP and OTHER.'):
            _ = falkland_islands_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.FalklandIslandsPound\'> '
                    'and <class \'str\'>.')):
            _ = falkland_islands_pound_one.__add__('1.00')
        assert (
            falkland_islands_pound_one +
            falkland_islands_pound_two) == falkland_islands_pound_three


    def test_falkland_islands_pound_slots(self):
        """test_falkland_islands_pound_slots."""
        falkland_islands_pound = FalklandIslandsPound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'FalklandIslandsPound\' '
                    'object has no attribute \'new_variable\'')):
            falkland_islands_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pound Sterling representation."""

from multicurrency import PoundSterling


class TestPoundSterling:

    def test_pound_sterling(self):
        """test_pound_sterling."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pound_sterling = PoundSterling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling.amount == decimal
        assert pound_sterling.numeric_code == '826'
        assert pound_sterling.alpha_code == 'GBP'
        assert pound_sterling.decimal_places == 2
        assert pound_sterling.decimal_sign == '.'
        assert pound_sterling.grouping_places == 3
        assert pound_sterling.grouping_sign == ','
        assert not pound_sterling.international
        assert pound_sterling.symbol == '£'
        assert pound_sterling.symbol_ahead
        assert pound_sterling.symbol_separator == ''
        assert pound_sterling.localized_symbol == '£'
        assert pound_sterling.convertion == ''
        assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling.__repr__() == (
            'PoundSterling(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling.__str__() == '£0.14'


    def test_pound_sterling_negative(self):
        """test_pound_sterling_negative."""
        amount = -100
        pound_sterling = PoundSterling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling.numeric_code == '826'
        assert pound_sterling.alpha_code == 'GBP'
        assert pound_sterling.decimal_places == 2
        assert pound_sterling.decimal_sign == '.'
        assert pound_sterling.grouping_places == 3
        assert pound_sterling.grouping_sign == ','
        assert not pound_sterling.international
        assert pound_sterling.symbol == '£'
        assert pound_sterling.symbol_ahead
        assert pound_sterling.symbol_separator == ''
        assert pound_sterling.localized_symbol == '£'
        assert pound_sterling.convertion == ''
        assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling.__repr__() == (
            'PoundSterling(amount: -100, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling.__str__() == '£-100.00'


    def test_pound_sterling_custom(self):
        """test_pound_sterling_custom."""
        amount = 1000
        pound_sterling = PoundSterling(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling.amount == decimal
        assert pound_sterling.numeric_code == '826'
        assert pound_sterling.alpha_code == 'GBP'
        assert pound_sterling.decimal_places == 5
        assert pound_sterling.decimal_sign == ','
        assert pound_sterling.grouping_places == 2
        assert pound_sterling.grouping_sign == '.'
        assert pound_sterling.international
        assert pound_sterling.symbol == '£'
        assert not pound_sterling.symbol_ahead
        assert pound_sterling.symbol_separator == '_'
        assert pound_sterling.localized_symbol == '£'
        assert pound_sterling.convertion == ''
        assert pound_sterling.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling.__repr__() == (
            'PoundSterling(amount: 1000, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "£", '
            'numeric_code: "826", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pound_sterling.__str__() == 'GBP 10,00.00000'


    def test_pound_sterling_changed(self):
        """test_cpound_sterling_changed."""
        pound_sterling = PoundSterling(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling.international = True


    def test_pound_sterling_math_add(self):
        """test_pound_sterling_math_add."""
        pound_sterling_one = PoundSterling(amount=1)
        pound_sterling_two = PoundSterling(amount=2)
        pound_sterling_three = PoundSterling(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GBP and OTHER.'):
            _ = pound_sterling_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.PoundSterling\'> '
                    'and <class \'str\'>.')):
            _ = pound_sterling_one.__add__('1.00')
        assert (
            pound_sterling_one +
            pound_sterling_two) == pound_sterling_three


    def test_pound_sterling_slots(self):
        """test_pound_sterling_slots."""
        pound_sterling = PoundSterling(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PoundSterling\' '
                    'object has no attribute \'new_variable\'')):
            pound_sterling.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pound Sterling GG representation."""

from multicurrency import PoundSterlingGG


class TestPoundSterlingGG:

    def test_pound_sterling_gg(self):
        """test_pound_sterling_gg."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pound_sterling_gg = PoundSterlingGG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gg.amount == decimal
        assert pound_sterling_gg.numeric_code == '826'
        assert pound_sterling_gg.alpha_code == 'GBP'
        assert pound_sterling_gg.decimal_places == 2
        assert pound_sterling_gg.decimal_sign == '.'
        assert pound_sterling_gg.grouping_places == 3
        assert pound_sterling_gg.grouping_sign == ','
        assert not pound_sterling_gg.international
        assert pound_sterling_gg.symbol == '£'
        assert pound_sterling_gg.symbol_ahead
        assert pound_sterling_gg.symbol_separator == ''
        assert pound_sterling_gg.localized_symbol == 'GG£'
        assert pound_sterling_gg.convertion == ''
        assert pound_sterling_gg.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gg.__repr__() == (
            'PoundSterlingGG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GG£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_gg.__str__() == '£0.14'


    def test_pound_sterling_gg_negative(self):
        """test_pound_sterling_gg_negative."""
        amount = -100
        pound_sterling_gg = PoundSterlingGG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gg.numeric_code == '826'
        assert pound_sterling_gg.alpha_code == 'GBP'
        assert pound_sterling_gg.decimal_places == 2
        assert pound_sterling_gg.decimal_sign == '.'
        assert pound_sterling_gg.grouping_places == 3
        assert pound_sterling_gg.grouping_sign == ','
        assert not pound_sterling_gg.international
        assert pound_sterling_gg.symbol == '£'
        assert pound_sterling_gg.symbol_ahead
        assert pound_sterling_gg.symbol_separator == ''
        assert pound_sterling_gg.localized_symbol == 'GG£'
        assert pound_sterling_gg.convertion == ''
        assert pound_sterling_gg.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gg.__repr__() == (
            'PoundSterlingGG(amount: -100, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GG£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_gg.__str__() == '£-100.00'


    def test_pound_sterling_gg_custom(self):
        """test_pound_sterling_gg_custom."""
        amount = 1000
        pound_sterling_gg = PoundSterlingGG(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gg.amount == decimal
        assert pound_sterling_gg.numeric_code == '826'
        assert pound_sterling_gg.alpha_code == 'GBP'
        assert pound_sterling_gg.decimal_places == 5
        assert pound_sterling_gg.decimal_sign == ','
        assert pound_sterling_gg.grouping_places == 2
        assert pound_sterling_gg.grouping_sign == '.'
        assert pound_sterling_gg.international
        assert pound_sterling_gg.symbol == '£'
        assert not pound_sterling_gg.symbol_ahead
        assert pound_sterling_gg.symbol_separator == '_'
        assert pound_sterling_gg.localized_symbol == 'GG£'
        assert pound_sterling_gg.convertion == ''
        assert pound_sterling_gg.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gg.__repr__() == (
            'PoundSterlingGG(amount: 1000, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GG£", '
            'numeric_code: "826", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pound_sterling_gg.__str__() == 'GBP 10,00.00000'


    def test_pound_sterling_gg_changed(self):
        """test_cpound_sterling_gg_changed."""
        pound_sterling_gg = PoundSterlingGG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gg.international = True


    def test_pound_sterling_gg_math_add(self):
        """test_pound_sterling_gg_math_add."""
        pound_sterling_gg_one = PoundSterlingGG(amount=1)
        pound_sterling_gg_two = PoundSterlingGG(amount=2)
        pound_sterling_gg_three = PoundSterlingGG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GBP and OTHER.'):
            _ = pound_sterling_gg_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.PoundSterlingGG\'> '
                    'and <class \'str\'>.')):
            _ = pound_sterling_gg_one.__add__('1.00')
        assert (
            pound_sterling_gg_one +
            pound_sterling_gg_two) == pound_sterling_gg_three


    def test_pound_sterling_gg_slots(self):
        """test_pound_sterling_gg_slots."""
        pound_sterling_gg = PoundSterlingGG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PoundSterlingGG\' '
                    'object has no attribute \'new_variable\'')):
            pound_sterling_gg.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pound Sterling IO representation."""

from multicurrency import PoundSterlingIO


class TestPoundSterlingIO:

    def test_pound_sterling_io(self):
        """test_pound_sterling_io."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pound_sterling_io = PoundSterlingIO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_io.amount == decimal
        assert pound_sterling_io.numeric_code == '826'
        assert pound_sterling_io.alpha_code == 'GBP'
        assert pound_sterling_io.decimal_places == 2
        assert pound_sterling_io.decimal_sign == '.'
        assert pound_sterling_io.grouping_places == 3
        assert pound_sterling_io.grouping_sign == ','
        assert not pound_sterling_io.international
        assert pound_sterling_io.symbol == '£'
        assert pound_sterling_io.symbol_ahead
        assert pound_sterling_io.symbol_separator == ''
        assert pound_sterling_io.localized_symbol == 'IO£'
        assert pound_sterling_io.convertion == ''
        assert pound_sterling_io.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_io.__repr__() == (
            'PoundSterlingIO(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IO£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_io.__str__() == '£0.14'


    def test_pound_sterling_io_negative(self):
        """test_pound_sterling_io_negative."""
        amount = -100
        pound_sterling_io = PoundSterlingIO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_io.numeric_code == '826'
        assert pound_sterling_io.alpha_code == 'GBP'
        assert pound_sterling_io.decimal_places == 2
        assert pound_sterling_io.decimal_sign == '.'
        assert pound_sterling_io.grouping_places == 3
        assert pound_sterling_io.grouping_sign == ','
        assert not pound_sterling_io.international
        assert pound_sterling_io.symbol == '£'
        assert pound_sterling_io.symbol_ahead
        assert pound_sterling_io.symbol_separator == ''
        assert pound_sterling_io.localized_symbol == 'IO£'
        assert pound_sterling_io.convertion == ''
        assert pound_sterling_io.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_io.__repr__() == (
            'PoundSterlingIO(amount: -100, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IO£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_io.__str__() == '£-100.00'


    def test_pound_sterling_io_custom(self):
        """test_pound_sterling_io_custom."""
        amount = 1000
        pound_sterling_io = PoundSterlingIO(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_io.amount == decimal
        assert pound_sterling_io.numeric_code == '826'
        assert pound_sterling_io.alpha_code == 'GBP'
        assert pound_sterling_io.decimal_places == 5
        assert pound_sterling_io.decimal_sign == ','
        assert pound_sterling_io.grouping_places == 2
        assert pound_sterling_io.grouping_sign == '.'
        assert pound_sterling_io.international
        assert pound_sterling_io.symbol == '£'
        assert not pound_sterling_io.symbol_ahead
        assert pound_sterling_io.symbol_separator == '_'
        assert pound_sterling_io.localized_symbol == 'IO£'
        assert pound_sterling_io.convertion == ''
        assert pound_sterling_io.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_io.__repr__() == (
            'PoundSterlingIO(amount: 1000, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IO£", '
            'numeric_code: "826", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pound_sterling_io.__str__() == 'GBP 10,00.00000'


    def test_pound_sterling_io_changed(self):
        """test_cpound_sterling_io_changed."""
        pound_sterling_io = PoundSterlingIO(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_io.international = True


    def test_pound_sterling_io_math_add(self):
        """test_pound_sterling_io_math_add."""
        pound_sterling_io_one = PoundSterlingIO(amount=1)
        pound_sterling_io_two = PoundSterlingIO(amount=2)
        pound_sterling_io_three = PoundSterlingIO(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GBP and OTHER.'):
            _ = pound_sterling_io_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.PoundSterlingIO\'> '
                    'and <class \'str\'>.')):
            _ = pound_sterling_io_one.__add__('1.00')
        assert (
            pound_sterling_io_one +
            pound_sterling_io_two) == pound_sterling_io_three


    def test_pound_sterling_io_slots(self):
        """test_pound_sterling_io_slots."""
        pound_sterling_io = PoundSterlingIO(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PoundSterlingIO\' '
                    'object has no attribute \'new_variable\'')):
            pound_sterling_io.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pound Sterling GB representation."""

from multicurrency import PoundSterlingGB


class TestPoundSterlingGB:

    def test_pound_sterling_gb(self):
        """test_pound_sterling_gb."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pound_sterling_gb = PoundSterlingGB(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gb.amount == decimal
        assert pound_sterling_gb.numeric_code == '826'
        assert pound_sterling_gb.alpha_code == 'GBP'
        assert pound_sterling_gb.decimal_places == 2
        assert pound_sterling_gb.decimal_sign == '.'
        assert pound_sterling_gb.grouping_places == 3
        assert pound_sterling_gb.grouping_sign == ','
        assert not pound_sterling_gb.international
        assert pound_sterling_gb.symbol == '£'
        assert pound_sterling_gb.symbol_ahead
        assert pound_sterling_gb.symbol_separator == ''
        assert pound_sterling_gb.localized_symbol == 'GB£'
        assert pound_sterling_gb.convertion == ''
        assert pound_sterling_gb.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gb.__repr__() == (
            'PoundSterlingGB(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GB£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_gb.__str__() == '£0.14'


    def test_pound_sterling_gb_negative(self):
        """test_pound_sterling_gb_negative."""
        amount = -100
        pound_sterling_gb = PoundSterlingGB(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gb.numeric_code == '826'
        assert pound_sterling_gb.alpha_code == 'GBP'
        assert pound_sterling_gb.decimal_places == 2
        assert pound_sterling_gb.decimal_sign == '.'
        assert pound_sterling_gb.grouping_places == 3
        assert pound_sterling_gb.grouping_sign == ','
        assert not pound_sterling_gb.international
        assert pound_sterling_gb.symbol == '£'
        assert pound_sterling_gb.symbol_ahead
        assert pound_sterling_gb.symbol_separator == ''
        assert pound_sterling_gb.localized_symbol == 'GB£'
        assert pound_sterling_gb.convertion == ''
        assert pound_sterling_gb.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gb.__repr__() == (
            'PoundSterlingGB(amount: -100, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GB£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_gb.__str__() == '£-100.00'


    def test_pound_sterling_gb_custom(self):
        """test_pound_sterling_gb_custom."""
        amount = 1000
        pound_sterling_gb = PoundSterlingGB(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_gb.amount == decimal
        assert pound_sterling_gb.numeric_code == '826'
        assert pound_sterling_gb.alpha_code == 'GBP'
        assert pound_sterling_gb.decimal_places == 5
        assert pound_sterling_gb.decimal_sign == ','
        assert pound_sterling_gb.grouping_places == 2
        assert pound_sterling_gb.grouping_sign == '.'
        assert pound_sterling_gb.international
        assert pound_sterling_gb.symbol == '£'
        assert not pound_sterling_gb.symbol_ahead
        assert pound_sterling_gb.symbol_separator == '_'
        assert pound_sterling_gb.localized_symbol == 'GB£'
        assert pound_sterling_gb.convertion == ''
        assert pound_sterling_gb.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_gb.__repr__() == (
            'PoundSterlingGB(amount: 1000, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GB£", '
            'numeric_code: "826", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pound_sterling_gb.__str__() == 'GBP 10,00.00000'


    def test_pound_sterling_gb_changed(self):
        """test_cpound_sterling_gb_changed."""
        pound_sterling_gb = PoundSterlingGB(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_gb.international = True


    def test_pound_sterling_gb_math_add(self):
        """test_pound_sterling_gb_math_add."""
        pound_sterling_gb_one = PoundSterlingGB(amount=1)
        pound_sterling_gb_two = PoundSterlingGB(amount=2)
        pound_sterling_gb_three = PoundSterlingGB(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GBP and OTHER.'):
            _ = pound_sterling_gb_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.PoundSterlingGB\'> '
                    'and <class \'str\'>.')):
            _ = pound_sterling_gb_one.__add__('1.00')
        assert (
            pound_sterling_gb_one +
            pound_sterling_gb_two) == pound_sterling_gb_three


    def test_pound_sterling_gb_slots(self):
        """test_pound_sterling_gb_slots."""
        pound_sterling_gb = PoundSterlingGB(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PoundSterlingGB\' '
                    'object has no attribute \'new_variable\'')):
            pound_sterling_gb.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pound Sterling IM representation."""

from multicurrency import PoundSterlingIM


class TestPoundSterlingIM:

    def test_pound_sterling_im(self):
        """test_pound_sterling_im."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pound_sterling_im = PoundSterlingIM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_im.amount == decimal
        assert pound_sterling_im.numeric_code == '826'
        assert pound_sterling_im.alpha_code == 'GBP'
        assert pound_sterling_im.decimal_places == 2
        assert pound_sterling_im.decimal_sign == '.'
        assert pound_sterling_im.grouping_places == 3
        assert pound_sterling_im.grouping_sign == ','
        assert not pound_sterling_im.international
        assert pound_sterling_im.symbol == '£'
        assert pound_sterling_im.symbol_ahead
        assert pound_sterling_im.symbol_separator == ''
        assert pound_sterling_im.localized_symbol == 'IM£'
        assert pound_sterling_im.convertion == ''
        assert pound_sterling_im.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_im.__repr__() == (
            'PoundSterlingIM(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IM£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_im.__str__() == '£0.14'


    def test_pound_sterling_im_negative(self):
        """test_pound_sterling_im_negative."""
        amount = -100
        pound_sterling_im = PoundSterlingIM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_im.numeric_code == '826'
        assert pound_sterling_im.alpha_code == 'GBP'
        assert pound_sterling_im.decimal_places == 2
        assert pound_sterling_im.decimal_sign == '.'
        assert pound_sterling_im.grouping_places == 3
        assert pound_sterling_im.grouping_sign == ','
        assert not pound_sterling_im.international
        assert pound_sterling_im.symbol == '£'
        assert pound_sterling_im.symbol_ahead
        assert pound_sterling_im.symbol_separator == ''
        assert pound_sterling_im.localized_symbol == 'IM£'
        assert pound_sterling_im.convertion == ''
        assert pound_sterling_im.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_im.__repr__() == (
            'PoundSterlingIM(amount: -100, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IM£", '
            'numeric_code: "826", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pound_sterling_im.__str__() == '£-100.00'


    def test_pound_sterling_im_custom(self):
        """test_pound_sterling_im_custom."""
        amount = 1000
        pound_sterling_im = PoundSterlingIM(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pound_sterling_im.amount == decimal
        assert pound_sterling_im.numeric_code == '826'
        assert pound_sterling_im.alpha_code == 'GBP'
        assert pound_sterling_im.decimal_places == 5
        assert pound_sterling_im.decimal_sign == ','
        assert pound_sterling_im.grouping_places == 2
        assert pound_sterling_im.grouping_sign == '.'
        assert pound_sterling_im.international
        assert pound_sterling_im.symbol == '£'
        assert not pound_sterling_im.symbol_ahead
        assert pound_sterling_im.symbol_separator == '_'
        assert pound_sterling_im.localized_symbol == 'IM£'
        assert pound_sterling_im.convertion == ''
        assert pound_sterling_im.__hash__() == hash((decimal, 'GBP', '826'))
        assert pound_sterling_im.__repr__() == (
            'PoundSterlingIM(amount: 1000, '
            'alpha_code: "GBP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IM£", '
            'numeric_code: "826", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pound_sterling_im.__str__() == 'GBP 10,00.00000'


    def test_pound_sterling_im_changed(self):
        """test_cpound_sterling_im_changed."""
        pound_sterling_im = PoundSterlingIM(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pound_sterling_im.international = True


    def test_pound_sterling_im_math_add(self):
        """test_pound_sterling_im_math_add."""
        pound_sterling_im_one = PoundSterlingIM(amount=1)
        pound_sterling_im_two = PoundSterlingIM(amount=2)
        pound_sterling_im_three = PoundSterlingIM(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GBP and OTHER.'):
            _ = pound_sterling_im_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.PoundSterlingIM\'> '
                    'and <class \'str\'>.')):
            _ = pound_sterling_im_one.__add__('1.00')
        assert (
            pound_sterling_im_one +
            pound_sterling_im_two) == pound_sterling_im_three


    def test_pound_sterling_im_slots(self):
        """test_pound_sterling_im_slots."""
        pound_sterling_im = PoundSterlingIM(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PoundSterlingIM\' '
                    'object has no attribute \'new_variable\'')):
            pound_sterling_im.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Gibraltar Pound representation."""

from multicurrency import GibraltarPound


class TestGibraltarPound:

    def test_gibraltar_pound(self):
        """test_gibraltar_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        gibraltar_pound = GibraltarPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert gibraltar_pound.amount == decimal
        assert gibraltar_pound.numeric_code == '292'
        assert gibraltar_pound.alpha_code == 'GIP'
        assert gibraltar_pound.decimal_places == 2
        assert gibraltar_pound.decimal_sign == '.'
        assert gibraltar_pound.grouping_places == 3
        assert gibraltar_pound.grouping_sign == ','
        assert not gibraltar_pound.international
        assert gibraltar_pound.symbol == '£'
        assert gibraltar_pound.symbol_ahead
        assert gibraltar_pound.symbol_separator == ''
        assert gibraltar_pound.localized_symbol == 'GI£'
        assert gibraltar_pound.convertion == ''
        assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
        assert gibraltar_pound.__repr__() == (
            'GibraltarPound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GIP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GI£", '
            'numeric_code: "292", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert gibraltar_pound.__str__() == '£0.14'


    def test_gibraltar_pound_negative(self):
        """test_gibraltar_pound_negative."""
        amount = -100
        gibraltar_pound = GibraltarPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert gibraltar_pound.numeric_code == '292'
        assert gibraltar_pound.alpha_code == 'GIP'
        assert gibraltar_pound.decimal_places == 2
        assert gibraltar_pound.decimal_sign == '.'
        assert gibraltar_pound.grouping_places == 3
        assert gibraltar_pound.grouping_sign == ','
        assert not gibraltar_pound.international
        assert gibraltar_pound.symbol == '£'
        assert gibraltar_pound.symbol_ahead
        assert gibraltar_pound.symbol_separator == ''
        assert gibraltar_pound.localized_symbol == 'GI£'
        assert gibraltar_pound.convertion == ''
        assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
        assert gibraltar_pound.__repr__() == (
            'GibraltarPound(amount: -100, '
            'alpha_code: "GIP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GI£", '
            'numeric_code: "292", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert gibraltar_pound.__str__() == '£-100.00'


    def test_gibraltar_pound_custom(self):
        """test_gibraltar_pound_custom."""
        amount = 1000
        gibraltar_pound = GibraltarPound(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert gibraltar_pound.amount == decimal
        assert gibraltar_pound.numeric_code == '292'
        assert gibraltar_pound.alpha_code == 'GIP'
        assert gibraltar_pound.decimal_places == 5
        assert gibraltar_pound.decimal_sign == ','
        assert gibraltar_pound.grouping_places == 2
        assert gibraltar_pound.grouping_sign == '.'
        assert gibraltar_pound.international
        assert gibraltar_pound.symbol == '£'
        assert not gibraltar_pound.symbol_ahead
        assert gibraltar_pound.symbol_separator == '_'
        assert gibraltar_pound.localized_symbol == 'GI£'
        assert gibraltar_pound.convertion == ''
        assert gibraltar_pound.__hash__() == hash((decimal, 'GIP', '292'))
        assert gibraltar_pound.__repr__() == (
            'GibraltarPound(amount: 1000, '
            'alpha_code: "GIP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GI£", '
            'numeric_code: "292", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert gibraltar_pound.__str__() == 'GIP 10,00.00000'


    def test_gibraltar_pound_changed(self):
        """test_cgibraltar_pound_changed."""
        gibraltar_pound = GibraltarPound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            gibraltar_pound.international = True


    def test_gibraltar_pound_math_add(self):
        """test_gibraltar_pound_math_add."""
        gibraltar_pound_one = GibraltarPound(amount=1)
        gibraltar_pound_two = GibraltarPound(amount=2)
        gibraltar_pound_three = GibraltarPound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GIP and OTHER.'):
            _ = gibraltar_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.GibraltarPound\'> '
                    'and <class \'str\'>.')):
            _ = gibraltar_pound_one.__add__('1.00')
        assert (
            gibraltar_pound_one +
            gibraltar_pound_two) == gibraltar_pound_three


    def test_gibraltar_pound_slots(self):
        """test_gibraltar_pound_slots."""
        gibraltar_pound = GibraltarPound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'GibraltarPound\' '
                    'object has no attribute \'new_variable\'')):
            gibraltar_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Lebanese Pound representation."""

from multicurrency import LebanesePound


class TestLebanesePound:

    def test_lebanese_pound(self):
        """test_lebanese_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        lebanese_pound = LebanesePound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lebanese_pound.amount == decimal
        assert lebanese_pound.numeric_code == '422'
        assert lebanese_pound.alpha_code == 'LBP'
        assert lebanese_pound.decimal_places == 0
        assert lebanese_pound.decimal_sign == '\u066B'
        assert lebanese_pound.grouping_places == 3
        assert lebanese_pound.grouping_sign == '\u066C'
        assert not lebanese_pound.international
        assert lebanese_pound.symbol == 'ل.ل.'
        assert lebanese_pound.symbol_ahead
        assert lebanese_pound.symbol_separator == '\u00A0'
        assert lebanese_pound.localized_symbol == 'ل.ل.'
        assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
        assert lebanese_pound.__repr__() == (
            'LebanesePound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "LBP", '
            'symbol: "ل.ل.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ل.ل.", '
            'numeric_code: "422", '
            'decimal_places: "0", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert lebanese_pound.__str__() == 'ل.ل. ٠'


    def test_lebanese_pound_negative(self):
        """test_lebanese_pound_negative."""
        amount = -100
        lebanese_pound = LebanesePound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert lebanese_pound.numeric_code == '422'
        assert lebanese_pound.alpha_code == 'LBP'
        assert lebanese_pound.decimal_places == 0
        assert lebanese_pound.decimal_sign == '\u066B'
        assert lebanese_pound.grouping_places == 3
        assert lebanese_pound.grouping_sign == '\u066C'
        assert not lebanese_pound.international
        assert lebanese_pound.symbol == 'ل.ل.'
        assert lebanese_pound.symbol_ahead
        assert lebanese_pound.symbol_separator == '\u00A0'
        assert lebanese_pound.localized_symbol == 'ل.ل.'
        assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
        assert lebanese_pound.__repr__() == (
            'LebanesePound(amount: -100, '
            'alpha_code: "LBP", '
            'symbol: "ل.ل.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ل.ل.", '
            'numeric_code: "422", '
            'decimal_places: "0", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert lebanese_pound.__str__() == 'ل.ل. -١٠٠'


    def test_lebanese_pound_custom(self):
        """test_lebanese_pound_custom."""
        amount = 1000
        lebanese_pound = LebanesePound(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert lebanese_pound.amount == decimal
        assert lebanese_pound.numeric_code == '422'
        assert lebanese_pound.alpha_code == 'LBP'
        assert lebanese_pound.decimal_places == 5
        assert lebanese_pound.decimal_sign == '\u066C'
        assert lebanese_pound.grouping_places == 2
        assert lebanese_pound.grouping_sign == '\u066B'
        assert lebanese_pound.international
        assert lebanese_pound.symbol == 'ل.ل.'
        assert not lebanese_pound.symbol_ahead
        assert lebanese_pound.symbol_separator == '_'
        assert lebanese_pound.localized_symbol == 'ل.ل.'
        assert lebanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert lebanese_pound.__hash__() == hash((decimal, 'LBP', '422'))
        assert lebanese_pound.__repr__() == (
            'LebanesePound(amount: 1000, '
            'alpha_code: "LBP", '
            'symbol: "ل.ل.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ل.ل.", '
            'numeric_code: "422", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert lebanese_pound.__str__() == 'LBP 10,00.00000'


    def test_lebanese_pound_changed(self):
        """test_clebanese_pound_changed."""
        lebanese_pound = LebanesePound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            lebanese_pound.international = True


    def test_lebanese_pound_math_add(self):
        """test_lebanese_pound_math_add."""
        lebanese_pound_one = LebanesePound(amount=1)
        lebanese_pound_two = LebanesePound(amount=2)
        lebanese_pound_three = LebanesePound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency LBP and OTHER.'):
            _ = lebanese_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.LebanesePound\'> '
                    'and <class \'str\'>.')):
            _ = lebanese_pound_one.__add__('1.00')
        assert (
            lebanese_pound_one +
            lebanese_pound_two) == lebanese_pound_three


    def test_lebanese_pound_slots(self):
        """test_lebanese_pound_slots."""
        lebanese_pound = LebanesePound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'LebanesePound\' '
                    'object has no attribute \'new_variable\'')):
            lebanese_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Sudanese Pound representation."""

from multicurrency import SudanesePound


class TestSudanesePound:

    def test_sudanese_pound(self):
        """test_sudanese_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        sudanese_pound = SudanesePound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert sudanese_pound.amount == decimal
        assert sudanese_pound.numeric_code == '938'
        assert sudanese_pound.alpha_code == 'SDG'
        assert sudanese_pound.decimal_places == 2
        assert sudanese_pound.decimal_sign == '\u066B'
        assert sudanese_pound.grouping_places == 3
        assert sudanese_pound.grouping_sign == '\u066C'
        assert not sudanese_pound.international
        assert sudanese_pound.symbol == 'ج.س'
        assert not sudanese_pound.symbol_ahead
        assert sudanese_pound.symbol_separator == '\u00A0'
        assert sudanese_pound.localized_symbol == 'ج.س'
        assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
        assert sudanese_pound.__repr__() == (
            'SudanesePound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SDG", '
            'symbol: "ج.س", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ج.س", '
            'numeric_code: "938", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert sudanese_pound.__str__() == '٠٫١٤ ج.س'


    def test_sudanese_pound_negative(self):
        """test_sudanese_pound_negative."""
        amount = -100
        sudanese_pound = SudanesePound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert sudanese_pound.numeric_code == '938'
        assert sudanese_pound.alpha_code == 'SDG'
        assert sudanese_pound.decimal_places == 2
        assert sudanese_pound.decimal_sign == '\u066B'
        assert sudanese_pound.grouping_places == 3
        assert sudanese_pound.grouping_sign == '\u066C'
        assert not sudanese_pound.international
        assert sudanese_pound.symbol == 'ج.س'
        assert not sudanese_pound.symbol_ahead
        assert sudanese_pound.symbol_separator == '\u00A0'
        assert sudanese_pound.localized_symbol == 'ج.س'
        assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
        assert sudanese_pound.__repr__() == (
            'SudanesePound(amount: -100, '
            'alpha_code: "SDG", '
            'symbol: "ج.س", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ج.س", '
            'numeric_code: "938", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert sudanese_pound.__str__() == '-١٠٠٫٠٠ ج.س'


    def test_sudanese_pound_custom(self):
        """test_sudanese_pound_custom."""
        amount = 1000
        sudanese_pound = SudanesePound(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert sudanese_pound.amount == decimal
        assert sudanese_pound.numeric_code == '938'
        assert sudanese_pound.alpha_code == 'SDG'
        assert sudanese_pound.decimal_places == 5
        assert sudanese_pound.decimal_sign == '\u066C'
        assert sudanese_pound.grouping_places == 2
        assert sudanese_pound.grouping_sign == '\u066B'
        assert sudanese_pound.international
        assert sudanese_pound.symbol == 'ج.س'
        assert not sudanese_pound.symbol_ahead
        assert sudanese_pound.symbol_separator == '_'
        assert sudanese_pound.localized_symbol == 'ج.س'
        assert sudanese_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert sudanese_pound.__hash__() == hash((decimal, 'SDG', '938'))
        assert sudanese_pound.__repr__() == (
            'SudanesePound(amount: 1000, '
            'alpha_code: "SDG", '
            'symbol: "ج.س", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ج.س", '
            'numeric_code: "938", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert sudanese_pound.__str__() == 'SDG 10,00.00000'


    def test_sudanese_pound_changed(self):
        """test_csudanese_pound_changed."""
        sudanese_pound = SudanesePound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sudanese_pound.international = True


    def test_sudanese_pound_math_add(self):
        """test_sudanese_pound_math_add."""
        sudanese_pound_one = SudanesePound(amount=1)
        sudanese_pound_two = SudanesePound(amount=2)
        sudanese_pound_three = SudanesePound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SDG and OTHER.'):
            _ = sudanese_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.SudanesePound\'> '
                    'and <class \'str\'>.')):
            _ = sudanese_pound_one.__add__('1.00')
        assert (
            sudanese_pound_one +
            sudanese_pound_two) == sudanese_pound_three


    def test_sudanese_pound_slots(self):
        """test_sudanese_pound_slots."""
        sudanese_pound = SudanesePound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SudanesePound\' '
                    'object has no attribute \'new_variable\'')):
            sudanese_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Saint Helena Pound representation."""

from multicurrency import SaintHelenaPound


class TestSaintHelenaPound:

    def test_saint_helena_pound(self):
        """test_saint_helena_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        saint_helena_pound = SaintHelenaPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert saint_helena_pound.amount == decimal
        assert saint_helena_pound.numeric_code == '654'
        assert saint_helena_pound.alpha_code == 'SHP'
        assert saint_helena_pound.decimal_places == 2
        assert saint_helena_pound.decimal_sign == '.'
        assert saint_helena_pound.grouping_places == 3
        assert saint_helena_pound.grouping_sign == ','
        assert not saint_helena_pound.international
        assert saint_helena_pound.symbol == '£'
        assert saint_helena_pound.symbol_ahead
        assert saint_helena_pound.symbol_separator == ''
        assert saint_helena_pound.localized_symbol == 'SH£'
        assert saint_helena_pound.convertion == ''
        assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
        assert saint_helena_pound.__repr__() == (
            'SaintHelenaPound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SHP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SH£", '
            'numeric_code: "654", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert saint_helena_pound.__str__() == '£0.14'


    def test_saint_helena_pound_negative(self):
        """test_saint_helena_pound_negative."""
        amount = -100
        saint_helena_pound = SaintHelenaPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert saint_helena_pound.numeric_code == '654'
        assert saint_helena_pound.alpha_code == 'SHP'
        assert saint_helena_pound.decimal_places == 2
        assert saint_helena_pound.decimal_sign == '.'
        assert saint_helena_pound.grouping_places == 3
        assert saint_helena_pound.grouping_sign == ','
        assert not saint_helena_pound.international
        assert saint_helena_pound.symbol == '£'
        assert saint_helena_pound.symbol_ahead
        assert saint_helena_pound.symbol_separator == ''
        assert saint_helena_pound.localized_symbol == 'SH£'
        assert saint_helena_pound.convertion == ''
        assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
        assert saint_helena_pound.__repr__() == (
            'SaintHelenaPound(amount: -100, '
            'alpha_code: "SHP", '
            'symbol: "£", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SH£", '
            'numeric_code: "654", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert saint_helena_pound.__str__() == '£-100.00'


    def test_saint_helena_pound_custom(self):
        """test_saint_helena_pound_custom."""
        amount = 1000
        saint_helena_pound = SaintHelenaPound(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert saint_helena_pound.amount == decimal
        assert saint_helena_pound.numeric_code == '654'
        assert saint_helena_pound.alpha_code == 'SHP'
        assert saint_helena_pound.decimal_places == 5
        assert saint_helena_pound.decimal_sign == ','
        assert saint_helena_pound.grouping_places == 2
        assert saint_helena_pound.grouping_sign == '.'
        assert saint_helena_pound.international
        assert saint_helena_pound.symbol == '£'
        assert not saint_helena_pound.symbol_ahead
        assert saint_helena_pound.symbol_separator == '_'
        assert saint_helena_pound.localized_symbol == 'SH£'
        assert saint_helena_pound.convertion == ''
        assert saint_helena_pound.__hash__() == hash((decimal, 'SHP', '654'))
        assert saint_helena_pound.__repr__() == (
            'SaintHelenaPound(amount: 1000, '
            'alpha_code: "SHP", '
            'symbol: "£", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SH£", '
            'numeric_code: "654", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert saint_helena_pound.__str__() == 'SHP 10,00.00000'


    def test_saint_helena_pound_changed(self):
        """test_csaint_helena_pound_changed."""
        saint_helena_pound = SaintHelenaPound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            saint_helena_pound.international = True


    def test_saint_helena_pound_math_add(self):
        """test_saint_helena_pound_math_add."""
        saint_helena_pound_one = SaintHelenaPound(amount=1)
        saint_helena_pound_two = SaintHelenaPound(amount=2)
        saint_helena_pound_three = SaintHelenaPound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SHP and OTHER.'):
            _ = saint_helena_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.SaintHelenaPound\'> '
                    'and <class \'str\'>.')):
            _ = saint_helena_pound_one.__add__('1.00')
        assert (
            saint_helena_pound_one +
            saint_helena_pound_two) == saint_helena_pound_three


    def test_saint_helena_pound_slots(self):
        """test_saint_helena_pound_slots."""
        saint_helena_pound = SaintHelenaPound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SaintHelenaPound\' '
                    'object has no attribute \'new_variable\'')):
            saint_helena_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Syrian Pound representation."""

from multicurrency import SyrianPound


class TestSyrianPound:

    def test_syrian_pound(self):
        """test_syrian_pound."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        syrian_pound = SyrianPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert syrian_pound.amount == decimal
        assert syrian_pound.numeric_code == '760'
        assert syrian_pound.alpha_code == 'SYP'
        assert syrian_pound.decimal_places == 2
        assert syrian_pound.decimal_sign == '\u066B'
        assert syrian_pound.grouping_places == 3
        assert syrian_pound.grouping_sign == '\u066C'
        assert not syrian_pound.international
        assert syrian_pound.symbol == 'ل.س'
        assert not syrian_pound.symbol_ahead
        assert syrian_pound.symbol_separator == '\u00A0'
        assert syrian_pound.localized_symbol == 'ل.س'
        assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
        assert syrian_pound.__repr__() == (
            'SyrianPound(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SYP", '
            'symbol: "ل.س", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ل.س", '
            'numeric_code: "760", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert syrian_pound.__str__() == '٠٫١٤ ل.س'


    def test_syrian_pound_negative(self):
        """test_syrian_pound_negative."""
        amount = -100
        syrian_pound = SyrianPound(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert syrian_pound.numeric_code == '760'
        assert syrian_pound.alpha_code == 'SYP'
        assert syrian_pound.decimal_places == 2
        assert syrian_pound.decimal_sign == '\u066B'
        assert syrian_pound.grouping_places == 3
        assert syrian_pound.grouping_sign == '\u066C'
        assert not syrian_pound.international
        assert syrian_pound.symbol == 'ل.س'
        assert not syrian_pound.symbol_ahead
        assert syrian_pound.symbol_separator == '\u00A0'
        assert syrian_pound.localized_symbol == 'ل.س'
        assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
        assert syrian_pound.__repr__() == (
            'SyrianPound(amount: -100, '
            'alpha_code: "SYP", '
            'symbol: "ل.س", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ل.س", '
            'numeric_code: "760", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert syrian_pound.__str__() == '-١٠٠٫٠٠ ل.س'


    def test_syrian_pound_custom(self):
        """test_syrian_pound_custom."""
        amount = 1000
        syrian_pound = SyrianPound(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert syrian_pound.amount == decimal
        assert syrian_pound.numeric_code == '760'
        assert syrian_pound.alpha_code == 'SYP'
        assert syrian_pound.decimal_places == 5
        assert syrian_pound.decimal_sign == '\u066C'
        assert syrian_pound.grouping_places == 2
        assert syrian_pound.grouping_sign == '\u066B'
        assert syrian_pound.international
        assert syrian_pound.symbol == 'ل.س'
        assert not syrian_pound.symbol_ahead
        assert syrian_pound.symbol_separator == '_'
        assert syrian_pound.localized_symbol == 'ل.س'
        assert syrian_pound.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert syrian_pound.__hash__() == hash((decimal, 'SYP', '760'))
        assert syrian_pound.__repr__() == (
            'SyrianPound(amount: 1000, '
            'alpha_code: "SYP", '
            'symbol: "ل.س", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ل.س", '
            'numeric_code: "760", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert syrian_pound.__str__() == 'SYP 10,00.00000'


    def test_syrian_pound_changed(self):
        """test_csyrian_pound_changed."""
        syrian_pound = SyrianPound(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            syrian_pound.international = True


    def test_syrian_pound_math_add(self):
        """test_syrian_pound_math_add."""
        syrian_pound_one = SyrianPound(amount=1)
        syrian_pound_two = SyrianPound(amount=2)
        syrian_pound_three = SyrianPound(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SYP and OTHER.'):
            _ = syrian_pound_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'pound.SyrianPound\'> '
                    'and <class \'str\'>.')):
            _ = syrian_pound_one.__add__('1.00')
        assert (
            syrian_pound_one +
            syrian_pound_two) == syrian_pound_three


    def test_syrian_pound_slots(self):
        """test_syrian_pound_slots."""
        syrian_pound = SyrianPound(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SyrianPound\' '
                    'object has no attribute \'new_variable\'')):
            syrian_pound.new_variable = 'fail'  # pylint: disable=assigning-non-slot
