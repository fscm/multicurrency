# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Gourde currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.gourde import Gourde


class TestGourde:
    """Gourde currency tests."""

    gourde_minus_one = Gourde(-1)
    gourde_one_other = Gourde(1)
    gourde_one = Gourde(1)
    gourde_two = Gourde(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'G\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'G\xa03.14'),
        (10, '10', 'G\xa010.00'),
        (Decimal('10'), '10', 'G\xa010.00'),
        ('-3.14', '-3.14', 'G\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'G\xa0-3.14'),
        (-10, '-10', 'G\xa0-10.00'),
        (Decimal('-10'), '-10', 'G\xa0-10.00')
    ])
    def test_gourde_default(amount, result, printed):
        default = Gourde(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'HTG'
        assert default.numeric_code == '332'
        assert default.symbol == 'G'
        assert default.localized_symbol == 'G'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'HTG',
            '332'))
        assert default.__repr__() == (
            'Gourde('
            f'amount: {result}, '
            'alpha_code: "HTG", '
            'numeric_code: "332", '
            'symbol: "G", '
            'localized_symbol: "G", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'G10.00,00000'),
        (-1000, 'G10.00,00000-')
    ])
    def test_gourde_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Gourde(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'HTG'
        assert custom.numeric_code == '332'
        assert custom.symbol == 'G'
        assert custom.localized_symbol == 'G'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'HTG',
            '332'))
        assert custom.__repr__() == (
            'Gourde('
            f'amount: {amount}, '
            'alpha_code: "HTG", '
            'numeric_code: "332", '
            'symbol: "G", '
            'localized_symbol: "G", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_gourde_recreate(amount, new_amount):
        default = Gourde(amount)
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
    def test_gourde_change_attributes(attribute, value):
        immutable = Gourde(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Gourde\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_gourde_add_attributes(attribute, value):
        immutable = Gourde(1000)
        with raises(
                AttributeError,
                match=f'\'Gourde\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (gourde_one, gourde_one, gourde_two, None),
        (gourde_one, gourde_one_other, gourde_two, None),
        (gourde_two, gourde_minus_one, gourde_one, None),
        (gourde_one, other, None, CurrencyMismatchException),
        (gourde_one, 1.00, None, CurrencyTypeException),
        (gourde_one, '1.00', None, CurrencyTypeException)
    ])
    def test_gourde_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (gourde_one)
    ])
    def test_gourde_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'HTG'
        assert new.numeric_code == '332'
        assert new.symbol == 'G'
        assert new.localized_symbol == 'G'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
