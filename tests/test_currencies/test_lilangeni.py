# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lilangeni currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lilangeni import Lilangeni


class TestLilangeni:
    """Lilangeni currency tests."""

    lilangeni_minus_one = Lilangeni(-1)
    lilangeni_one_other = Lilangeni(1)
    lilangeni_one = Lilangeni(1)
    lilangeni_two = Lilangeni(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'L\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'L\xa03.14'),
        (10, '10', 'L\xa010.00'),
        (Decimal('10'), '10', 'L\xa010.00'),
        ('-3.14', '-3.14', 'L\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'L\xa0-3.14'),
        (-10, '-10', 'L\xa0-10.00'),
        (Decimal('-10'), '-10', 'L\xa0-10.00')
    ])
    def test_lilangeni_default(amount, result, printed):
        default = Lilangeni(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SZL'
        assert default.numeric_code == '748'
        assert default.symbol == 'L'
        assert default.localized_symbol == 'L'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SZL',
            '748'))
        assert default.__repr__() == (
            'Lilangeni('
            f'amount: {result}, '
            'alpha_code: "SZL", '
            'numeric_code: "748", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'L10.00,00000'),
        (-1000, 'L10.00,00000-')
    ])
    def test_lilangeni_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Lilangeni(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SZL'
        assert custom.numeric_code == '748'
        assert custom.symbol == 'L'
        assert custom.localized_symbol == 'L'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SZL',
            '748'))
        assert custom.__repr__() == (
            'Lilangeni('
            f'amount: {amount}, '
            'alpha_code: "SZL", '
            'numeric_code: "748", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_lilangeni_recreate(amount, new_amount):
        default = Lilangeni(amount)
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
    def test_lilangeni_change_attributes(attribute, value):
        immutable = Lilangeni(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Lilangeni\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_lilangeni_add_attributes(attribute, value):
        immutable = Lilangeni(1000)
        with raises(
                AttributeError,
                match=f'\'Lilangeni\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (lilangeni_one, lilangeni_one, lilangeni_two, None),
        (lilangeni_one, lilangeni_one_other, lilangeni_two, None),
        (lilangeni_two, lilangeni_minus_one, lilangeni_one, None),
        (lilangeni_one, other, None, CurrencyMismatchException),
        (lilangeni_one, 1.00, None, CurrencyTypeException),
        (lilangeni_one, '1.00', None, CurrencyTypeException)
    ])
    def test_lilangeni_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (lilangeni_one)
    ])
    def test_lilangeni_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SZL'
        assert new.numeric_code == '748'
        assert new.symbol == 'L'
        assert new.localized_symbol == 'L'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
