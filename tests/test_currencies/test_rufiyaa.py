# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rufiyaa currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.rufiyaa import Rufiyaa


class TestRufiyaa:
    """Rufiyaa currency tests."""

    rufiyaa_minus_one = Rufiyaa(-1)
    rufiyaa_one_other = Rufiyaa(1)
    rufiyaa_one = Rufiyaa(1)
    rufiyaa_two = Rufiyaa(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ރ.\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ރ.\xa03.14'),
        (10, '10', 'ރ.\xa010.00'),
        (Decimal('10'), '10', 'ރ.\xa010.00'),
        ('-3.14', '-3.14', 'ރ.\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ރ.\xa0-3.14'),
        (-10, '-10', 'ރ.\xa0-10.00'),
        (Decimal('-10'), '-10', 'ރ.\xa0-10.00')
    ])
    def test_rufiyaa_default(amount, result, printed):
        default = Rufiyaa(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MVR'
        assert default.numeric_code == '462'
        assert default.symbol == 'ރ.'
        assert default.localized_symbol == 'ރ.'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MVR',
            '462'))
        assert default.__repr__() == (
            'Rufiyaa('
            f'amount: {result}, '
            'alpha_code: "MVR", '
            'numeric_code: "462", '
            'symbol: "ރ.", '
            'localized_symbol: "ރ.", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ރ.10.00,00000'),
        (-1000, 'ރ.10.00,00000-')
    ])
    def test_rufiyaa_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Rufiyaa(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MVR'
        assert custom.numeric_code == '462'
        assert custom.symbol == 'ރ.'
        assert custom.localized_symbol == 'ރ.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MVR',
            '462'))
        assert custom.__repr__() == (
            'Rufiyaa('
            f'amount: {amount}, '
            'alpha_code: "MVR", '
            'numeric_code: "462", '
            'symbol: "ރ.", '
            'localized_symbol: "ރ.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rufiyaa_recreate(amount, new_amount):
        default = Rufiyaa(amount)
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
    def test_rufiyaa_change_attributes(attribute, value):
        immutable = Rufiyaa(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Rufiyaa\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rufiyaa_add_attributes(attribute, value):
        immutable = Rufiyaa(1000)
        with raises(
                AttributeError,
                match=f'\'Rufiyaa\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rufiyaa_one, rufiyaa_one, rufiyaa_two, None),
        (rufiyaa_one, rufiyaa_one_other, rufiyaa_two, None),
        (rufiyaa_two, rufiyaa_minus_one, rufiyaa_one, None),
        (rufiyaa_one, other, None, CurrencyMismatchException),
        (rufiyaa_one, 1.00, None, CurrencyTypeException),
        (rufiyaa_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rufiyaa_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rufiyaa_one)
    ])
    def test_rufiyaa_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MVR'
        assert new.numeric_code == '462'
        assert new.symbol == 'ރ.'
        assert new.localized_symbol == 'ރ.'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
