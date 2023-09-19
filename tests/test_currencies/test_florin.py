# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Florin currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.florin import ArubanFlorin


class TestArubanFlorin:
    """Aruban Florin currency tests."""

    aruban_florin_minus_one = ArubanFlorin(-1)
    aruban_florin_one_other = ArubanFlorin(1)
    aruban_florin_one = ArubanFlorin(1)
    aruban_florin_two = ArubanFlorin(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ƒ3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ƒ3.14'),
        (10, '10', 'ƒ10.00'),
        (Decimal('10'), '10', 'ƒ10.00'),
        ('-3.14', '-3.14', '-ƒ3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-ƒ3.14'),
        (-10, '-10', '-ƒ10.00'),
        (Decimal('-10'), '-10', '-ƒ10.00')
    ])
    def test_aruban_florin_default(amount, result, printed):
        default = ArubanFlorin(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AWG'
        assert default.numeric_code == '533'
        assert default.symbol == 'ƒ'
        assert default.localized_symbol == 'ƒ'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AWG',
            '533'))
        assert default.__repr__() == (
            'ArubanFlorin('
            f'amount: {result}, '
            'alpha_code: "AWG", '
            'numeric_code: "533", '
            'symbol: "ƒ", '
            'localized_symbol: "ƒ", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ƒ10.00,00000'),
        (-1000, 'ƒ10.00,00000-')
    ])
    def test_aruban_florin_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ArubanFlorin(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AWG'
        assert custom.numeric_code == '533'
        assert custom.symbol == 'ƒ'
        assert custom.localized_symbol == 'ƒ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AWG',
            '533'))
        assert custom.__repr__() == (
            'ArubanFlorin('
            f'amount: {amount}, '
            'alpha_code: "AWG", '
            'numeric_code: "533", '
            'symbol: "ƒ", '
            'localized_symbol: "ƒ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_aruban_florin_recreate(amount, new_amount):
        default = ArubanFlorin(amount)
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
    def test_aruban_florin_change_attributes(attribute, value):
        immutable = ArubanFlorin(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ArubanFlorin\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_aruban_florin_add_attributes(attribute, value):
        immutable = ArubanFlorin(1000)
        with raises(
                AttributeError,
                match=f'\'ArubanFlorin\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (aruban_florin_one, aruban_florin_one, aruban_florin_two, None),
        (aruban_florin_one, aruban_florin_one_other, aruban_florin_two, None),
        (aruban_florin_two, aruban_florin_minus_one, aruban_florin_one, None),
        (aruban_florin_one, other, None, CurrencyMismatchException),
        (aruban_florin_one, 1.00, None, CurrencyTypeException),
        (aruban_florin_one, '1.00', None, CurrencyTypeException)
    ])
    def test_aruban_florin_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (aruban_florin_one)
    ])
    def test_aruban_florin_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AWG'
        assert new.numeric_code == '533'
        assert new.symbol == 'ƒ'
        assert new.localized_symbol == 'ƒ'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
