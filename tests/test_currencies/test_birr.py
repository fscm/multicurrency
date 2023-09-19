# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Birr currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.birr import EthiopianBirr


class TestEthiopianBirr:
    """Ethiopian Birr currency tests."""

    ethiopian_birr_minus_one = EthiopianBirr(-1)
    ethiopian_birr_one_other = EthiopianBirr(1)
    ethiopian_birr_one = EthiopianBirr(1)
    ethiopian_birr_two = EthiopianBirr(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ብር\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ብር\xa03.14'),
        (10, '10', 'ብር\xa010.00'),
        (Decimal('10'), '10', 'ብር\xa010.00'),
        ('-3.14', '-3.14', 'ብር\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ብር\xa0-3.14'),
        (-10, '-10', 'ብር\xa0-10.00'),
        (Decimal('-10'), '-10', 'ብር\xa0-10.00')
    ])
    def test_ethiopian_birr_default(amount, result, printed):
        default = EthiopianBirr(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ETB'
        assert default.numeric_code == '230'
        assert default.symbol == 'ብር'
        assert default.localized_symbol == 'ብር'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ETB',
            '230'))
        assert default.__repr__() == (
            'EthiopianBirr('
            f'amount: {result}, '
            'alpha_code: "ETB", '
            'numeric_code: "230", '
            'symbol: "ብር", '
            'localized_symbol: "ብር", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ብር10.00,00000'),
        (-1000, 'ብር10.00,00000-')
    ])
    def test_ethiopian_birr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EthiopianBirr(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ETB'
        assert custom.numeric_code == '230'
        assert custom.symbol == 'ብር'
        assert custom.localized_symbol == 'ብር'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ETB',
            '230'))
        assert custom.__repr__() == (
            'EthiopianBirr('
            f'amount: {amount}, '
            'alpha_code: "ETB", '
            'numeric_code: "230", '
            'symbol: "ብር", '
            'localized_symbol: "ብር", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_ethiopian_birr_recreate(amount, new_amount):
        default = EthiopianBirr(amount)
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
    def test_ethiopian_birr_change_attributes(attribute, value):
        immutable = EthiopianBirr(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EthiopianBirr\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_ethiopian_birr_add_attributes(attribute, value):
        immutable = EthiopianBirr(1000)
        with raises(
                AttributeError,
                match=f'\'EthiopianBirr\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (ethiopian_birr_one, ethiopian_birr_one, ethiopian_birr_two, None),
        (ethiopian_birr_one, ethiopian_birr_one_other, ethiopian_birr_two, None),
        (ethiopian_birr_two, ethiopian_birr_minus_one, ethiopian_birr_one, None),
        (ethiopian_birr_one, other, None, CurrencyMismatchException),
        (ethiopian_birr_one, 1.00, None, CurrencyTypeException),
        (ethiopian_birr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_ethiopian_birr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (ethiopian_birr_one)
    ])
    def test_ethiopian_birr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ETB'
        assert new.numeric_code == '230'
        assert new.symbol == 'ብር'
        assert new.localized_symbol == 'ብር'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
