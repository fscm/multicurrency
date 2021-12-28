# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Franc currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Burundi Franc representation."""

from multicurrency import BurundiFranc


class TestBurundiFranc:
    """BurundiFranc currency tests."""

    def test_burundi_franc(self):
        """test_burundi_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        burundi_franc = BurundiFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert burundi_franc.amount == decimal
        assert burundi_franc.numeric_code == '108'
        assert burundi_franc.alpha_code == 'BIF'
        assert burundi_franc.decimal_places == 0
        assert burundi_franc.decimal_sign == ','
        assert burundi_franc.grouping_places == 3
        assert burundi_franc.grouping_sign == '\u202F'
        assert not burundi_franc.international
        assert burundi_franc.symbol == '₣'
        assert not burundi_franc.symbol_ahead
        assert burundi_franc.symbol_separator == '\u00A0'
        assert burundi_franc.localized_symbol == 'BI₣'
        assert burundi_franc.convertion == ''
        assert burundi_franc.__hash__() == hash(
            (burundi_franc.__class__, decimal, 'BIF', '108'))
        assert burundi_franc.__repr__() == (
            'BurundiFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "BIF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BI₣", '
            'numeric_code: "108", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert burundi_franc.__str__() == '0 ₣'

    def test_burundi_franc_negative(self):
        """test_burundi_franc_negative."""
        amount = -100
        burundi_franc = BurundiFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert burundi_franc.numeric_code == '108'
        assert burundi_franc.alpha_code == 'BIF'
        assert burundi_franc.decimal_places == 0
        assert burundi_franc.decimal_sign == ','
        assert burundi_franc.grouping_places == 3
        assert burundi_franc.grouping_sign == '\u202F'
        assert not burundi_franc.international
        assert burundi_franc.symbol == '₣'
        assert not burundi_franc.symbol_ahead
        assert burundi_franc.symbol_separator == '\u00A0'
        assert burundi_franc.localized_symbol == 'BI₣'
        assert burundi_franc.convertion == ''
        assert burundi_franc.__hash__() == hash(
            (burundi_franc.__class__, decimal, 'BIF', '108'))
        assert burundi_franc.__repr__() == (
            'BurundiFranc(amount: -100, '
            'alpha_code: "BIF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BI₣", '
            'numeric_code: "108", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert burundi_franc.__str__() == '-100 ₣'

    def test_burundi_franc_custom(self):
        """test_burundi_franc_custom."""
        amount = 1000
        burundi_franc = BurundiFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert burundi_franc.amount == decimal
        assert burundi_franc.numeric_code == '108'
        assert burundi_franc.alpha_code == 'BIF'
        assert burundi_franc.decimal_places == 5
        assert burundi_franc.decimal_sign == '\u202F'
        assert burundi_franc.grouping_places == 2
        assert burundi_franc.grouping_sign == ','
        assert burundi_franc.international
        assert burundi_franc.symbol == '₣'
        assert not burundi_franc.symbol_ahead
        assert burundi_franc.symbol_separator == '_'
        assert burundi_franc.localized_symbol == 'BI₣'
        assert burundi_franc.convertion == ''
        assert burundi_franc.__hash__() == hash(
            (burundi_franc.__class__, decimal, 'BIF', '108'))
        assert burundi_franc.__repr__() == (
            'BurundiFranc(amount: 1000, '
            'alpha_code: "BIF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BI₣", '
            'numeric_code: "108", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert burundi_franc.__str__() == 'BIF 10,00.00000'

    def test_burundi_franc_changed(self):
        """test_cburundi_franc_changed."""
        burundi_franc = BurundiFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            burundi_franc.international = True

    def test_burundi_franc_math_add(self):
        """test_burundi_franc_math_add."""
        burundi_franc_one = BurundiFranc(amount=1)
        burundi_franc_two = BurundiFranc(amount=2)
        burundi_franc_three = BurundiFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency BIF and OTHER.'):
            _ = burundi_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.BurundiFranc\'> '
                    'and <class \'str\'>.')):
            _ = burundi_franc_one.__add__('1.00')
        assert (
            burundi_franc_one +
            burundi_franc_two) == burundi_franc_three

    def test_burundi_franc_slots(self):
        """test_burundi_franc_slots."""
        burundi_franc = BurundiFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'BurundiFranc\' '
                    'object has no attribute \'new_variable\'')):
            burundi_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Congolese Franc representation."""

from multicurrency import CongoleseFranc


class TestCongoleseFranc:
    """CongoleseFranc currency tests."""

    def test_congolese_franc(self):
        """test_congolese_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        congolese_franc = CongoleseFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert congolese_franc.amount == decimal
        assert congolese_franc.numeric_code == '976'
        assert congolese_franc.alpha_code == 'CDF'
        assert congolese_franc.decimal_places == 2
        assert congolese_franc.decimal_sign == ','
        assert congolese_franc.grouping_places == 3
        assert congolese_franc.grouping_sign == '\u202F'
        assert not congolese_franc.international
        assert congolese_franc.symbol == '₣'
        assert not congolese_franc.symbol_ahead
        assert congolese_franc.symbol_separator == '\u00A0'
        assert congolese_franc.localized_symbol == 'CD₣'
        assert congolese_franc.convertion == ''
        assert congolese_franc.__hash__() == hash(
            (congolese_franc.__class__, decimal, 'CDF', '976'))
        assert congolese_franc.__repr__() == (
            'CongoleseFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CDF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CD₣", '
            'numeric_code: "976", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert congolese_franc.__str__() == '0,14 ₣'

    def test_congolese_franc_negative(self):
        """test_congolese_franc_negative."""
        amount = -100
        congolese_franc = CongoleseFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert congolese_franc.numeric_code == '976'
        assert congolese_franc.alpha_code == 'CDF'
        assert congolese_franc.decimal_places == 2
        assert congolese_franc.decimal_sign == ','
        assert congolese_franc.grouping_places == 3
        assert congolese_franc.grouping_sign == '\u202F'
        assert not congolese_franc.international
        assert congolese_franc.symbol == '₣'
        assert not congolese_franc.symbol_ahead
        assert congolese_franc.symbol_separator == '\u00A0'
        assert congolese_franc.localized_symbol == 'CD₣'
        assert congolese_franc.convertion == ''
        assert congolese_franc.__hash__() == hash(
            (congolese_franc.__class__, decimal, 'CDF', '976'))
        assert congolese_franc.__repr__() == (
            'CongoleseFranc(amount: -100, '
            'alpha_code: "CDF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CD₣", '
            'numeric_code: "976", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert congolese_franc.__str__() == '-100,00 ₣'

    def test_congolese_franc_custom(self):
        """test_congolese_franc_custom."""
        amount = 1000
        congolese_franc = CongoleseFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert congolese_franc.amount == decimal
        assert congolese_franc.numeric_code == '976'
        assert congolese_franc.alpha_code == 'CDF'
        assert congolese_franc.decimal_places == 5
        assert congolese_franc.decimal_sign == '\u202F'
        assert congolese_franc.grouping_places == 2
        assert congolese_franc.grouping_sign == ','
        assert congolese_franc.international
        assert congolese_franc.symbol == '₣'
        assert not congolese_franc.symbol_ahead
        assert congolese_franc.symbol_separator == '_'
        assert congolese_franc.localized_symbol == 'CD₣'
        assert congolese_franc.convertion == ''
        assert congolese_franc.__hash__() == hash(
            (congolese_franc.__class__, decimal, 'CDF', '976'))
        assert congolese_franc.__repr__() == (
            'CongoleseFranc(amount: 1000, '
            'alpha_code: "CDF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CD₣", '
            'numeric_code: "976", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert congolese_franc.__str__() == 'CDF 10,00.00000'

    def test_congolese_franc_changed(self):
        """test_ccongolese_franc_changed."""
        congolese_franc = CongoleseFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            congolese_franc.international = True

    def test_congolese_franc_math_add(self):
        """test_congolese_franc_math_add."""
        congolese_franc_one = CongoleseFranc(amount=1)
        congolese_franc_two = CongoleseFranc(amount=2)
        congolese_franc_three = CongoleseFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CDF and OTHER.'):
            _ = congolese_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CongoleseFranc\'> '
                    'and <class \'str\'>.')):
            _ = congolese_franc_one.__add__('1.00')
        assert (
            congolese_franc_one +
            congolese_franc_two) == congolese_franc_three

    def test_congolese_franc_slots(self):
        """test_congolese_franc_slots."""
        congolese_franc = CongoleseFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CongoleseFranc\' '
                    'object has no attribute \'new_variable\'')):
            congolese_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Swiss Franc representation."""

from multicurrency import SwissFranc


class TestSwissFranc:
    """SwissFranc currency tests."""

    def test_swiss_franc(self):
        """test_swiss_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        swiss_franc = SwissFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc.amount == decimal
        assert swiss_franc.numeric_code == '756'
        assert swiss_franc.alpha_code == 'CHF'
        assert swiss_franc.decimal_places == 2
        assert swiss_franc.decimal_sign == '.'
        assert swiss_franc.grouping_places == 3
        assert swiss_franc.grouping_sign == '\''
        assert not swiss_franc.international
        assert swiss_franc.symbol == '₣'
        assert swiss_franc.symbol_ahead
        assert swiss_franc.symbol_separator == '\u00A0'
        assert swiss_franc.localized_symbol == '₣'
        assert swiss_franc.convertion == ''
        assert swiss_franc.__hash__() == hash(
            (swiss_franc.__class__, decimal, 'CHF', '756'))
        assert swiss_franc.__repr__() == (
            'SwissFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc.__str__() == '₣ 0.14'

    def test_swiss_franc_negative(self):
        """test_swiss_franc_negative."""
        amount = -100
        swiss_franc = SwissFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc.numeric_code == '756'
        assert swiss_franc.alpha_code == 'CHF'
        assert swiss_franc.decimal_places == 2
        assert swiss_franc.decimal_sign == '.'
        assert swiss_franc.grouping_places == 3
        assert swiss_franc.grouping_sign == '\''
        assert not swiss_franc.international
        assert swiss_franc.symbol == '₣'
        assert swiss_franc.symbol_ahead
        assert swiss_franc.symbol_separator == '\u00A0'
        assert swiss_franc.localized_symbol == '₣'
        assert swiss_franc.convertion == ''
        assert swiss_franc.__hash__() == hash(
            (swiss_franc.__class__, decimal, 'CHF', '756'))
        assert swiss_franc.__repr__() == (
            'SwissFranc(amount: -100, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc.__str__() == '₣ -100.00'

    def test_swiss_franc_custom(self):
        """test_swiss_franc_custom."""
        amount = 1000
        swiss_franc = SwissFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\'',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc.amount == decimal
        assert swiss_franc.numeric_code == '756'
        assert swiss_franc.alpha_code == 'CHF'
        assert swiss_franc.decimal_places == 5
        assert swiss_franc.decimal_sign == '\''
        assert swiss_franc.grouping_places == 2
        assert swiss_franc.grouping_sign == '.'
        assert swiss_franc.international
        assert swiss_franc.symbol == '₣'
        assert not swiss_franc.symbol_ahead
        assert swiss_franc.symbol_separator == '_'
        assert swiss_franc.localized_symbol == '₣'
        assert swiss_franc.convertion == ''
        assert swiss_franc.__hash__() == hash(
            (swiss_franc.__class__, decimal, 'CHF', '756'))
        assert swiss_franc.__repr__() == (
            'SwissFranc(amount: 1000, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₣", '
            'numeric_code: "756", '
            'decimal_places: "5", '
            'decimal_sign: "\'", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert swiss_franc.__str__() == 'CHF 10,00.00000'

    def test_swiss_franc_changed(self):
        """test_cswiss_franc_changed."""
        swiss_franc = SwissFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc.international = True

    def test_swiss_franc_math_add(self):
        """test_swiss_franc_math_add."""
        swiss_franc_one = SwissFranc(amount=1)
        swiss_franc_two = SwissFranc(amount=2)
        swiss_franc_three = SwissFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CHF and OTHER.'):
            _ = swiss_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.SwissFranc\'> '
                    'and <class \'str\'>.')):
            _ = swiss_franc_one.__add__('1.00')
        assert (
            swiss_franc_one +
            swiss_franc_two) == swiss_franc_three

    def test_swiss_franc_slots(self):
        """test_swiss_franc_slots."""
        swiss_franc = SwissFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SwissFranc\' '
                    'object has no attribute \'new_variable\'')):
            swiss_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Swiss Franc LI representation."""

from multicurrency import SwissFrancLI


class TestSwissFrancLI:
    """SwissFrancLI currency tests."""

    def test_swiss_franc_li(self):
        """test_swiss_franc_li."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        swiss_franc_li = SwissFrancLI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_li.amount == decimal
        assert swiss_franc_li.numeric_code == '756'
        assert swiss_franc_li.alpha_code == 'CHF'
        assert swiss_franc_li.decimal_places == 2
        assert swiss_franc_li.decimal_sign == '.'
        assert swiss_franc_li.grouping_places == 3
        assert swiss_franc_li.grouping_sign == '\''
        assert not swiss_franc_li.international
        assert swiss_franc_li.symbol == '₣'
        assert swiss_franc_li.symbol_ahead
        assert swiss_franc_li.symbol_separator == '\u00A0'
        assert swiss_franc_li.localized_symbol == 'LI₣'
        assert swiss_franc_li.convertion == ''
        assert swiss_franc_li.__hash__() == hash(
            (swiss_franc_li.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_li.__repr__() == (
            'SwissFrancLI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LI₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc_li.__str__() == '₣ 0.14'

    def test_swiss_franc_li_negative(self):
        """test_swiss_franc_li_negative."""
        amount = -100
        swiss_franc_li = SwissFrancLI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_li.numeric_code == '756'
        assert swiss_franc_li.alpha_code == 'CHF'
        assert swiss_franc_li.decimal_places == 2
        assert swiss_franc_li.decimal_sign == '.'
        assert swiss_franc_li.grouping_places == 3
        assert swiss_franc_li.grouping_sign == '\''
        assert not swiss_franc_li.international
        assert swiss_franc_li.symbol == '₣'
        assert swiss_franc_li.symbol_ahead
        assert swiss_franc_li.symbol_separator == '\u00A0'
        assert swiss_franc_li.localized_symbol == 'LI₣'
        assert swiss_franc_li.convertion == ''
        assert swiss_franc_li.__hash__() == hash(
            (swiss_franc_li.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_li.__repr__() == (
            'SwissFrancLI(amount: -100, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LI₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc_li.__str__() == '₣ -100.00'

    def test_swiss_franc_li_custom(self):
        """test_swiss_franc_li_custom."""
        amount = 1000
        swiss_franc_li = SwissFrancLI(
            amount=amount,
            decimal_places=5,
            decimal_sign='\'',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_li.amount == decimal
        assert swiss_franc_li.numeric_code == '756'
        assert swiss_franc_li.alpha_code == 'CHF'
        assert swiss_franc_li.decimal_places == 5
        assert swiss_franc_li.decimal_sign == '\''
        assert swiss_franc_li.grouping_places == 2
        assert swiss_franc_li.grouping_sign == '.'
        assert swiss_franc_li.international
        assert swiss_franc_li.symbol == '₣'
        assert not swiss_franc_li.symbol_ahead
        assert swiss_franc_li.symbol_separator == '_'
        assert swiss_franc_li.localized_symbol == 'LI₣'
        assert swiss_franc_li.convertion == ''
        assert swiss_franc_li.__hash__() == hash(
            (swiss_franc_li.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_li.__repr__() == (
            'SwissFrancLI(amount: 1000, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LI₣", '
            'numeric_code: "756", '
            'decimal_places: "5", '
            'decimal_sign: "\'", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert swiss_franc_li.__str__() == 'CHF 10,00.00000'

    def test_swiss_franc_li_changed(self):
        """test_cswiss_franc_li_changed."""
        swiss_franc_li = SwissFrancLI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_li.international = True

    def test_swiss_franc_li_math_add(self):
        """test_swiss_franc_li_math_add."""
        swiss_franc_li_one = SwissFrancLI(amount=1)
        swiss_franc_li_two = SwissFrancLI(amount=2)
        swiss_franc_li_three = SwissFrancLI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CHF and OTHER.'):
            _ = swiss_franc_li_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.SwissFrancLI\'> '
                    'and <class \'str\'>.')):
            _ = swiss_franc_li_one.__add__('1.00')
        assert (
            swiss_franc_li_one +
            swiss_franc_li_two) == swiss_franc_li_three

    def test_swiss_franc_li_slots(self):
        """test_swiss_franc_li_slots."""
        swiss_franc_li = SwissFrancLI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SwissFrancLI\' '
                    'object has no attribute \'new_variable\'')):
            swiss_franc_li.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Swiss Franc CH representation."""

from multicurrency import SwissFrancCH


class TestSwissFrancCH:
    """SwissFrancCH currency tests."""

    def test_swiss_franc_ch(self):
        """test_swiss_franc_ch."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        swiss_franc_ch = SwissFrancCH(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_ch.amount == decimal
        assert swiss_franc_ch.numeric_code == '756'
        assert swiss_franc_ch.alpha_code == 'CHF'
        assert swiss_franc_ch.decimal_places == 2
        assert swiss_franc_ch.decimal_sign == '.'
        assert swiss_franc_ch.grouping_places == 3
        assert swiss_franc_ch.grouping_sign == '\''
        assert not swiss_franc_ch.international
        assert swiss_franc_ch.symbol == '₣'
        assert swiss_franc_ch.symbol_ahead
        assert swiss_franc_ch.symbol_separator == '\u00A0'
        assert swiss_franc_ch.localized_symbol == 'CH₣'
        assert swiss_franc_ch.convertion == ''
        assert swiss_franc_ch.__hash__() == hash(
            (swiss_franc_ch.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_ch.__repr__() == (
            'SwissFrancCH(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CH₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc_ch.__str__() == '₣ 0.14'

    def test_swiss_franc_ch_negative(self):
        """test_swiss_franc_ch_negative."""
        amount = -100
        swiss_franc_ch = SwissFrancCH(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_ch.numeric_code == '756'
        assert swiss_franc_ch.alpha_code == 'CHF'
        assert swiss_franc_ch.decimal_places == 2
        assert swiss_franc_ch.decimal_sign == '.'
        assert swiss_franc_ch.grouping_places == 3
        assert swiss_franc_ch.grouping_sign == '\''
        assert not swiss_franc_ch.international
        assert swiss_franc_ch.symbol == '₣'
        assert swiss_franc_ch.symbol_ahead
        assert swiss_franc_ch.symbol_separator == '\u00A0'
        assert swiss_franc_ch.localized_symbol == 'CH₣'
        assert swiss_franc_ch.convertion == ''
        assert swiss_franc_ch.__hash__() == hash(
            (swiss_franc_ch.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_ch.__repr__() == (
            'SwissFrancCH(amount: -100, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CH₣", '
            'numeric_code: "756", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: "\'", '
            'convertion: "", '
            'international: False)')
        assert swiss_franc_ch.__str__() == '₣ -100.00'

    def test_swiss_franc_ch_custom(self):
        """test_swiss_franc_ch_custom."""
        amount = 1000
        swiss_franc_ch = SwissFrancCH(
            amount=amount,
            decimal_places=5,
            decimal_sign='\'',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert swiss_franc_ch.amount == decimal
        assert swiss_franc_ch.numeric_code == '756'
        assert swiss_franc_ch.alpha_code == 'CHF'
        assert swiss_franc_ch.decimal_places == 5
        assert swiss_franc_ch.decimal_sign == '\''
        assert swiss_franc_ch.grouping_places == 2
        assert swiss_franc_ch.grouping_sign == '.'
        assert swiss_franc_ch.international
        assert swiss_franc_ch.symbol == '₣'
        assert not swiss_franc_ch.symbol_ahead
        assert swiss_franc_ch.symbol_separator == '_'
        assert swiss_franc_ch.localized_symbol == 'CH₣'
        assert swiss_franc_ch.convertion == ''
        assert swiss_franc_ch.__hash__() == hash(
            (swiss_franc_ch.__class__, decimal, 'CHF', '756'))
        assert swiss_franc_ch.__repr__() == (
            'SwissFrancCH(amount: 1000, '
            'alpha_code: "CHF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CH₣", '
            'numeric_code: "756", '
            'decimal_places: "5", '
            'decimal_sign: "\'", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert swiss_franc_ch.__str__() == 'CHF 10,00.00000'

    def test_swiss_franc_ch_changed(self):
        """test_cswiss_franc_ch_changed."""
        swiss_franc_ch = SwissFrancCH(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            swiss_franc_ch.international = True

    def test_swiss_franc_ch_math_add(self):
        """test_swiss_franc_ch_math_add."""
        swiss_franc_ch_one = SwissFrancCH(amount=1)
        swiss_franc_ch_two = SwissFrancCH(amount=2)
        swiss_franc_ch_three = SwissFrancCH(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CHF and OTHER.'):
            _ = swiss_franc_ch_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.SwissFrancCH\'> '
                    'and <class \'str\'>.')):
            _ = swiss_franc_ch_one.__add__('1.00')
        assert (
            swiss_franc_ch_one +
            swiss_franc_ch_two) == swiss_franc_ch_three

    def test_swiss_franc_ch_slots(self):
        """test_swiss_franc_ch_slots."""
        swiss_franc_ch = SwissFrancCH(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SwissFrancCH\' '
                    'object has no attribute \'new_variable\'')):
            swiss_franc_ch.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Djibouti Franc representation."""

from multicurrency import DjiboutiFranc


class TestDjiboutiFranc:
    """DjiboutiFranc currency tests."""

    def test_djibouti_franc(self):
        """test_djibouti_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        djibouti_franc = DjiboutiFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert djibouti_franc.amount == decimal
        assert djibouti_franc.numeric_code == '262'
        assert djibouti_franc.alpha_code == 'DJF'
        assert djibouti_franc.decimal_places == 0
        assert djibouti_franc.decimal_sign == ','
        assert djibouti_franc.grouping_places == 3
        assert djibouti_franc.grouping_sign == '\u202F'
        assert not djibouti_franc.international
        assert djibouti_franc.symbol == '₣'
        assert not djibouti_franc.symbol_ahead
        assert djibouti_franc.symbol_separator == '\u00A0'
        assert djibouti_franc.localized_symbol == 'DJ₣'
        assert djibouti_franc.convertion == ''
        assert djibouti_franc.__hash__() == hash(
            (djibouti_franc.__class__, decimal, 'DJF', '262'))
        assert djibouti_franc.__repr__() == (
            'DjiboutiFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "DJF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "DJ₣", '
            'numeric_code: "262", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert djibouti_franc.__str__() == '0 ₣'

    def test_djibouti_franc_negative(self):
        """test_djibouti_franc_negative."""
        amount = -100
        djibouti_franc = DjiboutiFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert djibouti_franc.numeric_code == '262'
        assert djibouti_franc.alpha_code == 'DJF'
        assert djibouti_franc.decimal_places == 0
        assert djibouti_franc.decimal_sign == ','
        assert djibouti_franc.grouping_places == 3
        assert djibouti_franc.grouping_sign == '\u202F'
        assert not djibouti_franc.international
        assert djibouti_franc.symbol == '₣'
        assert not djibouti_franc.symbol_ahead
        assert djibouti_franc.symbol_separator == '\u00A0'
        assert djibouti_franc.localized_symbol == 'DJ₣'
        assert djibouti_franc.convertion == ''
        assert djibouti_franc.__hash__() == hash(
            (djibouti_franc.__class__, decimal, 'DJF', '262'))
        assert djibouti_franc.__repr__() == (
            'DjiboutiFranc(amount: -100, '
            'alpha_code: "DJF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "DJ₣", '
            'numeric_code: "262", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert djibouti_franc.__str__() == '-100 ₣'

    def test_djibouti_franc_custom(self):
        """test_djibouti_franc_custom."""
        amount = 1000
        djibouti_franc = DjiboutiFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert djibouti_franc.amount == decimal
        assert djibouti_franc.numeric_code == '262'
        assert djibouti_franc.alpha_code == 'DJF'
        assert djibouti_franc.decimal_places == 5
        assert djibouti_franc.decimal_sign == '\u202F'
        assert djibouti_franc.grouping_places == 2
        assert djibouti_franc.grouping_sign == ','
        assert djibouti_franc.international
        assert djibouti_franc.symbol == '₣'
        assert not djibouti_franc.symbol_ahead
        assert djibouti_franc.symbol_separator == '_'
        assert djibouti_franc.localized_symbol == 'DJ₣'
        assert djibouti_franc.convertion == ''
        assert djibouti_franc.__hash__() == hash(
            (djibouti_franc.__class__, decimal, 'DJF', '262'))
        assert djibouti_franc.__repr__() == (
            'DjiboutiFranc(amount: 1000, '
            'alpha_code: "DJF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "DJ₣", '
            'numeric_code: "262", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert djibouti_franc.__str__() == 'DJF 10,00.00000'

    def test_djibouti_franc_changed(self):
        """test_cdjibouti_franc_changed."""
        djibouti_franc = DjiboutiFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            djibouti_franc.international = True

    def test_djibouti_franc_math_add(self):
        """test_djibouti_franc_math_add."""
        djibouti_franc_one = DjiboutiFranc(amount=1)
        djibouti_franc_two = DjiboutiFranc(amount=2)
        djibouti_franc_three = DjiboutiFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency DJF and OTHER.'):
            _ = djibouti_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.DjiboutiFranc\'> '
                    'and <class \'str\'>.')):
            _ = djibouti_franc_one.__add__('1.00')
        assert (
            djibouti_franc_one +
            djibouti_franc_two) == djibouti_franc_three

    def test_djibouti_franc_slots(self):
        """test_djibouti_franc_slots."""
        djibouti_franc = DjiboutiFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'DjiboutiFranc\' '
                    'object has no attribute \'new_variable\'')):
            djibouti_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Guinea Franc representation."""

from multicurrency import GuineaFranc


class TestGuineaFranc:
    """GuineaFranc currency tests."""

    def test_guinea_franc(self):
        """test_guinea_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        guinea_franc = GuineaFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guinea_franc.amount == decimal
        assert guinea_franc.numeric_code == '324'
        assert guinea_franc.alpha_code == 'GNF'
        assert guinea_franc.decimal_places == 0
        assert guinea_franc.decimal_sign == ','
        assert guinea_franc.grouping_places == 3
        assert guinea_franc.grouping_sign == '\u202F'
        assert not guinea_franc.international
        assert guinea_franc.symbol == '₣'
        assert not guinea_franc.symbol_ahead
        assert guinea_franc.symbol_separator == '\u00A0'
        assert guinea_franc.localized_symbol == 'GN₣'
        assert guinea_franc.convertion == ''
        assert guinea_franc.__hash__() == hash(
            (guinea_franc.__class__, decimal, 'GNF', '324'))
        assert guinea_franc.__repr__() == (
            'GuineaFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "GNF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GN₣", '
            'numeric_code: "324", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert guinea_franc.__str__() == '0 ₣'

    def test_guinea_franc_negative(self):
        """test_guinea_franc_negative."""
        amount = -100
        guinea_franc = GuineaFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert guinea_franc.numeric_code == '324'
        assert guinea_franc.alpha_code == 'GNF'
        assert guinea_franc.decimal_places == 0
        assert guinea_franc.decimal_sign == ','
        assert guinea_franc.grouping_places == 3
        assert guinea_franc.grouping_sign == '\u202F'
        assert not guinea_franc.international
        assert guinea_franc.symbol == '₣'
        assert not guinea_franc.symbol_ahead
        assert guinea_franc.symbol_separator == '\u00A0'
        assert guinea_franc.localized_symbol == 'GN₣'
        assert guinea_franc.convertion == ''
        assert guinea_franc.__hash__() == hash(
            (guinea_franc.__class__, decimal, 'GNF', '324'))
        assert guinea_franc.__repr__() == (
            'GuineaFranc(amount: -100, '
            'alpha_code: "GNF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GN₣", '
            'numeric_code: "324", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert guinea_franc.__str__() == '-100 ₣'

    def test_guinea_franc_custom(self):
        """test_guinea_franc_custom."""
        amount = 1000
        guinea_franc = GuineaFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert guinea_franc.amount == decimal
        assert guinea_franc.numeric_code == '324'
        assert guinea_franc.alpha_code == 'GNF'
        assert guinea_franc.decimal_places == 5
        assert guinea_franc.decimal_sign == '\u202F'
        assert guinea_franc.grouping_places == 2
        assert guinea_franc.grouping_sign == ','
        assert guinea_franc.international
        assert guinea_franc.symbol == '₣'
        assert not guinea_franc.symbol_ahead
        assert guinea_franc.symbol_separator == '_'
        assert guinea_franc.localized_symbol == 'GN₣'
        assert guinea_franc.convertion == ''
        assert guinea_franc.__hash__() == hash(
            (guinea_franc.__class__, decimal, 'GNF', '324'))
        assert guinea_franc.__repr__() == (
            'GuineaFranc(amount: 1000, '
            'alpha_code: "GNF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GN₣", '
            'numeric_code: "324", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert guinea_franc.__str__() == 'GNF 10,00.00000'

    def test_guinea_franc_changed(self):
        """test_cguinea_franc_changed."""
        guinea_franc = GuineaFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            guinea_franc.international = True

    def test_guinea_franc_math_add(self):
        """test_guinea_franc_math_add."""
        guinea_franc_one = GuineaFranc(amount=1)
        guinea_franc_two = GuineaFranc(amount=2)
        guinea_franc_three = GuineaFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency GNF and OTHER.'):
            _ = guinea_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.GuineaFranc\'> '
                    'and <class \'str\'>.')):
            _ = guinea_franc_one.__add__('1.00')
        assert (
            guinea_franc_one +
            guinea_franc_two) == guinea_franc_three

    def test_guinea_franc_slots(self):
        """test_guinea_franc_slots."""
        guinea_franc = GuineaFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'GuineaFranc\' '
                    'object has no attribute \'new_variable\'')):
            guinea_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Rwanda Franc representation."""

from multicurrency import RwandaFranc


class TestRwandaFranc:
    """RwandaFranc currency tests."""

    def test_rwanda_franc(self):
        """test_rwanda_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        rwanda_franc = RwandaFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rwanda_franc.amount == decimal
        assert rwanda_franc.numeric_code == '646'
        assert rwanda_franc.alpha_code == 'RWF'
        assert rwanda_franc.decimal_places == 0
        assert rwanda_franc.decimal_sign == ','
        assert rwanda_franc.grouping_places == 3
        assert rwanda_franc.grouping_sign == '.'
        assert not rwanda_franc.international
        assert rwanda_franc.symbol == '₣'
        assert rwanda_franc.symbol_ahead
        assert rwanda_franc.symbol_separator == '\u00A0'
        assert rwanda_franc.localized_symbol == 'RW₣'
        assert rwanda_franc.convertion == ''
        assert rwanda_franc.__hash__() == hash(
            (rwanda_franc.__class__, decimal, 'RWF', '646'))
        assert rwanda_franc.__repr__() == (
            'RwandaFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RWF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RW₣", '
            'numeric_code: "646", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert rwanda_franc.__str__() == '₣ 0'

    def test_rwanda_franc_negative(self):
        """test_rwanda_franc_negative."""
        amount = -100
        rwanda_franc = RwandaFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert rwanda_franc.numeric_code == '646'
        assert rwanda_franc.alpha_code == 'RWF'
        assert rwanda_franc.decimal_places == 0
        assert rwanda_franc.decimal_sign == ','
        assert rwanda_franc.grouping_places == 3
        assert rwanda_franc.grouping_sign == '.'
        assert not rwanda_franc.international
        assert rwanda_franc.symbol == '₣'
        assert rwanda_franc.symbol_ahead
        assert rwanda_franc.symbol_separator == '\u00A0'
        assert rwanda_franc.localized_symbol == 'RW₣'
        assert rwanda_franc.convertion == ''
        assert rwanda_franc.__hash__() == hash(
            (rwanda_franc.__class__, decimal, 'RWF', '646'))
        assert rwanda_franc.__repr__() == (
            'RwandaFranc(amount: -100, '
            'alpha_code: "RWF", '
            'symbol: "₣", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "RW₣", '
            'numeric_code: "646", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert rwanda_franc.__str__() == '₣ -100'

    def test_rwanda_franc_custom(self):
        """test_rwanda_franc_custom."""
        amount = 1000
        rwanda_franc = RwandaFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert rwanda_franc.amount == decimal
        assert rwanda_franc.numeric_code == '646'
        assert rwanda_franc.alpha_code == 'RWF'
        assert rwanda_franc.decimal_places == 5
        assert rwanda_franc.decimal_sign == '.'
        assert rwanda_franc.grouping_places == 2
        assert rwanda_franc.grouping_sign == ','
        assert rwanda_franc.international
        assert rwanda_franc.symbol == '₣'
        assert not rwanda_franc.symbol_ahead
        assert rwanda_franc.symbol_separator == '_'
        assert rwanda_franc.localized_symbol == 'RW₣'
        assert rwanda_franc.convertion == ''
        assert rwanda_franc.__hash__() == hash(
            (rwanda_franc.__class__, decimal, 'RWF', '646'))
        assert rwanda_franc.__repr__() == (
            'RwandaFranc(amount: 1000, '
            'alpha_code: "RWF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "RW₣", '
            'numeric_code: "646", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert rwanda_franc.__str__() == 'RWF 10,00.00000'

    def test_rwanda_franc_changed(self):
        """test_crwanda_franc_changed."""
        rwanda_franc = RwandaFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            rwanda_franc.international = True

    def test_rwanda_franc_math_add(self):
        """test_rwanda_franc_math_add."""
        rwanda_franc_one = RwandaFranc(amount=1)
        rwanda_franc_two = RwandaFranc(amount=2)
        rwanda_franc_three = RwandaFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RWF and OTHER.'):
            _ = rwanda_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.RwandaFranc\'> '
                    'and <class \'str\'>.')):
            _ = rwanda_franc_one.__add__('1.00')
        assert (
            rwanda_franc_one +
            rwanda_franc_two) == rwanda_franc_three

    def test_rwanda_franc_slots(self):
        """test_rwanda_franc_slots."""
        rwanda_franc = RwandaFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RwandaFranc\' '
                    'object has no attribute \'new_variable\'')):
            rwanda_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC representation."""

from multicurrency import CFAFrancBEAC


class TestCFAFrancBEAC:
    """CFAFrancBEAC currency tests."""

    def test_cfa_franc_beac(self):
        """test_cfa_franc_beac."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac = CFAFrancBEAC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac.amount == decimal
        assert cfa_franc_beac.numeric_code == '950'
        assert cfa_franc_beac.alpha_code == 'XAF'
        assert cfa_franc_beac.decimal_places == 0
        assert cfa_franc_beac.decimal_sign == ','
        assert cfa_franc_beac.grouping_places == 3
        assert cfa_franc_beac.grouping_sign == '\u202F'
        assert not cfa_franc_beac.international
        assert cfa_franc_beac.symbol == '₣'
        assert not cfa_franc_beac.symbol_ahead
        assert cfa_franc_beac.symbol_separator == '\u00A0'
        assert cfa_franc_beac.localized_symbol == '₣'
        assert cfa_franc_beac.convertion == ''
        assert cfa_franc_beac.__hash__() == hash(
            (cfa_franc_beac.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac.__repr__() == (
            'CFAFrancBEAC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac.__str__() == '0 ₣'

    def test_cfa_franc_beac_negative(self):
        """test_cfa_franc_beac_negative."""
        amount = -100
        cfa_franc_beac = CFAFrancBEAC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac.numeric_code == '950'
        assert cfa_franc_beac.alpha_code == 'XAF'
        assert cfa_franc_beac.decimal_places == 0
        assert cfa_franc_beac.decimal_sign == ','
        assert cfa_franc_beac.grouping_places == 3
        assert cfa_franc_beac.grouping_sign == '\u202F'
        assert not cfa_franc_beac.international
        assert cfa_franc_beac.symbol == '₣'
        assert not cfa_franc_beac.symbol_ahead
        assert cfa_franc_beac.symbol_separator == '\u00A0'
        assert cfa_franc_beac.localized_symbol == '₣'
        assert cfa_franc_beac.convertion == ''
        assert cfa_franc_beac.__hash__() == hash(
            (cfa_franc_beac.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac.__repr__() == (
            'CFAFrancBEAC(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac.__str__() == '-100 ₣'

    def test_cfa_franc_beac_custom(self):
        """test_cfa_franc_beac_custom."""
        amount = 1000
        cfa_franc_beac = CFAFrancBEAC(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac.amount == decimal
        assert cfa_franc_beac.numeric_code == '950'
        assert cfa_franc_beac.alpha_code == 'XAF'
        assert cfa_franc_beac.decimal_places == 5
        assert cfa_franc_beac.decimal_sign == '\u202F'
        assert cfa_franc_beac.grouping_places == 2
        assert cfa_franc_beac.grouping_sign == ','
        assert cfa_franc_beac.international
        assert cfa_franc_beac.symbol == '₣'
        assert not cfa_franc_beac.symbol_ahead
        assert cfa_franc_beac.symbol_separator == '_'
        assert cfa_franc_beac.localized_symbol == '₣'
        assert cfa_franc_beac.convertion == ''
        assert cfa_franc_beac.__hash__() == hash(
            (cfa_franc_beac.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac.__repr__() == (
            'CFAFrancBEAC(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_changed(self):
        """test_ccfa_franc_beac_changed."""
        cfa_franc_beac = CFAFrancBEAC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac.international = True

    def test_cfa_franc_beac_math_add(self):
        """test_cfa_franc_beac_math_add."""
        cfa_franc_beac_one = CFAFrancBEAC(amount=1)
        cfa_franc_beac_two = CFAFrancBEAC(amount=2)
        cfa_franc_beac_three = CFAFrancBEAC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEAC\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_one.__add__('1.00')
        assert (
            cfa_franc_beac_one +
            cfa_franc_beac_two) == cfa_franc_beac_three

    def test_cfa_franc_beac_slots(self):
        """test_cfa_franc_beac_slots."""
        cfa_franc_beac = CFAFrancBEAC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEAC\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC CM representation."""

from multicurrency import CFAFrancBEACCM


class TestCFAFrancBEACCM:
    """CFAFrancBEACCM currency tests."""

    def test_cfa_franc_beac_cm(self):
        """test_cfa_franc_beac_cm."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_cm = CFAFrancBEACCM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cm.amount == decimal
        assert cfa_franc_beac_cm.numeric_code == '950'
        assert cfa_franc_beac_cm.alpha_code == 'XAF'
        assert cfa_franc_beac_cm.decimal_places == 0
        assert cfa_franc_beac_cm.decimal_sign == ','
        assert cfa_franc_beac_cm.grouping_places == 3
        assert cfa_franc_beac_cm.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cm.international
        assert cfa_franc_beac_cm.symbol == '₣'
        assert not cfa_franc_beac_cm.symbol_ahead
        assert cfa_franc_beac_cm.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cm.localized_symbol == 'CM₣'
        assert cfa_franc_beac_cm.convertion == ''
        assert cfa_franc_beac_cm.__hash__() == hash(
            (cfa_franc_beac_cm.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cm.__repr__() == (
            'CFAFrancBEACCM(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CM₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cm.__str__() == '0 ₣'

    def test_cfa_franc_beac_cm_negative(self):
        """test_cfa_franc_beac_cm_negative."""
        amount = -100
        cfa_franc_beac_cm = CFAFrancBEACCM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cm.numeric_code == '950'
        assert cfa_franc_beac_cm.alpha_code == 'XAF'
        assert cfa_franc_beac_cm.decimal_places == 0
        assert cfa_franc_beac_cm.decimal_sign == ','
        assert cfa_franc_beac_cm.grouping_places == 3
        assert cfa_franc_beac_cm.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cm.international
        assert cfa_franc_beac_cm.symbol == '₣'
        assert not cfa_franc_beac_cm.symbol_ahead
        assert cfa_franc_beac_cm.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cm.localized_symbol == 'CM₣'
        assert cfa_franc_beac_cm.convertion == ''
        assert cfa_franc_beac_cm.__hash__() == hash(
            (cfa_franc_beac_cm.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cm.__repr__() == (
            'CFAFrancBEACCM(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CM₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cm.__str__() == '-100 ₣'

    def test_cfa_franc_beac_cm_custom(self):
        """test_cfa_franc_beac_cm_custom."""
        amount = 1000
        cfa_franc_beac_cm = CFAFrancBEACCM(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cm.amount == decimal
        assert cfa_franc_beac_cm.numeric_code == '950'
        assert cfa_franc_beac_cm.alpha_code == 'XAF'
        assert cfa_franc_beac_cm.decimal_places == 5
        assert cfa_franc_beac_cm.decimal_sign == '\u202F'
        assert cfa_franc_beac_cm.grouping_places == 2
        assert cfa_franc_beac_cm.grouping_sign == ','
        assert cfa_franc_beac_cm.international
        assert cfa_franc_beac_cm.symbol == '₣'
        assert not cfa_franc_beac_cm.symbol_ahead
        assert cfa_franc_beac_cm.symbol_separator == '_'
        assert cfa_franc_beac_cm.localized_symbol == 'CM₣'
        assert cfa_franc_beac_cm.convertion == ''
        assert cfa_franc_beac_cm.__hash__() == hash(
            (cfa_franc_beac_cm.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cm.__repr__() == (
            'CFAFrancBEACCM(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CM₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_cm.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_cm_changed(self):
        """test_ccfa_franc_beac_cm_changed."""
        cfa_franc_beac_cm = CFAFrancBEACCM(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cm.international = True

    def test_cfa_franc_beac_cm_math_add(self):
        """test_cfa_franc_beac_cm_math_add."""
        cfa_franc_beac_cm_one = CFAFrancBEACCM(amount=1)
        cfa_franc_beac_cm_two = CFAFrancBEACCM(amount=2)
        cfa_franc_beac_cm_three = CFAFrancBEACCM(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_cm_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACCM\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_cm_one.__add__('1.00')
        assert (
            cfa_franc_beac_cm_one +
            cfa_franc_beac_cm_two) == cfa_franc_beac_cm_three

    def test_cfa_franc_beac_cm_slots(self):
        """test_cfa_franc_beac_cm_slots."""
        cfa_franc_beac_cm = CFAFrancBEACCM(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACCM\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_cm.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC CF representation."""

from multicurrency import CFAFrancBEACCF


class TestCFAFrancBEACCF:
    """CFAFrancBEACCF currency tests."""

    def test_cfa_franc_beac_cf(self):
        """test_cfa_franc_beac_cf."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_cf = CFAFrancBEACCF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cf.amount == decimal
        assert cfa_franc_beac_cf.numeric_code == '950'
        assert cfa_franc_beac_cf.alpha_code == 'XAF'
        assert cfa_franc_beac_cf.decimal_places == 0
        assert cfa_franc_beac_cf.decimal_sign == ','
        assert cfa_franc_beac_cf.grouping_places == 3
        assert cfa_franc_beac_cf.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cf.international
        assert cfa_franc_beac_cf.symbol == '₣'
        assert not cfa_franc_beac_cf.symbol_ahead
        assert cfa_franc_beac_cf.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cf.localized_symbol == 'CF₣'
        assert cfa_franc_beac_cf.convertion == ''
        assert cfa_franc_beac_cf.__hash__() == hash(
            (cfa_franc_beac_cf.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cf.__repr__() == (
            'CFAFrancBEACCF(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CF₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cf.__str__() == '0 ₣'

    def test_cfa_franc_beac_cf_negative(self):
        """test_cfa_franc_beac_cf_negative."""
        amount = -100
        cfa_franc_beac_cf = CFAFrancBEACCF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cf.numeric_code == '950'
        assert cfa_franc_beac_cf.alpha_code == 'XAF'
        assert cfa_franc_beac_cf.decimal_places == 0
        assert cfa_franc_beac_cf.decimal_sign == ','
        assert cfa_franc_beac_cf.grouping_places == 3
        assert cfa_franc_beac_cf.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cf.international
        assert cfa_franc_beac_cf.symbol == '₣'
        assert not cfa_franc_beac_cf.symbol_ahead
        assert cfa_franc_beac_cf.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cf.localized_symbol == 'CF₣'
        assert cfa_franc_beac_cf.convertion == ''
        assert cfa_franc_beac_cf.__hash__() == hash(
            (cfa_franc_beac_cf.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cf.__repr__() == (
            'CFAFrancBEACCF(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CF₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cf.__str__() == '-100 ₣'

    def test_cfa_franc_beac_cf_custom(self):
        """test_cfa_franc_beac_cf_custom."""
        amount = 1000
        cfa_franc_beac_cf = CFAFrancBEACCF(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cf.amount == decimal
        assert cfa_franc_beac_cf.numeric_code == '950'
        assert cfa_franc_beac_cf.alpha_code == 'XAF'
        assert cfa_franc_beac_cf.decimal_places == 5
        assert cfa_franc_beac_cf.decimal_sign == '\u202F'
        assert cfa_franc_beac_cf.grouping_places == 2
        assert cfa_franc_beac_cf.grouping_sign == ','
        assert cfa_franc_beac_cf.international
        assert cfa_franc_beac_cf.symbol == '₣'
        assert not cfa_franc_beac_cf.symbol_ahead
        assert cfa_franc_beac_cf.symbol_separator == '_'
        assert cfa_franc_beac_cf.localized_symbol == 'CF₣'
        assert cfa_franc_beac_cf.convertion == ''
        assert cfa_franc_beac_cf.__hash__() == hash(
            (cfa_franc_beac_cf.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cf.__repr__() == (
            'CFAFrancBEACCF(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CF₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_cf.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_cf_changed(self):
        """test_ccfa_franc_beac_cf_changed."""
        cfa_franc_beac_cf = CFAFrancBEACCF(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cf.international = True

    def test_cfa_franc_beac_cf_math_add(self):
        """test_cfa_franc_beac_cf_math_add."""
        cfa_franc_beac_cf_one = CFAFrancBEACCF(amount=1)
        cfa_franc_beac_cf_two = CFAFrancBEACCF(amount=2)
        cfa_franc_beac_cf_three = CFAFrancBEACCF(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_cf_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACCF\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_cf_one.__add__('1.00')
        assert (
            cfa_franc_beac_cf_one +
            cfa_franc_beac_cf_two) == cfa_franc_beac_cf_three

    def test_cfa_franc_beac_cf_slots(self):
        """test_cfa_franc_beac_cf_slots."""
        cfa_franc_beac_cf = CFAFrancBEACCF(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACCF\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_cf.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC TD representation."""

from multicurrency import CFAFrancBEACTD


class TestCFAFrancBEACTD:
    """CFAFrancBEACTD currency tests."""

    def test_cfa_franc_beac_td(self):
        """test_cfa_franc_beac_td."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_td = CFAFrancBEACTD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_td.amount == decimal
        assert cfa_franc_beac_td.numeric_code == '950'
        assert cfa_franc_beac_td.alpha_code == 'XAF'
        assert cfa_franc_beac_td.decimal_places == 0
        assert cfa_franc_beac_td.decimal_sign == ','
        assert cfa_franc_beac_td.grouping_places == 3
        assert cfa_franc_beac_td.grouping_sign == '\u202F'
        assert not cfa_franc_beac_td.international
        assert cfa_franc_beac_td.symbol == '₣'
        assert not cfa_franc_beac_td.symbol_ahead
        assert cfa_franc_beac_td.symbol_separator == '\u00A0'
        assert cfa_franc_beac_td.localized_symbol == 'TD₣'
        assert cfa_franc_beac_td.convertion == ''
        assert cfa_franc_beac_td.__hash__() == hash(
            (cfa_franc_beac_td.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_td.__repr__() == (
            'CFAFrancBEACTD(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TD₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_td.__str__() == '0 ₣'

    def test_cfa_franc_beac_td_negative(self):
        """test_cfa_franc_beac_td_negative."""
        amount = -100
        cfa_franc_beac_td = CFAFrancBEACTD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_td.numeric_code == '950'
        assert cfa_franc_beac_td.alpha_code == 'XAF'
        assert cfa_franc_beac_td.decimal_places == 0
        assert cfa_franc_beac_td.decimal_sign == ','
        assert cfa_franc_beac_td.grouping_places == 3
        assert cfa_franc_beac_td.grouping_sign == '\u202F'
        assert not cfa_franc_beac_td.international
        assert cfa_franc_beac_td.symbol == '₣'
        assert not cfa_franc_beac_td.symbol_ahead
        assert cfa_franc_beac_td.symbol_separator == '\u00A0'
        assert cfa_franc_beac_td.localized_symbol == 'TD₣'
        assert cfa_franc_beac_td.convertion == ''
        assert cfa_franc_beac_td.__hash__() == hash(
            (cfa_franc_beac_td.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_td.__repr__() == (
            'CFAFrancBEACTD(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TD₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_td.__str__() == '-100 ₣'

    def test_cfa_franc_beac_td_custom(self):
        """test_cfa_franc_beac_td_custom."""
        amount = 1000
        cfa_franc_beac_td = CFAFrancBEACTD(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_td.amount == decimal
        assert cfa_franc_beac_td.numeric_code == '950'
        assert cfa_franc_beac_td.alpha_code == 'XAF'
        assert cfa_franc_beac_td.decimal_places == 5
        assert cfa_franc_beac_td.decimal_sign == '\u202F'
        assert cfa_franc_beac_td.grouping_places == 2
        assert cfa_franc_beac_td.grouping_sign == ','
        assert cfa_franc_beac_td.international
        assert cfa_franc_beac_td.symbol == '₣'
        assert not cfa_franc_beac_td.symbol_ahead
        assert cfa_franc_beac_td.symbol_separator == '_'
        assert cfa_franc_beac_td.localized_symbol == 'TD₣'
        assert cfa_franc_beac_td.convertion == ''
        assert cfa_franc_beac_td.__hash__() == hash(
            (cfa_franc_beac_td.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_td.__repr__() == (
            'CFAFrancBEACTD(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TD₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_td.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_td_changed(self):
        """test_ccfa_franc_beac_td_changed."""
        cfa_franc_beac_td = CFAFrancBEACTD(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_td.international = True

    def test_cfa_franc_beac_td_math_add(self):
        """test_cfa_franc_beac_td_math_add."""
        cfa_franc_beac_td_one = CFAFrancBEACTD(amount=1)
        cfa_franc_beac_td_two = CFAFrancBEACTD(amount=2)
        cfa_franc_beac_td_three = CFAFrancBEACTD(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_td_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACTD\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_td_one.__add__('1.00')
        assert (
            cfa_franc_beac_td_one +
            cfa_franc_beac_td_two) == cfa_franc_beac_td_three

    def test_cfa_franc_beac_td_slots(self):
        """test_cfa_franc_beac_td_slots."""
        cfa_franc_beac_td = CFAFrancBEACTD(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACTD\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_td.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC CD representation."""

from multicurrency import CFAFrancBEACCD


class TestCFAFrancBEACCD:
    """CFAFrancBEACCD currency tests."""

    def test_cfa_franc_beac_cd(self):
        """test_cfa_franc_beac_cd."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_cd = CFAFrancBEACCD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cd.amount == decimal
        assert cfa_franc_beac_cd.numeric_code == '950'
        assert cfa_franc_beac_cd.alpha_code == 'XAF'
        assert cfa_franc_beac_cd.decimal_places == 0
        assert cfa_franc_beac_cd.decimal_sign == ','
        assert cfa_franc_beac_cd.grouping_places == 3
        assert cfa_franc_beac_cd.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cd.international
        assert cfa_franc_beac_cd.symbol == '₣'
        assert not cfa_franc_beac_cd.symbol_ahead
        assert cfa_franc_beac_cd.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cd.localized_symbol == 'CD₣'
        assert cfa_franc_beac_cd.convertion == ''
        assert cfa_franc_beac_cd.__hash__() == hash(
            (cfa_franc_beac_cd.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cd.__repr__() == (
            'CFAFrancBEACCD(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CD₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cd.__str__() == '0 ₣'

    def test_cfa_franc_beac_cd_negative(self):
        """test_cfa_franc_beac_cd_negative."""
        amount = -100
        cfa_franc_beac_cd = CFAFrancBEACCD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cd.numeric_code == '950'
        assert cfa_franc_beac_cd.alpha_code == 'XAF'
        assert cfa_franc_beac_cd.decimal_places == 0
        assert cfa_franc_beac_cd.decimal_sign == ','
        assert cfa_franc_beac_cd.grouping_places == 3
        assert cfa_franc_beac_cd.grouping_sign == '\u202F'
        assert not cfa_franc_beac_cd.international
        assert cfa_franc_beac_cd.symbol == '₣'
        assert not cfa_franc_beac_cd.symbol_ahead
        assert cfa_franc_beac_cd.symbol_separator == '\u00A0'
        assert cfa_franc_beac_cd.localized_symbol == 'CD₣'
        assert cfa_franc_beac_cd.convertion == ''
        assert cfa_franc_beac_cd.__hash__() == hash(
            (cfa_franc_beac_cd.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cd.__repr__() == (
            'CFAFrancBEACCD(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CD₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_cd.__str__() == '-100 ₣'

    def test_cfa_franc_beac_cd_custom(self):
        """test_cfa_franc_beac_cd_custom."""
        amount = 1000
        cfa_franc_beac_cd = CFAFrancBEACCD(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_cd.amount == decimal
        assert cfa_franc_beac_cd.numeric_code == '950'
        assert cfa_franc_beac_cd.alpha_code == 'XAF'
        assert cfa_franc_beac_cd.decimal_places == 5
        assert cfa_franc_beac_cd.decimal_sign == '\u202F'
        assert cfa_franc_beac_cd.grouping_places == 2
        assert cfa_franc_beac_cd.grouping_sign == ','
        assert cfa_franc_beac_cd.international
        assert cfa_franc_beac_cd.symbol == '₣'
        assert not cfa_franc_beac_cd.symbol_ahead
        assert cfa_franc_beac_cd.symbol_separator == '_'
        assert cfa_franc_beac_cd.localized_symbol == 'CD₣'
        assert cfa_franc_beac_cd.convertion == ''
        assert cfa_franc_beac_cd.__hash__() == hash(
            (cfa_franc_beac_cd.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_cd.__repr__() == (
            'CFAFrancBEACCD(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CD₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_cd.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_cd_changed(self):
        """test_ccfa_franc_beac_cd_changed."""
        cfa_franc_beac_cd = CFAFrancBEACCD(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_cd.international = True

    def test_cfa_franc_beac_cd_math_add(self):
        """test_cfa_franc_beac_cd_math_add."""
        cfa_franc_beac_cd_one = CFAFrancBEACCD(amount=1)
        cfa_franc_beac_cd_two = CFAFrancBEACCD(amount=2)
        cfa_franc_beac_cd_three = CFAFrancBEACCD(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_cd_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACCD\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_cd_one.__add__('1.00')
        assert (
            cfa_franc_beac_cd_one +
            cfa_franc_beac_cd_two) == cfa_franc_beac_cd_three

    def test_cfa_franc_beac_cd_slots(self):
        """test_cfa_franc_beac_cd_slots."""
        cfa_franc_beac_cd = CFAFrancBEACCD(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACCD\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_cd.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC GQ representation."""

from multicurrency import CFAFrancBEACGQ


class TestCFAFrancBEACGQ:
    """CFAFrancBEACGQ currency tests."""

    def test_cfa_franc_beac_gq(self):
        """test_cfa_franc_beac_gq."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_gq = CFAFrancBEACGQ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_gq.amount == decimal
        assert cfa_franc_beac_gq.numeric_code == '950'
        assert cfa_franc_beac_gq.alpha_code == 'XAF'
        assert cfa_franc_beac_gq.decimal_places == 0
        assert cfa_franc_beac_gq.decimal_sign == ','
        assert cfa_franc_beac_gq.grouping_places == 3
        assert cfa_franc_beac_gq.grouping_sign == '\u202F'
        assert not cfa_franc_beac_gq.international
        assert cfa_franc_beac_gq.symbol == '₣'
        assert not cfa_franc_beac_gq.symbol_ahead
        assert cfa_franc_beac_gq.symbol_separator == '\u00A0'
        assert cfa_franc_beac_gq.localized_symbol == 'GQ₣'
        assert cfa_franc_beac_gq.convertion == ''
        assert cfa_franc_beac_gq.__hash__() == hash(
            (cfa_franc_beac_gq.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_gq.__repr__() == (
            'CFAFrancBEACGQ(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GQ₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_gq.__str__() == '0 ₣'

    def test_cfa_franc_beac_gq_negative(self):
        """test_cfa_franc_beac_gq_negative."""
        amount = -100
        cfa_franc_beac_gq = CFAFrancBEACGQ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_gq.numeric_code == '950'
        assert cfa_franc_beac_gq.alpha_code == 'XAF'
        assert cfa_franc_beac_gq.decimal_places == 0
        assert cfa_franc_beac_gq.decimal_sign == ','
        assert cfa_franc_beac_gq.grouping_places == 3
        assert cfa_franc_beac_gq.grouping_sign == '\u202F'
        assert not cfa_franc_beac_gq.international
        assert cfa_franc_beac_gq.symbol == '₣'
        assert not cfa_franc_beac_gq.symbol_ahead
        assert cfa_franc_beac_gq.symbol_separator == '\u00A0'
        assert cfa_franc_beac_gq.localized_symbol == 'GQ₣'
        assert cfa_franc_beac_gq.convertion == ''
        assert cfa_franc_beac_gq.__hash__() == hash(
            (cfa_franc_beac_gq.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_gq.__repr__() == (
            'CFAFrancBEACGQ(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GQ₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_gq.__str__() == '-100 ₣'

    def test_cfa_franc_beac_gq_custom(self):
        """test_cfa_franc_beac_gq_custom."""
        amount = 1000
        cfa_franc_beac_gq = CFAFrancBEACGQ(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_gq.amount == decimal
        assert cfa_franc_beac_gq.numeric_code == '950'
        assert cfa_franc_beac_gq.alpha_code == 'XAF'
        assert cfa_franc_beac_gq.decimal_places == 5
        assert cfa_franc_beac_gq.decimal_sign == '\u202F'
        assert cfa_franc_beac_gq.grouping_places == 2
        assert cfa_franc_beac_gq.grouping_sign == ','
        assert cfa_franc_beac_gq.international
        assert cfa_franc_beac_gq.symbol == '₣'
        assert not cfa_franc_beac_gq.symbol_ahead
        assert cfa_franc_beac_gq.symbol_separator == '_'
        assert cfa_franc_beac_gq.localized_symbol == 'GQ₣'
        assert cfa_franc_beac_gq.convertion == ''
        assert cfa_franc_beac_gq.__hash__() == hash(
            (cfa_franc_beac_gq.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_gq.__repr__() == (
            'CFAFrancBEACGQ(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GQ₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_gq.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_gq_changed(self):
        """test_ccfa_franc_beac_gq_changed."""
        cfa_franc_beac_gq = CFAFrancBEACGQ(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_gq.international = True

    def test_cfa_franc_beac_gq_math_add(self):
        """test_cfa_franc_beac_gq_math_add."""
        cfa_franc_beac_gq_one = CFAFrancBEACGQ(amount=1)
        cfa_franc_beac_gq_two = CFAFrancBEACGQ(amount=2)
        cfa_franc_beac_gq_three = CFAFrancBEACGQ(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_gq_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACGQ\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_gq_one.__add__('1.00')
        assert (
            cfa_franc_beac_gq_one +
            cfa_franc_beac_gq_two) == cfa_franc_beac_gq_three

    def test_cfa_franc_beac_gq_slots(self):
        """test_cfa_franc_beac_gq_slots."""
        cfa_franc_beac_gq = CFAFrancBEACGQ(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACGQ\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_gq.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BEAC GA representation."""

from multicurrency import CFAFrancBEACGA


class TestCFAFrancBEACGA:
    """CFAFrancBEACGA currency tests."""

    def test_cfa_franc_beac_ga(self):
        """test_cfa_franc_beac_ga."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_beac_ga = CFAFrancBEACGA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_ga.amount == decimal
        assert cfa_franc_beac_ga.numeric_code == '950'
        assert cfa_franc_beac_ga.alpha_code == 'XAF'
        assert cfa_franc_beac_ga.decimal_places == 0
        assert cfa_franc_beac_ga.decimal_sign == ','
        assert cfa_franc_beac_ga.grouping_places == 3
        assert cfa_franc_beac_ga.grouping_sign == '\u202F'
        assert not cfa_franc_beac_ga.international
        assert cfa_franc_beac_ga.symbol == '₣'
        assert not cfa_franc_beac_ga.symbol_ahead
        assert cfa_franc_beac_ga.symbol_separator == '\u00A0'
        assert cfa_franc_beac_ga.localized_symbol == 'GA₣'
        assert cfa_franc_beac_ga.convertion == ''
        assert cfa_franc_beac_ga.__hash__() == hash(
            (cfa_franc_beac_ga.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_ga.__repr__() == (
            'CFAFrancBEACGA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GA₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_ga.__str__() == '0 ₣'

    def test_cfa_franc_beac_ga_negative(self):
        """test_cfa_franc_beac_ga_negative."""
        amount = -100
        cfa_franc_beac_ga = CFAFrancBEACGA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_ga.numeric_code == '950'
        assert cfa_franc_beac_ga.alpha_code == 'XAF'
        assert cfa_franc_beac_ga.decimal_places == 0
        assert cfa_franc_beac_ga.decimal_sign == ','
        assert cfa_franc_beac_ga.grouping_places == 3
        assert cfa_franc_beac_ga.grouping_sign == '\u202F'
        assert not cfa_franc_beac_ga.international
        assert cfa_franc_beac_ga.symbol == '₣'
        assert not cfa_franc_beac_ga.symbol_ahead
        assert cfa_franc_beac_ga.symbol_separator == '\u00A0'
        assert cfa_franc_beac_ga.localized_symbol == 'GA₣'
        assert cfa_franc_beac_ga.convertion == ''
        assert cfa_franc_beac_ga.__hash__() == hash(
            (cfa_franc_beac_ga.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_ga.__repr__() == (
            'CFAFrancBEACGA(amount: -100, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GA₣", '
            'numeric_code: "950", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_beac_ga.__str__() == '-100 ₣'

    def test_cfa_franc_beac_ga_custom(self):
        """test_cfa_franc_beac_ga_custom."""
        amount = 1000
        cfa_franc_beac_ga = CFAFrancBEACGA(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_beac_ga.amount == decimal
        assert cfa_franc_beac_ga.numeric_code == '950'
        assert cfa_franc_beac_ga.alpha_code == 'XAF'
        assert cfa_franc_beac_ga.decimal_places == 5
        assert cfa_franc_beac_ga.decimal_sign == '\u202F'
        assert cfa_franc_beac_ga.grouping_places == 2
        assert cfa_franc_beac_ga.grouping_sign == ','
        assert cfa_franc_beac_ga.international
        assert cfa_franc_beac_ga.symbol == '₣'
        assert not cfa_franc_beac_ga.symbol_ahead
        assert cfa_franc_beac_ga.symbol_separator == '_'
        assert cfa_franc_beac_ga.localized_symbol == 'GA₣'
        assert cfa_franc_beac_ga.convertion == ''
        assert cfa_franc_beac_ga.__hash__() == hash(
            (cfa_franc_beac_ga.__class__, decimal, 'XAF', '950'))
        assert cfa_franc_beac_ga.__repr__() == (
            'CFAFrancBEACGA(amount: 1000, '
            'alpha_code: "XAF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GA₣", '
            'numeric_code: "950", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_beac_ga.__str__() == 'XAF 10,00.00000'

    def test_cfa_franc_beac_ga_changed(self):
        """test_ccfa_franc_beac_ga_changed."""
        cfa_franc_beac_ga = CFAFrancBEACGA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_beac_ga.international = True

    def test_cfa_franc_beac_ga_math_add(self):
        """test_cfa_franc_beac_ga_math_add."""
        cfa_franc_beac_ga_one = CFAFrancBEACGA(amount=1)
        cfa_franc_beac_ga_two = CFAFrancBEACGA(amount=2)
        cfa_franc_beac_ga_three = CFAFrancBEACGA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XAF and OTHER.'):
            _ = cfa_franc_beac_ga_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBEACGA\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_beac_ga_one.__add__('1.00')
        assert (
            cfa_franc_beac_ga_one +
            cfa_franc_beac_ga_two) == cfa_franc_beac_ga_three

    def test_cfa_franc_beac_ga_slots(self):
        """test_cfa_franc_beac_ga_slots."""
        cfa_franc_beac_ga = CFAFrancBEACGA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBEACGA\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_beac_ga.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO representation."""

from multicurrency import CFAFrancBCEAO


class TestCFAFrancBCEAO:
    """CFAFrancBCEAO currency tests."""

    def test_cfa_franc_bceao(self):
        """test_cfa_franc_bceao."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao = CFAFrancBCEAO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao.amount == decimal
        assert cfa_franc_bceao.numeric_code == '952'
        assert cfa_franc_bceao.alpha_code == 'XOF'
        assert cfa_franc_bceao.decimal_places == 0
        assert cfa_franc_bceao.decimal_sign == ','
        assert cfa_franc_bceao.grouping_places == 3
        assert cfa_franc_bceao.grouping_sign == '\u202F'
        assert not cfa_franc_bceao.international
        assert cfa_franc_bceao.symbol == '₣'
        assert not cfa_franc_bceao.symbol_ahead
        assert cfa_franc_bceao.symbol_separator == '\u00A0'
        assert cfa_franc_bceao.localized_symbol == '₣'
        assert cfa_franc_bceao.convertion == ''
        assert cfa_franc_bceao.__hash__() == hash(
            (cfa_franc_bceao.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao.__repr__() == (
            'CFAFrancBCEAO(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao.__str__() == '0 ₣'

    def test_cfa_franc_bceao_negative(self):
        """test_cfa_franc_bceao_negative."""
        amount = -100
        cfa_franc_bceao = CFAFrancBCEAO(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao.numeric_code == '952'
        assert cfa_franc_bceao.alpha_code == 'XOF'
        assert cfa_franc_bceao.decimal_places == 0
        assert cfa_franc_bceao.decimal_sign == ','
        assert cfa_franc_bceao.grouping_places == 3
        assert cfa_franc_bceao.grouping_sign == '\u202F'
        assert not cfa_franc_bceao.international
        assert cfa_franc_bceao.symbol == '₣'
        assert not cfa_franc_bceao.symbol_ahead
        assert cfa_franc_bceao.symbol_separator == '\u00A0'
        assert cfa_franc_bceao.localized_symbol == '₣'
        assert cfa_franc_bceao.convertion == ''
        assert cfa_franc_bceao.__hash__() == hash(
            (cfa_franc_bceao.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao.__repr__() == (
            'CFAFrancBCEAO(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_custom(self):
        """test_cfa_franc_bceao_custom."""
        amount = 1000
        cfa_franc_bceao = CFAFrancBCEAO(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao.amount == decimal
        assert cfa_franc_bceao.numeric_code == '952'
        assert cfa_franc_bceao.alpha_code == 'XOF'
        assert cfa_franc_bceao.decimal_places == 5
        assert cfa_franc_bceao.decimal_sign == '\u202F'
        assert cfa_franc_bceao.grouping_places == 2
        assert cfa_franc_bceao.grouping_sign == ','
        assert cfa_franc_bceao.international
        assert cfa_franc_bceao.symbol == '₣'
        assert not cfa_franc_bceao.symbol_ahead
        assert cfa_franc_bceao.symbol_separator == '_'
        assert cfa_franc_bceao.localized_symbol == '₣'
        assert cfa_franc_bceao.convertion == ''
        assert cfa_franc_bceao.__hash__() == hash(
            (cfa_franc_bceao.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao.__repr__() == (
            'CFAFrancBCEAO(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_changed(self):
        """test_ccfa_franc_bceao_changed."""
        cfa_franc_bceao = CFAFrancBCEAO(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao.international = True

    def test_cfa_franc_bceao_math_add(self):
        """test_cfa_franc_bceao_math_add."""
        cfa_franc_bceao_one = CFAFrancBCEAO(amount=1)
        cfa_franc_bceao_two = CFAFrancBCEAO(amount=2)
        cfa_franc_bceao_three = CFAFrancBCEAO(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAO\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_one.__add__('1.00')
        assert (
            cfa_franc_bceao_one +
            cfa_franc_bceao_two) == cfa_franc_bceao_three

    def test_cfa_franc_bceao_slots(self):
        """test_cfa_franc_bceao_slots."""
        cfa_franc_bceao = CFAFrancBCEAO(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAO\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO BJ representation."""

from multicurrency import CFAFrancBCEAOBJ


class TestCFAFrancBCEAOBJ:
    """CFAFrancBCEAOBJ currency tests."""

    def test_cfa_franc_bceao_bj(self):
        """test_cfa_franc_bceao_bj."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_bj = CFAFrancBCEAOBJ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bj.amount == decimal
        assert cfa_franc_bceao_bj.numeric_code == '952'
        assert cfa_franc_bceao_bj.alpha_code == 'XOF'
        assert cfa_franc_bceao_bj.decimal_places == 0
        assert cfa_franc_bceao_bj.decimal_sign == ','
        assert cfa_franc_bceao_bj.grouping_places == 3
        assert cfa_franc_bceao_bj.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_bj.international
        assert cfa_franc_bceao_bj.symbol == '₣'
        assert not cfa_franc_bceao_bj.symbol_ahead
        assert cfa_franc_bceao_bj.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_bj.localized_symbol == 'BJ₣'
        assert cfa_franc_bceao_bj.convertion == ''
        assert cfa_franc_bceao_bj.__hash__() == hash(
            (cfa_franc_bceao_bj.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bj.__repr__() == (
            'CFAFrancBCEAOBJ(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BJ₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_bj.__str__() == '0 ₣'

    def test_cfa_franc_bceao_bj_negative(self):
        """test_cfa_franc_bceao_bj_negative."""
        amount = -100
        cfa_franc_bceao_bj = CFAFrancBCEAOBJ(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bj.numeric_code == '952'
        assert cfa_franc_bceao_bj.alpha_code == 'XOF'
        assert cfa_franc_bceao_bj.decimal_places == 0
        assert cfa_franc_bceao_bj.decimal_sign == ','
        assert cfa_franc_bceao_bj.grouping_places == 3
        assert cfa_franc_bceao_bj.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_bj.international
        assert cfa_franc_bceao_bj.symbol == '₣'
        assert not cfa_franc_bceao_bj.symbol_ahead
        assert cfa_franc_bceao_bj.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_bj.localized_symbol == 'BJ₣'
        assert cfa_franc_bceao_bj.convertion == ''
        assert cfa_franc_bceao_bj.__hash__() == hash(
            (cfa_franc_bceao_bj.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bj.__repr__() == (
            'CFAFrancBCEAOBJ(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BJ₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_bj.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_bj_custom(self):
        """test_cfa_franc_bceao_bj_custom."""
        amount = 1000
        cfa_franc_bceao_bj = CFAFrancBCEAOBJ(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bj.amount == decimal
        assert cfa_franc_bceao_bj.numeric_code == '952'
        assert cfa_franc_bceao_bj.alpha_code == 'XOF'
        assert cfa_franc_bceao_bj.decimal_places == 5
        assert cfa_franc_bceao_bj.decimal_sign == '\u202F'
        assert cfa_franc_bceao_bj.grouping_places == 2
        assert cfa_franc_bceao_bj.grouping_sign == ','
        assert cfa_franc_bceao_bj.international
        assert cfa_franc_bceao_bj.symbol == '₣'
        assert not cfa_franc_bceao_bj.symbol_ahead
        assert cfa_franc_bceao_bj.symbol_separator == '_'
        assert cfa_franc_bceao_bj.localized_symbol == 'BJ₣'
        assert cfa_franc_bceao_bj.convertion == ''
        assert cfa_franc_bceao_bj.__hash__() == hash(
            (cfa_franc_bceao_bj.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bj.__repr__() == (
            'CFAFrancBCEAOBJ(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BJ₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_bj.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_bj_changed(self):
        """test_ccfa_franc_bceao_bj_changed."""
        cfa_franc_bceao_bj = CFAFrancBCEAOBJ(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bj.international = True

    def test_cfa_franc_bceao_bj_math_add(self):
        """test_cfa_franc_bceao_bj_math_add."""
        cfa_franc_bceao_bj_one = CFAFrancBCEAOBJ(amount=1)
        cfa_franc_bceao_bj_two = CFAFrancBCEAOBJ(amount=2)
        cfa_franc_bceao_bj_three = CFAFrancBCEAOBJ(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_bj_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOBJ\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_bj_one.__add__('1.00')
        assert (
            cfa_franc_bceao_bj_one +
            cfa_franc_bceao_bj_two) == cfa_franc_bceao_bj_three

    def test_cfa_franc_bceao_bj_slots(self):
        """test_cfa_franc_bceao_bj_slots."""
        cfa_franc_bceao_bj = CFAFrancBCEAOBJ(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOBJ\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_bj.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO BF representation."""

from multicurrency import CFAFrancBCEAOBF


class TestCFAFrancBCEAOBF:
    """CFAFrancBCEAOBF currency tests."""

    def test_cfa_franc_bceao_bf(self):
        """test_cfa_franc_bceao_bf."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_bf = CFAFrancBCEAOBF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bf.amount == decimal
        assert cfa_franc_bceao_bf.numeric_code == '952'
        assert cfa_franc_bceao_bf.alpha_code == 'XOF'
        assert cfa_franc_bceao_bf.decimal_places == 0
        assert cfa_franc_bceao_bf.decimal_sign == ','
        assert cfa_franc_bceao_bf.grouping_places == 3
        assert cfa_franc_bceao_bf.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_bf.international
        assert cfa_franc_bceao_bf.symbol == '₣'
        assert not cfa_franc_bceao_bf.symbol_ahead
        assert cfa_franc_bceao_bf.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_bf.localized_symbol == 'BF₣'
        assert cfa_franc_bceao_bf.convertion == ''
        assert cfa_franc_bceao_bf.__hash__() == hash(
            (cfa_franc_bceao_bf.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bf.__repr__() == (
            'CFAFrancBCEAOBF(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BF₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_bf.__str__() == '0 ₣'

    def test_cfa_franc_bceao_bf_negative(self):
        """test_cfa_franc_bceao_bf_negative."""
        amount = -100
        cfa_franc_bceao_bf = CFAFrancBCEAOBF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bf.numeric_code == '952'
        assert cfa_franc_bceao_bf.alpha_code == 'XOF'
        assert cfa_franc_bceao_bf.decimal_places == 0
        assert cfa_franc_bceao_bf.decimal_sign == ','
        assert cfa_franc_bceao_bf.grouping_places == 3
        assert cfa_franc_bceao_bf.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_bf.international
        assert cfa_franc_bceao_bf.symbol == '₣'
        assert not cfa_franc_bceao_bf.symbol_ahead
        assert cfa_franc_bceao_bf.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_bf.localized_symbol == 'BF₣'
        assert cfa_franc_bceao_bf.convertion == ''
        assert cfa_franc_bceao_bf.__hash__() == hash(
            (cfa_franc_bceao_bf.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bf.__repr__() == (
            'CFAFrancBCEAOBF(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BF₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_bf.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_bf_custom(self):
        """test_cfa_franc_bceao_bf_custom."""
        amount = 1000
        cfa_franc_bceao_bf = CFAFrancBCEAOBF(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_bf.amount == decimal
        assert cfa_franc_bceao_bf.numeric_code == '952'
        assert cfa_franc_bceao_bf.alpha_code == 'XOF'
        assert cfa_franc_bceao_bf.decimal_places == 5
        assert cfa_franc_bceao_bf.decimal_sign == '\u202F'
        assert cfa_franc_bceao_bf.grouping_places == 2
        assert cfa_franc_bceao_bf.grouping_sign == ','
        assert cfa_franc_bceao_bf.international
        assert cfa_franc_bceao_bf.symbol == '₣'
        assert not cfa_franc_bceao_bf.symbol_ahead
        assert cfa_franc_bceao_bf.symbol_separator == '_'
        assert cfa_franc_bceao_bf.localized_symbol == 'BF₣'
        assert cfa_franc_bceao_bf.convertion == ''
        assert cfa_franc_bceao_bf.__hash__() == hash(
            (cfa_franc_bceao_bf.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_bf.__repr__() == (
            'CFAFrancBCEAOBF(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BF₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_bf.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_bf_changed(self):
        """test_ccfa_franc_bceao_bf_changed."""
        cfa_franc_bceao_bf = CFAFrancBCEAOBF(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_bf.international = True

    def test_cfa_franc_bceao_bf_math_add(self):
        """test_cfa_franc_bceao_bf_math_add."""
        cfa_franc_bceao_bf_one = CFAFrancBCEAOBF(amount=1)
        cfa_franc_bceao_bf_two = CFAFrancBCEAOBF(amount=2)
        cfa_franc_bceao_bf_three = CFAFrancBCEAOBF(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_bf_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOBF\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_bf_one.__add__('1.00')
        assert (
            cfa_franc_bceao_bf_one +
            cfa_franc_bceao_bf_two) == cfa_franc_bceao_bf_three

    def test_cfa_franc_bceao_bf_slots(self):
        """test_cfa_franc_bceao_bf_slots."""
        cfa_franc_bceao_bf = CFAFrancBCEAOBF(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOBF\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_bf.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO CI representation."""

from multicurrency import CFAFrancBCEAOCI


class TestCFAFrancBCEAOCI:
    """CFAFrancBCEAOCI currency tests."""

    def test_cfa_franc_bceao_ci(self):
        """test_cfa_franc_bceao_ci."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_ci = CFAFrancBCEAOCI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ci.amount == decimal
        assert cfa_franc_bceao_ci.numeric_code == '952'
        assert cfa_franc_bceao_ci.alpha_code == 'XOF'
        assert cfa_franc_bceao_ci.decimal_places == 0
        assert cfa_franc_bceao_ci.decimal_sign == ','
        assert cfa_franc_bceao_ci.grouping_places == 3
        assert cfa_franc_bceao_ci.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ci.international
        assert cfa_franc_bceao_ci.symbol == '₣'
        assert not cfa_franc_bceao_ci.symbol_ahead
        assert cfa_franc_bceao_ci.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ci.localized_symbol == 'CI₣'
        assert cfa_franc_bceao_ci.convertion == ''
        assert cfa_franc_bceao_ci.__hash__() == hash(
            (cfa_franc_bceao_ci.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ci.__repr__() == (
            'CFAFrancBCEAOCI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CI₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ci.__str__() == '0 ₣'

    def test_cfa_franc_bceao_ci_negative(self):
        """test_cfa_franc_bceao_ci_negative."""
        amount = -100
        cfa_franc_bceao_ci = CFAFrancBCEAOCI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ci.numeric_code == '952'
        assert cfa_franc_bceao_ci.alpha_code == 'XOF'
        assert cfa_franc_bceao_ci.decimal_places == 0
        assert cfa_franc_bceao_ci.decimal_sign == ','
        assert cfa_franc_bceao_ci.grouping_places == 3
        assert cfa_franc_bceao_ci.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ci.international
        assert cfa_franc_bceao_ci.symbol == '₣'
        assert not cfa_franc_bceao_ci.symbol_ahead
        assert cfa_franc_bceao_ci.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ci.localized_symbol == 'CI₣'
        assert cfa_franc_bceao_ci.convertion == ''
        assert cfa_franc_bceao_ci.__hash__() == hash(
            (cfa_franc_bceao_ci.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ci.__repr__() == (
            'CFAFrancBCEAOCI(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CI₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ci.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_ci_custom(self):
        """test_cfa_franc_bceao_ci_custom."""
        amount = 1000
        cfa_franc_bceao_ci = CFAFrancBCEAOCI(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ci.amount == decimal
        assert cfa_franc_bceao_ci.numeric_code == '952'
        assert cfa_franc_bceao_ci.alpha_code == 'XOF'
        assert cfa_franc_bceao_ci.decimal_places == 5
        assert cfa_franc_bceao_ci.decimal_sign == '\u202F'
        assert cfa_franc_bceao_ci.grouping_places == 2
        assert cfa_franc_bceao_ci.grouping_sign == ','
        assert cfa_franc_bceao_ci.international
        assert cfa_franc_bceao_ci.symbol == '₣'
        assert not cfa_franc_bceao_ci.symbol_ahead
        assert cfa_franc_bceao_ci.symbol_separator == '_'
        assert cfa_franc_bceao_ci.localized_symbol == 'CI₣'
        assert cfa_franc_bceao_ci.convertion == ''
        assert cfa_franc_bceao_ci.__hash__() == hash(
            (cfa_franc_bceao_ci.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ci.__repr__() == (
            'CFAFrancBCEAOCI(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CI₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_ci.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_ci_changed(self):
        """test_ccfa_franc_bceao_ci_changed."""
        cfa_franc_bceao_ci = CFAFrancBCEAOCI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ci.international = True

    def test_cfa_franc_bceao_ci_math_add(self):
        """test_cfa_franc_bceao_ci_math_add."""
        cfa_franc_bceao_ci_one = CFAFrancBCEAOCI(amount=1)
        cfa_franc_bceao_ci_two = CFAFrancBCEAOCI(amount=2)
        cfa_franc_bceao_ci_three = CFAFrancBCEAOCI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_ci_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOCI\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_ci_one.__add__('1.00')
        assert (
            cfa_franc_bceao_ci_one +
            cfa_franc_bceao_ci_two) == cfa_franc_bceao_ci_three

    def test_cfa_franc_bceao_ci_slots(self):
        """test_cfa_franc_bceao_ci_slots."""
        cfa_franc_bceao_ci = CFAFrancBCEAOCI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOCI\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_ci.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO GW representation."""

from multicurrency import CFAFrancBCEAOGW


class TestCFAFrancBCEAOGW:
    """CFAFrancBCEAOGW currency tests."""

    def test_cfa_franc_bceao_gw(self):
        """test_cfa_franc_bceao_gw."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_gw = CFAFrancBCEAOGW(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_gw.amount == decimal
        assert cfa_franc_bceao_gw.numeric_code == '952'
        assert cfa_franc_bceao_gw.alpha_code == 'XOF'
        assert cfa_franc_bceao_gw.decimal_places == 0
        assert cfa_franc_bceao_gw.decimal_sign == ','
        assert cfa_franc_bceao_gw.grouping_places == 3
        assert cfa_franc_bceao_gw.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_gw.international
        assert cfa_franc_bceao_gw.symbol == '₣'
        assert not cfa_franc_bceao_gw.symbol_ahead
        assert cfa_franc_bceao_gw.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_gw.localized_symbol == 'GW₣'
        assert cfa_franc_bceao_gw.convertion == ''
        assert cfa_franc_bceao_gw.__hash__() == hash(
            (cfa_franc_bceao_gw.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_gw.__repr__() == (
            'CFAFrancBCEAOGW(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GW₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_gw.__str__() == '0 ₣'

    def test_cfa_franc_bceao_gw_negative(self):
        """test_cfa_franc_bceao_gw_negative."""
        amount = -100
        cfa_franc_bceao_gw = CFAFrancBCEAOGW(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_gw.numeric_code == '952'
        assert cfa_franc_bceao_gw.alpha_code == 'XOF'
        assert cfa_franc_bceao_gw.decimal_places == 0
        assert cfa_franc_bceao_gw.decimal_sign == ','
        assert cfa_franc_bceao_gw.grouping_places == 3
        assert cfa_franc_bceao_gw.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_gw.international
        assert cfa_franc_bceao_gw.symbol == '₣'
        assert not cfa_franc_bceao_gw.symbol_ahead
        assert cfa_franc_bceao_gw.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_gw.localized_symbol == 'GW₣'
        assert cfa_franc_bceao_gw.convertion == ''
        assert cfa_franc_bceao_gw.__hash__() == hash(
            (cfa_franc_bceao_gw.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_gw.__repr__() == (
            'CFAFrancBCEAOGW(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GW₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_gw.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_gw_custom(self):
        """test_cfa_franc_bceao_gw_custom."""
        amount = 1000
        cfa_franc_bceao_gw = CFAFrancBCEAOGW(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_gw.amount == decimal
        assert cfa_franc_bceao_gw.numeric_code == '952'
        assert cfa_franc_bceao_gw.alpha_code == 'XOF'
        assert cfa_franc_bceao_gw.decimal_places == 5
        assert cfa_franc_bceao_gw.decimal_sign == '\u202F'
        assert cfa_franc_bceao_gw.grouping_places == 2
        assert cfa_franc_bceao_gw.grouping_sign == ','
        assert cfa_franc_bceao_gw.international
        assert cfa_franc_bceao_gw.symbol == '₣'
        assert not cfa_franc_bceao_gw.symbol_ahead
        assert cfa_franc_bceao_gw.symbol_separator == '_'
        assert cfa_franc_bceao_gw.localized_symbol == 'GW₣'
        assert cfa_franc_bceao_gw.convertion == ''
        assert cfa_franc_bceao_gw.__hash__() == hash(
            (cfa_franc_bceao_gw.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_gw.__repr__() == (
            'CFAFrancBCEAOGW(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GW₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_gw.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_gw_changed(self):
        """test_ccfa_franc_bceao_gw_changed."""
        cfa_franc_bceao_gw = CFAFrancBCEAOGW(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_gw.international = True

    def test_cfa_franc_bceao_gw_math_add(self):
        """test_cfa_franc_bceao_gw_math_add."""
        cfa_franc_bceao_gw_one = CFAFrancBCEAOGW(amount=1)
        cfa_franc_bceao_gw_two = CFAFrancBCEAOGW(amount=2)
        cfa_franc_bceao_gw_three = CFAFrancBCEAOGW(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_gw_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOGW\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_gw_one.__add__('1.00')
        assert (
            cfa_franc_bceao_gw_one +
            cfa_franc_bceao_gw_two) == cfa_franc_bceao_gw_three

    def test_cfa_franc_bceao_gw_slots(self):
        """test_cfa_franc_bceao_gw_slots."""
        cfa_franc_bceao_gw = CFAFrancBCEAOGW(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOGW\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_gw.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO ML representation."""

from multicurrency import CFAFrancBCEAOML


class TestCFAFrancBCEAOML:
    """CFAFrancBCEAOML currency tests."""

    def test_cfa_franc_bceao_ml(self):
        """test_cfa_franc_bceao_ml."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_ml = CFAFrancBCEAOML(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ml.amount == decimal
        assert cfa_franc_bceao_ml.numeric_code == '952'
        assert cfa_franc_bceao_ml.alpha_code == 'XOF'
        assert cfa_franc_bceao_ml.decimal_places == 0
        assert cfa_franc_bceao_ml.decimal_sign == ','
        assert cfa_franc_bceao_ml.grouping_places == 3
        assert cfa_franc_bceao_ml.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ml.international
        assert cfa_franc_bceao_ml.symbol == '₣'
        assert not cfa_franc_bceao_ml.symbol_ahead
        assert cfa_franc_bceao_ml.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ml.localized_symbol == 'ML₣'
        assert cfa_franc_bceao_ml.convertion == ''
        assert cfa_franc_bceao_ml.__hash__() == hash(
            (cfa_franc_bceao_ml.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ml.__repr__() == (
            'CFAFrancBCEAOML(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ML₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ml.__str__() == '0 ₣'

    def test_cfa_franc_bceao_ml_negative(self):
        """test_cfa_franc_bceao_ml_negative."""
        amount = -100
        cfa_franc_bceao_ml = CFAFrancBCEAOML(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ml.numeric_code == '952'
        assert cfa_franc_bceao_ml.alpha_code == 'XOF'
        assert cfa_franc_bceao_ml.decimal_places == 0
        assert cfa_franc_bceao_ml.decimal_sign == ','
        assert cfa_franc_bceao_ml.grouping_places == 3
        assert cfa_franc_bceao_ml.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ml.international
        assert cfa_franc_bceao_ml.symbol == '₣'
        assert not cfa_franc_bceao_ml.symbol_ahead
        assert cfa_franc_bceao_ml.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ml.localized_symbol == 'ML₣'
        assert cfa_franc_bceao_ml.convertion == ''
        assert cfa_franc_bceao_ml.__hash__() == hash(
            (cfa_franc_bceao_ml.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ml.__repr__() == (
            'CFAFrancBCEAOML(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ML₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ml.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_ml_custom(self):
        """test_cfa_franc_bceao_ml_custom."""
        amount = 1000
        cfa_franc_bceao_ml = CFAFrancBCEAOML(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ml.amount == decimal
        assert cfa_franc_bceao_ml.numeric_code == '952'
        assert cfa_franc_bceao_ml.alpha_code == 'XOF'
        assert cfa_franc_bceao_ml.decimal_places == 5
        assert cfa_franc_bceao_ml.decimal_sign == '\u202F'
        assert cfa_franc_bceao_ml.grouping_places == 2
        assert cfa_franc_bceao_ml.grouping_sign == ','
        assert cfa_franc_bceao_ml.international
        assert cfa_franc_bceao_ml.symbol == '₣'
        assert not cfa_franc_bceao_ml.symbol_ahead
        assert cfa_franc_bceao_ml.symbol_separator == '_'
        assert cfa_franc_bceao_ml.localized_symbol == 'ML₣'
        assert cfa_franc_bceao_ml.convertion == ''
        assert cfa_franc_bceao_ml.__hash__() == hash(
            (cfa_franc_bceao_ml.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ml.__repr__() == (
            'CFAFrancBCEAOML(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ML₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_ml.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_ml_changed(self):
        """test_ccfa_franc_bceao_ml_changed."""
        cfa_franc_bceao_ml = CFAFrancBCEAOML(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ml.international = True

    def test_cfa_franc_bceao_ml_math_add(self):
        """test_cfa_franc_bceao_ml_math_add."""
        cfa_franc_bceao_ml_one = CFAFrancBCEAOML(amount=1)
        cfa_franc_bceao_ml_two = CFAFrancBCEAOML(amount=2)
        cfa_franc_bceao_ml_three = CFAFrancBCEAOML(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_ml_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOML\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_ml_one.__add__('1.00')
        assert (
            cfa_franc_bceao_ml_one +
            cfa_franc_bceao_ml_two) == cfa_franc_bceao_ml_three

    def test_cfa_franc_bceao_ml_slots(self):
        """test_cfa_franc_bceao_ml_slots."""
        cfa_franc_bceao_ml = CFAFrancBCEAOML(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOML\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_ml.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO NG representation."""

from multicurrency import CFAFrancBCEAONG


class TestCFAFrancBCEAONG:
    """CFAFrancBCEAONG currency tests."""

    def test_cfa_franc_bceao_ng(self):
        """test_cfa_franc_bceao_ng."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_ng = CFAFrancBCEAONG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ng.amount == decimal
        assert cfa_franc_bceao_ng.numeric_code == '952'
        assert cfa_franc_bceao_ng.alpha_code == 'XOF'
        assert cfa_franc_bceao_ng.decimal_places == 0
        assert cfa_franc_bceao_ng.decimal_sign == ','
        assert cfa_franc_bceao_ng.grouping_places == 3
        assert cfa_franc_bceao_ng.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ng.international
        assert cfa_franc_bceao_ng.symbol == '₣'
        assert not cfa_franc_bceao_ng.symbol_ahead
        assert cfa_franc_bceao_ng.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ng.localized_symbol == 'NG₣'
        assert cfa_franc_bceao_ng.convertion == ''
        assert cfa_franc_bceao_ng.__hash__() == hash(
            (cfa_franc_bceao_ng.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ng.__repr__() == (
            'CFAFrancBCEAONG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NG₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ng.__str__() == '0 ₣'

    def test_cfa_franc_bceao_ng_negative(self):
        """test_cfa_franc_bceao_ng_negative."""
        amount = -100
        cfa_franc_bceao_ng = CFAFrancBCEAONG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ng.numeric_code == '952'
        assert cfa_franc_bceao_ng.alpha_code == 'XOF'
        assert cfa_franc_bceao_ng.decimal_places == 0
        assert cfa_franc_bceao_ng.decimal_sign == ','
        assert cfa_franc_bceao_ng.grouping_places == 3
        assert cfa_franc_bceao_ng.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_ng.international
        assert cfa_franc_bceao_ng.symbol == '₣'
        assert not cfa_franc_bceao_ng.symbol_ahead
        assert cfa_franc_bceao_ng.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_ng.localized_symbol == 'NG₣'
        assert cfa_franc_bceao_ng.convertion == ''
        assert cfa_franc_bceao_ng.__hash__() == hash(
            (cfa_franc_bceao_ng.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ng.__repr__() == (
            'CFAFrancBCEAONG(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NG₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_ng.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_ng_custom(self):
        """test_cfa_franc_bceao_ng_custom."""
        amount = 1000
        cfa_franc_bceao_ng = CFAFrancBCEAONG(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_ng.amount == decimal
        assert cfa_franc_bceao_ng.numeric_code == '952'
        assert cfa_franc_bceao_ng.alpha_code == 'XOF'
        assert cfa_franc_bceao_ng.decimal_places == 5
        assert cfa_franc_bceao_ng.decimal_sign == '\u202F'
        assert cfa_franc_bceao_ng.grouping_places == 2
        assert cfa_franc_bceao_ng.grouping_sign == ','
        assert cfa_franc_bceao_ng.international
        assert cfa_franc_bceao_ng.symbol == '₣'
        assert not cfa_franc_bceao_ng.symbol_ahead
        assert cfa_franc_bceao_ng.symbol_separator == '_'
        assert cfa_franc_bceao_ng.localized_symbol == 'NG₣'
        assert cfa_franc_bceao_ng.convertion == ''
        assert cfa_franc_bceao_ng.__hash__() == hash(
            (cfa_franc_bceao_ng.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_ng.__repr__() == (
            'CFAFrancBCEAONG(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NG₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_ng.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_ng_changed(self):
        """test_ccfa_franc_bceao_ng_changed."""
        cfa_franc_bceao_ng = CFAFrancBCEAONG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_ng.international = True

    def test_cfa_franc_bceao_ng_math_add(self):
        """test_cfa_franc_bceao_ng_math_add."""
        cfa_franc_bceao_ng_one = CFAFrancBCEAONG(amount=1)
        cfa_franc_bceao_ng_two = CFAFrancBCEAONG(amount=2)
        cfa_franc_bceao_ng_three = CFAFrancBCEAONG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_ng_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAONG\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_ng_one.__add__('1.00')
        assert (
            cfa_franc_bceao_ng_one +
            cfa_franc_bceao_ng_two) == cfa_franc_bceao_ng_three

    def test_cfa_franc_bceao_ng_slots(self):
        """test_cfa_franc_bceao_ng_slots."""
        cfa_franc_bceao_ng = CFAFrancBCEAONG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAONG\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_ng.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO SN representation."""

from multicurrency import CFAFrancBCEAOSN


class TestCFAFrancBCEAOSN:
    """CFAFrancBCEAOSN currency tests."""

    def test_cfa_franc_bceao_sn(self):
        """test_cfa_franc_bceao_sn."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_sn = CFAFrancBCEAOSN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_sn.amount == decimal
        assert cfa_franc_bceao_sn.numeric_code == '952'
        assert cfa_franc_bceao_sn.alpha_code == 'XOF'
        assert cfa_franc_bceao_sn.decimal_places == 0
        assert cfa_franc_bceao_sn.decimal_sign == ','
        assert cfa_franc_bceao_sn.grouping_places == 3
        assert cfa_franc_bceao_sn.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_sn.international
        assert cfa_franc_bceao_sn.symbol == '₣'
        assert not cfa_franc_bceao_sn.symbol_ahead
        assert cfa_franc_bceao_sn.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_sn.localized_symbol == 'SN₣'
        assert cfa_franc_bceao_sn.convertion == ''
        assert cfa_franc_bceao_sn.__hash__() == hash(
            (cfa_franc_bceao_sn.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_sn.__repr__() == (
            'CFAFrancBCEAOSN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SN₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_sn.__str__() == '0 ₣'

    def test_cfa_franc_bceao_sn_negative(self):
        """test_cfa_franc_bceao_sn_negative."""
        amount = -100
        cfa_franc_bceao_sn = CFAFrancBCEAOSN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_sn.numeric_code == '952'
        assert cfa_franc_bceao_sn.alpha_code == 'XOF'
        assert cfa_franc_bceao_sn.decimal_places == 0
        assert cfa_franc_bceao_sn.decimal_sign == ','
        assert cfa_franc_bceao_sn.grouping_places == 3
        assert cfa_franc_bceao_sn.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_sn.international
        assert cfa_franc_bceao_sn.symbol == '₣'
        assert not cfa_franc_bceao_sn.symbol_ahead
        assert cfa_franc_bceao_sn.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_sn.localized_symbol == 'SN₣'
        assert cfa_franc_bceao_sn.convertion == ''
        assert cfa_franc_bceao_sn.__hash__() == hash(
            (cfa_franc_bceao_sn.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_sn.__repr__() == (
            'CFAFrancBCEAOSN(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SN₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_sn.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_sn_custom(self):
        """test_cfa_franc_bceao_sn_custom."""
        amount = 1000
        cfa_franc_bceao_sn = CFAFrancBCEAOSN(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_sn.amount == decimal
        assert cfa_franc_bceao_sn.numeric_code == '952'
        assert cfa_franc_bceao_sn.alpha_code == 'XOF'
        assert cfa_franc_bceao_sn.decimal_places == 5
        assert cfa_franc_bceao_sn.decimal_sign == '\u202F'
        assert cfa_franc_bceao_sn.grouping_places == 2
        assert cfa_franc_bceao_sn.grouping_sign == ','
        assert cfa_franc_bceao_sn.international
        assert cfa_franc_bceao_sn.symbol == '₣'
        assert not cfa_franc_bceao_sn.symbol_ahead
        assert cfa_franc_bceao_sn.symbol_separator == '_'
        assert cfa_franc_bceao_sn.localized_symbol == 'SN₣'
        assert cfa_franc_bceao_sn.convertion == ''
        assert cfa_franc_bceao_sn.__hash__() == hash(
            (cfa_franc_bceao_sn.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_sn.__repr__() == (
            'CFAFrancBCEAOSN(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SN₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_sn.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_sn_changed(self):
        """test_ccfa_franc_bceao_sn_changed."""
        cfa_franc_bceao_sn = CFAFrancBCEAOSN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_sn.international = True

    def test_cfa_franc_bceao_sn_math_add(self):
        """test_cfa_franc_bceao_sn_math_add."""
        cfa_franc_bceao_sn_one = CFAFrancBCEAOSN(amount=1)
        cfa_franc_bceao_sn_two = CFAFrancBCEAOSN(amount=2)
        cfa_franc_bceao_sn_three = CFAFrancBCEAOSN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_sn_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOSN\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_sn_one.__add__('1.00')
        assert (
            cfa_franc_bceao_sn_one +
            cfa_franc_bceao_sn_two) == cfa_franc_bceao_sn_three

    def test_cfa_franc_bceao_sn_slots(self):
        """test_cfa_franc_bceao_sn_slots."""
        cfa_franc_bceao_sn = CFAFrancBCEAOSN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOSN\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_sn.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFA Franc BCEAO TG representation."""

from multicurrency import CFAFrancBCEAOTG


class TestCFAFrancBCEAOTG:
    """CFAFrancBCEAOTG currency tests."""

    def test_cfa_franc_bceao_tg(self):
        """test_cfa_franc_bceao_tg."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfa_franc_bceao_tg = CFAFrancBCEAOTG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_tg.amount == decimal
        assert cfa_franc_bceao_tg.numeric_code == '952'
        assert cfa_franc_bceao_tg.alpha_code == 'XOF'
        assert cfa_franc_bceao_tg.decimal_places == 0
        assert cfa_franc_bceao_tg.decimal_sign == ','
        assert cfa_franc_bceao_tg.grouping_places == 3
        assert cfa_franc_bceao_tg.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_tg.international
        assert cfa_franc_bceao_tg.symbol == '₣'
        assert not cfa_franc_bceao_tg.symbol_ahead
        assert cfa_franc_bceao_tg.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_tg.localized_symbol == 'TG₣'
        assert cfa_franc_bceao_tg.convertion == ''
        assert cfa_franc_bceao_tg.__hash__() == hash(
            (cfa_franc_bceao_tg.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_tg.__repr__() == (
            'CFAFrancBCEAOTG(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TG₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_tg.__str__() == '0 ₣'

    def test_cfa_franc_bceao_tg_negative(self):
        """test_cfa_franc_bceao_tg_negative."""
        amount = -100
        cfa_franc_bceao_tg = CFAFrancBCEAOTG(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_tg.numeric_code == '952'
        assert cfa_franc_bceao_tg.alpha_code == 'XOF'
        assert cfa_franc_bceao_tg.decimal_places == 0
        assert cfa_franc_bceao_tg.decimal_sign == ','
        assert cfa_franc_bceao_tg.grouping_places == 3
        assert cfa_franc_bceao_tg.grouping_sign == '\u202F'
        assert not cfa_franc_bceao_tg.international
        assert cfa_franc_bceao_tg.symbol == '₣'
        assert not cfa_franc_bceao_tg.symbol_ahead
        assert cfa_franc_bceao_tg.symbol_separator == '\u00A0'
        assert cfa_franc_bceao_tg.localized_symbol == 'TG₣'
        assert cfa_franc_bceao_tg.convertion == ''
        assert cfa_franc_bceao_tg.__hash__() == hash(
            (cfa_franc_bceao_tg.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_tg.__repr__() == (
            'CFAFrancBCEAOTG(amount: -100, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TG₣", '
            'numeric_code: "952", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfa_franc_bceao_tg.__str__() == '-100 ₣'

    def test_cfa_franc_bceao_tg_custom(self):
        """test_cfa_franc_bceao_tg_custom."""
        amount = 1000
        cfa_franc_bceao_tg = CFAFrancBCEAOTG(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfa_franc_bceao_tg.amount == decimal
        assert cfa_franc_bceao_tg.numeric_code == '952'
        assert cfa_franc_bceao_tg.alpha_code == 'XOF'
        assert cfa_franc_bceao_tg.decimal_places == 5
        assert cfa_franc_bceao_tg.decimal_sign == '\u202F'
        assert cfa_franc_bceao_tg.grouping_places == 2
        assert cfa_franc_bceao_tg.grouping_sign == ','
        assert cfa_franc_bceao_tg.international
        assert cfa_franc_bceao_tg.symbol == '₣'
        assert not cfa_franc_bceao_tg.symbol_ahead
        assert cfa_franc_bceao_tg.symbol_separator == '_'
        assert cfa_franc_bceao_tg.localized_symbol == 'TG₣'
        assert cfa_franc_bceao_tg.convertion == ''
        assert cfa_franc_bceao_tg.__hash__() == hash(
            (cfa_franc_bceao_tg.__class__, decimal, 'XOF', '952'))
        assert cfa_franc_bceao_tg.__repr__() == (
            'CFAFrancBCEAOTG(amount: 1000, '
            'alpha_code: "XOF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TG₣", '
            'numeric_code: "952", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfa_franc_bceao_tg.__str__() == 'XOF 10,00.00000'

    def test_cfa_franc_bceao_tg_changed(self):
        """test_ccfa_franc_bceao_tg_changed."""
        cfa_franc_bceao_tg = CFAFrancBCEAOTG(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfa_franc_bceao_tg.international = True

    def test_cfa_franc_bceao_tg_math_add(self):
        """test_cfa_franc_bceao_tg_math_add."""
        cfa_franc_bceao_tg_one = CFAFrancBCEAOTG(amount=1)
        cfa_franc_bceao_tg_two = CFAFrancBCEAOTG(amount=2)
        cfa_franc_bceao_tg_three = CFAFrancBCEAOTG(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XOF and OTHER.'):
            _ = cfa_franc_bceao_tg_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFAFrancBCEAOTG\'> '
                    'and <class \'str\'>.')):
            _ = cfa_franc_bceao_tg_one.__add__('1.00')
        assert (
            cfa_franc_bceao_tg_one +
            cfa_franc_bceao_tg_two) == cfa_franc_bceao_tg_three

    def test_cfa_franc_bceao_tg_slots(self):
        """test_cfa_franc_bceao_tg_slots."""
        cfa_franc_bceao_tg = CFAFrancBCEAOTG(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFAFrancBCEAOTG\' '
                    'object has no attribute \'new_variable\'')):
            cfa_franc_bceao_tg.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFP Franc representation."""

from multicurrency import CFPFranc


class TestCFPFranc:
    """CFPFranc currency tests."""

    def test_cfp_franc(self):
        """test_cfp_franc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfp_franc = CFPFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc.amount == decimal
        assert cfp_franc.numeric_code == '953'
        assert cfp_franc.alpha_code == 'XPF'
        assert cfp_franc.decimal_places == 0
        assert cfp_franc.decimal_sign == ','
        assert cfp_franc.grouping_places == 3
        assert cfp_franc.grouping_sign == '\u202F'
        assert not cfp_franc.international
        assert cfp_franc.symbol == '₣'
        assert not cfp_franc.symbol_ahead
        assert cfp_franc.symbol_separator == '\u00A0'
        assert cfp_franc.localized_symbol == '₣'
        assert cfp_franc.convertion == ''
        assert cfp_franc.__hash__() == hash(
            (cfp_franc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc.__repr__() == (
            'CFPFranc(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc.__str__() == '0 ₣'

    def test_cfp_franc_negative(self):
        """test_cfp_franc_negative."""
        amount = -100
        cfp_franc = CFPFranc(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc.numeric_code == '953'
        assert cfp_franc.alpha_code == 'XPF'
        assert cfp_franc.decimal_places == 0
        assert cfp_franc.decimal_sign == ','
        assert cfp_franc.grouping_places == 3
        assert cfp_franc.grouping_sign == '\u202F'
        assert not cfp_franc.international
        assert cfp_franc.symbol == '₣'
        assert not cfp_franc.symbol_ahead
        assert cfp_franc.symbol_separator == '\u00A0'
        assert cfp_franc.localized_symbol == '₣'
        assert cfp_franc.convertion == ''
        assert cfp_franc.__hash__() == hash(
            (cfp_franc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc.__repr__() == (
            'CFPFranc(amount: -100, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc.__str__() == '-100 ₣'

    def test_cfp_franc_custom(self):
        """test_cfp_franc_custom."""
        amount = 1000
        cfp_franc = CFPFranc(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc.amount == decimal
        assert cfp_franc.numeric_code == '953'
        assert cfp_franc.alpha_code == 'XPF'
        assert cfp_franc.decimal_places == 5
        assert cfp_franc.decimal_sign == '\u202F'
        assert cfp_franc.grouping_places == 2
        assert cfp_franc.grouping_sign == ','
        assert cfp_franc.international
        assert cfp_franc.symbol == '₣'
        assert not cfp_franc.symbol_ahead
        assert cfp_franc.symbol_separator == '_'
        assert cfp_franc.localized_symbol == '₣'
        assert cfp_franc.convertion == ''
        assert cfp_franc.__hash__() == hash(
            (cfp_franc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc.__repr__() == (
            'CFPFranc(amount: 1000, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₣", '
            'numeric_code: "953", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfp_franc.__str__() == 'XPF 10,00.00000'

    def test_cfp_franc_changed(self):
        """test_ccfp_franc_changed."""
        cfp_franc = CFPFranc(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc.international = True

    def test_cfp_franc_math_add(self):
        """test_cfp_franc_math_add."""
        cfp_franc_one = CFPFranc(amount=1)
        cfp_franc_two = CFPFranc(amount=2)
        cfp_franc_three = CFPFranc(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XPF and OTHER.'):
            _ = cfp_franc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFPFranc\'> '
                    'and <class \'str\'>.')):
            _ = cfp_franc_one.__add__('1.00')
        assert (
            cfp_franc_one +
            cfp_franc_two) == cfp_franc_three

    def test_cfp_franc_slots(self):
        """test_cfp_franc_slots."""
        cfp_franc = CFPFranc(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFPFranc\' '
                    'object has no attribute \'new_variable\'')):
            cfp_franc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFP Franc PF representation."""

from multicurrency import CFPFrancPF


class TestCFPFrancPF:
    """CFPFrancPF currency tests."""

    def test_cfp_franc_pf(self):
        """test_cfp_franc_pf."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfp_franc_pf = CFPFrancPF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_pf.amount == decimal
        assert cfp_franc_pf.numeric_code == '953'
        assert cfp_franc_pf.alpha_code == 'XPF'
        assert cfp_franc_pf.decimal_places == 0
        assert cfp_franc_pf.decimal_sign == ','
        assert cfp_franc_pf.grouping_places == 3
        assert cfp_franc_pf.grouping_sign == '\u202F'
        assert not cfp_franc_pf.international
        assert cfp_franc_pf.symbol == '₣'
        assert not cfp_franc_pf.symbol_ahead
        assert cfp_franc_pf.symbol_separator == '\u00A0'
        assert cfp_franc_pf.localized_symbol == 'PF₣'
        assert cfp_franc_pf.convertion == ''
        assert cfp_franc_pf.__hash__() == hash(
            (cfp_franc_pf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_pf.__repr__() == (
            'CFPFrancPF(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PF₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_pf.__str__() == '0 ₣'

    def test_cfp_franc_pf_negative(self):
        """test_cfp_franc_pf_negative."""
        amount = -100
        cfp_franc_pf = CFPFrancPF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_pf.numeric_code == '953'
        assert cfp_franc_pf.alpha_code == 'XPF'
        assert cfp_franc_pf.decimal_places == 0
        assert cfp_franc_pf.decimal_sign == ','
        assert cfp_franc_pf.grouping_places == 3
        assert cfp_franc_pf.grouping_sign == '\u202F'
        assert not cfp_franc_pf.international
        assert cfp_franc_pf.symbol == '₣'
        assert not cfp_franc_pf.symbol_ahead
        assert cfp_franc_pf.symbol_separator == '\u00A0'
        assert cfp_franc_pf.localized_symbol == 'PF₣'
        assert cfp_franc_pf.convertion == ''
        assert cfp_franc_pf.__hash__() == hash(
            (cfp_franc_pf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_pf.__repr__() == (
            'CFPFrancPF(amount: -100, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PF₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_pf.__str__() == '-100 ₣'

    def test_cfp_franc_pf_custom(self):
        """test_cfp_franc_pf_custom."""
        amount = 1000
        cfp_franc_pf = CFPFrancPF(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_pf.amount == decimal
        assert cfp_franc_pf.numeric_code == '953'
        assert cfp_franc_pf.alpha_code == 'XPF'
        assert cfp_franc_pf.decimal_places == 5
        assert cfp_franc_pf.decimal_sign == '\u202F'
        assert cfp_franc_pf.grouping_places == 2
        assert cfp_franc_pf.grouping_sign == ','
        assert cfp_franc_pf.international
        assert cfp_franc_pf.symbol == '₣'
        assert not cfp_franc_pf.symbol_ahead
        assert cfp_franc_pf.symbol_separator == '_'
        assert cfp_franc_pf.localized_symbol == 'PF₣'
        assert cfp_franc_pf.convertion == ''
        assert cfp_franc_pf.__hash__() == hash(
            (cfp_franc_pf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_pf.__repr__() == (
            'CFPFrancPF(amount: 1000, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PF₣", '
            'numeric_code: "953", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfp_franc_pf.__str__() == 'XPF 10,00.00000'

    def test_cfp_franc_pf_changed(self):
        """test_ccfp_franc_pf_changed."""
        cfp_franc_pf = CFPFrancPF(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_pf.international = True

    def test_cfp_franc_pf_math_add(self):
        """test_cfp_franc_pf_math_add."""
        cfp_franc_pf_one = CFPFrancPF(amount=1)
        cfp_franc_pf_two = CFPFrancPF(amount=2)
        cfp_franc_pf_three = CFPFrancPF(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XPF and OTHER.'):
            _ = cfp_franc_pf_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFPFrancPF\'> '
                    'and <class \'str\'>.')):
            _ = cfp_franc_pf_one.__add__('1.00')
        assert (
            cfp_franc_pf_one +
            cfp_franc_pf_two) == cfp_franc_pf_three

    def test_cfp_franc_pf_slots(self):
        """test_cfp_franc_pf_slots."""
        cfp_franc_pf = CFPFrancPF(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFPFrancPF\' '
                    'object has no attribute \'new_variable\'')):
            cfp_franc_pf.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFP Franc NC representation."""

from multicurrency import CFPFrancNC


class TestCFPFrancNC:
    """CFPFrancNC currency tests."""

    def test_cfp_franc_nc(self):
        """test_cfp_franc_nc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfp_franc_nc = CFPFrancNC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_nc.amount == decimal
        assert cfp_franc_nc.numeric_code == '953'
        assert cfp_franc_nc.alpha_code == 'XPF'
        assert cfp_franc_nc.decimal_places == 0
        assert cfp_franc_nc.decimal_sign == ','
        assert cfp_franc_nc.grouping_places == 3
        assert cfp_franc_nc.grouping_sign == '\u202F'
        assert not cfp_franc_nc.international
        assert cfp_franc_nc.symbol == '₣'
        assert not cfp_franc_nc.symbol_ahead
        assert cfp_franc_nc.symbol_separator == '\u00A0'
        assert cfp_franc_nc.localized_symbol == 'NC₣'
        assert cfp_franc_nc.convertion == ''
        assert cfp_franc_nc.__hash__() == hash(
            (cfp_franc_nc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_nc.__repr__() == (
            'CFPFrancNC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NC₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_nc.__str__() == '0 ₣'

    def test_cfp_franc_nc_negative(self):
        """test_cfp_franc_nc_negative."""
        amount = -100
        cfp_franc_nc = CFPFrancNC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_nc.numeric_code == '953'
        assert cfp_franc_nc.alpha_code == 'XPF'
        assert cfp_franc_nc.decimal_places == 0
        assert cfp_franc_nc.decimal_sign == ','
        assert cfp_franc_nc.grouping_places == 3
        assert cfp_franc_nc.grouping_sign == '\u202F'
        assert not cfp_franc_nc.international
        assert cfp_franc_nc.symbol == '₣'
        assert not cfp_franc_nc.symbol_ahead
        assert cfp_franc_nc.symbol_separator == '\u00A0'
        assert cfp_franc_nc.localized_symbol == 'NC₣'
        assert cfp_franc_nc.convertion == ''
        assert cfp_franc_nc.__hash__() == hash(
            (cfp_franc_nc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_nc.__repr__() == (
            'CFPFrancNC(amount: -100, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NC₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_nc.__str__() == '-100 ₣'

    def test_cfp_franc_nc_custom(self):
        """test_cfp_franc_nc_custom."""
        amount = 1000
        cfp_franc_nc = CFPFrancNC(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_nc.amount == decimal
        assert cfp_franc_nc.numeric_code == '953'
        assert cfp_franc_nc.alpha_code == 'XPF'
        assert cfp_franc_nc.decimal_places == 5
        assert cfp_franc_nc.decimal_sign == '\u202F'
        assert cfp_franc_nc.grouping_places == 2
        assert cfp_franc_nc.grouping_sign == ','
        assert cfp_franc_nc.international
        assert cfp_franc_nc.symbol == '₣'
        assert not cfp_franc_nc.symbol_ahead
        assert cfp_franc_nc.symbol_separator == '_'
        assert cfp_franc_nc.localized_symbol == 'NC₣'
        assert cfp_franc_nc.convertion == ''
        assert cfp_franc_nc.__hash__() == hash(
            (cfp_franc_nc.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_nc.__repr__() == (
            'CFPFrancNC(amount: 1000, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NC₣", '
            'numeric_code: "953", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfp_franc_nc.__str__() == 'XPF 10,00.00000'

    def test_cfp_franc_nc_changed(self):
        """test_ccfp_franc_nc_changed."""
        cfp_franc_nc = CFPFrancNC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_nc.international = True

    def test_cfp_franc_nc_math_add(self):
        """test_cfp_franc_nc_math_add."""
        cfp_franc_nc_one = CFPFrancNC(amount=1)
        cfp_franc_nc_two = CFPFrancNC(amount=2)
        cfp_franc_nc_three = CFPFrancNC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XPF and OTHER.'):
            _ = cfp_franc_nc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFPFrancNC\'> '
                    'and <class \'str\'>.')):
            _ = cfp_franc_nc_one.__add__('1.00')
        assert (
            cfp_franc_nc_one +
            cfp_franc_nc_two) == cfp_franc_nc_three

    def test_cfp_franc_nc_slots(self):
        """test_cfp_franc_nc_slots."""
        cfp_franc_nc = CFPFrancNC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFPFrancNC\' '
                    'object has no attribute \'new_variable\'')):
            cfp_franc_nc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the CFP Franc WF representation."""

from multicurrency import CFPFrancWF


class TestCFPFrancWF:
    """CFPFrancWF currency tests."""

    def test_cfp_franc_wf(self):
        """test_cfp_franc_wf."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cfp_franc_wf = CFPFrancWF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_wf.amount == decimal
        assert cfp_franc_wf.numeric_code == '953'
        assert cfp_franc_wf.alpha_code == 'XPF'
        assert cfp_franc_wf.decimal_places == 0
        assert cfp_franc_wf.decimal_sign == ','
        assert cfp_franc_wf.grouping_places == 3
        assert cfp_franc_wf.grouping_sign == '\u202F'
        assert not cfp_franc_wf.international
        assert cfp_franc_wf.symbol == '₣'
        assert not cfp_franc_wf.symbol_ahead
        assert cfp_franc_wf.symbol_separator == '\u00A0'
        assert cfp_franc_wf.localized_symbol == 'WF₣'
        assert cfp_franc_wf.convertion == ''
        assert cfp_franc_wf.__hash__() == hash(
            (cfp_franc_wf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_wf.__repr__() == (
            'CFPFrancWF(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "WF₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_wf.__str__() == '0 ₣'

    def test_cfp_franc_wf_negative(self):
        """test_cfp_franc_wf_negative."""
        amount = -100
        cfp_franc_wf = CFPFrancWF(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_wf.numeric_code == '953'
        assert cfp_franc_wf.alpha_code == 'XPF'
        assert cfp_franc_wf.decimal_places == 0
        assert cfp_franc_wf.decimal_sign == ','
        assert cfp_franc_wf.grouping_places == 3
        assert cfp_franc_wf.grouping_sign == '\u202F'
        assert not cfp_franc_wf.international
        assert cfp_franc_wf.symbol == '₣'
        assert not cfp_franc_wf.symbol_ahead
        assert cfp_franc_wf.symbol_separator == '\u00A0'
        assert cfp_franc_wf.localized_symbol == 'WF₣'
        assert cfp_franc_wf.convertion == ''
        assert cfp_franc_wf.__hash__() == hash(
            (cfp_franc_wf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_wf.__repr__() == (
            'CFPFrancWF(amount: -100, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "WF₣", '
            'numeric_code: "953", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert cfp_franc_wf.__str__() == '-100 ₣'

    def test_cfp_franc_wf_custom(self):
        """test_cfp_franc_wf_custom."""
        amount = 1000
        cfp_franc_wf = CFPFrancWF(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cfp_franc_wf.amount == decimal
        assert cfp_franc_wf.numeric_code == '953'
        assert cfp_franc_wf.alpha_code == 'XPF'
        assert cfp_franc_wf.decimal_places == 5
        assert cfp_franc_wf.decimal_sign == '\u202F'
        assert cfp_franc_wf.grouping_places == 2
        assert cfp_franc_wf.grouping_sign == ','
        assert cfp_franc_wf.international
        assert cfp_franc_wf.symbol == '₣'
        assert not cfp_franc_wf.symbol_ahead
        assert cfp_franc_wf.symbol_separator == '_'
        assert cfp_franc_wf.localized_symbol == 'WF₣'
        assert cfp_franc_wf.convertion == ''
        assert cfp_franc_wf.__hash__() == hash(
            (cfp_franc_wf.__class__, decimal, 'XPF', '953'))
        assert cfp_franc_wf.__repr__() == (
            'CFPFrancWF(amount: 1000, '
            'alpha_code: "XPF", '
            'symbol: "₣", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "WF₣", '
            'numeric_code: "953", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert cfp_franc_wf.__str__() == 'XPF 10,00.00000'

    def test_cfp_franc_wf_changed(self):
        """test_ccfp_franc_wf_changed."""
        cfp_franc_wf = CFPFrancWF(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cfp_franc_wf.international = True

    def test_cfp_franc_wf_math_add(self):
        """test_cfp_franc_wf_math_add."""
        cfp_franc_wf_one = CFPFrancWF(amount=1)
        cfp_franc_wf_two = CFPFrancWF(amount=2)
        cfp_franc_wf_three = CFPFrancWF(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XPF and OTHER.'):
            _ = cfp_franc_wf_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'franc.CFPFrancWF\'> '
                    'and <class \'str\'>.')):
            _ = cfp_franc_wf_one.__add__('1.00')
        assert (
            cfp_franc_wf_one +
            cfp_franc_wf_two) == cfp_franc_wf_three

    def test_cfp_franc_wf_slots(self):
        """test_cfp_franc_wf_slots."""
        cfp_franc_wf = CFPFrancWF(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CFPFrancWF\' '
                    'object has no attribute \'new_variable\'')):
            cfp_franc_wf.new_variable = 'fail'  # pylint: disable=assigning-non-slot
