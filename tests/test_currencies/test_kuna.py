# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kuna currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kuna import CroatianKuna


class TestCroatianKuna:
    """Croatian Kuna currency tests."""

    croatian_kuna_minus_one = CroatianKuna(-1)
    croatian_kuna_one_other = CroatianKuna(1)
    croatian_kuna_one = CroatianKuna(1)
    croatian_kuna_two = CroatianKuna(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Kn'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Kn'),
        (10, '10', '10,00\xa0Kn'),
        (Decimal('10'), '10', '10,00\xa0Kn'),
        ('-3.14', '-3.14', '-3,14\xa0Kn'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Kn'),
        (-10, '-10', '-10,00\xa0Kn'),
        (Decimal('-10'), '-10', '-10,00\xa0Kn')
    ])
    def test_croatian_kuna_default(amount, result, printed):
        default = CroatianKuna(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'HRK'
        assert default.numeric_code == '191'
        assert default.symbol == 'Kn'
        assert default.localized_symbol == 'Kn'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'HRK',
            '191'))
        assert default.__repr__() == (
            'CroatianKuna('
            f'amount: {result}, '
            'alpha_code: "HRK", '
            'numeric_code: "191", '
            'symbol: "Kn", '
            'localized_symbol: "Kn", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Kn10.00,00000'),
        (-1000, 'Kn10.00,00000-')
    ])
    def test_croatian_kuna_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CroatianKuna(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'HRK'
        assert custom.numeric_code == '191'
        assert custom.symbol == 'Kn'
        assert custom.localized_symbol == 'Kn'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'HRK',
            '191'))
        assert custom.__repr__() == (
            'CroatianKuna('
            f'amount: {amount}, '
            'alpha_code: "HRK", '
            'numeric_code: "191", '
            'symbol: "Kn", '
            'localized_symbol: "Kn", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_croatian_kuna_recreate(amount, new_amount):
        default = CroatianKuna(amount)
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
    def test_croatian_kuna_change_attributes(attribute, value):
        immutable = CroatianKuna(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CroatianKuna\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_croatian_kuna_add_attributes(attribute, value):
        immutable = CroatianKuna(1000)
        with raises(
                AttributeError,
                match=f'\'CroatianKuna\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (croatian_kuna_one, croatian_kuna_one, croatian_kuna_two, None),
        (croatian_kuna_one, croatian_kuna_one_other, croatian_kuna_two, None),
        (croatian_kuna_two, croatian_kuna_minus_one, croatian_kuna_one, None),
        (croatian_kuna_one, other, None, CurrencyMismatchException),
        (croatian_kuna_one, 1.00, None, CurrencyTypeException),
        (croatian_kuna_one, '1.00', None, CurrencyTypeException)
    ])
    def test_croatian_kuna_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (croatian_kuna_one)
    ])
    def test_croatian_kuna_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'HRK'
        assert new.numeric_code == '191'
        assert new.symbol == 'Kn'
        assert new.localized_symbol == 'Kn'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'
