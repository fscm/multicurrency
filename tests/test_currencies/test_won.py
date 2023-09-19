# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Won currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.won import (
    NorthKoreanWon,
    SouthKoreanWon)


class TestNorthKoreanWon:
    """North Korean Won currency tests."""

    north_korean_won_minus_one = NorthKoreanWon(-1)
    north_korean_won_one_other = NorthKoreanWon(1)
    north_korean_won_one = NorthKoreanWon(1)
    north_korean_won_two = NorthKoreanWon(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₩\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₩\xa03.14'),
        (10, '10', '₩\xa010.00'),
        (Decimal('10'), '10', '₩\xa010.00'),
        ('-3.14', '-3.14', '₩\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₩\xa0-3.14'),
        (-10, '-10', '₩\xa0-10.00'),
        (Decimal('-10'), '-10', '₩\xa0-10.00')
    ])
    def test_north_korean_won_default(amount, result, printed):
        default = NorthKoreanWon(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KPW'
        assert default.numeric_code == '408'
        assert default.symbol == '₩'
        assert default.localized_symbol == '₩'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KPW',
            '408'))
        assert default.__repr__() == (
            'NorthKoreanWon('
            f'amount: {result}, '
            'alpha_code: "KPW", '
            'numeric_code: "408", '
            'symbol: "₩", '
            'localized_symbol: "₩", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₩10.00,00000'),
        (-1000, '₩10.00,00000-')
    ])
    def test_north_korean_won_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NorthKoreanWon(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KPW'
        assert custom.numeric_code == '408'
        assert custom.symbol == '₩'
        assert custom.localized_symbol == '₩'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KPW',
            '408'))
        assert custom.__repr__() == (
            'NorthKoreanWon('
            f'amount: {amount}, '
            'alpha_code: "KPW", '
            'numeric_code: "408", '
            'symbol: "₩", '
            'localized_symbol: "₩", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_north_korean_won_recreate(amount, new_amount):
        default = NorthKoreanWon(amount)
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
    def test_north_korean_won_change_attributes(attribute, value):
        immutable = NorthKoreanWon(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NorthKoreanWon\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_north_korean_won_add_attributes(attribute, value):
        immutable = NorthKoreanWon(1000)
        with raises(
                AttributeError,
                match=f'\'NorthKoreanWon\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (north_korean_won_one, north_korean_won_one, north_korean_won_two, None),
        (north_korean_won_one, north_korean_won_one_other, north_korean_won_two, None),
        (north_korean_won_two, north_korean_won_minus_one, north_korean_won_one, None),
        (north_korean_won_one, other, None, CurrencyMismatchException),
        (north_korean_won_one, 1.00, None, CurrencyTypeException),
        (north_korean_won_one, '1.00', None, CurrencyTypeException)
    ])
    def test_north_korean_won_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (north_korean_won_one)
    ])
    def test_north_korean_won_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KPW'
        assert new.numeric_code == '408'
        assert new.symbol == '₩'
        assert new.localized_symbol == '₩'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestSouthKoreanWon:
    """South Korean Won currency tests."""

    south_korean_won_minus_one = SouthKoreanWon(-1)
    south_korean_won_one_other = SouthKoreanWon(1)
    south_korean_won_one = SouthKoreanWon(1)
    south_korean_won_two = SouthKoreanWon(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₩3'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₩3'),
        (10, '10', '₩10'),
        (Decimal('10'), '10', '₩10'),
        ('-3.14', '-3.14', '-₩3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₩3'),
        (-10, '-10', '-₩10'),
        (Decimal('-10'), '-10', '-₩10')
    ])
    def test_south_korean_won_default(amount, result, printed):
        default = SouthKoreanWon(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KRW'
        assert default.numeric_code == '410'
        assert default.symbol == '₩'
        assert default.localized_symbol == '₩'
        assert default.convertion == ''
        assert default.pattern == '0.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KRW',
            '410'))
        assert default.__repr__() == (
            'SouthKoreanWon('
            f'amount: {result}, '
            'alpha_code: "KRW", '
            'numeric_code: "410", '
            'symbol: "₩", '
            'localized_symbol: "₩", '
            'convertion: "", '
            'pattern: "0.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₩10.00,00000'),
        (-1000, '₩10.00,00000-')
    ])
    def test_south_korean_won_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SouthKoreanWon(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KRW'
        assert custom.numeric_code == '410'
        assert custom.symbol == '₩'
        assert custom.localized_symbol == '₩'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KRW',
            '410'))
        assert custom.__repr__() == (
            'SouthKoreanWon('
            f'amount: {amount}, '
            'alpha_code: "KRW", '
            'numeric_code: "410", '
            'symbol: "₩", '
            'localized_symbol: "₩", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_south_korean_won_recreate(amount, new_amount):
        default = SouthKoreanWon(amount)
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
    def test_south_korean_won_change_attributes(attribute, value):
        immutable = SouthKoreanWon(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SouthKoreanWon\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_south_korean_won_add_attributes(attribute, value):
        immutable = SouthKoreanWon(1000)
        with raises(
                AttributeError,
                match=f'\'SouthKoreanWon\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (south_korean_won_one, south_korean_won_one, south_korean_won_two, None),
        (south_korean_won_one, south_korean_won_one_other, south_korean_won_two, None),
        (south_korean_won_two, south_korean_won_minus_one, south_korean_won_one, None),
        (south_korean_won_one, other, None, CurrencyMismatchException),
        (south_korean_won_one, 1.00, None, CurrencyTypeException),
        (south_korean_won_one, '1.00', None, CurrencyTypeException)
    ])
    def test_south_korean_won_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (south_korean_won_one)
    ])
    def test_south_korean_won_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KRW'
        assert new.numeric_code == '410'
        assert new.symbol == '₩'
        assert new.localized_symbol == '₩'
        assert new.convertion == ''
        assert new.pattern == '0.,3%-%s%u'
