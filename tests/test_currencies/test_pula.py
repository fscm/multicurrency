# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pula currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.pula import Pula


class TestPula:
    """Pula currency tests."""

    pula_minus_one = Pula(-1)
    pula_one_other = Pula(1)
    pula_one = Pula(1)
    pula_two = Pula(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'P\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'P\xa03.14'),
        (10, '10', 'P\xa010.00'),
        (Decimal('10'), '10', 'P\xa010.00'),
        ('-3.14', '-3.14', 'P\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'P\xa0-3.14'),
        (-10, '-10', 'P\xa0-10.00'),
        (Decimal('-10'), '-10', 'P\xa0-10.00')
    ])
    def test_pula_default(amount, result, printed):
        default = Pula(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BWP'
        assert default.numeric_code == '072'
        assert default.symbol == 'P'
        assert default.localized_symbol == 'P'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BWP',
            '072'))
        assert default.__repr__() == (
            'Pula('
            f'amount: {result}, '
            'alpha_code: "BWP", '
            'numeric_code: "072", '
            'symbol: "P", '
            'localized_symbol: "P", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'P10.00,00000'),
        (-1000, 'P10.00,00000-')
    ])
    def test_pula_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Pula(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BWP'
        assert custom.numeric_code == '072'
        assert custom.symbol == 'P'
        assert custom.localized_symbol == 'P'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BWP',
            '072'))
        assert custom.__repr__() == (
            'Pula('
            f'amount: {amount}, '
            'alpha_code: "BWP", '
            'numeric_code: "072", '
            'symbol: "P", '
            'localized_symbol: "P", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pula_recreate(amount, new_amount):
        default = Pula(amount)
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
    def test_pula_change_attributes(attribute, value):
        immutable = Pula(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Pula\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pula_add_attributes(attribute, value):
        immutable = Pula(1000)
        with raises(
                AttributeError,
                match=f'\'Pula\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pula_one, pula_one, pula_two, None),
        (pula_one, pula_one_other, pula_two, None),
        (pula_two, pula_minus_one, pula_one, None),
        (pula_one, other, None, CurrencyMismatchException),
        (pula_one, 1.00, None, CurrencyTypeException),
        (pula_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pula_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pula_one)
    ])
    def test_pula_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BWP'
        assert new.numeric_code == '072'
        assert new.symbol == 'P'
        assert new.localized_symbol == 'P'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
