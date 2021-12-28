# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Euro currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Euro representation."""

from multicurrency import Euro


class TestEuro:
    """Euro currency tests."""

    def test_euro(self):
        """test_euro."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euro = Euro(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euro.amount == decimal
        assert euro.numeric_code == '978'
        assert euro.alpha_code == 'EUR'
        assert euro.decimal_places == 2
        assert euro.decimal_sign == ','
        assert euro.grouping_places == 3
        assert euro.grouping_sign == '.'
        assert not euro.international
        assert euro.symbol == '€'
        assert not euro.symbol_ahead
        assert euro.symbol_separator == '\u00A0'
        assert euro.localized_symbol == '€'
        assert euro.convertion == ''
        assert euro.__hash__() == hash(
            (euro.__class__, decimal, 'EUR', '978'))
        assert euro.__repr__() == (
            'Euro(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euro.__str__() == '0,14 €'

    def test_euro_negative(self):
        """test_euro_negative."""
        amount = -100
        euro = Euro(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euro.numeric_code == '978'
        assert euro.alpha_code == 'EUR'
        assert euro.decimal_places == 2
        assert euro.decimal_sign == ','
        assert euro.grouping_places == 3
        assert euro.grouping_sign == '.'
        assert not euro.international
        assert euro.symbol == '€'
        assert not euro.symbol_ahead
        assert euro.symbol_separator == '\u00A0'
        assert euro.localized_symbol == '€'
        assert euro.convertion == ''
        assert euro.__hash__() == hash(
            (euro.__class__, decimal, 'EUR', '978'))
        assert euro.__repr__() == (
            'Euro(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euro.__str__() == '-100,00 €'

    def test_euro_custom(self):
        """test_euro_custom."""
        amount = 1000
        euro = Euro(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euro.amount == decimal
        assert euro.numeric_code == '978'
        assert euro.alpha_code == 'EUR'
        assert euro.decimal_places == 5
        assert euro.decimal_sign == '.'
        assert euro.grouping_places == 2
        assert euro.grouping_sign == ','
        assert euro.international
        assert euro.symbol == '€'
        assert not euro.symbol_ahead
        assert euro.symbol_separator == '_'
        assert euro.localized_symbol == '€'
        assert euro.convertion == ''
        assert euro.__hash__() == hash(
            (euro.__class__, decimal, 'EUR', '978'))
        assert euro.__repr__() == (
            'Euro(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euro.__str__() == 'EUR 10,00.00000'

    def test_euro_changed(self):
        """test_ceuro_changed."""
        euro = Euro(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euro.international = True

    def test_euro_math_add(self):
        """test_euro_math_add."""
        euro_one = Euro(amount=1)
        euro_two = Euro(amount=2)
        euro_three = Euro(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euro_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.Euro\'> '
                    'and <class \'str\'>.')):
            _ = euro_one.__add__('1.00')
        assert (
            euro_one +
            euro_two) == euro_three

    def test_euro_slots(self):
        """test_euro_slots."""
        euro = Euro(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Euro\' '
                    'object has no attribute \'new_variable\'')):
            euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroSBA representation."""

from multicurrency import EuroSBA


class TestEuroSBA:
    """EuroSBA currency tests."""

    def test_eurosba(self):
        """test_eurosba."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurosba = EuroSBA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosba.amount == decimal
        assert eurosba.numeric_code == '978'
        assert eurosba.alpha_code == 'EUR'
        assert eurosba.decimal_places == 2
        assert eurosba.decimal_sign == ','
        assert eurosba.grouping_places == 3
        assert eurosba.grouping_sign == '.'
        assert not eurosba.international
        assert eurosba.symbol == '€'
        assert not eurosba.symbol_ahead
        assert eurosba.symbol_separator == '\u00A0'
        assert eurosba.localized_symbol == '€'
        assert eurosba.convertion == ''
        assert eurosba.__hash__() == hash(
            (eurosba.__class__, decimal, 'EUR', '978'))
        assert eurosba.__repr__() == (
            'EuroSBA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosba.__str__() == '0,14 €'

    def test_eurosba_negative(self):
        """test_eurosba_negative."""
        amount = -100
        eurosba = EuroSBA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosba.numeric_code == '978'
        assert eurosba.alpha_code == 'EUR'
        assert eurosba.decimal_places == 2
        assert eurosba.decimal_sign == ','
        assert eurosba.grouping_places == 3
        assert eurosba.grouping_sign == '.'
        assert not eurosba.international
        assert eurosba.symbol == '€'
        assert not eurosba.symbol_ahead
        assert eurosba.symbol_separator == '\u00A0'
        assert eurosba.localized_symbol == '€'
        assert eurosba.convertion == ''
        assert eurosba.__hash__() == hash(
            (eurosba.__class__, decimal, 'EUR', '978'))
        assert eurosba.__repr__() == (
            'EuroSBA(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosba.__str__() == '-100,00 €'

    def test_eurosba_custom(self):
        """test_eurosba_custom."""
        amount = 1000
        eurosba = EuroSBA(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurosba.amount == decimal
        assert eurosba.numeric_code == '978'
        assert eurosba.alpha_code == 'EUR'
        assert eurosba.decimal_places == 5
        assert eurosba.decimal_sign == '.'
        assert eurosba.grouping_places == 2
        assert eurosba.grouping_sign == ','
        assert eurosba.international
        assert eurosba.symbol == '€'
        assert not eurosba.symbol_ahead
        assert eurosba.symbol_separator == '_'
        assert eurosba.localized_symbol == '€'
        assert eurosba.convertion == ''
        assert eurosba.__hash__() == hash(
            (eurosba.__class__, decimal, 'EUR', '978'))
        assert eurosba.__repr__() == (
            'EuroSBA(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurosba.__str__() == 'EUR 10,00.00000'

    def test_eurosba_changed(self):
        """test_ceurosba_changed."""
        eurosba = EuroSBA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosba.international = True

    def test_eurosba_math_add(self):
        """test_eurosba_math_add."""
        eurosba_one = EuroSBA(amount=1)
        eurosba_two = EuroSBA(amount=2)
        eurosba_three = EuroSBA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurosba_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroSBA\'> '
                    'and <class \'str\'>.')):
            _ = eurosba_one.__add__('1.00')
        assert (
            eurosba_one +
            eurosba_two) == eurosba_three

    def test_eurosba_slots(self):
        """test_eurosba_slots."""
        eurosba = EuroSBA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroSBA\' '
                    'object has no attribute \'new_variable\'')):
            eurosba.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroAD representation."""

from multicurrency import EuroAD


class TestEuroAD:
    """EuroAD currency tests."""

    def test_euroad(self):
        """test_euroad."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroad = EuroAD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroad.amount == decimal
        assert euroad.numeric_code == '978'
        assert euroad.alpha_code == 'EUR'
        assert euroad.decimal_places == 2
        assert euroad.decimal_sign == ','
        assert euroad.grouping_places == 3
        assert euroad.grouping_sign == '.'
        assert not euroad.international
        assert euroad.symbol == '€'
        assert not euroad.symbol_ahead
        assert euroad.symbol_separator == '\u00A0'
        assert euroad.localized_symbol == 'AD€'
        assert euroad.convertion == ''
        assert euroad.__hash__() == hash(
            (euroad.__class__, decimal, 'EUR', '978'))
        assert euroad.__repr__() == (
            'EuroAD(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AD€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroad.__str__() == '0,14 €'

    def test_euroad_negative(self):
        """test_euroad_negative."""
        amount = -100
        euroad = EuroAD(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroad.numeric_code == '978'
        assert euroad.alpha_code == 'EUR'
        assert euroad.decimal_places == 2
        assert euroad.decimal_sign == ','
        assert euroad.grouping_places == 3
        assert euroad.grouping_sign == '.'
        assert not euroad.international
        assert euroad.symbol == '€'
        assert not euroad.symbol_ahead
        assert euroad.symbol_separator == '\u00A0'
        assert euroad.localized_symbol == 'AD€'
        assert euroad.convertion == ''
        assert euroad.__hash__() == hash(
            (euroad.__class__, decimal, 'EUR', '978'))
        assert euroad.__repr__() == (
            'EuroAD(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AD€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroad.__str__() == '-100,00 €'

    def test_euroad_custom(self):
        """test_euroad_custom."""
        amount = 1000
        euroad = EuroAD(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroad.amount == decimal
        assert euroad.numeric_code == '978'
        assert euroad.alpha_code == 'EUR'
        assert euroad.decimal_places == 5
        assert euroad.decimal_sign == '.'
        assert euroad.grouping_places == 2
        assert euroad.grouping_sign == ','
        assert euroad.international
        assert euroad.symbol == '€'
        assert not euroad.symbol_ahead
        assert euroad.symbol_separator == '_'
        assert euroad.localized_symbol == 'AD€'
        assert euroad.convertion == ''
        assert euroad.__hash__() == hash(
            (euroad.__class__, decimal, 'EUR', '978'))
        assert euroad.__repr__() == (
            'EuroAD(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AD€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroad.__str__() == 'EUR 10,00.00000'

    def test_euroad_changed(self):
        """test_ceuroad_changed."""
        euroad = EuroAD(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroad.international = True

    def test_euroad_math_add(self):
        """test_euroad_math_add."""
        euroad_one = EuroAD(amount=1)
        euroad_two = EuroAD(amount=2)
        euroad_three = EuroAD(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroad_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroAD\'> '
                    'and <class \'str\'>.')):
            _ = euroad_one.__add__('1.00')
        assert (
            euroad_one +
            euroad_two) == euroad_three

    def test_euroad_slots(self):
        """test_euroad_slots."""
        euroad = EuroAD(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroAD\' '
                    'object has no attribute \'new_variable\'')):
            euroad.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroAT representation."""

from multicurrency import EuroAT


class TestEuroAT:
    """EuroAT currency tests."""

    def test_euroat(self):
        """test_euroat."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroat = EuroAT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroat.amount == decimal
        assert euroat.numeric_code == '978'
        assert euroat.alpha_code == 'EUR'
        assert euroat.decimal_places == 2
        assert euroat.decimal_sign == ','
        assert euroat.grouping_places == 3
        assert euroat.grouping_sign == '.'
        assert not euroat.international
        assert euroat.symbol == '€'
        assert euroat.symbol_ahead
        assert euroat.symbol_separator == '\u00A0'
        assert euroat.localized_symbol == 'AT€'
        assert euroat.convertion == ''
        assert euroat.__hash__() == hash(
            (euroat.__class__, decimal, 'EUR', '978'))
        assert euroat.__repr__() == (
            'EuroAT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroat.__str__() == '€ 0,14'

    def test_euroat_negative(self):
        """test_euroat_negative."""
        amount = -100
        euroat = EuroAT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroat.numeric_code == '978'
        assert euroat.alpha_code == 'EUR'
        assert euroat.decimal_places == 2
        assert euroat.decimal_sign == ','
        assert euroat.grouping_places == 3
        assert euroat.grouping_sign == '.'
        assert not euroat.international
        assert euroat.symbol == '€'
        assert euroat.symbol_ahead
        assert euroat.symbol_separator == '\u00A0'
        assert euroat.localized_symbol == 'AT€'
        assert euroat.convertion == ''
        assert euroat.__hash__() == hash(
            (euroat.__class__, decimal, 'EUR', '978'))
        assert euroat.__repr__() == (
            'EuroAT(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroat.__str__() == '€ -100,00'

    def test_euroat_custom(self):
        """test_euroat_custom."""
        amount = 1000
        euroat = EuroAT(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroat.amount == decimal
        assert euroat.numeric_code == '978'
        assert euroat.alpha_code == 'EUR'
        assert euroat.decimal_places == 5
        assert euroat.decimal_sign == '.'
        assert euroat.grouping_places == 2
        assert euroat.grouping_sign == ','
        assert euroat.international
        assert euroat.symbol == '€'
        assert not euroat.symbol_ahead
        assert euroat.symbol_separator == '_'
        assert euroat.localized_symbol == 'AT€'
        assert euroat.convertion == ''
        assert euroat.__hash__() == hash(
            (euroat.__class__, decimal, 'EUR', '978'))
        assert euroat.__repr__() == (
            'EuroAT(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AT€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroat.__str__() == 'EUR 10,00.00000'

    def test_euroat_changed(self):
        """test_ceuroat_changed."""
        euroat = EuroAT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroat.international = True

    def test_euroat_math_add(self):
        """test_euroat_math_add."""
        euroat_one = EuroAT(amount=1)
        euroat_two = EuroAT(amount=2)
        euroat_three = EuroAT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroat_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroAT\'> '
                    'and <class \'str\'>.')):
            _ = euroat_one.__add__('1.00')
        assert (
            euroat_one +
            euroat_two) == euroat_three

    def test_euroat_slots(self):
        """test_euroat_slots."""
        euroat = EuroAT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroAT\' '
                    'object has no attribute \'new_variable\'')):
            euroat.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroBE representation."""

from multicurrency import EuroBE


class TestEuroBE:
    """EuroBE currency tests."""

    def test_eurobe(self):
        """test_eurobe."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurobe = EuroBE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurobe.amount == decimal
        assert eurobe.numeric_code == '978'
        assert eurobe.alpha_code == 'EUR'
        assert eurobe.decimal_places == 2
        assert eurobe.decimal_sign == ','
        assert eurobe.grouping_places == 3
        assert eurobe.grouping_sign == '.'
        assert not eurobe.international
        assert eurobe.symbol == '€'
        assert eurobe.symbol_ahead
        assert eurobe.symbol_separator == '\u00A0'
        assert eurobe.localized_symbol == 'BE€'
        assert eurobe.convertion == ''
        assert eurobe.__hash__() == hash(
            (eurobe.__class__, decimal, 'EUR', '978'))
        assert eurobe.__repr__() == (
            'EuroBE(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurobe.__str__() == '€ 0,14'

    def test_eurobe_negative(self):
        """test_eurobe_negative."""
        amount = -100
        eurobe = EuroBE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurobe.numeric_code == '978'
        assert eurobe.alpha_code == 'EUR'
        assert eurobe.decimal_places == 2
        assert eurobe.decimal_sign == ','
        assert eurobe.grouping_places == 3
        assert eurobe.grouping_sign == '.'
        assert not eurobe.international
        assert eurobe.symbol == '€'
        assert eurobe.symbol_ahead
        assert eurobe.symbol_separator == '\u00A0'
        assert eurobe.localized_symbol == 'BE€'
        assert eurobe.convertion == ''
        assert eurobe.__hash__() == hash(
            (eurobe.__class__, decimal, 'EUR', '978'))
        assert eurobe.__repr__() == (
            'EuroBE(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "BE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurobe.__str__() == '€ -100,00'

    def test_eurobe_custom(self):
        """test_eurobe_custom."""
        amount = 1000
        eurobe = EuroBE(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurobe.amount == decimal
        assert eurobe.numeric_code == '978'
        assert eurobe.alpha_code == 'EUR'
        assert eurobe.decimal_places == 5
        assert eurobe.decimal_sign == '.'
        assert eurobe.grouping_places == 2
        assert eurobe.grouping_sign == ','
        assert eurobe.international
        assert eurobe.symbol == '€'
        assert not eurobe.symbol_ahead
        assert eurobe.symbol_separator == '_'
        assert eurobe.localized_symbol == 'BE€'
        assert eurobe.convertion == ''
        assert eurobe.__hash__() == hash(
            (eurobe.__class__, decimal, 'EUR', '978'))
        assert eurobe.__repr__() == (
            'EuroBE(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "BE€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurobe.__str__() == 'EUR 10,00.00000'

    def test_eurobe_changed(self):
        """test_ceurobe_changed."""
        eurobe = EuroBE(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurobe.international = True

    def test_eurobe_math_add(self):
        """test_eurobe_math_add."""
        eurobe_one = EuroBE(amount=1)
        eurobe_two = EuroBE(amount=2)
        eurobe_three = EuroBE(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurobe_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroBE\'> '
                    'and <class \'str\'>.')):
            _ = eurobe_one.__add__('1.00')
        assert (
            eurobe_one +
            eurobe_two) == eurobe_three

    def test_eurobe_slots(self):
        """test_eurobe_slots."""
        eurobe = EuroBE(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroBE\' '
                    'object has no attribute \'new_variable\'')):
            eurobe.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroCY representation."""

from multicurrency import EuroCY


class TestEuroCY:
    """EuroCY currency tests."""

    def test_eurocy(self):
        """test_eurocy."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurocy = EuroCY(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurocy.amount == decimal
        assert eurocy.numeric_code == '978'
        assert eurocy.alpha_code == 'EUR'
        assert eurocy.decimal_places == 2
        assert eurocy.decimal_sign == ','
        assert eurocy.grouping_places == 3
        assert eurocy.grouping_sign == '.'
        assert not eurocy.international
        assert eurocy.symbol == '€'
        assert not eurocy.symbol_ahead
        assert eurocy.symbol_separator == '\u00A0'
        assert eurocy.localized_symbol == 'CY€'
        assert eurocy.convertion == ''
        assert eurocy.__hash__() == hash(
            (eurocy.__class__, decimal, 'EUR', '978'))
        assert eurocy.__repr__() == (
            'EuroCY(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CY€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurocy.__str__() == '0,14 €'

    def test_eurocy_negative(self):
        """test_eurocy_negative."""
        amount = -100
        eurocy = EuroCY(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurocy.numeric_code == '978'
        assert eurocy.alpha_code == 'EUR'
        assert eurocy.decimal_places == 2
        assert eurocy.decimal_sign == ','
        assert eurocy.grouping_places == 3
        assert eurocy.grouping_sign == '.'
        assert not eurocy.international
        assert eurocy.symbol == '€'
        assert not eurocy.symbol_ahead
        assert eurocy.symbol_separator == '\u00A0'
        assert eurocy.localized_symbol == 'CY€'
        assert eurocy.convertion == ''
        assert eurocy.__hash__() == hash(
            (eurocy.__class__, decimal, 'EUR', '978'))
        assert eurocy.__repr__() == (
            'EuroCY(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CY€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurocy.__str__() == '-100,00 €'

    def test_eurocy_custom(self):
        """test_eurocy_custom."""
        amount = 1000
        eurocy = EuroCY(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurocy.amount == decimal
        assert eurocy.numeric_code == '978'
        assert eurocy.alpha_code == 'EUR'
        assert eurocy.decimal_places == 5
        assert eurocy.decimal_sign == '.'
        assert eurocy.grouping_places == 2
        assert eurocy.grouping_sign == ','
        assert eurocy.international
        assert eurocy.symbol == '€'
        assert not eurocy.symbol_ahead
        assert eurocy.symbol_separator == '_'
        assert eurocy.localized_symbol == 'CY€'
        assert eurocy.convertion == ''
        assert eurocy.__hash__() == hash(
            (eurocy.__class__, decimal, 'EUR', '978'))
        assert eurocy.__repr__() == (
            'EuroCY(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CY€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurocy.__str__() == 'EUR 10,00.00000'

    def test_eurocy_changed(self):
        """test_ceurocy_changed."""
        eurocy = EuroCY(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurocy.international = True

    def test_eurocy_math_add(self):
        """test_eurocy_math_add."""
        eurocy_one = EuroCY(amount=1)
        eurocy_two = EuroCY(amount=2)
        eurocy_three = EuroCY(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurocy_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroCY\'> '
                    'and <class \'str\'>.')):
            _ = eurocy_one.__add__('1.00')
        assert (
            eurocy_one +
            eurocy_two) == eurocy_three

    def test_eurocy_slots(self):
        """test_eurocy_slots."""
        eurocy = EuroCY(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroCY\' '
                    'object has no attribute \'new_variable\'')):
            eurocy.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroEE representation."""

from multicurrency import EuroEE


class TestEuroEE:
    """EuroEE currency tests."""

    def test_euroee(self):
        """test_euroee."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroee = EuroEE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroee.amount == decimal
        assert euroee.numeric_code == '978'
        assert euroee.alpha_code == 'EUR'
        assert euroee.decimal_places == 2
        assert euroee.decimal_sign == ','
        assert euroee.grouping_places == 3
        assert euroee.grouping_sign == '\u202F'
        assert not euroee.international
        assert euroee.symbol == '€'
        assert not euroee.symbol_ahead
        assert euroee.symbol_separator == '\u00A0'
        assert euroee.localized_symbol == 'EE€'
        assert euroee.convertion == ''
        assert euroee.__hash__() == hash(
            (euroee.__class__, decimal, 'EUR', '978'))
        assert euroee.__repr__() == (
            'EuroEE(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "EE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euroee.__str__() == '0,14 €'

    def test_euroee_negative(self):
        """test_euroee_negative."""
        amount = -100
        euroee = EuroEE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroee.numeric_code == '978'
        assert euroee.alpha_code == 'EUR'
        assert euroee.decimal_places == 2
        assert euroee.decimal_sign == ','
        assert euroee.grouping_places == 3
        assert euroee.grouping_sign == '\u202F'
        assert not euroee.international
        assert euroee.symbol == '€'
        assert not euroee.symbol_ahead
        assert euroee.symbol_separator == '\u00A0'
        assert euroee.localized_symbol == 'EE€'
        assert euroee.convertion == ''
        assert euroee.__hash__() == hash(
            (euroee.__class__, decimal, 'EUR', '978'))
        assert euroee.__repr__() == (
            'EuroEE(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "EE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euroee.__str__() == '-100,00 €'

    def test_euroee_custom(self):
        """test_euroee_custom."""
        amount = 1000
        euroee = EuroEE(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroee.amount == decimal
        assert euroee.numeric_code == '978'
        assert euroee.alpha_code == 'EUR'
        assert euroee.decimal_places == 5
        assert euroee.decimal_sign == '\u202F'
        assert euroee.grouping_places == 2
        assert euroee.grouping_sign == ','
        assert euroee.international
        assert euroee.symbol == '€'
        assert not euroee.symbol_ahead
        assert euroee.symbol_separator == '_'
        assert euroee.localized_symbol == 'EE€'
        assert euroee.convertion == ''
        assert euroee.__hash__() == hash(
            (euroee.__class__, decimal, 'EUR', '978'))
        assert euroee.__repr__() == (
            'EuroEE(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "EE€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroee.__str__() == 'EUR 10,00.00000'

    def test_euroee_changed(self):
        """test_ceuroee_changed."""
        euroee = EuroEE(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroee.international = True

    def test_euroee_math_add(self):
        """test_euroee_math_add."""
        euroee_one = EuroEE(amount=1)
        euroee_two = EuroEE(amount=2)
        euroee_three = EuroEE(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroee_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroEE\'> '
                    'and <class \'str\'>.')):
            _ = euroee_one.__add__('1.00')
        assert (
            euroee_one +
            euroee_two) == euroee_three

    def test_euroee_slots(self):
        """test_euroee_slots."""
        euroee = EuroEE(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroEE\' '
                    'object has no attribute \'new_variable\'')):
            euroee.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroFI representation."""

from multicurrency import EuroFI


class TestEuroFI:
    """EuroFI currency tests."""

    def test_eurofi(self):
        """test_eurofi."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurofi = EuroFI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurofi.amount == decimal
        assert eurofi.numeric_code == '978'
        assert eurofi.alpha_code == 'EUR'
        assert eurofi.decimal_places == 2
        assert eurofi.decimal_sign == ','
        assert eurofi.grouping_places == 3
        assert eurofi.grouping_sign == '\u202F'
        assert not eurofi.international
        assert eurofi.symbol == '€'
        assert not eurofi.symbol_ahead
        assert eurofi.symbol_separator == '\u00A0'
        assert eurofi.localized_symbol == 'FI€'
        assert eurofi.convertion == ''
        assert eurofi.__hash__() == hash(
            (eurofi.__class__, decimal, 'EUR', '978'))
        assert eurofi.__repr__() == (
            'EuroFI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "FI€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurofi.__str__() == '0,14 €'

    def test_eurofi_negative(self):
        """test_eurofi_negative."""
        amount = -100
        eurofi = EuroFI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurofi.numeric_code == '978'
        assert eurofi.alpha_code == 'EUR'
        assert eurofi.decimal_places == 2
        assert eurofi.decimal_sign == ','
        assert eurofi.grouping_places == 3
        assert eurofi.grouping_sign == '\u202F'
        assert not eurofi.international
        assert eurofi.symbol == '€'
        assert not eurofi.symbol_ahead
        assert eurofi.symbol_separator == '\u00A0'
        assert eurofi.localized_symbol == 'FI€'
        assert eurofi.convertion == ''
        assert eurofi.__hash__() == hash(
            (eurofi.__class__, decimal, 'EUR', '978'))
        assert eurofi.__repr__() == (
            'EuroFI(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "FI€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurofi.__str__() == '-100,00 €'

    def test_eurofi_custom(self):
        """test_eurofi_custom."""
        amount = 1000
        eurofi = EuroFI(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurofi.amount == decimal
        assert eurofi.numeric_code == '978'
        assert eurofi.alpha_code == 'EUR'
        assert eurofi.decimal_places == 5
        assert eurofi.decimal_sign == '\u202F'
        assert eurofi.grouping_places == 2
        assert eurofi.grouping_sign == ','
        assert eurofi.international
        assert eurofi.symbol == '€'
        assert not eurofi.symbol_ahead
        assert eurofi.symbol_separator == '_'
        assert eurofi.localized_symbol == 'FI€'
        assert eurofi.convertion == ''
        assert eurofi.__hash__() == hash(
            (eurofi.__class__, decimal, 'EUR', '978'))
        assert eurofi.__repr__() == (
            'EuroFI(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "FI€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurofi.__str__() == 'EUR 10,00.00000'

    def test_eurofi_changed(self):
        """test_ceurofi_changed."""
        eurofi = EuroFI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofi.international = True

    def test_eurofi_math_add(self):
        """test_eurofi_math_add."""
        eurofi_one = EuroFI(amount=1)
        eurofi_two = EuroFI(amount=2)
        eurofi_three = EuroFI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurofi_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroFI\'> '
                    'and <class \'str\'>.')):
            _ = eurofi_one.__add__('1.00')
        assert (
            eurofi_one +
            eurofi_two) == eurofi_three

    def test_eurofi_slots(self):
        """test_eurofi_slots."""
        eurofi = EuroFI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroFI\' '
                    'object has no attribute \'new_variable\'')):
            eurofi.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroFR representation."""

from multicurrency import EuroFR


class TestEuroFR:
    """EuroFR currency tests."""

    def test_eurofr(self):
        """test_eurofr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurofr = EuroFR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurofr.amount == decimal
        assert eurofr.numeric_code == '978'
        assert eurofr.alpha_code == 'EUR'
        assert eurofr.decimal_places == 2
        assert eurofr.decimal_sign == ','
        assert eurofr.grouping_places == 3
        assert eurofr.grouping_sign == '\u202F'
        assert not eurofr.international
        assert eurofr.symbol == '€'
        assert not eurofr.symbol_ahead
        assert eurofr.symbol_separator == '\u00A0'
        assert eurofr.localized_symbol == 'FR€'
        assert eurofr.convertion == ''
        assert eurofr.__hash__() == hash(
            (eurofr.__class__, decimal, 'EUR', '978'))
        assert eurofr.__repr__() == (
            'EuroFR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "FR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurofr.__str__() == '0,14 €'

    def test_eurofr_negative(self):
        """test_eurofr_negative."""
        amount = -100
        eurofr = EuroFR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurofr.numeric_code == '978'
        assert eurofr.alpha_code == 'EUR'
        assert eurofr.decimal_places == 2
        assert eurofr.decimal_sign == ','
        assert eurofr.grouping_places == 3
        assert eurofr.grouping_sign == '\u202F'
        assert not eurofr.international
        assert eurofr.symbol == '€'
        assert not eurofr.symbol_ahead
        assert eurofr.symbol_separator == '\u00A0'
        assert eurofr.localized_symbol == 'FR€'
        assert eurofr.convertion == ''
        assert eurofr.__hash__() == hash(
            (eurofr.__class__, decimal, 'EUR', '978'))
        assert eurofr.__repr__() == (
            'EuroFR(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "FR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurofr.__str__() == '-100,00 €'

    def test_eurofr_custom(self):
        """test_eurofr_custom."""
        amount = 1000
        eurofr = EuroFR(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurofr.amount == decimal
        assert eurofr.numeric_code == '978'
        assert eurofr.alpha_code == 'EUR'
        assert eurofr.decimal_places == 5
        assert eurofr.decimal_sign == '\u202F'
        assert eurofr.grouping_places == 2
        assert eurofr.grouping_sign == ','
        assert eurofr.international
        assert eurofr.symbol == '€'
        assert not eurofr.symbol_ahead
        assert eurofr.symbol_separator == '_'
        assert eurofr.localized_symbol == 'FR€'
        assert eurofr.convertion == ''
        assert eurofr.__hash__() == hash(
            (eurofr.__class__, decimal, 'EUR', '978'))
        assert eurofr.__repr__() == (
            'EuroFR(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "FR€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurofr.__str__() == 'EUR 10,00.00000'

    def test_eurofr_changed(self):
        """test_ceurofr_changed."""
        eurofr = EuroFR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurofr.international = True

    def test_eurofr_math_add(self):
        """test_eurofr_math_add."""
        eurofr_one = EuroFR(amount=1)
        eurofr_two = EuroFR(amount=2)
        eurofr_three = EuroFR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurofr_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroFR\'> '
                    'and <class \'str\'>.')):
            _ = eurofr_one.__add__('1.00')
        assert (
            eurofr_one +
            eurofr_two) == eurofr_three

    def test_eurofr_slots(self):
        """test_eurofr_slots."""
        eurofr = EuroFR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroFR\' '
                    'object has no attribute \'new_variable\'')):
            eurofr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroDE representation."""

from multicurrency import EuroDE


class TestEuroDE:
    """EuroDE currency tests."""

    def test_eurode(self):
        """test_eurode."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurode = EuroDE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurode.amount == decimal
        assert eurode.numeric_code == '978'
        assert eurode.alpha_code == 'EUR'
        assert eurode.decimal_places == 2
        assert eurode.decimal_sign == ','
        assert eurode.grouping_places == 3
        assert eurode.grouping_sign == '.'
        assert not eurode.international
        assert eurode.symbol == '€'
        assert not eurode.symbol_ahead
        assert eurode.symbol_separator == '\u00A0'
        assert eurode.localized_symbol == 'DE€'
        assert eurode.convertion == ''
        assert eurode.__hash__() == hash(
            (eurode.__class__, decimal, 'EUR', '978'))
        assert eurode.__repr__() == (
            'EuroDE(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "DE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurode.__str__() == '0,14 €'

    def test_eurode_negative(self):
        """test_eurode_negative."""
        amount = -100
        eurode = EuroDE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurode.numeric_code == '978'
        assert eurode.alpha_code == 'EUR'
        assert eurode.decimal_places == 2
        assert eurode.decimal_sign == ','
        assert eurode.grouping_places == 3
        assert eurode.grouping_sign == '.'
        assert not eurode.international
        assert eurode.symbol == '€'
        assert not eurode.symbol_ahead
        assert eurode.symbol_separator == '\u00A0'
        assert eurode.localized_symbol == 'DE€'
        assert eurode.convertion == ''
        assert eurode.__hash__() == hash(
            (eurode.__class__, decimal, 'EUR', '978'))
        assert eurode.__repr__() == (
            'EuroDE(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "DE€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurode.__str__() == '-100,00 €'

    def test_eurode_custom(self):
        """test_eurode_custom."""
        amount = 1000
        eurode = EuroDE(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurode.amount == decimal
        assert eurode.numeric_code == '978'
        assert eurode.alpha_code == 'EUR'
        assert eurode.decimal_places == 5
        assert eurode.decimal_sign == '.'
        assert eurode.grouping_places == 2
        assert eurode.grouping_sign == ','
        assert eurode.international
        assert eurode.symbol == '€'
        assert not eurode.symbol_ahead
        assert eurode.symbol_separator == '_'
        assert eurode.localized_symbol == 'DE€'
        assert eurode.convertion == ''
        assert eurode.__hash__() == hash(
            (eurode.__class__, decimal, 'EUR', '978'))
        assert eurode.__repr__() == (
            'EuroDE(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "DE€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurode.__str__() == 'EUR 10,00.00000'

    def test_eurode_changed(self):
        """test_ceurode_changed."""
        eurode = EuroDE(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurode.international = True

    def test_eurode_math_add(self):
        """test_eurode_math_add."""
        eurode_one = EuroDE(amount=1)
        eurode_two = EuroDE(amount=2)
        eurode_three = EuroDE(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurode_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroDE\'> '
                    'and <class \'str\'>.')):
            _ = eurode_one.__add__('1.00')
        assert (
            eurode_one +
            eurode_two) == eurode_three

    def test_eurode_slots(self):
        """test_eurode_slots."""
        eurode = EuroDE(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroDE\' '
                    'object has no attribute \'new_variable\'')):
            eurode.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroGR representation."""

from multicurrency import EuroGR


class TestEuroGR:
    """EuroGR currency tests."""

    def test_eurogr(self):
        """test_eurogr."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurogr = EuroGR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurogr.amount == decimal
        assert eurogr.numeric_code == '978'
        assert eurogr.alpha_code == 'EUR'
        assert eurogr.decimal_places == 2
        assert eurogr.decimal_sign == ','
        assert eurogr.grouping_places == 3
        assert eurogr.grouping_sign == '.'
        assert not eurogr.international
        assert eurogr.symbol == '€'
        assert not eurogr.symbol_ahead
        assert eurogr.symbol_separator == '\u00A0'
        assert eurogr.localized_symbol == 'GR€'
        assert eurogr.convertion == ''
        assert eurogr.__hash__() == hash(
            (eurogr.__class__, decimal, 'EUR', '978'))
        assert eurogr.__repr__() == (
            'EuroGR(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurogr.__str__() == '0,14 €'

    def test_eurogr_negative(self):
        """test_eurogr_negative."""
        amount = -100
        eurogr = EuroGR(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurogr.numeric_code == '978'
        assert eurogr.alpha_code == 'EUR'
        assert eurogr.decimal_places == 2
        assert eurogr.decimal_sign == ','
        assert eurogr.grouping_places == 3
        assert eurogr.grouping_sign == '.'
        assert not eurogr.international
        assert eurogr.symbol == '€'
        assert not eurogr.symbol_ahead
        assert eurogr.symbol_separator == '\u00A0'
        assert eurogr.localized_symbol == 'GR€'
        assert eurogr.convertion == ''
        assert eurogr.__hash__() == hash(
            (eurogr.__class__, decimal, 'EUR', '978'))
        assert eurogr.__repr__() == (
            'EuroGR(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "GR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurogr.__str__() == '-100,00 €'

    def test_eurogr_custom(self):
        """test_eurogr_custom."""
        amount = 1000
        eurogr = EuroGR(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurogr.amount == decimal
        assert eurogr.numeric_code == '978'
        assert eurogr.alpha_code == 'EUR'
        assert eurogr.decimal_places == 5
        assert eurogr.decimal_sign == '.'
        assert eurogr.grouping_places == 2
        assert eurogr.grouping_sign == ','
        assert eurogr.international
        assert eurogr.symbol == '€'
        assert not eurogr.symbol_ahead
        assert eurogr.symbol_separator == '_'
        assert eurogr.localized_symbol == 'GR€'
        assert eurogr.convertion == ''
        assert eurogr.__hash__() == hash(
            (eurogr.__class__, decimal, 'EUR', '978'))
        assert eurogr.__repr__() == (
            'EuroGR(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "GR€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurogr.__str__() == 'EUR 10,00.00000'

    def test_eurogr_changed(self):
        """test_ceurogr_changed."""
        eurogr = EuroGR(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurogr.international = True

    def test_eurogr_math_add(self):
        """test_eurogr_math_add."""
        eurogr_one = EuroGR(amount=1)
        eurogr_two = EuroGR(amount=2)
        eurogr_three = EuroGR(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurogr_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroGR\'> '
                    'and <class \'str\'>.')):
            _ = eurogr_one.__add__('1.00')
        assert (
            eurogr_one +
            eurogr_two) == eurogr_three

    def test_eurogr_slots(self):
        """test_eurogr_slots."""
        eurogr = EuroGR(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroGR\' '
                    'object has no attribute \'new_variable\'')):
            eurogr.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroIE representation."""

from multicurrency import EuroIE


class TestEuroIE:
    """EuroIE currency tests."""

    def test_euroie(self):
        """test_euroie."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroie = EuroIE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroie.amount == decimal
        assert euroie.numeric_code == '978'
        assert euroie.alpha_code == 'EUR'
        assert euroie.decimal_places == 2
        assert euroie.decimal_sign == '.'
        assert euroie.grouping_places == 3
        assert euroie.grouping_sign == ','
        assert not euroie.international
        assert euroie.symbol == '€'
        assert euroie.symbol_ahead
        assert euroie.symbol_separator == ''
        assert euroie.localized_symbol == 'IR€'
        assert euroie.convertion == ''
        assert euroie.__hash__() == hash(
            (euroie.__class__, decimal, 'EUR', '978'))
        assert euroie.__repr__() == (
            'EuroIE(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert euroie.__str__() == '€0.14'

    def test_euroie_negative(self):
        """test_euroie_negative."""
        amount = -100
        euroie = EuroIE(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroie.numeric_code == '978'
        assert euroie.alpha_code == 'EUR'
        assert euroie.decimal_places == 2
        assert euroie.decimal_sign == '.'
        assert euroie.grouping_places == 3
        assert euroie.grouping_sign == ','
        assert not euroie.international
        assert euroie.symbol == '€'
        assert euroie.symbol_ahead
        assert euroie.symbol_separator == ''
        assert euroie.localized_symbol == 'IR€'
        assert euroie.convertion == ''
        assert euroie.__hash__() == hash(
            (euroie.__class__, decimal, 'EUR', '978'))
        assert euroie.__repr__() == (
            'EuroIE(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "IR€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert euroie.__str__() == '€-100.00'

    def test_euroie_custom(self):
        """test_euroie_custom."""
        amount = 1000
        euroie = EuroIE(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroie.amount == decimal
        assert euroie.numeric_code == '978'
        assert euroie.alpha_code == 'EUR'
        assert euroie.decimal_places == 5
        assert euroie.decimal_sign == ','
        assert euroie.grouping_places == 2
        assert euroie.grouping_sign == '.'
        assert euroie.international
        assert euroie.symbol == '€'
        assert not euroie.symbol_ahead
        assert euroie.symbol_separator == '_'
        assert euroie.localized_symbol == 'IR€'
        assert euroie.convertion == ''
        assert euroie.__hash__() == hash(
            (euroie.__class__, decimal, 'EUR', '978'))
        assert euroie.__repr__() == (
            'EuroIE(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IR€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert euroie.__str__() == 'EUR 10,00.00000'

    def test_euroie_changed(self):
        """test_ceuroie_changed."""
        euroie = EuroIE(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroie.international = True

    def test_euroie_math_add(self):
        """test_euroie_math_add."""
        euroie_one = EuroIE(amount=1)
        euroie_two = EuroIE(amount=2)
        euroie_three = EuroIE(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroie_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroIE\'> '
                    'and <class \'str\'>.')):
            _ = euroie_one.__add__('1.00')
        assert (
            euroie_one +
            euroie_two) == euroie_three

    def test_euroie_slots(self):
        """test_euroie_slots."""
        euroie = EuroIE(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroIE\' '
                    'object has no attribute \'new_variable\'')):
            euroie.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroIT representation."""

from multicurrency import EuroIT


class TestEuroIT:
    """EuroIT currency tests."""

    def test_euroit(self):
        """test_euroit."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroit = EuroIT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroit.amount == decimal
        assert euroit.numeric_code == '978'
        assert euroit.alpha_code == 'EUR'
        assert euroit.decimal_places == 2
        assert euroit.decimal_sign == ','
        assert euroit.grouping_places == 3
        assert euroit.grouping_sign == '.'
        assert not euroit.international
        assert euroit.symbol == '€'
        assert not euroit.symbol_ahead
        assert euroit.symbol_separator == '\u00A0'
        assert euroit.localized_symbol == 'IT€'
        assert euroit.convertion == ''
        assert euroit.__hash__() == hash(
            (euroit.__class__, decimal, 'EUR', '978'))
        assert euroit.__repr__() == (
            'EuroIT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "IT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroit.__str__() == '0,14 €'

    def test_euroit_negative(self):
        """test_euroit_negative."""
        amount = -100
        euroit = EuroIT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroit.numeric_code == '978'
        assert euroit.alpha_code == 'EUR'
        assert euroit.decimal_places == 2
        assert euroit.decimal_sign == ','
        assert euroit.grouping_places == 3
        assert euroit.grouping_sign == '.'
        assert not euroit.international
        assert euroit.symbol == '€'
        assert not euroit.symbol_ahead
        assert euroit.symbol_separator == '\u00A0'
        assert euroit.localized_symbol == 'IT€'
        assert euroit.convertion == ''
        assert euroit.__hash__() == hash(
            (euroit.__class__, decimal, 'EUR', '978'))
        assert euroit.__repr__() == (
            'EuroIT(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "IT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroit.__str__() == '-100,00 €'

    def test_euroit_custom(self):
        """test_euroit_custom."""
        amount = 1000
        euroit = EuroIT(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroit.amount == decimal
        assert euroit.numeric_code == '978'
        assert euroit.alpha_code == 'EUR'
        assert euroit.decimal_places == 5
        assert euroit.decimal_sign == '.'
        assert euroit.grouping_places == 2
        assert euroit.grouping_sign == ','
        assert euroit.international
        assert euroit.symbol == '€'
        assert not euroit.symbol_ahead
        assert euroit.symbol_separator == '_'
        assert euroit.localized_symbol == 'IT€'
        assert euroit.convertion == ''
        assert euroit.__hash__() == hash(
            (euroit.__class__, decimal, 'EUR', '978'))
        assert euroit.__repr__() == (
            'EuroIT(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "IT€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroit.__str__() == 'EUR 10,00.00000'

    def test_euroit_changed(self):
        """test_ceuroit_changed."""
        euroit = EuroIT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroit.international = True

    def test_euroit_math_add(self):
        """test_euroit_math_add."""
        euroit_one = EuroIT(amount=1)
        euroit_two = EuroIT(amount=2)
        euroit_three = EuroIT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroit_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroIT\'> '
                    'and <class \'str\'>.')):
            _ = euroit_one.__add__('1.00')
        assert (
            euroit_one +
            euroit_two) == euroit_three

    def test_euroit_slots(self):
        """test_euroit_slots."""
        euroit = EuroIT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroIT\' '
                    'object has no attribute \'new_variable\'')):
            euroit.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroXK representation."""

from multicurrency import EuroXK


class TestEuroXK:
    """EuroXK currency tests."""

    def test_euroxk(self):
        """test_euroxk."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroxk = EuroXK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroxk.amount == decimal
        assert euroxk.numeric_code == '978'
        assert euroxk.alpha_code == 'EUR'
        assert euroxk.decimal_places == 2
        assert euroxk.decimal_sign == ','
        assert euroxk.grouping_places == 3
        assert euroxk.grouping_sign == '\u202F'
        assert not euroxk.international
        assert euroxk.symbol == '€'
        assert not euroxk.symbol_ahead
        assert euroxk.symbol_separator == '\u00A0'
        assert euroxk.localized_symbol == 'XK€'
        assert euroxk.convertion == ''
        assert euroxk.__hash__() == hash(
            (euroxk.__class__, decimal, 'EUR', '978'))
        assert euroxk.__repr__() == (
            'EuroXK(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "XK€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euroxk.__str__() == '0,14 €'

    def test_euroxk_negative(self):
        """test_euroxk_negative."""
        amount = -100
        euroxk = EuroXK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroxk.numeric_code == '978'
        assert euroxk.alpha_code == 'EUR'
        assert euroxk.decimal_places == 2
        assert euroxk.decimal_sign == ','
        assert euroxk.grouping_places == 3
        assert euroxk.grouping_sign == '\u202F'
        assert not euroxk.international
        assert euroxk.symbol == '€'
        assert not euroxk.symbol_ahead
        assert euroxk.symbol_separator == '\u00A0'
        assert euroxk.localized_symbol == 'XK€'
        assert euroxk.convertion == ''
        assert euroxk.__hash__() == hash(
            (euroxk.__class__, decimal, 'EUR', '978'))
        assert euroxk.__repr__() == (
            'EuroXK(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "XK€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euroxk.__str__() == '-100,00 €'

    def test_euroxk_custom(self):
        """test_euroxk_custom."""
        amount = 1000
        euroxk = EuroXK(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroxk.amount == decimal
        assert euroxk.numeric_code == '978'
        assert euroxk.alpha_code == 'EUR'
        assert euroxk.decimal_places == 5
        assert euroxk.decimal_sign == '\u202F'
        assert euroxk.grouping_places == 2
        assert euroxk.grouping_sign == ','
        assert euroxk.international
        assert euroxk.symbol == '€'
        assert not euroxk.symbol_ahead
        assert euroxk.symbol_separator == '_'
        assert euroxk.localized_symbol == 'XK€'
        assert euroxk.convertion == ''
        assert euroxk.__hash__() == hash(
            (euroxk.__class__, decimal, 'EUR', '978'))
        assert euroxk.__repr__() == (
            'EuroXK(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "XK€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroxk.__str__() == 'EUR 10,00.00000'

    def test_euroxk_changed(self):
        """test_ceuroxk_changed."""
        euroxk = EuroXK(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroxk.international = True

    def test_euroxk_math_add(self):
        """test_euroxk_math_add."""
        euroxk_one = EuroXK(amount=1)
        euroxk_two = EuroXK(amount=2)
        euroxk_three = EuroXK(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroxk_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroXK\'> '
                    'and <class \'str\'>.')):
            _ = euroxk_one.__add__('1.00')
        assert (
            euroxk_one +
            euroxk_two) == euroxk_three

    def test_euroxk_slots(self):
        """test_euroxk_slots."""
        euroxk = EuroXK(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroXK\' '
                    'object has no attribute \'new_variable\'')):
            euroxk.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroLV representation."""

from multicurrency import EuroLV


class TestEuroLV:
    """EuroLV currency tests."""

    def test_eurolv(self):
        """test_eurolv."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurolv = EuroLV(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolv.amount == decimal
        assert eurolv.numeric_code == '978'
        assert eurolv.alpha_code == 'EUR'
        assert eurolv.decimal_places == 2
        assert eurolv.decimal_sign == ','
        assert eurolv.grouping_places == 3
        assert eurolv.grouping_sign == '\u202F'
        assert not eurolv.international
        assert eurolv.symbol == '€'
        assert not eurolv.symbol_ahead
        assert eurolv.symbol_separator == '\u00A0'
        assert eurolv.localized_symbol == 'LV€'
        assert eurolv.convertion == ''
        assert eurolv.__hash__() == hash(
            (eurolv.__class__, decimal, 'EUR', '978'))
        assert eurolv.__repr__() == (
            'EuroLV(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LV€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurolv.__str__() == '0,14 €'

    def test_eurolv_negative(self):
        """test_eurolv_negative."""
        amount = -100
        eurolv = EuroLV(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolv.numeric_code == '978'
        assert eurolv.alpha_code == 'EUR'
        assert eurolv.decimal_places == 2
        assert eurolv.decimal_sign == ','
        assert eurolv.grouping_places == 3
        assert eurolv.grouping_sign == '\u202F'
        assert not eurolv.international
        assert eurolv.symbol == '€'
        assert not eurolv.symbol_ahead
        assert eurolv.symbol_separator == '\u00A0'
        assert eurolv.localized_symbol == 'LV€'
        assert eurolv.convertion == ''
        assert eurolv.__hash__() == hash(
            (eurolv.__class__, decimal, 'EUR', '978'))
        assert eurolv.__repr__() == (
            'EuroLV(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LV€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurolv.__str__() == '-100,00 €'

    def test_eurolv_custom(self):
        """test_eurolv_custom."""
        amount = 1000
        eurolv = EuroLV(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurolv.amount == decimal
        assert eurolv.numeric_code == '978'
        assert eurolv.alpha_code == 'EUR'
        assert eurolv.decimal_places == 5
        assert eurolv.decimal_sign == '\u202F'
        assert eurolv.grouping_places == 2
        assert eurolv.grouping_sign == ','
        assert eurolv.international
        assert eurolv.symbol == '€'
        assert not eurolv.symbol_ahead
        assert eurolv.symbol_separator == '_'
        assert eurolv.localized_symbol == 'LV€'
        assert eurolv.convertion == ''
        assert eurolv.__hash__() == hash(
            (eurolv.__class__, decimal, 'EUR', '978'))
        assert eurolv.__repr__() == (
            'EuroLV(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LV€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurolv.__str__() == 'EUR 10,00.00000'

    def test_eurolv_changed(self):
        """test_ceurolv_changed."""
        eurolv = EuroLV(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolv.international = True

    def test_eurolv_math_add(self):
        """test_eurolv_math_add."""
        eurolv_one = EuroLV(amount=1)
        eurolv_two = EuroLV(amount=2)
        eurolv_three = EuroLV(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurolv_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroLV\'> '
                    'and <class \'str\'>.')):
            _ = eurolv_one.__add__('1.00')
        assert (
            eurolv_one +
            eurolv_two) == eurolv_three

    def test_eurolv_slots(self):
        """test_eurolv_slots."""
        eurolv = EuroLV(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroLV\' '
                    'object has no attribute \'new_variable\'')):
            eurolv.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroLT representation."""

from multicurrency import EuroLT


class TestEuroLT:
    """EuroLT currency tests."""

    def test_eurolt(self):
        """test_eurolt."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurolt = EuroLT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolt.amount == decimal
        assert eurolt.numeric_code == '978'
        assert eurolt.alpha_code == 'EUR'
        assert eurolt.decimal_places == 2
        assert eurolt.decimal_sign == ','
        assert eurolt.grouping_places == 3
        assert eurolt.grouping_sign == '\u202F'
        assert not eurolt.international
        assert eurolt.symbol == '€'
        assert not eurolt.symbol_ahead
        assert eurolt.symbol_separator == '\u00A0'
        assert eurolt.localized_symbol == 'LT€'
        assert eurolt.convertion == ''
        assert eurolt.__hash__() == hash(
            (eurolt.__class__, decimal, 'EUR', '978'))
        assert eurolt.__repr__() == (
            'EuroLT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurolt.__str__() == '0,14 €'

    def test_eurolt_negative(self):
        """test_eurolt_negative."""
        amount = -100
        eurolt = EuroLT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolt.numeric_code == '978'
        assert eurolt.alpha_code == 'EUR'
        assert eurolt.decimal_places == 2
        assert eurolt.decimal_sign == ','
        assert eurolt.grouping_places == 3
        assert eurolt.grouping_sign == '\u202F'
        assert not eurolt.international
        assert eurolt.symbol == '€'
        assert not eurolt.symbol_ahead
        assert eurolt.symbol_separator == '\u00A0'
        assert eurolt.localized_symbol == 'LT€'
        assert eurolt.convertion == ''
        assert eurolt.__hash__() == hash(
            (eurolt.__class__, decimal, 'EUR', '978'))
        assert eurolt.__repr__() == (
            'EuroLT(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurolt.__str__() == '-100,00 €'

    def test_eurolt_custom(self):
        """test_eurolt_custom."""
        amount = 1000
        eurolt = EuroLT(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurolt.amount == decimal
        assert eurolt.numeric_code == '978'
        assert eurolt.alpha_code == 'EUR'
        assert eurolt.decimal_places == 5
        assert eurolt.decimal_sign == '\u202F'
        assert eurolt.grouping_places == 2
        assert eurolt.grouping_sign == ','
        assert eurolt.international
        assert eurolt.symbol == '€'
        assert not eurolt.symbol_ahead
        assert eurolt.symbol_separator == '_'
        assert eurolt.localized_symbol == 'LT€'
        assert eurolt.convertion == ''
        assert eurolt.__hash__() == hash(
            (eurolt.__class__, decimal, 'EUR', '978'))
        assert eurolt.__repr__() == (
            'EuroLT(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LT€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurolt.__str__() == 'EUR 10,00.00000'

    def test_eurolt_changed(self):
        """test_ceurolt_changed."""
        eurolt = EuroLT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolt.international = True

    def test_eurolt_math_add(self):
        """test_eurolt_math_add."""
        eurolt_one = EuroLT(amount=1)
        eurolt_two = EuroLT(amount=2)
        eurolt_three = EuroLT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurolt_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroLT\'> '
                    'and <class \'str\'>.')):
            _ = eurolt_one.__add__('1.00')
        assert (
            eurolt_one +
            eurolt_two) == eurolt_three

    def test_eurolt_slots(self):
        """test_eurolt_slots."""
        eurolt = EuroLT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroLT\' '
                    'object has no attribute \'new_variable\'')):
            eurolt.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroLU representation."""

from multicurrency import EuroLU


class TestEuroLU:
    """EuroLU currency tests."""

    def test_eurolu(self):
        """test_eurolu."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurolu = EuroLU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolu.amount == decimal
        assert eurolu.numeric_code == '978'
        assert eurolu.alpha_code == 'EUR'
        assert eurolu.decimal_places == 2
        assert eurolu.decimal_sign == ','
        assert eurolu.grouping_places == 3
        assert eurolu.grouping_sign == '.'
        assert not eurolu.international
        assert eurolu.symbol == '€'
        assert not eurolu.symbol_ahead
        assert eurolu.symbol_separator == '\u00A0'
        assert eurolu.localized_symbol == 'LU€'
        assert eurolu.convertion == ''
        assert eurolu.__hash__() == hash(
            (eurolu.__class__, decimal, 'EUR', '978'))
        assert eurolu.__repr__() == (
            'EuroLU(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LU€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurolu.__str__() == '0,14 €'

    def test_eurolu_negative(self):
        """test_eurolu_negative."""
        amount = -100
        eurolu = EuroLU(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurolu.numeric_code == '978'
        assert eurolu.alpha_code == 'EUR'
        assert eurolu.decimal_places == 2
        assert eurolu.decimal_sign == ','
        assert eurolu.grouping_places == 3
        assert eurolu.grouping_sign == '.'
        assert not eurolu.international
        assert eurolu.symbol == '€'
        assert not eurolu.symbol_ahead
        assert eurolu.symbol_separator == '\u00A0'
        assert eurolu.localized_symbol == 'LU€'
        assert eurolu.convertion == ''
        assert eurolu.__hash__() == hash(
            (eurolu.__class__, decimal, 'EUR', '978'))
        assert eurolu.__repr__() == (
            'EuroLU(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "LU€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurolu.__str__() == '-100,00 €'

    def test_eurolu_custom(self):
        """test_eurolu_custom."""
        amount = 1000
        eurolu = EuroLU(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurolu.amount == decimal
        assert eurolu.numeric_code == '978'
        assert eurolu.alpha_code == 'EUR'
        assert eurolu.decimal_places == 5
        assert eurolu.decimal_sign == '.'
        assert eurolu.grouping_places == 2
        assert eurolu.grouping_sign == ','
        assert eurolu.international
        assert eurolu.symbol == '€'
        assert not eurolu.symbol_ahead
        assert eurolu.symbol_separator == '_'
        assert eurolu.localized_symbol == 'LU€'
        assert eurolu.convertion == ''
        assert eurolu.__hash__() == hash(
            (eurolu.__class__, decimal, 'EUR', '978'))
        assert eurolu.__repr__() == (
            'EuroLU(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "LU€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurolu.__str__() == 'EUR 10,00.00000'

    def test_eurolu_changed(self):
        """test_ceurolu_changed."""
        eurolu = EuroLU(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurolu.international = True

    def test_eurolu_math_add(self):
        """test_eurolu_math_add."""
        eurolu_one = EuroLU(amount=1)
        eurolu_two = EuroLU(amount=2)
        eurolu_three = EuroLU(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurolu_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroLU\'> '
                    'and <class \'str\'>.')):
            _ = eurolu_one.__add__('1.00')
        assert (
            eurolu_one +
            eurolu_two) == eurolu_three

    def test_eurolu_slots(self):
        """test_eurolu_slots."""
        eurolu = EuroLU(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroLU\' '
                    'object has no attribute \'new_variable\'')):
            eurolu.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroMT representation."""

from multicurrency import EuroMT


class TestEuroMT:
    """EuroMT currency tests."""

    def test_euromt(self):
        """test_euromt."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euromt = EuroMT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euromt.amount == decimal
        assert euromt.numeric_code == '978'
        assert euromt.alpha_code == 'EUR'
        assert euromt.decimal_places == 2
        assert euromt.decimal_sign == '.'
        assert euromt.grouping_places == 3
        assert euromt.grouping_sign == ','
        assert not euromt.international
        assert euromt.symbol == '€'
        assert euromt.symbol_ahead
        assert euromt.symbol_separator == ''
        assert euromt.localized_symbol == 'MT€'
        assert euromt.convertion == ''
        assert euromt.__hash__() == hash(
            (euromt.__class__, decimal, 'EUR', '978'))
        assert euromt.__repr__() == (
            'EuroMT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert euromt.__str__() == '€0.14'

    def test_euromt_negative(self):
        """test_euromt_negative."""
        amount = -100
        euromt = EuroMT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euromt.numeric_code == '978'
        assert euromt.alpha_code == 'EUR'
        assert euromt.decimal_places == 2
        assert euromt.decimal_sign == '.'
        assert euromt.grouping_places == 3
        assert euromt.grouping_sign == ','
        assert not euromt.international
        assert euromt.symbol == '€'
        assert euromt.symbol_ahead
        assert euromt.symbol_separator == ''
        assert euromt.localized_symbol == 'MT€'
        assert euromt.convertion == ''
        assert euromt.__hash__() == hash(
            (euromt.__class__, decimal, 'EUR', '978'))
        assert euromt.__repr__() == (
            'EuroMT(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert euromt.__str__() == '€-100.00'

    def test_euromt_custom(self):
        """test_euromt_custom."""
        amount = 1000
        euromt = EuroMT(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euromt.amount == decimal
        assert euromt.numeric_code == '978'
        assert euromt.alpha_code == 'EUR'
        assert euromt.decimal_places == 5
        assert euromt.decimal_sign == ','
        assert euromt.grouping_places == 2
        assert euromt.grouping_sign == '.'
        assert euromt.international
        assert euromt.symbol == '€'
        assert not euromt.symbol_ahead
        assert euromt.symbol_separator == '_'
        assert euromt.localized_symbol == 'MT€'
        assert euromt.convertion == ''
        assert euromt.__hash__() == hash(
            (euromt.__class__, decimal, 'EUR', '978'))
        assert euromt.__repr__() == (
            'EuroMT(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MT€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert euromt.__str__() == 'EUR 10,00.00000'

    def test_euromt_changed(self):
        """test_ceuromt_changed."""
        euromt = EuroMT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromt.international = True

    def test_euromt_math_add(self):
        """test_euromt_math_add."""
        euromt_one = EuroMT(amount=1)
        euromt_two = EuroMT(amount=2)
        euromt_three = EuroMT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euromt_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroMT\'> '
                    'and <class \'str\'>.')):
            _ = euromt_one.__add__('1.00')
        assert (
            euromt_one +
            euromt_two) == euromt_three

    def test_euromt_slots(self):
        """test_euromt_slots."""
        euromt = EuroMT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroMT\' '
                    'object has no attribute \'new_variable\'')):
            euromt.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroMC representation."""

from multicurrency import EuroMC


class TestEuroMC:
    """EuroMC currency tests."""

    def test_euromc(self):
        """test_euromc."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euromc = EuroMC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euromc.amount == decimal
        assert euromc.numeric_code == '978'
        assert euromc.alpha_code == 'EUR'
        assert euromc.decimal_places == 2
        assert euromc.decimal_sign == ','
        assert euromc.grouping_places == 3
        assert euromc.grouping_sign == '\u202F'
        assert not euromc.international
        assert euromc.symbol == '€'
        assert not euromc.symbol_ahead
        assert euromc.symbol_separator == '\u00A0'
        assert euromc.localized_symbol == 'MC€'
        assert euromc.convertion == ''
        assert euromc.__hash__() == hash(
            (euromc.__class__, decimal, 'EUR', '978'))
        assert euromc.__repr__() == (
            'EuroMC(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MC€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euromc.__str__() == '0,14 €'

    def test_euromc_negative(self):
        """test_euromc_negative."""
        amount = -100
        euromc = EuroMC(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euromc.numeric_code == '978'
        assert euromc.alpha_code == 'EUR'
        assert euromc.decimal_places == 2
        assert euromc.decimal_sign == ','
        assert euromc.grouping_places == 3
        assert euromc.grouping_sign == '\u202F'
        assert not euromc.international
        assert euromc.symbol == '€'
        assert not euromc.symbol_ahead
        assert euromc.symbol_separator == '\u00A0'
        assert euromc.localized_symbol == 'MC€'
        assert euromc.convertion == ''
        assert euromc.__hash__() == hash(
            (euromc.__class__, decimal, 'EUR', '978'))
        assert euromc.__repr__() == (
            'EuroMC(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "MC€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert euromc.__str__() == '-100,00 €'

    def test_euromc_custom(self):
        """test_euromc_custom."""
        amount = 1000
        euromc = EuroMC(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euromc.amount == decimal
        assert euromc.numeric_code == '978'
        assert euromc.alpha_code == 'EUR'
        assert euromc.decimal_places == 5
        assert euromc.decimal_sign == '\u202F'
        assert euromc.grouping_places == 2
        assert euromc.grouping_sign == ','
        assert euromc.international
        assert euromc.symbol == '€'
        assert not euromc.symbol_ahead
        assert euromc.symbol_separator == '_'
        assert euromc.localized_symbol == 'MC€'
        assert euromc.convertion == ''
        assert euromc.__hash__() == hash(
            (euromc.__class__, decimal, 'EUR', '978'))
        assert euromc.__repr__() == (
            'EuroMC(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MC€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euromc.__str__() == 'EUR 10,00.00000'

    def test_euromc_changed(self):
        """test_ceuromc_changed."""
        euromc = EuroMC(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euromc.international = True

    def test_euromc_math_add(self):
        """test_euromc_math_add."""
        euromc_one = EuroMC(amount=1)
        euromc_two = EuroMC(amount=2)
        euromc_three = EuroMC(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euromc_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroMC\'> '
                    'and <class \'str\'>.')):
            _ = euromc_one.__add__('1.00')
        assert (
            euromc_one +
            euromc_two) == euromc_three

    def test_euromc_slots(self):
        """test_euromc_slots."""
        euromc = EuroMC(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroMC\' '
                    'object has no attribute \'new_variable\'')):
            euromc.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroME representation."""

from multicurrency import EuroME


class TestEuroME:
    """EuroME currency tests."""

    def test_eurome(self):
        """test_eurome."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurome = EuroME(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurome.amount == decimal
        assert eurome.numeric_code == '978'
        assert eurome.alpha_code == 'EUR'
        assert eurome.decimal_places == 2
        assert eurome.decimal_sign == ','
        assert eurome.grouping_places == 3
        assert eurome.grouping_sign == '.'
        assert not eurome.international
        assert eurome.symbol == '€'
        assert not eurome.symbol_ahead
        assert eurome.symbol_separator == '\u00A0'
        assert eurome.localized_symbol == 'ME€'
        assert eurome.convertion == ''
        assert eurome.__hash__() == hash(
            (eurome.__class__, decimal, 'EUR', '978'))
        assert eurome.__repr__() == (
            'EuroME(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ME€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurome.__str__() == '0,14 €'

    def test_eurome_negative(self):
        """test_eurome_negative."""
        amount = -100
        eurome = EuroME(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurome.numeric_code == '978'
        assert eurome.alpha_code == 'EUR'
        assert eurome.decimal_places == 2
        assert eurome.decimal_sign == ','
        assert eurome.grouping_places == 3
        assert eurome.grouping_sign == '.'
        assert not eurome.international
        assert eurome.symbol == '€'
        assert not eurome.symbol_ahead
        assert eurome.symbol_separator == '\u00A0'
        assert eurome.localized_symbol == 'ME€'
        assert eurome.convertion == ''
        assert eurome.__hash__() == hash(
            (eurome.__class__, decimal, 'EUR', '978'))
        assert eurome.__repr__() == (
            'EuroME(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ME€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurome.__str__() == '-100,00 €'

    def test_eurome_custom(self):
        """test_eurome_custom."""
        amount = 1000
        eurome = EuroME(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurome.amount == decimal
        assert eurome.numeric_code == '978'
        assert eurome.alpha_code == 'EUR'
        assert eurome.decimal_places == 5
        assert eurome.decimal_sign == '.'
        assert eurome.grouping_places == 2
        assert eurome.grouping_sign == ','
        assert eurome.international
        assert eurome.symbol == '€'
        assert not eurome.symbol_ahead
        assert eurome.symbol_separator == '_'
        assert eurome.localized_symbol == 'ME€'
        assert eurome.convertion == ''
        assert eurome.__hash__() == hash(
            (eurome.__class__, decimal, 'EUR', '978'))
        assert eurome.__repr__() == (
            'EuroME(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ME€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurome.__str__() == 'EUR 10,00.00000'

    def test_eurome_changed(self):
        """test_ceurome_changed."""
        eurome = EuroME(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurome.international = True

    def test_eurome_math_add(self):
        """test_eurome_math_add."""
        eurome_one = EuroME(amount=1)
        eurome_two = EuroME(amount=2)
        eurome_three = EuroME(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurome_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroME\'> '
                    'and <class \'str\'>.')):
            _ = eurome_one.__add__('1.00')
        assert (
            eurome_one +
            eurome_two) == eurome_three

    def test_eurome_slots(self):
        """test_eurome_slots."""
        eurome = EuroME(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroME\' '
                    'object has no attribute \'new_variable\'')):
            eurome.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroNL representation."""

from multicurrency import EuroNL


class TestEuroNL:
    """EuroNL currency tests."""

    def test_euronl(self):
        """test_euronl."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euronl = EuroNL(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euronl.amount == decimal
        assert euronl.numeric_code == '978'
        assert euronl.alpha_code == 'EUR'
        assert euronl.decimal_places == 2
        assert euronl.decimal_sign == ','
        assert euronl.grouping_places == 3
        assert euronl.grouping_sign == '.'
        assert not euronl.international
        assert euronl.symbol == '€'
        assert euronl.symbol_ahead
        assert euronl.symbol_separator == '\u00A0'
        assert euronl.localized_symbol == 'NL€'
        assert euronl.convertion == ''
        assert euronl.__hash__() == hash(
            (euronl.__class__, decimal, 'EUR', '978'))
        assert euronl.__repr__() == (
            'EuroNL(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NL€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euronl.__str__() == '€ 0,14'

    def test_euronl_negative(self):
        """test_euronl_negative."""
        amount = -100
        euronl = EuroNL(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euronl.numeric_code == '978'
        assert euronl.alpha_code == 'EUR'
        assert euronl.decimal_places == 2
        assert euronl.decimal_sign == ','
        assert euronl.grouping_places == 3
        assert euronl.grouping_sign == '.'
        assert not euronl.international
        assert euronl.symbol == '€'
        assert euronl.symbol_ahead
        assert euronl.symbol_separator == '\u00A0'
        assert euronl.localized_symbol == 'NL€'
        assert euronl.convertion == ''
        assert euronl.__hash__() == hash(
            (euronl.__class__, decimal, 'EUR', '978'))
        assert euronl.__repr__() == (
            'EuroNL(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "NL€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euronl.__str__() == '€ -100,00'

    def test_euronl_custom(self):
        """test_euronl_custom."""
        amount = 1000
        euronl = EuroNL(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euronl.amount == decimal
        assert euronl.numeric_code == '978'
        assert euronl.alpha_code == 'EUR'
        assert euronl.decimal_places == 5
        assert euronl.decimal_sign == '.'
        assert euronl.grouping_places == 2
        assert euronl.grouping_sign == ','
        assert euronl.international
        assert euronl.symbol == '€'
        assert not euronl.symbol_ahead
        assert euronl.symbol_separator == '_'
        assert euronl.localized_symbol == 'NL€'
        assert euronl.convertion == ''
        assert euronl.__hash__() == hash(
            (euronl.__class__, decimal, 'EUR', '978'))
        assert euronl.__repr__() == (
            'EuroNL(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "NL€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euronl.__str__() == 'EUR 10,00.00000'

    def test_euronl_changed(self):
        """test_ceuronl_changed."""
        euronl = EuroNL(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euronl.international = True

    def test_euronl_math_add(self):
        """test_euronl_math_add."""
        euronl_one = EuroNL(amount=1)
        euronl_two = EuroNL(amount=2)
        euronl_three = EuroNL(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euronl_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroNL\'> '
                    'and <class \'str\'>.')):
            _ = euronl_one.__add__('1.00')
        assert (
            euronl_one +
            euronl_two) == euronl_three

    def test_euronl_slots(self):
        """test_euronl_slots."""
        euronl = EuroNL(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroNL\' '
                    'object has no attribute \'new_variable\'')):
            euronl.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroPT representation."""

from multicurrency import EuroPT


class TestEuroPT:
    """EuroPT currency tests."""

    def test_europt(self):
        """test_europt."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        europt = EuroPT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert europt.amount == decimal
        assert europt.numeric_code == '978'
        assert europt.alpha_code == 'EUR'
        assert europt.decimal_places == 2
        assert europt.decimal_sign == ','
        assert europt.grouping_places == 3
        assert europt.grouping_sign == '.'
        assert not europt.international
        assert europt.symbol == '€'
        assert europt.symbol_ahead
        assert europt.symbol_separator == '\u00A0'
        assert europt.localized_symbol == 'PT€'
        assert europt.convertion == ''
        assert europt.__hash__() == hash(
            (europt.__class__, decimal, 'EUR', '978'))
        assert europt.__repr__() == (
            'EuroPT(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert europt.__str__() == '€ 0,14'

    def test_europt_negative(self):
        """test_europt_negative."""
        amount = -100
        europt = EuroPT(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert europt.numeric_code == '978'
        assert europt.alpha_code == 'EUR'
        assert europt.decimal_places == 2
        assert europt.decimal_sign == ','
        assert europt.grouping_places == 3
        assert europt.grouping_sign == '.'
        assert not europt.international
        assert europt.symbol == '€'
        assert europt.symbol_ahead
        assert europt.symbol_separator == '\u00A0'
        assert europt.localized_symbol == 'PT€'
        assert europt.convertion == ''
        assert europt.__hash__() == hash(
            (europt.__class__, decimal, 'EUR', '978'))
        assert europt.__repr__() == (
            'EuroPT(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "PT€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert europt.__str__() == '€ -100,00'

    def test_europt_custom(self):
        """test_europt_custom."""
        amount = 1000
        europt = EuroPT(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert europt.amount == decimal
        assert europt.numeric_code == '978'
        assert europt.alpha_code == 'EUR'
        assert europt.decimal_places == 5
        assert europt.decimal_sign == '.'
        assert europt.grouping_places == 2
        assert europt.grouping_sign == ','
        assert europt.international
        assert europt.symbol == '€'
        assert not europt.symbol_ahead
        assert europt.symbol_separator == '_'
        assert europt.localized_symbol == 'PT€'
        assert europt.convertion == ''
        assert europt.__hash__() == hash(
            (europt.__class__, decimal, 'EUR', '978'))
        assert europt.__repr__() == (
            'EuroPT(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "PT€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert europt.__str__() == 'EUR 10,00.00000'

    def test_europt_changed(self):
        """test_ceuropt_changed."""
        europt = EuroPT(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            europt.international = True

    def test_europt_math_add(self):
        """test_europt_math_add."""
        europt_one = EuroPT(amount=1)
        europt_two = EuroPT(amount=2)
        europt_three = EuroPT(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = europt_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroPT\'> '
                    'and <class \'str\'>.')):
            _ = europt_one.__add__('1.00')
        assert (
            europt_one +
            europt_two) == europt_three

    def test_europt_slots(self):
        """test_europt_slots."""
        europt = EuroPT(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroPT\' '
                    'object has no attribute \'new_variable\'')):
            europt.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroSM representation."""

from multicurrency import EuroSM


class TestEuroSM:
    """EuroSM currency tests."""

    def test_eurosm(self):
        """test_eurosm."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurosm = EuroSM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosm.amount == decimal
        assert eurosm.numeric_code == '978'
        assert eurosm.alpha_code == 'EUR'
        assert eurosm.decimal_places == 2
        assert eurosm.decimal_sign == ','
        assert eurosm.grouping_places == 3
        assert eurosm.grouping_sign == '.'
        assert not eurosm.international
        assert eurosm.symbol == '€'
        assert not eurosm.symbol_ahead
        assert eurosm.symbol_separator == '\u00A0'
        assert eurosm.localized_symbol == 'SM€'
        assert eurosm.convertion == ''
        assert eurosm.__hash__() == hash(
            (eurosm.__class__, decimal, 'EUR', '978'))
        assert eurosm.__repr__() == (
            'EuroSM(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SM€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosm.__str__() == '0,14 €'

    def test_eurosm_negative(self):
        """test_eurosm_negative."""
        amount = -100
        eurosm = EuroSM(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosm.numeric_code == '978'
        assert eurosm.alpha_code == 'EUR'
        assert eurosm.decimal_places == 2
        assert eurosm.decimal_sign == ','
        assert eurosm.grouping_places == 3
        assert eurosm.grouping_sign == '.'
        assert not eurosm.international
        assert eurosm.symbol == '€'
        assert not eurosm.symbol_ahead
        assert eurosm.symbol_separator == '\u00A0'
        assert eurosm.localized_symbol == 'SM€'
        assert eurosm.convertion == ''
        assert eurosm.__hash__() == hash(
            (eurosm.__class__, decimal, 'EUR', '978'))
        assert eurosm.__repr__() == (
            'EuroSM(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SM€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosm.__str__() == '-100,00 €'

    def test_eurosm_custom(self):
        """test_eurosm_custom."""
        amount = 1000
        eurosm = EuroSM(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurosm.amount == decimal
        assert eurosm.numeric_code == '978'
        assert eurosm.alpha_code == 'EUR'
        assert eurosm.decimal_places == 5
        assert eurosm.decimal_sign == '.'
        assert eurosm.grouping_places == 2
        assert eurosm.grouping_sign == ','
        assert eurosm.international
        assert eurosm.symbol == '€'
        assert not eurosm.symbol_ahead
        assert eurosm.symbol_separator == '_'
        assert eurosm.localized_symbol == 'SM€'
        assert eurosm.convertion == ''
        assert eurosm.__hash__() == hash(
            (eurosm.__class__, decimal, 'EUR', '978'))
        assert eurosm.__repr__() == (
            'EuroSM(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SM€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurosm.__str__() == 'EUR 10,00.00000'

    def test_eurosm_changed(self):
        """test_ceurosm_changed."""
        eurosm = EuroSM(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosm.international = True

    def test_eurosm_math_add(self):
        """test_eurosm_math_add."""
        eurosm_one = EuroSM(amount=1)
        eurosm_two = EuroSM(amount=2)
        eurosm_three = EuroSM(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurosm_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroSM\'> '
                    'and <class \'str\'>.')):
            _ = eurosm_one.__add__('1.00')
        assert (
            eurosm_one +
            eurosm_two) == eurosm_three

    def test_eurosm_slots(self):
        """test_eurosm_slots."""
        eurosm = EuroSM(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroSM\' '
                    'object has no attribute \'new_variable\'')):
            eurosm.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroSK representation."""

from multicurrency import EuroSK


class TestEuroSK:
    """EuroSK currency tests."""

    def test_eurosk(self):
        """test_eurosk."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurosk = EuroSK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosk.amount == decimal
        assert eurosk.numeric_code == '978'
        assert eurosk.alpha_code == 'EUR'
        assert eurosk.decimal_places == 2
        assert eurosk.decimal_sign == ','
        assert eurosk.grouping_places == 3
        assert eurosk.grouping_sign == '\u202F'
        assert not eurosk.international
        assert eurosk.symbol == '€'
        assert not eurosk.symbol_ahead
        assert eurosk.symbol_separator == '\u00A0'
        assert eurosk.localized_symbol == 'SK€'
        assert eurosk.convertion == ''
        assert eurosk.__hash__() == hash(
            (eurosk.__class__, decimal, 'EUR', '978'))
        assert eurosk.__repr__() == (
            'EuroSK(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SK€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurosk.__str__() == '0,14 €'

    def test_eurosk_negative(self):
        """test_eurosk_negative."""
        amount = -100
        eurosk = EuroSK(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosk.numeric_code == '978'
        assert eurosk.alpha_code == 'EUR'
        assert eurosk.decimal_places == 2
        assert eurosk.decimal_sign == ','
        assert eurosk.grouping_places == 3
        assert eurosk.grouping_sign == '\u202F'
        assert not eurosk.international
        assert eurosk.symbol == '€'
        assert not eurosk.symbol_ahead
        assert eurosk.symbol_separator == '\u00A0'
        assert eurosk.localized_symbol == 'SK€'
        assert eurosk.convertion == ''
        assert eurosk.__hash__() == hash(
            (eurosk.__class__, decimal, 'EUR', '978'))
        assert eurosk.__repr__() == (
            'EuroSK(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SK€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: "\u202F", '
            'convertion: "", '
            'international: False)')
        assert eurosk.__str__() == '-100,00 €'

    def test_eurosk_custom(self):
        """test_eurosk_custom."""
        amount = 1000
        eurosk = EuroSK(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u202F',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurosk.amount == decimal
        assert eurosk.numeric_code == '978'
        assert eurosk.alpha_code == 'EUR'
        assert eurosk.decimal_places == 5
        assert eurosk.decimal_sign == '\u202F'
        assert eurosk.grouping_places == 2
        assert eurosk.grouping_sign == ','
        assert eurosk.international
        assert eurosk.symbol == '€'
        assert not eurosk.symbol_ahead
        assert eurosk.symbol_separator == '_'
        assert eurosk.localized_symbol == 'SK€'
        assert eurosk.convertion == ''
        assert eurosk.__hash__() == hash(
            (eurosk.__class__, decimal, 'EUR', '978'))
        assert eurosk.__repr__() == (
            'EuroSK(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SK€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: "\u202F", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurosk.__str__() == 'EUR 10,00.00000'

    def test_eurosk_changed(self):
        """test_ceurosk_changed."""
        eurosk = EuroSK(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosk.international = True

    def test_eurosk_math_add(self):
        """test_eurosk_math_add."""
        eurosk_one = EuroSK(amount=1)
        eurosk_two = EuroSK(amount=2)
        eurosk_three = EuroSK(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurosk_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroSK\'> '
                    'and <class \'str\'>.')):
            _ = eurosk_one.__add__('1.00')
        assert (
            eurosk_one +
            eurosk_two) == eurosk_three

    def test_eurosk_slots(self):
        """test_eurosk_slots."""
        eurosk = EuroSK(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroSK\' '
                    'object has no attribute \'new_variable\'')):
            eurosk.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroSI representation."""

from multicurrency import EuroSI


class TestEuroSI:
    """EuroSI currency tests."""

    def test_eurosi(self):
        """test_eurosi."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurosi = EuroSI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosi.amount == decimal
        assert eurosi.numeric_code == '978'
        assert eurosi.alpha_code == 'EUR'
        assert eurosi.decimal_places == 2
        assert eurosi.decimal_sign == ','
        assert eurosi.grouping_places == 3
        assert eurosi.grouping_sign == '.'
        assert not eurosi.international
        assert eurosi.symbol == '€'
        assert not eurosi.symbol_ahead
        assert eurosi.symbol_separator == '\u00A0'
        assert eurosi.localized_symbol == 'SI€'
        assert eurosi.convertion == ''
        assert eurosi.__hash__() == hash(
            (eurosi.__class__, decimal, 'EUR', '978'))
        assert eurosi.__repr__() == (
            'EuroSI(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SI€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosi.__str__() == '0,14 €'

    def test_eurosi_negative(self):
        """test_eurosi_negative."""
        amount = -100
        eurosi = EuroSI(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurosi.numeric_code == '978'
        assert eurosi.alpha_code == 'EUR'
        assert eurosi.decimal_places == 2
        assert eurosi.decimal_sign == ','
        assert eurosi.grouping_places == 3
        assert eurosi.grouping_sign == '.'
        assert not eurosi.international
        assert eurosi.symbol == '€'
        assert not eurosi.symbol_ahead
        assert eurosi.symbol_separator == '\u00A0'
        assert eurosi.localized_symbol == 'SI€'
        assert eurosi.convertion == ''
        assert eurosi.__hash__() == hash(
            (eurosi.__class__, decimal, 'EUR', '978'))
        assert eurosi.__repr__() == (
            'EuroSI(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "SI€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert eurosi.__str__() == '-100,00 €'

    def test_eurosi_custom(self):
        """test_eurosi_custom."""
        amount = 1000
        eurosi = EuroSI(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurosi.amount == decimal
        assert eurosi.numeric_code == '978'
        assert eurosi.alpha_code == 'EUR'
        assert eurosi.decimal_places == 5
        assert eurosi.decimal_sign == '.'
        assert eurosi.grouping_places == 2
        assert eurosi.grouping_sign == ','
        assert eurosi.international
        assert eurosi.symbol == '€'
        assert not eurosi.symbol_ahead
        assert eurosi.symbol_separator == '_'
        assert eurosi.localized_symbol == 'SI€'
        assert eurosi.convertion == ''
        assert eurosi.__hash__() == hash(
            (eurosi.__class__, decimal, 'EUR', '978'))
        assert eurosi.__repr__() == (
            'EuroSI(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "SI€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert eurosi.__str__() == 'EUR 10,00.00000'

    def test_eurosi_changed(self):
        """test_ceurosi_changed."""
        eurosi = EuroSI(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurosi.international = True

    def test_eurosi_math_add(self):
        """test_eurosi_math_add."""
        eurosi_one = EuroSI(amount=1)
        eurosi_two = EuroSI(amount=2)
        eurosi_three = EuroSI(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurosi_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroSI\'> '
                    'and <class \'str\'>.')):
            _ = eurosi_one.__add__('1.00')
        assert (
            eurosi_one +
            eurosi_two) == eurosi_three

    def test_eurosi_slots(self):
        """test_eurosi_slots."""
        eurosi = EuroSI(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroSI\' '
                    'object has no attribute \'new_variable\'')):
            eurosi.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroES representation."""

from multicurrency import EuroES


class TestEuroES:
    """EuroES currency tests."""

    def test_euroes(self):
        """test_euroes."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        euroes = EuroES(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroes.amount == decimal
        assert euroes.numeric_code == '978'
        assert euroes.alpha_code == 'EUR'
        assert euroes.decimal_places == 2
        assert euroes.decimal_sign == ','
        assert euroes.grouping_places == 3
        assert euroes.grouping_sign == '.'
        assert not euroes.international
        assert euroes.symbol == '€'
        assert not euroes.symbol_ahead
        assert euroes.symbol_separator == '\u00A0'
        assert euroes.localized_symbol == 'ES€'
        assert euroes.convertion == ''
        assert euroes.__hash__() == hash(
            (euroes.__class__, decimal, 'EUR', '978'))
        assert euroes.__repr__() == (
            'EuroES(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ES€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroes.__str__() == '0,14 €'

    def test_euroes_negative(self):
        """test_euroes_negative."""
        amount = -100
        euroes = EuroES(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert euroes.numeric_code == '978'
        assert euroes.alpha_code == 'EUR'
        assert euroes.decimal_places == 2
        assert euroes.decimal_sign == ','
        assert euroes.grouping_places == 3
        assert euroes.grouping_sign == '.'
        assert not euroes.international
        assert euroes.symbol == '€'
        assert not euroes.symbol_ahead
        assert euroes.symbol_separator == '\u00A0'
        assert euroes.localized_symbol == 'ES€'
        assert euroes.convertion == ''
        assert euroes.__hash__() == hash(
            (euroes.__class__, decimal, 'EUR', '978'))
        assert euroes.__repr__() == (
            'EuroES(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ES€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert euroes.__str__() == '-100,00 €'

    def test_euroes_custom(self):
        """test_euroes_custom."""
        amount = 1000
        euroes = EuroES(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert euroes.amount == decimal
        assert euroes.numeric_code == '978'
        assert euroes.alpha_code == 'EUR'
        assert euroes.decimal_places == 5
        assert euroes.decimal_sign == '.'
        assert euroes.grouping_places == 2
        assert euroes.grouping_sign == ','
        assert euroes.international
        assert euroes.symbol == '€'
        assert not euroes.symbol_ahead
        assert euroes.symbol_separator == '_'
        assert euroes.localized_symbol == 'ES€'
        assert euroes.convertion == ''
        assert euroes.__hash__() == hash(
            (euroes.__class__, decimal, 'EUR', '978'))
        assert euroes.__repr__() == (
            'EuroES(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ES€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert euroes.__str__() == 'EUR 10,00.00000'

    def test_euroes_changed(self):
        """test_ceuroes_changed."""
        euroes = EuroES(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            euroes.international = True

    def test_euroes_math_add(self):
        """test_euroes_math_add."""
        euroes_one = EuroES(amount=1)
        euroes_two = EuroES(amount=2)
        euroes_three = EuroES(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = euroes_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroES\'> '
                    'and <class \'str\'>.')):
            _ = euroes_one.__add__('1.00')
        assert (
            euroes_one +
            euroes_two) == euroes_three

    def test_euroes_slots(self):
        """test_euroes_slots."""
        euroes = EuroES(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroES\' '
                    'object has no attribute \'new_variable\'')):
            euroes.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the EuroVA representation."""

from multicurrency import EuroVA


class TestEuroVA:
    """EuroVA currency tests."""

    def test_eurova(self):
        """test_eurova."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        eurova = EuroVA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurova.amount == decimal
        assert eurova.numeric_code == '978'
        assert eurova.alpha_code == 'EUR'
        assert eurova.decimal_places == 2
        assert eurova.decimal_sign == '.'
        assert eurova.grouping_places == 3
        assert eurova.grouping_sign == ','
        assert not eurova.international
        assert eurova.symbol == '€'
        assert eurova.symbol_ahead
        assert eurova.symbol_separator == ''
        assert eurova.localized_symbol == 'VA€'
        assert eurova.convertion == ''
        assert eurova.__hash__() == hash(
            (eurova.__class__, decimal, 'EUR', '978'))
        assert eurova.__repr__() == (
            'EuroVA(amount: 0.1428571428571428571428571429, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VA€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eurova.__str__() == '€0.14'

    def test_eurova_negative(self):
        """test_eurova_negative."""
        amount = -100
        eurova = EuroVA(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert eurova.numeric_code == '978'
        assert eurova.alpha_code == 'EUR'
        assert eurova.decimal_places == 2
        assert eurova.decimal_sign == '.'
        assert eurova.grouping_places == 3
        assert eurova.grouping_sign == ','
        assert not eurova.international
        assert eurova.symbol == '€'
        assert eurova.symbol_ahead
        assert eurova.symbol_separator == ''
        assert eurova.localized_symbol == 'VA€'
        assert eurova.convertion == ''
        assert eurova.__hash__() == hash(
            (eurova.__class__, decimal, 'EUR', '978'))
        assert eurova.__repr__() == (
            'EuroVA(amount: -100, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "VA€", '
            'numeric_code: "978", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert eurova.__str__() == '€-100.00'

    def test_eurova_custom(self):
        """test_eurova_custom."""
        amount = 1000
        eurova = EuroVA(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert eurova.amount == decimal
        assert eurova.numeric_code == '978'
        assert eurova.alpha_code == 'EUR'
        assert eurova.decimal_places == 5
        assert eurova.decimal_sign == ','
        assert eurova.grouping_places == 2
        assert eurova.grouping_sign == '.'
        assert eurova.international
        assert eurova.symbol == '€'
        assert not eurova.symbol_ahead
        assert eurova.symbol_separator == '_'
        assert eurova.localized_symbol == 'VA€'
        assert eurova.convertion == ''
        assert eurova.__hash__() == hash(
            (eurova.__class__, decimal, 'EUR', '978'))
        assert eurova.__repr__() == (
            'EuroVA(amount: 1000, '
            'alpha_code: "EUR", '
            'symbol: "€", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "VA€", '
            'numeric_code: "978", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert eurova.__str__() == 'EUR 10,00.00000'

    def test_eurova_changed(self):
        """test_ceurova_changed."""
        eurova = EuroVA(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            eurova.international = True

    def test_eurova_math_add(self):
        """test_eurova_math_add."""
        eurova_one = EuroVA(amount=1)
        eurova_two = EuroVA(amount=2)
        eurova_three = EuroVA(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency EUR and OTHER.'):
            _ = eurova_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'euro.EuroVA\'> '
                    'and <class \'str\'>.')):
            _ = eurova_one.__add__('1.00')
        assert (
            eurova_one +
            eurova_two) == eurova_three

    def test_eurova_slots(self):
        """test_eurova_slots."""
        eurova = EuroVA(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'EuroVA\' '
                    'object has no attribute \'new_variable\'')):
            eurova.new_variable = 'fail'  # pylint: disable=assigning-non-slot
