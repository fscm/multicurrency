# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Metical currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.metical import Metical


class TestMetical:
    """Metical currency tests."""

    metical_minus_one = Metical(-1)
    metical_one_other = Metical(1)
    metical_one = Metical(1)
    metical_two = Metical(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0MTn'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0MTn'),
        (10, '10', '10\xa0MTn'),
        (Decimal('10'), '10', '10\xa0MTn'),
        ('-3.14', '-3.14', '-3\xa0MTn'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0MTn'),
        (-10, '-10', '-10\xa0MTn'),
        (Decimal('-10'), '-10', '-10\xa0MTn')
    ])
    def test_metical_default(amount, result, printed):
        default = Metical(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MZN'
        assert default.numeric_code == '943'
        assert default.symbol == 'MTn'
        assert default.localized_symbol == 'MTn'
        assert default.convertion == ''
        assert default.pattern == '0,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MZN',
            '943'))
        assert default.__repr__() == (
            'Metical('
            f'amount: {result}, '
            'alpha_code: "MZN", '
            'numeric_code: "943", '
            'symbol: "MTn", '
            'localized_symbol: "MTn", '
            'convertion: "", '
            'pattern: "0,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'MTn10.00,00000'),
        (-1000, 'MTn10.00,00000-')
    ])
    def test_metical_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Metical(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MZN'
        assert custom.numeric_code == '943'
        assert custom.symbol == 'MTn'
        assert custom.localized_symbol == 'MTn'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MZN',
            '943'))
        assert custom.__repr__() == (
            'Metical('
            f'amount: {amount}, '
            'alpha_code: "MZN", '
            'numeric_code: "943", '
            'symbol: "MTn", '
            'localized_symbol: "MTn", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_metical_recreate(amount, new_amount):
        default = Metical(amount)
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
    def test_metical_change_attributes(attribute, value):
        immutable = Metical(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Metical\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_metical_add_attributes(attribute, value):
        immutable = Metical(1000)
        with raises(
                AttributeError,
                match=f'\'Metical\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (metical_one, metical_one, metical_two, None),
        (metical_one, metical_one_other, metical_two, None),
        (metical_two, metical_minus_one, metical_one, None),
        (metical_one, other, None, CurrencyMismatchException),
        (metical_one, 1.00, None, CurrencyTypeException),
        (metical_one, '1.00', None, CurrencyTypeException)
    ])
    def test_metical_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (metical_one)
    ])
    def test_metical_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MZN'
        assert new.numeric_code == '943'
        assert new.symbol == 'MTn'
        assert new.localized_symbol == 'MTn'
        assert new.convertion == ''
        assert new.pattern == '0,.3%a\u00A0%s'
