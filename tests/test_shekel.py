# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Shekel currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the New Israeli Shekel representation."""

from multicurrency import NewIsraeliShekel


class TestNewIsraeliShekel:

    def test_new_israeli_shekel(self):
        """test_new_israeli_shekel."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_israeli_shekel = NewIsraeliShekel(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel.amount == decimal
        assert new_israeli_shekel.numeric_code == '376'
        assert new_israeli_shekel.alpha_code == 'ILS'
        assert new_israeli_shekel.decimal_places == 2
        assert new_israeli_shekel.decimal_sign == '.'
        assert new_israeli_shekel.grouping_places == 3
        assert new_israeli_shekel.grouping_sign == ','
        assert not new_israeli_shekel.international
        assert new_israeli_shekel.symbol == '₪'
        assert not new_israeli_shekel.symbol_ahead
        assert new_israeli_shekel.symbol_separator == '\u00A0'
        assert new_israeli_shekel.localized_symbol == '₪'
        assert new_israeli_shekel.convertion == ''
        assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel.__repr__() == (
            'NewIsraeliShekel(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel.__str__() == '0.14 ₪'


    def test_new_israeli_shekel_negative(self):
        """test_new_israeli_shekel_negative."""
        amount = -100
        new_israeli_shekel = NewIsraeliShekel(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel.numeric_code == '376'
        assert new_israeli_shekel.alpha_code == 'ILS'
        assert new_israeli_shekel.decimal_places == 2
        assert new_israeli_shekel.decimal_sign == '.'
        assert new_israeli_shekel.grouping_places == 3
        assert new_israeli_shekel.grouping_sign == ','
        assert not new_israeli_shekel.international
        assert new_israeli_shekel.symbol == '₪'
        assert not new_israeli_shekel.symbol_ahead
        assert new_israeli_shekel.symbol_separator == '\u00A0'
        assert new_israeli_shekel.localized_symbol == '₪'
        assert new_israeli_shekel.convertion == ''
        assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel.__repr__() == (
            'NewIsraeliShekel(amount: -100, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel.__str__() == '-100.00 ₪'


    def test_new_israeli_shekel_custom(self):
        """test_new_israeli_shekel_custom."""
        amount = 1000
        new_israeli_shekel = NewIsraeliShekel(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel.amount == decimal
        assert new_israeli_shekel.numeric_code == '376'
        assert new_israeli_shekel.alpha_code == 'ILS'
        assert new_israeli_shekel.decimal_places == 5
        assert new_israeli_shekel.decimal_sign == ','
        assert new_israeli_shekel.grouping_places == 2
        assert new_israeli_shekel.grouping_sign == '.'
        assert new_israeli_shekel.international
        assert new_israeli_shekel.symbol == '₪'
        assert not new_israeli_shekel.symbol_ahead
        assert new_israeli_shekel.symbol_separator == '_'
        assert new_israeli_shekel.localized_symbol == '₪'
        assert new_israeli_shekel.convertion == ''
        assert new_israeli_shekel.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel.__repr__() == (
            'NewIsraeliShekel(amount: 1000, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₪", '
            'numeric_code: "376", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_israeli_shekel.__str__() == 'ILS 10,00.00000'


    def test_new_israeli_shekel_changed(self):
        """test_cnew_israeli_shekel_changed."""
        new_israeli_shekel = NewIsraeliShekel(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel.international = True


    def test_new_israeli_shekel_math_add(self):
        """test_new_israeli_shekel_math_add."""
        new_israeli_shekel_one = NewIsraeliShekel(amount=1)
        new_israeli_shekel_two = NewIsraeliShekel(amount=2)
        new_israeli_shekel_three = NewIsraeliShekel(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ILS and OTHER.'):
            _ = new_israeli_shekel_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'shekel.NewIsraeliShekel\'> '
                    'and <class \'str\'>.')):
            _ = new_israeli_shekel_one.__add__('1.00')
        assert (
            new_israeli_shekel_one +
            new_israeli_shekel_two) == new_israeli_shekel_three


    def test_new_israeli_shekel_slots(self):
        """test_new_israeli_shekel_slots."""
        new_israeli_shekel = NewIsraeliShekel(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewIsraeliShekel\' '
                    'object has no attribute \'new_variable\'')):
            new_israeli_shekel.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Israeli Shekel IL representation."""

from multicurrency import NewIsraeliShekelIL


class TestNewIsraeliShekelIL:

    def test_new_israeli_shekel_il(self):
        """test_new_israeli_shekel_il."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_israeli_shekel_il = NewIsraeliShekelIL(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_il.amount == decimal
        assert new_israeli_shekel_il.numeric_code == '376'
        assert new_israeli_shekel_il.alpha_code == 'ILS'
        assert new_israeli_shekel_il.decimal_places == 2
        assert new_israeli_shekel_il.decimal_sign == '.'
        assert new_israeli_shekel_il.grouping_places == 3
        assert new_israeli_shekel_il.grouping_sign == ','
        assert not new_israeli_shekel_il.international
        assert new_israeli_shekel_il.symbol == '₪'
        assert not new_israeli_shekel_il.symbol_ahead
        assert new_israeli_shekel_il.symbol_separator == '\u00A0'
        assert new_israeli_shekel_il.localized_symbol == 'IL₪'
        assert new_israeli_shekel_il.convertion == ''
        assert new_israeli_shekel_il.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_il.__repr__() == (
            'NewIsraeliShekelIL(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "IL₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel_il.__str__() == '0.14 ₪'


    def test_new_israeli_shekel_il_negative(self):
        """test_new_israeli_shekel_il_negative."""
        amount = -100
        new_israeli_shekel_il = NewIsraeliShekelIL(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_il.numeric_code == '376'
        assert new_israeli_shekel_il.alpha_code == 'ILS'
        assert new_israeli_shekel_il.decimal_places == 2
        assert new_israeli_shekel_il.decimal_sign == '.'
        assert new_israeli_shekel_il.grouping_places == 3
        assert new_israeli_shekel_il.grouping_sign == ','
        assert not new_israeli_shekel_il.international
        assert new_israeli_shekel_il.symbol == '₪'
        assert not new_israeli_shekel_il.symbol_ahead
        assert new_israeli_shekel_il.symbol_separator == '\u00A0'
        assert new_israeli_shekel_il.localized_symbol == 'IL₪'
        assert new_israeli_shekel_il.convertion == ''
        assert new_israeli_shekel_il.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_il.__repr__() == (
            'NewIsraeliShekelIL(amount: -100, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "IL₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel_il.__str__() == '-100.00 ₪'


    def test_new_israeli_shekel_il_custom(self):
        """test_new_israeli_shekel_il_custom."""
        amount = 1000
        new_israeli_shekel_il = NewIsraeliShekelIL(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_il.amount == decimal
        assert new_israeli_shekel_il.numeric_code == '376'
        assert new_israeli_shekel_il.alpha_code == 'ILS'
        assert new_israeli_shekel_il.decimal_places == 5
        assert new_israeli_shekel_il.decimal_sign == ','
        assert new_israeli_shekel_il.grouping_places == 2
        assert new_israeli_shekel_il.grouping_sign == '.'
        assert new_israeli_shekel_il.international
        assert new_israeli_shekel_il.symbol == '₪'
        assert not new_israeli_shekel_il.symbol_ahead
        assert new_israeli_shekel_il.symbol_separator == '_'
        assert new_israeli_shekel_il.localized_symbol == 'IL₪'
        assert new_israeli_shekel_il.convertion == ''
        assert new_israeli_shekel_il.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_il.__repr__() == (
            'NewIsraeliShekelIL(amount: 1000, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IL₪", '
            'numeric_code: "376", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_israeli_shekel_il.__str__() == 'ILS 10,00.00000'


    def test_new_israeli_shekel_il_changed(self):
        """test_cnew_israeli_shekel_il_changed."""
        new_israeli_shekel_il = NewIsraeliShekelIL(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_il.international = True


    def test_new_israeli_shekel_il_math_add(self):
        """test_new_israeli_shekel_il_math_add."""
        new_israeli_shekel_il_one = NewIsraeliShekelIL(amount=1)
        new_israeli_shekel_il_two = NewIsraeliShekelIL(amount=2)
        new_israeli_shekel_il_three = NewIsraeliShekelIL(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ILS and OTHER.'):
            _ = new_israeli_shekel_il_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'shekel.NewIsraeliShekelIL\'> '
                    'and <class \'str\'>.')):
            _ = new_israeli_shekel_il_one.__add__('1.00')
        assert (
            new_israeli_shekel_il_one +
            new_israeli_shekel_il_two) == new_israeli_shekel_il_three


    def test_new_israeli_shekel_il_slots(self):
        """test_new_israeli_shekel_il_slots."""
        new_israeli_shekel_il = NewIsraeliShekelIL(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewIsraeliShekelIL\' '
                    'object has no attribute \'new_variable\'')):
            new_israeli_shekel_il.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the New Israeli Shekel PS representation."""

from multicurrency import NewIsraeliShekelPS


class TestNewIsraeliShekelPS:

    def test_new_israeli_shekel_ps(self):
        """test_new_israeli_shekel_ps."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        new_israeli_shekel_ps = NewIsraeliShekelPS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_ps.amount == decimal
        assert new_israeli_shekel_ps.numeric_code == '376'
        assert new_israeli_shekel_ps.alpha_code == 'ILS'
        assert new_israeli_shekel_ps.decimal_places == 2
        assert new_israeli_shekel_ps.decimal_sign == '.'
        assert new_israeli_shekel_ps.grouping_places == 3
        assert new_israeli_shekel_ps.grouping_sign == ','
        assert not new_israeli_shekel_ps.international
        assert new_israeli_shekel_ps.symbol == '₪'
        assert not new_israeli_shekel_ps.symbol_ahead
        assert new_israeli_shekel_ps.symbol_separator == '\u00A0'
        assert new_israeli_shekel_ps.localized_symbol == 'PS₪'
        assert new_israeli_shekel_ps.convertion == ''
        assert new_israeli_shekel_ps.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_ps.__repr__() == (
            'NewIsraeliShekelPS(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PS₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel_ps.__str__() == '0.14 ₪'


    def test_new_israeli_shekel_ps_negative(self):
        """test_new_israeli_shekel_ps_negative."""
        amount = -100
        new_israeli_shekel_ps = NewIsraeliShekelPS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_ps.numeric_code == '376'
        assert new_israeli_shekel_ps.alpha_code == 'ILS'
        assert new_israeli_shekel_ps.decimal_places == 2
        assert new_israeli_shekel_ps.decimal_sign == '.'
        assert new_israeli_shekel_ps.grouping_places == 3
        assert new_israeli_shekel_ps.grouping_sign == ','
        assert not new_israeli_shekel_ps.international
        assert new_israeli_shekel_ps.symbol == '₪'
        assert not new_israeli_shekel_ps.symbol_ahead
        assert new_israeli_shekel_ps.symbol_separator == '\u00A0'
        assert new_israeli_shekel_ps.localized_symbol == 'PS₪'
        assert new_israeli_shekel_ps.convertion == ''
        assert new_israeli_shekel_ps.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_ps.__repr__() == (
            'NewIsraeliShekelPS(amount: -100, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PS₪", '
            'numeric_code: "376", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert new_israeli_shekel_ps.__str__() == '-100.00 ₪'


    def test_new_israeli_shekel_ps_custom(self):
        """test_new_israeli_shekel_ps_custom."""
        amount = 1000
        new_israeli_shekel_ps = NewIsraeliShekelPS(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert new_israeli_shekel_ps.amount == decimal
        assert new_israeli_shekel_ps.numeric_code == '376'
        assert new_israeli_shekel_ps.alpha_code == 'ILS'
        assert new_israeli_shekel_ps.decimal_places == 5
        assert new_israeli_shekel_ps.decimal_sign == ','
        assert new_israeli_shekel_ps.grouping_places == 2
        assert new_israeli_shekel_ps.grouping_sign == '.'
        assert new_israeli_shekel_ps.international
        assert new_israeli_shekel_ps.symbol == '₪'
        assert not new_israeli_shekel_ps.symbol_ahead
        assert new_israeli_shekel_ps.symbol_separator == '_'
        assert new_israeli_shekel_ps.localized_symbol == 'PS₪'
        assert new_israeli_shekel_ps.convertion == ''
        assert new_israeli_shekel_ps.__hash__() == hash((decimal, 'ILS', '376'))
        assert new_israeli_shekel_ps.__repr__() == (
            'NewIsraeliShekelPS(amount: 1000, '
            'alpha_code: "ILS", '
            'symbol: "₪", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PS₪", '
            'numeric_code: "376", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert new_israeli_shekel_ps.__str__() == 'ILS 10,00.00000'


    def test_new_israeli_shekel_ps_changed(self):
        """test_cnew_israeli_shekel_ps_changed."""
        new_israeli_shekel_ps = NewIsraeliShekelPS(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            new_israeli_shekel_ps.international = True


    def test_new_israeli_shekel_ps_math_add(self):
        """test_new_israeli_shekel_ps_math_add."""
        new_israeli_shekel_ps_one = NewIsraeliShekelPS(amount=1)
        new_israeli_shekel_ps_two = NewIsraeliShekelPS(amount=2)
        new_israeli_shekel_ps_three = NewIsraeliShekelPS(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ILS and OTHER.'):
            _ = new_israeli_shekel_ps_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'shekel.NewIsraeliShekelPS\'> '
                    'and <class \'str\'>.')):
            _ = new_israeli_shekel_ps_one.__add__('1.00')
        assert (
            new_israeli_shekel_ps_one +
            new_israeli_shekel_ps_two) == new_israeli_shekel_ps_three


    def test_new_israeli_shekel_ps_slots(self):
        """test_new_israeli_shekel_ps_slots."""
        new_israeli_shekel_ps = NewIsraeliShekelPS(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NewIsraeliShekelPS\' '
                    'object has no attribute \'new_variable\'')):
            new_israeli_shekel_ps.new_variable = 'fail'  # pylint: disable=assigning-non-slot
