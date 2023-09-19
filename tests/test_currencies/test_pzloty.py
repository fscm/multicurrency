# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the PZloty currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.pzloty import PZloty


class TestPZloty:
    """PZloty currency tests."""

    pzloty_minus_one = PZloty(-1)
    pzloty_one_other = PZloty(1)
    pzloty_one = PZloty(1)
    pzloty_two = PZloty(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0zł'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0zł'),
        (10, '10', '10,00\xa0zł'),
        (Decimal('10'), '10', '10,00\xa0zł'),
        ('-3.14', '-3.14', '-3,14\xa0zł'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0zł'),
        (-10, '-10', '-10,00\xa0zł'),
        (Decimal('-10'), '-10', '-10,00\xa0zł')
    ])
    def test_pzloty_default(amount, result, printed):
        default = PZloty(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PLN'
        assert default.numeric_code == '985'
        assert default.symbol == 'zł'
        assert default.localized_symbol == 'zł'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PLN',
            '985'))
        assert default.__repr__() == (
            'PZloty('
            f'amount: {result}, '
            'alpha_code: "PLN", '
            'numeric_code: "985", '
            'symbol: "zł", '
            'localized_symbol: "zł", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'zł10.00,00000'),
        (-1000, 'zł10.00,00000-')
    ])
    def test_pzloty_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PZloty(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PLN'
        assert custom.numeric_code == '985'
        assert custom.symbol == 'zł'
        assert custom.localized_symbol == 'zł'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PLN',
            '985'))
        assert custom.__repr__() == (
            'PZloty('
            f'amount: {amount}, '
            'alpha_code: "PLN", '
            'numeric_code: "985", '
            'symbol: "zł", '
            'localized_symbol: "zł", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pzloty_recreate(amount, new_amount):
        default = PZloty(amount)
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
    def test_pzloty_change_attributes(attribute, value):
        immutable = PZloty(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PZloty\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pzloty_add_attributes(attribute, value):
        immutable = PZloty(1000)
        with raises(
                AttributeError,
                match=f'\'PZloty\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pzloty_one, pzloty_one, pzloty_two, None),
        (pzloty_one, pzloty_one_other, pzloty_two, None),
        (pzloty_two, pzloty_minus_one, pzloty_one, None),
        (pzloty_one, other, None, CurrencyMismatchException),
        (pzloty_one, 1.00, None, CurrencyTypeException),
        (pzloty_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pzloty_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pzloty_one)
    ])
    def test_pzloty_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PLN'
        assert new.numeric_code == '985'
        assert new.symbol == 'zł'
        assert new.localized_symbol == 'zł'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
