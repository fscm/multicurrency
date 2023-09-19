# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dram currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dram import ArmenianDram


class TestArmenianDram:
    """Armenian Dram currency tests."""

    armenian_dram_minus_one = ArmenianDram(-1)
    armenian_dram_one_other = ArmenianDram(1)
    armenian_dram_one = ArmenianDram(1)
    armenian_dram_two = ArmenianDram(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Դ'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Դ'),
        (10, '10', '10,00\xa0Դ'),
        (Decimal('10'), '10', '10,00\xa0Դ'),
        ('-3.14', '-3.14', '-3,14\xa0Դ'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Դ'),
        (-10, '-10', '-10,00\xa0Դ'),
        (Decimal('-10'), '-10', '-10,00\xa0Դ')
    ])
    def test_armenian_dram_default(amount, result, printed):
        default = ArmenianDram(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AMD'
        assert default.numeric_code == '051'
        assert default.symbol == 'Դ'
        assert default.localized_symbol == 'Դ'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AMD',
            '051'))
        assert default.__repr__() == (
            'ArmenianDram('
            f'amount: {result}, '
            'alpha_code: "AMD", '
            'numeric_code: "051", '
            'symbol: "Դ", '
            'localized_symbol: "Դ", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Դ10.00,00000'),
        (-1000, 'Դ10.00,00000-')
    ])
    def test_armenian_dram_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ArmenianDram(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AMD'
        assert custom.numeric_code == '051'
        assert custom.symbol == 'Դ'
        assert custom.localized_symbol == 'Դ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AMD',
            '051'))
        assert custom.__repr__() == (
            'ArmenianDram('
            f'amount: {amount}, '
            'alpha_code: "AMD", '
            'numeric_code: "051", '
            'symbol: "Դ", '
            'localized_symbol: "Դ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_armenian_dram_recreate(amount, new_amount):
        default = ArmenianDram(amount)
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
    def test_armenian_dram_change_attributes(attribute, value):
        immutable = ArmenianDram(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ArmenianDram\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_armenian_dram_add_attributes(attribute, value):
        immutable = ArmenianDram(1000)
        with raises(
                AttributeError,
                match=f'\'ArmenianDram\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (armenian_dram_one, armenian_dram_one, armenian_dram_two, None),
        (armenian_dram_one, armenian_dram_one_other, armenian_dram_two, None),
        (armenian_dram_two, armenian_dram_minus_one, armenian_dram_one, None),
        (armenian_dram_one, other, None, CurrencyMismatchException),
        (armenian_dram_one, 1.00, None, CurrencyTypeException),
        (armenian_dram_one, '1.00', None, CurrencyTypeException)
    ])
    def test_armenian_dram_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (armenian_dram_one)
    ])
    def test_armenian_dram_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AMD'
        assert new.numeric_code == '051'
        assert new.symbol == 'Դ'
        assert new.localized_symbol == 'Դ'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
