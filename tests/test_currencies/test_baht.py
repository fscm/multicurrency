# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Baht currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.baht import Baht


class TestBaht:
    """Baht currency tests."""

    baht_minus_one = Baht(-1)
    baht_one_other = Baht(1)
    baht_one = Baht(1)
    baht_two = Baht(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '฿3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '฿3.14'),
        (10, '10', '฿10.00'),
        (Decimal('10'), '10', '฿10.00'),
        ('-3.14', '-3.14', '-฿3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-฿3.14'),
        (-10, '-10', '-฿10.00'),
        (Decimal('-10'), '-10', '-฿10.00')
    ])
    def test_baht_default(amount, result, printed):
        default = Baht(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'THB'
        assert default.numeric_code == '764'
        assert default.symbol == '฿'
        assert default.localized_symbol == '฿'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'THB',
            '764'))
        assert default.__repr__() == (
            'Baht('
            f'amount: {result}, '
            'alpha_code: "THB", '
            'numeric_code: "764", '
            'symbol: "฿", '
            'localized_symbol: "฿", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '฿10.00,00000'),
        (-1000, '฿10.00,00000-')
    ])
    def test_baht_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Baht(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'THB'
        assert custom.numeric_code == '764'
        assert custom.symbol == '฿'
        assert custom.localized_symbol == '฿'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'THB',
            '764'))
        assert custom.__repr__() == (
            'Baht('
            f'amount: {amount}, '
            'alpha_code: "THB", '
            'numeric_code: "764", '
            'symbol: "฿", '
            'localized_symbol: "฿", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_baht_recreate(amount, new_amount):
        default = Baht(amount)
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
    def test_baht_change_attributes(attribute, value):
        immutable = Baht(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Baht\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_baht_add_attributes(attribute, value):
        immutable = Baht(1000)
        with raises(
                AttributeError,
                match=f'\'Baht\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (baht_one, baht_one, baht_two, None),
        (baht_one, baht_one_other, baht_two, None),
        (baht_two, baht_minus_one, baht_one, None),
        (baht_one, other, None, CurrencyMismatchException),
        (baht_one, 1.00, None, CurrencyTypeException),
        (baht_one, '1.00', None, CurrencyTypeException)
    ])
    def test_baht_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (baht_one)
    ])
    def test_baht_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'THB'
        assert new.numeric_code == '764'
        assert new.symbol == '฿'
        assert new.localized_symbol == '฿'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
