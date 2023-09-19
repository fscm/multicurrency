# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Real currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.real import BrazilianReal


class TestBrazilianReal:
    """Brazilian Real currency tests."""

    brazilian_real_minus_one = BrazilianReal(-1)
    brazilian_real_one_other = BrazilianReal(1)
    brazilian_real_one = BrazilianReal(1)
    brazilian_real_two = BrazilianReal(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'R$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'R$\xa03,14'),
        (10, '10', 'R$\xa010,00'),
        (Decimal('10'), '10', 'R$\xa010,00'),
        ('-3.14', '-3.14', 'R$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'R$\xa0-3,14'),
        (-10, '-10', 'R$\xa0-10,00'),
        (Decimal('-10'), '-10', 'R$\xa0-10,00')
    ])
    def test_brazilian_real_default(amount, result, printed):
        default = BrazilianReal(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BRL'
        assert default.numeric_code == '986'
        assert default.symbol == 'R$'
        assert default.localized_symbol == 'R$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BRL',
            '986'))
        assert default.__repr__() == (
            'BrazilianReal('
            f'amount: {result}, '
            'alpha_code: "BRL", '
            'numeric_code: "986", '
            'symbol: "R$", '
            'localized_symbol: "R$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'R$10.00,00000'),
        (-1000, 'R$10.00,00000-')
    ])
    def test_brazilian_real_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BrazilianReal(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BRL'
        assert custom.numeric_code == '986'
        assert custom.symbol == 'R$'
        assert custom.localized_symbol == 'R$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BRL',
            '986'))
        assert custom.__repr__() == (
            'BrazilianReal('
            f'amount: {amount}, '
            'alpha_code: "BRL", '
            'numeric_code: "986", '
            'symbol: "R$", '
            'localized_symbol: "R$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_brazilian_real_recreate(amount, new_amount):
        default = BrazilianReal(amount)
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
    def test_brazilian_real_change_attributes(attribute, value):
        immutable = BrazilianReal(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BrazilianReal\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_brazilian_real_add_attributes(attribute, value):
        immutable = BrazilianReal(1000)
        with raises(
                AttributeError,
                match=f'\'BrazilianReal\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (brazilian_real_one, brazilian_real_one, brazilian_real_two, None),
        (brazilian_real_one, brazilian_real_one_other, brazilian_real_two, None),
        (brazilian_real_two, brazilian_real_minus_one, brazilian_real_one, None),
        (brazilian_real_one, other, None, CurrencyMismatchException),
        (brazilian_real_one, 1.00, None, CurrencyTypeException),
        (brazilian_real_one, '1.00', None, CurrencyTypeException)
    ])
    def test_brazilian_real_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (brazilian_real_one)
    ])
    def test_brazilian_real_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BRL'
        assert new.numeric_code == '986'
        assert new.symbol == 'R$'
        assert new.localized_symbol == 'R$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'
