# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Forint currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.forint import Forint


class TestForint:
    """Forint currency tests."""

    forint_minus_one = Forint(-1)
    forint_one_other = Forint(1)
    forint_one = Forint(1)
    forint_two = Forint(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0Ft'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0Ft'),
        (10, '10', '10\xa0Ft'),
        (Decimal('10'), '10', '10\xa0Ft'),
        ('-3.14', '-3.14', '-3\xa0Ft'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0Ft'),
        (-10, '-10', '-10\xa0Ft'),
        (Decimal('-10'), '-10', '-10\xa0Ft')
    ])
    def test_forint_default(amount, result, printed):
        default = Forint(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'HUF'
        assert default.numeric_code == '348'
        assert default.symbol == 'Ft'
        assert default.localized_symbol == 'Ft'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'HUF',
            '348'))
        assert default.__repr__() == (
            'Forint('
            f'amount: {result}, '
            'alpha_code: "HUF", '
            'numeric_code: "348", '
            'symbol: "Ft", '
            'localized_symbol: "Ft", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Ft10.00,00000'),
        (-1000, 'Ft10.00,00000-')
    ])
    def test_forint_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Forint(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'HUF'
        assert custom.numeric_code == '348'
        assert custom.symbol == 'Ft'
        assert custom.localized_symbol == 'Ft'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'HUF',
            '348'))
        assert custom.__repr__() == (
            'Forint('
            f'amount: {amount}, '
            'alpha_code: "HUF", '
            'numeric_code: "348", '
            'symbol: "Ft", '
            'localized_symbol: "Ft", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_forint_recreate(amount, new_amount):
        default = Forint(amount)
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
    def test_forint_change_attributes(attribute, value):
        immutable = Forint(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Forint\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_forint_add_attributes(attribute, value):
        immutable = Forint(1000)
        with raises(
                AttributeError,
                match=f'\'Forint\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (forint_one, forint_one, forint_two, None),
        (forint_one, forint_one_other, forint_two, None),
        (forint_two, forint_minus_one, forint_one, None),
        (forint_one, other, None, CurrencyMismatchException),
        (forint_one, 1.00, None, CurrencyTypeException),
        (forint_one, '1.00', None, CurrencyTypeException)
    ])
    def test_forint_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (forint_one)
    ])
    def test_forint_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'HUF'
        assert new.numeric_code == '348'
        assert new.symbol == 'Ft'
        assert new.localized_symbol == 'Ft'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'
