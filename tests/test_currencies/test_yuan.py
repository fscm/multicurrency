# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yuan currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.yuan import Yuan


class TestYuan:
    """Yuan currency tests."""

    yuan_minus_one = Yuan(-1)
    yuan_one_other = Yuan(1)
    yuan_one = Yuan(1)
    yuan_two = Yuan(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '¥3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '¥3.14'),
        (10, '10', '¥10.00'),
        (Decimal('10'), '10', '¥10.00'),
        ('-3.14', '-3.14', '-¥3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-¥3.14'),
        (-10, '-10', '-¥10.00'),
        (Decimal('-10'), '-10', '-¥10.00')
    ])
    def test_yuan_default(amount, result, printed):
        default = Yuan(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CNY'
        assert default.numeric_code == '156'
        assert default.symbol == '¥'
        assert default.localized_symbol == '¥'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CNY',
            '156'))
        assert default.__repr__() == (
            'Yuan('
            f'amount: {result}, '
            'alpha_code: "CNY", '
            'numeric_code: "156", '
            'symbol: "¥", '
            'localized_symbol: "¥", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '¥10.00,00000'),
        (-1000, '¥10.00,00000-')
    ])
    def test_yuan_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Yuan(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CNY'
        assert custom.numeric_code == '156'
        assert custom.symbol == '¥'
        assert custom.localized_symbol == '¥'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CNY',
            '156'))
        assert custom.__repr__() == (
            'Yuan('
            f'amount: {amount}, '
            'alpha_code: "CNY", '
            'numeric_code: "156", '
            'symbol: "¥", '
            'localized_symbol: "¥", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_yuan_recreate(amount, new_amount):
        default = Yuan(amount)
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
    def test_yuan_change_attributes(attribute, value):
        immutable = Yuan(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Yuan\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_yuan_add_attributes(attribute, value):
        immutable = Yuan(1000)
        with raises(
                AttributeError,
                match=f'\'Yuan\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (yuan_one, yuan_one, yuan_two, None),
        (yuan_one, yuan_one_other, yuan_two, None),
        (yuan_two, yuan_minus_one, yuan_one, None),
        (yuan_one, other, None, CurrencyMismatchException),
        (yuan_one, 1.00, None, CurrencyTypeException),
        (yuan_one, '1.00', None, CurrencyTypeException)
    ])
    def test_yuan_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (yuan_one)
    ])
    def test_yuan_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CNY'
        assert new.numeric_code == '156'
        assert new.symbol == '¥'
        assert new.localized_symbol == '¥'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
