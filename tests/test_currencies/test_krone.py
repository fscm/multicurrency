# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Krone currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.krone import (
    DanishKrone,
    NorwegianKrone)


class TestDanishKrone:
    """Danish Krone currency tests."""

    danish_krone_minus_one = DanishKrone(-1)
    danish_krone_one_other = DanishKrone(1)
    danish_krone_one = DanishKrone(1)
    danish_krone_two = DanishKrone(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0kr'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0kr'),
        (10, '10', '10,00\xa0kr'),
        (Decimal('10'), '10', '10,00\xa0kr'),
        ('-3.14', '-3.14', '-3,14\xa0kr'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0kr'),
        (-10, '-10', '-10,00\xa0kr'),
        (Decimal('-10'), '-10', '-10,00\xa0kr')
    ])
    def test_danish_krone_default(amount, result, printed):
        default = DanishKrone(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'DKK'
        assert default.numeric_code == '208'
        assert default.symbol == 'kr'
        assert default.localized_symbol == 'kr'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'DKK',
            '208'))
        assert default.__repr__() == (
            'DanishKrone('
            f'amount: {result}, '
            'alpha_code: "DKK", '
            'numeric_code: "208", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'kr10.00,00000'),
        (-1000, 'kr10.00,00000-')
    ])
    def test_danish_krone_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = DanishKrone(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'DKK'
        assert custom.numeric_code == '208'
        assert custom.symbol == 'kr'
        assert custom.localized_symbol == 'kr'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'DKK',
            '208'))
        assert custom.__repr__() == (
            'DanishKrone('
            f'amount: {amount}, '
            'alpha_code: "DKK", '
            'numeric_code: "208", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_danish_krone_recreate(amount, new_amount):
        default = DanishKrone(amount)
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
    def test_danish_krone_change_attributes(attribute, value):
        immutable = DanishKrone(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'DanishKrone\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_danish_krone_add_attributes(attribute, value):
        immutable = DanishKrone(1000)
        with raises(
                AttributeError,
                match=f'\'DanishKrone\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (danish_krone_one, danish_krone_one, danish_krone_two, None),
        (danish_krone_one, danish_krone_one_other, danish_krone_two, None),
        (danish_krone_two, danish_krone_minus_one, danish_krone_one, None),
        (danish_krone_one, other, None, CurrencyMismatchException),
        (danish_krone_one, 1.00, None, CurrencyTypeException),
        (danish_krone_one, '1.00', None, CurrencyTypeException)
    ])
    def test_danish_krone_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (danish_krone_one)
    ])
    def test_danish_krone_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'DKK'
        assert new.numeric_code == '208'
        assert new.symbol == 'kr'
        assert new.localized_symbol == 'kr'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestNorwegianKrone:
    """Norwegian Krone currency tests."""

    norwegian_krone_minus_one = NorwegianKrone(-1)
    norwegian_krone_one_other = NorwegianKrone(1)
    norwegian_krone_one = NorwegianKrone(1)
    norwegian_krone_two = NorwegianKrone(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'kr\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'kr\xa03,14'),
        (10, '10', 'kr\xa010,00'),
        (Decimal('10'), '10', 'kr\xa010,00'),
        ('-3.14', '-3.14', 'kr\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'kr\xa0-3,14'),
        (-10, '-10', 'kr\xa0-10,00'),
        (Decimal('-10'), '-10', 'kr\xa0-10,00')
    ])
    def test_norwegian_krone_default(amount, result, printed):
        default = NorwegianKrone(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NOK'
        assert default.numeric_code == '578'
        assert default.symbol == 'kr'
        assert default.localized_symbol == 'kr'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NOK',
            '578'))
        assert default.__repr__() == (
            'NorwegianKrone('
            f'amount: {result}, '
            'alpha_code: "NOK", '
            'numeric_code: "578", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            'pattern: "2, 3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'kr10.00,00000'),
        (-1000, 'kr10.00,00000-')
    ])
    def test_norwegian_krone_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NorwegianKrone(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NOK'
        assert custom.numeric_code == '578'
        assert custom.symbol == 'kr'
        assert custom.localized_symbol == 'kr'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NOK',
            '578'))
        assert custom.__repr__() == (
            'NorwegianKrone('
            f'amount: {amount}, '
            'alpha_code: "NOK", '
            'numeric_code: "578", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_norwegian_krone_recreate(amount, new_amount):
        default = NorwegianKrone(amount)
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
    def test_norwegian_krone_change_attributes(attribute, value):
        immutable = NorwegianKrone(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NorwegianKrone\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_norwegian_krone_add_attributes(attribute, value):
        immutable = NorwegianKrone(1000)
        with raises(
                AttributeError,
                match=f'\'NorwegianKrone\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (norwegian_krone_one, norwegian_krone_one, norwegian_krone_two, None),
        (norwegian_krone_one, norwegian_krone_one_other, norwegian_krone_two, None),
        (norwegian_krone_two, norwegian_krone_minus_one, norwegian_krone_one, None),
        (norwegian_krone_one, other, None, CurrencyMismatchException),
        (norwegian_krone_one, 1.00, None, CurrencyTypeException),
        (norwegian_krone_one, '1.00', None, CurrencyTypeException)
    ])
    def test_norwegian_krone_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (norwegian_krone_one)
    ])
    def test_norwegian_krone_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NOK'
        assert new.numeric_code == '578'
        assert new.symbol == 'kr'
        assert new.localized_symbol == 'kr'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%s\u00A0%a'
