# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Loti currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.loti import Loti


class TestLoti:
    """Loti currency tests."""

    loti_minus_one = Loti(-1)
    loti_one_other = Loti(1)
    loti_one = Loti(1)
    loti_two = Loti(2)
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
    def test_loti_default(amount, result, printed):
        default = Loti(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LSL'
        assert default.numeric_code == '426'
        assert default.symbol == 'L'
        assert default.localized_symbol == 'L'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LSL',
            '426'))
        assert default.__repr__() == (
            'Loti('
            f'amount: {result}, '
            'alpha_code: "LSL", '
            'numeric_code: "426", '
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
    def test_loti_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Loti(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LSL'
        assert custom.numeric_code == '426'
        assert custom.symbol == 'L'
        assert custom.localized_symbol == 'L'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LSL',
            '426'))
        assert custom.__repr__() == (
            'Loti('
            f'amount: {amount}, '
            'alpha_code: "LSL", '
            'numeric_code: "426", '
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
    def test_loti_recreate(amount, new_amount):
        default = Loti(amount)
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
    def test_loti_change_attributes(attribute, value):
        immutable = Loti(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Loti\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_loti_add_attributes(attribute, value):
        immutable = Loti(1000)
        with raises(
                AttributeError,
                match=f'\'Loti\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (loti_one, loti_one, loti_two, None),
        (loti_one, loti_one_other, loti_two, None),
        (loti_two, loti_minus_one, loti_one, None),
        (loti_one, other, None, CurrencyMismatchException),
        (loti_one, 1.00, None, CurrencyTypeException),
        (loti_one, '1.00', None, CurrencyTypeException)
    ])
    def test_loti_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (loti_one)
    ])
    def test_loti_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LSL'
        assert new.numeric_code == '426'
        assert new.symbol == 'L'
        assert new.localized_symbol == 'L'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
