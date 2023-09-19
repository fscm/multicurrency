# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tenge currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.tenge import Tenge


class TestTenge:
    """Tenge currency tests."""

    tenge_minus_one = Tenge(-1)
    tenge_one_other = Tenge(1)
    tenge_one = Tenge(1)
    tenge_two = Tenge(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0〒'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0〒'),
        (10, '10', '10,00\xa0〒'),
        (Decimal('10'), '10', '10,00\xa0〒'),
        ('-3.14', '-3.14', '-3,14\xa0〒'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0〒'),
        (-10, '-10', '-10,00\xa0〒'),
        (Decimal('-10'), '-10', '-10,00\xa0〒')
    ])
    def test_tenge_default(amount, result, printed):
        default = Tenge(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KZT'
        assert default.numeric_code == '398'
        assert default.symbol == '〒'
        assert default.localized_symbol == '〒'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KZT',
            '398'))
        assert default.__repr__() == (
            'Tenge('
            f'amount: {result}, '
            'alpha_code: "KZT", '
            'numeric_code: "398", '
            'symbol: "〒", '
            'localized_symbol: "〒", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '〒10.00,00000'),
        (-1000, '〒10.00,00000-')
    ])
    def test_tenge_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Tenge(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KZT'
        assert custom.numeric_code == '398'
        assert custom.symbol == '〒'
        assert custom.localized_symbol == '〒'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KZT',
            '398'))
        assert custom.__repr__() == (
            'Tenge('
            f'amount: {amount}, '
            'alpha_code: "KZT", '
            'numeric_code: "398", '
            'symbol: "〒", '
            'localized_symbol: "〒", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tenge_recreate(amount, new_amount):
        default = Tenge(amount)
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
    def test_tenge_change_attributes(attribute, value):
        immutable = Tenge(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Tenge\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tenge_add_attributes(attribute, value):
        immutable = Tenge(1000)
        with raises(
                AttributeError,
                match=f'\'Tenge\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tenge_one, tenge_one, tenge_two, None),
        (tenge_one, tenge_one_other, tenge_two, None),
        (tenge_two, tenge_minus_one, tenge_one, None),
        (tenge_one, other, None, CurrencyMismatchException),
        (tenge_one, 1.00, None, CurrencyTypeException),
        (tenge_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tenge_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tenge_one)
    ])
    def test_tenge_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KZT'
        assert new.numeric_code == '398'
        assert new.symbol == '〒'
        assert new.localized_symbol == '〒'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
