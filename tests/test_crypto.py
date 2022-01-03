# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Crypto currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the EOS representation."""

from multicurrency import EOS


class TestEOS:
    """EOS currency tests."""

    def test_eos(self):
        """test_eos."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eos = EOS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eos.amount == decimal
        assert eos.numeric_code == '0'
        assert eos.alpha_code == 'EOS'
        assert eos.decimal_places == 4
        assert eos.decimal_sign == '.'
        assert eos.grouping_places == 3
        assert eos.grouping_sign == ','
        assert not eos.international
        assert eos.symbol == 'ε'
        assert eos.symbol_ahead
        assert eos.symbol_separator == ''
        assert eos.localized_symbol == 'ε'
        assert eos.convertion == ''
        assert eos.__hash__() == hash(
            (eos.__class__, decimal, 'EOS', '0'))
        assert eos.__repr__() == (
            'EOS(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EOS", '
            'symbol: "ε", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ε", '
            'numeric_code: "0", '
            'decimal_places: "4", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eos.__str__() == 'ε0.1429'

    def test_eos_negative(self):
        """test_eos_negative."""
        amount = -100
        eos = EOS(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eos.numeric_code == '0'
        assert eos.alpha_code == 'EOS'
        assert eos.decimal_places == 4
        assert eos.decimal_sign == '.'
        assert eos.grouping_places == 3
        assert eos.grouping_sign == ','
        assert not eos.international
        assert eos.symbol == 'ε'
        assert eos.symbol_ahead
        assert eos.symbol_separator == ''
        assert eos.localized_symbol == 'ε'
        assert eos.convertion == ''
        assert eos.__hash__() == hash(
            (eos.__class__, decimal, 'EOS', '0'))
        assert eos.__repr__() == (
            'EOS(amount: -100, '
            'alpha_code: "EOS", '
            'symbol: "ε", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ε", '
            'numeric_code: "0", '
            'decimal_places: "4", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eos.__str__() == 'ε-100.0000'

    def test_eos_custom(self):
        """test_eos_custom."""
        amount = 1000
        eos = EOS(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eos.amount == decimal
        assert eos.numeric_code == '0'
        assert eos.alpha_code == 'EOS'
        assert eos.decimal_places == 5
        assert eos.decimal_sign == ','
        assert eos.grouping_places == 2
        assert eos.grouping_sign == '.'
        assert eos.international
        assert eos.symbol == 'ε'
        assert not eos.symbol_ahead
        assert eos.symbol_separator == '_'
        assert eos.localized_symbol == 'ε'
        assert eos.convertion == ''
        assert eos.__hash__() == hash(
            (eos.__class__, decimal, 'EOS', '0'))
        assert eos.__repr__() == (
            'EOS(amount: 1000, '
            'alpha_code: "EOS", '
            'symbol: "ε", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ε", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eos.__str__() == 'EOS 10,00.00000'

    def test_eos_changed(self):
        """test_ceos_changed."""
        eos = EOS(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eos.international = True

    def test_eos_math_add(self):
        """test_eos_math_add."""
        eos_one = EOS(amount=1)
        eos_two = EOS(amount=2)
        eos_three = EOS(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EOS and OTHER.'):
            _ = eos_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.EOS\'> '
                    'and <class \'str\'>.')):
            _ = eos_one.__add__('1.00')
        assert (
            eos_one +
            eos_two) == eos_three

    def test_eos_slots(self):
        """test_eos_slots."""
        eos = EOS(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EOS\' '
                    'object has no attribute \'new_variable\'')):
            eos.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Ethereum representation."""

from multicurrency import Ethereum


class TestEthereum:
    """Ethereum currency tests."""

    def test_ethereum(self):
        """test_ethereum."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        ethereum = Ethereum(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ethereum.amount == decimal
        assert ethereum.numeric_code == '0'
        assert ethereum.alpha_code == 'ETH'
        assert ethereum.decimal_places == 18
        assert ethereum.decimal_sign == '.'
        assert ethereum.grouping_places == 3
        assert ethereum.grouping_sign == ','
        assert not ethereum.international
        assert ethereum.symbol == 'Ξ'
        assert ethereum.symbol_ahead
        assert ethereum.symbol_separator == ''
        assert ethereum.localized_symbol == 'Ξ'
        assert ethereum.convertion == ''
        assert ethereum.__hash__() == hash(
            (ethereum.__class__, decimal, 'ETH', '0'))
        assert ethereum.__repr__() == (
            'Ethereum(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ETH", '
            'symbol: "Ξ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "Ξ", '
            'numeric_code: "0", '
            'decimal_places: "18", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ethereum.__str__() == 'Ξ0.142857142857142857'

    def test_ethereum_negative(self):
        """test_ethereum_negative."""
        amount = -100
        ethereum = Ethereum(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ethereum.numeric_code == '0'
        assert ethereum.alpha_code == 'ETH'
        assert ethereum.decimal_places == 18
        assert ethereum.decimal_sign == '.'
        assert ethereum.grouping_places == 3
        assert ethereum.grouping_sign == ','
        assert not ethereum.international
        assert ethereum.symbol == 'Ξ'
        assert ethereum.symbol_ahead
        assert ethereum.symbol_separator == ''
        assert ethereum.localized_symbol == 'Ξ'
        assert ethereum.convertion == ''
        assert ethereum.__hash__() == hash(
            (ethereum.__class__, decimal, 'ETH', '0'))
        assert ethereum.__repr__() == (
            'Ethereum(amount: -100, '
            'alpha_code: "ETH", '
            'symbol: "Ξ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "Ξ", '
            'numeric_code: "0", '
            'decimal_places: "18", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ethereum.__str__() == 'Ξ-100.000000000000000000'

    def test_ethereum_custom(self):
        """test_ethereum_custom."""
        amount = 1000
        ethereum = Ethereum(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert ethereum.amount == decimal
        assert ethereum.numeric_code == '0'
        assert ethereum.alpha_code == 'ETH'
        assert ethereum.decimal_places == 5
        assert ethereum.decimal_sign == ','
        assert ethereum.grouping_places == 2
        assert ethereum.grouping_sign == '.'
        assert ethereum.international
        assert ethereum.symbol == 'Ξ'
        assert not ethereum.symbol_ahead
        assert ethereum.symbol_separator == '_'
        assert ethereum.localized_symbol == 'Ξ'
        assert ethereum.convertion == ''
        assert ethereum.__hash__() == hash(
            (ethereum.__class__, decimal, 'ETH', '0'))
        assert ethereum.__repr__() == (
            'Ethereum(amount: 1000, '
            'alpha_code: "ETH", '
            'symbol: "Ξ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Ξ", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert ethereum.__str__() == 'ETH 10,00.00000'

    def test_ethereum_changed(self):
        """test_cethereum_changed."""
        ethereum = Ethereum(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ethereum.international = True

    def test_ethereum_math_add(self):
        """test_ethereum_math_add."""
        ethereum_one = Ethereum(amount=1)
        ethereum_two = Ethereum(amount=2)
        ethereum_three = Ethereum(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ETH and OTHER.'):
            _ = ethereum_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Ethereum\'> '
                    'and <class \'str\'>.')):
            _ = ethereum_one.__add__('1.00')
        assert (
            ethereum_one +
            ethereum_two) == ethereum_three

    def test_ethereum_slots(self):
        """test_ethereum_slots."""
        ethereum = Ethereum(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Ethereum\' '
                    'object has no attribute \'new_variable\'')):
            ethereum.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Bitcoin representation."""

from multicurrency import Bitcoin


class TestBitcoin:
    """Bitcoin currency tests."""

    def test_bitcoin(self):
        """test_bitcoin."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        bitcoin = Bitcoin(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bitcoin.amount == decimal
        assert bitcoin.numeric_code == '0'
        assert bitcoin.alpha_code == 'XBT'
        assert bitcoin.decimal_places == 8
        assert bitcoin.decimal_sign == '.'
        assert bitcoin.grouping_places == 3
        assert bitcoin.grouping_sign == ','
        assert not bitcoin.international
        assert bitcoin.symbol == '₿'
        assert bitcoin.symbol_ahead
        assert bitcoin.symbol_separator == ''
        assert bitcoin.localized_symbol == '₿'
        assert bitcoin.convertion == ''
        assert bitcoin.__hash__() == hash(
            (bitcoin.__class__, decimal, 'XBT', '0'))
        assert bitcoin.__repr__() == (
            'Bitcoin(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XBT", '
            'symbol: "₿", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₿", '
            'numeric_code: "0", '
            'decimal_places: "8", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bitcoin.__str__() == '₿0.14285714'

    def test_bitcoin_negative(self):
        """test_bitcoin_negative."""
        amount = -100
        bitcoin = Bitcoin(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert bitcoin.numeric_code == '0'
        assert bitcoin.alpha_code == 'XBT'
        assert bitcoin.decimal_places == 8
        assert bitcoin.decimal_sign == '.'
        assert bitcoin.grouping_places == 3
        assert bitcoin.grouping_sign == ','
        assert not bitcoin.international
        assert bitcoin.symbol == '₿'
        assert bitcoin.symbol_ahead
        assert bitcoin.symbol_separator == ''
        assert bitcoin.localized_symbol == '₿'
        assert bitcoin.convertion == ''
        assert bitcoin.__hash__() == hash(
            (bitcoin.__class__, decimal, 'XBT', '0'))
        assert bitcoin.__repr__() == (
            'Bitcoin(amount: -100, '
            'alpha_code: "XBT", '
            'symbol: "₿", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₿", '
            'numeric_code: "0", '
            'decimal_places: "8", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert bitcoin.__str__() == '₿-100.00000000'

    def test_bitcoin_custom(self):
        """test_bitcoin_custom."""
        amount = 1000
        bitcoin = Bitcoin(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert bitcoin.amount == decimal
        assert bitcoin.numeric_code == '0'
        assert bitcoin.alpha_code == 'XBT'
        assert bitcoin.decimal_places == 5
        assert bitcoin.decimal_sign == ','
        assert bitcoin.grouping_places == 2
        assert bitcoin.grouping_sign == '.'
        assert bitcoin.international
        assert bitcoin.symbol == '₿'
        assert not bitcoin.symbol_ahead
        assert bitcoin.symbol_separator == '_'
        assert bitcoin.localized_symbol == '₿'
        assert bitcoin.convertion == ''
        assert bitcoin.__hash__() == hash(
            (bitcoin.__class__, decimal, 'XBT', '0'))
        assert bitcoin.__repr__() == (
            'Bitcoin(amount: 1000, '
            'alpha_code: "XBT", '
            'symbol: "₿", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₿", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert bitcoin.__str__() == 'XBT 10,00.00000'

    def test_bitcoin_changed(self):
        """test_cbitcoin_changed."""
        bitcoin = Bitcoin(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            bitcoin.international = True

    def test_bitcoin_math_add(self):
        """test_bitcoin_math_add."""
        bitcoin_one = Bitcoin(amount=1)
        bitcoin_two = Bitcoin(amount=2)
        bitcoin_three = Bitcoin(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XBT and OTHER.'):
            _ = bitcoin_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Bitcoin\'> '
                    'and <class \'str\'>.')):
            _ = bitcoin_one.__add__('1.00')
        assert (
            bitcoin_one +
            bitcoin_two) == bitcoin_three

    def test_bitcoin_slots(self):
        """test_bitcoin_slots."""
        bitcoin = Bitcoin(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Bitcoin\' '
                    'object has no attribute \'new_variable\'')):
            bitcoin.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Stellar Lumens representation."""

from multicurrency import StellarLumens


class TestStellarLumens:
    """StellarLumens currency tests."""

    def test_stellar_lumens(self):
        """test_stellar_lumens."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        stellar_lumens = StellarLumens(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert stellar_lumens.amount == decimal
        assert stellar_lumens.numeric_code == '0'
        assert stellar_lumens.alpha_code == 'XLM'
        assert stellar_lumens.decimal_places == 7
        assert stellar_lumens.decimal_sign == '.'
        assert stellar_lumens.grouping_places == 3
        assert stellar_lumens.grouping_sign == ','
        assert not stellar_lumens.international
        assert stellar_lumens.symbol == '*'
        assert stellar_lumens.symbol_ahead
        assert stellar_lumens.symbol_separator == ''
        assert stellar_lumens.localized_symbol == '*'
        assert stellar_lumens.convertion == ''
        assert stellar_lumens.__hash__() == hash(
            (stellar_lumens.__class__, decimal, 'XLM', '0'))
        assert stellar_lumens.__repr__() == (
            'StellarLumens(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XLM", '
            'symbol: "*", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "*", '
            'numeric_code: "0", '
            'decimal_places: "7", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert stellar_lumens.__str__() == '*0.1428571'

    def test_stellar_lumens_negative(self):
        """test_stellar_lumens_negative."""
        amount = -100
        stellar_lumens = StellarLumens(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert stellar_lumens.numeric_code == '0'
        assert stellar_lumens.alpha_code == 'XLM'
        assert stellar_lumens.decimal_places == 7
        assert stellar_lumens.decimal_sign == '.'
        assert stellar_lumens.grouping_places == 3
        assert stellar_lumens.grouping_sign == ','
        assert not stellar_lumens.international
        assert stellar_lumens.symbol == '*'
        assert stellar_lumens.symbol_ahead
        assert stellar_lumens.symbol_separator == ''
        assert stellar_lumens.localized_symbol == '*'
        assert stellar_lumens.convertion == ''
        assert stellar_lumens.__hash__() == hash(
            (stellar_lumens.__class__, decimal, 'XLM', '0'))
        assert stellar_lumens.__repr__() == (
            'StellarLumens(amount: -100, '
            'alpha_code: "XLM", '
            'symbol: "*", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "*", '
            'numeric_code: "0", '
            'decimal_places: "7", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert stellar_lumens.__str__() == '*-100.0000000'

    def test_stellar_lumens_custom(self):
        """test_stellar_lumens_custom."""
        amount = 1000
        stellar_lumens = StellarLumens(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert stellar_lumens.amount == decimal
        assert stellar_lumens.numeric_code == '0'
        assert stellar_lumens.alpha_code == 'XLM'
        assert stellar_lumens.decimal_places == 5
        assert stellar_lumens.decimal_sign == ','
        assert stellar_lumens.grouping_places == 2
        assert stellar_lumens.grouping_sign == '.'
        assert stellar_lumens.international
        assert stellar_lumens.symbol == '*'
        assert not stellar_lumens.symbol_ahead
        assert stellar_lumens.symbol_separator == '_'
        assert stellar_lumens.localized_symbol == '*'
        assert stellar_lumens.convertion == ''
        assert stellar_lumens.__hash__() == hash(
            (stellar_lumens.__class__, decimal, 'XLM', '0'))
        assert stellar_lumens.__repr__() == (
            'StellarLumens(amount: 1000, '
            'alpha_code: "XLM", '
            'symbol: "*", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "*", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert stellar_lumens.__str__() == 'XLM 10,00.00000'

    def test_stellar_lumens_changed(self):
        """test_cstellar_lumens_changed."""
        stellar_lumens = StellarLumens(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            stellar_lumens.international = True

    def test_stellar_lumens_math_add(self):
        """test_stellar_lumens_math_add."""
        stellar_lumens_one = StellarLumens(amount=1)
        stellar_lumens_two = StellarLumens(amount=2)
        stellar_lumens_three = StellarLumens(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XLM and OTHER.'):
            _ = stellar_lumens_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.StellarLumens\'> '
                    'and <class \'str\'>.')):
            _ = stellar_lumens_one.__add__('1.00')
        assert (
            stellar_lumens_one +
            stellar_lumens_two) == stellar_lumens_three

    def test_stellar_lumens_slots(self):
        """test_stellar_lumens_slots."""
        stellar_lumens = StellarLumens(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'StellarLumens\' '
                    'object has no attribute \'new_variable\'')):
            stellar_lumens.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Monero representation."""

from multicurrency import Monero


class TestMonero:
    """Monero currency tests."""

    def test_monero(self):
        """test_monero."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        monero = Monero(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert monero.amount == decimal
        assert monero.numeric_code == '0'
        assert monero.alpha_code == 'XMR'
        assert monero.decimal_places == 12
        assert monero.decimal_sign == '.'
        assert monero.grouping_places == 3
        assert monero.grouping_sign == ','
        assert not monero.international
        assert monero.symbol == 'ɱ'
        assert monero.symbol_ahead
        assert monero.symbol_separator == ''
        assert monero.localized_symbol == 'ɱ'
        assert monero.convertion == ''
        assert monero.__hash__() == hash(
            (monero.__class__, decimal, 'XMR', '0'))
        assert monero.__repr__() == (
            'Monero(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XMR", '
            'symbol: "ɱ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ɱ", '
            'numeric_code: "0", '
            'decimal_places: "12", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert monero.__str__() == 'ɱ0.142857142857'

    def test_monero_negative(self):
        """test_monero_negative."""
        amount = -100
        monero = Monero(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert monero.numeric_code == '0'
        assert monero.alpha_code == 'XMR'
        assert monero.decimal_places == 12
        assert monero.decimal_sign == '.'
        assert monero.grouping_places == 3
        assert monero.grouping_sign == ','
        assert not monero.international
        assert monero.symbol == 'ɱ'
        assert monero.symbol_ahead
        assert monero.symbol_separator == ''
        assert monero.localized_symbol == 'ɱ'
        assert monero.convertion == ''
        assert monero.__hash__() == hash(
            (monero.__class__, decimal, 'XMR', '0'))
        assert monero.__repr__() == (
            'Monero(amount: -100, '
            'alpha_code: "XMR", '
            'symbol: "ɱ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ɱ", '
            'numeric_code: "0", '
            'decimal_places: "12", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert monero.__str__() == 'ɱ-100.000000000000'

    def test_monero_custom(self):
        """test_monero_custom."""
        amount = 1000
        monero = Monero(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert monero.amount == decimal
        assert monero.numeric_code == '0'
        assert monero.alpha_code == 'XMR'
        assert monero.decimal_places == 5
        assert monero.decimal_sign == ','
        assert monero.grouping_places == 2
        assert monero.grouping_sign == '.'
        assert monero.international
        assert monero.symbol == 'ɱ'
        assert not monero.symbol_ahead
        assert monero.symbol_separator == '_'
        assert monero.localized_symbol == 'ɱ'
        assert monero.convertion == ''
        assert monero.__hash__() == hash(
            (monero.__class__, decimal, 'XMR', '0'))
        assert monero.__repr__() == (
            'Monero(amount: 1000, '
            'alpha_code: "XMR", '
            'symbol: "ɱ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ɱ", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert monero.__str__() == 'XMR 10,00.00000'

    def test_monero_changed(self):
        """test_cmonero_changed."""
        monero = Monero(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            monero.international = True

    def test_monero_math_add(self):
        """test_monero_math_add."""
        monero_one = Monero(amount=1)
        monero_two = Monero(amount=2)
        monero_three = Monero(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XMR and OTHER.'):
            _ = monero_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Monero\'> '
                    'and <class \'str\'>.')):
            _ = monero_one.__add__('1.00')
        assert (
            monero_one +
            monero_two) == monero_three

    def test_monero_slots(self):
        """test_monero_slots."""
        monero = Monero(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Monero\' '
                    'object has no attribute \'new_variable\'')):
            monero.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Ripple representation."""

from multicurrency import Ripple


class TestRipple:
    """Ripple currency tests."""

    def test_ripple(self):
        """test_ripple."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        ripple = Ripple(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ripple.amount == decimal
        assert ripple.numeric_code == '0'
        assert ripple.alpha_code == 'XRP'
        assert ripple.decimal_places == 6
        assert ripple.decimal_sign == '.'
        assert ripple.grouping_places == 3
        assert ripple.grouping_sign == ','
        assert not ripple.international
        assert ripple.symbol == '✕'
        assert ripple.symbol_ahead
        assert ripple.symbol_separator == ''
        assert ripple.localized_symbol == '✕'
        assert ripple.convertion == ''
        assert ripple.__hash__() == hash(
            (ripple.__class__, decimal, 'XRP', '0'))
        assert ripple.__repr__() == (
            'Ripple(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XRP", '
            'symbol: "✕", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "✕", '
            'numeric_code: "0", '
            'decimal_places: "6", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ripple.__str__() == '✕0.142857'

    def test_ripple_negative(self):
        """test_ripple_negative."""
        amount = -100
        ripple = Ripple(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert ripple.numeric_code == '0'
        assert ripple.alpha_code == 'XRP'
        assert ripple.decimal_places == 6
        assert ripple.decimal_sign == '.'
        assert ripple.grouping_places == 3
        assert ripple.grouping_sign == ','
        assert not ripple.international
        assert ripple.symbol == '✕'
        assert ripple.symbol_ahead
        assert ripple.symbol_separator == ''
        assert ripple.localized_symbol == '✕'
        assert ripple.convertion == ''
        assert ripple.__hash__() == hash(
            (ripple.__class__, decimal, 'XRP', '0'))
        assert ripple.__repr__() == (
            'Ripple(amount: -100, '
            'alpha_code: "XRP", '
            'symbol: "✕", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "✕", '
            'numeric_code: "0", '
            'decimal_places: "6", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert ripple.__str__() == '✕-100.000000'

    def test_ripple_custom(self):
        """test_ripple_custom."""
        amount = 1000
        ripple = Ripple(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert ripple.amount == decimal
        assert ripple.numeric_code == '0'
        assert ripple.alpha_code == 'XRP'
        assert ripple.decimal_places == 5
        assert ripple.decimal_sign == ','
        assert ripple.grouping_places == 2
        assert ripple.grouping_sign == '.'
        assert ripple.international
        assert ripple.symbol == '✕'
        assert not ripple.symbol_ahead
        assert ripple.symbol_separator == '_'
        assert ripple.localized_symbol == '✕'
        assert ripple.convertion == ''
        assert ripple.__hash__() == hash(
            (ripple.__class__, decimal, 'XRP', '0'))
        assert ripple.__repr__() == (
            'Ripple(amount: 1000, '
            'alpha_code: "XRP", '
            'symbol: "✕", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "✕", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert ripple.__str__() == 'XRP 10,00.00000'

    def test_ripple_changed(self):
        """test_cripple_changed."""
        ripple = Ripple(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            ripple.international = True

    def test_ripple_math_add(self):
        """test_ripple_math_add."""
        ripple_one = Ripple(amount=1)
        ripple_two = Ripple(amount=2)
        ripple_three = Ripple(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XRP and OTHER.'):
            _ = ripple_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Ripple\'> '
                    'and <class \'str\'>.')):
            _ = ripple_one.__add__('1.00')
        assert (
            ripple_one +
            ripple_two) == ripple_three

    def test_ripple_slots(self):
        """test_ripple_slots."""
        ripple = Ripple(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Ripple\' '
                    'object has no attribute \'new_variable\'')):
            ripple.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Tezos representation."""

from multicurrency import Tezos


class TestTezos:
    """Tezos currency tests."""

    def test_tezos(self):
        """test_tezos."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        tezos = Tezos(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tezos.amount == decimal
        assert tezos.numeric_code == '0'
        assert tezos.alpha_code == 'XTZ'
        assert tezos.decimal_places == 6
        assert tezos.decimal_sign == '.'
        assert tezos.grouping_places == 3
        assert tezos.grouping_sign == ','
        assert not tezos.international
        assert tezos.symbol == 'ꜩ'
        assert tezos.symbol_ahead
        assert tezos.symbol_separator == ''
        assert tezos.localized_symbol == 'ꜩ'
        assert tezos.convertion == ''
        assert tezos.__hash__() == hash(
            (tezos.__class__, decimal, 'XTZ', '0'))
        assert tezos.__repr__() == (
            'Tezos(amount: 0.1428571428571428571428571429, '
            'alpha_code: "XTZ", '
            'symbol: "ꜩ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ꜩ", '
            'numeric_code: "0", '
            'decimal_places: "6", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tezos.__str__() == 'ꜩ0.142857'

    def test_tezos_negative(self):
        """test_tezos_negative."""
        amount = -100
        tezos = Tezos(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tezos.numeric_code == '0'
        assert tezos.alpha_code == 'XTZ'
        assert tezos.decimal_places == 6
        assert tezos.decimal_sign == '.'
        assert tezos.grouping_places == 3
        assert tezos.grouping_sign == ','
        assert not tezos.international
        assert tezos.symbol == 'ꜩ'
        assert tezos.symbol_ahead
        assert tezos.symbol_separator == ''
        assert tezos.localized_symbol == 'ꜩ'
        assert tezos.convertion == ''
        assert tezos.__hash__() == hash(
            (tezos.__class__, decimal, 'XTZ', '0'))
        assert tezos.__repr__() == (
            'Tezos(amount: -100, '
            'alpha_code: "XTZ", '
            'symbol: "ꜩ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ꜩ", '
            'numeric_code: "0", '
            'decimal_places: "6", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tezos.__str__() == 'ꜩ-100.000000'

    def test_tezos_custom(self):
        """test_tezos_custom."""
        amount = 1000
        tezos = Tezos(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert tezos.amount == decimal
        assert tezos.numeric_code == '0'
        assert tezos.alpha_code == 'XTZ'
        assert tezos.decimal_places == 5
        assert tezos.decimal_sign == ','
        assert tezos.grouping_places == 2
        assert tezos.grouping_sign == '.'
        assert tezos.international
        assert tezos.symbol == 'ꜩ'
        assert not tezos.symbol_ahead
        assert tezos.symbol_separator == '_'
        assert tezos.localized_symbol == 'ꜩ'
        assert tezos.convertion == ''
        assert tezos.__hash__() == hash(
            (tezos.__class__, decimal, 'XTZ', '0'))
        assert tezos.__repr__() == (
            'Tezos(amount: 1000, '
            'alpha_code: "XTZ", '
            'symbol: "ꜩ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ꜩ", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert tezos.__str__() == 'XTZ 10,00.00000'

    def test_tezos_changed(self):
        """test_ctezos_changed."""
        tezos = Tezos(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tezos.international = True

    def test_tezos_math_add(self):
        """test_tezos_math_add."""
        tezos_one = Tezos(amount=1)
        tezos_two = Tezos(amount=2)
        tezos_three = Tezos(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency XTZ and OTHER.'):
            _ = tezos_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Tezos\'> '
                    'and <class \'str\'>.')):
            _ = tezos_one.__add__('1.00')
        assert (
            tezos_one +
            tezos_two) == tezos_three

    def test_tezos_slots(self):
        """test_tezos_slots."""
        tezos = Tezos(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Tezos\' '
                    'object has no attribute \'new_variable\'')):
            tezos.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Zcash representation."""

from multicurrency import Zcash


class TestZcash:
    """Zcash currency tests."""

    def test_zcash(self):
        """test_zcash."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        zcash = Zcash(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zcash.amount == decimal
        assert zcash.numeric_code == '0'
        assert zcash.alpha_code == 'ZEC'
        assert zcash.decimal_places == 8
        assert zcash.decimal_sign == '.'
        assert zcash.grouping_places == 3
        assert zcash.grouping_sign == ','
        assert not zcash.international
        assert zcash.symbol == 'ⓩ'
        assert zcash.symbol_ahead
        assert zcash.symbol_separator == ''
        assert zcash.localized_symbol == 'ⓩ'
        assert zcash.convertion == ''
        assert zcash.__hash__() == hash(
            (zcash.__class__, decimal, 'ZEC', '0'))
        assert zcash.__repr__() == (
            'Zcash(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ZEC", '
            'symbol: "ⓩ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ⓩ", '
            'numeric_code: "0", '
            'decimal_places: "8", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zcash.__str__() == 'ⓩ0.14285714'

    def test_zcash_negative(self):
        """test_zcash_negative."""
        amount = -100
        zcash = Zcash(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert zcash.numeric_code == '0'
        assert zcash.alpha_code == 'ZEC'
        assert zcash.decimal_places == 8
        assert zcash.decimal_sign == '.'
        assert zcash.grouping_places == 3
        assert zcash.grouping_sign == ','
        assert not zcash.international
        assert zcash.symbol == 'ⓩ'
        assert zcash.symbol_ahead
        assert zcash.symbol_separator == ''
        assert zcash.localized_symbol == 'ⓩ'
        assert zcash.convertion == ''
        assert zcash.__hash__() == hash(
            (zcash.__class__, decimal, 'ZEC', '0'))
        assert zcash.__repr__() == (
            'Zcash(amount: -100, '
            'alpha_code: "ZEC", '
            'symbol: "ⓩ", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "ⓩ", '
            'numeric_code: "0", '
            'decimal_places: "8", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert zcash.__str__() == 'ⓩ-100.00000000'

    def test_zcash_custom(self):
        """test_zcash_custom."""
        amount = 1000
        zcash = Zcash(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert zcash.amount == decimal
        assert zcash.numeric_code == '0'
        assert zcash.alpha_code == 'ZEC'
        assert zcash.decimal_places == 5
        assert zcash.decimal_sign == ','
        assert zcash.grouping_places == 2
        assert zcash.grouping_sign == '.'
        assert zcash.international
        assert zcash.symbol == 'ⓩ'
        assert not zcash.symbol_ahead
        assert zcash.symbol_separator == '_'
        assert zcash.localized_symbol == 'ⓩ'
        assert zcash.convertion == ''
        assert zcash.__hash__() == hash(
            (zcash.__class__, decimal, 'ZEC', '0'))
        assert zcash.__repr__() == (
            'Zcash(amount: 1000, '
            'alpha_code: "ZEC", '
            'symbol: "ⓩ", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ⓩ", '
            'numeric_code: "0", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert zcash.__str__() == 'ZEC 10,00.00000'

    def test_zcash_changed(self):
        """test_czcash_changed."""
        zcash = Zcash(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            zcash.international = True

    def test_zcash_math_add(self):
        """test_zcash_math_add."""
        zcash_one = Zcash(amount=1)
        zcash_two = Zcash(amount=2)
        zcash_three = Zcash(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ZEC and OTHER.'):
            _ = zcash_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'crypto.Zcash\'> '
                    'and <class \'str\'>.')):
            _ = zcash_one.__add__('1.00')
        assert (
            zcash_one +
            zcash_two) == zcash_three

    def test_zcash_slots(self):
        """test_zcash_slots."""
        zcash = Zcash(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Zcash\' '
                    'object has no attribute \'new_variable\'')):
            zcash.new_variable = 'fail'  # pylint: disable=assigning-non-slot
