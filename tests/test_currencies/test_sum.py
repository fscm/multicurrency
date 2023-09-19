# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Sum currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.sum import UzbekistanSum


class TestUzbekistanSum:
    """Uzbekistan Sum currency tests."""

    uzbekistan_sum_minus_one = UzbekistanSum(-1)
    uzbekistan_sum_one_other = UzbekistanSum(1)
    uzbekistan_sum_one = UzbekistanSum(1)
    uzbekistan_sum_two = UzbekistanSum(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0сўм'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0сўм'),
        (10, '10', '10,00\xa0сўм'),
        (Decimal('10'), '10', '10,00\xa0сўм'),
        ('-3.14', '-3.14', '-3,14\xa0сўм'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0сўм'),
        (-10, '-10', '-10,00\xa0сўм'),
        (Decimal('-10'), '-10', '-10,00\xa0сўм')
    ])
    def test_uzbekistan_sum_default(amount, result, printed):
        default = UzbekistanSum(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'UZS'
        assert default.numeric_code == '860'
        assert default.symbol == 'сўм'
        assert default.localized_symbol == 'сўм'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'UZS',
            '860'))
        assert default.__repr__() == (
            'UzbekistanSum('
            f'amount: {result}, '
            'alpha_code: "UZS", '
            'numeric_code: "860", '
            'symbol: "сўм", '
            'localized_symbol: "сўм", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'сўм10.00,00000'),
        (-1000, 'сўм10.00,00000-')
    ])
    def test_uzbekistan_sum_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = UzbekistanSum(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'UZS'
        assert custom.numeric_code == '860'
        assert custom.symbol == 'сўм'
        assert custom.localized_symbol == 'сўм'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'UZS',
            '860'))
        assert custom.__repr__() == (
            'UzbekistanSum('
            f'amount: {amount}, '
            'alpha_code: "UZS", '
            'numeric_code: "860", '
            'symbol: "сўм", '
            'localized_symbol: "сўм", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_uzbekistan_sum_recreate(amount, new_amount):
        default = UzbekistanSum(amount)
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
    def test_uzbekistan_sum_change_attributes(attribute, value):
        immutable = UzbekistanSum(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'UzbekistanSum\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_uzbekistan_sum_add_attributes(attribute, value):
        immutable = UzbekistanSum(1000)
        with raises(
                AttributeError,
                match=f'\'UzbekistanSum\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (uzbekistan_sum_one, uzbekistan_sum_one, uzbekistan_sum_two, None),
        (uzbekistan_sum_one, uzbekistan_sum_one_other, uzbekistan_sum_two, None),
        (uzbekistan_sum_two, uzbekistan_sum_minus_one, uzbekistan_sum_one, None),
        (uzbekistan_sum_one, other, None, CurrencyMismatchException),
        (uzbekistan_sum_one, 1.00, None, CurrencyTypeException),
        (uzbekistan_sum_one, '1.00', None, CurrencyTypeException)
    ])
    def test_uzbekistan_sum_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (uzbekistan_sum_one)
    ])
    def test_uzbekistan_sum_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'UZS'
        assert new.numeric_code == '860'
        assert new.symbol == 'сўм'
        assert new.localized_symbol == 'сўм'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
