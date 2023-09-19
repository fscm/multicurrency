# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Colon currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.colon import CostaRicanColon


class TestCostaRicanColon:
    """Costa Rican Colon currency tests."""

    costa_rican_colon_minus_one = CostaRicanColon(-1)
    costa_rican_colon_one_other = CostaRicanColon(1)
    costa_rican_colon_one = CostaRicanColon(1)
    costa_rican_colon_two = CostaRicanColon(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₡3,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₡3,14'),
        (10, '10', '₡10,00'),
        (Decimal('10'), '10', '₡10,00'),
        ('-3.14', '-3.14', '-₡3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₡3,14'),
        (-10, '-10', '-₡10,00'),
        (Decimal('-10'), '-10', '-₡10,00')
    ])
    def test_costa_rican_colon_default(amount, result, printed):
        default = CostaRicanColon(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CRC'
        assert default.numeric_code == '188'
        assert default.symbol == '₡'
        assert default.localized_symbol == '₡'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CRC',
            '188'))
        assert default.__repr__() == (
            'CostaRicanColon('
            f'amount: {result}, '
            'alpha_code: "CRC", '
            'numeric_code: "188", '
            'symbol: "₡", '
            'localized_symbol: "₡", '
            'convertion: "", '
            'pattern: "2, 3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₡10.00,00000'),
        (-1000, '₡10.00,00000-')
    ])
    def test_costa_rican_colon_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CostaRicanColon(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CRC'
        assert custom.numeric_code == '188'
        assert custom.symbol == '₡'
        assert custom.localized_symbol == '₡'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CRC',
            '188'))
        assert custom.__repr__() == (
            'CostaRicanColon('
            f'amount: {amount}, '
            'alpha_code: "CRC", '
            'numeric_code: "188", '
            'symbol: "₡", '
            'localized_symbol: "₡", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_costa_rican_colon_recreate(amount, new_amount):
        default = CostaRicanColon(amount)
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
    def test_costa_rican_colon_change_attributes(attribute, value):
        immutable = CostaRicanColon(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CostaRicanColon\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_costa_rican_colon_add_attributes(attribute, value):
        immutable = CostaRicanColon(1000)
        with raises(
                AttributeError,
                match=f'\'CostaRicanColon\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (costa_rican_colon_one, costa_rican_colon_one, costa_rican_colon_two, None),
        (costa_rican_colon_one, costa_rican_colon_one_other, costa_rican_colon_two, None),
        (costa_rican_colon_two, costa_rican_colon_minus_one, costa_rican_colon_one, None),
        (costa_rican_colon_one, other, None, CurrencyMismatchException),
        (costa_rican_colon_one, 1.00, None, CurrencyTypeException),
        (costa_rican_colon_one, '1.00', None, CurrencyTypeException)
    ])
    def test_costa_rican_colon_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (costa_rican_colon_one)
    ])
    def test_costa_rican_colon_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CRC'
        assert new.numeric_code == '188'
        assert new.symbol == '₡'
        assert new.localized_symbol == '₡'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%-%s%u'
