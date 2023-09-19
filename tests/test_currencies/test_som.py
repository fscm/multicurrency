# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Som currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.som import Som


class TestSom:
    """Som currency tests."""

    som_minus_one = Som(-1)
    som_one_other = Som(1)
    som_one = Som(1)
    som_two = Som(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Лв'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Лв'),
        (10, '10', '10,00\xa0Лв'),
        (Decimal('10'), '10', '10,00\xa0Лв'),
        ('-3.14', '-3.14', '-3,14\xa0Лв'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Лв'),
        (-10, '-10', '-10,00\xa0Лв'),
        (Decimal('-10'), '-10', '-10,00\xa0Лв')
    ])
    def test_som_default(amount, result, printed):
        default = Som(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KGS'
        assert default.numeric_code == '417'
        assert default.symbol == 'Лв'
        assert default.localized_symbol == 'Лв'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KGS',
            '417'))
        assert default.__repr__() == (
            'Som('
            f'amount: {result}, '
            'alpha_code: "KGS", '
            'numeric_code: "417", '
            'symbol: "Лв", '
            'localized_symbol: "Лв", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Лв10.00,00000'),
        (-1000, 'Лв10.00,00000-')
    ])
    def test_som_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Som(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KGS'
        assert custom.numeric_code == '417'
        assert custom.symbol == 'Лв'
        assert custom.localized_symbol == 'Лв'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KGS',
            '417'))
        assert custom.__repr__() == (
            'Som('
            f'amount: {amount}, '
            'alpha_code: "KGS", '
            'numeric_code: "417", '
            'symbol: "Лв", '
            'localized_symbol: "Лв", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_som_recreate(amount, new_amount):
        default = Som(amount)
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
    def test_som_change_attributes(attribute, value):
        immutable = Som(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Som\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_som_add_attributes(attribute, value):
        immutable = Som(1000)
        with raises(
                AttributeError,
                match=f'\'Som\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (som_one, som_one, som_two, None),
        (som_one, som_one_other, som_two, None),
        (som_two, som_minus_one, som_one, None),
        (som_one, other, None, CurrencyMismatchException),
        (som_one, 1.00, None, CurrencyTypeException),
        (som_one, '1.00', None, CurrencyTypeException)
    ])
    def test_som_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (som_one)
    ])
    def test_som_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KGS'
        assert new.numeric_code == '417'
        assert new.symbol == 'Лв'
        assert new.localized_symbol == 'Лв'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
