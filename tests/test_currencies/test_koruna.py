# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Koruna currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.koruna import CzechKoruna


class TestCzechKoruna:
    """Czech Koruna currency tests."""

    czech_koruna_minus_one = CzechKoruna(-1)
    czech_koruna_one_other = CzechKoruna(1)
    czech_koruna_one = CzechKoruna(1)
    czech_koruna_two = CzechKoruna(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Kč'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Kč'),
        (10, '10', '10,00\xa0Kč'),
        (Decimal('10'), '10', '10,00\xa0Kč'),
        ('-3.14', '-3.14', '-3,14\xa0Kč'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Kč'),
        (-10, '-10', '-10,00\xa0Kč'),
        (Decimal('-10'), '-10', '-10,00\xa0Kč')
    ])
    def test_czech_koruna_default(amount, result, printed):
        default = CzechKoruna(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CZK'
        assert default.numeric_code == '203'
        assert default.symbol == 'Kč'
        assert default.localized_symbol == 'Kč'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CZK',
            '203'))
        assert default.__repr__() == (
            'CzechKoruna('
            f'amount: {result}, '
            'alpha_code: "CZK", '
            'numeric_code: "203", '
            'symbol: "Kč", '
            'localized_symbol: "Kč", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Kč10.00,00000'),
        (-1000, 'Kč10.00,00000-')
    ])
    def test_czech_koruna_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CzechKoruna(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CZK'
        assert custom.numeric_code == '203'
        assert custom.symbol == 'Kč'
        assert custom.localized_symbol == 'Kč'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CZK',
            '203'))
        assert custom.__repr__() == (
            'CzechKoruna('
            f'amount: {amount}, '
            'alpha_code: "CZK", '
            'numeric_code: "203", '
            'symbol: "Kč", '
            'localized_symbol: "Kč", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_czech_koruna_recreate(amount, new_amount):
        default = CzechKoruna(amount)
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
    def test_czech_koruna_change_attributes(attribute, value):
        immutable = CzechKoruna(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CzechKoruna\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_czech_koruna_add_attributes(attribute, value):
        immutable = CzechKoruna(1000)
        with raises(
                AttributeError,
                match=f'\'CzechKoruna\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (czech_koruna_one, czech_koruna_one, czech_koruna_two, None),
        (czech_koruna_one, czech_koruna_one_other, czech_koruna_two, None),
        (czech_koruna_two, czech_koruna_minus_one, czech_koruna_one, None),
        (czech_koruna_one, other, None, CurrencyMismatchException),
        (czech_koruna_one, 1.00, None, CurrencyTypeException),
        (czech_koruna_one, '1.00', None, CurrencyTypeException)
    ])
    def test_czech_koruna_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (czech_koruna_one)
    ])
    def test_czech_koruna_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CZK'
        assert new.numeric_code == '203'
        assert new.symbol == 'Kč'
        assert new.localized_symbol == 'Kč'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
