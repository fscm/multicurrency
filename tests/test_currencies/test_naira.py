# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Naira currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.naira import Naira


class TestNaira:
    """Naira currency tests."""

    naira_minus_one = Naira(-1)
    naira_one_other = Naira(1)
    naira_one = Naira(1)
    naira_two = Naira(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₦3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₦3.14'),
        (10, '10', '₦10.00'),
        (Decimal('10'), '10', '₦10.00'),
        ('-3.14', '-3.14', '-₦3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₦3.14'),
        (-10, '-10', '-₦10.00'),
        (Decimal('-10'), '-10', '-₦10.00')
    ])
    def test_naira_default(amount, result, printed):
        default = Naira(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NGN'
        assert default.numeric_code == '566'
        assert default.symbol == '₦'
        assert default.localized_symbol == '₦'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NGN',
            '566'))
        assert default.__repr__() == (
            'Naira('
            f'amount: {result}, '
            'alpha_code: "NGN", '
            'numeric_code: "566", '
            'symbol: "₦", '
            'localized_symbol: "₦", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₦10.00,00000'),
        (-1000, '₦10.00,00000-')
    ])
    def test_naira_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Naira(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NGN'
        assert custom.numeric_code == '566'
        assert custom.symbol == '₦'
        assert custom.localized_symbol == '₦'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NGN',
            '566'))
        assert custom.__repr__() == (
            'Naira('
            f'amount: {amount}, '
            'alpha_code: "NGN", '
            'numeric_code: "566", '
            'symbol: "₦", '
            'localized_symbol: "₦", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_naira_recreate(amount, new_amount):
        default = Naira(amount)
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
    def test_naira_change_attributes(attribute, value):
        immutable = Naira(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Naira\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_naira_add_attributes(attribute, value):
        immutable = Naira(1000)
        with raises(
                AttributeError,
                match=f'\'Naira\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (naira_one, naira_one, naira_two, None),
        (naira_one, naira_one_other, naira_two, None),
        (naira_two, naira_minus_one, naira_one, None),
        (naira_one, other, None, CurrencyMismatchException),
        (naira_one, 1.00, None, CurrencyTypeException),
        (naira_one, '1.00', None, CurrencyTypeException)
    ])
    def test_naira_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (naira_one)
    ])
    def test_naira_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NGN'
        assert new.numeric_code == '566'
        assert new.symbol == '₦'
        assert new.localized_symbol == '₦'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
