# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Marka currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.marka import KonvertibilnaMarka


class TestKonvertibilnaMarka:
    """Konvertibilna Marka currency tests."""

    konvertibilna_marka_minus_one = KonvertibilnaMarka(-1)
    konvertibilna_marka_one_other = KonvertibilnaMarka(1)
    konvertibilna_marka_one = KonvertibilnaMarka(1)
    konvertibilna_marka_two = KonvertibilnaMarka(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3.14\xa0КМ'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3.14\xa0КМ'),
        (10, '10', '10.00\xa0КМ'),
        (Decimal('10'), '10', '10.00\xa0КМ'),
        ('-3.14', '-3.14', '-3.14\xa0КМ'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3.14\xa0КМ'),
        (-10, '-10', '-10.00\xa0КМ'),
        (Decimal('-10'), '-10', '-10.00\xa0КМ')
    ])
    def test_konvertibilna_marka_default(amount, result, printed):
        default = KonvertibilnaMarka(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BAM'
        assert default.numeric_code == '977'
        assert default.symbol == 'КМ'
        assert default.localized_symbol == 'КМ'
        assert default.convertion == ''
        assert default.pattern == '2.,3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BAM',
            '977'))
        assert default.__repr__() == (
            'KonvertibilnaMarka('
            f'amount: {result}, '
            'alpha_code: "BAM", '
            'numeric_code: "977", '
            'symbol: "КМ", '
            'localized_symbol: "КМ", '
            'convertion: "", '
            'pattern: "2.,3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'КМ10.00,00000'),
        (-1000, 'КМ10.00,00000-')
    ])
    def test_konvertibilna_marka_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = KonvertibilnaMarka(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BAM'
        assert custom.numeric_code == '977'
        assert custom.symbol == 'КМ'
        assert custom.localized_symbol == 'КМ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BAM',
            '977'))
        assert custom.__repr__() == (
            'KonvertibilnaMarka('
            f'amount: {amount}, '
            'alpha_code: "BAM", '
            'numeric_code: "977", '
            'symbol: "КМ", '
            'localized_symbol: "КМ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_konvertibilna_marka_recreate(amount, new_amount):
        default = KonvertibilnaMarka(amount)
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
    def test_konvertibilna_marka_change_attributes(attribute, value):
        immutable = KonvertibilnaMarka(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'KonvertibilnaMarka\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_konvertibilna_marka_add_attributes(attribute, value):
        immutable = KonvertibilnaMarka(1000)
        with raises(
                AttributeError,
                match=f'\'KonvertibilnaMarka\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (konvertibilna_marka_one, konvertibilna_marka_one, konvertibilna_marka_two, None),
        (konvertibilna_marka_one, konvertibilna_marka_one_other, konvertibilna_marka_two, None),
        (konvertibilna_marka_two, konvertibilna_marka_minus_one, konvertibilna_marka_one, None),
        (konvertibilna_marka_one, other, None, CurrencyMismatchException),
        (konvertibilna_marka_one, 1.00, None, CurrencyTypeException),
        (konvertibilna_marka_one, '1.00', None, CurrencyTypeException)
    ])
    def test_konvertibilna_marka_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (konvertibilna_marka_one)
    ])
    def test_konvertibilna_marka_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BAM'
        assert new.numeric_code == '977'
        assert new.symbol == 'КМ'
        assert new.localized_symbol == 'КМ'
        assert new.convertion == ''
        assert new.pattern == '2.,3%a\u00A0%s'
