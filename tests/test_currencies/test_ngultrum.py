# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ngultrum currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.ngultrum import Ngultrum


class TestNgultrum:
    """Ngultrum currency tests."""

    ngultrum_minus_one = Ngultrum(-1)
    ngultrum_one_other = Ngultrum(1)
    ngultrum_one = Ngultrum(1)
    ngultrum_two = Ngultrum(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Nu.\xa0༣.༡༤'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Nu.\xa0༣.༡༤'),
        (10, '10', 'Nu.\xa0༡༠.༠༠'),
        (Decimal('10'), '10', 'Nu.\xa0༡༠.༠༠'),
        ('-3.14', '-3.14', 'Nu.\xa0-༣.༡༤'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Nu.\xa0-༣.༡༤'),
        (-10, '-10', 'Nu.\xa0-༡༠.༠༠'),
        (Decimal('-10'), '-10', 'Nu.\xa0-༡༠.༠༠')
    ])
    def test_ngultrum_default(amount, result, printed):
        default = Ngultrum(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BTN'
        assert default.numeric_code == '064'
        assert default.symbol == 'Nu.'
        assert default.localized_symbol == 'Nu.'
        assert default.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BTN',
            '064'))
        assert default.__repr__() == (
            'Ngultrum('
            f'amount: {result}, '
            'alpha_code: "BTN", '
            'numeric_code: "064", '
            'symbol: "Nu.", '
            'localized_symbol: "Nu.", '
            'convertion: "༠༡༢༣༤༥༦༧༨༩-", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Nu.༡༠.༠༠,༠༠༠༠༠'),
        (-1000, 'Nu.༡༠.༠༠,༠༠༠༠༠-')
    ])
    def test_ngultrum_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Ngultrum(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BTN'
        assert custom.numeric_code == '064'
        assert custom.symbol == 'Nu.'
        assert custom.localized_symbol == 'Nu.'
        assert custom.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BTN',
            '064'))
        assert custom.__repr__() == (
            'Ngultrum('
            f'amount: {amount}, '
            'alpha_code: "BTN", '
            'numeric_code: "064", '
            'symbol: "Nu.", '
            'localized_symbol: "Nu.", '
            'convertion: "༠༡༢༣༤༥༦༧༨༩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_ngultrum_recreate(amount, new_amount):
        default = Ngultrum(amount)
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
    def test_ngultrum_change_attributes(attribute, value):
        immutable = Ngultrum(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Ngultrum\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_ngultrum_add_attributes(attribute, value):
        immutable = Ngultrum(1000)
        with raises(
                AttributeError,
                match=f'\'Ngultrum\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (ngultrum_one, ngultrum_one, ngultrum_two, None),
        (ngultrum_one, ngultrum_one_other, ngultrum_two, None),
        (ngultrum_two, ngultrum_minus_one, ngultrum_one, None),
        (ngultrum_one, other, None, CurrencyMismatchException),
        (ngultrum_one, 1.00, None, CurrencyTypeException),
        (ngultrum_one, '1.00', None, CurrencyTypeException)
    ])
    def test_ngultrum_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (ngultrum_one)
    ])
    def test_ngultrum_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BTN'
        assert new.numeric_code == '064'
        assert new.symbol == 'Nu.'
        assert new.localized_symbol == 'Nu.'
        assert new.convertion == '༠༡༢༣༤༥༦༧༨༩-'
        assert new.pattern == '2.,3%s\u00A0%a'
