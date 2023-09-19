# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kina currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kina import Kina


class TestKina:
    """Kina currency tests."""

    kina_minus_one = Kina(-1)
    kina_one_other = Kina(1)
    kina_one = Kina(1)
    kina_two = Kina(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'K\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'K\xa03.14'),
        (10, '10', 'K\xa010.00'),
        (Decimal('10'), '10', 'K\xa010.00'),
        ('-3.14', '-3.14', 'K\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'K\xa0-3.14'),
        (-10, '-10', 'K\xa0-10.00'),
        (Decimal('-10'), '-10', 'K\xa0-10.00')
    ])
    def test_kina_default(amount, result, printed):
        default = Kina(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PGK'
        assert default.numeric_code == '598'
        assert default.symbol == 'K'
        assert default.localized_symbol == 'K'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PGK',
            '598'))
        assert default.__repr__() == (
            'Kina('
            f'amount: {result}, '
            'alpha_code: "PGK", '
            'numeric_code: "598", '
            'symbol: "K", '
            'localized_symbol: "K", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'K10.00,00000'),
        (-1000, 'K10.00,00000-')
    ])
    def test_kina_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Kina(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PGK'
        assert custom.numeric_code == '598'
        assert custom.symbol == 'K'
        assert custom.localized_symbol == 'K'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PGK',
            '598'))
        assert custom.__repr__() == (
            'Kina('
            f'amount: {amount}, '
            'alpha_code: "PGK", '
            'numeric_code: "598", '
            'symbol: "K", '
            'localized_symbol: "K", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kina_recreate(amount, new_amount):
        default = Kina(amount)
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
    def test_kina_change_attributes(attribute, value):
        immutable = Kina(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Kina\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kina_add_attributes(attribute, value):
        immutable = Kina(1000)
        with raises(
                AttributeError,
                match=f'\'Kina\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kina_one, kina_one, kina_two, None),
        (kina_one, kina_one_other, kina_two, None),
        (kina_two, kina_minus_one, kina_one, None),
        (kina_one, other, None, CurrencyMismatchException),
        (kina_one, 1.00, None, CurrencyTypeException),
        (kina_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kina_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kina_one)
    ])
    def test_kina_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PGK'
        assert new.numeric_code == '598'
        assert new.symbol == 'K'
        assert new.localized_symbol == 'K'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
