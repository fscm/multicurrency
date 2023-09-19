# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Riel currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.riel import Riel


class TestRiel:
    """Riel currency tests."""

    riel_minus_one = Riel(-1)
    riel_one_other = Riel(1)
    riel_one = Riel(1)
    riel_two = Riel(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14៛'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14៛'),
        (10, '10', '10,00៛'),
        (Decimal('10'), '10', '10,00៛'),
        ('-3.14', '-3.14', '-3,14៛'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14៛'),
        (-10, '-10', '-10,00៛'),
        (Decimal('-10'), '-10', '-10,00៛')
    ])
    def test_riel_default(amount, result, printed):
        default = Riel(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KHR'
        assert default.numeric_code == '116'
        assert default.symbol == '៛'
        assert default.localized_symbol == '៛'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KHR',
            '116'))
        assert default.__repr__() == (
            'Riel('
            f'amount: {result}, '
            'alpha_code: "KHR", '
            'numeric_code: "116", '
            'symbol: "៛", '
            'localized_symbol: "៛", '
            'convertion: "", '
            'pattern: "2,.3%a%s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '៛10.00,00000'),
        (-1000, '៛10.00,00000-')
    ])
    def test_riel_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Riel(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KHR'
        assert custom.numeric_code == '116'
        assert custom.symbol == '៛'
        assert custom.localized_symbol == '៛'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KHR',
            '116'))
        assert custom.__repr__() == (
            'Riel('
            f'amount: {amount}, '
            'alpha_code: "KHR", '
            'numeric_code: "116", '
            'symbol: "៛", '
            'localized_symbol: "៛", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_riel_recreate(amount, new_amount):
        default = Riel(amount)
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
    def test_riel_change_attributes(attribute, value):
        immutable = Riel(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Riel\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_riel_add_attributes(attribute, value):
        immutable = Riel(1000)
        with raises(
                AttributeError,
                match=f'\'Riel\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (riel_one, riel_one, riel_two, None),
        (riel_one, riel_one_other, riel_two, None),
        (riel_two, riel_minus_one, riel_one, None),
        (riel_one, other, None, CurrencyMismatchException),
        (riel_one, 1.00, None, CurrencyTypeException),
        (riel_one, '1.00', None, CurrencyTypeException)
    ])
    def test_riel_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (riel_one)
    ])
    def test_riel_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KHR'
        assert new.numeric_code == '116'
        assert new.symbol == '៛'
        assert new.localized_symbol == '៛'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a%s'
