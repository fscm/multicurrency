# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Balboa currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.balboa import Balboa


class TestBalboa:
    """Balboa currency tests."""

    balboa_minus_one = Balboa(-1)
    balboa_one_other = Balboa(1)
    balboa_one = Balboa(1)
    balboa_two = Balboa(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'B/.\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'B/.\xa03.14'),
        (10, '10', 'B/.\xa010.00'),
        (Decimal('10'), '10', 'B/.\xa010.00'),
        ('-3.14', '-3.14', 'B/.\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'B/.\xa0-3.14'),
        (-10, '-10', 'B/.\xa0-10.00'),
        (Decimal('-10'), '-10', 'B/.\xa0-10.00')
    ])
    def test_balboa_default(amount, result, printed):
        default = Balboa(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PAB'
        assert default.numeric_code == '590'
        assert default.symbol == 'B/.'
        assert default.localized_symbol == 'B/.'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PAB',
            '590'))
        assert default.__repr__() == (
            'Balboa('
            f'amount: {result}, '
            'alpha_code: "PAB", '
            'numeric_code: "590", '
            'symbol: "B/.", '
            'localized_symbol: "B/.", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'B/.10.00,00000'),
        (-1000, 'B/.10.00,00000-')
    ])
    def test_balboa_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Balboa(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PAB'
        assert custom.numeric_code == '590'
        assert custom.symbol == 'B/.'
        assert custom.localized_symbol == 'B/.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PAB',
            '590'))
        assert custom.__repr__() == (
            'Balboa('
            f'amount: {amount}, '
            'alpha_code: "PAB", '
            'numeric_code: "590", '
            'symbol: "B/.", '
            'localized_symbol: "B/.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_balboa_recreate(amount, new_amount):
        default = Balboa(amount)
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
    def test_balboa_change_attributes(attribute, value):
        immutable = Balboa(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Balboa\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_balboa_add_attributes(attribute, value):
        immutable = Balboa(1000)
        with raises(
                AttributeError,
                match=f'\'Balboa\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (balboa_one, balboa_one, balboa_two, None),
        (balboa_one, balboa_one_other, balboa_two, None),
        (balboa_two, balboa_minus_one, balboa_one, None),
        (balboa_one, other, None, CurrencyMismatchException),
        (balboa_one, 1.00, None, CurrencyTypeException),
        (balboa_one, '1.00', None, CurrencyTypeException)
    ])
    def test_balboa_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (balboa_one)
    ])
    def test_balboa_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PAB'
        assert new.numeric_code == '590'
        assert new.symbol == 'B/.'
        assert new.localized_symbol == 'B/.'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
