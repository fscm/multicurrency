# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Taka currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.taka import Taka


class TestTaka:
    """Taka currency tests."""

    taka_minus_one = Taka(-1)
    taka_one_other = Taka(1)
    taka_one = Taka(1)
    taka_two = Taka(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '৩.১৪৳'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '৩.১৪৳'),
        (10, '10', '১০.০০৳'),
        (Decimal('10'), '10', '১০.০০৳'),
        ('-3.14', '-3.14', '-৩.১৪৳'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-৩.১৪৳'),
        (-10, '-10', '-১০.০০৳'),
        (Decimal('-10'), '-10', '-১০.০০৳')
    ])
    def test_taka_default(amount, result, printed):
        default = Taka(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BDT'
        assert default.numeric_code == '050'
        assert default.symbol == '৳'
        assert default.localized_symbol == '৳'
        assert default.convertion == '০১২৩৪৫৬৭৮৯-,.'
        assert default.pattern == '2.,3%a%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BDT',
            '050'))
        assert default.__repr__() == (
            'Taka('
            f'amount: {result}, '
            'alpha_code: "BDT", '
            'numeric_code: "050", '
            'symbol: "৳", '
            'localized_symbol: "৳", '
            'convertion: "০১২৩৪৫৬৭৮৯-,.", '
            'pattern: "2.,3%a%s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '৳১০.০০,০০০০০'),
        (-1000, '৳১০.০০,০০০০০-')
    ])
    def test_taka_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Taka(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BDT'
        assert custom.numeric_code == '050'
        assert custom.symbol == '৳'
        assert custom.localized_symbol == '৳'
        assert custom.convertion == '০১২৩৪৫৬৭৮৯-,.'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BDT',
            '050'))
        assert custom.__repr__() == (
            'Taka('
            f'amount: {amount}, '
            'alpha_code: "BDT", '
            'numeric_code: "050", '
            'symbol: "৳", '
            'localized_symbol: "৳", '
            'convertion: "০১২৩৪৫৬৭৮৯-,.", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_taka_recreate(amount, new_amount):
        default = Taka(amount)
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
    def test_taka_change_attributes(attribute, value):
        immutable = Taka(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Taka\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_taka_add_attributes(attribute, value):
        immutable = Taka(1000)
        with raises(
                AttributeError,
                match=f'\'Taka\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (taka_one, taka_one, taka_two, None),
        (taka_one, taka_one_other, taka_two, None),
        (taka_two, taka_minus_one, taka_one, None),
        (taka_one, other, None, CurrencyMismatchException),
        (taka_one, 1.00, None, CurrencyTypeException),
        (taka_one, '1.00', None, CurrencyTypeException)
    ])
    def test_taka_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (taka_one)
    ])
    def test_taka_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BDT'
        assert new.numeric_code == '050'
        assert new.symbol == '৳'
        assert new.localized_symbol == '৳'
        assert new.convertion == '০১২৩৪৫৬৭৮৯-,.'
        assert new.pattern == '2.,3%a%s'
