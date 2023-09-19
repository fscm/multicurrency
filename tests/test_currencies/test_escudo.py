# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Escudo currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.escudo import CapeVerdeEscudo


class TestCapeVerdeEscudo:
    """Cape Verde Escudo currency tests."""

    cape_verde_escudo_minus_one = CapeVerdeEscudo(-1)
    cape_verde_escudo_one_other = CapeVerdeEscudo(1)
    cape_verde_escudo_one = CapeVerdeEscudo(1)
    cape_verde_escudo_two = CapeVerdeEscudo(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3$14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3$14'),
        (10, '10', '10$00'),
        (Decimal('10'), '10', '10$00'),
        ('-3.14', '-3.14', '-3$14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3$14'),
        (-10, '-10', '-10$00'),
        (Decimal('-10'), '-10', '-10$00')
    ])
    def test_cape_verde_escudo_default(amount, result, printed):
        default = CapeVerdeEscudo(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CVE'
        assert default.numeric_code == '132'
        assert default.symbol == ''
        assert default.localized_symbol == ''
        assert default.convertion == ''
        assert default.pattern == '2$\u202F3%a%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CVE',
            '132'))
        assert default.__repr__() == (
            'CapeVerdeEscudo('
            f'amount: {result}, '
            'alpha_code: "CVE", '
            'numeric_code: "132", '
            'symbol: "", '
            'localized_symbol: "", '
            'convertion: "", '
            'pattern: "2$ 3%a%s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '10.00,00000'),
        (-1000, '10.00,00000-')
    ])
    def test_cape_verde_escudo_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CapeVerdeEscudo(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CVE'
        assert custom.numeric_code == '132'
        assert custom.symbol == ''
        assert custom.localized_symbol == ''
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CVE',
            '132'))
        assert custom.__repr__() == (
            'CapeVerdeEscudo('
            f'amount: {amount}, '
            'alpha_code: "CVE", '
            'numeric_code: "132", '
            'symbol: "", '
            'localized_symbol: "", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cape_verde_escudo_recreate(amount, new_amount):
        default = CapeVerdeEscudo(amount)
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
    def test_cape_verde_escudo_change_attributes(attribute, value):
        immutable = CapeVerdeEscudo(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CapeVerdeEscudo\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cape_verde_escudo_add_attributes(attribute, value):
        immutable = CapeVerdeEscudo(1000)
        with raises(
                AttributeError,
                match=f'\'CapeVerdeEscudo\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cape_verde_escudo_one, cape_verde_escudo_one, cape_verde_escudo_two, None),
        (cape_verde_escudo_one, cape_verde_escudo_one_other, cape_verde_escudo_two, None),
        (cape_verde_escudo_two, cape_verde_escudo_minus_one, cape_verde_escudo_one, None),
        (cape_verde_escudo_one, other, None, CurrencyMismatchException),
        (cape_verde_escudo_one, 1.00, None, CurrencyTypeException),
        (cape_verde_escudo_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cape_verde_escudo_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cape_verde_escudo_one)
    ])
    def test_cape_verde_escudo_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CVE'
        assert new.numeric_code == '132'
        assert new.symbol == ''
        assert new.localized_symbol == ''
        assert new.convertion == ''
        assert new.pattern == '2$\u202F3%a%s'
