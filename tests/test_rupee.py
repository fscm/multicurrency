# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rupee currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Indian Rupee representation."""

from multicurrency import IndianRupee


class TestIndianRupee:
    """IndianRupee currency tests."""

    def test_indian_rupee(self):
        """test_indian_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        indian_rupee = IndianRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee.amount == decimal
        assert indian_rupee.numeric_code == '356'
        assert indian_rupee.alpha_code == 'INR'
        assert indian_rupee.decimal_places == 2
        assert indian_rupee.decimal_sign == '.'
        assert indian_rupee.grouping_places == 3
        assert indian_rupee.grouping_sign == ','
        assert not indian_rupee.international
        assert indian_rupee.symbol == '₹'
        assert indian_rupee.symbol_ahead
        assert indian_rupee.symbol_separator == ''
        assert indian_rupee.localized_symbol == '₹'
        assert indian_rupee.convertion == ''
        assert indian_rupee.__hash__() == hash(
            (indian_rupee.__class__, decimal, 'INR', '356'))
        assert indian_rupee.__repr__() == (
            'IndianRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee.__str__() == '₹0.14'

    def test_indian_rupee_negative(self):
        """test_indian_rupee_negative."""
        amount = -100
        indian_rupee = IndianRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee.numeric_code == '356'
        assert indian_rupee.alpha_code == 'INR'
        assert indian_rupee.decimal_places == 2
        assert indian_rupee.decimal_sign == '.'
        assert indian_rupee.grouping_places == 3
        assert indian_rupee.grouping_sign == ','
        assert not indian_rupee.international
        assert indian_rupee.symbol == '₹'
        assert indian_rupee.symbol_ahead
        assert indian_rupee.symbol_separator == ''
        assert indian_rupee.localized_symbol == '₹'
        assert indian_rupee.convertion == ''
        assert indian_rupee.__hash__() == hash(
            (indian_rupee.__class__, decimal, 'INR', '356'))
        assert indian_rupee.__repr__() == (
            'IndianRupee(amount: -100, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee.__str__() == '₹-100.00'

    def test_indian_rupee_custom(self):
        """test_indian_rupee_custom."""
        amount = 1000
        indian_rupee = IndianRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee.amount == decimal
        assert indian_rupee.numeric_code == '356'
        assert indian_rupee.alpha_code == 'INR'
        assert indian_rupee.decimal_places == 5
        assert indian_rupee.decimal_sign == ','
        assert indian_rupee.grouping_places == 2
        assert indian_rupee.grouping_sign == '.'
        assert indian_rupee.international
        assert indian_rupee.symbol == '₹'
        assert not indian_rupee.symbol_ahead
        assert indian_rupee.symbol_separator == '_'
        assert indian_rupee.localized_symbol == '₹'
        assert indian_rupee.convertion == ''
        assert indian_rupee.__hash__() == hash(
            (indian_rupee.__class__, decimal, 'INR', '356'))
        assert indian_rupee.__repr__() == (
            'IndianRupee(amount: 1000, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₹", '
            'numeric_code: "356", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert indian_rupee.__str__() == 'INR 10,00.00000'

    def test_indian_rupee_changed(self):
        """test_cindian_rupee_changed."""
        indian_rupee = IndianRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee.international = True

    def test_indian_rupee_math_add(self):
        """test_indian_rupee_math_add."""
        indian_rupee_one = IndianRupee(amount=1)
        indian_rupee_two = IndianRupee(amount=2)
        indian_rupee_three = IndianRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency INR and OTHER.'):
            _ = indian_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.IndianRupee\'> '
                    'and <class \'str\'>.')):
            _ = indian_rupee_one.__add__('1.00')
        assert (
            indian_rupee_one +
            indian_rupee_two) == indian_rupee_three

    def test_indian_rupee_slots(self):
        """test_indian_rupee_slots."""
        indian_rupee = IndianRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IndianRupee\' '
                    'object has no attribute \'new_variable\'')):
            indian_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Indian Rupee BT representation."""

from multicurrency import IndianRupeeBT


class TestIndianRupeeBT:
    """IndianRupeeBT currency tests."""

    def test_indian_rupee_bt(self):
        """test_indian_rupee_bt."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        indian_rupee_bt = IndianRupeeBT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_bt.amount == decimal
        assert indian_rupee_bt.numeric_code == '356'
        assert indian_rupee_bt.alpha_code == 'INR'
        assert indian_rupee_bt.decimal_places == 2
        assert indian_rupee_bt.decimal_sign == '.'
        assert indian_rupee_bt.grouping_places == 3
        assert indian_rupee_bt.grouping_sign == ','
        assert not indian_rupee_bt.international
        assert indian_rupee_bt.symbol == '₹'
        assert indian_rupee_bt.symbol_ahead
        assert indian_rupee_bt.symbol_separator == ''
        assert indian_rupee_bt.localized_symbol == 'BT₹'
        assert indian_rupee_bt.convertion == ''
        assert indian_rupee_bt.__hash__() == hash(
            (indian_rupee_bt.__class__, decimal, 'INR', '356'))
        assert indian_rupee_bt.__repr__() == (
            'IndianRupeeBT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BT₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee_bt.__str__() == '₹0.14'

    def test_indian_rupee_bt_negative(self):
        """test_indian_rupee_bt_negative."""
        amount = -100
        indian_rupee_bt = IndianRupeeBT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_bt.numeric_code == '356'
        assert indian_rupee_bt.alpha_code == 'INR'
        assert indian_rupee_bt.decimal_places == 2
        assert indian_rupee_bt.decimal_sign == '.'
        assert indian_rupee_bt.grouping_places == 3
        assert indian_rupee_bt.grouping_sign == ','
        assert not indian_rupee_bt.international
        assert indian_rupee_bt.symbol == '₹'
        assert indian_rupee_bt.symbol_ahead
        assert indian_rupee_bt.symbol_separator == ''
        assert indian_rupee_bt.localized_symbol == 'BT₹'
        assert indian_rupee_bt.convertion == ''
        assert indian_rupee_bt.__hash__() == hash(
            (indian_rupee_bt.__class__, decimal, 'INR', '356'))
        assert indian_rupee_bt.__repr__() == (
            'IndianRupeeBT(amount: -100, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "BT₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee_bt.__str__() == '₹-100.00'

    def test_indian_rupee_bt_custom(self):
        """test_indian_rupee_bt_custom."""
        amount = 1000
        indian_rupee_bt = IndianRupeeBT(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_bt.amount == decimal
        assert indian_rupee_bt.numeric_code == '356'
        assert indian_rupee_bt.alpha_code == 'INR'
        assert indian_rupee_bt.decimal_places == 5
        assert indian_rupee_bt.decimal_sign == ','
        assert indian_rupee_bt.grouping_places == 2
        assert indian_rupee_bt.grouping_sign == '.'
        assert indian_rupee_bt.international
        assert indian_rupee_bt.symbol == '₹'
        assert not indian_rupee_bt.symbol_ahead
        assert indian_rupee_bt.symbol_separator == '_'
        assert indian_rupee_bt.localized_symbol == 'BT₹'
        assert indian_rupee_bt.convertion == ''
        assert indian_rupee_bt.__hash__() == hash(
            (indian_rupee_bt.__class__, decimal, 'INR', '356'))
        assert indian_rupee_bt.__repr__() == (
            'IndianRupeeBT(amount: 1000, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BT₹", '
            'numeric_code: "356", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert indian_rupee_bt.__str__() == 'INR 10,00.00000'

    def test_indian_rupee_bt_changed(self):
        """test_cindian_rupee_bt_changed."""
        indian_rupee_bt = IndianRupeeBT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_bt.international = True

    def test_indian_rupee_bt_math_add(self):
        """test_indian_rupee_bt_math_add."""
        indian_rupee_bt_one = IndianRupeeBT(amount=1)
        indian_rupee_bt_two = IndianRupeeBT(amount=2)
        indian_rupee_bt_three = IndianRupeeBT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency INR and OTHER.'):
            _ = indian_rupee_bt_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.IndianRupeeBT\'> '
                    'and <class \'str\'>.')):
            _ = indian_rupee_bt_one.__add__('1.00')
        assert (
            indian_rupee_bt_one +
            indian_rupee_bt_two) == indian_rupee_bt_three

    def test_indian_rupee_bt_slots(self):
        """test_indian_rupee_bt_slots."""
        indian_rupee_bt = IndianRupeeBT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IndianRupeeBT\' '
                    'object has no attribute \'new_variable\'')):
            indian_rupee_bt.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Indian Rupee IN representation."""

from multicurrency import IndianRupeeIN


class TestIndianRupeeIN:
    """IndianRupeeIN currency tests."""

    def test_indian_rupee_in(self):
        """test_indian_rupee_in."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        indian_rupee_in = IndianRupeeIN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_in.amount == decimal
        assert indian_rupee_in.numeric_code == '356'
        assert indian_rupee_in.alpha_code == 'INR'
        assert indian_rupee_in.decimal_places == 2
        assert indian_rupee_in.decimal_sign == '.'
        assert indian_rupee_in.grouping_places == 3
        assert indian_rupee_in.grouping_sign == ','
        assert not indian_rupee_in.international
        assert indian_rupee_in.symbol == '₹'
        assert indian_rupee_in.symbol_ahead
        assert indian_rupee_in.symbol_separator == ''
        assert indian_rupee_in.localized_symbol == 'IN₹'
        assert indian_rupee_in.convertion == ''
        assert indian_rupee_in.__hash__() == hash(
            (indian_rupee_in.__class__, decimal, 'INR', '356'))
        assert indian_rupee_in.__repr__() == (
            'IndianRupeeIN(amount: 0.1428571428571428571428571429, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IN₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee_in.__str__() == '₹0.14'

    def test_indian_rupee_in_negative(self):
        """test_indian_rupee_in_negative."""
        amount = -100
        indian_rupee_in = IndianRupeeIN(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_in.numeric_code == '356'
        assert indian_rupee_in.alpha_code == 'INR'
        assert indian_rupee_in.decimal_places == 2
        assert indian_rupee_in.decimal_sign == '.'
        assert indian_rupee_in.grouping_places == 3
        assert indian_rupee_in.grouping_sign == ','
        assert not indian_rupee_in.international
        assert indian_rupee_in.symbol == '₹'
        assert indian_rupee_in.symbol_ahead
        assert indian_rupee_in.symbol_separator == ''
        assert indian_rupee_in.localized_symbol == 'IN₹'
        assert indian_rupee_in.convertion == ''
        assert indian_rupee_in.__hash__() == hash(
            (indian_rupee_in.__class__, decimal, 'INR', '356'))
        assert indian_rupee_in.__repr__() == (
            'IndianRupeeIN(amount: -100, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IN₹", '
            'numeric_code: "356", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert indian_rupee_in.__str__() == '₹-100.00'

    def test_indian_rupee_in_custom(self):
        """test_indian_rupee_in_custom."""
        amount = 1000
        indian_rupee_in = IndianRupeeIN(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert indian_rupee_in.amount == decimal
        assert indian_rupee_in.numeric_code == '356'
        assert indian_rupee_in.alpha_code == 'INR'
        assert indian_rupee_in.decimal_places == 5
        assert indian_rupee_in.decimal_sign == ','
        assert indian_rupee_in.grouping_places == 2
        assert indian_rupee_in.grouping_sign == '.'
        assert indian_rupee_in.international
        assert indian_rupee_in.symbol == '₹'
        assert not indian_rupee_in.symbol_ahead
        assert indian_rupee_in.symbol_separator == '_'
        assert indian_rupee_in.localized_symbol == 'IN₹'
        assert indian_rupee_in.convertion == ''
        assert indian_rupee_in.__hash__() == hash(
            (indian_rupee_in.__class__, decimal, 'INR', '356'))
        assert indian_rupee_in.__repr__() == (
            'IndianRupeeIN(amount: 1000, '
            'alpha_code: "INR", '
            'symbol: "₹", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IN₹", '
            'numeric_code: "356", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert indian_rupee_in.__str__() == 'INR 10,00.00000'

    def test_indian_rupee_in_changed(self):
        """test_cindian_rupee_in_changed."""
        indian_rupee_in = IndianRupeeIN(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            indian_rupee_in.international = True

    def test_indian_rupee_in_math_add(self):
        """test_indian_rupee_in_math_add."""
        indian_rupee_in_one = IndianRupeeIN(amount=1)
        indian_rupee_in_two = IndianRupeeIN(amount=2)
        indian_rupee_in_three = IndianRupeeIN(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency INR and OTHER.'):
            _ = indian_rupee_in_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.IndianRupeeIN\'> '
                    'and <class \'str\'>.')):
            _ = indian_rupee_in_one.__add__('1.00')
        assert (
            indian_rupee_in_one +
            indian_rupee_in_two) == indian_rupee_in_three

    def test_indian_rupee_in_slots(self):
        """test_indian_rupee_in_slots."""
        indian_rupee_in = IndianRupeeIN(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IndianRupeeIN\' '
                    'object has no attribute \'new_variable\'')):
            indian_rupee_in.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Sri Lanka Rupee representation."""

from multicurrency import SriLankaRupee


class TestSriLankaRupee:
    """SriLankaRupee currency tests."""

    def test_sri_lanka_rupee(self):
        """test_sri_lanka_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        sri_lanka_rupee = SriLankaRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert sri_lanka_rupee.amount == decimal
        assert sri_lanka_rupee.numeric_code == '144'
        assert sri_lanka_rupee.alpha_code == 'LKR'
        assert sri_lanka_rupee.decimal_places == 2
        assert sri_lanka_rupee.decimal_sign == '.'
        assert sri_lanka_rupee.grouping_places == 3
        assert sri_lanka_rupee.grouping_sign == ','
        assert not sri_lanka_rupee.international
        assert sri_lanka_rupee.symbol == 'රු.'
        assert sri_lanka_rupee.symbol_ahead
        assert sri_lanka_rupee.symbol_separator == '\u00A0'
        assert sri_lanka_rupee.localized_symbol == 'රු.'
        assert sri_lanka_rupee.convertion == ''
        assert sri_lanka_rupee.__hash__() == hash(
            (sri_lanka_rupee.__class__, decimal, 'LKR', '144'))
        assert sri_lanka_rupee.__repr__() == (
            'SriLankaRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "LKR", '
            'symbol: "රු.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "රු.", '
            'numeric_code: "144", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert sri_lanka_rupee.__str__() == 'රු. 0.14'

    def test_sri_lanka_rupee_negative(self):
        """test_sri_lanka_rupee_negative."""
        amount = -100
        sri_lanka_rupee = SriLankaRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert sri_lanka_rupee.numeric_code == '144'
        assert sri_lanka_rupee.alpha_code == 'LKR'
        assert sri_lanka_rupee.decimal_places == 2
        assert sri_lanka_rupee.decimal_sign == '.'
        assert sri_lanka_rupee.grouping_places == 3
        assert sri_lanka_rupee.grouping_sign == ','
        assert not sri_lanka_rupee.international
        assert sri_lanka_rupee.symbol == 'රු.'
        assert sri_lanka_rupee.symbol_ahead
        assert sri_lanka_rupee.symbol_separator == '\u00A0'
        assert sri_lanka_rupee.localized_symbol == 'රු.'
        assert sri_lanka_rupee.convertion == ''
        assert sri_lanka_rupee.__hash__() == hash(
            (sri_lanka_rupee.__class__, decimal, 'LKR', '144'))
        assert sri_lanka_rupee.__repr__() == (
            'SriLankaRupee(amount: -100, '
            'alpha_code: "LKR", '
            'symbol: "රු.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "රු.", '
            'numeric_code: "144", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert sri_lanka_rupee.__str__() == 'රු. -100.00'

    def test_sri_lanka_rupee_custom(self):
        """test_sri_lanka_rupee_custom."""
        amount = 1000
        sri_lanka_rupee = SriLankaRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert sri_lanka_rupee.amount == decimal
        assert sri_lanka_rupee.numeric_code == '144'
        assert sri_lanka_rupee.alpha_code == 'LKR'
        assert sri_lanka_rupee.decimal_places == 5
        assert sri_lanka_rupee.decimal_sign == ','
        assert sri_lanka_rupee.grouping_places == 2
        assert sri_lanka_rupee.grouping_sign == '.'
        assert sri_lanka_rupee.international
        assert sri_lanka_rupee.symbol == 'රු.'
        assert not sri_lanka_rupee.symbol_ahead
        assert sri_lanka_rupee.symbol_separator == '_'
        assert sri_lanka_rupee.localized_symbol == 'රු.'
        assert sri_lanka_rupee.convertion == ''
        assert sri_lanka_rupee.__hash__() == hash(
            (sri_lanka_rupee.__class__, decimal, 'LKR', '144'))
        assert sri_lanka_rupee.__repr__() == (
            'SriLankaRupee(amount: 1000, '
            'alpha_code: "LKR", '
            'symbol: "රු.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "රු.", '
            'numeric_code: "144", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert sri_lanka_rupee.__str__() == 'LKR 10,00.00000'

    def test_sri_lanka_rupee_changed(self):
        """test_csri_lanka_rupee_changed."""
        sri_lanka_rupee = SriLankaRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            sri_lanka_rupee.international = True

    def test_sri_lanka_rupee_math_add(self):
        """test_sri_lanka_rupee_math_add."""
        sri_lanka_rupee_one = SriLankaRupee(amount=1)
        sri_lanka_rupee_two = SriLankaRupee(amount=2)
        sri_lanka_rupee_three = SriLankaRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency LKR and OTHER.'):
            _ = sri_lanka_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.SriLankaRupee\'> '
                    'and <class \'str\'>.')):
            _ = sri_lanka_rupee_one.__add__('1.00')
        assert (
            sri_lanka_rupee_one +
            sri_lanka_rupee_two) == sri_lanka_rupee_three

    def test_sri_lanka_rupee_slots(self):
        """test_sri_lanka_rupee_slots."""
        sri_lanka_rupee = SriLankaRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SriLankaRupee\' '
                    'object has no attribute \'new_variable\'')):
            sri_lanka_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Mauritius Rupee representation."""

from multicurrency import MauritiusRupee


class TestMauritiusRupee:
    """MauritiusRupee currency tests."""

    def test_mauritius_rupee(self):
        """test_mauritius_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        mauritius_rupee = MauritiusRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert mauritius_rupee.amount == decimal
        assert mauritius_rupee.numeric_code == '480'
        assert mauritius_rupee.alpha_code == 'MUR'
        assert mauritius_rupee.decimal_places == 2
        assert mauritius_rupee.decimal_sign == '.'
        assert mauritius_rupee.grouping_places == 3
        assert mauritius_rupee.grouping_sign == ','
        assert not mauritius_rupee.international
        assert mauritius_rupee.symbol == '₨'
        assert mauritius_rupee.symbol_ahead
        assert mauritius_rupee.symbol_separator == '\u00A0'
        assert mauritius_rupee.localized_symbol == '₨'
        assert mauritius_rupee.convertion == ''
        assert mauritius_rupee.__hash__() == hash(
            (mauritius_rupee.__class__, decimal, 'MUR', '480'))
        assert mauritius_rupee.__repr__() == (
            'MauritiusRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MUR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "480", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert mauritius_rupee.__str__() == '₨ 0.14'

    def test_mauritius_rupee_negative(self):
        """test_mauritius_rupee_negative."""
        amount = -100
        mauritius_rupee = MauritiusRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert mauritius_rupee.numeric_code == '480'
        assert mauritius_rupee.alpha_code == 'MUR'
        assert mauritius_rupee.decimal_places == 2
        assert mauritius_rupee.decimal_sign == '.'
        assert mauritius_rupee.grouping_places == 3
        assert mauritius_rupee.grouping_sign == ','
        assert not mauritius_rupee.international
        assert mauritius_rupee.symbol == '₨'
        assert mauritius_rupee.symbol_ahead
        assert mauritius_rupee.symbol_separator == '\u00A0'
        assert mauritius_rupee.localized_symbol == '₨'
        assert mauritius_rupee.convertion == ''
        assert mauritius_rupee.__hash__() == hash(
            (mauritius_rupee.__class__, decimal, 'MUR', '480'))
        assert mauritius_rupee.__repr__() == (
            'MauritiusRupee(amount: -100, '
            'alpha_code: "MUR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "480", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert mauritius_rupee.__str__() == '₨ -100.00'

    def test_mauritius_rupee_custom(self):
        """test_mauritius_rupee_custom."""
        amount = 1000
        mauritius_rupee = MauritiusRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert mauritius_rupee.amount == decimal
        assert mauritius_rupee.numeric_code == '480'
        assert mauritius_rupee.alpha_code == 'MUR'
        assert mauritius_rupee.decimal_places == 5
        assert mauritius_rupee.decimal_sign == ','
        assert mauritius_rupee.grouping_places == 2
        assert mauritius_rupee.grouping_sign == '.'
        assert mauritius_rupee.international
        assert mauritius_rupee.symbol == '₨'
        assert not mauritius_rupee.symbol_ahead
        assert mauritius_rupee.symbol_separator == '_'
        assert mauritius_rupee.localized_symbol == '₨'
        assert mauritius_rupee.convertion == ''
        assert mauritius_rupee.__hash__() == hash(
            (mauritius_rupee.__class__, decimal, 'MUR', '480'))
        assert mauritius_rupee.__repr__() == (
            'MauritiusRupee(amount: 1000, '
            'alpha_code: "MUR", '
            'symbol: "₨", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₨", '
            'numeric_code: "480", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert mauritius_rupee.__str__() == 'MUR 10,00.00000'

    def test_mauritius_rupee_changed(self):
        """test_cmauritius_rupee_changed."""
        mauritius_rupee = MauritiusRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mauritius_rupee.international = True

    def test_mauritius_rupee_math_add(self):
        """test_mauritius_rupee_math_add."""
        mauritius_rupee_one = MauritiusRupee(amount=1)
        mauritius_rupee_two = MauritiusRupee(amount=2)
        mauritius_rupee_three = MauritiusRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MUR and OTHER.'):
            _ = mauritius_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.MauritiusRupee\'> '
                    'and <class \'str\'>.')):
            _ = mauritius_rupee_one.__add__('1.00')
        assert (
            mauritius_rupee_one +
            mauritius_rupee_two) == mauritius_rupee_three

    def test_mauritius_rupee_slots(self):
        """test_mauritius_rupee_slots."""
        mauritius_rupee = MauritiusRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'MauritiusRupee\' '
                    'object has no attribute \'new_variable\'')):
            mauritius_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Nepalese Rupee representation."""

from multicurrency import NepaleseRupee


class TestNepaleseRupee:
    """NepaleseRupee currency tests."""

    def test_nepalese_rupee(self):
        """test_nepalese_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        nepalese_rupee = NepaleseRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert nepalese_rupee.amount == decimal
        assert nepalese_rupee.numeric_code == '524'
        assert nepalese_rupee.alpha_code == 'NPR'
        assert nepalese_rupee.decimal_places == 2
        assert nepalese_rupee.decimal_sign == '.'
        assert nepalese_rupee.grouping_places == 3
        assert nepalese_rupee.grouping_sign == ','
        assert not nepalese_rupee.international
        assert nepalese_rupee.symbol == 'नेरू'
        assert nepalese_rupee.symbol_ahead
        assert nepalese_rupee.symbol_separator == '\u00A0'
        assert nepalese_rupee.localized_symbol == 'नेरू'
        assert nepalese_rupee.convertion == '०१२३४५६७८९-'
        assert nepalese_rupee.__hash__() == hash(
            (nepalese_rupee.__class__, decimal, 'NPR', '524'))
        assert nepalese_rupee.__repr__() == (
            'NepaleseRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "NPR", '
            'symbol: "नेरू", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "नेरू", '
            'numeric_code: "524", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "०१२३४५६७८९-", '
            'international: False)')
        assert nepalese_rupee.__str__() == 'नेरू ०.१४'

    def test_nepalese_rupee_negative(self):
        """test_nepalese_rupee_negative."""
        amount = -100
        nepalese_rupee = NepaleseRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert nepalese_rupee.numeric_code == '524'
        assert nepalese_rupee.alpha_code == 'NPR'
        assert nepalese_rupee.decimal_places == 2
        assert nepalese_rupee.decimal_sign == '.'
        assert nepalese_rupee.grouping_places == 3
        assert nepalese_rupee.grouping_sign == ','
        assert not nepalese_rupee.international
        assert nepalese_rupee.symbol == 'नेरू'
        assert nepalese_rupee.symbol_ahead
        assert nepalese_rupee.symbol_separator == '\u00A0'
        assert nepalese_rupee.localized_symbol == 'नेरू'
        assert nepalese_rupee.convertion == '०१२३४५६७८९-'
        assert nepalese_rupee.__hash__() == hash(
            (nepalese_rupee.__class__, decimal, 'NPR', '524'))
        assert nepalese_rupee.__repr__() == (
            'NepaleseRupee(amount: -100, '
            'alpha_code: "NPR", '
            'symbol: "नेरू", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "नेरू", '
            'numeric_code: "524", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "०१२३४५६७८९-", '
            'international: False)')
        assert nepalese_rupee.__str__() == 'नेरू -१००.००'

    def test_nepalese_rupee_custom(self):
        """test_nepalese_rupee_custom."""
        amount = 1000
        nepalese_rupee = NepaleseRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert nepalese_rupee.amount == decimal
        assert nepalese_rupee.numeric_code == '524'
        assert nepalese_rupee.alpha_code == 'NPR'
        assert nepalese_rupee.decimal_places == 5
        assert nepalese_rupee.decimal_sign == ','
        assert nepalese_rupee.grouping_places == 2
        assert nepalese_rupee.grouping_sign == '.'
        assert nepalese_rupee.international
        assert nepalese_rupee.symbol == 'नेरू'
        assert not nepalese_rupee.symbol_ahead
        assert nepalese_rupee.symbol_separator == '_'
        assert nepalese_rupee.localized_symbol == 'नेरू'
        assert nepalese_rupee.convertion == '०१२३४५६७८९-'
        assert nepalese_rupee.__hash__() == hash(
            (nepalese_rupee.__class__, decimal, 'NPR', '524'))
        assert nepalese_rupee.__repr__() == (
            'NepaleseRupee(amount: 1000, '
            'alpha_code: "NPR", '
            'symbol: "नेरू", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "नेरू", '
            'numeric_code: "524", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "०१२३४५६७८९-", '
            'international: True)')
        assert nepalese_rupee.__str__() == 'NPR 10,00.00000'

    def test_nepalese_rupee_changed(self):
        """test_cnepalese_rupee_changed."""
        nepalese_rupee = NepaleseRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            nepalese_rupee.international = True

    def test_nepalese_rupee_math_add(self):
        """test_nepalese_rupee_math_add."""
        nepalese_rupee_one = NepaleseRupee(amount=1)
        nepalese_rupee_two = NepaleseRupee(amount=2)
        nepalese_rupee_three = NepaleseRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency NPR and OTHER.'):
            _ = nepalese_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.NepaleseRupee\'> '
                    'and <class \'str\'>.')):
            _ = nepalese_rupee_one.__add__('1.00')
        assert (
            nepalese_rupee_one +
            nepalese_rupee_two) == nepalese_rupee_three

    def test_nepalese_rupee_slots(self):
        """test_nepalese_rupee_slots."""
        nepalese_rupee = NepaleseRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'NepaleseRupee\' '
                    'object has no attribute \'new_variable\'')):
            nepalese_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Pakistan Rupee representation."""

from multicurrency import PakistanRupee


class TestPakistanRupee:
    """PakistanRupee currency tests."""

    def test_pakistan_rupee(self):
        """test_pakistan_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        pakistan_rupee = PakistanRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pakistan_rupee.amount == decimal
        assert pakistan_rupee.numeric_code == '586'
        assert pakistan_rupee.alpha_code == 'PKR'
        assert pakistan_rupee.decimal_places == 2
        assert pakistan_rupee.decimal_sign == '.'
        assert pakistan_rupee.grouping_places == 3
        assert pakistan_rupee.grouping_sign == ','
        assert not pakistan_rupee.international
        assert pakistan_rupee.symbol == '₨'
        assert pakistan_rupee.symbol_ahead
        assert pakistan_rupee.symbol_separator == '\u00A0'
        assert pakistan_rupee.localized_symbol == '₨'
        assert pakistan_rupee.convertion == ''
        assert pakistan_rupee.__hash__() == hash(
            (pakistan_rupee.__class__, decimal, 'PKR', '586'))
        assert pakistan_rupee.__repr__() == (
            'PakistanRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "PKR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "586", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pakistan_rupee.__str__() == '₨ 0.14'

    def test_pakistan_rupee_negative(self):
        """test_pakistan_rupee_negative."""
        amount = -100
        pakistan_rupee = PakistanRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert pakistan_rupee.numeric_code == '586'
        assert pakistan_rupee.alpha_code == 'PKR'
        assert pakistan_rupee.decimal_places == 2
        assert pakistan_rupee.decimal_sign == '.'
        assert pakistan_rupee.grouping_places == 3
        assert pakistan_rupee.grouping_sign == ','
        assert not pakistan_rupee.international
        assert pakistan_rupee.symbol == '₨'
        assert pakistan_rupee.symbol_ahead
        assert pakistan_rupee.symbol_separator == '\u00A0'
        assert pakistan_rupee.localized_symbol == '₨'
        assert pakistan_rupee.convertion == ''
        assert pakistan_rupee.__hash__() == hash(
            (pakistan_rupee.__class__, decimal, 'PKR', '586'))
        assert pakistan_rupee.__repr__() == (
            'PakistanRupee(amount: -100, '
            'alpha_code: "PKR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "586", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert pakistan_rupee.__str__() == '₨ -100.00'

    def test_pakistan_rupee_custom(self):
        """test_pakistan_rupee_custom."""
        amount = 1000
        pakistan_rupee = PakistanRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert pakistan_rupee.amount == decimal
        assert pakistan_rupee.numeric_code == '586'
        assert pakistan_rupee.alpha_code == 'PKR'
        assert pakistan_rupee.decimal_places == 5
        assert pakistan_rupee.decimal_sign == ','
        assert pakistan_rupee.grouping_places == 2
        assert pakistan_rupee.grouping_sign == '.'
        assert pakistan_rupee.international
        assert pakistan_rupee.symbol == '₨'
        assert not pakistan_rupee.symbol_ahead
        assert pakistan_rupee.symbol_separator == '_'
        assert pakistan_rupee.localized_symbol == '₨'
        assert pakistan_rupee.convertion == ''
        assert pakistan_rupee.__hash__() == hash(
            (pakistan_rupee.__class__, decimal, 'PKR', '586'))
        assert pakistan_rupee.__repr__() == (
            'PakistanRupee(amount: 1000, '
            'alpha_code: "PKR", '
            'symbol: "₨", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₨", '
            'numeric_code: "586", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert pakistan_rupee.__str__() == 'PKR 10,00.00000'

    def test_pakistan_rupee_changed(self):
        """test_cpakistan_rupee_changed."""
        pakistan_rupee = PakistanRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            pakistan_rupee.international = True

    def test_pakistan_rupee_math_add(self):
        """test_pakistan_rupee_math_add."""
        pakistan_rupee_one = PakistanRupee(amount=1)
        pakistan_rupee_two = PakistanRupee(amount=2)
        pakistan_rupee_three = PakistanRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency PKR and OTHER.'):
            _ = pakistan_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.PakistanRupee\'> '
                    'and <class \'str\'>.')):
            _ = pakistan_rupee_one.__add__('1.00')
        assert (
            pakistan_rupee_one +
            pakistan_rupee_two) == pakistan_rupee_three

    def test_pakistan_rupee_slots(self):
        """test_pakistan_rupee_slots."""
        pakistan_rupee = PakistanRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PakistanRupee\' '
                    'object has no attribute \'new_variable\'')):
            pakistan_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Seychelles Rupee representation."""

from multicurrency import SeychellesRupee


class TestSeychellesRupee:
    """SeychellesRupee currency tests."""

    def test_seychelles_rupee(self):
        """test_seychelles_rupee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        seychelles_rupee = SeychellesRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert seychelles_rupee.amount == decimal
        assert seychelles_rupee.numeric_code == '690'
        assert seychelles_rupee.alpha_code == 'SCR'
        assert seychelles_rupee.decimal_places == 2
        assert seychelles_rupee.decimal_sign == '.'
        assert seychelles_rupee.grouping_places == 3
        assert seychelles_rupee.grouping_sign == ','
        assert not seychelles_rupee.international
        assert seychelles_rupee.symbol == '₨'
        assert seychelles_rupee.symbol_ahead
        assert seychelles_rupee.symbol_separator == '\u00A0'
        assert seychelles_rupee.localized_symbol == '₨'
        assert seychelles_rupee.convertion == ''
        assert seychelles_rupee.__hash__() == hash(
            (seychelles_rupee.__class__, decimal, 'SCR', '690'))
        assert seychelles_rupee.__repr__() == (
            'SeychellesRupee(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SCR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "690", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert seychelles_rupee.__str__() == '₨ 0.14'

    def test_seychelles_rupee_negative(self):
        """test_seychelles_rupee_negative."""
        amount = -100
        seychelles_rupee = SeychellesRupee(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert seychelles_rupee.numeric_code == '690'
        assert seychelles_rupee.alpha_code == 'SCR'
        assert seychelles_rupee.decimal_places == 2
        assert seychelles_rupee.decimal_sign == '.'
        assert seychelles_rupee.grouping_places == 3
        assert seychelles_rupee.grouping_sign == ','
        assert not seychelles_rupee.international
        assert seychelles_rupee.symbol == '₨'
        assert seychelles_rupee.symbol_ahead
        assert seychelles_rupee.symbol_separator == '\u00A0'
        assert seychelles_rupee.localized_symbol == '₨'
        assert seychelles_rupee.convertion == ''
        assert seychelles_rupee.__hash__() == hash(
            (seychelles_rupee.__class__, decimal, 'SCR', '690'))
        assert seychelles_rupee.__repr__() == (
            'SeychellesRupee(amount: -100, '
            'alpha_code: "SCR", '
            'symbol: "₨", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "₨", '
            'numeric_code: "690", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert seychelles_rupee.__str__() == '₨ -100.00'

    def test_seychelles_rupee_custom(self):
        """test_seychelles_rupee_custom."""
        amount = 1000
        seychelles_rupee = SeychellesRupee(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert seychelles_rupee.amount == decimal
        assert seychelles_rupee.numeric_code == '690'
        assert seychelles_rupee.alpha_code == 'SCR'
        assert seychelles_rupee.decimal_places == 5
        assert seychelles_rupee.decimal_sign == ','
        assert seychelles_rupee.grouping_places == 2
        assert seychelles_rupee.grouping_sign == '.'
        assert seychelles_rupee.international
        assert seychelles_rupee.symbol == '₨'
        assert not seychelles_rupee.symbol_ahead
        assert seychelles_rupee.symbol_separator == '_'
        assert seychelles_rupee.localized_symbol == '₨'
        assert seychelles_rupee.convertion == ''
        assert seychelles_rupee.__hash__() == hash(
            (seychelles_rupee.__class__, decimal, 'SCR', '690'))
        assert seychelles_rupee.__repr__() == (
            'SeychellesRupee(amount: 1000, '
            'alpha_code: "SCR", '
            'symbol: "₨", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₨", '
            'numeric_code: "690", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert seychelles_rupee.__str__() == 'SCR 10,00.00000'

    def test_seychelles_rupee_changed(self):
        """test_cseychelles_rupee_changed."""
        seychelles_rupee = SeychellesRupee(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            seychelles_rupee.international = True

    def test_seychelles_rupee_math_add(self):
        """test_seychelles_rupee_math_add."""
        seychelles_rupee_one = SeychellesRupee(amount=1)
        seychelles_rupee_two = SeychellesRupee(amount=2)
        seychelles_rupee_three = SeychellesRupee(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SCR and OTHER.'):
            _ = seychelles_rupee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'rupee.SeychellesRupee\'> '
                    'and <class \'str\'>.')):
            _ = seychelles_rupee_one.__add__('1.00')
        assert (
            seychelles_rupee_one +
            seychelles_rupee_two) == seychelles_rupee_three

    def test_seychelles_rupee_slots(self):
        """test_seychelles_rupee_slots."""
        seychelles_rupee = SeychellesRupee(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SeychellesRupee\' '
                    'object has no attribute \'new_variable\'')):
            seychelles_rupee.new_variable = 'fail'  # pylint: disable=assigning-non-slot
