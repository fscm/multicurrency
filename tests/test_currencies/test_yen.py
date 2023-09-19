# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yen currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.yen import Yen


class TestYen:
    """Yen currency tests."""

    yen_minus_one = Yen(-1)
    yen_one_other = Yen(1)
    yen_one = Yen(1)
    yen_two = Yen(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '¥3'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '¥3'),
        (10, '10', '¥10'),
        (Decimal('10'), '10', '¥10'),
        ('-3.14', '-3.14', '-¥3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-¥3'),
        (-10, '-10', '-¥10'),
        (Decimal('-10'), '-10', '-¥10')
    ])
    def test_yen_default(amount, result, printed):
        default = Yen(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'JPY'
        assert default.numeric_code == '392'
        assert default.symbol == '¥'
        assert default.localized_symbol == '¥'
        assert default.convertion == ''
        assert default.pattern == '0.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'JPY',
            '392'))
        assert default.__repr__() == (
            'Yen('
            f'amount: {result}, '
            'alpha_code: "JPY", '
            'numeric_code: "392", '
            'symbol: "¥", '
            'localized_symbol: "¥", '
            'convertion: "", '
            'pattern: "0.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '¥10.00,00000'),
        (-1000, '¥10.00,00000-')
    ])
    def test_yen_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Yen(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'JPY'
        assert custom.numeric_code == '392'
        assert custom.symbol == '¥'
        assert custom.localized_symbol == '¥'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'JPY',
            '392'))
        assert custom.__repr__() == (
            'Yen('
            f'amount: {amount}, '
            'alpha_code: "JPY", '
            'numeric_code: "392", '
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
    def test_yen_recreate(amount, new_amount):
        default = Yen(amount)
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
    def test_yen_change_attributes(attribute, value):
        immutable = Yen(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Yen\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_yen_add_attributes(attribute, value):
        immutable = Yen(1000)
        with raises(
                AttributeError,
                match=f'\'Yen\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (yen_one, yen_one, yen_two, None),
        (yen_one, yen_one_other, yen_two, None),
        (yen_two, yen_minus_one, yen_one, None),
        (yen_one, other, None, CurrencyMismatchException),
        (yen_one, 1.00, None, CurrencyTypeException),
        (yen_one, '1.00', None, CurrencyTypeException)
    ])
    def test_yen_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (yen_one)
    ])
    def test_yen_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'JPY'
        assert new.numeric_code == '392'
        assert new.symbol == '¥'
        assert new.localized_symbol == '¥'
        assert new.convertion == ''
        assert new.pattern == '0.,3%-%s%u'
