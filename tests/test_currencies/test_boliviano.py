# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Boliviano currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.boliviano import Boliviano


class TestBoliviano:
    """Boliviano currency tests."""

    boliviano_minus_one = Boliviano(-1)
    boliviano_one_other = Boliviano(1)
    boliviano_one = Boliviano(1)
    boliviano_two = Boliviano(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Bs.\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Bs.\xa03,14'),
        (10, '10', 'Bs.\xa010,00'),
        (Decimal('10'), '10', 'Bs.\xa010,00'),
        ('-3.14', '-3.14', 'Bs.\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Bs.\xa0-3,14'),
        (-10, '-10', 'Bs.\xa0-10,00'),
        (Decimal('-10'), '-10', 'Bs.\xa0-10,00')
    ])
    def test_boliviano_default(amount, result, printed):
        default = Boliviano(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BOB'
        assert default.numeric_code == '068'
        assert default.symbol == 'Bs.'
        assert default.localized_symbol == 'Bs.'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BOB',
            '068'))
        assert default.__repr__() == (
            'Boliviano('
            f'amount: {result}, '
            'alpha_code: "BOB", '
            'numeric_code: "068", '
            'symbol: "Bs.", '
            'localized_symbol: "Bs.", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Bs.10.00,00000'),
        (-1000, 'Bs.10.00,00000-')
    ])
    def test_boliviano_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Boliviano(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BOB'
        assert custom.numeric_code == '068'
        assert custom.symbol == 'Bs.'
        assert custom.localized_symbol == 'Bs.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BOB',
            '068'))
        assert custom.__repr__() == (
            'Boliviano('
            f'amount: {amount}, '
            'alpha_code: "BOB", '
            'numeric_code: "068", '
            'symbol: "Bs.", '
            'localized_symbol: "Bs.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_boliviano_recreate(amount, new_amount):
        default = Boliviano(amount)
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
    def test_boliviano_change_attributes(attribute, value):
        immutable = Boliviano(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Boliviano\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_boliviano_add_attributes(attribute, value):
        immutable = Boliviano(1000)
        with raises(
                AttributeError,
                match=f'\'Boliviano\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (boliviano_one, boliviano_one, boliviano_two, None),
        (boliviano_one, boliviano_one_other, boliviano_two, None),
        (boliviano_two, boliviano_minus_one, boliviano_one, None),
        (boliviano_one, other, None, CurrencyMismatchException),
        (boliviano_one, 1.00, None, CurrencyTypeException),
        (boliviano_one, '1.00', None, CurrencyTypeException)
    ])
    def test_boliviano_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (boliviano_one)
    ])
    def test_boliviano_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BOB'
        assert new.numeric_code == '068'
        assert new.symbol == 'Bs.'
        assert new.localized_symbol == 'Bs.'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'
