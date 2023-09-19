# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rupiah currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.rupiah import Rupiah


class TestRupiah:
    """Rupiah currency tests."""

    rupiah_minus_one = Rupiah(-1)
    rupiah_one_other = Rupiah(1)
    rupiah_one = Rupiah(1)
    rupiah_two = Rupiah(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Rp\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Rp\xa03,14'),
        (10, '10', 'Rp\xa010,00'),
        (Decimal('10'), '10', 'Rp\xa010,00'),
        ('-3.14', '-3.14', 'Rp\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Rp\xa0-3,14'),
        (-10, '-10', 'Rp\xa0-10,00'),
        (Decimal('-10'), '-10', 'Rp\xa0-10,00')
    ])
    def test_rupiah_default(amount, result, printed):
        default = Rupiah(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'IDR'
        assert default.numeric_code == '360'
        assert default.symbol == 'Rp'
        assert default.localized_symbol == 'Rp'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'IDR',
            '360'))
        assert default.__repr__() == (
            'Rupiah('
            f'amount: {result}, '
            'alpha_code: "IDR", '
            'numeric_code: "360", '
            'symbol: "Rp", '
            'localized_symbol: "Rp", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Rp10.00,00000'),
        (-1000, 'Rp10.00,00000-')
    ])
    def test_rupiah_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Rupiah(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'IDR'
        assert custom.numeric_code == '360'
        assert custom.symbol == 'Rp'
        assert custom.localized_symbol == 'Rp'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'IDR',
            '360'))
        assert custom.__repr__() == (
            'Rupiah('
            f'amount: {amount}, '
            'alpha_code: "IDR", '
            'numeric_code: "360", '
            'symbol: "Rp", '
            'localized_symbol: "Rp", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rupiah_recreate(amount, new_amount):
        default = Rupiah(amount)
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
    def test_rupiah_change_attributes(attribute, value):
        immutable = Rupiah(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Rupiah\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rupiah_add_attributes(attribute, value):
        immutable = Rupiah(1000)
        with raises(
                AttributeError,
                match=f'\'Rupiah\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rupiah_one, rupiah_one, rupiah_two, None),
        (rupiah_one, rupiah_one_other, rupiah_two, None),
        (rupiah_two, rupiah_minus_one, rupiah_one, None),
        (rupiah_one, other, None, CurrencyMismatchException),
        (rupiah_one, 1.00, None, CurrencyTypeException),
        (rupiah_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rupiah_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rupiah_one)
    ])
    def test_rupiah_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'IDR'
        assert new.numeric_code == '360'
        assert new.symbol == 'Rp'
        assert new.localized_symbol == 'Rp'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'
