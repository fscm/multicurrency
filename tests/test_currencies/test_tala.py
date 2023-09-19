# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tala currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.tala import Tala


class TestTala:
    """Tala currency tests."""

    tala_minus_one = Tala(-1)
    tala_one_other = Tala(1)
    tala_one = Tala(1)
    tala_two = Tala(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'T\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'T\xa03.14'),
        (10, '10', 'T\xa010.00'),
        (Decimal('10'), '10', 'T\xa010.00'),
        ('-3.14', '-3.14', 'T\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'T\xa0-3.14'),
        (-10, '-10', 'T\xa0-10.00'),
        (Decimal('-10'), '-10', 'T\xa0-10.00')
    ])
    def test_tala_default(amount, result, printed):
        default = Tala(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'WST'
        assert default.numeric_code == '882'
        assert default.symbol == 'T'
        assert default.localized_symbol == 'T'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'WST',
            '882'))
        assert default.__repr__() == (
            'Tala('
            f'amount: {result}, '
            'alpha_code: "WST", '
            'numeric_code: "882", '
            'symbol: "T", '
            'localized_symbol: "T", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'T10.00,00000'),
        (-1000, 'T10.00,00000-')
    ])
    def test_tala_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Tala(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'WST'
        assert custom.numeric_code == '882'
        assert custom.symbol == 'T'
        assert custom.localized_symbol == 'T'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'WST',
            '882'))
        assert custom.__repr__() == (
            'Tala('
            f'amount: {amount}, '
            'alpha_code: "WST", '
            'numeric_code: "882", '
            'symbol: "T", '
            'localized_symbol: "T", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tala_recreate(amount, new_amount):
        default = Tala(amount)
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
    def test_tala_change_attributes(attribute, value):
        immutable = Tala(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Tala\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tala_add_attributes(attribute, value):
        immutable = Tala(1000)
        with raises(
                AttributeError,
                match=f'\'Tala\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tala_one, tala_one, tala_two, None),
        (tala_one, tala_one_other, tala_two, None),
        (tala_two, tala_minus_one, tala_one, None),
        (tala_one, other, None, CurrencyMismatchException),
        (tala_one, 1.00, None, CurrencyTypeException),
        (tala_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tala_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tala_one)
    ])
    def test_tala_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'WST'
        assert new.numeric_code == '882'
        assert new.symbol == 'T'
        assert new.localized_symbol == 'T'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
