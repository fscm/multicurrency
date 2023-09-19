# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lempira currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lempira import Lempira


class TestLempira:
    """Lempira currency tests."""

    lempira_minus_one = Lempira(-1)
    lempira_one_other = Lempira(1)
    lempira_one = Lempira(1)
    lempira_two = Lempira(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'L\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'L\xa03.14'),
        (10, '10', 'L\xa010.00'),
        (Decimal('10'), '10', 'L\xa010.00'),
        ('-3.14', '-3.14', 'L\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'L\xa0-3.14'),
        (-10, '-10', 'L\xa0-10.00'),
        (Decimal('-10'), '-10', 'L\xa0-10.00')
    ])
    def test_lempira_default(amount, result, printed):
        default = Lempira(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'HNL'
        assert default.numeric_code == '340'
        assert default.symbol == 'L'
        assert default.localized_symbol == 'L'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'HNL',
            '340'))
        assert default.__repr__() == (
            'Lempira('
            f'amount: {result}, '
            'alpha_code: "HNL", '
            'numeric_code: "340", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'L10.00,00000'),
        (-1000, 'L10.00,00000-')
    ])
    def test_lempira_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Lempira(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'HNL'
        assert custom.numeric_code == '340'
        assert custom.symbol == 'L'
        assert custom.localized_symbol == 'L'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'HNL',
            '340'))
        assert custom.__repr__() == (
            'Lempira('
            f'amount: {amount}, '
            'alpha_code: "HNL", '
            'numeric_code: "340", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_lempira_recreate(amount, new_amount):
        default = Lempira(amount)
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
    def test_lempira_change_attributes(attribute, value):
        immutable = Lempira(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Lempira\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_lempira_add_attributes(attribute, value):
        immutable = Lempira(1000)
        with raises(
                AttributeError,
                match=f'\'Lempira\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (lempira_one, lempira_one, lempira_two, None),
        (lempira_one, lempira_one_other, lempira_two, None),
        (lempira_two, lempira_minus_one, lempira_one, None),
        (lempira_one, other, None, CurrencyMismatchException),
        (lempira_one, 1.00, None, CurrencyTypeException),
        (lempira_one, '1.00', None, CurrencyTypeException)
    ])
    def test_lempira_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (lempira_one)
    ])
    def test_lempira_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'HNL'
        assert new.numeric_code == '340'
        assert new.symbol == 'L'
        assert new.localized_symbol == 'L'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
