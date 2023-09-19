# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Oro currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.oro import CordobaOro


class TestCordobaOro:
    """Cordoba Oro currency tests."""

    cordoba_oro_minus_one = CordobaOro(-1)
    cordoba_oro_one_other = CordobaOro(1)
    cordoba_oro_one = CordobaOro(1)
    cordoba_oro_two = CordobaOro(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'C$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'C$3.14'),
        (10, '10', 'C$10.00'),
        (Decimal('10'), '10', 'C$10.00'),
        ('-3.14', '-3.14', '-C$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-C$3.14'),
        (-10, '-10', '-C$10.00'),
        (Decimal('-10'), '-10', '-C$10.00')
    ])
    def test_cordoba_oro_default(amount, result, printed):
        default = CordobaOro(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NIO'
        assert default.numeric_code == '558'
        assert default.symbol == 'C$'
        assert default.localized_symbol == 'C$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NIO',
            '558'))
        assert default.__repr__() == (
            'CordobaOro('
            f'amount: {result}, '
            'alpha_code: "NIO", '
            'numeric_code: "558", '
            'symbol: "C$", '
            'localized_symbol: "C$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'C$10.00,00000'),
        (-1000, 'C$10.00,00000-')
    ])
    def test_cordoba_oro_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CordobaOro(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NIO'
        assert custom.numeric_code == '558'
        assert custom.symbol == 'C$'
        assert custom.localized_symbol == 'C$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NIO',
            '558'))
        assert custom.__repr__() == (
            'CordobaOro('
            f'amount: {amount}, '
            'alpha_code: "NIO", '
            'numeric_code: "558", '
            'symbol: "C$", '
            'localized_symbol: "C$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cordoba_oro_recreate(amount, new_amount):
        default = CordobaOro(amount)
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
    def test_cordoba_oro_change_attributes(attribute, value):
        immutable = CordobaOro(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CordobaOro\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cordoba_oro_add_attributes(attribute, value):
        immutable = CordobaOro(1000)
        with raises(
                AttributeError,
                match=f'\'CordobaOro\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cordoba_oro_one, cordoba_oro_one, cordoba_oro_two, None),
        (cordoba_oro_one, cordoba_oro_one_other, cordoba_oro_two, None),
        (cordoba_oro_two, cordoba_oro_minus_one, cordoba_oro_one, None),
        (cordoba_oro_one, other, None, CurrencyMismatchException),
        (cordoba_oro_one, 1.00, None, CurrencyTypeException),
        (cordoba_oro_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cordoba_oro_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cordoba_oro_one)
    ])
    def test_cordoba_oro_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NIO'
        assert new.numeric_code == '558'
        assert new.symbol == 'C$'
        assert new.localized_symbol == 'C$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
