# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Peso currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.peso import (
    ArgentinePeso,
    ChileanPeso,
    ColombianPeso,
    CubanPeso,
    DominicanPeso,
    MexicanPeso,
    PhilippinePeso,
    PesoUruguayo)


class TestArgentinePeso:
    """Argentine Peso currency tests."""

    argentine_peso_minus_one = ArgentinePeso(-1)
    argentine_peso_one_other = ArgentinePeso(1)
    argentine_peso_one = ArgentinePeso(1)
    argentine_peso_two = ArgentinePeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_argentine_peso_default(amount, result, printed):
        default = ArgentinePeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ARS'
        assert default.numeric_code == '032'
        assert default.symbol == '$'
        assert default.localized_symbol == 'AR$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ARS',
            '032'))
        assert default.__repr__() == (
            'ArgentinePeso('
            f'amount: {result}, '
            'alpha_code: "ARS", '
            'numeric_code: "032", '
            'symbol: "$", '
            'localized_symbol: "AR$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_argentine_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ArgentinePeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ARS'
        assert custom.numeric_code == '032'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'AR$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ARS',
            '032'))
        assert custom.__repr__() == (
            'ArgentinePeso('
            f'amount: {amount}, '
            'alpha_code: "ARS", '
            'numeric_code: "032", '
            'symbol: "$", '
            'localized_symbol: "AR$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_argentine_peso_recreate(amount, new_amount):
        default = ArgentinePeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_argentine_peso_change_attributes(attribute, value):
        immutable = ArgentinePeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ArgentinePeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_argentine_peso_add_attributes(attribute, value):
        immutable = ArgentinePeso(1000)
        with raises(
                AttributeError,
                match=f'\'ArgentinePeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (argentine_peso_one, argentine_peso_one, argentine_peso_two, None),
        (argentine_peso_one, argentine_peso_one_other, argentine_peso_two, None),
        (argentine_peso_two, argentine_peso_minus_one, argentine_peso_one, None),
        (argentine_peso_one, other, None, CurrencyMismatchException),
        (argentine_peso_one, 1.00, None, CurrencyTypeException),
        (argentine_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_argentine_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (argentine_peso_one)
    ])
    def test_argentine_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ARS'
        assert new.numeric_code == '032'
        assert new.symbol == '$'
        assert new.localized_symbol == 'AR$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestChileanPeso:
    """Chilean Peso currency tests."""

    chilean_peso_minus_one = ChileanPeso(-1)
    chilean_peso_one_other = ChileanPeso(1)
    chilean_peso_one = ChileanPeso(1)
    chilean_peso_two = ChileanPeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3'),
        (10, '10', '$10'),
        (Decimal('10'), '10', '$10'),
        ('-3.14', '-3.14', '-$3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3'),
        (-10, '-10', '-$10'),
        (Decimal('-10'), '-10', '-$10')
    ])
    def test_chilean_peso_default(amount, result, printed):
        default = ChileanPeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CLP'
        assert default.numeric_code == '152'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CL$'
        assert default.convertion == ''
        assert default.pattern == '0,.3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CLP',
            '152'))
        assert default.__repr__() == (
            'ChileanPeso('
            f'amount: {result}, '
            'alpha_code: "CLP", '
            'numeric_code: "152", '
            'symbol: "$", '
            'localized_symbol: "CL$", '
            'convertion: "", '
            'pattern: "0,.3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_chilean_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ChileanPeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CLP'
        assert custom.numeric_code == '152'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CL$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CLP',
            '152'))
        assert custom.__repr__() == (
            'ChileanPeso('
            f'amount: {amount}, '
            'alpha_code: "CLP", '
            'numeric_code: "152", '
            'symbol: "$", '
            'localized_symbol: "CL$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_chilean_peso_recreate(amount, new_amount):
        default = ChileanPeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_chilean_peso_change_attributes(attribute, value):
        immutable = ChileanPeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ChileanPeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_chilean_peso_add_attributes(attribute, value):
        immutable = ChileanPeso(1000)
        with raises(
                AttributeError,
                match=f'\'ChileanPeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (chilean_peso_one, chilean_peso_one, chilean_peso_two, None),
        (chilean_peso_one, chilean_peso_one_other, chilean_peso_two, None),
        (chilean_peso_two, chilean_peso_minus_one, chilean_peso_one, None),
        (chilean_peso_one, other, None, CurrencyMismatchException),
        (chilean_peso_one, 1.00, None, CurrencyTypeException),
        (chilean_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_chilean_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (chilean_peso_one)
    ])
    def test_chilean_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CLP'
        assert new.numeric_code == '152'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CL$'
        assert new.convertion == ''
        assert new.pattern == '0,.3%-%s%u'


class TestColombianPeso:
    """Colombian Peso currency tests."""

    colombian_peso_minus_one = ColombianPeso(-1)
    colombian_peso_one_other = ColombianPeso(1)
    colombian_peso_one = ColombianPeso(1)
    colombian_peso_two = ColombianPeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_colombian_peso_default(amount, result, printed):
        default = ColombianPeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'COP'
        assert default.numeric_code == '170'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CO$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'COP',
            '170'))
        assert default.__repr__() == (
            'ColombianPeso('
            f'amount: {result}, '
            'alpha_code: "COP", '
            'numeric_code: "170", '
            'symbol: "$", '
            'localized_symbol: "CO$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_colombian_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ColombianPeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'COP'
        assert custom.numeric_code == '170'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CO$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'COP',
            '170'))
        assert custom.__repr__() == (
            'ColombianPeso('
            f'amount: {amount}, '
            'alpha_code: "COP", '
            'numeric_code: "170", '
            'symbol: "$", '
            'localized_symbol: "CO$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_colombian_peso_recreate(amount, new_amount):
        default = ColombianPeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_colombian_peso_change_attributes(attribute, value):
        immutable = ColombianPeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ColombianPeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_colombian_peso_add_attributes(attribute, value):
        immutable = ColombianPeso(1000)
        with raises(
                AttributeError,
                match=f'\'ColombianPeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (colombian_peso_one, colombian_peso_one, colombian_peso_two, None),
        (colombian_peso_one, colombian_peso_one_other, colombian_peso_two, None),
        (colombian_peso_two, colombian_peso_minus_one, colombian_peso_one, None),
        (colombian_peso_one, other, None, CurrencyMismatchException),
        (colombian_peso_one, 1.00, None, CurrencyTypeException),
        (colombian_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_colombian_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (colombian_peso_one)
    ])
    def test_colombian_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'COP'
        assert new.numeric_code == '170'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CO$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestCubanPeso:
    """Cuban Peso currency tests."""

    cuban_peso_minus_one = CubanPeso(-1)
    cuban_peso_one_other = CubanPeso(1)
    cuban_peso_one = CubanPeso(1)
    cuban_peso_two = CubanPeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_cuban_peso_default(amount, result, printed):
        default = CubanPeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CUP'
        assert default.numeric_code == '192'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CU$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CUP',
            '192'))
        assert default.__repr__() == (
            'CubanPeso('
            f'amount: {result}, '
            'alpha_code: "CUP", '
            'numeric_code: "192", '
            'symbol: "$", '
            'localized_symbol: "CU$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_cuban_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CubanPeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CUP'
        assert custom.numeric_code == '192'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CU$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CUP',
            '192'))
        assert custom.__repr__() == (
            'CubanPeso('
            f'amount: {amount}, '
            'alpha_code: "CUP", '
            'numeric_code: "192", '
            'symbol: "$", '
            'localized_symbol: "CU$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cuban_peso_recreate(amount, new_amount):
        default = CubanPeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_cuban_peso_change_attributes(attribute, value):
        immutable = CubanPeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CubanPeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cuban_peso_add_attributes(attribute, value):
        immutable = CubanPeso(1000)
        with raises(
                AttributeError,
                match=f'\'CubanPeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cuban_peso_one, cuban_peso_one, cuban_peso_two, None),
        (cuban_peso_one, cuban_peso_one_other, cuban_peso_two, None),
        (cuban_peso_two, cuban_peso_minus_one, cuban_peso_one, None),
        (cuban_peso_one, other, None, CurrencyMismatchException),
        (cuban_peso_one, 1.00, None, CurrencyTypeException),
        (cuban_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cuban_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cuban_peso_one)
    ])
    def test_cuban_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CUP'
        assert new.numeric_code == '192'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CU$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestDominicanPeso:
    """Dominican Peso currency tests."""

    dominican_peso_minus_one = DominicanPeso(-1)
    dominican_peso_one_other = DominicanPeso(1)
    dominican_peso_one = DominicanPeso(1)
    dominican_peso_two = DominicanPeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_dominican_peso_default(amount, result, printed):
        default = DominicanPeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'DOP'
        assert default.numeric_code == '214'
        assert default.symbol == '$'
        assert default.localized_symbol == 'DO$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'DOP',
            '214'))
        assert default.__repr__() == (
            'DominicanPeso('
            f'amount: {result}, '
            'alpha_code: "DOP", '
            'numeric_code: "214", '
            'symbol: "$", '
            'localized_symbol: "DO$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_dominican_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = DominicanPeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'DOP'
        assert custom.numeric_code == '214'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'DO$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'DOP',
            '214'))
        assert custom.__repr__() == (
            'DominicanPeso('
            f'amount: {amount}, '
            'alpha_code: "DOP", '
            'numeric_code: "214", '
            'symbol: "$", '
            'localized_symbol: "DO$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_dominican_peso_recreate(amount, new_amount):
        default = DominicanPeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_dominican_peso_change_attributes(attribute, value):
        immutable = DominicanPeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'DominicanPeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_dominican_peso_add_attributes(attribute, value):
        immutable = DominicanPeso(1000)
        with raises(
                AttributeError,
                match=f'\'DominicanPeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (dominican_peso_one, dominican_peso_one, dominican_peso_two, None),
        (dominican_peso_one, dominican_peso_one_other, dominican_peso_two, None),
        (dominican_peso_two, dominican_peso_minus_one, dominican_peso_one, None),
        (dominican_peso_one, other, None, CurrencyMismatchException),
        (dominican_peso_one, 1.00, None, CurrencyTypeException),
        (dominican_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_dominican_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (dominican_peso_one)
    ])
    def test_dominican_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'DOP'
        assert new.numeric_code == '214'
        assert new.symbol == '$'
        assert new.localized_symbol == 'DO$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestMexicanPeso:
    """Mexican Peso currency tests."""

    mexican_peso_minus_one = MexicanPeso(-1)
    mexican_peso_one_other = MexicanPeso(1)
    mexican_peso_one = MexicanPeso(1)
    mexican_peso_two = MexicanPeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_mexican_peso_default(amount, result, printed):
        default = MexicanPeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MXN'
        assert default.numeric_code == '484'
        assert default.symbol == '$'
        assert default.localized_symbol == 'MX$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MXN',
            '484'))
        assert default.__repr__() == (
            'MexicanPeso('
            f'amount: {result}, '
            'alpha_code: "MXN", '
            'numeric_code: "484", '
            'symbol: "$", '
            'localized_symbol: "MX$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_mexican_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MexicanPeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MXN'
        assert custom.numeric_code == '484'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'MX$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MXN',
            '484'))
        assert custom.__repr__() == (
            'MexicanPeso('
            f'amount: {amount}, '
            'alpha_code: "MXN", '
            'numeric_code: "484", '
            'symbol: "$", '
            'localized_symbol: "MX$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_mexican_peso_recreate(amount, new_amount):
        default = MexicanPeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_mexican_peso_change_attributes(attribute, value):
        immutable = MexicanPeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MexicanPeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_mexican_peso_add_attributes(attribute, value):
        immutable = MexicanPeso(1000)
        with raises(
                AttributeError,
                match=f'\'MexicanPeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (mexican_peso_one, mexican_peso_one, mexican_peso_two, None),
        (mexican_peso_one, mexican_peso_one_other, mexican_peso_two, None),
        (mexican_peso_two, mexican_peso_minus_one, mexican_peso_one, None),
        (mexican_peso_one, other, None, CurrencyMismatchException),
        (mexican_peso_one, 1.00, None, CurrencyTypeException),
        (mexican_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_mexican_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (mexican_peso_one)
    ])
    def test_mexican_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MXN'
        assert new.numeric_code == '484'
        assert new.symbol == '$'
        assert new.localized_symbol == 'MX$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPhilippinePeso:
    """Philippine Peso currency tests."""

    philippine_peso_minus_one = PhilippinePeso(-1)
    philippine_peso_one_other = PhilippinePeso(1)
    philippine_peso_one = PhilippinePeso(1)
    philippine_peso_two = PhilippinePeso(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₱3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₱3.14'),
        (10, '10', '₱10.00'),
        (Decimal('10'), '10', '₱10.00'),
        ('-3.14', '-3.14', '-₱3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₱3.14'),
        (-10, '-10', '-₱10.00'),
        (Decimal('-10'), '-10', '-₱10.00')
    ])
    def test_philippine_peso_default(amount, result, printed):
        default = PhilippinePeso(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PHP'
        assert default.numeric_code == '608'
        assert default.symbol == '₱'
        assert default.localized_symbol == '₱'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PHP',
            '608'))
        assert default.__repr__() == (
            'PhilippinePeso('
            f'amount: {result}, '
            'alpha_code: "PHP", '
            'numeric_code: "608", '
            'symbol: "₱", '
            'localized_symbol: "₱", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₱10.00,00000'),
        (-1000, '₱10.00,00000-')
    ])
    def test_philippine_peso_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PhilippinePeso(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PHP'
        assert custom.numeric_code == '608'
        assert custom.symbol == '₱'
        assert custom.localized_symbol == '₱'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PHP',
            '608'))
        assert custom.__repr__() == (
            'PhilippinePeso('
            f'amount: {amount}, '
            'alpha_code: "PHP", '
            'numeric_code: "608", '
            'symbol: "₱", '
            'localized_symbol: "₱", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_philippine_peso_recreate(amount, new_amount):
        default = PhilippinePeso(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_philippine_peso_change_attributes(attribute, value):
        immutable = PhilippinePeso(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PhilippinePeso\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_philippine_peso_add_attributes(attribute, value):
        immutable = PhilippinePeso(1000)
        with raises(
                AttributeError,
                match=f'\'PhilippinePeso\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (philippine_peso_one, philippine_peso_one, philippine_peso_two, None),
        (philippine_peso_one, philippine_peso_one_other, philippine_peso_two, None),
        (philippine_peso_two, philippine_peso_minus_one, philippine_peso_one, None),
        (philippine_peso_one, other, None, CurrencyMismatchException),
        (philippine_peso_one, 1.00, None, CurrencyTypeException),
        (philippine_peso_one, '1.00', None, CurrencyTypeException)
    ])
    def test_philippine_peso_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (philippine_peso_one)
    ])
    def test_philippine_peso_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PHP'
        assert new.numeric_code == '608'
        assert new.symbol == '₱'
        assert new.localized_symbol == '₱'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPesoUruguayo:
    """Peso Uruguayo currency tests."""

    peso_uruguayo_minus_one = PesoUruguayo(-1)
    peso_uruguayo_one_other = PesoUruguayo(1)
    peso_uruguayo_one = PesoUruguayo(1)
    peso_uruguayo_two = PesoUruguayo(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_peso_uruguayo_default(amount, result, printed):
        default = PesoUruguayo(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'UYU'
        assert default.numeric_code == '858'
        assert default.symbol == '$'
        assert default.localized_symbol == 'UY$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'UYU',
            '858'))
        assert default.__repr__() == (
            'PesoUruguayo('
            f'amount: {result}, '
            'alpha_code: "UYU", '
            'numeric_code: "858", '
            'symbol: "$", '
            'localized_symbol: "UY$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_peso_uruguayo_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PesoUruguayo(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'UYU'
        assert custom.numeric_code == '858'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'UY$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'UYU',
            '858'))
        assert custom.__repr__() == (
            'PesoUruguayo('
            f'amount: {amount}, '
            'alpha_code: "UYU", '
            'numeric_code: "858", '
            'symbol: "$", '
            'localized_symbol: "UY$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_peso_uruguayo_recreate(amount, new_amount):
        default = PesoUruguayo(amount)
        new = default.__recreate__(new_amount)
        assert new is not default
        assert default.amount == amount
        assert new.amount == new_amount

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('amount', 999),
        ('alpha_code', 'EUR'),
        ('numeric_code', '978'),
        ('symbol', '€'),
        ('localized_symbol', 'PT€'),
        ('convertion', '0123456789-'),
        ('pattern', '2,.3%-%s%u')
    ])
    def test_peso_uruguayo_change_attributes(attribute, value):
        immutable = PesoUruguayo(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PesoUruguayo\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_peso_uruguayo_add_attributes(attribute, value):
        immutable = PesoUruguayo(1000)
        with raises(
                AttributeError,
                match=f'\'PesoUruguayo\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (peso_uruguayo_one, peso_uruguayo_one, peso_uruguayo_two, None),
        (peso_uruguayo_one, peso_uruguayo_one_other, peso_uruguayo_two, None),
        (peso_uruguayo_two, peso_uruguayo_minus_one, peso_uruguayo_one, None),
        (peso_uruguayo_one, other, None, CurrencyMismatchException),
        (peso_uruguayo_one, 1.00, None, CurrencyTypeException),
        (peso_uruguayo_one, '1.00', None, CurrencyTypeException)
    ])
    def test_peso_uruguayo_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (peso_uruguayo_one)
    ])
    def test_peso_uruguayo_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'UYU'
        assert new.numeric_code == '858'
        assert new.symbol == '$'
        assert new.localized_symbol == 'UY$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'
