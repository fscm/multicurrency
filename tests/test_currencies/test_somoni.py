# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Somoni currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.somoni import Somoni


class TestSomoni:
    """Somoni currency tests."""

    somoni_minus_one = Somoni(-1)
    somoni_one_other = Somoni(1)
    somoni_one = Somoni(1)
    somoni_two = Somoni(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ЅМ\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ЅМ\xa03.14'),
        (10, '10', 'ЅМ\xa010.00'),
        (Decimal('10'), '10', 'ЅМ\xa010.00'),
        ('-3.14', '-3.14', 'ЅМ\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ЅМ\xa0-3.14'),
        (-10, '-10', 'ЅМ\xa0-10.00'),
        (Decimal('-10'), '-10', 'ЅМ\xa0-10.00')
    ])
    def test_somoni_default(amount, result, printed):
        default = Somoni(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TJS'
        assert default.numeric_code == '972'
        assert default.symbol == 'ЅМ'
        assert default.localized_symbol == 'ЅМ'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TJS',
            '972'))
        assert default.__repr__() == (
            'Somoni('
            f'amount: {result}, '
            'alpha_code: "TJS", '
            'numeric_code: "972", '
            'symbol: "ЅМ", '
            'localized_symbol: "ЅМ", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ЅМ10.00,00000'),
        (-1000, 'ЅМ10.00,00000-')
    ])
    def test_somoni_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Somoni(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TJS'
        assert custom.numeric_code == '972'
        assert custom.symbol == 'ЅМ'
        assert custom.localized_symbol == 'ЅМ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TJS',
            '972'))
        assert custom.__repr__() == (
            'Somoni('
            f'amount: {amount}, '
            'alpha_code: "TJS", '
            'numeric_code: "972", '
            'symbol: "ЅМ", '
            'localized_symbol: "ЅМ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_somoni_recreate(amount, new_amount):
        default = Somoni(amount)
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
    def test_somoni_change_attributes(attribute, value):
        immutable = Somoni(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Somoni\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_somoni_add_attributes(attribute, value):
        immutable = Somoni(1000)
        with raises(
                AttributeError,
                match=f'\'Somoni\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (somoni_one, somoni_one, somoni_two, None),
        (somoni_one, somoni_one_other, somoni_two, None),
        (somoni_two, somoni_minus_one, somoni_one, None),
        (somoni_one, other, None, CurrencyMismatchException),
        (somoni_one, 1.00, None, CurrencyTypeException),
        (somoni_one, '1.00', None, CurrencyTypeException)
    ])
    def test_somoni_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (somoni_one)
    ])
    def test_somoni_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TJS'
        assert new.numeric_code == '972'
        assert new.symbol == 'ЅМ'
        assert new.localized_symbol == 'ЅМ'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
