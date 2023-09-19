# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Vatu currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.vatu import Vatu


class TestVatu:
    """Vatu currency tests."""

    vatu_minus_one = Vatu(-1)
    vatu_one_other = Vatu(1)
    vatu_one = Vatu(1)
    vatu_two = Vatu(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Vt\xa03'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Vt\xa03'),
        (10, '10', 'Vt\xa010'),
        (Decimal('10'), '10', 'Vt\xa010'),
        ('-3.14', '-3.14', 'Vt\xa0-3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Vt\xa0-3'),
        (-10, '-10', 'Vt\xa0-10'),
        (Decimal('-10'), '-10', 'Vt\xa0-10')
    ])
    def test_vatu_default(amount, result, printed):
        default = Vatu(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'VUV'
        assert default.numeric_code == '548'
        assert default.symbol == 'Vt'
        assert default.localized_symbol == 'Vt'
        assert default.convertion == ''
        assert default.pattern == '0.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'VUV',
            '548'))
        assert default.__repr__() == (
            'Vatu('
            f'amount: {result}, '
            'alpha_code: "VUV", '
            'numeric_code: "548", '
            'symbol: "Vt", '
            'localized_symbol: "Vt", '
            'convertion: "", '
            'pattern: "0.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Vt10.00,00000'),
        (-1000, 'Vt10.00,00000-')
    ])
    def test_vatu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Vatu(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'VUV'
        assert custom.numeric_code == '548'
        assert custom.symbol == 'Vt'
        assert custom.localized_symbol == 'Vt'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'VUV',
            '548'))
        assert custom.__repr__() == (
            'Vatu('
            f'amount: {amount}, '
            'alpha_code: "VUV", '
            'numeric_code: "548", '
            'symbol: "Vt", '
            'localized_symbol: "Vt", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_vatu_recreate(amount, new_amount):
        default = Vatu(amount)
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
    def test_vatu_change_attributes(attribute, value):
        immutable = Vatu(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Vatu\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_vatu_add_attributes(attribute, value):
        immutable = Vatu(1000)
        with raises(
                AttributeError,
                match=f'\'Vatu\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (vatu_one, vatu_one, vatu_two, None),
        (vatu_one, vatu_one_other, vatu_two, None),
        (vatu_two, vatu_minus_one, vatu_one, None),
        (vatu_one, other, None, CurrencyMismatchException),
        (vatu_one, 1.00, None, CurrencyTypeException),
        (vatu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_vatu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (vatu_one)
    ])
    def test_vatu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'VUV'
        assert new.numeric_code == '548'
        assert new.symbol == 'Vt'
        assert new.localized_symbol == 'Vt'
        assert new.convertion == ''
        assert new.pattern == '0.,3%s\u00A0%a'
