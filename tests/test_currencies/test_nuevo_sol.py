# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nuevo Sol currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.nuevo_sol import NuevoSol


class TestNuevoSol:
    """Nuevo Sol currency tests."""

    nuevo_sol_minus_one = NuevoSol(-1)
    nuevo_sol_one_other = NuevoSol(1)
    nuevo_sol_one = NuevoSol(1)
    nuevo_sol_two = NuevoSol(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'S/.\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'S/.\xa03.14'),
        (10, '10', 'S/.\xa010.00'),
        (Decimal('10'), '10', 'S/.\xa010.00'),
        ('-3.14', '-3.14', 'S/.\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'S/.\xa0-3.14'),
        (-10, '-10', 'S/.\xa0-10.00'),
        (Decimal('-10'), '-10', 'S/.\xa0-10.00')
    ])
    def test_nuevo_sol_default(amount, result, printed):
        default = NuevoSol(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PEN'
        assert default.numeric_code == '604'
        assert default.symbol == 'S/.'
        assert default.localized_symbol == 'S/.'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PEN',
            '604'))
        assert default.__repr__() == (
            'NuevoSol('
            f'amount: {result}, '
            'alpha_code: "PEN", '
            'numeric_code: "604", '
            'symbol: "S/.", '
            'localized_symbol: "S/.", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'S/.10.00,00000'),
        (-1000, 'S/.10.00,00000-')
    ])
    def test_nuevo_sol_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NuevoSol(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PEN'
        assert custom.numeric_code == '604'
        assert custom.symbol == 'S/.'
        assert custom.localized_symbol == 'S/.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PEN',
            '604'))
        assert custom.__repr__() == (
            'NuevoSol('
            f'amount: {amount}, '
            'alpha_code: "PEN", '
            'numeric_code: "604", '
            'symbol: "S/.", '
            'localized_symbol: "S/.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_nuevo_sol_recreate(amount, new_amount):
        default = NuevoSol(amount)
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
    def test_nuevo_sol_change_attributes(attribute, value):
        immutable = NuevoSol(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NuevoSol\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_nuevo_sol_add_attributes(attribute, value):
        immutable = NuevoSol(1000)
        with raises(
                AttributeError,
                match=f'\'NuevoSol\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (nuevo_sol_one, nuevo_sol_one, nuevo_sol_two, None),
        (nuevo_sol_one, nuevo_sol_one_other, nuevo_sol_two, None),
        (nuevo_sol_two, nuevo_sol_minus_one, nuevo_sol_one, None),
        (nuevo_sol_one, other, None, CurrencyMismatchException),
        (nuevo_sol_one, 1.00, None, CurrencyTypeException),
        (nuevo_sol_one, '1.00', None, CurrencyTypeException)
    ])
    def test_nuevo_sol_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (nuevo_sol_one)
    ])
    def test_nuevo_sol_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PEN'
        assert new.numeric_code == '604'
        assert new.symbol == 'S/.'
        assert new.localized_symbol == 'S/.'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
