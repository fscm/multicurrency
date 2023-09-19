# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dalasi currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dalasi import Dalasi


class TestDalasi:
    """Dalasi currency tests."""

    dalasi_minus_one = Dalasi(-1)
    dalasi_one_other = Dalasi(1)
    dalasi_one = Dalasi(1)
    dalasi_two = Dalasi(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'D\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'D\xa03.14'),
        (10, '10', 'D\xa010.00'),
        (Decimal('10'), '10', 'D\xa010.00'),
        ('-3.14', '-3.14', 'D\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'D\xa0-3.14'),
        (-10, '-10', 'D\xa0-10.00'),
        (Decimal('-10'), '-10', 'D\xa0-10.00')
    ])
    def test_dalasi_default(amount, result, printed):
        default = Dalasi(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GMD'
        assert default.numeric_code == '270'
        assert default.symbol == 'D'
        assert default.localized_symbol == 'D'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GMD',
            '270'))
        assert default.__repr__() == (
            'Dalasi('
            f'amount: {result}, '
            'alpha_code: "GMD", '
            'numeric_code: "270", '
            'symbol: "D", '
            'localized_symbol: "D", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'D10.00,00000'),
        (-1000, 'D10.00,00000-')
    ])
    def test_dalasi_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Dalasi(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GMD'
        assert custom.numeric_code == '270'
        assert custom.symbol == 'D'
        assert custom.localized_symbol == 'D'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GMD',
            '270'))
        assert custom.__repr__() == (
            'Dalasi('
            f'amount: {amount}, '
            'alpha_code: "GMD", '
            'numeric_code: "270", '
            'symbol: "D", '
            'localized_symbol: "D", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_dalasi_recreate(amount, new_amount):
        default = Dalasi(amount)
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
    def test_dalasi_change_attributes(attribute, value):
        immutable = Dalasi(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Dalasi\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_dalasi_add_attributes(attribute, value):
        immutable = Dalasi(1000)
        with raises(
                AttributeError,
                match=f'\'Dalasi\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (dalasi_one, dalasi_one, dalasi_two, None),
        (dalasi_one, dalasi_one_other, dalasi_two, None),
        (dalasi_two, dalasi_minus_one, dalasi_one, None),
        (dalasi_one, other, None, CurrencyMismatchException),
        (dalasi_one, 1.00, None, CurrencyTypeException),
        (dalasi_one, '1.00', None, CurrencyTypeException)
    ])
    def test_dalasi_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (dalasi_one)
    ])
    def test_dalasi_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GMD'
        assert new.numeric_code == '270'
        assert new.symbol == 'D'
        assert new.localized_symbol == 'D'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
