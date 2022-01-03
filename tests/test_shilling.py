# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Shilling currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Kenyan Shilling representation."""

from multicurrency import KenyanShilling


class TestKenyanShilling:
    """KenyanShilling currency tests."""

    def test_kenyan_shilling(self):
        """test_kenyan_shilling."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        kenyan_shilling = KenyanShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kenyan_shilling.amount == decimal
        assert kenyan_shilling.numeric_code == '404'
        assert kenyan_shilling.alpha_code == 'KES'
        assert kenyan_shilling.decimal_places == 2
        assert kenyan_shilling.decimal_sign == '.'
        assert kenyan_shilling.grouping_places == 3
        assert kenyan_shilling.grouping_sign == ','
        assert not kenyan_shilling.international
        assert kenyan_shilling.symbol == 'Ksh'
        assert kenyan_shilling.symbol_ahead
        assert kenyan_shilling.symbol_separator == '\u00A0'
        assert kenyan_shilling.localized_symbol == 'Ksh'
        assert kenyan_shilling.convertion == ''
        assert kenyan_shilling.__hash__() == hash(
            (kenyan_shilling.__class__, decimal, 'KES', '404'))
        assert kenyan_shilling.__repr__() == (
            'KenyanShilling(amount: 0.1428571428571428571428571429, '
            'alpha_code: "KES", '
            'symbol: "Ksh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Ksh", '
            'numeric_code: "404", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert kenyan_shilling.__str__() == 'Ksh 0.14'

    def test_kenyan_shilling_negative(self):
        """test_kenyan_shilling_negative."""
        amount = -100
        kenyan_shilling = KenyanShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert kenyan_shilling.numeric_code == '404'
        assert kenyan_shilling.alpha_code == 'KES'
        assert kenyan_shilling.decimal_places == 2
        assert kenyan_shilling.decimal_sign == '.'
        assert kenyan_shilling.grouping_places == 3
        assert kenyan_shilling.grouping_sign == ','
        assert not kenyan_shilling.international
        assert kenyan_shilling.symbol == 'Ksh'
        assert kenyan_shilling.symbol_ahead
        assert kenyan_shilling.symbol_separator == '\u00A0'
        assert kenyan_shilling.localized_symbol == 'Ksh'
        assert kenyan_shilling.convertion == ''
        assert kenyan_shilling.__hash__() == hash(
            (kenyan_shilling.__class__, decimal, 'KES', '404'))
        assert kenyan_shilling.__repr__() == (
            'KenyanShilling(amount: -100, '
            'alpha_code: "KES", '
            'symbol: "Ksh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "Ksh", '
            'numeric_code: "404", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert kenyan_shilling.__str__() == 'Ksh -100.00'

    def test_kenyan_shilling_custom(self):
        """test_kenyan_shilling_custom."""
        amount = 1000
        kenyan_shilling = KenyanShilling(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert kenyan_shilling.amount == decimal
        assert kenyan_shilling.numeric_code == '404'
        assert kenyan_shilling.alpha_code == 'KES'
        assert kenyan_shilling.decimal_places == 5
        assert kenyan_shilling.decimal_sign == ','
        assert kenyan_shilling.grouping_places == 2
        assert kenyan_shilling.grouping_sign == '.'
        assert kenyan_shilling.international
        assert kenyan_shilling.symbol == 'Ksh'
        assert not kenyan_shilling.symbol_ahead
        assert kenyan_shilling.symbol_separator == '_'
        assert kenyan_shilling.localized_symbol == 'Ksh'
        assert kenyan_shilling.convertion == ''
        assert kenyan_shilling.__hash__() == hash(
            (kenyan_shilling.__class__, decimal, 'KES', '404'))
        assert kenyan_shilling.__repr__() == (
            'KenyanShilling(amount: 1000, '
            'alpha_code: "KES", '
            'symbol: "Ksh", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "Ksh", '
            'numeric_code: "404", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert kenyan_shilling.__str__() == 'KES 10,00.00000'

    def test_kenyan_shilling_changed(self):
        """test_ckenyan_shilling_changed."""
        kenyan_shilling = KenyanShilling(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            kenyan_shilling.international = True

    def test_kenyan_shilling_math_add(self):
        """test_kenyan_shilling_math_add."""
        kenyan_shilling_one = KenyanShilling(amount=1)
        kenyan_shilling_two = KenyanShilling(amount=2)
        kenyan_shilling_three = KenyanShilling(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency KES and OTHER.'):
            _ = kenyan_shilling_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'shilling.KenyanShilling\'> '
                    'and <class \'str\'>.')):
            _ = kenyan_shilling_one.__add__('1.00')
        assert (
            kenyan_shilling_one +
            kenyan_shilling_two) == kenyan_shilling_three

    def test_kenyan_shilling_slots(self):
        """test_kenyan_shilling_slots."""
        kenyan_shilling = KenyanShilling(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'KenyanShilling\' '
                    'object has no attribute \'new_variable\'')):
            kenyan_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Somali Shilling representation."""

from multicurrency import SomaliShilling


class TestSomaliShilling:
    """SomaliShilling currency tests."""

    def test_somali_shilling(self):
        """test_somali_shilling."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        somali_shilling = SomaliShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert somali_shilling.amount == decimal
        assert somali_shilling.numeric_code == '706'
        assert somali_shilling.alpha_code == 'SOS'
        assert somali_shilling.decimal_places == 2
        assert somali_shilling.decimal_sign == '.'
        assert somali_shilling.grouping_places == 3
        assert somali_shilling.grouping_sign == ','
        assert not somali_shilling.international
        assert somali_shilling.symbol == 'SSh'
        assert somali_shilling.symbol_ahead
        assert somali_shilling.symbol_separator == '\u00A0'
        assert somali_shilling.localized_symbol == 'SSh'
        assert somali_shilling.convertion == ''
        assert somali_shilling.__hash__() == hash(
            (somali_shilling.__class__, decimal, 'SOS', '706'))
        assert somali_shilling.__repr__() == (
            'SomaliShilling(amount: 0.1428571428571428571428571429, '
            'alpha_code: "SOS", '
            'symbol: "SSh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SSh", '
            'numeric_code: "706", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert somali_shilling.__str__() == 'SSh 0.14'

    def test_somali_shilling_negative(self):
        """test_somali_shilling_negative."""
        amount = -100
        somali_shilling = SomaliShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert somali_shilling.numeric_code == '706'
        assert somali_shilling.alpha_code == 'SOS'
        assert somali_shilling.decimal_places == 2
        assert somali_shilling.decimal_sign == '.'
        assert somali_shilling.grouping_places == 3
        assert somali_shilling.grouping_sign == ','
        assert not somali_shilling.international
        assert somali_shilling.symbol == 'SSh'
        assert somali_shilling.symbol_ahead
        assert somali_shilling.symbol_separator == '\u00A0'
        assert somali_shilling.localized_symbol == 'SSh'
        assert somali_shilling.convertion == ''
        assert somali_shilling.__hash__() == hash(
            (somali_shilling.__class__, decimal, 'SOS', '706'))
        assert somali_shilling.__repr__() == (
            'SomaliShilling(amount: -100, '
            'alpha_code: "SOS", '
            'symbol: "SSh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SSh", '
            'numeric_code: "706", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert somali_shilling.__str__() == 'SSh -100.00'

    def test_somali_shilling_custom(self):
        """test_somali_shilling_custom."""
        amount = 1000
        somali_shilling = SomaliShilling(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert somali_shilling.amount == decimal
        assert somali_shilling.numeric_code == '706'
        assert somali_shilling.alpha_code == 'SOS'
        assert somali_shilling.decimal_places == 5
        assert somali_shilling.decimal_sign == ','
        assert somali_shilling.grouping_places == 2
        assert somali_shilling.grouping_sign == '.'
        assert somali_shilling.international
        assert somali_shilling.symbol == 'SSh'
        assert not somali_shilling.symbol_ahead
        assert somali_shilling.symbol_separator == '_'
        assert somali_shilling.localized_symbol == 'SSh'
        assert somali_shilling.convertion == ''
        assert somali_shilling.__hash__() == hash(
            (somali_shilling.__class__, decimal, 'SOS', '706'))
        assert somali_shilling.__repr__() == (
            'SomaliShilling(amount: 1000, '
            'alpha_code: "SOS", '
            'symbol: "SSh", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SSh", '
            'numeric_code: "706", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert somali_shilling.__str__() == 'SOS 10,00.00000'

    def test_somali_shilling_changed(self):
        """test_csomali_shilling_changed."""
        somali_shilling = SomaliShilling(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            somali_shilling.international = True

    def test_somali_shilling_math_add(self):
        """test_somali_shilling_math_add."""
        somali_shilling_one = SomaliShilling(amount=1)
        somali_shilling_two = SomaliShilling(amount=2)
        somali_shilling_three = SomaliShilling(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency SOS and OTHER.'):
            _ = somali_shilling_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'shilling.SomaliShilling\'> '
                    'and <class \'str\'>.')):
            _ = somali_shilling_one.__add__('1.00')
        assert (
            somali_shilling_one +
            somali_shilling_two) == somali_shilling_three

    def test_somali_shilling_slots(self):
        """test_somali_shilling_slots."""
        somali_shilling = SomaliShilling(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'SomaliShilling\' '
                    'object has no attribute \'new_variable\'')):
            somali_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Tanzanian Shilling representation."""

from multicurrency import TanzanianShilling


class TestTanzanianShilling:
    """TanzanianShilling currency tests."""

    def test_tanzanian_shilling(self):
        """test_tanzanian_shilling."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        tanzanian_shilling = TanzanianShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tanzanian_shilling.amount == decimal
        assert tanzanian_shilling.numeric_code == '834'
        assert tanzanian_shilling.alpha_code == 'TZS'
        assert tanzanian_shilling.decimal_places == 2
        assert tanzanian_shilling.decimal_sign == '.'
        assert tanzanian_shilling.grouping_places == 3
        assert tanzanian_shilling.grouping_sign == ','
        assert not tanzanian_shilling.international
        assert tanzanian_shilling.symbol == 'TSh'
        assert tanzanian_shilling.symbol_ahead
        assert tanzanian_shilling.symbol_separator == '\u00A0'
        assert tanzanian_shilling.localized_symbol == 'TSh'
        assert tanzanian_shilling.convertion == ''
        assert tanzanian_shilling.__hash__() == hash(
            (tanzanian_shilling.__class__, decimal, 'TZS', '834'))
        assert tanzanian_shilling.__repr__() == (
            'TanzanianShilling(amount: 0.1428571428571428571428571429, '
            'alpha_code: "TZS", '
            'symbol: "TSh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TSh", '
            'numeric_code: "834", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tanzanian_shilling.__str__() == 'TSh 0.14'

    def test_tanzanian_shilling_negative(self):
        """test_tanzanian_shilling_negative."""
        amount = -100
        tanzanian_shilling = TanzanianShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert tanzanian_shilling.numeric_code == '834'
        assert tanzanian_shilling.alpha_code == 'TZS'
        assert tanzanian_shilling.decimal_places == 2
        assert tanzanian_shilling.decimal_sign == '.'
        assert tanzanian_shilling.grouping_places == 3
        assert tanzanian_shilling.grouping_sign == ','
        assert not tanzanian_shilling.international
        assert tanzanian_shilling.symbol == 'TSh'
        assert tanzanian_shilling.symbol_ahead
        assert tanzanian_shilling.symbol_separator == '\u00A0'
        assert tanzanian_shilling.localized_symbol == 'TSh'
        assert tanzanian_shilling.convertion == ''
        assert tanzanian_shilling.__hash__() == hash(
            (tanzanian_shilling.__class__, decimal, 'TZS', '834'))
        assert tanzanian_shilling.__repr__() == (
            'TanzanianShilling(amount: -100, '
            'alpha_code: "TZS", '
            'symbol: "TSh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "TSh", '
            'numeric_code: "834", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert tanzanian_shilling.__str__() == 'TSh -100.00'

    def test_tanzanian_shilling_custom(self):
        """test_tanzanian_shilling_custom."""
        amount = 1000
        tanzanian_shilling = TanzanianShilling(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert tanzanian_shilling.amount == decimal
        assert tanzanian_shilling.numeric_code == '834'
        assert tanzanian_shilling.alpha_code == 'TZS'
        assert tanzanian_shilling.decimal_places == 5
        assert tanzanian_shilling.decimal_sign == ','
        assert tanzanian_shilling.grouping_places == 2
        assert tanzanian_shilling.grouping_sign == '.'
        assert tanzanian_shilling.international
        assert tanzanian_shilling.symbol == 'TSh'
        assert not tanzanian_shilling.symbol_ahead
        assert tanzanian_shilling.symbol_separator == '_'
        assert tanzanian_shilling.localized_symbol == 'TSh'
        assert tanzanian_shilling.convertion == ''
        assert tanzanian_shilling.__hash__() == hash(
            (tanzanian_shilling.__class__, decimal, 'TZS', '834'))
        assert tanzanian_shilling.__repr__() == (
            'TanzanianShilling(amount: 1000, '
            'alpha_code: "TZS", '
            'symbol: "TSh", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "TSh", '
            'numeric_code: "834", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert tanzanian_shilling.__str__() == 'TZS 10,00.00000'

    def test_tanzanian_shilling_changed(self):
        """test_ctanzanian_shilling_changed."""
        tanzanian_shilling = TanzanianShilling(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            tanzanian_shilling.international = True

    def test_tanzanian_shilling_math_add(self):
        """test_tanzanian_shilling_math_add."""
        tanzanian_shilling_one = TanzanianShilling(amount=1)
        tanzanian_shilling_two = TanzanianShilling(amount=2)
        tanzanian_shilling_three = TanzanianShilling(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency TZS and OTHER.'):
            _ = tanzanian_shilling_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'shilling.TanzanianShilling\'> '
                    'and <class \'str\'>.')):
            _ = tanzanian_shilling_one.__add__('1.00')
        assert (
            tanzanian_shilling_one +
            tanzanian_shilling_two) == tanzanian_shilling_three

    def test_tanzanian_shilling_slots(self):
        """test_tanzanian_shilling_slots."""
        tanzanian_shilling = TanzanianShilling(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'TanzanianShilling\' '
                    'object has no attribute \'new_variable\'')):
            tanzanian_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Uganda Shilling representation."""

from multicurrency import UgandaShilling


class TestUgandaShilling:
    """UgandaShilling currency tests."""

    def test_uganda_shilling(self):
        """test_uganda_shilling."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        uganda_shilling = UgandaShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert uganda_shilling.amount == decimal
        assert uganda_shilling.numeric_code == '800'
        assert uganda_shilling.alpha_code == 'UGX'
        assert uganda_shilling.decimal_places == 0
        assert uganda_shilling.decimal_sign == '.'
        assert uganda_shilling.grouping_places == 3
        assert uganda_shilling.grouping_sign == ','
        assert not uganda_shilling.international
        assert uganda_shilling.symbol == 'USh'
        assert uganda_shilling.symbol_ahead
        assert uganda_shilling.symbol_separator == '\u00A0'
        assert uganda_shilling.localized_symbol == 'USh'
        assert uganda_shilling.convertion == ''
        assert uganda_shilling.__hash__() == hash(
            (uganda_shilling.__class__, decimal, 'UGX', '800'))
        assert uganda_shilling.__repr__() == (
            'UgandaShilling(amount: 0.1428571428571428571428571429, '
            'alpha_code: "UGX", '
            'symbol: "USh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "USh", '
            'numeric_code: "800", '
            'decimal_places: "0", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert uganda_shilling.__str__() == 'USh 0'

    def test_uganda_shilling_negative(self):
        """test_uganda_shilling_negative."""
        amount = -100
        uganda_shilling = UgandaShilling(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert uganda_shilling.numeric_code == '800'
        assert uganda_shilling.alpha_code == 'UGX'
        assert uganda_shilling.decimal_places == 0
        assert uganda_shilling.decimal_sign == '.'
        assert uganda_shilling.grouping_places == 3
        assert uganda_shilling.grouping_sign == ','
        assert not uganda_shilling.international
        assert uganda_shilling.symbol == 'USh'
        assert uganda_shilling.symbol_ahead
        assert uganda_shilling.symbol_separator == '\u00A0'
        assert uganda_shilling.localized_symbol == 'USh'
        assert uganda_shilling.convertion == ''
        assert uganda_shilling.__hash__() == hash(
            (uganda_shilling.__class__, decimal, 'UGX', '800'))
        assert uganda_shilling.__repr__() == (
            'UgandaShilling(amount: -100, '
            'alpha_code: "UGX", '
            'symbol: "USh", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "USh", '
            'numeric_code: "800", '
            'decimal_places: "0", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert uganda_shilling.__str__() == 'USh -100'

    def test_uganda_shilling_custom(self):
        """test_uganda_shilling_custom."""
        amount = 1000
        uganda_shilling = UgandaShilling(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert uganda_shilling.amount == decimal
        assert uganda_shilling.numeric_code == '800'
        assert uganda_shilling.alpha_code == 'UGX'
        assert uganda_shilling.decimal_places == 5
        assert uganda_shilling.decimal_sign == ','
        assert uganda_shilling.grouping_places == 2
        assert uganda_shilling.grouping_sign == '.'
        assert uganda_shilling.international
        assert uganda_shilling.symbol == 'USh'
        assert not uganda_shilling.symbol_ahead
        assert uganda_shilling.symbol_separator == '_'
        assert uganda_shilling.localized_symbol == 'USh'
        assert uganda_shilling.convertion == ''
        assert uganda_shilling.__hash__() == hash(
            (uganda_shilling.__class__, decimal, 'UGX', '800'))
        assert uganda_shilling.__repr__() == (
            'UgandaShilling(amount: 1000, '
            'alpha_code: "UGX", '
            'symbol: "USh", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "USh", '
            'numeric_code: "800", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert uganda_shilling.__str__() == 'UGX 10,00.00000'

    def test_uganda_shilling_changed(self):
        """test_cuganda_shilling_changed."""
        uganda_shilling = UgandaShilling(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            uganda_shilling.international = True

    def test_uganda_shilling_math_add(self):
        """test_uganda_shilling_math_add."""
        uganda_shilling_one = UgandaShilling(amount=1)
        uganda_shilling_two = UgandaShilling(amount=2)
        uganda_shilling_three = UgandaShilling(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency UGX and OTHER.'):
            _ = uganda_shilling_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'shilling.UgandaShilling\'> '
                    'and <class \'str\'>.')):
            _ = uganda_shilling_one.__add__('1.00')
        assert (
            uganda_shilling_one +
            uganda_shilling_two) == uganda_shilling_three

    def test_uganda_shilling_slots(self):
        """test_uganda_shilling_slots."""
        uganda_shilling = UgandaShilling(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'UgandaShilling\' '
                    'object has no attribute \'new_variable\'')):
            uganda_shilling.new_variable = 'fail'  # pylint: disable=assigning-non-slot
