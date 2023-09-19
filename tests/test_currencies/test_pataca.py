# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pataca currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.pataca import Pataca


class TestPataca:
    """Pataca currency tests."""

    pataca_minus_one = Pataca(-1)
    pataca_one_other = Pataca(1)
    pataca_one = Pataca(1)
    pataca_two = Pataca(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'P\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'P\xa03.14'),
        (10, '10', 'P\xa010.00'),
        (Decimal('10'), '10', 'P\xa010.00'),
        ('-3.14', '-3.14', 'P\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'P\xa0-3.14'),
        (-10, '-10', 'P\xa0-10.00'),
        (Decimal('-10'), '-10', 'P\xa0-10.00')
    ])
    def test_pataca_default(amount, result, printed):
        default = Pataca(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MOP'
        assert default.numeric_code == '446'
        assert default.symbol == 'P'
        assert default.localized_symbol == 'P'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MOP',
            '446'))
        assert default.__repr__() == (
            'Pataca('
            f'amount: {result}, '
            'alpha_code: "MOP", '
            'numeric_code: "446", '
            'symbol: "P", '
            'localized_symbol: "P", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'P10.00,00000'),
        (-1000, 'P10.00,00000-')
    ])
    def test_pataca_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Pataca(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MOP'
        assert custom.numeric_code == '446'
        assert custom.symbol == 'P'
        assert custom.localized_symbol == 'P'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MOP',
            '446'))
        assert custom.__repr__() == (
            'Pataca('
            f'amount: {amount}, '
            'alpha_code: "MOP", '
            'numeric_code: "446", '
            'symbol: "P", '
            'localized_symbol: "P", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pataca_recreate(amount, new_amount):
        default = Pataca(amount)
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
    def test_pataca_change_attributes(attribute, value):
        immutable = Pataca(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Pataca\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pataca_add_attributes(attribute, value):
        immutable = Pataca(1000)
        with raises(
                AttributeError,
                match=f'\'Pataca\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pataca_one, pataca_one, pataca_two, None),
        (pataca_one, pataca_one_other, pataca_two, None),
        (pataca_two, pataca_minus_one, pataca_one, None),
        (pataca_one, other, None, CurrencyMismatchException),
        (pataca_one, 1.00, None, CurrencyTypeException),
        (pataca_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pataca_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pataca_one)
    ])
    def test_pataca_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MOP'
        assert new.numeric_code == '446'
        assert new.symbol == 'P'
        assert new.localized_symbol == 'P'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
