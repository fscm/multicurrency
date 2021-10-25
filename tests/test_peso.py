# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Peso currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Argentine Peso representation."""

from multicurrency import ArgentinePeso


class TestArgentinePeso:

    def test_argentine_peso(self):
        """test_argentine_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        argentine_peso = ArgentinePeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert argentine_peso.amount == decimal
        assert argentine_peso.numeric_code == '032'
        assert argentine_peso.alpha_code == 'ARS'
        assert argentine_peso.decimal_places == 2
        assert argentine_peso.decimal_sign == ','
        assert argentine_peso.grouping_places == 3
        assert argentine_peso.grouping_sign == '.'
        assert not argentine_peso.international
        assert argentine_peso.symbol == '$'
        assert argentine_peso.symbol_ahead
        assert argentine_peso.symbol_separator == '\u00A0'
        assert argentine_peso.localized_symbol == 'AR$'
        assert argentine_peso.convertion == ''
        assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
        assert argentine_peso.__repr__() == (
            'ArgentinePeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "ARS", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AR$", '
            'numeric_code: "032", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert argentine_peso.__str__() == '$ 0,14'


    def test_argentine_peso_negative(self):
        """test_argentine_peso_negative."""
        amount = -100
        argentine_peso = ArgentinePeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert argentine_peso.numeric_code == '032'
        assert argentine_peso.alpha_code == 'ARS'
        assert argentine_peso.decimal_places == 2
        assert argentine_peso.decimal_sign == ','
        assert argentine_peso.grouping_places == 3
        assert argentine_peso.grouping_sign == '.'
        assert not argentine_peso.international
        assert argentine_peso.symbol == '$'
        assert argentine_peso.symbol_ahead
        assert argentine_peso.symbol_separator == '\u00A0'
        assert argentine_peso.localized_symbol == 'AR$'
        assert argentine_peso.convertion == ''
        assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
        assert argentine_peso.__repr__() == (
            'ArgentinePeso(amount: -100, '
            'alpha_code: "ARS", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "AR$", '
            'numeric_code: "032", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert argentine_peso.__str__() == '$ -100,00'


    def test_argentine_peso_custom(self):
        """test_argentine_peso_custom."""
        amount = 1000
        argentine_peso = ArgentinePeso(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert argentine_peso.amount == decimal
        assert argentine_peso.numeric_code == '032'
        assert argentine_peso.alpha_code == 'ARS'
        assert argentine_peso.decimal_places == 5
        assert argentine_peso.decimal_sign == '.'
        assert argentine_peso.grouping_places == 2
        assert argentine_peso.grouping_sign == ','
        assert argentine_peso.international
        assert argentine_peso.symbol == '$'
        assert not argentine_peso.symbol_ahead
        assert argentine_peso.symbol_separator == '_'
        assert argentine_peso.localized_symbol == 'AR$'
        assert argentine_peso.convertion == ''
        assert argentine_peso.__hash__() == hash((decimal, 'ARS', '032'))
        assert argentine_peso.__repr__() == (
            'ArgentinePeso(amount: 1000, '
            'alpha_code: "ARS", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "AR$", '
            'numeric_code: "032", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert argentine_peso.__str__() == 'ARS 10,00.00000'


    def test_argentine_peso_changed(self):
        """test_cargentine_peso_changed."""
        argentine_peso = ArgentinePeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            argentine_peso.international = True


    def test_argentine_peso_math_add(self):
        """test_argentine_peso_math_add."""
        argentine_peso_one = ArgentinePeso(amount=1)
        argentine_peso_two = ArgentinePeso(amount=2)
        argentine_peso_three = ArgentinePeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency ARS and OTHER.'):
            _ = argentine_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.ArgentinePeso\'> '
                    'and <class \'str\'>.')):
            _ = argentine_peso_one.__add__('1.00')
        assert (
            argentine_peso_one +
            argentine_peso_two) == argentine_peso_three


    def test_argentine_peso_slots(self):
        """test_argentine_peso_slots."""
        argentine_peso = ArgentinePeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ArgentinePeso\' '
                    'object has no attribute \'new_variable\'')):
            argentine_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Chilean Peso representation."""

from multicurrency import ChileanPeso


class TestChileanPeso:

    def test_chilean_peso(self):
        """test_chilean_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        chilean_peso = ChileanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert chilean_peso.amount == decimal
        assert chilean_peso.numeric_code == '152'
        assert chilean_peso.alpha_code == 'CLP'
        assert chilean_peso.decimal_places == 0
        assert chilean_peso.decimal_sign == ','
        assert chilean_peso.grouping_places == 3
        assert chilean_peso.grouping_sign == '.'
        assert not chilean_peso.international
        assert chilean_peso.symbol == '$'
        assert chilean_peso.symbol_ahead
        assert chilean_peso.symbol_separator == ''
        assert chilean_peso.localized_symbol == 'CL$'
        assert chilean_peso.convertion == ''
        assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
        assert chilean_peso.__repr__() == (
            'ChileanPeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CLP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CL$", '
            'numeric_code: "152", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert chilean_peso.__str__() == '$0'


    def test_chilean_peso_negative(self):
        """test_chilean_peso_negative."""
        amount = -100
        chilean_peso = ChileanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert chilean_peso.numeric_code == '152'
        assert chilean_peso.alpha_code == 'CLP'
        assert chilean_peso.decimal_places == 0
        assert chilean_peso.decimal_sign == ','
        assert chilean_peso.grouping_places == 3
        assert chilean_peso.grouping_sign == '.'
        assert not chilean_peso.international
        assert chilean_peso.symbol == '$'
        assert chilean_peso.symbol_ahead
        assert chilean_peso.symbol_separator == ''
        assert chilean_peso.localized_symbol == 'CL$'
        assert chilean_peso.convertion == ''
        assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
        assert chilean_peso.__repr__() == (
            'ChileanPeso(amount: -100, '
            'alpha_code: "CLP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CL$", '
            'numeric_code: "152", '
            'decimal_places: "0", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert chilean_peso.__str__() == '$-100'


    def test_chilean_peso_custom(self):
        """test_chilean_peso_custom."""
        amount = 1000
        chilean_peso = ChileanPeso(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert chilean_peso.amount == decimal
        assert chilean_peso.numeric_code == '152'
        assert chilean_peso.alpha_code == 'CLP'
        assert chilean_peso.decimal_places == 5
        assert chilean_peso.decimal_sign == '.'
        assert chilean_peso.grouping_places == 2
        assert chilean_peso.grouping_sign == ','
        assert chilean_peso.international
        assert chilean_peso.symbol == '$'
        assert not chilean_peso.symbol_ahead
        assert chilean_peso.symbol_separator == '_'
        assert chilean_peso.localized_symbol == 'CL$'
        assert chilean_peso.convertion == ''
        assert chilean_peso.__hash__() == hash((decimal, 'CLP', '152'))
        assert chilean_peso.__repr__() == (
            'ChileanPeso(amount: 1000, '
            'alpha_code: "CLP", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CL$", '
            'numeric_code: "152", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert chilean_peso.__str__() == 'CLP 10,00.00000'


    def test_chilean_peso_changed(self):
        """test_cchilean_peso_changed."""
        chilean_peso = ChileanPeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            chilean_peso.international = True


    def test_chilean_peso_math_add(self):
        """test_chilean_peso_math_add."""
        chilean_peso_one = ChileanPeso(amount=1)
        chilean_peso_two = ChileanPeso(amount=2)
        chilean_peso_three = ChileanPeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CLP and OTHER.'):
            _ = chilean_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.ChileanPeso\'> '
                    'and <class \'str\'>.')):
            _ = chilean_peso_one.__add__('1.00')
        assert (
            chilean_peso_one +
            chilean_peso_two) == chilean_peso_three


    def test_chilean_peso_slots(self):
        """test_chilean_peso_slots."""
        chilean_peso = ChileanPeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ChileanPeso\' '
                    'object has no attribute \'new_variable\'')):
            chilean_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Colombian Peso representation."""

from multicurrency import ColombianPeso


class TestColombianPeso:

    def test_colombian_peso(self):
        """test_colombian_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        colombian_peso = ColombianPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert colombian_peso.amount == decimal
        assert colombian_peso.numeric_code == '170'
        assert colombian_peso.alpha_code == 'COP'
        assert colombian_peso.decimal_places == 2
        assert colombian_peso.decimal_sign == ','
        assert colombian_peso.grouping_places == 3
        assert colombian_peso.grouping_sign == '.'
        assert not colombian_peso.international
        assert colombian_peso.symbol == '$'
        assert colombian_peso.symbol_ahead
        assert colombian_peso.symbol_separator == '\u00A0'
        assert colombian_peso.localized_symbol == 'CO$'
        assert colombian_peso.convertion == ''
        assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
        assert colombian_peso.__repr__() == (
            'ColombianPeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "COP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CO$", '
            'numeric_code: "170", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert colombian_peso.__str__() == '$ 0,14'


    def test_colombian_peso_negative(self):
        """test_colombian_peso_negative."""
        amount = -100
        colombian_peso = ColombianPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert colombian_peso.numeric_code == '170'
        assert colombian_peso.alpha_code == 'COP'
        assert colombian_peso.decimal_places == 2
        assert colombian_peso.decimal_sign == ','
        assert colombian_peso.grouping_places == 3
        assert colombian_peso.grouping_sign == '.'
        assert not colombian_peso.international
        assert colombian_peso.symbol == '$'
        assert colombian_peso.symbol_ahead
        assert colombian_peso.symbol_separator == '\u00A0'
        assert colombian_peso.localized_symbol == 'CO$'
        assert colombian_peso.convertion == ''
        assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
        assert colombian_peso.__repr__() == (
            'ColombianPeso(amount: -100, '
            'alpha_code: "COP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "CO$", '
            'numeric_code: "170", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert colombian_peso.__str__() == '$ -100,00'


    def test_colombian_peso_custom(self):
        """test_colombian_peso_custom."""
        amount = 1000
        colombian_peso = ColombianPeso(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert colombian_peso.amount == decimal
        assert colombian_peso.numeric_code == '170'
        assert colombian_peso.alpha_code == 'COP'
        assert colombian_peso.decimal_places == 5
        assert colombian_peso.decimal_sign == '.'
        assert colombian_peso.grouping_places == 2
        assert colombian_peso.grouping_sign == ','
        assert colombian_peso.international
        assert colombian_peso.symbol == '$'
        assert not colombian_peso.symbol_ahead
        assert colombian_peso.symbol_separator == '_'
        assert colombian_peso.localized_symbol == 'CO$'
        assert colombian_peso.convertion == ''
        assert colombian_peso.__hash__() == hash((decimal, 'COP', '170'))
        assert colombian_peso.__repr__() == (
            'ColombianPeso(amount: 1000, '
            'alpha_code: "COP", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CO$", '
            'numeric_code: "170", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert colombian_peso.__str__() == 'COP 10,00.00000'


    def test_colombian_peso_changed(self):
        """test_ccolombian_peso_changed."""
        colombian_peso = ColombianPeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            colombian_peso.international = True


    def test_colombian_peso_math_add(self):
        """test_colombian_peso_math_add."""
        colombian_peso_one = ColombianPeso(amount=1)
        colombian_peso_two = ColombianPeso(amount=2)
        colombian_peso_three = ColombianPeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency COP and OTHER.'):
            _ = colombian_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.ColombianPeso\'> '
                    'and <class \'str\'>.')):
            _ = colombian_peso_one.__add__('1.00')
        assert (
            colombian_peso_one +
            colombian_peso_two) == colombian_peso_three


    def test_colombian_peso_slots(self):
        """test_colombian_peso_slots."""
        colombian_peso = ColombianPeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'ColombianPeso\' '
                    'object has no attribute \'new_variable\'')):
            colombian_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Cuban Peso representation."""

from multicurrency import CubanPeso


class TestCubanPeso:

    def test_cuban_peso(self):
        """test_cuban_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        cuban_peso = CubanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cuban_peso.amount == decimal
        assert cuban_peso.numeric_code == '192'
        assert cuban_peso.alpha_code == 'CUP'
        assert cuban_peso.decimal_places == 2
        assert cuban_peso.decimal_sign == '.'
        assert cuban_peso.grouping_places == 3
        assert cuban_peso.grouping_sign == ','
        assert not cuban_peso.international
        assert cuban_peso.symbol == '$'
        assert cuban_peso.symbol_ahead
        assert cuban_peso.symbol_separator == ''
        assert cuban_peso.localized_symbol == 'CU$'
        assert cuban_peso.convertion == ''
        assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
        assert cuban_peso.__repr__() == (
            'CubanPeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "CUP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CU$", '
            'numeric_code: "192", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert cuban_peso.__str__() == '$0.14'


    def test_cuban_peso_negative(self):
        """test_cuban_peso_negative."""
        amount = -100
        cuban_peso = CubanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert cuban_peso.numeric_code == '192'
        assert cuban_peso.alpha_code == 'CUP'
        assert cuban_peso.decimal_places == 2
        assert cuban_peso.decimal_sign == '.'
        assert cuban_peso.grouping_places == 3
        assert cuban_peso.grouping_sign == ','
        assert not cuban_peso.international
        assert cuban_peso.symbol == '$'
        assert cuban_peso.symbol_ahead
        assert cuban_peso.symbol_separator == ''
        assert cuban_peso.localized_symbol == 'CU$'
        assert cuban_peso.convertion == ''
        assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
        assert cuban_peso.__repr__() == (
            'CubanPeso(amount: -100, '
            'alpha_code: "CUP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "CU$", '
            'numeric_code: "192", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert cuban_peso.__str__() == '$-100.00'


    def test_cuban_peso_custom(self):
        """test_cuban_peso_custom."""
        amount = 1000
        cuban_peso = CubanPeso(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert cuban_peso.amount == decimal
        assert cuban_peso.numeric_code == '192'
        assert cuban_peso.alpha_code == 'CUP'
        assert cuban_peso.decimal_places == 5
        assert cuban_peso.decimal_sign == ','
        assert cuban_peso.grouping_places == 2
        assert cuban_peso.grouping_sign == '.'
        assert cuban_peso.international
        assert cuban_peso.symbol == '$'
        assert not cuban_peso.symbol_ahead
        assert cuban_peso.symbol_separator == '_'
        assert cuban_peso.localized_symbol == 'CU$'
        assert cuban_peso.convertion == ''
        assert cuban_peso.__hash__() == hash((decimal, 'CUP', '192'))
        assert cuban_peso.__repr__() == (
            'CubanPeso(amount: 1000, '
            'alpha_code: "CUP", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "CU$", '
            'numeric_code: "192", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert cuban_peso.__str__() == 'CUP 10,00.00000'


    def test_cuban_peso_changed(self):
        """test_ccuban_peso_changed."""
        cuban_peso = CubanPeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            cuban_peso.international = True


    def test_cuban_peso_math_add(self):
        """test_cuban_peso_math_add."""
        cuban_peso_one = CubanPeso(amount=1)
        cuban_peso_two = CubanPeso(amount=2)
        cuban_peso_three = CubanPeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency CUP and OTHER.'):
            _ = cuban_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.CubanPeso\'> '
                    'and <class \'str\'>.')):
            _ = cuban_peso_one.__add__('1.00')
        assert (
            cuban_peso_one +
            cuban_peso_two) == cuban_peso_three


    def test_cuban_peso_slots(self):
        """test_cuban_peso_slots."""
        cuban_peso = CubanPeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'CubanPeso\' '
                    'object has no attribute \'new_variable\'')):
            cuban_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Dominican Peso representation."""

from multicurrency import DominicanPeso


class TestDominicanPeso:

    def test_dominican_peso(self):
        """test_dominican_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        dominican_peso = DominicanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert dominican_peso.amount == decimal
        assert dominican_peso.numeric_code == '214'
        assert dominican_peso.alpha_code == 'DOP'
        assert dominican_peso.decimal_places == 2
        assert dominican_peso.decimal_sign == '.'
        assert dominican_peso.grouping_places == 3
        assert dominican_peso.grouping_sign == ','
        assert not dominican_peso.international
        assert dominican_peso.symbol == '$'
        assert dominican_peso.symbol_ahead
        assert dominican_peso.symbol_separator == ''
        assert dominican_peso.localized_symbol == 'DO$'
        assert dominican_peso.convertion == ''
        assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
        assert dominican_peso.__repr__() == (
            'DominicanPeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "DOP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "DO$", '
            'numeric_code: "214", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert dominican_peso.__str__() == '$0.14'


    def test_dominican_peso_negative(self):
        """test_dominican_peso_negative."""
        amount = -100
        dominican_peso = DominicanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert dominican_peso.numeric_code == '214'
        assert dominican_peso.alpha_code == 'DOP'
        assert dominican_peso.decimal_places == 2
        assert dominican_peso.decimal_sign == '.'
        assert dominican_peso.grouping_places == 3
        assert dominican_peso.grouping_sign == ','
        assert not dominican_peso.international
        assert dominican_peso.symbol == '$'
        assert dominican_peso.symbol_ahead
        assert dominican_peso.symbol_separator == ''
        assert dominican_peso.localized_symbol == 'DO$'
        assert dominican_peso.convertion == ''
        assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
        assert dominican_peso.__repr__() == (
            'DominicanPeso(amount: -100, '
            'alpha_code: "DOP", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "DO$", '
            'numeric_code: "214", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert dominican_peso.__str__() == '$-100.00'


    def test_dominican_peso_custom(self):
        """test_dominican_peso_custom."""
        amount = 1000
        dominican_peso = DominicanPeso(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert dominican_peso.amount == decimal
        assert dominican_peso.numeric_code == '214'
        assert dominican_peso.alpha_code == 'DOP'
        assert dominican_peso.decimal_places == 5
        assert dominican_peso.decimal_sign == ','
        assert dominican_peso.grouping_places == 2
        assert dominican_peso.grouping_sign == '.'
        assert dominican_peso.international
        assert dominican_peso.symbol == '$'
        assert not dominican_peso.symbol_ahead
        assert dominican_peso.symbol_separator == '_'
        assert dominican_peso.localized_symbol == 'DO$'
        assert dominican_peso.convertion == ''
        assert dominican_peso.__hash__() == hash((decimal, 'DOP', '214'))
        assert dominican_peso.__repr__() == (
            'DominicanPeso(amount: 1000, '
            'alpha_code: "DOP", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "DO$", '
            'numeric_code: "214", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert dominican_peso.__str__() == 'DOP 10,00.00000'


    def test_dominican_peso_changed(self):
        """test_cdominican_peso_changed."""
        dominican_peso = DominicanPeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            dominican_peso.international = True


    def test_dominican_peso_math_add(self):
        """test_dominican_peso_math_add."""
        dominican_peso_one = DominicanPeso(amount=1)
        dominican_peso_two = DominicanPeso(amount=2)
        dominican_peso_three = DominicanPeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency DOP and OTHER.'):
            _ = dominican_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.DominicanPeso\'> '
                    'and <class \'str\'>.')):
            _ = dominican_peso_one.__add__('1.00')
        assert (
            dominican_peso_one +
            dominican_peso_two) == dominican_peso_three


    def test_dominican_peso_slots(self):
        """test_dominican_peso_slots."""
        dominican_peso = DominicanPeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'DominicanPeso\' '
                    'object has no attribute \'new_variable\'')):
            dominican_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Mexican Peso representation."""

from multicurrency import MexicanPeso


class TestMexicanPeso:

    def test_mexican_peso(self):
        """test_mexican_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        mexican_peso = MexicanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert mexican_peso.amount == decimal
        assert mexican_peso.numeric_code == '484'
        assert mexican_peso.alpha_code == 'MXN'
        assert mexican_peso.decimal_places == 2
        assert mexican_peso.decimal_sign == '.'
        assert mexican_peso.grouping_places == 3
        assert mexican_peso.grouping_sign == ','
        assert not mexican_peso.international
        assert mexican_peso.symbol == '$'
        assert mexican_peso.symbol_ahead
        assert mexican_peso.symbol_separator == ''
        assert mexican_peso.localized_symbol == 'MX$'
        assert mexican_peso.convertion == ''
        assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
        assert mexican_peso.__repr__() == (
            'MexicanPeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MXN", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MX$", '
            'numeric_code: "484", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert mexican_peso.__str__() == '$0.14'


    def test_mexican_peso_negative(self):
        """test_mexican_peso_negative."""
        amount = -100
        mexican_peso = MexicanPeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert mexican_peso.numeric_code == '484'
        assert mexican_peso.alpha_code == 'MXN'
        assert mexican_peso.decimal_places == 2
        assert mexican_peso.decimal_sign == '.'
        assert mexican_peso.grouping_places == 3
        assert mexican_peso.grouping_sign == ','
        assert not mexican_peso.international
        assert mexican_peso.symbol == '$'
        assert mexican_peso.symbol_ahead
        assert mexican_peso.symbol_separator == ''
        assert mexican_peso.localized_symbol == 'MX$'
        assert mexican_peso.convertion == ''
        assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
        assert mexican_peso.__repr__() == (
            'MexicanPeso(amount: -100, '
            'alpha_code: "MXN", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "MX$", '
            'numeric_code: "484", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert mexican_peso.__str__() == '$-100.00'


    def test_mexican_peso_custom(self):
        """test_mexican_peso_custom."""
        amount = 1000
        mexican_peso = MexicanPeso(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert mexican_peso.amount == decimal
        assert mexican_peso.numeric_code == '484'
        assert mexican_peso.alpha_code == 'MXN'
        assert mexican_peso.decimal_places == 5
        assert mexican_peso.decimal_sign == ','
        assert mexican_peso.grouping_places == 2
        assert mexican_peso.grouping_sign == '.'
        assert mexican_peso.international
        assert mexican_peso.symbol == '$'
        assert not mexican_peso.symbol_ahead
        assert mexican_peso.symbol_separator == '_'
        assert mexican_peso.localized_symbol == 'MX$'
        assert mexican_peso.convertion == ''
        assert mexican_peso.__hash__() == hash((decimal, 'MXN', '484'))
        assert mexican_peso.__repr__() == (
            'MexicanPeso(amount: 1000, '
            'alpha_code: "MXN", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "MX$", '
            'numeric_code: "484", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert mexican_peso.__str__() == 'MXN 10,00.00000'


    def test_mexican_peso_changed(self):
        """test_cmexican_peso_changed."""
        mexican_peso = MexicanPeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            mexican_peso.international = True


    def test_mexican_peso_math_add(self):
        """test_mexican_peso_math_add."""
        mexican_peso_one = MexicanPeso(amount=1)
        mexican_peso_two = MexicanPeso(amount=2)
        mexican_peso_three = MexicanPeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MXN and OTHER.'):
            _ = mexican_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.MexicanPeso\'> '
                    'and <class \'str\'>.')):
            _ = mexican_peso_one.__add__('1.00')
        assert (
            mexican_peso_one +
            mexican_peso_two) == mexican_peso_three


    def test_mexican_peso_slots(self):
        """test_mexican_peso_slots."""
        mexican_peso = MexicanPeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'MexicanPeso\' '
                    'object has no attribute \'new_variable\'')):
            mexican_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Philippine Peso representation."""

from multicurrency import PhilippinePeso


class TestPhilippinePeso:

    def test_philippine_peso(self):
        """test_philippine_peso."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        philippine_peso = PhilippinePeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert philippine_peso.amount == decimal
        assert philippine_peso.numeric_code == '608'
        assert philippine_peso.alpha_code == 'PHP'
        assert philippine_peso.decimal_places == 2
        assert philippine_peso.decimal_sign == '.'
        assert philippine_peso.grouping_places == 3
        assert philippine_peso.grouping_sign == ','
        assert not philippine_peso.international
        assert philippine_peso.symbol == '₱'
        assert philippine_peso.symbol_ahead
        assert philippine_peso.symbol_separator == ''
        assert philippine_peso.localized_symbol == '₱'
        assert philippine_peso.convertion == ''
        assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
        assert philippine_peso.__repr__() == (
            'PhilippinePeso(amount: 0.1428571428571428571428571429, '
            'alpha_code: "PHP", '
            'symbol: "₱", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₱", '
            'numeric_code: "608", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert philippine_peso.__str__() == '₱0.14'


    def test_philippine_peso_negative(self):
        """test_philippine_peso_negative."""
        amount = -100
        philippine_peso = PhilippinePeso(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert philippine_peso.numeric_code == '608'
        assert philippine_peso.alpha_code == 'PHP'
        assert philippine_peso.decimal_places == 2
        assert philippine_peso.decimal_sign == '.'
        assert philippine_peso.grouping_places == 3
        assert philippine_peso.grouping_sign == ','
        assert not philippine_peso.international
        assert philippine_peso.symbol == '₱'
        assert philippine_peso.symbol_ahead
        assert philippine_peso.symbol_separator == ''
        assert philippine_peso.localized_symbol == '₱'
        assert philippine_peso.convertion == ''
        assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
        assert philippine_peso.__repr__() == (
            'PhilippinePeso(amount: -100, '
            'alpha_code: "PHP", '
            'symbol: "₱", '
            'symbol_ahead: True, '
            'symbol_separator: "", '
            'localized_symbol: "₱", '
            'numeric_code: "608", '
            'decimal_places: "2", '
            'decimal_sign: ".", '
            'grouping_places: "3", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: False)')
        assert philippine_peso.__str__() == '₱-100.00'


    def test_philippine_peso_custom(self):
        """test_philippine_peso_custom."""
        amount = 1000
        philippine_peso = PhilippinePeso(
            amount=amount,
            decimal_places=5,
            decimal_sign=',',
            grouping_places=2,
            grouping_sign='.',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert philippine_peso.amount == decimal
        assert philippine_peso.numeric_code == '608'
        assert philippine_peso.alpha_code == 'PHP'
        assert philippine_peso.decimal_places == 5
        assert philippine_peso.decimal_sign == ','
        assert philippine_peso.grouping_places == 2
        assert philippine_peso.grouping_sign == '.'
        assert philippine_peso.international
        assert philippine_peso.symbol == '₱'
        assert not philippine_peso.symbol_ahead
        assert philippine_peso.symbol_separator == '_'
        assert philippine_peso.localized_symbol == '₱'
        assert philippine_peso.convertion == ''
        assert philippine_peso.__hash__() == hash((decimal, 'PHP', '608'))
        assert philippine_peso.__repr__() == (
            'PhilippinePeso(amount: 1000, '
            'alpha_code: "PHP", '
            'symbol: "₱", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "₱", '
            'numeric_code: "608", '
            'decimal_places: "5", '
            'decimal_sign: ",", '
            'grouping_places: "2", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: True)')
        assert philippine_peso.__str__() == 'PHP 10,00.00000'


    def test_philippine_peso_changed(self):
        """test_cphilippine_peso_changed."""
        philippine_peso = PhilippinePeso(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            philippine_peso.international = True


    def test_philippine_peso_math_add(self):
        """test_philippine_peso_math_add."""
        philippine_peso_one = PhilippinePeso(amount=1)
        philippine_peso_two = PhilippinePeso(amount=2)
        philippine_peso_three = PhilippinePeso(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency PHP and OTHER.'):
            _ = philippine_peso_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.PhilippinePeso\'> '
                    'and <class \'str\'>.')):
            _ = philippine_peso_one.__add__('1.00')
        assert (
            philippine_peso_one +
            philippine_peso_two) == philippine_peso_three


    def test_philippine_peso_slots(self):
        """test_philippine_peso_slots."""
        philippine_peso = PhilippinePeso(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PhilippinePeso\' '
                    'object has no attribute \'new_variable\'')):
            philippine_peso.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Peso Uruguayo representation."""

from multicurrency import PesoUruguayo


class TestPesoUruguayo:

    def test_peso_uruguayo(self):
        """test_peso_uruguayo."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        peso_uruguayo = PesoUruguayo(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert peso_uruguayo.amount == decimal
        assert peso_uruguayo.numeric_code == '858'
        assert peso_uruguayo.alpha_code == 'UYU'
        assert peso_uruguayo.decimal_places == 2
        assert peso_uruguayo.decimal_sign == ','
        assert peso_uruguayo.grouping_places == 3
        assert peso_uruguayo.grouping_sign == '.'
        assert not peso_uruguayo.international
        assert peso_uruguayo.symbol == '$'
        assert peso_uruguayo.symbol_ahead
        assert peso_uruguayo.symbol_separator == '\u00A0'
        assert peso_uruguayo.localized_symbol == 'UY$'
        assert peso_uruguayo.convertion == ''
        assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
        assert peso_uruguayo.__repr__() == (
            'PesoUruguayo(amount: 0.1428571428571428571428571429, '
            'alpha_code: "UYU", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "UY$", '
            'numeric_code: "858", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert peso_uruguayo.__str__() == '$ 0,14'


    def test_peso_uruguayo_negative(self):
        """test_peso_uruguayo_negative."""
        amount = -100
        peso_uruguayo = PesoUruguayo(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert peso_uruguayo.numeric_code == '858'
        assert peso_uruguayo.alpha_code == 'UYU'
        assert peso_uruguayo.decimal_places == 2
        assert peso_uruguayo.decimal_sign == ','
        assert peso_uruguayo.grouping_places == 3
        assert peso_uruguayo.grouping_sign == '.'
        assert not peso_uruguayo.international
        assert peso_uruguayo.symbol == '$'
        assert peso_uruguayo.symbol_ahead
        assert peso_uruguayo.symbol_separator == '\u00A0'
        assert peso_uruguayo.localized_symbol == 'UY$'
        assert peso_uruguayo.convertion == ''
        assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
        assert peso_uruguayo.__repr__() == (
            'PesoUruguayo(amount: -100, '
            'alpha_code: "UYU", '
            'symbol: "$", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "UY$", '
            'numeric_code: "858", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert peso_uruguayo.__str__() == '$ -100,00'


    def test_peso_uruguayo_custom(self):
        """test_peso_uruguayo_custom."""
        amount = 1000
        peso_uruguayo = PesoUruguayo(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert peso_uruguayo.amount == decimal
        assert peso_uruguayo.numeric_code == '858'
        assert peso_uruguayo.alpha_code == 'UYU'
        assert peso_uruguayo.decimal_places == 5
        assert peso_uruguayo.decimal_sign == '.'
        assert peso_uruguayo.grouping_places == 2
        assert peso_uruguayo.grouping_sign == ','
        assert peso_uruguayo.international
        assert peso_uruguayo.symbol == '$'
        assert not peso_uruguayo.symbol_ahead
        assert peso_uruguayo.symbol_separator == '_'
        assert peso_uruguayo.localized_symbol == 'UY$'
        assert peso_uruguayo.convertion == ''
        assert peso_uruguayo.__hash__() == hash((decimal, 'UYU', '858'))
        assert peso_uruguayo.__repr__() == (
            'PesoUruguayo(amount: 1000, '
            'alpha_code: "UYU", '
            'symbol: "$", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "UY$", '
            'numeric_code: "858", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert peso_uruguayo.__str__() == 'UYU 10,00.00000'


    def test_peso_uruguayo_changed(self):
        """test_cpeso_uruguayo_changed."""
        peso_uruguayo = PesoUruguayo(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            peso_uruguayo.international = True


    def test_peso_uruguayo_math_add(self):
        """test_peso_uruguayo_math_add."""
        peso_uruguayo_one = PesoUruguayo(amount=1)
        peso_uruguayo_two = PesoUruguayo(amount=2)
        peso_uruguayo_three = PesoUruguayo(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency UYU and OTHER.'):
            _ = peso_uruguayo_one + currency
        with raises(
                CurrencyTypeException,
                match=('unsupported operation between <class \'multicurrency.'
                    'peso.PesoUruguayo\'> '
                    'and <class \'str\'>.')):
            _ = peso_uruguayo_one.__add__('1.00')
        assert (
            peso_uruguayo_one +
            peso_uruguayo_two) == peso_uruguayo_three


    def test_peso_uruguayo_slots(self):
        """test_peso_uruguayo_slots."""
        peso_uruguayo = PesoUruguayo(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'PesoUruguayo\' '
                    'object has no attribute \'new_variable\'')):
            peso_uruguayo.new_variable = 'fail'  # pylint: disable=assigning-non-slot
