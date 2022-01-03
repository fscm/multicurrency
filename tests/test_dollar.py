# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dollar currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Australian Dollar representation."""

from multicurrency import AustralianDollar


class TestAustralianDollar:
    """AustralianDollar currency tests."""

    def test_australian_dollar(self):
        """test_australian_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar = AustralianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar.amount == decimal
        assert australian_dollar.numeric_code == '036'
        assert australian_dollar.alpha_code == 'AUD'
        assert australian_dollar.decimal_places == 2
        assert australian_dollar.decimal_sign == '.'
        assert australian_dollar.grouping_places == 3
        assert australian_dollar.grouping_sign == ','
        assert not australian_dollar.international
        assert australian_dollar.symbol == '$'
        assert australian_dollar.symbol_ahead
        assert australian_dollar.symbol_separator == ''
        assert australian_dollar.localized_symbol == '$'
        assert australian_dollar.convertion == ''
        assert australian_dollar.__hash__() == hash(
            (australian_dollar.__class__, decimal, 'AUD', '036'))
        assert australian_dollar.__repr__() == (
            'AustralianDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar.__str__() == '$0.14'

    def test_australian_dollar_negative(self):
        """test_australian_dollar_negative."""
        amount = -100
        australian_dollar = AustralianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar.numeric_code == '036'
        assert australian_dollar.alpha_code == 'AUD'
        assert australian_dollar.decimal_places == 2
        assert australian_dollar.decimal_sign == '.'
        assert australian_dollar.grouping_places == 3
        assert australian_dollar.grouping_sign == ','
        assert not australian_dollar.international
        assert australian_dollar.symbol == '$'
        assert australian_dollar.symbol_ahead
        assert australian_dollar.symbol_separator == ''
        assert australian_dollar.localized_symbol == '$'
        assert australian_dollar.convertion == ''
        assert australian_dollar.__hash__() == hash(
            (australian_dollar.__class__, decimal, 'AUD', '036'))
        assert australian_dollar.__repr__() == (
            'AustralianDollar(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar.__str__() == '$-100.00'

    def test_australian_dollar_custom(self):
        """test_australian_dollar_custom."""
        amount = 1000
        australian_dollar = AustralianDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar.amount == decimal
        assert australian_dollar.numeric_code == '036'
        assert australian_dollar.alpha_code == 'AUD'
        assert australian_dollar.decimal_places == 5
        assert australian_dollar.decimal_sign == ','
        assert australian_dollar.grouping_places == 2
        assert australian_dollar.grouping_sign == '.'
        assert australian_dollar.international
        assert australian_dollar.symbol == '$'
        assert not australian_dollar.symbol_ahead
        assert australian_dollar.symbol_separator == '_'
        assert australian_dollar.localized_symbol == '$'
        assert australian_dollar.convertion == ''
        assert australian_dollar.__hash__() == hash(
            (australian_dollar.__class__, decimal, 'AUD', '036'))
        assert australian_dollar.__repr__() == (
            'AustralianDollar(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_changed(self):
        """test_caustralian_dollar_changed."""
        australian_dollar = AustralianDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar.international = True

    def test_australian_dollar_math_add(self):
        """test_australian_dollar_math_add."""
        australian_dollar_one = AustralianDollar(amount=1)
        australian_dollar_two = AustralianDollar(amount=2)
        australian_dollar_three = AustralianDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollar\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_one.__add__('1.00')
        assert (
            australian_dollar_one +
            australian_dollar_two) == australian_dollar_three

    def test_australian_dollar_slots(self):
        """test_australian_dollar_slots."""
        australian_dollar = AustralianDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollar\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Australian Dollar AU representation."""

from multicurrency import AustralianDollarAU


class TestAustralianDollarAU:
    """AustralianDollarAU currency tests."""

    def test_australian_dollar_au(self):
        """test_australian_dollar_au."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar_au = AustralianDollarAU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_au.amount == decimal
        assert australian_dollar_au.numeric_code == '036'
        assert australian_dollar_au.alpha_code == 'AUD'
        assert australian_dollar_au.decimal_places == 2
        assert australian_dollar_au.decimal_sign == '.'
        assert australian_dollar_au.grouping_places == 3
        assert australian_dollar_au.grouping_sign == ','
        assert not australian_dollar_au.international
        assert australian_dollar_au.symbol == '$'
        assert australian_dollar_au.symbol_ahead
        assert australian_dollar_au.symbol_separator == ''
        assert australian_dollar_au.localized_symbol == 'AU$'
        assert australian_dollar_au.convertion == ''
        assert australian_dollar_au.__hash__() == hash(
            (australian_dollar_au.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_au.__repr__() == (
            'AustralianDollarAU(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AU$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_au.__str__() == '$0.14'

    def test_australian_dollar_au_negative(self):
        """test_australian_dollar_au_negative."""
        amount = -100
        australian_dollar_au = AustralianDollarAU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_au.numeric_code == '036'
        assert australian_dollar_au.alpha_code == 'AUD'
        assert australian_dollar_au.decimal_places == 2
        assert australian_dollar_au.decimal_sign == '.'
        assert australian_dollar_au.grouping_places == 3
        assert australian_dollar_au.grouping_sign == ','
        assert not australian_dollar_au.international
        assert australian_dollar_au.symbol == '$'
        assert australian_dollar_au.symbol_ahead
        assert australian_dollar_au.symbol_separator == ''
        assert australian_dollar_au.localized_symbol == 'AU$'
        assert australian_dollar_au.convertion == ''
        assert australian_dollar_au.__hash__() == hash(
            (australian_dollar_au.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_au.__repr__() == (
            'AustralianDollarAU(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AU$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_au.__str__() == '$-100.00'

    def test_australian_dollar_au_custom(self):
        """test_australian_dollar_au_custom."""
        amount = 1000
        australian_dollar_au = AustralianDollarAU(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_au.amount == decimal
        assert australian_dollar_au.numeric_code == '036'
        assert australian_dollar_au.alpha_code == 'AUD'
        assert australian_dollar_au.decimal_places == 5
        assert australian_dollar_au.decimal_sign == ','
        assert australian_dollar_au.grouping_places == 2
        assert australian_dollar_au.grouping_sign == '.'
        assert australian_dollar_au.international
        assert australian_dollar_au.symbol == '$'
        assert not australian_dollar_au.symbol_ahead
        assert australian_dollar_au.symbol_separator == '_'
        assert australian_dollar_au.localized_symbol == 'AU$'
        assert australian_dollar_au.convertion == ''
        assert australian_dollar_au.__hash__() == hash(
            (australian_dollar_au.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_au.__repr__() == (
            'AustralianDollarAU(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AU$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar_au.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_au_changed(self):
        """test_caustralian_dollar_au_changed."""
        australian_dollar_au = AustralianDollarAU(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_au.international = True

    def test_australian_dollar_au_math_add(self):
        """test_australian_dollar_au_math_add."""
        australian_dollar_au_one = AustralianDollarAU(amount=1)
        australian_dollar_au_two = AustralianDollarAU(amount=2)
        australian_dollar_au_three = AustralianDollarAU(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_au_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollarAU\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_au_one.__add__('1.00')
        assert (
            australian_dollar_au_one +
            australian_dollar_au_two) == australian_dollar_au_three

    def test_australian_dollar_au_slots(self):
        """test_australian_dollar_au_slots."""
        australian_dollar_au = AustralianDollarAU(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollarAU\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar_au.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Australian Dollar KI representation."""

from multicurrency import AustralianDollarKI


class TestAustralianDollarKI:
    """AustralianDollarKI currency tests."""

    def test_australian_dollar_ki(self):
        """test_australian_dollar_ki."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar_ki = AustralianDollarKI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_ki.amount == decimal
        assert australian_dollar_ki.numeric_code == '036'
        assert australian_dollar_ki.alpha_code == 'AUD'
        assert australian_dollar_ki.decimal_places == 2
        assert australian_dollar_ki.decimal_sign == '.'
        assert australian_dollar_ki.grouping_places == 3
        assert australian_dollar_ki.grouping_sign == ','
        assert not australian_dollar_ki.international
        assert australian_dollar_ki.symbol == '$'
        assert australian_dollar_ki.symbol_ahead
        assert australian_dollar_ki.symbol_separator == ''
        assert australian_dollar_ki.localized_symbol == 'KI$'
        assert australian_dollar_ki.convertion == ''
        assert australian_dollar_ki.__hash__() == hash(
            (australian_dollar_ki.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_ki.__repr__() == (
            'AustralianDollarKI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KI$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_ki.__str__() == '$0.14'

    def test_australian_dollar_ki_negative(self):
        """test_australian_dollar_ki_negative."""
        amount = -100
        australian_dollar_ki = AustralianDollarKI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_ki.numeric_code == '036'
        assert australian_dollar_ki.alpha_code == 'AUD'
        assert australian_dollar_ki.decimal_places == 2
        assert australian_dollar_ki.decimal_sign == '.'
        assert australian_dollar_ki.grouping_places == 3
        assert australian_dollar_ki.grouping_sign == ','
        assert not australian_dollar_ki.international
        assert australian_dollar_ki.symbol == '$'
        assert australian_dollar_ki.symbol_ahead
        assert australian_dollar_ki.symbol_separator == ''
        assert australian_dollar_ki.localized_symbol == 'KI$'
        assert australian_dollar_ki.convertion == ''
        assert australian_dollar_ki.__hash__() == hash(
            (australian_dollar_ki.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_ki.__repr__() == (
            'AustralianDollarKI(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KI$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_ki.__str__() == '$-100.00'

    def test_australian_dollar_ki_custom(self):
        """test_australian_dollar_ki_custom."""
        amount = 1000
        australian_dollar_ki = AustralianDollarKI(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_ki.amount == decimal
        assert australian_dollar_ki.numeric_code == '036'
        assert australian_dollar_ki.alpha_code == 'AUD'
        assert australian_dollar_ki.decimal_places == 5
        assert australian_dollar_ki.decimal_sign == ','
        assert australian_dollar_ki.grouping_places == 2
        assert australian_dollar_ki.grouping_sign == '.'
        assert australian_dollar_ki.international
        assert australian_dollar_ki.symbol == '$'
        assert not australian_dollar_ki.symbol_ahead
        assert australian_dollar_ki.symbol_separator == '_'
        assert australian_dollar_ki.localized_symbol == 'KI$'
        assert australian_dollar_ki.convertion == ''
        assert australian_dollar_ki.__hash__() == hash(
            (australian_dollar_ki.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_ki.__repr__() == (
            'AustralianDollarKI(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "KI$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar_ki.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_ki_changed(self):
        """test_caustralian_dollar_ki_changed."""
        australian_dollar_ki = AustralianDollarKI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_ki.international = True

    def test_australian_dollar_ki_math_add(self):
        """test_australian_dollar_ki_math_add."""
        australian_dollar_ki_one = AustralianDollarKI(amount=1)
        australian_dollar_ki_two = AustralianDollarKI(amount=2)
        australian_dollar_ki_three = AustralianDollarKI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_ki_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollarKI\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_ki_one.__add__('1.00')
        assert (
            australian_dollar_ki_one +
            australian_dollar_ki_two) == australian_dollar_ki_three

    def test_australian_dollar_ki_slots(self):
        """test_australian_dollar_ki_slots."""
        australian_dollar_ki = AustralianDollarKI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollarKI\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar_ki.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Australian Dollar CC representation."""

from multicurrency import AustralianDollarCC


class TestAustralianDollarCC:
    """AustralianDollarCC currency tests."""

    def test_australian_dollar_cc(self):
        """test_australian_dollar_cc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar_cc = AustralianDollarCC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_cc.amount == decimal
        assert australian_dollar_cc.numeric_code == '036'
        assert australian_dollar_cc.alpha_code == 'AUD'
        assert australian_dollar_cc.decimal_places == 2
        assert australian_dollar_cc.decimal_sign == '.'
        assert australian_dollar_cc.grouping_places == 3
        assert australian_dollar_cc.grouping_sign == ','
        assert not australian_dollar_cc.international
        assert australian_dollar_cc.symbol == '$'
        assert australian_dollar_cc.symbol_ahead
        assert australian_dollar_cc.symbol_separator == ''
        assert australian_dollar_cc.localized_symbol == 'CC$'
        assert australian_dollar_cc.convertion == ''
        assert australian_dollar_cc.__hash__() == hash(
            (australian_dollar_cc.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_cc.__repr__() == (
            'AustralianDollarCC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CC$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_cc.__str__() == '$0.14'

    def test_australian_dollar_cc_negative(self):
        """test_australian_dollar_cc_negative."""
        amount = -100
        australian_dollar_cc = AustralianDollarCC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_cc.numeric_code == '036'
        assert australian_dollar_cc.alpha_code == 'AUD'
        assert australian_dollar_cc.decimal_places == 2
        assert australian_dollar_cc.decimal_sign == '.'
        assert australian_dollar_cc.grouping_places == 3
        assert australian_dollar_cc.grouping_sign == ','
        assert not australian_dollar_cc.international
        assert australian_dollar_cc.symbol == '$'
        assert australian_dollar_cc.symbol_ahead
        assert australian_dollar_cc.symbol_separator == ''
        assert australian_dollar_cc.localized_symbol == 'CC$'
        assert australian_dollar_cc.convertion == ''
        assert australian_dollar_cc.__hash__() == hash(
            (australian_dollar_cc.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_cc.__repr__() == (
            'AustralianDollarCC(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CC$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_cc.__str__() == '$-100.00'

    def test_australian_dollar_cc_custom(self):
        """test_australian_dollar_cc_custom."""
        amount = 1000
        australian_dollar_cc = AustralianDollarCC(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_cc.amount == decimal
        assert australian_dollar_cc.numeric_code == '036'
        assert australian_dollar_cc.alpha_code == 'AUD'
        assert australian_dollar_cc.decimal_places == 5
        assert australian_dollar_cc.decimal_sign == ','
        assert australian_dollar_cc.grouping_places == 2
        assert australian_dollar_cc.grouping_sign == '.'
        assert australian_dollar_cc.international
        assert australian_dollar_cc.symbol == '$'
        assert not australian_dollar_cc.symbol_ahead
        assert australian_dollar_cc.symbol_separator == '_'
        assert australian_dollar_cc.localized_symbol == 'CC$'
        assert australian_dollar_cc.convertion == ''
        assert australian_dollar_cc.__hash__() == hash(
            (australian_dollar_cc.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_cc.__repr__() == (
            'AustralianDollarCC(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CC$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar_cc.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_cc_changed(self):
        """test_caustralian_dollar_cc_changed."""
        australian_dollar_cc = AustralianDollarCC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_cc.international = True

    def test_australian_dollar_cc_math_add(self):
        """test_australian_dollar_cc_math_add."""
        australian_dollar_cc_one = AustralianDollarCC(amount=1)
        australian_dollar_cc_two = AustralianDollarCC(amount=2)
        australian_dollar_cc_three = AustralianDollarCC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_cc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollarCC\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_cc_one.__add__('1.00')
        assert (
            australian_dollar_cc_one +
            australian_dollar_cc_two) == australian_dollar_cc_three

    def test_australian_dollar_cc_slots(self):
        """test_australian_dollar_cc_slots."""
        australian_dollar_cc = AustralianDollarCC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollarCC\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar_cc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Australian Dollar MR representation."""

from multicurrency import AustralianDollarMR


class TestAustralianDollarMR:
    """AustralianDollarMR currency tests."""

    def test_australian_dollar_mr(self):
        """test_australian_dollar_mr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar_mr = AustralianDollarMR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_mr.amount == decimal
        assert australian_dollar_mr.numeric_code == '036'
        assert australian_dollar_mr.alpha_code == 'AUD'
        assert australian_dollar_mr.decimal_places == 2
        assert australian_dollar_mr.decimal_sign == '.'
        assert australian_dollar_mr.grouping_places == 3
        assert australian_dollar_mr.grouping_sign == ','
        assert not australian_dollar_mr.international
        assert australian_dollar_mr.symbol == '$'
        assert australian_dollar_mr.symbol_ahead
        assert australian_dollar_mr.symbol_separator == ''
        assert australian_dollar_mr.localized_symbol == 'NR$'
        assert australian_dollar_mr.convertion == ''
        assert australian_dollar_mr.__hash__() == hash(
            (australian_dollar_mr.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_mr.__repr__() == (
            'AustralianDollarMR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NR$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_mr.__str__() == '$0.14'

    def test_australian_dollar_mr_negative(self):
        """test_australian_dollar_mr_negative."""
        amount = -100
        australian_dollar_mr = AustralianDollarMR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_mr.numeric_code == '036'
        assert australian_dollar_mr.alpha_code == 'AUD'
        assert australian_dollar_mr.decimal_places == 2
        assert australian_dollar_mr.decimal_sign == '.'
        assert australian_dollar_mr.grouping_places == 3
        assert australian_dollar_mr.grouping_sign == ','
        assert not australian_dollar_mr.international
        assert australian_dollar_mr.symbol == '$'
        assert australian_dollar_mr.symbol_ahead
        assert australian_dollar_mr.symbol_separator == ''
        assert australian_dollar_mr.localized_symbol == 'NR$'
        assert australian_dollar_mr.convertion == ''
        assert australian_dollar_mr.__hash__() == hash(
            (australian_dollar_mr.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_mr.__repr__() == (
            'AustralianDollarMR(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NR$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_mr.__str__() == '$-100.00'

    def test_australian_dollar_mr_custom(self):
        """test_australian_dollar_mr_custom."""
        amount = 1000
        australian_dollar_mr = AustralianDollarMR(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_mr.amount == decimal
        assert australian_dollar_mr.numeric_code == '036'
        assert australian_dollar_mr.alpha_code == 'AUD'
        assert australian_dollar_mr.decimal_places == 5
        assert australian_dollar_mr.decimal_sign == ','
        assert australian_dollar_mr.grouping_places == 2
        assert australian_dollar_mr.grouping_sign == '.'
        assert australian_dollar_mr.international
        assert australian_dollar_mr.symbol == '$'
        assert not australian_dollar_mr.symbol_ahead
        assert australian_dollar_mr.symbol_separator == '_'
        assert australian_dollar_mr.localized_symbol == 'NR$'
        assert australian_dollar_mr.convertion == ''
        assert australian_dollar_mr.__hash__() == hash(
            (australian_dollar_mr.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_mr.__repr__() == (
            'AustralianDollarMR(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NR$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar_mr.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_mr_changed(self):
        """test_caustralian_dollar_mr_changed."""
        australian_dollar_mr = AustralianDollarMR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_mr.international = True

    def test_australian_dollar_mr_math_add(self):
        """test_australian_dollar_mr_math_add."""
        australian_dollar_mr_one = AustralianDollarMR(amount=1)
        australian_dollar_mr_two = AustralianDollarMR(amount=2)
        australian_dollar_mr_three = AustralianDollarMR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_mr_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollarMR\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_mr_one.__add__('1.00')
        assert (
            australian_dollar_mr_one +
            australian_dollar_mr_two) == australian_dollar_mr_three

    def test_australian_dollar_mr_slots(self):
        """test_australian_dollar_mr_slots."""
        australian_dollar_mr = AustralianDollarMR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollarMR\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar_mr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Australian Dollar TV representation."""

from multicurrency import AustralianDollarTV


class TestAustralianDollarTV:
    """AustralianDollarTV currency tests."""

    def test_australian_dollar_tv(self):
        """test_australian_dollar_tv."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        australian_dollar_tv = AustralianDollarTV(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_tv.amount == decimal
        assert australian_dollar_tv.numeric_code == '036'
        assert australian_dollar_tv.alpha_code == 'AUD'
        assert australian_dollar_tv.decimal_places == 2
        assert australian_dollar_tv.decimal_sign == '.'
        assert australian_dollar_tv.grouping_places == 3
        assert australian_dollar_tv.grouping_sign == ','
        assert not australian_dollar_tv.international
        assert australian_dollar_tv.symbol == '$'
        assert australian_dollar_tv.symbol_ahead
        assert australian_dollar_tv.symbol_separator == ''
        assert australian_dollar_tv.localized_symbol == 'TV$'
        assert australian_dollar_tv.convertion == ''
        assert australian_dollar_tv.__hash__() == hash(
            (australian_dollar_tv.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_tv.__repr__() == (
            'AustralianDollarTV(amount: 0.1428571428571428571428571429, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TV$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_tv.__str__() == '$0.14'

    def test_australian_dollar_tv_negative(self):
        """test_australian_dollar_tv_negative."""
        amount = -100
        australian_dollar_tv = AustralianDollarTV(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_tv.numeric_code == '036'
        assert australian_dollar_tv.alpha_code == 'AUD'
        assert australian_dollar_tv.decimal_places == 2
        assert australian_dollar_tv.decimal_sign == '.'
        assert australian_dollar_tv.grouping_places == 3
        assert australian_dollar_tv.grouping_sign == ','
        assert not australian_dollar_tv.international
        assert australian_dollar_tv.symbol == '$'
        assert australian_dollar_tv.symbol_ahead
        assert australian_dollar_tv.symbol_separator == ''
        assert australian_dollar_tv.localized_symbol == 'TV$'
        assert australian_dollar_tv.convertion == ''
        assert australian_dollar_tv.__hash__() == hash(
            (australian_dollar_tv.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_tv.__repr__() == (
            'AustralianDollarTV(amount: -100, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TV$", '
            'numeric_code: "036", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert australian_dollar_tv.__str__() == '$-100.00'

    def test_australian_dollar_tv_custom(self):
        """test_australian_dollar_tv_custom."""
        amount = 1000
        australian_dollar_tv = AustralianDollarTV(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert australian_dollar_tv.amount == decimal
        assert australian_dollar_tv.numeric_code == '036'
        assert australian_dollar_tv.alpha_code == 'AUD'
        assert australian_dollar_tv.decimal_places == 5
        assert australian_dollar_tv.decimal_sign == ','
        assert australian_dollar_tv.grouping_places == 2
        assert australian_dollar_tv.grouping_sign == '.'
        assert australian_dollar_tv.international
        assert australian_dollar_tv.symbol == '$'
        assert not australian_dollar_tv.symbol_ahead
        assert australian_dollar_tv.symbol_separator == '_'
        assert australian_dollar_tv.localized_symbol == 'TV$'
        assert australian_dollar_tv.convertion == ''
        assert australian_dollar_tv.__hash__() == hash(
            (australian_dollar_tv.__class__, decimal, 'AUD', '036'))
        assert australian_dollar_tv.__repr__() == (
            'AustralianDollarTV(amount: 1000, '
            'alpha_code: "AUD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TV$", '
            'numeric_code: "036", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert australian_dollar_tv.__str__() == 'AUD 10,00.00000'

    def test_australian_dollar_tv_changed(self):
        """test_caustralian_dollar_tv_changed."""
        australian_dollar_tv = AustralianDollarTV(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            australian_dollar_tv.international = True

    def test_australian_dollar_tv_math_add(self):
        """test_australian_dollar_tv_math_add."""
        australian_dollar_tv_one = AustralianDollarTV(amount=1)
        australian_dollar_tv_two = AustralianDollarTV(amount=2)
        australian_dollar_tv_three = AustralianDollarTV(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency AUD and OTHER.'):
            _ = australian_dollar_tv_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.AustralianDollarTV\'> '
                    'and <class \'str\'>.')):
            _ = australian_dollar_tv_one.__add__('1.00')
        assert (
            australian_dollar_tv_one +
            australian_dollar_tv_two) == australian_dollar_tv_three

    def test_australian_dollar_tv_slots(self):
        """test_australian_dollar_tv_slots."""
        australian_dollar_tv = AustralianDollarTV(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'AustralianDollarTV\' '
                    'object has no attribute \'new_variable\'')):
            australian_dollar_tv.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Barbados Dollar representation."""

from multicurrency import BarbadosDollar


class TestBarbadosDollar:
    """BarbadosDollar currency tests."""

    def test_barbados_dollar(self):
        """test_barbados_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        barbados_dollar = BarbadosDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert barbados_dollar.amount == decimal
        assert barbados_dollar.numeric_code == '052'
        assert barbados_dollar.alpha_code == 'BBD'
        assert barbados_dollar.decimal_places == 2
        assert barbados_dollar.decimal_sign == '.'
        assert barbados_dollar.grouping_places == 3
        assert barbados_dollar.grouping_sign == ','
        assert not barbados_dollar.international
        assert barbados_dollar.symbol == '$'
        assert barbados_dollar.symbol_ahead
        assert barbados_dollar.symbol_separator == ''
        assert barbados_dollar.localized_symbol == 'BB$'
        assert barbados_dollar.convertion == ''
        assert barbados_dollar.__hash__() == hash(
            (barbados_dollar.__class__, decimal, 'BBD', '052'))
        assert barbados_dollar.__repr__() == (
            'BarbadosDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BBD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BB$", '
            'numeric_code: "052", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert barbados_dollar.__str__() == '$0.14'

    def test_barbados_dollar_negative(self):
        """test_barbados_dollar_negative."""
        amount = -100
        barbados_dollar = BarbadosDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert barbados_dollar.numeric_code == '052'
        assert barbados_dollar.alpha_code == 'BBD'
        assert barbados_dollar.decimal_places == 2
        assert barbados_dollar.decimal_sign == '.'
        assert barbados_dollar.grouping_places == 3
        assert barbados_dollar.grouping_sign == ','
        assert not barbados_dollar.international
        assert barbados_dollar.symbol == '$'
        assert barbados_dollar.symbol_ahead
        assert barbados_dollar.symbol_separator == ''
        assert barbados_dollar.localized_symbol == 'BB$'
        assert barbados_dollar.convertion == ''
        assert barbados_dollar.__hash__() == hash(
            (barbados_dollar.__class__, decimal, 'BBD', '052'))
        assert barbados_dollar.__repr__() == (
            'BarbadosDollar(amount: -100, '
            'alpha_code: "BBD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BB$", '
            'numeric_code: "052", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert barbados_dollar.__str__() == '$-100.00'

    def test_barbados_dollar_custom(self):
        """test_barbados_dollar_custom."""
        amount = 1000
        barbados_dollar = BarbadosDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert barbados_dollar.amount == decimal
        assert barbados_dollar.numeric_code == '052'
        assert barbados_dollar.alpha_code == 'BBD'
        assert barbados_dollar.decimal_places == 5
        assert barbados_dollar.decimal_sign == ','
        assert barbados_dollar.grouping_places == 2
        assert barbados_dollar.grouping_sign == '.'
        assert barbados_dollar.international
        assert barbados_dollar.symbol == '$'
        assert not barbados_dollar.symbol_ahead
        assert barbados_dollar.symbol_separator == '_'
        assert barbados_dollar.localized_symbol == 'BB$'
        assert barbados_dollar.convertion == ''
        assert barbados_dollar.__hash__() == hash(
            (barbados_dollar.__class__, decimal, 'BBD', '052'))
        assert barbados_dollar.__repr__() == (
            'BarbadosDollar(amount: 1000, '
            'alpha_code: "BBD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BB$", '
            'numeric_code: "052", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert barbados_dollar.__str__() == 'BBD 10,00.00000'

    def test_barbados_dollar_changed(self):
        """test_cbarbados_dollar_changed."""
        barbados_dollar = BarbadosDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            barbados_dollar.international = True

    def test_barbados_dollar_math_add(self):
        """test_barbados_dollar_math_add."""
        barbados_dollar_one = BarbadosDollar(amount=1)
        barbados_dollar_two = BarbadosDollar(amount=2)
        barbados_dollar_three = BarbadosDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BBD and OTHER.'):
            _ = barbados_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BarbadosDollar\'> '
                    'and <class \'str\'>.')):
            _ = barbados_dollar_one.__add__('1.00')
        assert (
            barbados_dollar_one +
            barbados_dollar_two) == barbados_dollar_three

    def test_barbados_dollar_slots(self):
        """test_barbados_dollar_slots."""
        barbados_dollar = BarbadosDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BarbadosDollar\' '
                    'object has no attribute \'new_variable\'')):
            barbados_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Bermudian Dollar representation."""

from multicurrency import BermudianDollar


class TestBermudianDollar:
    """BermudianDollar currency tests."""

    def test_bermudian_dollar(self):
        """test_bermudian_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        bermudian_dollar = BermudianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bermudian_dollar.amount == decimal
        assert bermudian_dollar.numeric_code == '060'
        assert bermudian_dollar.alpha_code == 'BMD'
        assert bermudian_dollar.decimal_places == 2
        assert bermudian_dollar.decimal_sign == '.'
        assert bermudian_dollar.grouping_places == 3
        assert bermudian_dollar.grouping_sign == ','
        assert not bermudian_dollar.international
        assert bermudian_dollar.symbol == '$'
        assert bermudian_dollar.symbol_ahead
        assert bermudian_dollar.symbol_separator == ''
        assert bermudian_dollar.localized_symbol == 'BM$'
        assert bermudian_dollar.convertion == ''
        assert bermudian_dollar.__hash__() == hash(
            (bermudian_dollar.__class__, decimal, 'BMD', '060'))
        assert bermudian_dollar.__repr__() == (
            'BermudianDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BMD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BM$", '
            'numeric_code: "060", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bermudian_dollar.__str__() == '$0.14'

    def test_bermudian_dollar_negative(self):
        """test_bermudian_dollar_negative."""
        amount = -100
        bermudian_dollar = BermudianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bermudian_dollar.numeric_code == '060'
        assert bermudian_dollar.alpha_code == 'BMD'
        assert bermudian_dollar.decimal_places == 2
        assert bermudian_dollar.decimal_sign == '.'
        assert bermudian_dollar.grouping_places == 3
        assert bermudian_dollar.grouping_sign == ','
        assert not bermudian_dollar.international
        assert bermudian_dollar.symbol == '$'
        assert bermudian_dollar.symbol_ahead
        assert bermudian_dollar.symbol_separator == ''
        assert bermudian_dollar.localized_symbol == 'BM$'
        assert bermudian_dollar.convertion == ''
        assert bermudian_dollar.__hash__() == hash(
            (bermudian_dollar.__class__, decimal, 'BMD', '060'))
        assert bermudian_dollar.__repr__() == (
            'BermudianDollar(amount: -100, '
            'alpha_code: "BMD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BM$", '
            'numeric_code: "060", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bermudian_dollar.__str__() == '$-100.00'

    def test_bermudian_dollar_custom(self):
        """test_bermudian_dollar_custom."""
        amount = 1000
        bermudian_dollar = BermudianDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert bermudian_dollar.amount == decimal
        assert bermudian_dollar.numeric_code == '060'
        assert bermudian_dollar.alpha_code == 'BMD'
        assert bermudian_dollar.decimal_places == 5
        assert bermudian_dollar.decimal_sign == ','
        assert bermudian_dollar.grouping_places == 2
        assert bermudian_dollar.grouping_sign == '.'
        assert bermudian_dollar.international
        assert bermudian_dollar.symbol == '$'
        assert not bermudian_dollar.symbol_ahead
        assert bermudian_dollar.symbol_separator == '_'
        assert bermudian_dollar.localized_symbol == 'BM$'
        assert bermudian_dollar.convertion == ''
        assert bermudian_dollar.__hash__() == hash(
            (bermudian_dollar.__class__, decimal, 'BMD', '060'))
        assert bermudian_dollar.__repr__() == (
            'BermudianDollar(amount: 1000, '
            'alpha_code: "BMD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BM$", '
            'numeric_code: "060", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert bermudian_dollar.__str__() == 'BMD 10,00.00000'

    def test_bermudian_dollar_changed(self):
        """test_cbermudian_dollar_changed."""
        bermudian_dollar = BermudianDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bermudian_dollar.international = True

    def test_bermudian_dollar_math_add(self):
        """test_bermudian_dollar_math_add."""
        bermudian_dollar_one = BermudianDollar(amount=1)
        bermudian_dollar_two = BermudianDollar(amount=2)
        bermudian_dollar_three = BermudianDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BMD and OTHER.'):
            _ = bermudian_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BermudianDollar\'> '
                    'and <class \'str\'>.')):
            _ = bermudian_dollar_one.__add__('1.00')
        assert (
            bermudian_dollar_one +
            bermudian_dollar_two) == bermudian_dollar_three

    def test_bermudian_dollar_slots(self):
        """test_bermudian_dollar_slots."""
        bermudian_dollar = BermudianDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BermudianDollar\' '
                    'object has no attribute \'new_variable\'')):
            bermudian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Brunei Dollar representation."""

from multicurrency import BruneiDollar


class TestBruneiDollar:
    """BruneiDollar currency tests."""

    def test_brunei_dollar(self):
        """test_brunei_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        brunei_dollar = BruneiDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar.amount == decimal
        assert brunei_dollar.numeric_code == '096'
        assert brunei_dollar.alpha_code == 'BND'
        assert brunei_dollar.decimal_places == 2
        assert brunei_dollar.decimal_sign == ','
        assert brunei_dollar.grouping_places == 3
        assert brunei_dollar.grouping_sign == '.'
        assert not brunei_dollar.international
        assert brunei_dollar.symbol == '$'
        assert brunei_dollar.symbol_ahead
        assert brunei_dollar.symbol_separator == '\u00A0'
        assert brunei_dollar.localized_symbol == '$'
        assert brunei_dollar.convertion == ''
        assert brunei_dollar.__hash__() == hash(
            (brunei_dollar.__class__, decimal, 'BND', '096'))
        assert brunei_dollar.__repr__() == (
            'BruneiDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar.__str__() == '$ 0,14'

    def test_brunei_dollar_negative(self):
        """test_brunei_dollar_negative."""
        amount = -100
        brunei_dollar = BruneiDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar.numeric_code == '096'
        assert brunei_dollar.alpha_code == 'BND'
        assert brunei_dollar.decimal_places == 2
        assert brunei_dollar.decimal_sign == ','
        assert brunei_dollar.grouping_places == 3
        assert brunei_dollar.grouping_sign == '.'
        assert not brunei_dollar.international
        assert brunei_dollar.symbol == '$'
        assert brunei_dollar.symbol_ahead
        assert brunei_dollar.symbol_separator == '\u00A0'
        assert brunei_dollar.localized_symbol == '$'
        assert brunei_dollar.convertion == ''
        assert brunei_dollar.__hash__() == hash(
            (brunei_dollar.__class__, decimal, 'BND', '096'))
        assert brunei_dollar.__repr__() == (
            'BruneiDollar(amount: -100, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar.__str__() == '$ -100,00'

    def test_brunei_dollar_custom(self):
        """test_brunei_dollar_custom."""
        amount = 1000
        brunei_dollar = BruneiDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar.amount == decimal
        assert brunei_dollar.numeric_code == '096'
        assert brunei_dollar.alpha_code == 'BND'
        assert brunei_dollar.decimal_places == 5
        assert brunei_dollar.decimal_sign == '.'
        assert brunei_dollar.grouping_places == 2
        assert brunei_dollar.grouping_sign == ','
        assert brunei_dollar.international
        assert brunei_dollar.symbol == '$'
        assert not brunei_dollar.symbol_ahead
        assert brunei_dollar.symbol_separator == '_'
        assert brunei_dollar.localized_symbol == '$'
        assert brunei_dollar.convertion == ''
        assert brunei_dollar.__hash__() == hash(
            (brunei_dollar.__class__, decimal, 'BND', '096'))
        assert brunei_dollar.__repr__() == (
            'BruneiDollar(amount: 1000, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "$", '
            'numeric_code: "096", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert brunei_dollar.__str__() == 'BND 10,00.00000'

    def test_brunei_dollar_changed(self):
        """test_cbrunei_dollar_changed."""
        brunei_dollar = BruneiDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar.international = True

    def test_brunei_dollar_math_add(self):
        """test_brunei_dollar_math_add."""
        brunei_dollar_one = BruneiDollar(amount=1)
        brunei_dollar_two = BruneiDollar(amount=2)
        brunei_dollar_three = BruneiDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BND and OTHER.'):
            _ = brunei_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BruneiDollar\'> '
                    'and <class \'str\'>.')):
            _ = brunei_dollar_one.__add__('1.00')
        assert (
            brunei_dollar_one +
            brunei_dollar_two) == brunei_dollar_three

    def test_brunei_dollar_slots(self):
        """test_brunei_dollar_slots."""
        brunei_dollar = BruneiDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BruneiDollar\' '
                    'object has no attribute \'new_variable\'')):
            brunei_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Brunei Dollar BN representation."""

from multicurrency import BruneiDollarBN


class TestBruneiDollarBN:
    """BruneiDollarBN currency tests."""

    def test_brunei_dollar_bn(self):
        """test_brunei_dollar_bn."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        brunei_dollar_bn = BruneiDollarBN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_bn.amount == decimal
        assert brunei_dollar_bn.numeric_code == '096'
        assert brunei_dollar_bn.alpha_code == 'BND'
        assert brunei_dollar_bn.decimal_places == 2
        assert brunei_dollar_bn.decimal_sign == ','
        assert brunei_dollar_bn.grouping_places == 3
        assert brunei_dollar_bn.grouping_sign == '.'
        assert not brunei_dollar_bn.international
        assert brunei_dollar_bn.symbol == '$'
        assert brunei_dollar_bn.symbol_ahead
        assert brunei_dollar_bn.symbol_separator == '\u00A0'
        assert brunei_dollar_bn.localized_symbol == 'BN$'
        assert brunei_dollar_bn.convertion == ''
        assert brunei_dollar_bn.__hash__() == hash(
            (brunei_dollar_bn.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_bn.__repr__() == (
            'BruneiDollarBN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BN$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar_bn.__str__() == '$ 0,14'

    def test_brunei_dollar_bn_negative(self):
        """test_brunei_dollar_bn_negative."""
        amount = -100
        brunei_dollar_bn = BruneiDollarBN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_bn.numeric_code == '096'
        assert brunei_dollar_bn.alpha_code == 'BND'
        assert brunei_dollar_bn.decimal_places == 2
        assert brunei_dollar_bn.decimal_sign == ','
        assert brunei_dollar_bn.grouping_places == 3
        assert brunei_dollar_bn.grouping_sign == '.'
        assert not brunei_dollar_bn.international
        assert brunei_dollar_bn.symbol == '$'
        assert brunei_dollar_bn.symbol_ahead
        assert brunei_dollar_bn.symbol_separator == '\u00A0'
        assert brunei_dollar_bn.localized_symbol == 'BN$'
        assert brunei_dollar_bn.convertion == ''
        assert brunei_dollar_bn.__hash__() == hash(
            (brunei_dollar_bn.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_bn.__repr__() == (
            'BruneiDollarBN(amount: -100, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BN$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar_bn.__str__() == '$ -100,00'

    def test_brunei_dollar_bn_custom(self):
        """test_brunei_dollar_bn_custom."""
        amount = 1000
        brunei_dollar_bn = BruneiDollarBN(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_bn.amount == decimal
        assert brunei_dollar_bn.numeric_code == '096'
        assert brunei_dollar_bn.alpha_code == 'BND'
        assert brunei_dollar_bn.decimal_places == 5
        assert brunei_dollar_bn.decimal_sign == '.'
        assert brunei_dollar_bn.grouping_places == 2
        assert brunei_dollar_bn.grouping_sign == ','
        assert brunei_dollar_bn.international
        assert brunei_dollar_bn.symbol == '$'
        assert not brunei_dollar_bn.symbol_ahead
        assert brunei_dollar_bn.symbol_separator == '_'
        assert brunei_dollar_bn.localized_symbol == 'BN$'
        assert brunei_dollar_bn.convertion == ''
        assert brunei_dollar_bn.__hash__() == hash(
            (brunei_dollar_bn.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_bn.__repr__() == (
            'BruneiDollarBN(amount: 1000, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BN$", '
            'numeric_code: "096", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert brunei_dollar_bn.__str__() == 'BND 10,00.00000'

    def test_brunei_dollar_bn_changed(self):
        """test_cbrunei_dollar_bn_changed."""
        brunei_dollar_bn = BruneiDollarBN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_bn.international = True

    def test_brunei_dollar_bn_math_add(self):
        """test_brunei_dollar_bn_math_add."""
        brunei_dollar_bn_one = BruneiDollarBN(amount=1)
        brunei_dollar_bn_two = BruneiDollarBN(amount=2)
        brunei_dollar_bn_three = BruneiDollarBN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BND and OTHER.'):
            _ = brunei_dollar_bn_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BruneiDollarBN\'> '
                    'and <class \'str\'>.')):
            _ = brunei_dollar_bn_one.__add__('1.00')
        assert (
            brunei_dollar_bn_one +
            brunei_dollar_bn_two) == brunei_dollar_bn_three

    def test_brunei_dollar_bn_slots(self):
        """test_brunei_dollar_bn_slots."""
        brunei_dollar_bn = BruneiDollarBN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BruneiDollarBN\' '
                    'object has no attribute \'new_variable\'')):
            brunei_dollar_bn.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Brunei Dollar SG representation."""

from multicurrency import BruneiDollarSG


class TestBruneiDollarSG:
    """BruneiDollarSG currency tests."""

    def test_brunei_dollar_sg(self):
        """test_brunei_dollar_sg."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        brunei_dollar_sg = BruneiDollarSG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_sg.amount == decimal
        assert brunei_dollar_sg.numeric_code == '096'
        assert brunei_dollar_sg.alpha_code == 'BND'
        assert brunei_dollar_sg.decimal_places == 2
        assert brunei_dollar_sg.decimal_sign == ','
        assert brunei_dollar_sg.grouping_places == 3
        assert brunei_dollar_sg.grouping_sign == '.'
        assert not brunei_dollar_sg.international
        assert brunei_dollar_sg.symbol == '$'
        assert brunei_dollar_sg.symbol_ahead
        assert brunei_dollar_sg.symbol_separator == '\u00A0'
        assert brunei_dollar_sg.localized_symbol == 'SG$'
        assert brunei_dollar_sg.convertion == ''
        assert brunei_dollar_sg.__hash__() == hash(
            (brunei_dollar_sg.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_sg.__repr__() == (
            'BruneiDollarSG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SG$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar_sg.__str__() == '$ 0,14'

    def test_brunei_dollar_sg_negative(self):
        """test_brunei_dollar_sg_negative."""
        amount = -100
        brunei_dollar_sg = BruneiDollarSG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_sg.numeric_code == '096'
        assert brunei_dollar_sg.alpha_code == 'BND'
        assert brunei_dollar_sg.decimal_places == 2
        assert brunei_dollar_sg.decimal_sign == ','
        assert brunei_dollar_sg.grouping_places == 3
        assert brunei_dollar_sg.grouping_sign == '.'
        assert not brunei_dollar_sg.international
        assert brunei_dollar_sg.symbol == '$'
        assert brunei_dollar_sg.symbol_ahead
        assert brunei_dollar_sg.symbol_separator == '\u00A0'
        assert brunei_dollar_sg.localized_symbol == 'SG$'
        assert brunei_dollar_sg.convertion == ''
        assert brunei_dollar_sg.__hash__() == hash(
            (brunei_dollar_sg.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_sg.__repr__() == (
            'BruneiDollarSG(amount: -100, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SG$", '
            'numeric_code: "096", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert brunei_dollar_sg.__str__() == '$ -100,00'

    def test_brunei_dollar_sg_custom(self):
        """test_brunei_dollar_sg_custom."""
        amount = 1000
        brunei_dollar_sg = BruneiDollarSG(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert brunei_dollar_sg.amount == decimal
        assert brunei_dollar_sg.numeric_code == '096'
        assert brunei_dollar_sg.alpha_code == 'BND'
        assert brunei_dollar_sg.decimal_places == 5
        assert brunei_dollar_sg.decimal_sign == '.'
        assert brunei_dollar_sg.grouping_places == 2
        assert brunei_dollar_sg.grouping_sign == ','
        assert brunei_dollar_sg.international
        assert brunei_dollar_sg.symbol == '$'
        assert not brunei_dollar_sg.symbol_ahead
        assert brunei_dollar_sg.symbol_separator == '_'
        assert brunei_dollar_sg.localized_symbol == 'SG$'
        assert brunei_dollar_sg.convertion == ''
        assert brunei_dollar_sg.__hash__() == hash(
            (brunei_dollar_sg.__class__, decimal, 'BND', '096'))
        assert brunei_dollar_sg.__repr__() == (
            'BruneiDollarSG(amount: 1000, '
            'alpha_code: "BND", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SG$", '
            'numeric_code: "096", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert brunei_dollar_sg.__str__() == 'BND 10,00.00000'

    def test_brunei_dollar_sg_changed(self):
        """test_cbrunei_dollar_sg_changed."""
        brunei_dollar_sg = BruneiDollarSG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            brunei_dollar_sg.international = True

    def test_brunei_dollar_sg_math_add(self):
        """test_brunei_dollar_sg_math_add."""
        brunei_dollar_sg_one = BruneiDollarSG(amount=1)
        brunei_dollar_sg_two = BruneiDollarSG(amount=2)
        brunei_dollar_sg_three = BruneiDollarSG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BND and OTHER.'):
            _ = brunei_dollar_sg_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BruneiDollarSG\'> '
                    'and <class \'str\'>.')):
            _ = brunei_dollar_sg_one.__add__('1.00')
        assert (
            brunei_dollar_sg_one +
            brunei_dollar_sg_two) == brunei_dollar_sg_three

    def test_brunei_dollar_sg_slots(self):
        """test_brunei_dollar_sg_slots."""
        brunei_dollar_sg = BruneiDollarSG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BruneiDollarSG\' '
                    'object has no attribute \'new_variable\'')):
            brunei_dollar_sg.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Bahamian Dollar representation."""

from multicurrency import BahamianDollar


class TestBahamianDollar:
    """BahamianDollar currency tests."""

    def test_bahamian_dollar(self):
        """test_bahamian_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        bahamian_dollar = BahamianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bahamian_dollar.amount == decimal
        assert bahamian_dollar.numeric_code == '044'
        assert bahamian_dollar.alpha_code == 'BSD'
        assert bahamian_dollar.decimal_places == 2
        assert bahamian_dollar.decimal_sign == '.'
        assert bahamian_dollar.grouping_places == 3
        assert bahamian_dollar.grouping_sign == ','
        assert not bahamian_dollar.international
        assert bahamian_dollar.symbol == '$'
        assert bahamian_dollar.symbol_ahead
        assert bahamian_dollar.symbol_separator == ''
        assert bahamian_dollar.localized_symbol == 'BS$'
        assert bahamian_dollar.convertion == ''
        assert bahamian_dollar.__hash__() == hash(
            (bahamian_dollar.__class__, decimal, 'BSD', '044'))
        assert bahamian_dollar.__repr__() == (
            'BahamianDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BSD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BS$", '
            'numeric_code: "044", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bahamian_dollar.__str__() == '$0.14'

    def test_bahamian_dollar_negative(self):
        """test_bahamian_dollar_negative."""
        amount = -100
        bahamian_dollar = BahamianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bahamian_dollar.numeric_code == '044'
        assert bahamian_dollar.alpha_code == 'BSD'
        assert bahamian_dollar.decimal_places == 2
        assert bahamian_dollar.decimal_sign == '.'
        assert bahamian_dollar.grouping_places == 3
        assert bahamian_dollar.grouping_sign == ','
        assert not bahamian_dollar.international
        assert bahamian_dollar.symbol == '$'
        assert bahamian_dollar.symbol_ahead
        assert bahamian_dollar.symbol_separator == ''
        assert bahamian_dollar.localized_symbol == 'BS$'
        assert bahamian_dollar.convertion == ''
        assert bahamian_dollar.__hash__() == hash(
            (bahamian_dollar.__class__, decimal, 'BSD', '044'))
        assert bahamian_dollar.__repr__() == (
            'BahamianDollar(amount: -100, '
            'alpha_code: "BSD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BS$", '
            'numeric_code: "044", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bahamian_dollar.__str__() == '$-100.00'

    def test_bahamian_dollar_custom(self):
        """test_bahamian_dollar_custom."""
        amount = 1000
        bahamian_dollar = BahamianDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert bahamian_dollar.amount == decimal
        assert bahamian_dollar.numeric_code == '044'
        assert bahamian_dollar.alpha_code == 'BSD'
        assert bahamian_dollar.decimal_places == 5
        assert bahamian_dollar.decimal_sign == ','
        assert bahamian_dollar.grouping_places == 2
        assert bahamian_dollar.grouping_sign == '.'
        assert bahamian_dollar.international
        assert bahamian_dollar.symbol == '$'
        assert not bahamian_dollar.symbol_ahead
        assert bahamian_dollar.symbol_separator == '_'
        assert bahamian_dollar.localized_symbol == 'BS$'
        assert bahamian_dollar.convertion == ''
        assert bahamian_dollar.__hash__() == hash(
            (bahamian_dollar.__class__, decimal, 'BSD', '044'))
        assert bahamian_dollar.__repr__() == (
            'BahamianDollar(amount: 1000, '
            'alpha_code: "BSD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BS$", '
            'numeric_code: "044", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert bahamian_dollar.__str__() == 'BSD 10,00.00000'

    def test_bahamian_dollar_changed(self):
        """test_cbahamian_dollar_changed."""
        bahamian_dollar = BahamianDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bahamian_dollar.international = True

    def test_bahamian_dollar_math_add(self):
        """test_bahamian_dollar_math_add."""
        bahamian_dollar_one = BahamianDollar(amount=1)
        bahamian_dollar_two = BahamianDollar(amount=2)
        bahamian_dollar_three = BahamianDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BSD and OTHER.'):
            _ = bahamian_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BahamianDollar\'> '
                    'and <class \'str\'>.')):
            _ = bahamian_dollar_one.__add__('1.00')
        assert (
            bahamian_dollar_one +
            bahamian_dollar_two) == bahamian_dollar_three

    def test_bahamian_dollar_slots(self):
        """test_bahamian_dollar_slots."""
        bahamian_dollar = BahamianDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BahamianDollar\' '
                    'object has no attribute \'new_variable\'')):
            bahamian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Belize Dollar representation."""

from multicurrency import BelizeDollar


class TestBelizeDollar:
    """BelizeDollar currency tests."""

    def test_belize_dollar(self):
        """test_belize_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        belize_dollar = BelizeDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert belize_dollar.amount == decimal
        assert belize_dollar.numeric_code == '084'
        assert belize_dollar.alpha_code == 'BZD'
        assert belize_dollar.decimal_places == 2
        assert belize_dollar.decimal_sign == '.'
        assert belize_dollar.grouping_places == 3
        assert belize_dollar.grouping_sign == ','
        assert not belize_dollar.international
        assert belize_dollar.symbol == '$'
        assert belize_dollar.symbol_ahead
        assert belize_dollar.symbol_separator == ''
        assert belize_dollar.localized_symbol == 'BZ$'
        assert belize_dollar.convertion == ''
        assert belize_dollar.__hash__() == hash(
            (belize_dollar.__class__, decimal, 'BZD', '084'))
        assert belize_dollar.__repr__() == (
            'BelizeDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BZ$", '
            'numeric_code: "084", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert belize_dollar.__str__() == '$0.14'

    def test_belize_dollar_negative(self):
        """test_belize_dollar_negative."""
        amount = -100
        belize_dollar = BelizeDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert belize_dollar.numeric_code == '084'
        assert belize_dollar.alpha_code == 'BZD'
        assert belize_dollar.decimal_places == 2
        assert belize_dollar.decimal_sign == '.'
        assert belize_dollar.grouping_places == 3
        assert belize_dollar.grouping_sign == ','
        assert not belize_dollar.international
        assert belize_dollar.symbol == '$'
        assert belize_dollar.symbol_ahead
        assert belize_dollar.symbol_separator == ''
        assert belize_dollar.localized_symbol == 'BZ$'
        assert belize_dollar.convertion == ''
        assert belize_dollar.__hash__() == hash(
            (belize_dollar.__class__, decimal, 'BZD', '084'))
        assert belize_dollar.__repr__() == (
            'BelizeDollar(amount: -100, '
            'alpha_code: "BZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BZ$", '
            'numeric_code: "084", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert belize_dollar.__str__() == '$-100.00'

    def test_belize_dollar_custom(self):
        """test_belize_dollar_custom."""
        amount = 1000
        belize_dollar = BelizeDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert belize_dollar.amount == decimal
        assert belize_dollar.numeric_code == '084'
        assert belize_dollar.alpha_code == 'BZD'
        assert belize_dollar.decimal_places == 5
        assert belize_dollar.decimal_sign == ','
        assert belize_dollar.grouping_places == 2
        assert belize_dollar.grouping_sign == '.'
        assert belize_dollar.international
        assert belize_dollar.symbol == '$'
        assert not belize_dollar.symbol_ahead
        assert belize_dollar.symbol_separator == '_'
        assert belize_dollar.localized_symbol == 'BZ$'
        assert belize_dollar.convertion == ''
        assert belize_dollar.__hash__() == hash(
            (belize_dollar.__class__, decimal, 'BZD', '084'))
        assert belize_dollar.__repr__() == (
            'BelizeDollar(amount: 1000, '
            'alpha_code: "BZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BZ$", '
            'numeric_code: "084", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert belize_dollar.__str__() == 'BZD 10,00.00000'

    def test_belize_dollar_changed(self):
        """test_cbelize_dollar_changed."""
        belize_dollar = BelizeDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            belize_dollar.international = True

    def test_belize_dollar_math_add(self):
        """test_belize_dollar_math_add."""
        belize_dollar_one = BelizeDollar(amount=1)
        belize_dollar_two = BelizeDollar(amount=2)
        belize_dollar_three = BelizeDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BZD and OTHER.'):
            _ = belize_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.BelizeDollar\'> '
                    'and <class \'str\'>.')):
            _ = belize_dollar_one.__add__('1.00')
        assert (
            belize_dollar_one +
            belize_dollar_two) == belize_dollar_three

    def test_belize_dollar_slots(self):
        """test_belize_dollar_slots."""
        belize_dollar = BelizeDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BelizeDollar\' '
                    'object has no attribute \'new_variable\'')):
            belize_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Canadian Dollar EN representation."""

from multicurrency import CanadianDollarEN


class TestCanadianDollarEN:
    """CanadianDollarEN currency tests."""

    def test_canadian_dollar_en(self):
        """test_canadian_dollar_en."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        canadian_dollar_en = CanadianDollarEN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_en.amount == decimal
        assert canadian_dollar_en.numeric_code == '124'
        assert canadian_dollar_en.alpha_code == 'CAD'
        assert canadian_dollar_en.decimal_places == 2
        assert canadian_dollar_en.decimal_sign == '.'
        assert canadian_dollar_en.grouping_places == 3
        assert canadian_dollar_en.grouping_sign == ','
        assert not canadian_dollar_en.international
        assert canadian_dollar_en.symbol == '$'
        assert canadian_dollar_en.symbol_ahead
        assert canadian_dollar_en.symbol_separator == ''
        assert canadian_dollar_en.localized_symbol == 'CA$'
        assert canadian_dollar_en.convertion == ''
        assert canadian_dollar_en.__hash__() == hash(
            (canadian_dollar_en.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_en.__repr__() == (
            'CanadianDollarEN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert canadian_dollar_en.__str__() == '$0.14'

    def test_canadian_dollar_en_negative(self):
        """test_canadian_dollar_en_negative."""
        amount = -100
        canadian_dollar_en = CanadianDollarEN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_en.numeric_code == '124'
        assert canadian_dollar_en.alpha_code == 'CAD'
        assert canadian_dollar_en.decimal_places == 2
        assert canadian_dollar_en.decimal_sign == '.'
        assert canadian_dollar_en.grouping_places == 3
        assert canadian_dollar_en.grouping_sign == ','
        assert not canadian_dollar_en.international
        assert canadian_dollar_en.symbol == '$'
        assert canadian_dollar_en.symbol_ahead
        assert canadian_dollar_en.symbol_separator == ''
        assert canadian_dollar_en.localized_symbol == 'CA$'
        assert canadian_dollar_en.convertion == ''
        assert canadian_dollar_en.__hash__() == hash(
            (canadian_dollar_en.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_en.__repr__() == (
            'CanadianDollarEN(amount: -100, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert canadian_dollar_en.__str__() == '$-100.00'

    def test_canadian_dollar_en_custom(self):
        """test_canadian_dollar_en_custom."""
        amount = 1000
        canadian_dollar_en = CanadianDollarEN(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_en.amount == decimal
        assert canadian_dollar_en.numeric_code == '124'
        assert canadian_dollar_en.alpha_code == 'CAD'
        assert canadian_dollar_en.decimal_places == 5
        assert canadian_dollar_en.decimal_sign == ','
        assert canadian_dollar_en.grouping_places == 2
        assert canadian_dollar_en.grouping_sign == '.'
        assert canadian_dollar_en.international
        assert canadian_dollar_en.symbol == '$'
        assert not canadian_dollar_en.symbol_ahead
        assert canadian_dollar_en.symbol_separator == '_'
        assert canadian_dollar_en.localized_symbol == 'CA$'
        assert canadian_dollar_en.convertion == ''
        assert canadian_dollar_en.__hash__() == hash(
            (canadian_dollar_en.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_en.__repr__() == (
            'CanadianDollarEN(amount: 1000, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert canadian_dollar_en.__str__() == 'CAD 10,00.00000'

    def test_canadian_dollar_en_changed(self):
        """test_ccanadian_dollar_en_changed."""
        canadian_dollar_en = CanadianDollarEN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_en.international = True

    def test_canadian_dollar_en_math_add(self):
        """test_canadian_dollar_en_math_add."""
        canadian_dollar_en_one = CanadianDollarEN(amount=1)
        canadian_dollar_en_two = CanadianDollarEN(amount=2)
        canadian_dollar_en_three = CanadianDollarEN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CAD and OTHER.'):
            _ = canadian_dollar_en_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.CanadianDollarEN\'> '
                    'and <class \'str\'>.')):
            _ = canadian_dollar_en_one.__add__('1.00')
        assert (
            canadian_dollar_en_one +
            canadian_dollar_en_two) == canadian_dollar_en_three

    def test_canadian_dollar_en_slots(self):
        """test_canadian_dollar_en_slots."""
        canadian_dollar_en = CanadianDollarEN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CanadianDollarEN\' '
                    'object has no attribute \'new_variable\'')):
            canadian_dollar_en.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Canadian Dollar FR representation."""

from multicurrency import CanadianDollarFR


class TestCanadianDollarFR:
    """CanadianDollarFR currency tests."""

    def test_canadian_dollar_fr(self):
        """test_canadian_dollar_fr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        canadian_dollar_fr = CanadianDollarFR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_fr.amount == decimal
        assert canadian_dollar_fr.numeric_code == '124'
        assert canadian_dollar_fr.alpha_code == 'CAD'
        assert canadian_dollar_fr.decimal_places == 2
        assert canadian_dollar_fr.decimal_sign == ','
        assert canadian_dollar_fr.grouping_places == 3
        assert canadian_dollar_fr.grouping_sign == '\u202F'
        assert not canadian_dollar_fr.international
        assert canadian_dollar_fr.symbol == '$'
        assert not canadian_dollar_fr.symbol_ahead
        assert canadian_dollar_fr.symbol_separator == '\u00A0'
        assert canadian_dollar_fr.localized_symbol == 'CA$'
        assert canadian_dollar_fr.convertion == ''
        assert canadian_dollar_fr.__hash__() == hash(
            (canadian_dollar_fr.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_fr.__repr__() == (
            'CanadianDollarFR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert canadian_dollar_fr.__str__() == '0,14 $'

    def test_canadian_dollar_fr_negative(self):
        """test_canadian_dollar_fr_negative."""
        amount = -100
        canadian_dollar_fr = CanadianDollarFR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_fr.numeric_code == '124'
        assert canadian_dollar_fr.alpha_code == 'CAD'
        assert canadian_dollar_fr.decimal_places == 2
        assert canadian_dollar_fr.decimal_sign == ','
        assert canadian_dollar_fr.grouping_places == 3
        assert canadian_dollar_fr.grouping_sign == '\u202F'
        assert not canadian_dollar_fr.international
        assert canadian_dollar_fr.symbol == '$'
        assert not canadian_dollar_fr.symbol_ahead
        assert canadian_dollar_fr.symbol_separator == '\u00A0'
        assert canadian_dollar_fr.localized_symbol == 'CA$'
        assert canadian_dollar_fr.convertion == ''
        assert canadian_dollar_fr.__hash__() == hash(
            (canadian_dollar_fr.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_fr.__repr__() == (
            'CanadianDollarFR(amount: -100, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert canadian_dollar_fr.__str__() == '-100,00 $'

    def test_canadian_dollar_fr_custom(self):
        """test_canadian_dollar_fr_custom."""
        amount = 1000
        canadian_dollar_fr = CanadianDollarFR(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert canadian_dollar_fr.amount == decimal
        assert canadian_dollar_fr.numeric_code == '124'
        assert canadian_dollar_fr.alpha_code == 'CAD'
        assert canadian_dollar_fr.decimal_places == 5
        assert canadian_dollar_fr.decimal_sign == '\u202F'
        assert canadian_dollar_fr.grouping_places == 2
        assert canadian_dollar_fr.grouping_sign == ','
        assert canadian_dollar_fr.international
        assert canadian_dollar_fr.symbol == '$'
        assert not canadian_dollar_fr.symbol_ahead
        assert canadian_dollar_fr.symbol_separator == '_'
        assert canadian_dollar_fr.localized_symbol == 'CA$'
        assert canadian_dollar_fr.convertion == ''
        assert canadian_dollar_fr.__hash__() == hash(
            (canadian_dollar_fr.__class__, decimal, 'CAD', '124'))
        assert canadian_dollar_fr.__repr__() == (
            'CanadianDollarFR(amount: 1000, '
            'alpha_code: "CAD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CA$", '
            'numeric_code: "124", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert canadian_dollar_fr.__str__() == 'CAD 10,00.00000'

    def test_canadian_dollar_fr_changed(self):
        """test_ccanadian_dollar_fr_changed."""
        canadian_dollar_fr = CanadianDollarFR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            canadian_dollar_fr.international = True

    def test_canadian_dollar_fr_math_add(self):
        """test_canadian_dollar_fr_math_add."""
        canadian_dollar_fr_one = CanadianDollarFR(amount=1)
        canadian_dollar_fr_two = CanadianDollarFR(amount=2)
        canadian_dollar_fr_three = CanadianDollarFR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CAD and OTHER.'):
            _ = canadian_dollar_fr_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.CanadianDollarFR\'> '
                    'and <class \'str\'>.')):
            _ = canadian_dollar_fr_one.__add__('1.00')
        assert (
            canadian_dollar_fr_one +
            canadian_dollar_fr_two) == canadian_dollar_fr_three

    def test_canadian_dollar_fr_slots(self):
        """test_canadian_dollar_fr_slots."""
        canadian_dollar_fr = CanadianDollarFR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CanadianDollarFR\' '
                    'object has no attribute \'new_variable\'')):
            canadian_dollar_fr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Fiji Dollar representation."""

from multicurrency import FijiDollar


class TestFijiDollar:
    """FijiDollar currency tests."""

    def test_fiji_dollar(self):
        """test_fiji_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        fiji_dollar = FijiDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert fiji_dollar.amount == decimal
        assert fiji_dollar.numeric_code == '242'
        assert fiji_dollar.alpha_code == 'FJD'
        assert fiji_dollar.decimal_places == 2
        assert fiji_dollar.decimal_sign == '.'
        assert fiji_dollar.grouping_places == 3
        assert fiji_dollar.grouping_sign == ','
        assert not fiji_dollar.international
        assert fiji_dollar.symbol == '$'
        assert fiji_dollar.symbol_ahead
        assert fiji_dollar.symbol_separator == ''
        assert fiji_dollar.localized_symbol == 'FJ$'
        assert fiji_dollar.convertion == ''
        assert fiji_dollar.__hash__() == hash(
            (fiji_dollar.__class__, decimal, 'FJD', '242'))
        assert fiji_dollar.__repr__() == (
            'FijiDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "FJD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FJ$", '
            'numeric_code: "242", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert fiji_dollar.__str__() == '$0.14'

    def test_fiji_dollar_negative(self):
        """test_fiji_dollar_negative."""
        amount = -100
        fiji_dollar = FijiDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert fiji_dollar.numeric_code == '242'
        assert fiji_dollar.alpha_code == 'FJD'
        assert fiji_dollar.decimal_places == 2
        assert fiji_dollar.decimal_sign == '.'
        assert fiji_dollar.grouping_places == 3
        assert fiji_dollar.grouping_sign == ','
        assert not fiji_dollar.international
        assert fiji_dollar.symbol == '$'
        assert fiji_dollar.symbol_ahead
        assert fiji_dollar.symbol_separator == ''
        assert fiji_dollar.localized_symbol == 'FJ$'
        assert fiji_dollar.convertion == ''
        assert fiji_dollar.__hash__() == hash(
            (fiji_dollar.__class__, decimal, 'FJD', '242'))
        assert fiji_dollar.__repr__() == (
            'FijiDollar(amount: -100, '
            'alpha_code: "FJD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FJ$", '
            'numeric_code: "242", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert fiji_dollar.__str__() == '$-100.00'

    def test_fiji_dollar_custom(self):
        """test_fiji_dollar_custom."""
        amount = 1000
        fiji_dollar = FijiDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert fiji_dollar.amount == decimal
        assert fiji_dollar.numeric_code == '242'
        assert fiji_dollar.alpha_code == 'FJD'
        assert fiji_dollar.decimal_places == 5
        assert fiji_dollar.decimal_sign == ','
        assert fiji_dollar.grouping_places == 2
        assert fiji_dollar.grouping_sign == '.'
        assert fiji_dollar.international
        assert fiji_dollar.symbol == '$'
        assert not fiji_dollar.symbol_ahead
        assert fiji_dollar.symbol_separator == '_'
        assert fiji_dollar.localized_symbol == 'FJ$'
        assert fiji_dollar.convertion == ''
        assert fiji_dollar.__hash__() == hash(
            (fiji_dollar.__class__, decimal, 'FJD', '242'))
        assert fiji_dollar.__repr__() == (
            'FijiDollar(amount: 1000, '
            'alpha_code: "FJD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "FJ$", '
            'numeric_code: "242", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert fiji_dollar.__str__() == 'FJD 10,00.00000'

    def test_fiji_dollar_changed(self):
        """test_cfiji_dollar_changed."""
        fiji_dollar = FijiDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            fiji_dollar.international = True

    def test_fiji_dollar_math_add(self):
        """test_fiji_dollar_math_add."""
        fiji_dollar_one = FijiDollar(amount=1)
        fiji_dollar_two = FijiDollar(amount=2)
        fiji_dollar_three = FijiDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency FJD and OTHER.'):
            _ = fiji_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.FijiDollar\'> '
                    'and <class \'str\'>.')):
            _ = fiji_dollar_one.__add__('1.00')
        assert (
            fiji_dollar_one +
            fiji_dollar_two) == fiji_dollar_three

    def test_fiji_dollar_slots(self):
        """test_fiji_dollar_slots."""
        fiji_dollar = FijiDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'FijiDollar\' '
                    'object has no attribute \'new_variable\'')):
            fiji_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Guyana Dollar representation."""

from multicurrency import GuyanaDollar


class TestGuyanaDollar:
    """GuyanaDollar currency tests."""

    def test_guyana_dollar(self):
        """test_guyana_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        guyana_dollar = GuyanaDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guyana_dollar.amount == decimal
        assert guyana_dollar.numeric_code == '328'
        assert guyana_dollar.alpha_code == 'GYD'
        assert guyana_dollar.decimal_places == 2
        assert guyana_dollar.decimal_sign == '.'
        assert guyana_dollar.grouping_places == 3
        assert guyana_dollar.grouping_sign == ','
        assert not guyana_dollar.international
        assert guyana_dollar.symbol == '$'
        assert guyana_dollar.symbol_ahead
        assert guyana_dollar.symbol_separator == ''
        assert guyana_dollar.localized_symbol == 'GY$'
        assert guyana_dollar.convertion == ''
        assert guyana_dollar.__hash__() == hash(
            (guyana_dollar.__class__, decimal, 'GYD', '328'))
        assert guyana_dollar.__repr__() == (
            'GuyanaDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GYD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GY$", '
            'numeric_code: "328", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert guyana_dollar.__str__() == '$0.14'

    def test_guyana_dollar_negative(self):
        """test_guyana_dollar_negative."""
        amount = -100
        guyana_dollar = GuyanaDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guyana_dollar.numeric_code == '328'
        assert guyana_dollar.alpha_code == 'GYD'
        assert guyana_dollar.decimal_places == 2
        assert guyana_dollar.decimal_sign == '.'
        assert guyana_dollar.grouping_places == 3
        assert guyana_dollar.grouping_sign == ','
        assert not guyana_dollar.international
        assert guyana_dollar.symbol == '$'
        assert guyana_dollar.symbol_ahead
        assert guyana_dollar.symbol_separator == ''
        assert guyana_dollar.localized_symbol == 'GY$'
        assert guyana_dollar.convertion == ''
        assert guyana_dollar.__hash__() == hash(
            (guyana_dollar.__class__, decimal, 'GYD', '328'))
        assert guyana_dollar.__repr__() == (
            'GuyanaDollar(amount: -100, '
            'alpha_code: "GYD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GY$", '
            'numeric_code: "328", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert guyana_dollar.__str__() == '$-100.00'

    def test_guyana_dollar_custom(self):
        """test_guyana_dollar_custom."""
        amount = 1000
        guyana_dollar = GuyanaDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert guyana_dollar.amount == decimal
        assert guyana_dollar.numeric_code == '328'
        assert guyana_dollar.alpha_code == 'GYD'
        assert guyana_dollar.decimal_places == 5
        assert guyana_dollar.decimal_sign == ','
        assert guyana_dollar.grouping_places == 2
        assert guyana_dollar.grouping_sign == '.'
        assert guyana_dollar.international
        assert guyana_dollar.symbol == '$'
        assert not guyana_dollar.symbol_ahead
        assert guyana_dollar.symbol_separator == '_'
        assert guyana_dollar.localized_symbol == 'GY$'
        assert guyana_dollar.convertion == ''
        assert guyana_dollar.__hash__() == hash(
            (guyana_dollar.__class__, decimal, 'GYD', '328'))
        assert guyana_dollar.__repr__() == (
            'GuyanaDollar(amount: 1000, '
            'alpha_code: "GYD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GY$", '
            'numeric_code: "328", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert guyana_dollar.__str__() == 'GYD 10,00.00000'

    def test_guyana_dollar_changed(self):
        """test_cguyana_dollar_changed."""
        guyana_dollar = GuyanaDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guyana_dollar.international = True

    def test_guyana_dollar_math_add(self):
        """test_guyana_dollar_math_add."""
        guyana_dollar_one = GuyanaDollar(amount=1)
        guyana_dollar_two = GuyanaDollar(amount=2)
        guyana_dollar_three = GuyanaDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GYD and OTHER.'):
            _ = guyana_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.GuyanaDollar\'> '
                    'and <class \'str\'>.')):
            _ = guyana_dollar_one.__add__('1.00')
        assert (
            guyana_dollar_one +
            guyana_dollar_two) == guyana_dollar_three

    def test_guyana_dollar_slots(self):
        """test_guyana_dollar_slots."""
        guyana_dollar = GuyanaDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'GuyanaDollar\' '
                    'object has no attribute \'new_variable\'')):
            guyana_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Hong Kong Dollar representation."""

from multicurrency import HongKongDollar


class TestHongKongDollar:
    """HongKongDollar currency tests."""

    def test_hong_kong_dollar(self):
        """test_hong_kong_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        hong_kong_dollar = HongKongDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert hong_kong_dollar.amount == decimal
        assert hong_kong_dollar.numeric_code == '344'
        assert hong_kong_dollar.alpha_code == 'HKD'
        assert hong_kong_dollar.decimal_places == 2
        assert hong_kong_dollar.decimal_sign == '.'
        assert hong_kong_dollar.grouping_places == 3
        assert hong_kong_dollar.grouping_sign == ','
        assert not hong_kong_dollar.international
        assert hong_kong_dollar.symbol == '$'
        assert hong_kong_dollar.symbol_ahead
        assert hong_kong_dollar.symbol_separator == ''
        assert hong_kong_dollar.localized_symbol == 'HK$'
        assert hong_kong_dollar.convertion == ''
        assert hong_kong_dollar.__hash__() == hash(
            (hong_kong_dollar.__class__, decimal, 'HKD', '344'))
        assert hong_kong_dollar.__repr__() == (
            'HongKongDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "HKD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "HK$", '
            'numeric_code: "344", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert hong_kong_dollar.__str__() == '$0.14'

    def test_hong_kong_dollar_negative(self):
        """test_hong_kong_dollar_negative."""
        amount = -100
        hong_kong_dollar = HongKongDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert hong_kong_dollar.numeric_code == '344'
        assert hong_kong_dollar.alpha_code == 'HKD'
        assert hong_kong_dollar.decimal_places == 2
        assert hong_kong_dollar.decimal_sign == '.'
        assert hong_kong_dollar.grouping_places == 3
        assert hong_kong_dollar.grouping_sign == ','
        assert not hong_kong_dollar.international
        assert hong_kong_dollar.symbol == '$'
        assert hong_kong_dollar.symbol_ahead
        assert hong_kong_dollar.symbol_separator == ''
        assert hong_kong_dollar.localized_symbol == 'HK$'
        assert hong_kong_dollar.convertion == ''
        assert hong_kong_dollar.__hash__() == hash(
            (hong_kong_dollar.__class__, decimal, 'HKD', '344'))
        assert hong_kong_dollar.__repr__() == (
            'HongKongDollar(amount: -100, '
            'alpha_code: "HKD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "HK$", '
            'numeric_code: "344", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert hong_kong_dollar.__str__() == '$-100.00'

    def test_hong_kong_dollar_custom(self):
        """test_hong_kong_dollar_custom."""
        amount = 1000
        hong_kong_dollar = HongKongDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert hong_kong_dollar.amount == decimal
        assert hong_kong_dollar.numeric_code == '344'
        assert hong_kong_dollar.alpha_code == 'HKD'
        assert hong_kong_dollar.decimal_places == 5
        assert hong_kong_dollar.decimal_sign == ','
        assert hong_kong_dollar.grouping_places == 2
        assert hong_kong_dollar.grouping_sign == '.'
        assert hong_kong_dollar.international
        assert hong_kong_dollar.symbol == '$'
        assert not hong_kong_dollar.symbol_ahead
        assert hong_kong_dollar.symbol_separator == '_'
        assert hong_kong_dollar.localized_symbol == 'HK$'
        assert hong_kong_dollar.convertion == ''
        assert hong_kong_dollar.__hash__() == hash(
            (hong_kong_dollar.__class__, decimal, 'HKD', '344'))
        assert hong_kong_dollar.__repr__() == (
            'HongKongDollar(amount: 1000, '
            'alpha_code: "HKD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "HK$", '
            'numeric_code: "344", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert hong_kong_dollar.__str__() == 'HKD 10,00.00000'

    def test_hong_kong_dollar_changed(self):
        """test_chong_kong_dollar_changed."""
        hong_kong_dollar = HongKongDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            hong_kong_dollar.international = True

    def test_hong_kong_dollar_math_add(self):
        """test_hong_kong_dollar_math_add."""
        hong_kong_dollar_one = HongKongDollar(amount=1)
        hong_kong_dollar_two = HongKongDollar(amount=2)
        hong_kong_dollar_three = HongKongDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency HKD and OTHER.'):
            _ = hong_kong_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.HongKongDollar\'> '
                    'and <class \'str\'>.')):
            _ = hong_kong_dollar_one.__add__('1.00')
        assert (
            hong_kong_dollar_one +
            hong_kong_dollar_two) == hong_kong_dollar_three

    def test_hong_kong_dollar_slots(self):
        """test_hong_kong_dollar_slots."""
        hong_kong_dollar = HongKongDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'HongKongDollar\' '
                    'object has no attribute \'new_variable\'')):
            hong_kong_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Jamaican Dollar representation."""

from multicurrency import JamaicanDollar


class TestJamaicanDollar:
    """JamaicanDollar currency tests."""

    def test_jamaican_dollar(self):
        """test_jamaican_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        jamaican_dollar = JamaicanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert jamaican_dollar.amount == decimal
        assert jamaican_dollar.numeric_code == '388'
        assert jamaican_dollar.alpha_code == 'JMD'
        assert jamaican_dollar.decimal_places == 2
        assert jamaican_dollar.decimal_sign == '.'
        assert jamaican_dollar.grouping_places == 3
        assert jamaican_dollar.grouping_sign == ','
        assert not jamaican_dollar.international
        assert jamaican_dollar.symbol == '$'
        assert jamaican_dollar.symbol_ahead
        assert jamaican_dollar.symbol_separator == ''
        assert jamaican_dollar.localized_symbol == 'JM$'
        assert jamaican_dollar.convertion == ''
        assert jamaican_dollar.__hash__() == hash(
            (jamaican_dollar.__class__, decimal, 'JMD', '388'))
        assert jamaican_dollar.__repr__() == (
            'JamaicanDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "JMD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "JM$", '
            'numeric_code: "388", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert jamaican_dollar.__str__() == '$0.14'

    def test_jamaican_dollar_negative(self):
        """test_jamaican_dollar_negative."""
        amount = -100
        jamaican_dollar = JamaicanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert jamaican_dollar.numeric_code == '388'
        assert jamaican_dollar.alpha_code == 'JMD'
        assert jamaican_dollar.decimal_places == 2
        assert jamaican_dollar.decimal_sign == '.'
        assert jamaican_dollar.grouping_places == 3
        assert jamaican_dollar.grouping_sign == ','
        assert not jamaican_dollar.international
        assert jamaican_dollar.symbol == '$'
        assert jamaican_dollar.symbol_ahead
        assert jamaican_dollar.symbol_separator == ''
        assert jamaican_dollar.localized_symbol == 'JM$'
        assert jamaican_dollar.convertion == ''
        assert jamaican_dollar.__hash__() == hash(
            (jamaican_dollar.__class__, decimal, 'JMD', '388'))
        assert jamaican_dollar.__repr__() == (
            'JamaicanDollar(amount: -100, '
            'alpha_code: "JMD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "JM$", '
            'numeric_code: "388", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert jamaican_dollar.__str__() == '$-100.00'

    def test_jamaican_dollar_custom(self):
        """test_jamaican_dollar_custom."""
        amount = 1000
        jamaican_dollar = JamaicanDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert jamaican_dollar.amount == decimal
        assert jamaican_dollar.numeric_code == '388'
        assert jamaican_dollar.alpha_code == 'JMD'
        assert jamaican_dollar.decimal_places == 5
        assert jamaican_dollar.decimal_sign == ','
        assert jamaican_dollar.grouping_places == 2
        assert jamaican_dollar.grouping_sign == '.'
        assert jamaican_dollar.international
        assert jamaican_dollar.symbol == '$'
        assert not jamaican_dollar.symbol_ahead
        assert jamaican_dollar.symbol_separator == '_'
        assert jamaican_dollar.localized_symbol == 'JM$'
        assert jamaican_dollar.convertion == ''
        assert jamaican_dollar.__hash__() == hash(
            (jamaican_dollar.__class__, decimal, 'JMD', '388'))
        assert jamaican_dollar.__repr__() == (
            'JamaicanDollar(amount: 1000, '
            'alpha_code: "JMD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "JM$", '
            'numeric_code: "388", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert jamaican_dollar.__str__() == 'JMD 10,00.00000'

    def test_jamaican_dollar_changed(self):
        """test_cjamaican_dollar_changed."""
        jamaican_dollar = JamaicanDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            jamaican_dollar.international = True

    def test_jamaican_dollar_math_add(self):
        """test_jamaican_dollar_math_add."""
        jamaican_dollar_one = JamaicanDollar(amount=1)
        jamaican_dollar_two = JamaicanDollar(amount=2)
        jamaican_dollar_three = JamaicanDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency JMD and OTHER.'):
            _ = jamaican_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.JamaicanDollar\'> '
                    'and <class \'str\'>.')):
            _ = jamaican_dollar_one.__add__('1.00')
        assert (
            jamaican_dollar_one +
            jamaican_dollar_two) == jamaican_dollar_three

    def test_jamaican_dollar_slots(self):
        """test_jamaican_dollar_slots."""
        jamaican_dollar = JamaicanDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'JamaicanDollar\' '
                    'object has no attribute \'new_variable\'')):
            jamaican_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Cayman Islands Dollar representation."""

from multicurrency import CaymanIslandsDollar


class TestCaymanIslandsDollar:
    """CaymanIslandsDollar currency tests."""

    def test_cayman_islands_dollar(self):
        """test_cayman_islands_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cayman_islands_dollar = CaymanIslandsDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cayman_islands_dollar.amount == decimal
        assert cayman_islands_dollar.numeric_code == '136'
        assert cayman_islands_dollar.alpha_code == 'KYD'
        assert cayman_islands_dollar.decimal_places == 2
        assert cayman_islands_dollar.decimal_sign == '.'
        assert cayman_islands_dollar.grouping_places == 3
        assert cayman_islands_dollar.grouping_sign == ','
        assert not cayman_islands_dollar.international
        assert cayman_islands_dollar.symbol == '$'
        assert cayman_islands_dollar.symbol_ahead
        assert cayman_islands_dollar.symbol_separator == ''
        assert cayman_islands_dollar.localized_symbol == 'KY$'
        assert cayman_islands_dollar.convertion == ''
        assert cayman_islands_dollar.__hash__() == hash(
            (cayman_islands_dollar.__class__, decimal, 'KYD', '136'))
        assert cayman_islands_dollar.__repr__() == (
            'CaymanIslandsDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "KYD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KY$", '
            'numeric_code: "136", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert cayman_islands_dollar.__str__() == '$0.14'

    def test_cayman_islands_dollar_negative(self):
        """test_cayman_islands_dollar_negative."""
        amount = -100
        cayman_islands_dollar = CaymanIslandsDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cayman_islands_dollar.numeric_code == '136'
        assert cayman_islands_dollar.alpha_code == 'KYD'
        assert cayman_islands_dollar.decimal_places == 2
        assert cayman_islands_dollar.decimal_sign == '.'
        assert cayman_islands_dollar.grouping_places == 3
        assert cayman_islands_dollar.grouping_sign == ','
        assert not cayman_islands_dollar.international
        assert cayman_islands_dollar.symbol == '$'
        assert cayman_islands_dollar.symbol_ahead
        assert cayman_islands_dollar.symbol_separator == ''
        assert cayman_islands_dollar.localized_symbol == 'KY$'
        assert cayman_islands_dollar.convertion == ''
        assert cayman_islands_dollar.__hash__() == hash(
            (cayman_islands_dollar.__class__, decimal, 'KYD', '136'))
        assert cayman_islands_dollar.__repr__() == (
            'CaymanIslandsDollar(amount: -100, '
            'alpha_code: "KYD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KY$", '
            'numeric_code: "136", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert cayman_islands_dollar.__str__() == '$-100.00'

    def test_cayman_islands_dollar_custom(self):
        """test_cayman_islands_dollar_custom."""
        amount = 1000
        cayman_islands_dollar = CaymanIslandsDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cayman_islands_dollar.amount == decimal
        assert cayman_islands_dollar.numeric_code == '136'
        assert cayman_islands_dollar.alpha_code == 'KYD'
        assert cayman_islands_dollar.decimal_places == 5
        assert cayman_islands_dollar.decimal_sign == ','
        assert cayman_islands_dollar.grouping_places == 2
        assert cayman_islands_dollar.grouping_sign == '.'
        assert cayman_islands_dollar.international
        assert cayman_islands_dollar.symbol == '$'
        assert not cayman_islands_dollar.symbol_ahead
        assert cayman_islands_dollar.symbol_separator == '_'
        assert cayman_islands_dollar.localized_symbol == 'KY$'
        assert cayman_islands_dollar.convertion == ''
        assert cayman_islands_dollar.__hash__() == hash(
            (cayman_islands_dollar.__class__, decimal, 'KYD', '136'))
        assert cayman_islands_dollar.__repr__() == (
            'CaymanIslandsDollar(amount: 1000, '
            'alpha_code: "KYD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "KY$", '
            'numeric_code: "136", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert cayman_islands_dollar.__str__() == 'KYD 10,00.00000'

    def test_cayman_islands_dollar_changed(self):
        """test_ccayman_islands_dollar_changed."""
        cayman_islands_dollar = CaymanIslandsDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cayman_islands_dollar.international = True

    def test_cayman_islands_dollar_math_add(self):
        """test_cayman_islands_dollar_math_add."""
        cayman_islands_dollar_one = CaymanIslandsDollar(amount=1)
        cayman_islands_dollar_two = CaymanIslandsDollar(amount=2)
        cayman_islands_dollar_three = CaymanIslandsDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency KYD and OTHER.'):
            _ = cayman_islands_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.CaymanIslandsDollar\'> '
                    'and <class \'str\'>.')):
            _ = cayman_islands_dollar_one.__add__('1.00')
        assert (
            cayman_islands_dollar_one +
            cayman_islands_dollar_two) == cayman_islands_dollar_three

    def test_cayman_islands_dollar_slots(self):
        """test_cayman_islands_dollar_slots."""
        cayman_islands_dollar = CaymanIslandsDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CaymanIslandsDollar\' '
                    'object has no attribute \'new_variable\'')):
            cayman_islands_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Liberian Dollar representation."""

from multicurrency import LiberianDollar


class TestLiberianDollar:
    """LiberianDollar currency tests."""

    def test_liberian_dollar(self):
        """test_liberian_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        liberian_dollar = LiberianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert liberian_dollar.amount == decimal
        assert liberian_dollar.numeric_code == '430'
        assert liberian_dollar.alpha_code == 'LRD'
        assert liberian_dollar.decimal_places == 2
        assert liberian_dollar.decimal_sign == '.'
        assert liberian_dollar.grouping_places == 3
        assert liberian_dollar.grouping_sign == ','
        assert not liberian_dollar.international
        assert liberian_dollar.symbol == '$'
        assert liberian_dollar.symbol_ahead
        assert liberian_dollar.symbol_separator == ''
        assert liberian_dollar.localized_symbol == 'LR$'
        assert liberian_dollar.convertion == ''
        assert liberian_dollar.__hash__() == hash(
            (liberian_dollar.__class__, decimal, 'LRD', '430'))
        assert liberian_dollar.__repr__() == (
            'LiberianDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "LRD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "LR$", '
            'numeric_code: "430", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert liberian_dollar.__str__() == '$0.14'

    def test_liberian_dollar_negative(self):
        """test_liberian_dollar_negative."""
        amount = -100
        liberian_dollar = LiberianDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert liberian_dollar.numeric_code == '430'
        assert liberian_dollar.alpha_code == 'LRD'
        assert liberian_dollar.decimal_places == 2
        assert liberian_dollar.decimal_sign == '.'
        assert liberian_dollar.grouping_places == 3
        assert liberian_dollar.grouping_sign == ','
        assert not liberian_dollar.international
        assert liberian_dollar.symbol == '$'
        assert liberian_dollar.symbol_ahead
        assert liberian_dollar.symbol_separator == ''
        assert liberian_dollar.localized_symbol == 'LR$'
        assert liberian_dollar.convertion == ''
        assert liberian_dollar.__hash__() == hash(
            (liberian_dollar.__class__, decimal, 'LRD', '430'))
        assert liberian_dollar.__repr__() == (
            'LiberianDollar(amount: -100, '
            'alpha_code: "LRD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "LR$", '
            'numeric_code: "430", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert liberian_dollar.__str__() == '$-100.00'

    def test_liberian_dollar_custom(self):
        """test_liberian_dollar_custom."""
        amount = 1000
        liberian_dollar = LiberianDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert liberian_dollar.amount == decimal
        assert liberian_dollar.numeric_code == '430'
        assert liberian_dollar.alpha_code == 'LRD'
        assert liberian_dollar.decimal_places == 5
        assert liberian_dollar.decimal_sign == ','
        assert liberian_dollar.grouping_places == 2
        assert liberian_dollar.grouping_sign == '.'
        assert liberian_dollar.international
        assert liberian_dollar.symbol == '$'
        assert not liberian_dollar.symbol_ahead
        assert liberian_dollar.symbol_separator == '_'
        assert liberian_dollar.localized_symbol == 'LR$'
        assert liberian_dollar.convertion == ''
        assert liberian_dollar.__hash__() == hash(
            (liberian_dollar.__class__, decimal, 'LRD', '430'))
        assert liberian_dollar.__repr__() == (
            'LiberianDollar(amount: 1000, '
            'alpha_code: "LRD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LR$", '
            'numeric_code: "430", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert liberian_dollar.__str__() == 'LRD 10,00.00000'

    def test_liberian_dollar_changed(self):
        """test_cliberian_dollar_changed."""
        liberian_dollar = LiberianDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            liberian_dollar.international = True

    def test_liberian_dollar_math_add(self):
        """test_liberian_dollar_math_add."""
        liberian_dollar_one = LiberianDollar(amount=1)
        liberian_dollar_two = LiberianDollar(amount=2)
        liberian_dollar_three = LiberianDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency LRD and OTHER.'):
            _ = liberian_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.LiberianDollar\'> '
                    'and <class \'str\'>.')):
            _ = liberian_dollar_one.__add__('1.00')
        assert (
            liberian_dollar_one +
            liberian_dollar_two) == liberian_dollar_three

    def test_liberian_dollar_slots(self):
        """test_liberian_dollar_slots."""
        liberian_dollar = LiberianDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'LiberianDollar\' '
                    'object has no attribute \'new_variable\'')):
            liberian_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Namibia Dollar representation."""

from multicurrency import NamibiaDollar


class TestNamibiaDollar:
    """NamibiaDollar currency tests."""

    def test_namibia_dollar(self):
        """test_namibia_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        namibia_dollar = NamibiaDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert namibia_dollar.amount == decimal
        assert namibia_dollar.numeric_code == '516'
        assert namibia_dollar.alpha_code == 'NAD'
        assert namibia_dollar.decimal_places == 2
        assert namibia_dollar.decimal_sign == '.'
        assert namibia_dollar.grouping_places == 3
        assert namibia_dollar.grouping_sign == ','
        assert not namibia_dollar.international
        assert namibia_dollar.symbol == '$'
        assert namibia_dollar.symbol_ahead
        assert namibia_dollar.symbol_separator == ''
        assert namibia_dollar.localized_symbol == 'NA$'
        assert namibia_dollar.convertion == ''
        assert namibia_dollar.__hash__() == hash(
            (namibia_dollar.__class__, decimal, 'NAD', '516'))
        assert namibia_dollar.__repr__() == (
            'NamibiaDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NAD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NA$", '
            'numeric_code: "516", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert namibia_dollar.__str__() == '$0.14'

    def test_namibia_dollar_negative(self):
        """test_namibia_dollar_negative."""
        amount = -100
        namibia_dollar = NamibiaDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert namibia_dollar.numeric_code == '516'
        assert namibia_dollar.alpha_code == 'NAD'
        assert namibia_dollar.decimal_places == 2
        assert namibia_dollar.decimal_sign == '.'
        assert namibia_dollar.grouping_places == 3
        assert namibia_dollar.grouping_sign == ','
        assert not namibia_dollar.international
        assert namibia_dollar.symbol == '$'
        assert namibia_dollar.symbol_ahead
        assert namibia_dollar.symbol_separator == ''
        assert namibia_dollar.localized_symbol == 'NA$'
        assert namibia_dollar.convertion == ''
        assert namibia_dollar.__hash__() == hash(
            (namibia_dollar.__class__, decimal, 'NAD', '516'))
        assert namibia_dollar.__repr__() == (
            'NamibiaDollar(amount: -100, '
            'alpha_code: "NAD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NA$", '
            'numeric_code: "516", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert namibia_dollar.__str__() == '$-100.00'

    def test_namibia_dollar_custom(self):
        """test_namibia_dollar_custom."""
        amount = 1000
        namibia_dollar = NamibiaDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert namibia_dollar.amount == decimal
        assert namibia_dollar.numeric_code == '516'
        assert namibia_dollar.alpha_code == 'NAD'
        assert namibia_dollar.decimal_places == 5
        assert namibia_dollar.decimal_sign == ','
        assert namibia_dollar.grouping_places == 2
        assert namibia_dollar.grouping_sign == '.'
        assert namibia_dollar.international
        assert namibia_dollar.symbol == '$'
        assert not namibia_dollar.symbol_ahead
        assert namibia_dollar.symbol_separator == '_'
        assert namibia_dollar.localized_symbol == 'NA$'
        assert namibia_dollar.convertion == ''
        assert namibia_dollar.__hash__() == hash(
            (namibia_dollar.__class__, decimal, 'NAD', '516'))
        assert namibia_dollar.__repr__() == (
            'NamibiaDollar(amount: 1000, '
            'alpha_code: "NAD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NA$", '
            'numeric_code: "516", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert namibia_dollar.__str__() == 'NAD 10,00.00000'

    def test_namibia_dollar_changed(self):
        """test_cnamibia_dollar_changed."""
        namibia_dollar = NamibiaDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            namibia_dollar.international = True

    def test_namibia_dollar_math_add(self):
        """test_namibia_dollar_math_add."""
        namibia_dollar_one = NamibiaDollar(amount=1)
        namibia_dollar_two = NamibiaDollar(amount=2)
        namibia_dollar_three = NamibiaDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NAD and OTHER.'):
            _ = namibia_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NamibiaDollar\'> '
                    'and <class \'str\'>.')):
            _ = namibia_dollar_one.__add__('1.00')
        assert (
            namibia_dollar_one +
            namibia_dollar_two) == namibia_dollar_three

    def test_namibia_dollar_slots(self):
        """test_namibia_dollar_slots."""
        namibia_dollar = NamibiaDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NamibiaDollar\' '
                    'object has no attribute \'new_variable\'')):
            namibia_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Zealand Dollar representation."""

from multicurrency import NewZealandDollar


class TestNewZealandDollar:
    """NewZealandDollar currency tests."""

    def test_new_zealand_dollar(self):
        """test_new_zealand_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_zealand_dollar = NewZealandDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar.amount == decimal
        assert new_zealand_dollar.numeric_code == '554'
        assert new_zealand_dollar.alpha_code == 'NZD'
        assert new_zealand_dollar.decimal_places == 2
        assert new_zealand_dollar.decimal_sign == '.'
        assert new_zealand_dollar.grouping_places == 3
        assert new_zealand_dollar.grouping_sign == ','
        assert not new_zealand_dollar.international
        assert new_zealand_dollar.symbol == '$'
        assert new_zealand_dollar.symbol_ahead
        assert new_zealand_dollar.symbol_separator == ''
        assert new_zealand_dollar.localized_symbol == '$'
        assert new_zealand_dollar.convertion == ''
        assert new_zealand_dollar.__hash__() == hash(
            (new_zealand_dollar.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar.__repr__() == (
            'NewZealandDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar.__str__() == '$0.14'

    def test_new_zealand_dollar_negative(self):
        """test_new_zealand_dollar_negative."""
        amount = -100
        new_zealand_dollar = NewZealandDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar.numeric_code == '554'
        assert new_zealand_dollar.alpha_code == 'NZD'
        assert new_zealand_dollar.decimal_places == 2
        assert new_zealand_dollar.decimal_sign == '.'
        assert new_zealand_dollar.grouping_places == 3
        assert new_zealand_dollar.grouping_sign == ','
        assert not new_zealand_dollar.international
        assert new_zealand_dollar.symbol == '$'
        assert new_zealand_dollar.symbol_ahead
        assert new_zealand_dollar.symbol_separator == ''
        assert new_zealand_dollar.localized_symbol == '$'
        assert new_zealand_dollar.convertion == ''
        assert new_zealand_dollar.__hash__() == hash(
            (new_zealand_dollar.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar.__repr__() == (
            'NewZealandDollar(amount: -100, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar.__str__() == '$-100.00'

    def test_new_zealand_dollar_custom(self):
        """test_new_zealand_dollar_custom."""
        amount = 1000
        new_zealand_dollar = NewZealandDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar.amount == decimal
        assert new_zealand_dollar.numeric_code == '554'
        assert new_zealand_dollar.alpha_code == 'NZD'
        assert new_zealand_dollar.decimal_places == 5
        assert new_zealand_dollar.decimal_sign == ','
        assert new_zealand_dollar.grouping_places == 2
        assert new_zealand_dollar.grouping_sign == '.'
        assert new_zealand_dollar.international
        assert new_zealand_dollar.symbol == '$'
        assert not new_zealand_dollar.symbol_ahead
        assert new_zealand_dollar.symbol_separator == '_'
        assert new_zealand_dollar.localized_symbol == '$'
        assert new_zealand_dollar.convertion == ''
        assert new_zealand_dollar.__hash__() == hash(
            (new_zealand_dollar.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar.__repr__() == (
            'NewZealandDollar(amount: 1000, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "$", '
            'numeric_code: "554", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_zealand_dollar.__str__() == 'NZD 10,00.00000'

    def test_new_zealand_dollar_changed(self):
        """test_cnew_zealand_dollar_changed."""
        new_zealand_dollar = NewZealandDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar.international = True

    def test_new_zealand_dollar_math_add(self):
        """test_new_zealand_dollar_math_add."""
        new_zealand_dollar_one = NewZealandDollar(amount=1)
        new_zealand_dollar_two = NewZealandDollar(amount=2)
        new_zealand_dollar_three = NewZealandDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NZD and OTHER.'):
            _ = new_zealand_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NewZealandDollar\'> '
                    'and <class \'str\'>.')):
            _ = new_zealand_dollar_one.__add__('1.00')
        assert (
            new_zealand_dollar_one +
            new_zealand_dollar_two) == new_zealand_dollar_three

    def test_new_zealand_dollar_slots(self):
        """test_new_zealand_dollar_slots."""
        new_zealand_dollar = NewZealandDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewZealandDollar\' '
                    'object has no attribute \'new_variable\'')):
            new_zealand_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Zealand Dollar CK representation."""

from multicurrency import NewZealandDollarCK


class TestNewZealandDollarCK:
    """NewZealandDollarCK currency tests."""

    def test_new_zealand_dollar_ck(self):
        """test_new_zealand_dollar_ck."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_zealand_dollar_ck = NewZealandDollarCK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_ck.amount == decimal
        assert new_zealand_dollar_ck.numeric_code == '554'
        assert new_zealand_dollar_ck.alpha_code == 'NZD'
        assert new_zealand_dollar_ck.decimal_places == 2
        assert new_zealand_dollar_ck.decimal_sign == '.'
        assert new_zealand_dollar_ck.grouping_places == 3
        assert new_zealand_dollar_ck.grouping_sign == ','
        assert not new_zealand_dollar_ck.international
        assert new_zealand_dollar_ck.symbol == '$'
        assert new_zealand_dollar_ck.symbol_ahead
        assert new_zealand_dollar_ck.symbol_separator == ''
        assert new_zealand_dollar_ck.localized_symbol == 'CK$'
        assert new_zealand_dollar_ck.convertion == ''
        assert new_zealand_dollar_ck.__hash__() == hash(
            (new_zealand_dollar_ck.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_ck.__repr__() == (
            'NewZealandDollarCK(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CK$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_ck.__str__() == '$0.14'

    def test_new_zealand_dollar_ck_negative(self):
        """test_new_zealand_dollar_ck_negative."""
        amount = -100
        new_zealand_dollar_ck = NewZealandDollarCK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_ck.numeric_code == '554'
        assert new_zealand_dollar_ck.alpha_code == 'NZD'
        assert new_zealand_dollar_ck.decimal_places == 2
        assert new_zealand_dollar_ck.decimal_sign == '.'
        assert new_zealand_dollar_ck.grouping_places == 3
        assert new_zealand_dollar_ck.grouping_sign == ','
        assert not new_zealand_dollar_ck.international
        assert new_zealand_dollar_ck.symbol == '$'
        assert new_zealand_dollar_ck.symbol_ahead
        assert new_zealand_dollar_ck.symbol_separator == ''
        assert new_zealand_dollar_ck.localized_symbol == 'CK$'
        assert new_zealand_dollar_ck.convertion == ''
        assert new_zealand_dollar_ck.__hash__() == hash(
            (new_zealand_dollar_ck.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_ck.__repr__() == (
            'NewZealandDollarCK(amount: -100, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CK$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_ck.__str__() == '$-100.00'

    def test_new_zealand_dollar_ck_custom(self):
        """test_new_zealand_dollar_ck_custom."""
        amount = 1000
        new_zealand_dollar_ck = NewZealandDollarCK(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_ck.amount == decimal
        assert new_zealand_dollar_ck.numeric_code == '554'
        assert new_zealand_dollar_ck.alpha_code == 'NZD'
        assert new_zealand_dollar_ck.decimal_places == 5
        assert new_zealand_dollar_ck.decimal_sign == ','
        assert new_zealand_dollar_ck.grouping_places == 2
        assert new_zealand_dollar_ck.grouping_sign == '.'
        assert new_zealand_dollar_ck.international
        assert new_zealand_dollar_ck.symbol == '$'
        assert not new_zealand_dollar_ck.symbol_ahead
        assert new_zealand_dollar_ck.symbol_separator == '_'
        assert new_zealand_dollar_ck.localized_symbol == 'CK$'
        assert new_zealand_dollar_ck.convertion == ''
        assert new_zealand_dollar_ck.__hash__() == hash(
            (new_zealand_dollar_ck.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_ck.__repr__() == (
            'NewZealandDollarCK(amount: 1000, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CK$", '
            'numeric_code: "554", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_zealand_dollar_ck.__str__() == 'NZD 10,00.00000'

    def test_new_zealand_dollar_ck_changed(self):
        """test_cnew_zealand_dollar_ck_changed."""
        new_zealand_dollar_ck = NewZealandDollarCK(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_ck.international = True

    def test_new_zealand_dollar_ck_math_add(self):
        """test_new_zealand_dollar_ck_math_add."""
        new_zealand_dollar_ck_one = NewZealandDollarCK(amount=1)
        new_zealand_dollar_ck_two = NewZealandDollarCK(amount=2)
        new_zealand_dollar_ck_three = NewZealandDollarCK(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NZD and OTHER.'):
            _ = new_zealand_dollar_ck_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NewZealandDollarCK\'> '
                    'and <class \'str\'>.')):
            _ = new_zealand_dollar_ck_one.__add__('1.00')
        assert (
            new_zealand_dollar_ck_one +
            new_zealand_dollar_ck_two) == new_zealand_dollar_ck_three

    def test_new_zealand_dollar_ck_slots(self):
        """test_new_zealand_dollar_ck_slots."""
        new_zealand_dollar_ck = NewZealandDollarCK(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewZealandDollarCK\' '
                    'object has no attribute \'new_variable\'')):
            new_zealand_dollar_ck.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Zealand Dollar NZ representation."""

from multicurrency import NewZealandDollarNZ


class TestNewZealandDollarNZ:
    """NewZealandDollarNZ currency tests."""

    def test_new_zealand_dollar_nz(self):
        """test_new_zealand_dollar_nz."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_zealand_dollar_nz = NewZealandDollarNZ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nz.amount == decimal
        assert new_zealand_dollar_nz.numeric_code == '554'
        assert new_zealand_dollar_nz.alpha_code == 'NZD'
        assert new_zealand_dollar_nz.decimal_places == 2
        assert new_zealand_dollar_nz.decimal_sign == '.'
        assert new_zealand_dollar_nz.grouping_places == 3
        assert new_zealand_dollar_nz.grouping_sign == ','
        assert not new_zealand_dollar_nz.international
        assert new_zealand_dollar_nz.symbol == '$'
        assert new_zealand_dollar_nz.symbol_ahead
        assert new_zealand_dollar_nz.symbol_separator == ''
        assert new_zealand_dollar_nz.localized_symbol == 'NZ$'
        assert new_zealand_dollar_nz.convertion == ''
        assert new_zealand_dollar_nz.__hash__() == hash(
            (new_zealand_dollar_nz.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nz.__repr__() == (
            'NewZealandDollarNZ(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NZ$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_nz.__str__() == '$0.14'

    def test_new_zealand_dollar_nz_negative(self):
        """test_new_zealand_dollar_nz_negative."""
        amount = -100
        new_zealand_dollar_nz = NewZealandDollarNZ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nz.numeric_code == '554'
        assert new_zealand_dollar_nz.alpha_code == 'NZD'
        assert new_zealand_dollar_nz.decimal_places == 2
        assert new_zealand_dollar_nz.decimal_sign == '.'
        assert new_zealand_dollar_nz.grouping_places == 3
        assert new_zealand_dollar_nz.grouping_sign == ','
        assert not new_zealand_dollar_nz.international
        assert new_zealand_dollar_nz.symbol == '$'
        assert new_zealand_dollar_nz.symbol_ahead
        assert new_zealand_dollar_nz.symbol_separator == ''
        assert new_zealand_dollar_nz.localized_symbol == 'NZ$'
        assert new_zealand_dollar_nz.convertion == ''
        assert new_zealand_dollar_nz.__hash__() == hash(
            (new_zealand_dollar_nz.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nz.__repr__() == (
            'NewZealandDollarNZ(amount: -100, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NZ$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_nz.__str__() == '$-100.00'

    def test_new_zealand_dollar_nz_custom(self):
        """test_new_zealand_dollar_nz_custom."""
        amount = 1000
        new_zealand_dollar_nz = NewZealandDollarNZ(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nz.amount == decimal
        assert new_zealand_dollar_nz.numeric_code == '554'
        assert new_zealand_dollar_nz.alpha_code == 'NZD'
        assert new_zealand_dollar_nz.decimal_places == 5
        assert new_zealand_dollar_nz.decimal_sign == ','
        assert new_zealand_dollar_nz.grouping_places == 2
        assert new_zealand_dollar_nz.grouping_sign == '.'
        assert new_zealand_dollar_nz.international
        assert new_zealand_dollar_nz.symbol == '$'
        assert not new_zealand_dollar_nz.symbol_ahead
        assert new_zealand_dollar_nz.symbol_separator == '_'
        assert new_zealand_dollar_nz.localized_symbol == 'NZ$'
        assert new_zealand_dollar_nz.convertion == ''
        assert new_zealand_dollar_nz.__hash__() == hash(
            (new_zealand_dollar_nz.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nz.__repr__() == (
            'NewZealandDollarNZ(amount: 1000, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NZ$", '
            'numeric_code: "554", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_zealand_dollar_nz.__str__() == 'NZD 10,00.00000'

    def test_new_zealand_dollar_nz_changed(self):
        """test_cnew_zealand_dollar_nz_changed."""
        new_zealand_dollar_nz = NewZealandDollarNZ(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nz.international = True

    def test_new_zealand_dollar_nz_math_add(self):
        """test_new_zealand_dollar_nz_math_add."""
        new_zealand_dollar_nz_one = NewZealandDollarNZ(amount=1)
        new_zealand_dollar_nz_two = NewZealandDollarNZ(amount=2)
        new_zealand_dollar_nz_three = NewZealandDollarNZ(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NZD and OTHER.'):
            _ = new_zealand_dollar_nz_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NewZealandDollarNZ\'> '
                    'and <class \'str\'>.')):
            _ = new_zealand_dollar_nz_one.__add__('1.00')
        assert (
            new_zealand_dollar_nz_one +
            new_zealand_dollar_nz_two) == new_zealand_dollar_nz_three

    def test_new_zealand_dollar_nz_slots(self):
        """test_new_zealand_dollar_nz_slots."""
        new_zealand_dollar_nz = NewZealandDollarNZ(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewZealandDollarNZ\' '
                    'object has no attribute \'new_variable\'')):
            new_zealand_dollar_nz.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Zealand Dollar NU representation."""

from multicurrency import NewZealandDollarNU


class TestNewZealandDollarNU:
    """NewZealandDollarNU currency tests."""

    def test_new_zealand_dollar_nu(self):
        """test_new_zealand_dollar_nu."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_zealand_dollar_nu = NewZealandDollarNU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nu.amount == decimal
        assert new_zealand_dollar_nu.numeric_code == '554'
        assert new_zealand_dollar_nu.alpha_code == 'NZD'
        assert new_zealand_dollar_nu.decimal_places == 2
        assert new_zealand_dollar_nu.decimal_sign == '.'
        assert new_zealand_dollar_nu.grouping_places == 3
        assert new_zealand_dollar_nu.grouping_sign == ','
        assert not new_zealand_dollar_nu.international
        assert new_zealand_dollar_nu.symbol == '$'
        assert new_zealand_dollar_nu.symbol_ahead
        assert new_zealand_dollar_nu.symbol_separator == ''
        assert new_zealand_dollar_nu.localized_symbol == 'NU$'
        assert new_zealand_dollar_nu.convertion == ''
        assert new_zealand_dollar_nu.__hash__() == hash(
            (new_zealand_dollar_nu.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nu.__repr__() == (
            'NewZealandDollarNU(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NU$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_nu.__str__() == '$0.14'

    def test_new_zealand_dollar_nu_negative(self):
        """test_new_zealand_dollar_nu_negative."""
        amount = -100
        new_zealand_dollar_nu = NewZealandDollarNU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nu.numeric_code == '554'
        assert new_zealand_dollar_nu.alpha_code == 'NZD'
        assert new_zealand_dollar_nu.decimal_places == 2
        assert new_zealand_dollar_nu.decimal_sign == '.'
        assert new_zealand_dollar_nu.grouping_places == 3
        assert new_zealand_dollar_nu.grouping_sign == ','
        assert not new_zealand_dollar_nu.international
        assert new_zealand_dollar_nu.symbol == '$'
        assert new_zealand_dollar_nu.symbol_ahead
        assert new_zealand_dollar_nu.symbol_separator == ''
        assert new_zealand_dollar_nu.localized_symbol == 'NU$'
        assert new_zealand_dollar_nu.convertion == ''
        assert new_zealand_dollar_nu.__hash__() == hash(
            (new_zealand_dollar_nu.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nu.__repr__() == (
            'NewZealandDollarNU(amount: -100, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "NU$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_nu.__str__() == '$-100.00'

    def test_new_zealand_dollar_nu_custom(self):
        """test_new_zealand_dollar_nu_custom."""
        amount = 1000
        new_zealand_dollar_nu = NewZealandDollarNU(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_nu.amount == decimal
        assert new_zealand_dollar_nu.numeric_code == '554'
        assert new_zealand_dollar_nu.alpha_code == 'NZD'
        assert new_zealand_dollar_nu.decimal_places == 5
        assert new_zealand_dollar_nu.decimal_sign == ','
        assert new_zealand_dollar_nu.grouping_places == 2
        assert new_zealand_dollar_nu.grouping_sign == '.'
        assert new_zealand_dollar_nu.international
        assert new_zealand_dollar_nu.symbol == '$'
        assert not new_zealand_dollar_nu.symbol_ahead
        assert new_zealand_dollar_nu.symbol_separator == '_'
        assert new_zealand_dollar_nu.localized_symbol == 'NU$'
        assert new_zealand_dollar_nu.convertion == ''
        assert new_zealand_dollar_nu.__hash__() == hash(
            (new_zealand_dollar_nu.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_nu.__repr__() == (
            'NewZealandDollarNU(amount: 1000, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NU$", '
            'numeric_code: "554", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_zealand_dollar_nu.__str__() == 'NZD 10,00.00000'

    def test_new_zealand_dollar_nu_changed(self):
        """test_cnew_zealand_dollar_nu_changed."""
        new_zealand_dollar_nu = NewZealandDollarNU(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_nu.international = True

    def test_new_zealand_dollar_nu_math_add(self):
        """test_new_zealand_dollar_nu_math_add."""
        new_zealand_dollar_nu_one = NewZealandDollarNU(amount=1)
        new_zealand_dollar_nu_two = NewZealandDollarNU(amount=2)
        new_zealand_dollar_nu_three = NewZealandDollarNU(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NZD and OTHER.'):
            _ = new_zealand_dollar_nu_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NewZealandDollarNU\'> '
                    'and <class \'str\'>.')):
            _ = new_zealand_dollar_nu_one.__add__('1.00')
        assert (
            new_zealand_dollar_nu_one +
            new_zealand_dollar_nu_two) == new_zealand_dollar_nu_three

    def test_new_zealand_dollar_nu_slots(self):
        """test_new_zealand_dollar_nu_slots."""
        new_zealand_dollar_nu = NewZealandDollarNU(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewZealandDollarNU\' '
                    'object has no attribute \'new_variable\'')):
            new_zealand_dollar_nu.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Zealand Dollar PN representation."""

from multicurrency import NewZealandDollarPN


class TestNewZealandDollarPN:
    """NewZealandDollarPN currency tests."""

    def test_new_zealand_dollar_pn(self):
        """test_new_zealand_dollar_pn."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_zealand_dollar_pn = NewZealandDollarPN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_pn.amount == decimal
        assert new_zealand_dollar_pn.numeric_code == '554'
        assert new_zealand_dollar_pn.alpha_code == 'NZD'
        assert new_zealand_dollar_pn.decimal_places == 2
        assert new_zealand_dollar_pn.decimal_sign == '.'
        assert new_zealand_dollar_pn.grouping_places == 3
        assert new_zealand_dollar_pn.grouping_sign == ','
        assert not new_zealand_dollar_pn.international
        assert new_zealand_dollar_pn.symbol == '$'
        assert new_zealand_dollar_pn.symbol_ahead
        assert new_zealand_dollar_pn.symbol_separator == ''
        assert new_zealand_dollar_pn.localized_symbol == 'PN$'
        assert new_zealand_dollar_pn.convertion == ''
        assert new_zealand_dollar_pn.__hash__() == hash(
            (new_zealand_dollar_pn.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_pn.__repr__() == (
            'NewZealandDollarPN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PN$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_pn.__str__() == '$0.14'

    def test_new_zealand_dollar_pn_negative(self):
        """test_new_zealand_dollar_pn_negative."""
        amount = -100
        new_zealand_dollar_pn = NewZealandDollarPN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_pn.numeric_code == '554'
        assert new_zealand_dollar_pn.alpha_code == 'NZD'
        assert new_zealand_dollar_pn.decimal_places == 2
        assert new_zealand_dollar_pn.decimal_sign == '.'
        assert new_zealand_dollar_pn.grouping_places == 3
        assert new_zealand_dollar_pn.grouping_sign == ','
        assert not new_zealand_dollar_pn.international
        assert new_zealand_dollar_pn.symbol == '$'
        assert new_zealand_dollar_pn.symbol_ahead
        assert new_zealand_dollar_pn.symbol_separator == ''
        assert new_zealand_dollar_pn.localized_symbol == 'PN$'
        assert new_zealand_dollar_pn.convertion == ''
        assert new_zealand_dollar_pn.__hash__() == hash(
            (new_zealand_dollar_pn.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_pn.__repr__() == (
            'NewZealandDollarPN(amount: -100, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PN$", '
            'numeric_code: "554", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_zealand_dollar_pn.__str__() == '$-100.00'

    def test_new_zealand_dollar_pn_custom(self):
        """test_new_zealand_dollar_pn_custom."""
        amount = 1000
        new_zealand_dollar_pn = NewZealandDollarPN(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_zealand_dollar_pn.amount == decimal
        assert new_zealand_dollar_pn.numeric_code == '554'
        assert new_zealand_dollar_pn.alpha_code == 'NZD'
        assert new_zealand_dollar_pn.decimal_places == 5
        assert new_zealand_dollar_pn.decimal_sign == ','
        assert new_zealand_dollar_pn.grouping_places == 2
        assert new_zealand_dollar_pn.grouping_sign == '.'
        assert new_zealand_dollar_pn.international
        assert new_zealand_dollar_pn.symbol == '$'
        assert not new_zealand_dollar_pn.symbol_ahead
        assert new_zealand_dollar_pn.symbol_separator == '_'
        assert new_zealand_dollar_pn.localized_symbol == 'PN$'
        assert new_zealand_dollar_pn.convertion == ''
        assert new_zealand_dollar_pn.__hash__() == hash(
            (new_zealand_dollar_pn.__class__, decimal, 'NZD', '554'))
        assert new_zealand_dollar_pn.__repr__() == (
            'NewZealandDollarPN(amount: 1000, '
            'alpha_code: "NZD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PN$", '
            'numeric_code: "554", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_zealand_dollar_pn.__str__() == 'NZD 10,00.00000'

    def test_new_zealand_dollar_pn_changed(self):
        """test_cnew_zealand_dollar_pn_changed."""
        new_zealand_dollar_pn = NewZealandDollarPN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_zealand_dollar_pn.international = True

    def test_new_zealand_dollar_pn_math_add(self):
        """test_new_zealand_dollar_pn_math_add."""
        new_zealand_dollar_pn_one = NewZealandDollarPN(amount=1)
        new_zealand_dollar_pn_two = NewZealandDollarPN(amount=2)
        new_zealand_dollar_pn_three = NewZealandDollarPN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NZD and OTHER.'):
            _ = new_zealand_dollar_pn_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.NewZealandDollarPN\'> '
                    'and <class \'str\'>.')):
            _ = new_zealand_dollar_pn_one.__add__('1.00')
        assert (
            new_zealand_dollar_pn_one +
            new_zealand_dollar_pn_two) == new_zealand_dollar_pn_three

    def test_new_zealand_dollar_pn_slots(self):
        """test_new_zealand_dollar_pn_slots."""
        new_zealand_dollar_pn = NewZealandDollarPN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewZealandDollarPN\' '
                    'object has no attribute \'new_variable\'')):
            new_zealand_dollar_pn.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Solomon Islands Dollar representation."""

from multicurrency import SolomonIslandsDollar


class TestSolomonIslandsDollar:
    """SolomonIslandsDollar currency tests."""

    def test_solomon_islands_dollar(self):
        """test_solomon_islands_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        solomon_islands_dollar = SolomonIslandsDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert solomon_islands_dollar.amount == decimal
        assert solomon_islands_dollar.numeric_code == '090'
        assert solomon_islands_dollar.alpha_code == 'SBD'
        assert solomon_islands_dollar.decimal_places == 2
        assert solomon_islands_dollar.decimal_sign == '.'
        assert solomon_islands_dollar.grouping_places == 3
        assert solomon_islands_dollar.grouping_sign == ','
        assert not solomon_islands_dollar.international
        assert solomon_islands_dollar.symbol == '$'
        assert solomon_islands_dollar.symbol_ahead
        assert solomon_islands_dollar.symbol_separator == ''
        assert solomon_islands_dollar.localized_symbol == 'SB$'
        assert solomon_islands_dollar.convertion == ''
        assert solomon_islands_dollar.__hash__() == hash(
            (solomon_islands_dollar.__class__, decimal, 'SBD', '090'))
        assert solomon_islands_dollar.__repr__() == (
            'SolomonIslandsDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SBD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SB$", '
            'numeric_code: "090", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert solomon_islands_dollar.__str__() == '$0.14'

    def test_solomon_islands_dollar_negative(self):
        """test_solomon_islands_dollar_negative."""
        amount = -100
        solomon_islands_dollar = SolomonIslandsDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert solomon_islands_dollar.numeric_code == '090'
        assert solomon_islands_dollar.alpha_code == 'SBD'
        assert solomon_islands_dollar.decimal_places == 2
        assert solomon_islands_dollar.decimal_sign == '.'
        assert solomon_islands_dollar.grouping_places == 3
        assert solomon_islands_dollar.grouping_sign == ','
        assert not solomon_islands_dollar.international
        assert solomon_islands_dollar.symbol == '$'
        assert solomon_islands_dollar.symbol_ahead
        assert solomon_islands_dollar.symbol_separator == ''
        assert solomon_islands_dollar.localized_symbol == 'SB$'
        assert solomon_islands_dollar.convertion == ''
        assert solomon_islands_dollar.__hash__() == hash(
            (solomon_islands_dollar.__class__, decimal, 'SBD', '090'))
        assert solomon_islands_dollar.__repr__() == (
            'SolomonIslandsDollar(amount: -100, '
            'alpha_code: "SBD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SB$", '
            'numeric_code: "090", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert solomon_islands_dollar.__str__() == '$-100.00'

    def test_solomon_islands_dollar_custom(self):
        """test_solomon_islands_dollar_custom."""
        amount = 1000
        solomon_islands_dollar = SolomonIslandsDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert solomon_islands_dollar.amount == decimal
        assert solomon_islands_dollar.numeric_code == '090'
        assert solomon_islands_dollar.alpha_code == 'SBD'
        assert solomon_islands_dollar.decimal_places == 5
        assert solomon_islands_dollar.decimal_sign == ','
        assert solomon_islands_dollar.grouping_places == 2
        assert solomon_islands_dollar.grouping_sign == '.'
        assert solomon_islands_dollar.international
        assert solomon_islands_dollar.symbol == '$'
        assert not solomon_islands_dollar.symbol_ahead
        assert solomon_islands_dollar.symbol_separator == '_'
        assert solomon_islands_dollar.localized_symbol == 'SB$'
        assert solomon_islands_dollar.convertion == ''
        assert solomon_islands_dollar.__hash__() == hash(
            (solomon_islands_dollar.__class__, decimal, 'SBD', '090'))
        assert solomon_islands_dollar.__repr__() == (
            'SolomonIslandsDollar(amount: 1000, '
            'alpha_code: "SBD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SB$", '
            'numeric_code: "090", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert solomon_islands_dollar.__str__() == 'SBD 10,00.00000'

    def test_solomon_islands_dollar_changed(self):
        """test_csolomon_islands_dollar_changed."""
        solomon_islands_dollar = SolomonIslandsDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            solomon_islands_dollar.international = True

    def test_solomon_islands_dollar_math_add(self):
        """test_solomon_islands_dollar_math_add."""
        solomon_islands_dollar_one = SolomonIslandsDollar(amount=1)
        solomon_islands_dollar_two = SolomonIslandsDollar(amount=2)
        solomon_islands_dollar_three = SolomonIslandsDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SBD and OTHER.'):
            _ = solomon_islands_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.SolomonIslandsDollar\'> '
                    'and <class \'str\'>.')):
            _ = solomon_islands_dollar_one.__add__('1.00')
        assert (
            solomon_islands_dollar_one +
            solomon_islands_dollar_two) == solomon_islands_dollar_three

    def test_solomon_islands_dollar_slots(self):
        """test_solomon_islands_dollar_slots."""
        solomon_islands_dollar = SolomonIslandsDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SolomonIslandsDollar\' '
                    'object has no attribute \'new_variable\'')):
            solomon_islands_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Singapore Dollar representation."""

from multicurrency import SingaporeDollar


class TestSingaporeDollar:
    """SingaporeDollar currency tests."""

    def test_singapore_dollar(self):
        """test_singapore_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        singapore_dollar = SingaporeDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar.amount == decimal
        assert singapore_dollar.numeric_code == '702'
        assert singapore_dollar.alpha_code == 'SGD'
        assert singapore_dollar.decimal_places == 2
        assert singapore_dollar.decimal_sign == '.'
        assert singapore_dollar.grouping_places == 3
        assert singapore_dollar.grouping_sign == ','
        assert not singapore_dollar.international
        assert singapore_dollar.symbol == '$'
        assert singapore_dollar.symbol_ahead
        assert singapore_dollar.symbol_separator == ''
        assert singapore_dollar.localized_symbol == '$'
        assert singapore_dollar.convertion == ''
        assert singapore_dollar.__hash__() == hash(
            (singapore_dollar.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar.__repr__() == (
            'SingaporeDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar.__str__() == '$0.14'

    def test_singapore_dollar_negative(self):
        """test_singapore_dollar_negative."""
        amount = -100
        singapore_dollar = SingaporeDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar.numeric_code == '702'
        assert singapore_dollar.alpha_code == 'SGD'
        assert singapore_dollar.decimal_places == 2
        assert singapore_dollar.decimal_sign == '.'
        assert singapore_dollar.grouping_places == 3
        assert singapore_dollar.grouping_sign == ','
        assert not singapore_dollar.international
        assert singapore_dollar.symbol == '$'
        assert singapore_dollar.symbol_ahead
        assert singapore_dollar.symbol_separator == ''
        assert singapore_dollar.localized_symbol == '$'
        assert singapore_dollar.convertion == ''
        assert singapore_dollar.__hash__() == hash(
            (singapore_dollar.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar.__repr__() == (
            'SingaporeDollar(amount: -100, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar.__str__() == '$-100.00'

    def test_singapore_dollar_custom(self):
        """test_singapore_dollar_custom."""
        amount = 1000
        singapore_dollar = SingaporeDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar.amount == decimal
        assert singapore_dollar.numeric_code == '702'
        assert singapore_dollar.alpha_code == 'SGD'
        assert singapore_dollar.decimal_places == 5
        assert singapore_dollar.decimal_sign == ','
        assert singapore_dollar.grouping_places == 2
        assert singapore_dollar.grouping_sign == '.'
        assert singapore_dollar.international
        assert singapore_dollar.symbol == '$'
        assert not singapore_dollar.symbol_ahead
        assert singapore_dollar.symbol_separator == '_'
        assert singapore_dollar.localized_symbol == '$'
        assert singapore_dollar.convertion == ''
        assert singapore_dollar.__hash__() == hash(
            (singapore_dollar.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar.__repr__() == (
            'SingaporeDollar(amount: 1000, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "$", '
            'numeric_code: "702", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert singapore_dollar.__str__() == 'SGD 10,00.00000'

    def test_singapore_dollar_changed(self):
        """test_csingapore_dollar_changed."""
        singapore_dollar = SingaporeDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar.international = True

    def test_singapore_dollar_math_add(self):
        """test_singapore_dollar_math_add."""
        singapore_dollar_one = SingaporeDollar(amount=1)
        singapore_dollar_two = SingaporeDollar(amount=2)
        singapore_dollar_three = SingaporeDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SGD and OTHER.'):
            _ = singapore_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.SingaporeDollar\'> '
                    'and <class \'str\'>.')):
            _ = singapore_dollar_one.__add__('1.00')
        assert (
            singapore_dollar_one +
            singapore_dollar_two) == singapore_dollar_three

    def test_singapore_dollar_slots(self):
        """test_singapore_dollar_slots."""
        singapore_dollar = SingaporeDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SingaporeDollar\' '
                    'object has no attribute \'new_variable\'')):
            singapore_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Singapore Dollar BN representation."""

from multicurrency import SingaporeDollarBN


class TestSingaporeDollarBN:
    """SingaporeDollarBN currency tests."""

    def test_singapore_dollar_bn(self):
        """test_singapore_dollar_bn."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        singapore_dollar_bn = SingaporeDollarBN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_bn.amount == decimal
        assert singapore_dollar_bn.numeric_code == '702'
        assert singapore_dollar_bn.alpha_code == 'SGD'
        assert singapore_dollar_bn.decimal_places == 2
        assert singapore_dollar_bn.decimal_sign == '.'
        assert singapore_dollar_bn.grouping_places == 3
        assert singapore_dollar_bn.grouping_sign == ','
        assert not singapore_dollar_bn.international
        assert singapore_dollar_bn.symbol == '$'
        assert singapore_dollar_bn.symbol_ahead
        assert singapore_dollar_bn.symbol_separator == ''
        assert singapore_dollar_bn.localized_symbol == 'BN$'
        assert singapore_dollar_bn.convertion == ''
        assert singapore_dollar_bn.__hash__() == hash(
            (singapore_dollar_bn.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_bn.__repr__() == (
            'SingaporeDollarBN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BN$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar_bn.__str__() == '$0.14'

    def test_singapore_dollar_bn_negative(self):
        """test_singapore_dollar_bn_negative."""
        amount = -100
        singapore_dollar_bn = SingaporeDollarBN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_bn.numeric_code == '702'
        assert singapore_dollar_bn.alpha_code == 'SGD'
        assert singapore_dollar_bn.decimal_places == 2
        assert singapore_dollar_bn.decimal_sign == '.'
        assert singapore_dollar_bn.grouping_places == 3
        assert singapore_dollar_bn.grouping_sign == ','
        assert not singapore_dollar_bn.international
        assert singapore_dollar_bn.symbol == '$'
        assert singapore_dollar_bn.symbol_ahead
        assert singapore_dollar_bn.symbol_separator == ''
        assert singapore_dollar_bn.localized_symbol == 'BN$'
        assert singapore_dollar_bn.convertion == ''
        assert singapore_dollar_bn.__hash__() == hash(
            (singapore_dollar_bn.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_bn.__repr__() == (
            'SingaporeDollarBN(amount: -100, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BN$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar_bn.__str__() == '$-100.00'

    def test_singapore_dollar_bn_custom(self):
        """test_singapore_dollar_bn_custom."""
        amount = 1000
        singapore_dollar_bn = SingaporeDollarBN(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_bn.amount == decimal
        assert singapore_dollar_bn.numeric_code == '702'
        assert singapore_dollar_bn.alpha_code == 'SGD'
        assert singapore_dollar_bn.decimal_places == 5
        assert singapore_dollar_bn.decimal_sign == ','
        assert singapore_dollar_bn.grouping_places == 2
        assert singapore_dollar_bn.grouping_sign == '.'
        assert singapore_dollar_bn.international
        assert singapore_dollar_bn.symbol == '$'
        assert not singapore_dollar_bn.symbol_ahead
        assert singapore_dollar_bn.symbol_separator == '_'
        assert singapore_dollar_bn.localized_symbol == 'BN$'
        assert singapore_dollar_bn.convertion == ''
        assert singapore_dollar_bn.__hash__() == hash(
            (singapore_dollar_bn.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_bn.__repr__() == (
            'SingaporeDollarBN(amount: 1000, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BN$", '
            'numeric_code: "702", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert singapore_dollar_bn.__str__() == 'SGD 10,00.00000'

    def test_singapore_dollar_bn_changed(self):
        """test_csingapore_dollar_bn_changed."""
        singapore_dollar_bn = SingaporeDollarBN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_bn.international = True

    def test_singapore_dollar_bn_math_add(self):
        """test_singapore_dollar_bn_math_add."""
        singapore_dollar_bn_one = SingaporeDollarBN(amount=1)
        singapore_dollar_bn_two = SingaporeDollarBN(amount=2)
        singapore_dollar_bn_three = SingaporeDollarBN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SGD and OTHER.'):
            _ = singapore_dollar_bn_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.SingaporeDollarBN\'> '
                    'and <class \'str\'>.')):
            _ = singapore_dollar_bn_one.__add__('1.00')
        assert (
            singapore_dollar_bn_one +
            singapore_dollar_bn_two) == singapore_dollar_bn_three

    def test_singapore_dollar_bn_slots(self):
        """test_singapore_dollar_bn_slots."""
        singapore_dollar_bn = SingaporeDollarBN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SingaporeDollarBN\' '
                    'object has no attribute \'new_variable\'')):
            singapore_dollar_bn.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Singapore Dollar SG representation."""

from multicurrency import SingaporeDollarSG


class TestSingaporeDollarSG:
    """SingaporeDollarSG currency tests."""

    def test_singapore_dollar_sg(self):
        """test_singapore_dollar_sg."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        singapore_dollar_sg = SingaporeDollarSG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_sg.amount == decimal
        assert singapore_dollar_sg.numeric_code == '702'
        assert singapore_dollar_sg.alpha_code == 'SGD'
        assert singapore_dollar_sg.decimal_places == 2
        assert singapore_dollar_sg.decimal_sign == '.'
        assert singapore_dollar_sg.grouping_places == 3
        assert singapore_dollar_sg.grouping_sign == ','
        assert not singapore_dollar_sg.international
        assert singapore_dollar_sg.symbol == '$'
        assert singapore_dollar_sg.symbol_ahead
        assert singapore_dollar_sg.symbol_separator == ''
        assert singapore_dollar_sg.localized_symbol == 'SG$'
        assert singapore_dollar_sg.convertion == ''
        assert singapore_dollar_sg.__hash__() == hash(
            (singapore_dollar_sg.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_sg.__repr__() == (
            'SingaporeDollarSG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SG$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar_sg.__str__() == '$0.14'

    def test_singapore_dollar_sg_negative(self):
        """test_singapore_dollar_sg_negative."""
        amount = -100
        singapore_dollar_sg = SingaporeDollarSG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_sg.numeric_code == '702'
        assert singapore_dollar_sg.alpha_code == 'SGD'
        assert singapore_dollar_sg.decimal_places == 2
        assert singapore_dollar_sg.decimal_sign == '.'
        assert singapore_dollar_sg.grouping_places == 3
        assert singapore_dollar_sg.grouping_sign == ','
        assert not singapore_dollar_sg.international
        assert singapore_dollar_sg.symbol == '$'
        assert singapore_dollar_sg.symbol_ahead
        assert singapore_dollar_sg.symbol_separator == ''
        assert singapore_dollar_sg.localized_symbol == 'SG$'
        assert singapore_dollar_sg.convertion == ''
        assert singapore_dollar_sg.__hash__() == hash(
            (singapore_dollar_sg.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_sg.__repr__() == (
            'SingaporeDollarSG(amount: -100, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "SG$", '
            'numeric_code: "702", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert singapore_dollar_sg.__str__() == '$-100.00'

    def test_singapore_dollar_sg_custom(self):
        """test_singapore_dollar_sg_custom."""
        amount = 1000
        singapore_dollar_sg = SingaporeDollarSG(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert singapore_dollar_sg.amount == decimal
        assert singapore_dollar_sg.numeric_code == '702'
        assert singapore_dollar_sg.alpha_code == 'SGD'
        assert singapore_dollar_sg.decimal_places == 5
        assert singapore_dollar_sg.decimal_sign == ','
        assert singapore_dollar_sg.grouping_places == 2
        assert singapore_dollar_sg.grouping_sign == '.'
        assert singapore_dollar_sg.international
        assert singapore_dollar_sg.symbol == '$'
        assert not singapore_dollar_sg.symbol_ahead
        assert singapore_dollar_sg.symbol_separator == '_'
        assert singapore_dollar_sg.localized_symbol == 'SG$'
        assert singapore_dollar_sg.convertion == ''
        assert singapore_dollar_sg.__hash__() == hash(
            (singapore_dollar_sg.__class__, decimal, 'SGD', '702'))
        assert singapore_dollar_sg.__repr__() == (
            'SingaporeDollarSG(amount: 1000, '
            'alpha_code: "SGD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SG$", '
            'numeric_code: "702", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert singapore_dollar_sg.__str__() == 'SGD 10,00.00000'

    def test_singapore_dollar_sg_changed(self):
        """test_csingapore_dollar_sg_changed."""
        singapore_dollar_sg = SingaporeDollarSG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            singapore_dollar_sg.international = True

    def test_singapore_dollar_sg_math_add(self):
        """test_singapore_dollar_sg_math_add."""
        singapore_dollar_sg_one = SingaporeDollarSG(amount=1)
        singapore_dollar_sg_two = SingaporeDollarSG(amount=2)
        singapore_dollar_sg_three = SingaporeDollarSG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SGD and OTHER.'):
            _ = singapore_dollar_sg_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.SingaporeDollarSG\'> '
                    'and <class \'str\'>.')):
            _ = singapore_dollar_sg_one.__add__('1.00')
        assert (
            singapore_dollar_sg_one +
            singapore_dollar_sg_two) == singapore_dollar_sg_three

    def test_singapore_dollar_sg_slots(self):
        """test_singapore_dollar_sg_slots."""
        singapore_dollar_sg = SingaporeDollarSG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SingaporeDollarSG\' '
                    'object has no attribute \'new_variable\'')):
            singapore_dollar_sg.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Suriname Dollar representation."""

from multicurrency import SurinameDollar


class TestSurinameDollar:
    """SurinameDollar currency tests."""

    def test_suriname_dollar(self):
        """test_suriname_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        suriname_dollar = SurinameDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert suriname_dollar.amount == decimal
        assert suriname_dollar.numeric_code == '968'
        assert suriname_dollar.alpha_code == 'SRD'
        assert suriname_dollar.decimal_places == 2
        assert suriname_dollar.decimal_sign == ','
        assert suriname_dollar.grouping_places == 3
        assert suriname_dollar.grouping_sign == '.'
        assert not suriname_dollar.international
        assert suriname_dollar.symbol == '$'
        assert suriname_dollar.symbol_ahead
        assert suriname_dollar.symbol_separator == '\u00A0'
        assert suriname_dollar.localized_symbol == 'SR$'
        assert suriname_dollar.convertion == ''
        assert suriname_dollar.__hash__() == hash(
            (suriname_dollar.__class__, decimal, 'SRD', '968'))
        assert suriname_dollar.__repr__() == (
            'SurinameDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SRD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SR$", '
            'numeric_code: "968", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert suriname_dollar.__str__() == '$ 0,14'

    def test_suriname_dollar_negative(self):
        """test_suriname_dollar_negative."""
        amount = -100
        suriname_dollar = SurinameDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert suriname_dollar.numeric_code == '968'
        assert suriname_dollar.alpha_code == 'SRD'
        assert suriname_dollar.decimal_places == 2
        assert suriname_dollar.decimal_sign == ','
        assert suriname_dollar.grouping_places == 3
        assert suriname_dollar.grouping_sign == '.'
        assert not suriname_dollar.international
        assert suriname_dollar.symbol == '$'
        assert suriname_dollar.symbol_ahead
        assert suriname_dollar.symbol_separator == '\u00A0'
        assert suriname_dollar.localized_symbol == 'SR$'
        assert suriname_dollar.convertion == ''
        assert suriname_dollar.__hash__() == hash(
            (suriname_dollar.__class__, decimal, 'SRD', '968'))
        assert suriname_dollar.__repr__() == (
            'SurinameDollar(amount: -100, '
            'alpha_code: "SRD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SR$", '
            'numeric_code: "968", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert suriname_dollar.__str__() == '$ -100,00'

    def test_suriname_dollar_custom(self):
        """test_suriname_dollar_custom."""
        amount = 1000
        suriname_dollar = SurinameDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert suriname_dollar.amount == decimal
        assert suriname_dollar.numeric_code == '968'
        assert suriname_dollar.alpha_code == 'SRD'
        assert suriname_dollar.decimal_places == 5
        assert suriname_dollar.decimal_sign == '.'
        assert suriname_dollar.grouping_places == 2
        assert suriname_dollar.grouping_sign == ','
        assert suriname_dollar.international
        assert suriname_dollar.symbol == '$'
        assert not suriname_dollar.symbol_ahead
        assert suriname_dollar.symbol_separator == '_'
        assert suriname_dollar.localized_symbol == 'SR$'
        assert suriname_dollar.convertion == ''
        assert suriname_dollar.__hash__() == hash(
            (suriname_dollar.__class__, decimal, 'SRD', '968'))
        assert suriname_dollar.__repr__() == (
            'SurinameDollar(amount: 1000, '
            'alpha_code: "SRD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SR$", '
            'numeric_code: "968", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert suriname_dollar.__str__() == 'SRD 10,00.00000'

    def test_suriname_dollar_changed(self):
        """test_csuriname_dollar_changed."""
        suriname_dollar = SurinameDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            suriname_dollar.international = True

    def test_suriname_dollar_math_add(self):
        """test_suriname_dollar_math_add."""
        suriname_dollar_one = SurinameDollar(amount=1)
        suriname_dollar_two = SurinameDollar(amount=2)
        suriname_dollar_three = SurinameDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SRD and OTHER.'):
            _ = suriname_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.SurinameDollar\'> '
                    'and <class \'str\'>.')):
            _ = suriname_dollar_one.__add__('1.00')
        assert (
            suriname_dollar_one +
            suriname_dollar_two) == suriname_dollar_three

    def test_suriname_dollar_slots(self):
        """test_suriname_dollar_slots."""
        suriname_dollar = SurinameDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SurinameDollar\' '
                    'object has no attribute \'new_variable\'')):
            suriname_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Trinidad and Tobago Dollar representation."""

from multicurrency import TrinidadandTobagoDollar


class TestTrinidadandTobagoDollar:
    """TrinidadandTobagoDollar currency tests."""

    def test_trinidad_and_tobago_dollar(self):
        """test_trinidad_and_tobago_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert trinidad_and_tobago_dollar.amount == decimal
        assert trinidad_and_tobago_dollar.numeric_code == '780'
        assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
        assert trinidad_and_tobago_dollar.decimal_places == 2
        assert trinidad_and_tobago_dollar.decimal_sign == '.'
        assert trinidad_and_tobago_dollar.grouping_places == 3
        assert trinidad_and_tobago_dollar.grouping_sign == ','
        assert not trinidad_and_tobago_dollar.international
        assert trinidad_and_tobago_dollar.symbol == '$'
        assert trinidad_and_tobago_dollar.symbol_ahead
        assert trinidad_and_tobago_dollar.symbol_separator == ''
        assert trinidad_and_tobago_dollar.localized_symbol == 'TT$'
        assert trinidad_and_tobago_dollar.convertion == ''
        assert trinidad_and_tobago_dollar.__hash__() == hash(
            (trinidad_and_tobago_dollar.__class__, decimal, 'TTD', '780'))
        assert trinidad_and_tobago_dollar.__repr__() == (
            'TrinidadandTobagoDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TTD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TT$", '
            'numeric_code: "780", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert trinidad_and_tobago_dollar.__str__() == '$0.14'

    def test_trinidad_and_tobago_dollar_negative(self):
        """test_trinidad_and_tobago_dollar_negative."""
        amount = -100
        trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert trinidad_and_tobago_dollar.numeric_code == '780'
        assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
        assert trinidad_and_tobago_dollar.decimal_places == 2
        assert trinidad_and_tobago_dollar.decimal_sign == '.'
        assert trinidad_and_tobago_dollar.grouping_places == 3
        assert trinidad_and_tobago_dollar.grouping_sign == ','
        assert not trinidad_and_tobago_dollar.international
        assert trinidad_and_tobago_dollar.symbol == '$'
        assert trinidad_and_tobago_dollar.symbol_ahead
        assert trinidad_and_tobago_dollar.symbol_separator == ''
        assert trinidad_and_tobago_dollar.localized_symbol == 'TT$'
        assert trinidad_and_tobago_dollar.convertion == ''
        assert trinidad_and_tobago_dollar.__hash__() == hash(
            (trinidad_and_tobago_dollar.__class__, decimal, 'TTD', '780'))
        assert trinidad_and_tobago_dollar.__repr__() == (
            'TrinidadandTobagoDollar(amount: -100, '
            'alpha_code: "TTD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TT$", '
            'numeric_code: "780", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert trinidad_and_tobago_dollar.__str__() == '$-100.00'

    def test_trinidad_and_tobago_dollar_custom(self):
        """test_trinidad_and_tobago_dollar_custom."""
        amount = 1000
        trinidad_and_tobago_dollar = TrinidadandTobagoDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert trinidad_and_tobago_dollar.amount == decimal
        assert trinidad_and_tobago_dollar.numeric_code == '780'
        assert trinidad_and_tobago_dollar.alpha_code == 'TTD'
        assert trinidad_and_tobago_dollar.decimal_places == 5
        assert trinidad_and_tobago_dollar.decimal_sign == ','
        assert trinidad_and_tobago_dollar.grouping_places == 2
        assert trinidad_and_tobago_dollar.grouping_sign == '.'
        assert trinidad_and_tobago_dollar.international
        assert trinidad_and_tobago_dollar.symbol == '$'
        assert not trinidad_and_tobago_dollar.symbol_ahead
        assert trinidad_and_tobago_dollar.symbol_separator == '_'
        assert trinidad_and_tobago_dollar.localized_symbol == 'TT$'
        assert trinidad_and_tobago_dollar.convertion == ''
        assert trinidad_and_tobago_dollar.__hash__() == hash(
            (trinidad_and_tobago_dollar.__class__, decimal, 'TTD', '780'))
        assert trinidad_and_tobago_dollar.__repr__() == (
            'TrinidadandTobagoDollar(amount: 1000, '
            'alpha_code: "TTD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TT$", '
            'numeric_code: "780", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert trinidad_and_tobago_dollar.__str__() == 'TTD 10,00.00000'

    def test_trinidad_and_tobago_dollar_changed(self):
        """test_ctrinidad_and_tobago_dollar_changed."""
        trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            trinidad_and_tobago_dollar.international = True

    def test_trinidad_and_tobago_dollar_math_add(self):
        """test_trinidad_and_tobago_dollar_math_add."""
        trinidad_and_tobago_dollar_one = TrinidadandTobagoDollar(amount=1)
        trinidad_and_tobago_dollar_two = TrinidadandTobagoDollar(amount=2)
        trinidad_and_tobago_dollar_three = TrinidadandTobagoDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TTD and OTHER.'):
            _ = trinidad_and_tobago_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.TrinidadandTobagoDollar\'> '
                    'and <class \'str\'>.')):
            _ = trinidad_and_tobago_dollar_one.__add__('1.00')
        assert (
            trinidad_and_tobago_dollar_one +
            trinidad_and_tobago_dollar_two) == trinidad_and_tobago_dollar_three

    def test_trinidad_and_tobago_dollar_slots(self):
        """test_trinidad_and_tobago_dollar_slots."""
        trinidad_and_tobago_dollar = TrinidadandTobagoDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TrinidadandTobagoDollar\' '
                    'object has no attribute \'new_variable\'')):
            trinidad_and_tobago_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Taiwan Dollar representation."""

from multicurrency import TaiwanDollar


class TestTaiwanDollar:
    """TaiwanDollar currency tests."""

    def test_taiwan_dollar(self):
        """test_taiwan_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        taiwan_dollar = TaiwanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert taiwan_dollar.amount == decimal
        assert taiwan_dollar.numeric_code == '901'
        assert taiwan_dollar.alpha_code == 'TWD'
        assert taiwan_dollar.decimal_places == 2
        assert taiwan_dollar.decimal_sign == '.'
        assert taiwan_dollar.grouping_places == 3
        assert taiwan_dollar.grouping_sign == ','
        assert not taiwan_dollar.international
        assert taiwan_dollar.symbol == '$'
        assert taiwan_dollar.symbol_ahead
        assert taiwan_dollar.symbol_separator == ''
        assert taiwan_dollar.localized_symbol == 'TW$'
        assert taiwan_dollar.convertion == ''
        assert taiwan_dollar.__hash__() == hash(
            (taiwan_dollar.__class__, decimal, 'TWD', '901'))
        assert taiwan_dollar.__repr__() == (
            'TaiwanDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TWD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TW$", '
            'numeric_code: "901", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert taiwan_dollar.__str__() == '$0.14'

    def test_taiwan_dollar_negative(self):
        """test_taiwan_dollar_negative."""
        amount = -100
        taiwan_dollar = TaiwanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert taiwan_dollar.numeric_code == '901'
        assert taiwan_dollar.alpha_code == 'TWD'
        assert taiwan_dollar.decimal_places == 2
        assert taiwan_dollar.decimal_sign == '.'
        assert taiwan_dollar.grouping_places == 3
        assert taiwan_dollar.grouping_sign == ','
        assert not taiwan_dollar.international
        assert taiwan_dollar.symbol == '$'
        assert taiwan_dollar.symbol_ahead
        assert taiwan_dollar.symbol_separator == ''
        assert taiwan_dollar.localized_symbol == 'TW$'
        assert taiwan_dollar.convertion == ''
        assert taiwan_dollar.__hash__() == hash(
            (taiwan_dollar.__class__, decimal, 'TWD', '901'))
        assert taiwan_dollar.__repr__() == (
            'TaiwanDollar(amount: -100, '
            'alpha_code: "TWD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TW$", '
            'numeric_code: "901", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert taiwan_dollar.__str__() == '$-100.00'

    def test_taiwan_dollar_custom(self):
        """test_taiwan_dollar_custom."""
        amount = 1000
        taiwan_dollar = TaiwanDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert taiwan_dollar.amount == decimal
        assert taiwan_dollar.numeric_code == '901'
        assert taiwan_dollar.alpha_code == 'TWD'
        assert taiwan_dollar.decimal_places == 5
        assert taiwan_dollar.decimal_sign == ','
        assert taiwan_dollar.grouping_places == 2
        assert taiwan_dollar.grouping_sign == '.'
        assert taiwan_dollar.international
        assert taiwan_dollar.symbol == '$'
        assert not taiwan_dollar.symbol_ahead
        assert taiwan_dollar.symbol_separator == '_'
        assert taiwan_dollar.localized_symbol == 'TW$'
        assert taiwan_dollar.convertion == ''
        assert taiwan_dollar.__hash__() == hash(
            (taiwan_dollar.__class__, decimal, 'TWD', '901'))
        assert taiwan_dollar.__repr__() == (
            'TaiwanDollar(amount: 1000, '
            'alpha_code: "TWD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TW$", '
            'numeric_code: "901", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert taiwan_dollar.__str__() == 'TWD 10,00.00000'

    def test_taiwan_dollar_changed(self):
        """test_ctaiwan_dollar_changed."""
        taiwan_dollar = TaiwanDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            taiwan_dollar.international = True

    def test_taiwan_dollar_math_add(self):
        """test_taiwan_dollar_math_add."""
        taiwan_dollar_one = TaiwanDollar(amount=1)
        taiwan_dollar_two = TaiwanDollar(amount=2)
        taiwan_dollar_three = TaiwanDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TWD and OTHER.'):
            _ = taiwan_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.TaiwanDollar\'> '
                    'and <class \'str\'>.')):
            _ = taiwan_dollar_one.__add__('1.00')
        assert (
            taiwan_dollar_one +
            taiwan_dollar_two) == taiwan_dollar_three

    def test_taiwan_dollar_slots(self):
        """test_taiwan_dollar_slots."""
        taiwan_dollar = TaiwanDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TaiwanDollar\' '
                    'object has no attribute \'new_variable\'')):
            taiwan_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar representation."""

from multicurrency import USDollar


class TestUSDollar:
    """USDollar currency tests."""

    def test_us_dollar(self):
        """test_us_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar = USDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar.amount == decimal
        assert us_dollar.numeric_code == '840'
        assert us_dollar.alpha_code == 'USD'
        assert us_dollar.decimal_places == 2
        assert us_dollar.decimal_sign == '.'
        assert us_dollar.grouping_places == 3
        assert us_dollar.grouping_sign == ','
        assert not us_dollar.international
        assert us_dollar.symbol == '$'
        assert us_dollar.symbol_ahead
        assert us_dollar.symbol_separator == ''
        assert us_dollar.localized_symbol == 'US$'
        assert us_dollar.convertion == ''
        assert us_dollar.__hash__() == hash(
            (us_dollar.__class__, decimal, 'USD', '840'))
        assert us_dollar.__repr__() == (
            'USDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "US$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar.__str__() == '$0.14'

    def test_us_dollar_negative(self):
        """test_us_dollar_negative."""
        amount = -100
        us_dollar = USDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar.numeric_code == '840'
        assert us_dollar.alpha_code == 'USD'
        assert us_dollar.decimal_places == 2
        assert us_dollar.decimal_sign == '.'
        assert us_dollar.grouping_places == 3
        assert us_dollar.grouping_sign == ','
        assert not us_dollar.international
        assert us_dollar.symbol == '$'
        assert us_dollar.symbol_ahead
        assert us_dollar.symbol_separator == ''
        assert us_dollar.localized_symbol == 'US$'
        assert us_dollar.convertion == ''
        assert us_dollar.__hash__() == hash(
            (us_dollar.__class__, decimal, 'USD', '840'))
        assert us_dollar.__repr__() == (
            'USDollar(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "US$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar.__str__() == '$-100.00'

    def test_us_dollar_custom(self):
        """test_us_dollar_custom."""
        amount = 1000
        us_dollar = USDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar.amount == decimal
        assert us_dollar.numeric_code == '840'
        assert us_dollar.alpha_code == 'USD'
        assert us_dollar.decimal_places == 5
        assert us_dollar.decimal_sign == ','
        assert us_dollar.grouping_places == 2
        assert us_dollar.grouping_sign == '.'
        assert us_dollar.international
        assert us_dollar.symbol == '$'
        assert not us_dollar.symbol_ahead
        assert us_dollar.symbol_separator == '_'
        assert us_dollar.localized_symbol == 'US$'
        assert us_dollar.convertion == ''
        assert us_dollar.__hash__() == hash(
            (us_dollar.__class__, decimal, 'USD', '840'))
        assert us_dollar.__repr__() == (
            'USDollar(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "US$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar.__str__() == 'USD 10,00.00000'

    def test_us_dollar_changed(self):
        """test_cus_dollar_changed."""
        us_dollar = USDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar.international = True

    def test_us_dollar_math_add(self):
        """test_us_dollar_math_add."""
        us_dollar_one = USDollar(amount=1)
        us_dollar_two = USDollar(amount=2)
        us_dollar_three = USDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollar\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_one.__add__('1.00')
        assert (
            us_dollar_one +
            us_dollar_two) == us_dollar_three

    def test_us_dollar_slots(self):
        """test_us_dollar_slots."""
        us_dollar = USDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollar\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar AS representation."""

from multicurrency import USDollarAS


class TestUSDollarAS:
    """USDollarAS currency tests."""

    def test_us_dollar_as(self):
        """test_us_dollar_as."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_as = USDollarAS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_as.amount == decimal
        assert us_dollar_as.numeric_code == '840'
        assert us_dollar_as.alpha_code == 'USD'
        assert us_dollar_as.decimal_places == 2
        assert us_dollar_as.decimal_sign == '.'
        assert us_dollar_as.grouping_places == 3
        assert us_dollar_as.grouping_sign == ','
        assert not us_dollar_as.international
        assert us_dollar_as.symbol == '$'
        assert us_dollar_as.symbol_ahead
        assert us_dollar_as.symbol_separator == ''
        assert us_dollar_as.localized_symbol == 'AS$'
        assert us_dollar_as.convertion == ''
        assert us_dollar_as.__hash__() == hash(
            (us_dollar_as.__class__, decimal, 'USD', '840'))
        assert us_dollar_as.__repr__() == (
            'USDollarAS(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AS$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_as.__str__() == '$0.14'

    def test_us_dollar_as_negative(self):
        """test_us_dollar_as_negative."""
        amount = -100
        us_dollar_as = USDollarAS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_as.numeric_code == '840'
        assert us_dollar_as.alpha_code == 'USD'
        assert us_dollar_as.decimal_places == 2
        assert us_dollar_as.decimal_sign == '.'
        assert us_dollar_as.grouping_places == 3
        assert us_dollar_as.grouping_sign == ','
        assert not us_dollar_as.international
        assert us_dollar_as.symbol == '$'
        assert us_dollar_as.symbol_ahead
        assert us_dollar_as.symbol_separator == ''
        assert us_dollar_as.localized_symbol == 'AS$'
        assert us_dollar_as.convertion == ''
        assert us_dollar_as.__hash__() == hash(
            (us_dollar_as.__class__, decimal, 'USD', '840'))
        assert us_dollar_as.__repr__() == (
            'USDollarAS(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AS$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_as.__str__() == '$-100.00'

    def test_us_dollar_as_custom(self):
        """test_us_dollar_as_custom."""
        amount = 1000
        us_dollar_as = USDollarAS(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_as.amount == decimal
        assert us_dollar_as.numeric_code == '840'
        assert us_dollar_as.alpha_code == 'USD'
        assert us_dollar_as.decimal_places == 5
        assert us_dollar_as.decimal_sign == ','
        assert us_dollar_as.grouping_places == 2
        assert us_dollar_as.grouping_sign == '.'
        assert us_dollar_as.international
        assert us_dollar_as.symbol == '$'
        assert not us_dollar_as.symbol_ahead
        assert us_dollar_as.symbol_separator == '_'
        assert us_dollar_as.localized_symbol == 'AS$'
        assert us_dollar_as.convertion == ''
        assert us_dollar_as.__hash__() == hash(
            (us_dollar_as.__class__, decimal, 'USD', '840'))
        assert us_dollar_as.__repr__() == (
            'USDollarAS(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AS$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_as.__str__() == 'USD 10,00.00000'

    def test_us_dollar_as_changed(self):
        """test_cus_dollar_as_changed."""
        us_dollar_as = USDollarAS(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_as.international = True

    def test_us_dollar_as_math_add(self):
        """test_us_dollar_as_math_add."""
        us_dollar_as_one = USDollarAS(amount=1)
        us_dollar_as_two = USDollarAS(amount=2)
        us_dollar_as_three = USDollarAS(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_as_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarAS\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_as_one.__add__('1.00')
        assert (
            us_dollar_as_one +
            us_dollar_as_two) == us_dollar_as_three

    def test_us_dollar_as_slots(self):
        """test_us_dollar_as_slots."""
        us_dollar_as = USDollarAS(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarAS\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_as.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar IO representation."""

from multicurrency import USDollarIO


class TestUSDollarIO:
    """USDollarIO currency tests."""

    def test_us_dollar_io(self):
        """test_us_dollar_io."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_io = USDollarIO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_io.amount == decimal
        assert us_dollar_io.numeric_code == '840'
        assert us_dollar_io.alpha_code == 'USD'
        assert us_dollar_io.decimal_places == 2
        assert us_dollar_io.decimal_sign == '.'
        assert us_dollar_io.grouping_places == 3
        assert us_dollar_io.grouping_sign == ','
        assert not us_dollar_io.international
        assert us_dollar_io.symbol == '$'
        assert us_dollar_io.symbol_ahead
        assert us_dollar_io.symbol_separator == ''
        assert us_dollar_io.localized_symbol == 'IO$'
        assert us_dollar_io.convertion == ''
        assert us_dollar_io.__hash__() == hash(
            (us_dollar_io.__class__, decimal, 'USD', '840'))
        assert us_dollar_io.__repr__() == (
            'USDollarIO(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IO$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_io.__str__() == '$0.14'

    def test_us_dollar_io_negative(self):
        """test_us_dollar_io_negative."""
        amount = -100
        us_dollar_io = USDollarIO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_io.numeric_code == '840'
        assert us_dollar_io.alpha_code == 'USD'
        assert us_dollar_io.decimal_places == 2
        assert us_dollar_io.decimal_sign == '.'
        assert us_dollar_io.grouping_places == 3
        assert us_dollar_io.grouping_sign == ','
        assert not us_dollar_io.international
        assert us_dollar_io.symbol == '$'
        assert us_dollar_io.symbol_ahead
        assert us_dollar_io.symbol_separator == ''
        assert us_dollar_io.localized_symbol == 'IO$'
        assert us_dollar_io.convertion == ''
        assert us_dollar_io.__hash__() == hash(
            (us_dollar_io.__class__, decimal, 'USD', '840'))
        assert us_dollar_io.__repr__() == (
            'USDollarIO(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IO$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_io.__str__() == '$-100.00'

    def test_us_dollar_io_custom(self):
        """test_us_dollar_io_custom."""
        amount = 1000
        us_dollar_io = USDollarIO(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_io.amount == decimal
        assert us_dollar_io.numeric_code == '840'
        assert us_dollar_io.alpha_code == 'USD'
        assert us_dollar_io.decimal_places == 5
        assert us_dollar_io.decimal_sign == ','
        assert us_dollar_io.grouping_places == 2
        assert us_dollar_io.grouping_sign == '.'
        assert us_dollar_io.international
        assert us_dollar_io.symbol == '$'
        assert not us_dollar_io.symbol_ahead
        assert us_dollar_io.symbol_separator == '_'
        assert us_dollar_io.localized_symbol == 'IO$'
        assert us_dollar_io.convertion == ''
        assert us_dollar_io.__hash__() == hash(
            (us_dollar_io.__class__, decimal, 'USD', '840'))
        assert us_dollar_io.__repr__() == (
            'USDollarIO(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IO$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_io.__str__() == 'USD 10,00.00000'

    def test_us_dollar_io_changed(self):
        """test_cus_dollar_io_changed."""
        us_dollar_io = USDollarIO(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_io.international = True

    def test_us_dollar_io_math_add(self):
        """test_us_dollar_io_math_add."""
        us_dollar_io_one = USDollarIO(amount=1)
        us_dollar_io_two = USDollarIO(amount=2)
        us_dollar_io_three = USDollarIO(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_io_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarIO\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_io_one.__add__('1.00')
        assert (
            us_dollar_io_one +
            us_dollar_io_two) == us_dollar_io_three

    def test_us_dollar_io_slots(self):
        """test_us_dollar_io_slots."""
        us_dollar_io = USDollarIO(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarIO\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_io.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar VG representation."""

from multicurrency import USDollarVG


class TestUSDollarVG:
    """USDollarVG currency tests."""

    def test_us_dollar_vg(self):
        """test_us_dollar_vg."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_vg = USDollarVG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vg.amount == decimal
        assert us_dollar_vg.numeric_code == '840'
        assert us_dollar_vg.alpha_code == 'USD'
        assert us_dollar_vg.decimal_places == 2
        assert us_dollar_vg.decimal_sign == '.'
        assert us_dollar_vg.grouping_places == 3
        assert us_dollar_vg.grouping_sign == ','
        assert not us_dollar_vg.international
        assert us_dollar_vg.symbol == '$'
        assert us_dollar_vg.symbol_ahead
        assert us_dollar_vg.symbol_separator == ''
        assert us_dollar_vg.localized_symbol == 'VG$'
        assert us_dollar_vg.convertion == ''
        assert us_dollar_vg.__hash__() == hash(
            (us_dollar_vg.__class__, decimal, 'USD', '840'))
        assert us_dollar_vg.__repr__() == (
            'USDollarVG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VG$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_vg.__str__() == '$0.14'

    def test_us_dollar_vg_negative(self):
        """test_us_dollar_vg_negative."""
        amount = -100
        us_dollar_vg = USDollarVG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vg.numeric_code == '840'
        assert us_dollar_vg.alpha_code == 'USD'
        assert us_dollar_vg.decimal_places == 2
        assert us_dollar_vg.decimal_sign == '.'
        assert us_dollar_vg.grouping_places == 3
        assert us_dollar_vg.grouping_sign == ','
        assert not us_dollar_vg.international
        assert us_dollar_vg.symbol == '$'
        assert us_dollar_vg.symbol_ahead
        assert us_dollar_vg.symbol_separator == ''
        assert us_dollar_vg.localized_symbol == 'VG$'
        assert us_dollar_vg.convertion == ''
        assert us_dollar_vg.__hash__() == hash(
            (us_dollar_vg.__class__, decimal, 'USD', '840'))
        assert us_dollar_vg.__repr__() == (
            'USDollarVG(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VG$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_vg.__str__() == '$-100.00'

    def test_us_dollar_vg_custom(self):
        """test_us_dollar_vg_custom."""
        amount = 1000
        us_dollar_vg = USDollarVG(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vg.amount == decimal
        assert us_dollar_vg.numeric_code == '840'
        assert us_dollar_vg.alpha_code == 'USD'
        assert us_dollar_vg.decimal_places == 5
        assert us_dollar_vg.decimal_sign == ','
        assert us_dollar_vg.grouping_places == 2
        assert us_dollar_vg.grouping_sign == '.'
        assert us_dollar_vg.international
        assert us_dollar_vg.symbol == '$'
        assert not us_dollar_vg.symbol_ahead
        assert us_dollar_vg.symbol_separator == '_'
        assert us_dollar_vg.localized_symbol == 'VG$'
        assert us_dollar_vg.convertion == ''
        assert us_dollar_vg.__hash__() == hash(
            (us_dollar_vg.__class__, decimal, 'USD', '840'))
        assert us_dollar_vg.__repr__() == (
            'USDollarVG(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "VG$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_vg.__str__() == 'USD 10,00.00000'

    def test_us_dollar_vg_changed(self):
        """test_cus_dollar_vg_changed."""
        us_dollar_vg = USDollarVG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vg.international = True

    def test_us_dollar_vg_math_add(self):
        """test_us_dollar_vg_math_add."""
        us_dollar_vg_one = USDollarVG(amount=1)
        us_dollar_vg_two = USDollarVG(amount=2)
        us_dollar_vg_three = USDollarVG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_vg_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarVG\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_vg_one.__add__('1.00')
        assert (
            us_dollar_vg_one +
            us_dollar_vg_two) == us_dollar_vg_three

    def test_us_dollar_vg_slots(self):
        """test_us_dollar_vg_slots."""
        us_dollar_vg = USDollarVG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarVG\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_vg.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar GU representation."""

from multicurrency import USDollarGU


class TestUSDollarGU:
    """USDollarGU currency tests."""

    def test_us_dollar_gu(self):
        """test_us_dollar_gu."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_gu = USDollarGU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_gu.amount == decimal
        assert us_dollar_gu.numeric_code == '840'
        assert us_dollar_gu.alpha_code == 'USD'
        assert us_dollar_gu.decimal_places == 2
        assert us_dollar_gu.decimal_sign == '.'
        assert us_dollar_gu.grouping_places == 3
        assert us_dollar_gu.grouping_sign == ','
        assert not us_dollar_gu.international
        assert us_dollar_gu.symbol == '$'
        assert us_dollar_gu.symbol_ahead
        assert us_dollar_gu.symbol_separator == ''
        assert us_dollar_gu.localized_symbol == 'GU$'
        assert us_dollar_gu.convertion == ''
        assert us_dollar_gu.__hash__() == hash(
            (us_dollar_gu.__class__, decimal, 'USD', '840'))
        assert us_dollar_gu.__repr__() == (
            'USDollarGU(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GU$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_gu.__str__() == '$0.14'

    def test_us_dollar_gu_negative(self):
        """test_us_dollar_gu_negative."""
        amount = -100
        us_dollar_gu = USDollarGU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_gu.numeric_code == '840'
        assert us_dollar_gu.alpha_code == 'USD'
        assert us_dollar_gu.decimal_places == 2
        assert us_dollar_gu.decimal_sign == '.'
        assert us_dollar_gu.grouping_places == 3
        assert us_dollar_gu.grouping_sign == ','
        assert not us_dollar_gu.international
        assert us_dollar_gu.symbol == '$'
        assert us_dollar_gu.symbol_ahead
        assert us_dollar_gu.symbol_separator == ''
        assert us_dollar_gu.localized_symbol == 'GU$'
        assert us_dollar_gu.convertion == ''
        assert us_dollar_gu.__hash__() == hash(
            (us_dollar_gu.__class__, decimal, 'USD', '840'))
        assert us_dollar_gu.__repr__() == (
            'USDollarGU(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GU$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_gu.__str__() == '$-100.00'

    def test_us_dollar_gu_custom(self):
        """test_us_dollar_gu_custom."""
        amount = 1000
        us_dollar_gu = USDollarGU(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_gu.amount == decimal
        assert us_dollar_gu.numeric_code == '840'
        assert us_dollar_gu.alpha_code == 'USD'
        assert us_dollar_gu.decimal_places == 5
        assert us_dollar_gu.decimal_sign == ','
        assert us_dollar_gu.grouping_places == 2
        assert us_dollar_gu.grouping_sign == '.'
        assert us_dollar_gu.international
        assert us_dollar_gu.symbol == '$'
        assert not us_dollar_gu.symbol_ahead
        assert us_dollar_gu.symbol_separator == '_'
        assert us_dollar_gu.localized_symbol == 'GU$'
        assert us_dollar_gu.convertion == ''
        assert us_dollar_gu.__hash__() == hash(
            (us_dollar_gu.__class__, decimal, 'USD', '840'))
        assert us_dollar_gu.__repr__() == (
            'USDollarGU(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GU$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_gu.__str__() == 'USD 10,00.00000'

    def test_us_dollar_gu_changed(self):
        """test_cus_dollar_gu_changed."""
        us_dollar_gu = USDollarGU(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_gu.international = True

    def test_us_dollar_gu_math_add(self):
        """test_us_dollar_gu_math_add."""
        us_dollar_gu_one = USDollarGU(amount=1)
        us_dollar_gu_two = USDollarGU(amount=2)
        us_dollar_gu_three = USDollarGU(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_gu_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarGU\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_gu_one.__add__('1.00')
        assert (
            us_dollar_gu_one +
            us_dollar_gu_two) == us_dollar_gu_three

    def test_us_dollar_gu_slots(self):
        """test_us_dollar_gu_slots."""
        us_dollar_gu = USDollarGU(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarGU\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_gu.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar HT representation."""

from multicurrency import USDollarHT


class TestUSDollarHT:
    """USDollarHT currency tests."""

    def test_us_dollar_ht(self):
        """test_us_dollar_ht."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_ht = USDollarHT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_ht.amount == decimal
        assert us_dollar_ht.numeric_code == '840'
        assert us_dollar_ht.alpha_code == 'USD'
        assert us_dollar_ht.decimal_places == 2
        assert us_dollar_ht.decimal_sign == '.'
        assert us_dollar_ht.grouping_places == 3
        assert us_dollar_ht.grouping_sign == ','
        assert not us_dollar_ht.international
        assert us_dollar_ht.symbol == '$'
        assert us_dollar_ht.symbol_ahead
        assert us_dollar_ht.symbol_separator == ''
        assert us_dollar_ht.localized_symbol == 'HT$'
        assert us_dollar_ht.convertion == ''
        assert us_dollar_ht.__hash__() == hash(
            (us_dollar_ht.__class__, decimal, 'USD', '840'))
        assert us_dollar_ht.__repr__() == (
            'USDollarHT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "HT$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_ht.__str__() == '$0.14'

    def test_us_dollar_ht_negative(self):
        """test_us_dollar_ht_negative."""
        amount = -100
        us_dollar_ht = USDollarHT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_ht.numeric_code == '840'
        assert us_dollar_ht.alpha_code == 'USD'
        assert us_dollar_ht.decimal_places == 2
        assert us_dollar_ht.decimal_sign == '.'
        assert us_dollar_ht.grouping_places == 3
        assert us_dollar_ht.grouping_sign == ','
        assert not us_dollar_ht.international
        assert us_dollar_ht.symbol == '$'
        assert us_dollar_ht.symbol_ahead
        assert us_dollar_ht.symbol_separator == ''
        assert us_dollar_ht.localized_symbol == 'HT$'
        assert us_dollar_ht.convertion == ''
        assert us_dollar_ht.__hash__() == hash(
            (us_dollar_ht.__class__, decimal, 'USD', '840'))
        assert us_dollar_ht.__repr__() == (
            'USDollarHT(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "HT$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_ht.__str__() == '$-100.00'

    def test_us_dollar_ht_custom(self):
        """test_us_dollar_ht_custom."""
        amount = 1000
        us_dollar_ht = USDollarHT(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_ht.amount == decimal
        assert us_dollar_ht.numeric_code == '840'
        assert us_dollar_ht.alpha_code == 'USD'
        assert us_dollar_ht.decimal_places == 5
        assert us_dollar_ht.decimal_sign == ','
        assert us_dollar_ht.grouping_places == 2
        assert us_dollar_ht.grouping_sign == '.'
        assert us_dollar_ht.international
        assert us_dollar_ht.symbol == '$'
        assert not us_dollar_ht.symbol_ahead
        assert us_dollar_ht.symbol_separator == '_'
        assert us_dollar_ht.localized_symbol == 'HT$'
        assert us_dollar_ht.convertion == ''
        assert us_dollar_ht.__hash__() == hash(
            (us_dollar_ht.__class__, decimal, 'USD', '840'))
        assert us_dollar_ht.__repr__() == (
            'USDollarHT(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "HT$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_ht.__str__() == 'USD 10,00.00000'

    def test_us_dollar_ht_changed(self):
        """test_cus_dollar_ht_changed."""
        us_dollar_ht = USDollarHT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_ht.international = True

    def test_us_dollar_ht_math_add(self):
        """test_us_dollar_ht_math_add."""
        us_dollar_ht_one = USDollarHT(amount=1)
        us_dollar_ht_two = USDollarHT(amount=2)
        us_dollar_ht_three = USDollarHT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_ht_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarHT\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_ht_one.__add__('1.00')
        assert (
            us_dollar_ht_one +
            us_dollar_ht_two) == us_dollar_ht_three

    def test_us_dollar_ht_slots(self):
        """test_us_dollar_ht_slots."""
        us_dollar_ht = USDollarHT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarHT\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_ht.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar MH representation."""

from multicurrency import USDollarMH


class TestUSDollarMH:
    """USDollarMH currency tests."""

    def test_us_dollar_mh(self):
        """test_us_dollar_mh."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_mh = USDollarMH(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mh.amount == decimal
        assert us_dollar_mh.numeric_code == '840'
        assert us_dollar_mh.alpha_code == 'USD'
        assert us_dollar_mh.decimal_places == 2
        assert us_dollar_mh.decimal_sign == '.'
        assert us_dollar_mh.grouping_places == 3
        assert us_dollar_mh.grouping_sign == ','
        assert not us_dollar_mh.international
        assert us_dollar_mh.symbol == '$'
        assert us_dollar_mh.symbol_ahead
        assert us_dollar_mh.symbol_separator == ''
        assert us_dollar_mh.localized_symbol == 'MH$'
        assert us_dollar_mh.convertion == ''
        assert us_dollar_mh.__hash__() == hash(
            (us_dollar_mh.__class__, decimal, 'USD', '840'))
        assert us_dollar_mh.__repr__() == (
            'USDollarMH(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MH$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_mh.__str__() == '$0.14'

    def test_us_dollar_mh_negative(self):
        """test_us_dollar_mh_negative."""
        amount = -100
        us_dollar_mh = USDollarMH(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mh.numeric_code == '840'
        assert us_dollar_mh.alpha_code == 'USD'
        assert us_dollar_mh.decimal_places == 2
        assert us_dollar_mh.decimal_sign == '.'
        assert us_dollar_mh.grouping_places == 3
        assert us_dollar_mh.grouping_sign == ','
        assert not us_dollar_mh.international
        assert us_dollar_mh.symbol == '$'
        assert us_dollar_mh.symbol_ahead
        assert us_dollar_mh.symbol_separator == ''
        assert us_dollar_mh.localized_symbol == 'MH$'
        assert us_dollar_mh.convertion == ''
        assert us_dollar_mh.__hash__() == hash(
            (us_dollar_mh.__class__, decimal, 'USD', '840'))
        assert us_dollar_mh.__repr__() == (
            'USDollarMH(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MH$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_mh.__str__() == '$-100.00'

    def test_us_dollar_mh_custom(self):
        """test_us_dollar_mh_custom."""
        amount = 1000
        us_dollar_mh = USDollarMH(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mh.amount == decimal
        assert us_dollar_mh.numeric_code == '840'
        assert us_dollar_mh.alpha_code == 'USD'
        assert us_dollar_mh.decimal_places == 5
        assert us_dollar_mh.decimal_sign == ','
        assert us_dollar_mh.grouping_places == 2
        assert us_dollar_mh.grouping_sign == '.'
        assert us_dollar_mh.international
        assert us_dollar_mh.symbol == '$'
        assert not us_dollar_mh.symbol_ahead
        assert us_dollar_mh.symbol_separator == '_'
        assert us_dollar_mh.localized_symbol == 'MH$'
        assert us_dollar_mh.convertion == ''
        assert us_dollar_mh.__hash__() == hash(
            (us_dollar_mh.__class__, decimal, 'USD', '840'))
        assert us_dollar_mh.__repr__() == (
            'USDollarMH(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MH$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_mh.__str__() == 'USD 10,00.00000'

    def test_us_dollar_mh_changed(self):
        """test_cus_dollar_mh_changed."""
        us_dollar_mh = USDollarMH(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mh.international = True

    def test_us_dollar_mh_math_add(self):
        """test_us_dollar_mh_math_add."""
        us_dollar_mh_one = USDollarMH(amount=1)
        us_dollar_mh_two = USDollarMH(amount=2)
        us_dollar_mh_three = USDollarMH(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_mh_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarMH\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_mh_one.__add__('1.00')
        assert (
            us_dollar_mh_one +
            us_dollar_mh_two) == us_dollar_mh_three

    def test_us_dollar_mh_slots(self):
        """test_us_dollar_mh_slots."""
        us_dollar_mh = USDollarMH(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarMH\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_mh.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar FM representation."""

from multicurrency import USDollarFM


class TestUSDollarFM:
    """USDollarFM currency tests."""

    def test_us_dollar_fm(self):
        """test_us_dollar_fm."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_fm = USDollarFM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_fm.amount == decimal
        assert us_dollar_fm.numeric_code == '840'
        assert us_dollar_fm.alpha_code == 'USD'
        assert us_dollar_fm.decimal_places == 2
        assert us_dollar_fm.decimal_sign == '.'
        assert us_dollar_fm.grouping_places == 3
        assert us_dollar_fm.grouping_sign == ','
        assert not us_dollar_fm.international
        assert us_dollar_fm.symbol == '$'
        assert us_dollar_fm.symbol_ahead
        assert us_dollar_fm.symbol_separator == ''
        assert us_dollar_fm.localized_symbol == 'FM$'
        assert us_dollar_fm.convertion == ''
        assert us_dollar_fm.__hash__() == hash(
            (us_dollar_fm.__class__, decimal, 'USD', '840'))
        assert us_dollar_fm.__repr__() == (
            'USDollarFM(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FM$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_fm.__str__() == '$0.14'

    def test_us_dollar_fm_negative(self):
        """test_us_dollar_fm_negative."""
        amount = -100
        us_dollar_fm = USDollarFM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_fm.numeric_code == '840'
        assert us_dollar_fm.alpha_code == 'USD'
        assert us_dollar_fm.decimal_places == 2
        assert us_dollar_fm.decimal_sign == '.'
        assert us_dollar_fm.grouping_places == 3
        assert us_dollar_fm.grouping_sign == ','
        assert not us_dollar_fm.international
        assert us_dollar_fm.symbol == '$'
        assert us_dollar_fm.symbol_ahead
        assert us_dollar_fm.symbol_separator == ''
        assert us_dollar_fm.localized_symbol == 'FM$'
        assert us_dollar_fm.convertion == ''
        assert us_dollar_fm.__hash__() == hash(
            (us_dollar_fm.__class__, decimal, 'USD', '840'))
        assert us_dollar_fm.__repr__() == (
            'USDollarFM(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "FM$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_fm.__str__() == '$-100.00'

    def test_us_dollar_fm_custom(self):
        """test_us_dollar_fm_custom."""
        amount = 1000
        us_dollar_fm = USDollarFM(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_fm.amount == decimal
        assert us_dollar_fm.numeric_code == '840'
        assert us_dollar_fm.alpha_code == 'USD'
        assert us_dollar_fm.decimal_places == 5
        assert us_dollar_fm.decimal_sign == ','
        assert us_dollar_fm.grouping_places == 2
        assert us_dollar_fm.grouping_sign == '.'
        assert us_dollar_fm.international
        assert us_dollar_fm.symbol == '$'
        assert not us_dollar_fm.symbol_ahead
        assert us_dollar_fm.symbol_separator == '_'
        assert us_dollar_fm.localized_symbol == 'FM$'
        assert us_dollar_fm.convertion == ''
        assert us_dollar_fm.__hash__() == hash(
            (us_dollar_fm.__class__, decimal, 'USD', '840'))
        assert us_dollar_fm.__repr__() == (
            'USDollarFM(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "FM$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_fm.__str__() == 'USD 10,00.00000'

    def test_us_dollar_fm_changed(self):
        """test_cus_dollar_fm_changed."""
        us_dollar_fm = USDollarFM(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_fm.international = True

    def test_us_dollar_fm_math_add(self):
        """test_us_dollar_fm_math_add."""
        us_dollar_fm_one = USDollarFM(amount=1)
        us_dollar_fm_two = USDollarFM(amount=2)
        us_dollar_fm_three = USDollarFM(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_fm_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarFM\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_fm_one.__add__('1.00')
        assert (
            us_dollar_fm_one +
            us_dollar_fm_two) == us_dollar_fm_three

    def test_us_dollar_fm_slots(self):
        """test_us_dollar_fm_slots."""
        us_dollar_fm = USDollarFM(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarFM\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_fm.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar MP representation."""

from multicurrency import USDollarMP


class TestUSDollarMP:
    """USDollarMP currency tests."""

    def test_us_dollar_mp(self):
        """test_us_dollar_mp."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_mp = USDollarMP(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mp.amount == decimal
        assert us_dollar_mp.numeric_code == '840'
        assert us_dollar_mp.alpha_code == 'USD'
        assert us_dollar_mp.decimal_places == 2
        assert us_dollar_mp.decimal_sign == '.'
        assert us_dollar_mp.grouping_places == 3
        assert us_dollar_mp.grouping_sign == ','
        assert not us_dollar_mp.international
        assert us_dollar_mp.symbol == '$'
        assert us_dollar_mp.symbol_ahead
        assert us_dollar_mp.symbol_separator == ''
        assert us_dollar_mp.localized_symbol == 'MP$'
        assert us_dollar_mp.convertion == ''
        assert us_dollar_mp.__hash__() == hash(
            (us_dollar_mp.__class__, decimal, 'USD', '840'))
        assert us_dollar_mp.__repr__() == (
            'USDollarMP(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MP$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_mp.__str__() == '$0.14'

    def test_us_dollar_mp_negative(self):
        """test_us_dollar_mp_negative."""
        amount = -100
        us_dollar_mp = USDollarMP(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mp.numeric_code == '840'
        assert us_dollar_mp.alpha_code == 'USD'
        assert us_dollar_mp.decimal_places == 2
        assert us_dollar_mp.decimal_sign == '.'
        assert us_dollar_mp.grouping_places == 3
        assert us_dollar_mp.grouping_sign == ','
        assert not us_dollar_mp.international
        assert us_dollar_mp.symbol == '$'
        assert us_dollar_mp.symbol_ahead
        assert us_dollar_mp.symbol_separator == ''
        assert us_dollar_mp.localized_symbol == 'MP$'
        assert us_dollar_mp.convertion == ''
        assert us_dollar_mp.__hash__() == hash(
            (us_dollar_mp.__class__, decimal, 'USD', '840'))
        assert us_dollar_mp.__repr__() == (
            'USDollarMP(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MP$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_mp.__str__() == '$-100.00'

    def test_us_dollar_mp_custom(self):
        """test_us_dollar_mp_custom."""
        amount = 1000
        us_dollar_mp = USDollarMP(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_mp.amount == decimal
        assert us_dollar_mp.numeric_code == '840'
        assert us_dollar_mp.alpha_code == 'USD'
        assert us_dollar_mp.decimal_places == 5
        assert us_dollar_mp.decimal_sign == ','
        assert us_dollar_mp.grouping_places == 2
        assert us_dollar_mp.grouping_sign == '.'
        assert us_dollar_mp.international
        assert us_dollar_mp.symbol == '$'
        assert not us_dollar_mp.symbol_ahead
        assert us_dollar_mp.symbol_separator == '_'
        assert us_dollar_mp.localized_symbol == 'MP$'
        assert us_dollar_mp.convertion == ''
        assert us_dollar_mp.__hash__() == hash(
            (us_dollar_mp.__class__, decimal, 'USD', '840'))
        assert us_dollar_mp.__repr__() == (
            'USDollarMP(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MP$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_mp.__str__() == 'USD 10,00.00000'

    def test_us_dollar_mp_changed(self):
        """test_cus_dollar_mp_changed."""
        us_dollar_mp = USDollarMP(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_mp.international = True

    def test_us_dollar_mp_math_add(self):
        """test_us_dollar_mp_math_add."""
        us_dollar_mp_one = USDollarMP(amount=1)
        us_dollar_mp_two = USDollarMP(amount=2)
        us_dollar_mp_three = USDollarMP(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_mp_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarMP\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_mp_one.__add__('1.00')
        assert (
            us_dollar_mp_one +
            us_dollar_mp_two) == us_dollar_mp_three

    def test_us_dollar_mp_slots(self):
        """test_us_dollar_mp_slots."""
        us_dollar_mp = USDollarMP(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarMP\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_mp.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar PC representation."""

from multicurrency import USDollarPC


class TestUSDollarPC:
    """USDollarPC currency tests."""

    def test_us_dollar_pc(self):
        """test_us_dollar_pc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_pc = USDollarPC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pc.amount == decimal
        assert us_dollar_pc.numeric_code == '840'
        assert us_dollar_pc.alpha_code == 'USD'
        assert us_dollar_pc.decimal_places == 2
        assert us_dollar_pc.decimal_sign == '.'
        assert us_dollar_pc.grouping_places == 3
        assert us_dollar_pc.grouping_sign == ','
        assert not us_dollar_pc.international
        assert us_dollar_pc.symbol == '$'
        assert us_dollar_pc.symbol_ahead
        assert us_dollar_pc.symbol_separator == ''
        assert us_dollar_pc.localized_symbol == 'PC$'
        assert us_dollar_pc.convertion == ''
        assert us_dollar_pc.__hash__() == hash(
            (us_dollar_pc.__class__, decimal, 'USD', '840'))
        assert us_dollar_pc.__repr__() == (
            'USDollarPC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PC$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pc.__str__() == '$0.14'

    def test_us_dollar_pc_negative(self):
        """test_us_dollar_pc_negative."""
        amount = -100
        us_dollar_pc = USDollarPC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pc.numeric_code == '840'
        assert us_dollar_pc.alpha_code == 'USD'
        assert us_dollar_pc.decimal_places == 2
        assert us_dollar_pc.decimal_sign == '.'
        assert us_dollar_pc.grouping_places == 3
        assert us_dollar_pc.grouping_sign == ','
        assert not us_dollar_pc.international
        assert us_dollar_pc.symbol == '$'
        assert us_dollar_pc.symbol_ahead
        assert us_dollar_pc.symbol_separator == ''
        assert us_dollar_pc.localized_symbol == 'PC$'
        assert us_dollar_pc.convertion == ''
        assert us_dollar_pc.__hash__() == hash(
            (us_dollar_pc.__class__, decimal, 'USD', '840'))
        assert us_dollar_pc.__repr__() == (
            'USDollarPC(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PC$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pc.__str__() == '$-100.00'

    def test_us_dollar_pc_custom(self):
        """test_us_dollar_pc_custom."""
        amount = 1000
        us_dollar_pc = USDollarPC(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pc.amount == decimal
        assert us_dollar_pc.numeric_code == '840'
        assert us_dollar_pc.alpha_code == 'USD'
        assert us_dollar_pc.decimal_places == 5
        assert us_dollar_pc.decimal_sign == ','
        assert us_dollar_pc.grouping_places == 2
        assert us_dollar_pc.grouping_sign == '.'
        assert us_dollar_pc.international
        assert us_dollar_pc.symbol == '$'
        assert not us_dollar_pc.symbol_ahead
        assert us_dollar_pc.symbol_separator == '_'
        assert us_dollar_pc.localized_symbol == 'PC$'
        assert us_dollar_pc.convertion == ''
        assert us_dollar_pc.__hash__() == hash(
            (us_dollar_pc.__class__, decimal, 'USD', '840'))
        assert us_dollar_pc.__repr__() == (
            'USDollarPC(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PC$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_pc.__str__() == 'USD 10,00.00000'

    def test_us_dollar_pc_changed(self):
        """test_cus_dollar_pc_changed."""
        us_dollar_pc = USDollarPC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pc.international = True

    def test_us_dollar_pc_math_add(self):
        """test_us_dollar_pc_math_add."""
        us_dollar_pc_one = USDollarPC(amount=1)
        us_dollar_pc_two = USDollarPC(amount=2)
        us_dollar_pc_three = USDollarPC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_pc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarPC\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_pc_one.__add__('1.00')
        assert (
            us_dollar_pc_one +
            us_dollar_pc_two) == us_dollar_pc_three

    def test_us_dollar_pc_slots(self):
        """test_us_dollar_pc_slots."""
        us_dollar_pc = USDollarPC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarPC\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_pc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar PW representation."""

from multicurrency import USDollarPW


class TestUSDollarPW:
    """USDollarPW currency tests."""

    def test_us_dollar_pw(self):
        """test_us_dollar_pw."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_pw = USDollarPW(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pw.amount == decimal
        assert us_dollar_pw.numeric_code == '840'
        assert us_dollar_pw.alpha_code == 'USD'
        assert us_dollar_pw.decimal_places == 2
        assert us_dollar_pw.decimal_sign == '.'
        assert us_dollar_pw.grouping_places == 3
        assert us_dollar_pw.grouping_sign == ','
        assert not us_dollar_pw.international
        assert us_dollar_pw.symbol == '$'
        assert us_dollar_pw.symbol_ahead
        assert us_dollar_pw.symbol_separator == ''
        assert us_dollar_pw.localized_symbol == 'PW$'
        assert us_dollar_pw.convertion == ''
        assert us_dollar_pw.__hash__() == hash(
            (us_dollar_pw.__class__, decimal, 'USD', '840'))
        assert us_dollar_pw.__repr__() == (
            'USDollarPW(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PW$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pw.__str__() == '$0.14'

    def test_us_dollar_pw_negative(self):
        """test_us_dollar_pw_negative."""
        amount = -100
        us_dollar_pw = USDollarPW(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pw.numeric_code == '840'
        assert us_dollar_pw.alpha_code == 'USD'
        assert us_dollar_pw.decimal_places == 2
        assert us_dollar_pw.decimal_sign == '.'
        assert us_dollar_pw.grouping_places == 3
        assert us_dollar_pw.grouping_sign == ','
        assert not us_dollar_pw.international
        assert us_dollar_pw.symbol == '$'
        assert us_dollar_pw.symbol_ahead
        assert us_dollar_pw.symbol_separator == ''
        assert us_dollar_pw.localized_symbol == 'PW$'
        assert us_dollar_pw.convertion == ''
        assert us_dollar_pw.__hash__() == hash(
            (us_dollar_pw.__class__, decimal, 'USD', '840'))
        assert us_dollar_pw.__repr__() == (
            'USDollarPW(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PW$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pw.__str__() == '$-100.00'

    def test_us_dollar_pw_custom(self):
        """test_us_dollar_pw_custom."""
        amount = 1000
        us_dollar_pw = USDollarPW(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pw.amount == decimal
        assert us_dollar_pw.numeric_code == '840'
        assert us_dollar_pw.alpha_code == 'USD'
        assert us_dollar_pw.decimal_places == 5
        assert us_dollar_pw.decimal_sign == ','
        assert us_dollar_pw.grouping_places == 2
        assert us_dollar_pw.grouping_sign == '.'
        assert us_dollar_pw.international
        assert us_dollar_pw.symbol == '$'
        assert not us_dollar_pw.symbol_ahead
        assert us_dollar_pw.symbol_separator == '_'
        assert us_dollar_pw.localized_symbol == 'PW$'
        assert us_dollar_pw.convertion == ''
        assert us_dollar_pw.__hash__() == hash(
            (us_dollar_pw.__class__, decimal, 'USD', '840'))
        assert us_dollar_pw.__repr__() == (
            'USDollarPW(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PW$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_pw.__str__() == 'USD 10,00.00000'

    def test_us_dollar_pw_changed(self):
        """test_cus_dollar_pw_changed."""
        us_dollar_pw = USDollarPW(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pw.international = True

    def test_us_dollar_pw_math_add(self):
        """test_us_dollar_pw_math_add."""
        us_dollar_pw_one = USDollarPW(amount=1)
        us_dollar_pw_two = USDollarPW(amount=2)
        us_dollar_pw_three = USDollarPW(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_pw_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarPW\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_pw_one.__add__('1.00')
        assert (
            us_dollar_pw_one +
            us_dollar_pw_two) == us_dollar_pw_three

    def test_us_dollar_pw_slots(self):
        """test_us_dollar_pw_slots."""
        us_dollar_pw = USDollarPW(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarPW\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_pw.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar PA representation."""

from multicurrency import USDollarPA


class TestUSDollarPA:
    """USDollarPA currency tests."""

    def test_us_dollar_pa(self):
        """test_us_dollar_pa."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_pa = USDollarPA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pa.amount == decimal
        assert us_dollar_pa.numeric_code == '840'
        assert us_dollar_pa.alpha_code == 'USD'
        assert us_dollar_pa.decimal_places == 2
        assert us_dollar_pa.decimal_sign == '.'
        assert us_dollar_pa.grouping_places == 3
        assert us_dollar_pa.grouping_sign == ','
        assert not us_dollar_pa.international
        assert us_dollar_pa.symbol == '$'
        assert us_dollar_pa.symbol_ahead
        assert us_dollar_pa.symbol_separator == ''
        assert us_dollar_pa.localized_symbol == 'PA$'
        assert us_dollar_pa.convertion == ''
        assert us_dollar_pa.__hash__() == hash(
            (us_dollar_pa.__class__, decimal, 'USD', '840'))
        assert us_dollar_pa.__repr__() == (
            'USDollarPA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PA$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pa.__str__() == '$0.14'

    def test_us_dollar_pa_negative(self):
        """test_us_dollar_pa_negative."""
        amount = -100
        us_dollar_pa = USDollarPA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pa.numeric_code == '840'
        assert us_dollar_pa.alpha_code == 'USD'
        assert us_dollar_pa.decimal_places == 2
        assert us_dollar_pa.decimal_sign == '.'
        assert us_dollar_pa.grouping_places == 3
        assert us_dollar_pa.grouping_sign == ','
        assert not us_dollar_pa.international
        assert us_dollar_pa.symbol == '$'
        assert us_dollar_pa.symbol_ahead
        assert us_dollar_pa.symbol_separator == ''
        assert us_dollar_pa.localized_symbol == 'PA$'
        assert us_dollar_pa.convertion == ''
        assert us_dollar_pa.__hash__() == hash(
            (us_dollar_pa.__class__, decimal, 'USD', '840'))
        assert us_dollar_pa.__repr__() == (
            'USDollarPA(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PA$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pa.__str__() == '$-100.00'

    def test_us_dollar_pa_custom(self):
        """test_us_dollar_pa_custom."""
        amount = 1000
        us_dollar_pa = USDollarPA(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pa.amount == decimal
        assert us_dollar_pa.numeric_code == '840'
        assert us_dollar_pa.alpha_code == 'USD'
        assert us_dollar_pa.decimal_places == 5
        assert us_dollar_pa.decimal_sign == ','
        assert us_dollar_pa.grouping_places == 2
        assert us_dollar_pa.grouping_sign == '.'
        assert us_dollar_pa.international
        assert us_dollar_pa.symbol == '$'
        assert not us_dollar_pa.symbol_ahead
        assert us_dollar_pa.symbol_separator == '_'
        assert us_dollar_pa.localized_symbol == 'PA$'
        assert us_dollar_pa.convertion == ''
        assert us_dollar_pa.__hash__() == hash(
            (us_dollar_pa.__class__, decimal, 'USD', '840'))
        assert us_dollar_pa.__repr__() == (
            'USDollarPA(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PA$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_pa.__str__() == 'USD 10,00.00000'

    def test_us_dollar_pa_changed(self):
        """test_cus_dollar_pa_changed."""
        us_dollar_pa = USDollarPA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pa.international = True

    def test_us_dollar_pa_math_add(self):
        """test_us_dollar_pa_math_add."""
        us_dollar_pa_one = USDollarPA(amount=1)
        us_dollar_pa_two = USDollarPA(amount=2)
        us_dollar_pa_three = USDollarPA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_pa_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarPA\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_pa_one.__add__('1.00')
        assert (
            us_dollar_pa_one +
            us_dollar_pa_two) == us_dollar_pa_three

    def test_us_dollar_pa_slots(self):
        """test_us_dollar_pa_slots."""
        us_dollar_pa = USDollarPA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarPA\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_pa.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar PR representation."""

from multicurrency import USDollarPR


class TestUSDollarPR:
    """USDollarPR currency tests."""

    def test_us_dollar_pr(self):
        """test_us_dollar_pr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_pr = USDollarPR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pr.amount == decimal
        assert us_dollar_pr.numeric_code == '840'
        assert us_dollar_pr.alpha_code == 'USD'
        assert us_dollar_pr.decimal_places == 2
        assert us_dollar_pr.decimal_sign == '.'
        assert us_dollar_pr.grouping_places == 3
        assert us_dollar_pr.grouping_sign == ','
        assert not us_dollar_pr.international
        assert us_dollar_pr.symbol == '$'
        assert us_dollar_pr.symbol_ahead
        assert us_dollar_pr.symbol_separator == ''
        assert us_dollar_pr.localized_symbol == 'PR$'
        assert us_dollar_pr.convertion == ''
        assert us_dollar_pr.__hash__() == hash(
            (us_dollar_pr.__class__, decimal, 'USD', '840'))
        assert us_dollar_pr.__repr__() == (
            'USDollarPR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PR$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pr.__str__() == '$0.14'

    def test_us_dollar_pr_negative(self):
        """test_us_dollar_pr_negative."""
        amount = -100
        us_dollar_pr = USDollarPR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pr.numeric_code == '840'
        assert us_dollar_pr.alpha_code == 'USD'
        assert us_dollar_pr.decimal_places == 2
        assert us_dollar_pr.decimal_sign == '.'
        assert us_dollar_pr.grouping_places == 3
        assert us_dollar_pr.grouping_sign == ','
        assert not us_dollar_pr.international
        assert us_dollar_pr.symbol == '$'
        assert us_dollar_pr.symbol_ahead
        assert us_dollar_pr.symbol_separator == ''
        assert us_dollar_pr.localized_symbol == 'PR$'
        assert us_dollar_pr.convertion == ''
        assert us_dollar_pr.__hash__() == hash(
            (us_dollar_pr.__class__, decimal, 'USD', '840'))
        assert us_dollar_pr.__repr__() == (
            'USDollarPR(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "PR$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_pr.__str__() == '$-100.00'

    def test_us_dollar_pr_custom(self):
        """test_us_dollar_pr_custom."""
        amount = 1000
        us_dollar_pr = USDollarPR(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_pr.amount == decimal
        assert us_dollar_pr.numeric_code == '840'
        assert us_dollar_pr.alpha_code == 'USD'
        assert us_dollar_pr.decimal_places == 5
        assert us_dollar_pr.decimal_sign == ','
        assert us_dollar_pr.grouping_places == 2
        assert us_dollar_pr.grouping_sign == '.'
        assert us_dollar_pr.international
        assert us_dollar_pr.symbol == '$'
        assert not us_dollar_pr.symbol_ahead
        assert us_dollar_pr.symbol_separator == '_'
        assert us_dollar_pr.localized_symbol == 'PR$'
        assert us_dollar_pr.convertion == ''
        assert us_dollar_pr.__hash__() == hash(
            (us_dollar_pr.__class__, decimal, 'USD', '840'))
        assert us_dollar_pr.__repr__() == (
            'USDollarPR(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PR$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_pr.__str__() == 'USD 10,00.00000'

    def test_us_dollar_pr_changed(self):
        """test_cus_dollar_pr_changed."""
        us_dollar_pr = USDollarPR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_pr.international = True

    def test_us_dollar_pr_math_add(self):
        """test_us_dollar_pr_math_add."""
        us_dollar_pr_one = USDollarPR(amount=1)
        us_dollar_pr_two = USDollarPR(amount=2)
        us_dollar_pr_three = USDollarPR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_pr_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarPR\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_pr_one.__add__('1.00')
        assert (
            us_dollar_pr_one +
            us_dollar_pr_two) == us_dollar_pr_three

    def test_us_dollar_pr_slots(self):
        """test_us_dollar_pr_slots."""
        us_dollar_pr = USDollarPR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarPR\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_pr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar TC representation."""

from multicurrency import USDollarTC


class TestUSDollarTC:
    """USDollarTC currency tests."""

    def test_us_dollar_tc(self):
        """test_us_dollar_tc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_tc = USDollarTC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_tc.amount == decimal
        assert us_dollar_tc.numeric_code == '840'
        assert us_dollar_tc.alpha_code == 'USD'
        assert us_dollar_tc.decimal_places == 2
        assert us_dollar_tc.decimal_sign == '.'
        assert us_dollar_tc.grouping_places == 3
        assert us_dollar_tc.grouping_sign == ','
        assert not us_dollar_tc.international
        assert us_dollar_tc.symbol == '$'
        assert us_dollar_tc.symbol_ahead
        assert us_dollar_tc.symbol_separator == ''
        assert us_dollar_tc.localized_symbol == 'TC$'
        assert us_dollar_tc.convertion == ''
        assert us_dollar_tc.__hash__() == hash(
            (us_dollar_tc.__class__, decimal, 'USD', '840'))
        assert us_dollar_tc.__repr__() == (
            'USDollarTC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TC$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_tc.__str__() == '$0.14'

    def test_us_dollar_tc_negative(self):
        """test_us_dollar_tc_negative."""
        amount = -100
        us_dollar_tc = USDollarTC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_tc.numeric_code == '840'
        assert us_dollar_tc.alpha_code == 'USD'
        assert us_dollar_tc.decimal_places == 2
        assert us_dollar_tc.decimal_sign == '.'
        assert us_dollar_tc.grouping_places == 3
        assert us_dollar_tc.grouping_sign == ','
        assert not us_dollar_tc.international
        assert us_dollar_tc.symbol == '$'
        assert us_dollar_tc.symbol_ahead
        assert us_dollar_tc.symbol_separator == ''
        assert us_dollar_tc.localized_symbol == 'TC$'
        assert us_dollar_tc.convertion == ''
        assert us_dollar_tc.__hash__() == hash(
            (us_dollar_tc.__class__, decimal, 'USD', '840'))
        assert us_dollar_tc.__repr__() == (
            'USDollarTC(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "TC$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_tc.__str__() == '$-100.00'

    def test_us_dollar_tc_custom(self):
        """test_us_dollar_tc_custom."""
        amount = 1000
        us_dollar_tc = USDollarTC(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_tc.amount == decimal
        assert us_dollar_tc.numeric_code == '840'
        assert us_dollar_tc.alpha_code == 'USD'
        assert us_dollar_tc.decimal_places == 5
        assert us_dollar_tc.decimal_sign == ','
        assert us_dollar_tc.grouping_places == 2
        assert us_dollar_tc.grouping_sign == '.'
        assert us_dollar_tc.international
        assert us_dollar_tc.symbol == '$'
        assert not us_dollar_tc.symbol_ahead
        assert us_dollar_tc.symbol_separator == '_'
        assert us_dollar_tc.localized_symbol == 'TC$'
        assert us_dollar_tc.convertion == ''
        assert us_dollar_tc.__hash__() == hash(
            (us_dollar_tc.__class__, decimal, 'USD', '840'))
        assert us_dollar_tc.__repr__() == (
            'USDollarTC(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TC$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_tc.__str__() == 'USD 10,00.00000'

    def test_us_dollar_tc_changed(self):
        """test_cus_dollar_tc_changed."""
        us_dollar_tc = USDollarTC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_tc.international = True

    def test_us_dollar_tc_math_add(self):
        """test_us_dollar_tc_math_add."""
        us_dollar_tc_one = USDollarTC(amount=1)
        us_dollar_tc_two = USDollarTC(amount=2)
        us_dollar_tc_three = USDollarTC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_tc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarTC\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_tc_one.__add__('1.00')
        assert (
            us_dollar_tc_one +
            us_dollar_tc_two) == us_dollar_tc_three

    def test_us_dollar_tc_slots(self):
        """test_us_dollar_tc_slots."""
        us_dollar_tc = USDollarTC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarTC\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_tc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the US Dollar VI representation."""

from multicurrency import USDollarVI


class TestUSDollarVI:
    """USDollarVI currency tests."""

    def test_us_dollar_vi(self):
        """test_us_dollar_vi."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        us_dollar_vi = USDollarVI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vi.amount == decimal
        assert us_dollar_vi.numeric_code == '840'
        assert us_dollar_vi.alpha_code == 'USD'
        assert us_dollar_vi.decimal_places == 2
        assert us_dollar_vi.decimal_sign == '.'
        assert us_dollar_vi.grouping_places == 3
        assert us_dollar_vi.grouping_sign == ','
        assert not us_dollar_vi.international
        assert us_dollar_vi.symbol == '$'
        assert us_dollar_vi.symbol_ahead
        assert us_dollar_vi.symbol_separator == ''
        assert us_dollar_vi.localized_symbol == 'VI$'
        assert us_dollar_vi.convertion == ''
        assert us_dollar_vi.__hash__() == hash(
            (us_dollar_vi.__class__, decimal, 'USD', '840'))
        assert us_dollar_vi.__repr__() == (
            'USDollarVI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VI$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_vi.__str__() == '$0.14'

    def test_us_dollar_vi_negative(self):
        """test_us_dollar_vi_negative."""
        amount = -100
        us_dollar_vi = USDollarVI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vi.numeric_code == '840'
        assert us_dollar_vi.alpha_code == 'USD'
        assert us_dollar_vi.decimal_places == 2
        assert us_dollar_vi.decimal_sign == '.'
        assert us_dollar_vi.grouping_places == 3
        assert us_dollar_vi.grouping_sign == ','
        assert not us_dollar_vi.international
        assert us_dollar_vi.symbol == '$'
        assert us_dollar_vi.symbol_ahead
        assert us_dollar_vi.symbol_separator == ''
        assert us_dollar_vi.localized_symbol == 'VI$'
        assert us_dollar_vi.convertion == ''
        assert us_dollar_vi.__hash__() == hash(
            (us_dollar_vi.__class__, decimal, 'USD', '840'))
        assert us_dollar_vi.__repr__() == (
            'USDollarVI(amount: -100, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VI$", '
            'numeric_code: "840", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert us_dollar_vi.__str__() == '$-100.00'

    def test_us_dollar_vi_custom(self):
        """test_us_dollar_vi_custom."""
        amount = 1000
        us_dollar_vi = USDollarVI(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert us_dollar_vi.amount == decimal
        assert us_dollar_vi.numeric_code == '840'
        assert us_dollar_vi.alpha_code == 'USD'
        assert us_dollar_vi.decimal_places == 5
        assert us_dollar_vi.decimal_sign == ','
        assert us_dollar_vi.grouping_places == 2
        assert us_dollar_vi.grouping_sign == '.'
        assert us_dollar_vi.international
        assert us_dollar_vi.symbol == '$'
        assert not us_dollar_vi.symbol_ahead
        assert us_dollar_vi.symbol_separator == '_'
        assert us_dollar_vi.localized_symbol == 'VI$'
        assert us_dollar_vi.convertion == ''
        assert us_dollar_vi.__hash__() == hash(
            (us_dollar_vi.__class__, decimal, 'USD', '840'))
        assert us_dollar_vi.__repr__() == (
            'USDollarVI(amount: 1000, '
            'alpha_code: "USD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "VI$", '
            'numeric_code: "840", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert us_dollar_vi.__str__() == 'USD 10,00.00000'

    def test_us_dollar_vi_changed(self):
        """test_cus_dollar_vi_changed."""
        us_dollar_vi = USDollarVI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            us_dollar_vi.international = True

    def test_us_dollar_vi_math_add(self):
        """test_us_dollar_vi_math_add."""
        us_dollar_vi_one = USDollarVI(amount=1)
        us_dollar_vi_two = USDollarVI(amount=2)
        us_dollar_vi_three = USDollarVI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency USD and OTHER.'):
            _ = us_dollar_vi_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.USDollarVI\'> '
                    'and <class \'str\'>.')):
            _ = us_dollar_vi_one.__add__('1.00')
        assert (
            us_dollar_vi_one +
            us_dollar_vi_two) == us_dollar_vi_three

    def test_us_dollar_vi_slots(self):
        """test_us_dollar_vi_slots."""
        us_dollar_vi = USDollarVI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'USDollarVI\' '
                    'object has no attribute \'new_variable\'')):
            us_dollar_vi.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar representation."""

from multicurrency import EasternCaribbeanDollar


class TestEasternCaribbeanDollar:
    """EasternCaribbeanDollar currency tests."""

    def test_eastern_caribbean_dollar(self):
        """test_eastern_caribbean_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar = EasternCaribbeanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar.amount == decimal
        assert eastern_caribbean_dollar.numeric_code == '951'
        assert eastern_caribbean_dollar.alpha_code == 'XCD'
        assert eastern_caribbean_dollar.decimal_places == 2
        assert eastern_caribbean_dollar.decimal_sign == '.'
        assert eastern_caribbean_dollar.grouping_places == 3
        assert eastern_caribbean_dollar.grouping_sign == ','
        assert not eastern_caribbean_dollar.international
        assert eastern_caribbean_dollar.symbol == '$'
        assert eastern_caribbean_dollar.symbol_ahead
        assert eastern_caribbean_dollar.symbol_separator == ''
        assert eastern_caribbean_dollar.localized_symbol == '$'
        assert eastern_caribbean_dollar.convertion == ''
        assert eastern_caribbean_dollar.__hash__() == hash(
            (eastern_caribbean_dollar.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar.__repr__() == (
            'EasternCaribbeanDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_negative(self):
        """test_eastern_caribbean_dollar_negative."""
        amount = -100
        eastern_caribbean_dollar = EasternCaribbeanDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar.numeric_code == '951'
        assert eastern_caribbean_dollar.alpha_code == 'XCD'
        assert eastern_caribbean_dollar.decimal_places == 2
        assert eastern_caribbean_dollar.decimal_sign == '.'
        assert eastern_caribbean_dollar.grouping_places == 3
        assert eastern_caribbean_dollar.grouping_sign == ','
        assert not eastern_caribbean_dollar.international
        assert eastern_caribbean_dollar.symbol == '$'
        assert eastern_caribbean_dollar.symbol_ahead
        assert eastern_caribbean_dollar.symbol_separator == ''
        assert eastern_caribbean_dollar.localized_symbol == '$'
        assert eastern_caribbean_dollar.convertion == ''
        assert eastern_caribbean_dollar.__hash__() == hash(
            (eastern_caribbean_dollar.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar.__repr__() == (
            'EasternCaribbeanDollar(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_custom(self):
        """test_eastern_caribbean_dollar_custom."""
        amount = 1000
        eastern_caribbean_dollar = EasternCaribbeanDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar.amount == decimal
        assert eastern_caribbean_dollar.numeric_code == '951'
        assert eastern_caribbean_dollar.alpha_code == 'XCD'
        assert eastern_caribbean_dollar.decimal_places == 5
        assert eastern_caribbean_dollar.decimal_sign == ','
        assert eastern_caribbean_dollar.grouping_places == 2
        assert eastern_caribbean_dollar.grouping_sign == '.'
        assert eastern_caribbean_dollar.international
        assert eastern_caribbean_dollar.symbol == '$'
        assert not eastern_caribbean_dollar.symbol_ahead
        assert eastern_caribbean_dollar.symbol_separator == '_'
        assert eastern_caribbean_dollar.localized_symbol == '$'
        assert eastern_caribbean_dollar.convertion == ''
        assert eastern_caribbean_dollar.__hash__() == hash(
            (eastern_caribbean_dollar.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar.__repr__() == (
            'EasternCaribbeanDollar(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_changed(self):
        """test_ceastern_caribbean_dollar_changed."""
        eastern_caribbean_dollar = EasternCaribbeanDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar.international = True

    def test_eastern_caribbean_dollar_math_add(self):
        """test_eastern_caribbean_dollar_math_add."""
        eastern_caribbean_dollar_one = EasternCaribbeanDollar(amount=1)
        eastern_caribbean_dollar_two = EasternCaribbeanDollar(amount=2)
        eastern_caribbean_dollar_three = EasternCaribbeanDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollar\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_one +
            eastern_caribbean_dollar_two) == eastern_caribbean_dollar_three

    def test_eastern_caribbean_dollar_slots(self):
        """test_eastern_caribbean_dollar_slots."""
        eastern_caribbean_dollar = EasternCaribbeanDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollar\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar AI representation."""

from multicurrency import EasternCaribbeanDollarAI


class TestEasternCaribbeanDollarAI:
    """EasternCaribbeanDollarAI currency tests."""

    def test_eastern_caribbean_dollar_ai(self):
        """test_eastern_caribbean_dollar_ai."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ai.amount == decimal
        assert eastern_caribbean_dollar_ai.numeric_code == '951'
        assert eastern_caribbean_dollar_ai.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ai.decimal_places == 2
        assert eastern_caribbean_dollar_ai.decimal_sign == '.'
        assert eastern_caribbean_dollar_ai.grouping_places == 3
        assert eastern_caribbean_dollar_ai.grouping_sign == ','
        assert not eastern_caribbean_dollar_ai.international
        assert eastern_caribbean_dollar_ai.symbol == '$'
        assert eastern_caribbean_dollar_ai.symbol_ahead
        assert eastern_caribbean_dollar_ai.symbol_separator == ''
        assert eastern_caribbean_dollar_ai.localized_symbol == 'AI$'
        assert eastern_caribbean_dollar_ai.convertion == ''
        assert eastern_caribbean_dollar_ai.__hash__() == hash(
            (eastern_caribbean_dollar_ai.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ai.__repr__() == (
            'EasternCaribbeanDollarAI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AI$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ai.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_ai_negative(self):
        """test_eastern_caribbean_dollar_ai_negative."""
        amount = -100
        eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ai.numeric_code == '951'
        assert eastern_caribbean_dollar_ai.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ai.decimal_places == 2
        assert eastern_caribbean_dollar_ai.decimal_sign == '.'
        assert eastern_caribbean_dollar_ai.grouping_places == 3
        assert eastern_caribbean_dollar_ai.grouping_sign == ','
        assert not eastern_caribbean_dollar_ai.international
        assert eastern_caribbean_dollar_ai.symbol == '$'
        assert eastern_caribbean_dollar_ai.symbol_ahead
        assert eastern_caribbean_dollar_ai.symbol_separator == ''
        assert eastern_caribbean_dollar_ai.localized_symbol == 'AI$'
        assert eastern_caribbean_dollar_ai.convertion == ''
        assert eastern_caribbean_dollar_ai.__hash__() == hash(
            (eastern_caribbean_dollar_ai.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ai.__repr__() == (
            'EasternCaribbeanDollarAI(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AI$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ai.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_ai_custom(self):
        """test_eastern_caribbean_dollar_ai_custom."""
        amount = 1000
        eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ai.amount == decimal
        assert eastern_caribbean_dollar_ai.numeric_code == '951'
        assert eastern_caribbean_dollar_ai.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ai.decimal_places == 5
        assert eastern_caribbean_dollar_ai.decimal_sign == ','
        assert eastern_caribbean_dollar_ai.grouping_places == 2
        assert eastern_caribbean_dollar_ai.grouping_sign == '.'
        assert eastern_caribbean_dollar_ai.international
        assert eastern_caribbean_dollar_ai.symbol == '$'
        assert not eastern_caribbean_dollar_ai.symbol_ahead
        assert eastern_caribbean_dollar_ai.symbol_separator == '_'
        assert eastern_caribbean_dollar_ai.localized_symbol == 'AI$'
        assert eastern_caribbean_dollar_ai.convertion == ''
        assert eastern_caribbean_dollar_ai.__hash__() == hash(
            (eastern_caribbean_dollar_ai.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ai.__repr__() == (
            'EasternCaribbeanDollarAI(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AI$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_ai.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_ai_changed(self):
        """test_ceastern_caribbean_dollar_ai_changed."""
        eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ai.international = True

    def test_eastern_caribbean_dollar_ai_math_add(self):
        """test_eastern_caribbean_dollar_ai_math_add."""
        eastern_caribbean_dollar_ai_one = EasternCaribbeanDollarAI(amount=1)
        eastern_caribbean_dollar_ai_two = EasternCaribbeanDollarAI(amount=2)
        eastern_caribbean_dollar_ai_three = EasternCaribbeanDollarAI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_ai_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarAI\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_ai_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_ai_one +
            eastern_caribbean_dollar_ai_two) == eastern_caribbean_dollar_ai_three

    def test_eastern_caribbean_dollar_ai_slots(self):
        """test_eastern_caribbean_dollar_ai_slots."""
        eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarAI\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_ai.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar AG representation."""

from multicurrency import EasternCaribbeanDollarAG


class TestEasternCaribbeanDollarAG:
    """EasternCaribbeanDollarAG currency tests."""

    def test_eastern_caribbean_dollar_ag(self):
        """test_eastern_caribbean_dollar_ag."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ag.amount == decimal
        assert eastern_caribbean_dollar_ag.numeric_code == '951'
        assert eastern_caribbean_dollar_ag.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ag.decimal_places == 2
        assert eastern_caribbean_dollar_ag.decimal_sign == '.'
        assert eastern_caribbean_dollar_ag.grouping_places == 3
        assert eastern_caribbean_dollar_ag.grouping_sign == ','
        assert not eastern_caribbean_dollar_ag.international
        assert eastern_caribbean_dollar_ag.symbol == '$'
        assert eastern_caribbean_dollar_ag.symbol_ahead
        assert eastern_caribbean_dollar_ag.symbol_separator == ''
        assert eastern_caribbean_dollar_ag.localized_symbol == 'AG$'
        assert eastern_caribbean_dollar_ag.convertion == ''
        assert eastern_caribbean_dollar_ag.__hash__() == hash(
            (eastern_caribbean_dollar_ag.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ag.__repr__() == (
            'EasternCaribbeanDollarAG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AG$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ag.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_ag_negative(self):
        """test_eastern_caribbean_dollar_ag_negative."""
        amount = -100
        eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ag.numeric_code == '951'
        assert eastern_caribbean_dollar_ag.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ag.decimal_places == 2
        assert eastern_caribbean_dollar_ag.decimal_sign == '.'
        assert eastern_caribbean_dollar_ag.grouping_places == 3
        assert eastern_caribbean_dollar_ag.grouping_sign == ','
        assert not eastern_caribbean_dollar_ag.international
        assert eastern_caribbean_dollar_ag.symbol == '$'
        assert eastern_caribbean_dollar_ag.symbol_ahead
        assert eastern_caribbean_dollar_ag.symbol_separator == ''
        assert eastern_caribbean_dollar_ag.localized_symbol == 'AG$'
        assert eastern_caribbean_dollar_ag.convertion == ''
        assert eastern_caribbean_dollar_ag.__hash__() == hash(
            (eastern_caribbean_dollar_ag.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ag.__repr__() == (
            'EasternCaribbeanDollarAG(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "AG$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ag.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_ag_custom(self):
        """test_eastern_caribbean_dollar_ag_custom."""
        amount = 1000
        eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ag.amount == decimal
        assert eastern_caribbean_dollar_ag.numeric_code == '951'
        assert eastern_caribbean_dollar_ag.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ag.decimal_places == 5
        assert eastern_caribbean_dollar_ag.decimal_sign == ','
        assert eastern_caribbean_dollar_ag.grouping_places == 2
        assert eastern_caribbean_dollar_ag.grouping_sign == '.'
        assert eastern_caribbean_dollar_ag.international
        assert eastern_caribbean_dollar_ag.symbol == '$'
        assert not eastern_caribbean_dollar_ag.symbol_ahead
        assert eastern_caribbean_dollar_ag.symbol_separator == '_'
        assert eastern_caribbean_dollar_ag.localized_symbol == 'AG$'
        assert eastern_caribbean_dollar_ag.convertion == ''
        assert eastern_caribbean_dollar_ag.__hash__() == hash(
            (eastern_caribbean_dollar_ag.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ag.__repr__() == (
            'EasternCaribbeanDollarAG(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AG$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_ag.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_ag_changed(self):
        """test_ceastern_caribbean_dollar_ag_changed."""
        eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ag.international = True

    def test_eastern_caribbean_dollar_ag_math_add(self):
        """test_eastern_caribbean_dollar_ag_math_add."""
        eastern_caribbean_dollar_ag_one = EasternCaribbeanDollarAG(amount=1)
        eastern_caribbean_dollar_ag_two = EasternCaribbeanDollarAG(amount=2)
        eastern_caribbean_dollar_ag_three = EasternCaribbeanDollarAG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_ag_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarAG\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_ag_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_ag_one +
            eastern_caribbean_dollar_ag_two) == eastern_caribbean_dollar_ag_three

    def test_eastern_caribbean_dollar_ag_slots(self):
        """test_eastern_caribbean_dollar_ag_slots."""
        eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarAG\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_ag.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar DM representation."""

from multicurrency import EasternCaribbeanDollarDM


class TestEasternCaribbeanDollarDM:
    """EasternCaribbeanDollarDM currency tests."""

    def test_eastern_caribbean_dollar_dm(self):
        """test_eastern_caribbean_dollar_dm."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_dm.amount == decimal
        assert eastern_caribbean_dollar_dm.numeric_code == '951'
        assert eastern_caribbean_dollar_dm.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_dm.decimal_places == 2
        assert eastern_caribbean_dollar_dm.decimal_sign == '.'
        assert eastern_caribbean_dollar_dm.grouping_places == 3
        assert eastern_caribbean_dollar_dm.grouping_sign == ','
        assert not eastern_caribbean_dollar_dm.international
        assert eastern_caribbean_dollar_dm.symbol == '$'
        assert eastern_caribbean_dollar_dm.symbol_ahead
        assert eastern_caribbean_dollar_dm.symbol_separator == ''
        assert eastern_caribbean_dollar_dm.localized_symbol == 'DM$'
        assert eastern_caribbean_dollar_dm.convertion == ''
        assert eastern_caribbean_dollar_dm.__hash__() == hash(
            (eastern_caribbean_dollar_dm.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_dm.__repr__() == (
            'EasternCaribbeanDollarDM(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "DM$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_dm.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_dm_negative(self):
        """test_eastern_caribbean_dollar_dm_negative."""
        amount = -100
        eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_dm.numeric_code == '951'
        assert eastern_caribbean_dollar_dm.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_dm.decimal_places == 2
        assert eastern_caribbean_dollar_dm.decimal_sign == '.'
        assert eastern_caribbean_dollar_dm.grouping_places == 3
        assert eastern_caribbean_dollar_dm.grouping_sign == ','
        assert not eastern_caribbean_dollar_dm.international
        assert eastern_caribbean_dollar_dm.symbol == '$'
        assert eastern_caribbean_dollar_dm.symbol_ahead
        assert eastern_caribbean_dollar_dm.symbol_separator == ''
        assert eastern_caribbean_dollar_dm.localized_symbol == 'DM$'
        assert eastern_caribbean_dollar_dm.convertion == ''
        assert eastern_caribbean_dollar_dm.__hash__() == hash(
            (eastern_caribbean_dollar_dm.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_dm.__repr__() == (
            'EasternCaribbeanDollarDM(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "DM$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_dm.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_dm_custom(self):
        """test_eastern_caribbean_dollar_dm_custom."""
        amount = 1000
        eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_dm.amount == decimal
        assert eastern_caribbean_dollar_dm.numeric_code == '951'
        assert eastern_caribbean_dollar_dm.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_dm.decimal_places == 5
        assert eastern_caribbean_dollar_dm.decimal_sign == ','
        assert eastern_caribbean_dollar_dm.grouping_places == 2
        assert eastern_caribbean_dollar_dm.grouping_sign == '.'
        assert eastern_caribbean_dollar_dm.international
        assert eastern_caribbean_dollar_dm.symbol == '$'
        assert not eastern_caribbean_dollar_dm.symbol_ahead
        assert eastern_caribbean_dollar_dm.symbol_separator == '_'
        assert eastern_caribbean_dollar_dm.localized_symbol == 'DM$'
        assert eastern_caribbean_dollar_dm.convertion == ''
        assert eastern_caribbean_dollar_dm.__hash__() == hash(
            (eastern_caribbean_dollar_dm.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_dm.__repr__() == (
            'EasternCaribbeanDollarDM(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "DM$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_dm.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_dm_changed(self):
        """test_ceastern_caribbean_dollar_dm_changed."""
        eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_dm.international = True

    def test_eastern_caribbean_dollar_dm_math_add(self):
        """test_eastern_caribbean_dollar_dm_math_add."""
        eastern_caribbean_dollar_dm_one = EasternCaribbeanDollarDM(amount=1)
        eastern_caribbean_dollar_dm_two = EasternCaribbeanDollarDM(amount=2)
        eastern_caribbean_dollar_dm_three = EasternCaribbeanDollarDM(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_dm_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarDM\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_dm_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_dm_one +
            eastern_caribbean_dollar_dm_two) == eastern_caribbean_dollar_dm_three

    def test_eastern_caribbean_dollar_dm_slots(self):
        """test_eastern_caribbean_dollar_dm_slots."""
        eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarDM\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_dm.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar GD representation."""

from multicurrency import EasternCaribbeanDollarGD


class TestEasternCaribbeanDollarGD:
    """EasternCaribbeanDollarGD currency tests."""

    def test_eastern_caribbean_dollar_gd(self):
        """test_eastern_caribbean_dollar_gd."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_gd.amount == decimal
        assert eastern_caribbean_dollar_gd.numeric_code == '951'
        assert eastern_caribbean_dollar_gd.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_gd.decimal_places == 2
        assert eastern_caribbean_dollar_gd.decimal_sign == '.'
        assert eastern_caribbean_dollar_gd.grouping_places == 3
        assert eastern_caribbean_dollar_gd.grouping_sign == ','
        assert not eastern_caribbean_dollar_gd.international
        assert eastern_caribbean_dollar_gd.symbol == '$'
        assert eastern_caribbean_dollar_gd.symbol_ahead
        assert eastern_caribbean_dollar_gd.symbol_separator == ''
        assert eastern_caribbean_dollar_gd.localized_symbol == 'GD$'
        assert eastern_caribbean_dollar_gd.convertion == ''
        assert eastern_caribbean_dollar_gd.__hash__() == hash(
            (eastern_caribbean_dollar_gd.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_gd.__repr__() == (
            'EasternCaribbeanDollarGD(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GD$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_gd.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_gd_negative(self):
        """test_eastern_caribbean_dollar_gd_negative."""
        amount = -100
        eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_gd.numeric_code == '951'
        assert eastern_caribbean_dollar_gd.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_gd.decimal_places == 2
        assert eastern_caribbean_dollar_gd.decimal_sign == '.'
        assert eastern_caribbean_dollar_gd.grouping_places == 3
        assert eastern_caribbean_dollar_gd.grouping_sign == ','
        assert not eastern_caribbean_dollar_gd.international
        assert eastern_caribbean_dollar_gd.symbol == '$'
        assert eastern_caribbean_dollar_gd.symbol_ahead
        assert eastern_caribbean_dollar_gd.symbol_separator == ''
        assert eastern_caribbean_dollar_gd.localized_symbol == 'GD$'
        assert eastern_caribbean_dollar_gd.convertion == ''
        assert eastern_caribbean_dollar_gd.__hash__() == hash(
            (eastern_caribbean_dollar_gd.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_gd.__repr__() == (
            'EasternCaribbeanDollarGD(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "GD$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_gd.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_gd_custom(self):
        """test_eastern_caribbean_dollar_gd_custom."""
        amount = 1000
        eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_gd.amount == decimal
        assert eastern_caribbean_dollar_gd.numeric_code == '951'
        assert eastern_caribbean_dollar_gd.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_gd.decimal_places == 5
        assert eastern_caribbean_dollar_gd.decimal_sign == ','
        assert eastern_caribbean_dollar_gd.grouping_places == 2
        assert eastern_caribbean_dollar_gd.grouping_sign == '.'
        assert eastern_caribbean_dollar_gd.international
        assert eastern_caribbean_dollar_gd.symbol == '$'
        assert not eastern_caribbean_dollar_gd.symbol_ahead
        assert eastern_caribbean_dollar_gd.symbol_separator == '_'
        assert eastern_caribbean_dollar_gd.localized_symbol == 'GD$'
        assert eastern_caribbean_dollar_gd.convertion == ''
        assert eastern_caribbean_dollar_gd.__hash__() == hash(
            (eastern_caribbean_dollar_gd.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_gd.__repr__() == (
            'EasternCaribbeanDollarGD(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GD$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_gd.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_gd_changed(self):
        """test_ceastern_caribbean_dollar_gd_changed."""
        eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_gd.international = True

    def test_eastern_caribbean_dollar_gd_math_add(self):
        """test_eastern_caribbean_dollar_gd_math_add."""
        eastern_caribbean_dollar_gd_one = EasternCaribbeanDollarGD(amount=1)
        eastern_caribbean_dollar_gd_two = EasternCaribbeanDollarGD(amount=2)
        eastern_caribbean_dollar_gd_three = EasternCaribbeanDollarGD(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_gd_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarGD\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_gd_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_gd_one +
            eastern_caribbean_dollar_gd_two) == eastern_caribbean_dollar_gd_three

    def test_eastern_caribbean_dollar_gd_slots(self):
        """test_eastern_caribbean_dollar_gd_slots."""
        eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarGD\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_gd.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar MS representation."""

from multicurrency import EasternCaribbeanDollarMS


class TestEasternCaribbeanDollarMS:
    """EasternCaribbeanDollarMS currency tests."""

    def test_eastern_caribbean_dollar_ms(self):
        """test_eastern_caribbean_dollar_ms."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ms.amount == decimal
        assert eastern_caribbean_dollar_ms.numeric_code == '951'
        assert eastern_caribbean_dollar_ms.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ms.decimal_places == 2
        assert eastern_caribbean_dollar_ms.decimal_sign == '.'
        assert eastern_caribbean_dollar_ms.grouping_places == 3
        assert eastern_caribbean_dollar_ms.grouping_sign == ','
        assert not eastern_caribbean_dollar_ms.international
        assert eastern_caribbean_dollar_ms.symbol == '$'
        assert eastern_caribbean_dollar_ms.symbol_ahead
        assert eastern_caribbean_dollar_ms.symbol_separator == ''
        assert eastern_caribbean_dollar_ms.localized_symbol == 'MS$'
        assert eastern_caribbean_dollar_ms.convertion == ''
        assert eastern_caribbean_dollar_ms.__hash__() == hash(
            (eastern_caribbean_dollar_ms.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ms.__repr__() == (
            'EasternCaribbeanDollarMS(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MS$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ms.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_ms_negative(self):
        """test_eastern_caribbean_dollar_ms_negative."""
        amount = -100
        eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ms.numeric_code == '951'
        assert eastern_caribbean_dollar_ms.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ms.decimal_places == 2
        assert eastern_caribbean_dollar_ms.decimal_sign == '.'
        assert eastern_caribbean_dollar_ms.grouping_places == 3
        assert eastern_caribbean_dollar_ms.grouping_sign == ','
        assert not eastern_caribbean_dollar_ms.international
        assert eastern_caribbean_dollar_ms.symbol == '$'
        assert eastern_caribbean_dollar_ms.symbol_ahead
        assert eastern_caribbean_dollar_ms.symbol_separator == ''
        assert eastern_caribbean_dollar_ms.localized_symbol == 'MS$'
        assert eastern_caribbean_dollar_ms.convertion == ''
        assert eastern_caribbean_dollar_ms.__hash__() == hash(
            (eastern_caribbean_dollar_ms.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ms.__repr__() == (
            'EasternCaribbeanDollarMS(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MS$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_ms.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_ms_custom(self):
        """test_eastern_caribbean_dollar_ms_custom."""
        amount = 1000
        eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_ms.amount == decimal
        assert eastern_caribbean_dollar_ms.numeric_code == '951'
        assert eastern_caribbean_dollar_ms.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_ms.decimal_places == 5
        assert eastern_caribbean_dollar_ms.decimal_sign == ','
        assert eastern_caribbean_dollar_ms.grouping_places == 2
        assert eastern_caribbean_dollar_ms.grouping_sign == '.'
        assert eastern_caribbean_dollar_ms.international
        assert eastern_caribbean_dollar_ms.symbol == '$'
        assert not eastern_caribbean_dollar_ms.symbol_ahead
        assert eastern_caribbean_dollar_ms.symbol_separator == '_'
        assert eastern_caribbean_dollar_ms.localized_symbol == 'MS$'
        assert eastern_caribbean_dollar_ms.convertion == ''
        assert eastern_caribbean_dollar_ms.__hash__() == hash(
            (eastern_caribbean_dollar_ms.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_ms.__repr__() == (
            'EasternCaribbeanDollarMS(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MS$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_ms.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_ms_changed(self):
        """test_ceastern_caribbean_dollar_ms_changed."""
        eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_ms.international = True

    def test_eastern_caribbean_dollar_ms_math_add(self):
        """test_eastern_caribbean_dollar_ms_math_add."""
        eastern_caribbean_dollar_ms_one = EasternCaribbeanDollarMS(amount=1)
        eastern_caribbean_dollar_ms_two = EasternCaribbeanDollarMS(amount=2)
        eastern_caribbean_dollar_ms_three = EasternCaribbeanDollarMS(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_ms_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarMS\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_ms_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_ms_one +
            eastern_caribbean_dollar_ms_two) == eastern_caribbean_dollar_ms_three

    def test_eastern_caribbean_dollar_ms_slots(self):
        """test_eastern_caribbean_dollar_ms_slots."""
        eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarMS\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_ms.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar KN representation."""

from multicurrency import EasternCaribbeanDollarKN


class TestEasternCaribbeanDollarKN:
    """EasternCaribbeanDollarKN currency tests."""

    def test_eastern_caribbean_dollar_kn(self):
        """test_eastern_caribbean_dollar_kn."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_kn.amount == decimal
        assert eastern_caribbean_dollar_kn.numeric_code == '951'
        assert eastern_caribbean_dollar_kn.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_kn.decimal_places == 2
        assert eastern_caribbean_dollar_kn.decimal_sign == '.'
        assert eastern_caribbean_dollar_kn.grouping_places == 3
        assert eastern_caribbean_dollar_kn.grouping_sign == ','
        assert not eastern_caribbean_dollar_kn.international
        assert eastern_caribbean_dollar_kn.symbol == '$'
        assert eastern_caribbean_dollar_kn.symbol_ahead
        assert eastern_caribbean_dollar_kn.symbol_separator == ''
        assert eastern_caribbean_dollar_kn.localized_symbol == 'KN$'
        assert eastern_caribbean_dollar_kn.convertion == ''
        assert eastern_caribbean_dollar_kn.__hash__() == hash(
            (eastern_caribbean_dollar_kn.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_kn.__repr__() == (
            'EasternCaribbeanDollarKN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KN$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_kn.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_kn_negative(self):
        """test_eastern_caribbean_dollar_kn_negative."""
        amount = -100
        eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_kn.numeric_code == '951'
        assert eastern_caribbean_dollar_kn.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_kn.decimal_places == 2
        assert eastern_caribbean_dollar_kn.decimal_sign == '.'
        assert eastern_caribbean_dollar_kn.grouping_places == 3
        assert eastern_caribbean_dollar_kn.grouping_sign == ','
        assert not eastern_caribbean_dollar_kn.international
        assert eastern_caribbean_dollar_kn.symbol == '$'
        assert eastern_caribbean_dollar_kn.symbol_ahead
        assert eastern_caribbean_dollar_kn.symbol_separator == ''
        assert eastern_caribbean_dollar_kn.localized_symbol == 'KN$'
        assert eastern_caribbean_dollar_kn.convertion == ''
        assert eastern_caribbean_dollar_kn.__hash__() == hash(
            (eastern_caribbean_dollar_kn.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_kn.__repr__() == (
            'EasternCaribbeanDollarKN(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "KN$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_kn.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_kn_custom(self):
        """test_eastern_caribbean_dollar_kn_custom."""
        amount = 1000
        eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_kn.amount == decimal
        assert eastern_caribbean_dollar_kn.numeric_code == '951'
        assert eastern_caribbean_dollar_kn.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_kn.decimal_places == 5
        assert eastern_caribbean_dollar_kn.decimal_sign == ','
        assert eastern_caribbean_dollar_kn.grouping_places == 2
        assert eastern_caribbean_dollar_kn.grouping_sign == '.'
        assert eastern_caribbean_dollar_kn.international
        assert eastern_caribbean_dollar_kn.symbol == '$'
        assert not eastern_caribbean_dollar_kn.symbol_ahead
        assert eastern_caribbean_dollar_kn.symbol_separator == '_'
        assert eastern_caribbean_dollar_kn.localized_symbol == 'KN$'
        assert eastern_caribbean_dollar_kn.convertion == ''
        assert eastern_caribbean_dollar_kn.__hash__() == hash(
            (eastern_caribbean_dollar_kn.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_kn.__repr__() == (
            'EasternCaribbeanDollarKN(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "KN$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_kn.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_kn_changed(self):
        """test_ceastern_caribbean_dollar_kn_changed."""
        eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_kn.international = True

    def test_eastern_caribbean_dollar_kn_math_add(self):
        """test_eastern_caribbean_dollar_kn_math_add."""
        eastern_caribbean_dollar_kn_one = EasternCaribbeanDollarKN(amount=1)
        eastern_caribbean_dollar_kn_two = EasternCaribbeanDollarKN(amount=2)
        eastern_caribbean_dollar_kn_three = EasternCaribbeanDollarKN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_kn_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarKN\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_kn_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_kn_one +
            eastern_caribbean_dollar_kn_two) == eastern_caribbean_dollar_kn_three

    def test_eastern_caribbean_dollar_kn_slots(self):
        """test_eastern_caribbean_dollar_kn_slots."""
        eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarKN\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_kn.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar LC representation."""

from multicurrency import EasternCaribbeanDollarLC


class TestEasternCaribbeanDollarLC:
    """EasternCaribbeanDollarLC currency tests."""

    def test_eastern_caribbean_dollar_lc(self):
        """test_eastern_caribbean_dollar_lc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_lc.amount == decimal
        assert eastern_caribbean_dollar_lc.numeric_code == '951'
        assert eastern_caribbean_dollar_lc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_lc.decimal_places == 2
        assert eastern_caribbean_dollar_lc.decimal_sign == '.'
        assert eastern_caribbean_dollar_lc.grouping_places == 3
        assert eastern_caribbean_dollar_lc.grouping_sign == ','
        assert not eastern_caribbean_dollar_lc.international
        assert eastern_caribbean_dollar_lc.symbol == '$'
        assert eastern_caribbean_dollar_lc.symbol_ahead
        assert eastern_caribbean_dollar_lc.symbol_separator == ''
        assert eastern_caribbean_dollar_lc.localized_symbol == 'LC$'
        assert eastern_caribbean_dollar_lc.convertion == ''
        assert eastern_caribbean_dollar_lc.__hash__() == hash(
            (eastern_caribbean_dollar_lc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_lc.__repr__() == (
            'EasternCaribbeanDollarLC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "LC$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_lc.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_lc_negative(self):
        """test_eastern_caribbean_dollar_lc_negative."""
        amount = -100
        eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_lc.numeric_code == '951'
        assert eastern_caribbean_dollar_lc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_lc.decimal_places == 2
        assert eastern_caribbean_dollar_lc.decimal_sign == '.'
        assert eastern_caribbean_dollar_lc.grouping_places == 3
        assert eastern_caribbean_dollar_lc.grouping_sign == ','
        assert not eastern_caribbean_dollar_lc.international
        assert eastern_caribbean_dollar_lc.symbol == '$'
        assert eastern_caribbean_dollar_lc.symbol_ahead
        assert eastern_caribbean_dollar_lc.symbol_separator == ''
        assert eastern_caribbean_dollar_lc.localized_symbol == 'LC$'
        assert eastern_caribbean_dollar_lc.convertion == ''
        assert eastern_caribbean_dollar_lc.__hash__() == hash(
            (eastern_caribbean_dollar_lc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_lc.__repr__() == (
            'EasternCaribbeanDollarLC(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "LC$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_lc.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_lc_custom(self):
        """test_eastern_caribbean_dollar_lc_custom."""
        amount = 1000
        eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_lc.amount == decimal
        assert eastern_caribbean_dollar_lc.numeric_code == '951'
        assert eastern_caribbean_dollar_lc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_lc.decimal_places == 5
        assert eastern_caribbean_dollar_lc.decimal_sign == ','
        assert eastern_caribbean_dollar_lc.grouping_places == 2
        assert eastern_caribbean_dollar_lc.grouping_sign == '.'
        assert eastern_caribbean_dollar_lc.international
        assert eastern_caribbean_dollar_lc.symbol == '$'
        assert not eastern_caribbean_dollar_lc.symbol_ahead
        assert eastern_caribbean_dollar_lc.symbol_separator == '_'
        assert eastern_caribbean_dollar_lc.localized_symbol == 'LC$'
        assert eastern_caribbean_dollar_lc.convertion == ''
        assert eastern_caribbean_dollar_lc.__hash__() == hash(
            (eastern_caribbean_dollar_lc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_lc.__repr__() == (
            'EasternCaribbeanDollarLC(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LC$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_lc.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_lc_changed(self):
        """test_ceastern_caribbean_dollar_lc_changed."""
        eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_lc.international = True

    def test_eastern_caribbean_dollar_lc_math_add(self):
        """test_eastern_caribbean_dollar_lc_math_add."""
        eastern_caribbean_dollar_lc_one = EasternCaribbeanDollarLC(amount=1)
        eastern_caribbean_dollar_lc_two = EasternCaribbeanDollarLC(amount=2)
        eastern_caribbean_dollar_lc_three = EasternCaribbeanDollarLC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_lc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarLC\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_lc_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_lc_one +
            eastern_caribbean_dollar_lc_two) == eastern_caribbean_dollar_lc_three

    def test_eastern_caribbean_dollar_lc_slots(self):
        """test_eastern_caribbean_dollar_lc_slots."""
        eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarLC\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_lc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Eastern Caribbean Dollar VC representation."""

from multicurrency import EasternCaribbeanDollarVC


class TestEasternCaribbeanDollarVC:
    """EasternCaribbeanDollarVC currency tests."""

    def test_eastern_caribbean_dollar_vc(self):
        """test_eastern_caribbean_dollar_vc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_vc.amount == decimal
        assert eastern_caribbean_dollar_vc.numeric_code == '951'
        assert eastern_caribbean_dollar_vc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_vc.decimal_places == 2
        assert eastern_caribbean_dollar_vc.decimal_sign == '.'
        assert eastern_caribbean_dollar_vc.grouping_places == 3
        assert eastern_caribbean_dollar_vc.grouping_sign == ','
        assert not eastern_caribbean_dollar_vc.international
        assert eastern_caribbean_dollar_vc.symbol == '$'
        assert eastern_caribbean_dollar_vc.symbol_ahead
        assert eastern_caribbean_dollar_vc.symbol_separator == ''
        assert eastern_caribbean_dollar_vc.localized_symbol == 'VC$'
        assert eastern_caribbean_dollar_vc.convertion == ''
        assert eastern_caribbean_dollar_vc.__hash__() == hash(
            (eastern_caribbean_dollar_vc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_vc.__repr__() == (
            'EasternCaribbeanDollarVC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VC$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_vc.__str__() == '$0.14'

    def test_eastern_caribbean_dollar_vc_negative(self):
        """test_eastern_caribbean_dollar_vc_negative."""
        amount = -100
        eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_vc.numeric_code == '951'
        assert eastern_caribbean_dollar_vc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_vc.decimal_places == 2
        assert eastern_caribbean_dollar_vc.decimal_sign == '.'
        assert eastern_caribbean_dollar_vc.grouping_places == 3
        assert eastern_caribbean_dollar_vc.grouping_sign == ','
        assert not eastern_caribbean_dollar_vc.international
        assert eastern_caribbean_dollar_vc.symbol == '$'
        assert eastern_caribbean_dollar_vc.symbol_ahead
        assert eastern_caribbean_dollar_vc.symbol_separator == ''
        assert eastern_caribbean_dollar_vc.localized_symbol == 'VC$'
        assert eastern_caribbean_dollar_vc.convertion == ''
        assert eastern_caribbean_dollar_vc.__hash__() == hash(
            (eastern_caribbean_dollar_vc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_vc.__repr__() == (
            'EasternCaribbeanDollarVC(amount: -100, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VC$", '
            'numeric_code: "951", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eastern_caribbean_dollar_vc.__str__() == '$-100.00'

    def test_eastern_caribbean_dollar_vc_custom(self):
        """test_eastern_caribbean_dollar_vc_custom."""
        amount = 1000
        eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eastern_caribbean_dollar_vc.amount == decimal
        assert eastern_caribbean_dollar_vc.numeric_code == '951'
        assert eastern_caribbean_dollar_vc.alpha_code == 'XCD'
        assert eastern_caribbean_dollar_vc.decimal_places == 5
        assert eastern_caribbean_dollar_vc.decimal_sign == ','
        assert eastern_caribbean_dollar_vc.grouping_places == 2
        assert eastern_caribbean_dollar_vc.grouping_sign == '.'
        assert eastern_caribbean_dollar_vc.international
        assert eastern_caribbean_dollar_vc.symbol == '$'
        assert not eastern_caribbean_dollar_vc.symbol_ahead
        assert eastern_caribbean_dollar_vc.symbol_separator == '_'
        assert eastern_caribbean_dollar_vc.localized_symbol == 'VC$'
        assert eastern_caribbean_dollar_vc.convertion == ''
        assert eastern_caribbean_dollar_vc.__hash__() == hash(
            (eastern_caribbean_dollar_vc.__class__, decimal, 'XCD', '951'))
        assert eastern_caribbean_dollar_vc.__repr__() == (
            'EasternCaribbeanDollarVC(amount: 1000, '
            'alpha_code: "XCD", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "VC$", '
            'numeric_code: "951", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eastern_caribbean_dollar_vc.__str__() == 'XCD 10,00.00000'

    def test_eastern_caribbean_dollar_vc_changed(self):
        """test_ceastern_caribbean_dollar_vc_changed."""
        eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eastern_caribbean_dollar_vc.international = True

    def test_eastern_caribbean_dollar_vc_math_add(self):
        """test_eastern_caribbean_dollar_vc_math_add."""
        eastern_caribbean_dollar_vc_one = EasternCaribbeanDollarVC(amount=1)
        eastern_caribbean_dollar_vc_two = EasternCaribbeanDollarVC(amount=2)
        eastern_caribbean_dollar_vc_three = EasternCaribbeanDollarVC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XCD and OTHER.'):
            _ = eastern_caribbean_dollar_vc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.EasternCaribbeanDollarVC\'> '
                    'and <class \'str\'>.')):
            _ = eastern_caribbean_dollar_vc_one.__add__('1.00')
        assert (
            eastern_caribbean_dollar_vc_one +
            eastern_caribbean_dollar_vc_two) == eastern_caribbean_dollar_vc_three

    def test_eastern_caribbean_dollar_vc_slots(self):
        """test_eastern_caribbean_dollar_vc_slots."""
        eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EasternCaribbeanDollarVC\' '
                    'object has no attribute \'new_variable\'')):
            eastern_caribbean_dollar_vc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Zimbabwe Dollar representation."""

from multicurrency import ZimbabweDollar


class TestZimbabweDollar:
    """ZimbabweDollar currency tests."""

    def test_zimbabwe_dollar(self):
        """test_zimbabwe_dollar."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        zimbabwe_dollar = ZimbabweDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zimbabwe_dollar.amount == decimal
        assert zimbabwe_dollar.numeric_code == '932'
        assert zimbabwe_dollar.alpha_code == 'ZWL'
        assert zimbabwe_dollar.decimal_places == 2
        assert zimbabwe_dollar.decimal_sign == '.'
        assert zimbabwe_dollar.grouping_places == 3
        assert zimbabwe_dollar.grouping_sign == ','
        assert not zimbabwe_dollar.international
        assert zimbabwe_dollar.symbol == '$'
        assert zimbabwe_dollar.symbol_ahead
        assert zimbabwe_dollar.symbol_separator == '\u00A0'
        assert zimbabwe_dollar.localized_symbol == 'ZW$'
        assert zimbabwe_dollar.convertion == ''
        assert zimbabwe_dollar.__hash__() == hash(
            (zimbabwe_dollar.__class__, decimal, 'ZWL', '932'))
        assert zimbabwe_dollar.__repr__() == (
            'ZimbabweDollar(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZWL", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZW$", '
            'numeric_code: "932", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zimbabwe_dollar.__str__() == '$ 0.14'

    def test_zimbabwe_dollar_negative(self):
        """test_zimbabwe_dollar_negative."""
        amount = -100
        zimbabwe_dollar = ZimbabweDollar(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zimbabwe_dollar.numeric_code == '932'
        assert zimbabwe_dollar.alpha_code == 'ZWL'
        assert zimbabwe_dollar.decimal_places == 2
        assert zimbabwe_dollar.decimal_sign == '.'
        assert zimbabwe_dollar.grouping_places == 3
        assert zimbabwe_dollar.grouping_sign == ','
        assert not zimbabwe_dollar.international
        assert zimbabwe_dollar.symbol == '$'
        assert zimbabwe_dollar.symbol_ahead
        assert zimbabwe_dollar.symbol_separator == '\u00A0'
        assert zimbabwe_dollar.localized_symbol == 'ZW$'
        assert zimbabwe_dollar.convertion == ''
        assert zimbabwe_dollar.__hash__() == hash(
            (zimbabwe_dollar.__class__, decimal, 'ZWL', '932'))
        assert zimbabwe_dollar.__repr__() == (
            'ZimbabweDollar(amount: -100, '
            'alpha_code: "ZWL", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ZW$", '
            'numeric_code: "932", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zimbabwe_dollar.__str__() == '$ -100.00'

    def test_zimbabwe_dollar_custom(self):
        """test_zimbabwe_dollar_custom."""
        amount = 1000
        zimbabwe_dollar = ZimbabweDollar(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert zimbabwe_dollar.amount == decimal
        assert zimbabwe_dollar.numeric_code == '932'
        assert zimbabwe_dollar.alpha_code == 'ZWL'
        assert zimbabwe_dollar.decimal_places == 5
        assert zimbabwe_dollar.decimal_sign == ','
        assert zimbabwe_dollar.grouping_places == 2
        assert zimbabwe_dollar.grouping_sign == '.'
        assert zimbabwe_dollar.international
        assert zimbabwe_dollar.symbol == '$'
        assert not zimbabwe_dollar.symbol_ahead
        assert zimbabwe_dollar.symbol_separator == '_'
        assert zimbabwe_dollar.localized_symbol == 'ZW$'
        assert zimbabwe_dollar.convertion == ''
        assert zimbabwe_dollar.__hash__() == hash(
            (zimbabwe_dollar.__class__, decimal, 'ZWL', '932'))
        assert zimbabwe_dollar.__repr__() == (
            'ZimbabweDollar(amount: 1000, '
            'alpha_code: "ZWL", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ZW$", '
            'numeric_code: "932", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert zimbabwe_dollar.__str__() == 'ZWL 10,00.00000'

    def test_zimbabwe_dollar_changed(self):
        """test_czimbabwe_dollar_changed."""
        zimbabwe_dollar = ZimbabweDollar(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zimbabwe_dollar.international = True

    def test_zimbabwe_dollar_math_add(self):
        """test_zimbabwe_dollar_math_add."""
        zimbabwe_dollar_one = ZimbabweDollar(amount=1)
        zimbabwe_dollar_two = ZimbabweDollar(amount=2)
        zimbabwe_dollar_three = ZimbabweDollar(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZWL and OTHER.'):
            _ = zimbabwe_dollar_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'dollar.ZimbabweDollar\'> '
                    'and <class \'str\'>.')):
            _ = zimbabwe_dollar_one.__add__('1.00')
        assert (
            zimbabwe_dollar_one +
            zimbabwe_dollar_two) == zimbabwe_dollar_three

    def test_zimbabwe_dollar_slots(self):
        """test_zimbabwe_dollar_slots."""
        zimbabwe_dollar = ZimbabweDollar(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ZimbabweDollar\' '
                    'object has no attribute \'new_variable\'')):
            zimbabwe_dollar.new_variable = 'fail'  # pylint: disable=assigning-non-slot
