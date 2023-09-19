# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Guarani currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.guarani import Guarani


class TestGuarani:
    """Guarani currency tests."""

    guarani_minus_one = Guarani(-1)
    guarani_one_other = Guarani(1)
    guarani_one = Guarani(1)
    guarani_two = Guarani(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₲\xa03'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₲\xa03'),
        (10, '10', '₲\xa010'),
        (Decimal('10'), '10', '₲\xa010'),
        ('-3.14', '-3.14', '₲\xa0-3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₲\xa0-3'),
        (-10, '-10', '₲\xa0-10'),
        (Decimal('-10'), '-10', '₲\xa0-10')
    ])
    def test_guarani_default(amount, result, printed):
        default = Guarani(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PYG'
        assert default.numeric_code == '600'
        assert default.symbol == '₲'
        assert default.localized_symbol == '₲'
        assert default.convertion == ''
        assert default.pattern == '0,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PYG',
            '600'))
        assert default.__repr__() == (
            'Guarani('
            f'amount: {result}, '
            'alpha_code: "PYG", '
            'numeric_code: "600", '
            'symbol: "₲", '
            'localized_symbol: "₲", '
            'convertion: "", '
            'pattern: "0,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₲10.00,00000'),
        (-1000, '₲10.00,00000-')
    ])
    def test_guarani_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Guarani(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PYG'
        assert custom.numeric_code == '600'
        assert custom.symbol == '₲'
        assert custom.localized_symbol == '₲'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PYG',
            '600'))
        assert custom.__repr__() == (
            'Guarani('
            f'amount: {amount}, '
            'alpha_code: "PYG", '
            'numeric_code: "600", '
            'symbol: "₲", '
            'localized_symbol: "₲", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_guarani_recreate(amount, new_amount):
        default = Guarani(amount)
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
    def test_guarani_change_attributes(attribute, value):
        immutable = Guarani(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Guarani\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_guarani_add_attributes(attribute, value):
        immutable = Guarani(1000)
        with raises(
                AttributeError,
                match=f'\'Guarani\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (guarani_one, guarani_one, guarani_two, None),
        (guarani_one, guarani_one_other, guarani_two, None),
        (guarani_two, guarani_minus_one, guarani_one, None),
        (guarani_one, other, None, CurrencyMismatchException),
        (guarani_one, 1.00, None, CurrencyTypeException),
        (guarani_one, '1.00', None, CurrencyTypeException)
    ])
    def test_guarani_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (guarani_one)
    ])
    def test_guarani_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PYG'
        assert new.numeric_code == '600'
        assert new.symbol == '₲'
        assert new.localized_symbol == '₲'
        assert new.convertion == ''
        assert new.pattern == '0,.3%s\u00A0%a'
