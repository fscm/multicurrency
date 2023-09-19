# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ringgit currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.ringgit import MalaysianRinggit


class TestMalaysianRinggit:
    """Malaysian Ringgit currency tests."""

    malaysian_ringgit_minus_one = MalaysianRinggit(-1)
    malaysian_ringgit_one_other = MalaysianRinggit(1)
    malaysian_ringgit_one = MalaysianRinggit(1)
    malaysian_ringgit_two = MalaysianRinggit(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'RM\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'RM\xa03.14'),
        (10, '10', 'RM\xa010.00'),
        (Decimal('10'), '10', 'RM\xa010.00'),
        ('-3.14', '-3.14', 'RM\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'RM\xa0-3.14'),
        (-10, '-10', 'RM\xa0-10.00'),
        (Decimal('-10'), '-10', 'RM\xa0-10.00')
    ])
    def test_malaysian_ringgit_default(amount, result, printed):
        default = MalaysianRinggit(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MYR'
        assert default.numeric_code == '458'
        assert default.symbol == 'RM'
        assert default.localized_symbol == 'RM'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MYR',
            '458'))
        assert default.__repr__() == (
            'MalaysianRinggit('
            f'amount: {result}, '
            'alpha_code: "MYR", '
            'numeric_code: "458", '
            'symbol: "RM", '
            'localized_symbol: "RM", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'RM10.00,00000'),
        (-1000, 'RM10.00,00000-')
    ])
    def test_malaysian_ringgit_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MalaysianRinggit(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MYR'
        assert custom.numeric_code == '458'
        assert custom.symbol == 'RM'
        assert custom.localized_symbol == 'RM'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MYR',
            '458'))
        assert custom.__repr__() == (
            'MalaysianRinggit('
            f'amount: {amount}, '
            'alpha_code: "MYR", '
            'numeric_code: "458", '
            'symbol: "RM", '
            'localized_symbol: "RM", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_malaysian_ringgit_recreate(amount, new_amount):
        default = MalaysianRinggit(amount)
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
    def test_malaysian_ringgit_change_attributes(attribute, value):
        immutable = MalaysianRinggit(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MalaysianRinggit\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_malaysian_ringgit_add_attributes(attribute, value):
        immutable = MalaysianRinggit(1000)
        with raises(
                AttributeError,
                match=f'\'MalaysianRinggit\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (malaysian_ringgit_one, malaysian_ringgit_one, malaysian_ringgit_two, None),
        (malaysian_ringgit_one, malaysian_ringgit_one_other, malaysian_ringgit_two, None),
        (malaysian_ringgit_two, malaysian_ringgit_minus_one, malaysian_ringgit_one, None),
        (malaysian_ringgit_one, other, None, CurrencyMismatchException),
        (malaysian_ringgit_one, 1.00, None, CurrencyTypeException),
        (malaysian_ringgit_one, '1.00', None, CurrencyTypeException)
    ])
    def test_malaysian_ringgit_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (malaysian_ringgit_one)
    ])
    def test_malaysian_ringgit_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MYR'
        assert new.numeric_code == '458'
        assert new.symbol == 'RM'
        assert new.localized_symbol == 'RM'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
