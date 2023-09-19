# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lek currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lek import Lek


class TestLek:
    """Lek currency tests."""

    lek_minus_one = Lek(-1)
    lek_one_other = Lek(1)
    lek_one = Lek(1)
    lek_two = Lek(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Lek'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Lek'),
        (10, '10', '10,00\xa0Lek'),
        (Decimal('10'), '10', '10,00\xa0Lek'),
        ('-3.14', '-3.14', '-3,14\xa0Lek'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Lek'),
        (-10, '-10', '-10,00\xa0Lek'),
        (Decimal('-10'), '-10', '-10,00\xa0Lek')
    ])
    def test_lek_default(amount, result, printed):
        default = Lek(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ALL'
        assert default.numeric_code == '008'
        assert default.symbol == 'Lek'
        assert default.localized_symbol == 'Lek'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ALL',
            '008'))
        assert default.__repr__() == (
            'Lek('
            f'amount: {result}, '
            'alpha_code: "ALL", '
            'numeric_code: "008", '
            'symbol: "Lek", '
            'localized_symbol: "Lek", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Lek10.00,00000'),
        (-1000, 'Lek10.00,00000-')
    ])
    def test_lek_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Lek(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ALL'
        assert custom.numeric_code == '008'
        assert custom.symbol == 'Lek'
        assert custom.localized_symbol == 'Lek'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ALL',
            '008'))
        assert custom.__repr__() == (
            'Lek('
            f'amount: {amount}, '
            'alpha_code: "ALL", '
            'numeric_code: "008", '
            'symbol: "Lek", '
            'localized_symbol: "Lek", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_lek_recreate(amount, new_amount):
        default = Lek(amount)
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
    def test_lek_change_attributes(attribute, value):
        immutable = Lek(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Lek\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_lek_add_attributes(attribute, value):
        immutable = Lek(1000)
        with raises(
                AttributeError,
                match=f'\'Lek\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (lek_one, lek_one, lek_two, None),
        (lek_one, lek_one_other, lek_two, None),
        (lek_two, lek_minus_one, lek_one, None),
        (lek_one, other, None, CurrencyMismatchException),
        (lek_one, 1.00, None, CurrencyTypeException),
        (lek_one, '1.00', None, CurrencyTypeException)
    ])
    def test_lek_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (lek_one)
    ])
    def test_lek_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ALL'
        assert new.numeric_code == '008'
        assert new.symbol == 'Lek'
        assert new.localized_symbol == 'Lek'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
