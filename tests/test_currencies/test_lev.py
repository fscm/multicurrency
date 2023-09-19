# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lev currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lev import BulgarianLev


class TestBulgarianLev:
    """Bulgarian Lev currency tests."""

    bulgarian_lev_minus_one = BulgarianLev(-1)
    bulgarian_lev_one_other = BulgarianLev(1)
    bulgarian_lev_one = BulgarianLev(1)
    bulgarian_lev_two = BulgarianLev(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0лв.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0лв.'),
        (10, '10', '10,00\xa0лв.'),
        (Decimal('10'), '10', '10,00\xa0лв.'),
        ('-3.14', '-3.14', '-3,14\xa0лв.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0лв.'),
        (-10, '-10', '-10,00\xa0лв.'),
        (Decimal('-10'), '-10', '-10,00\xa0лв.')
    ])
    def test_bulgarian_lev_default(amount, result, printed):
        default = BulgarianLev(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BGN'
        assert default.numeric_code == '975'
        assert default.symbol == 'лв.'
        assert default.localized_symbol == 'лв.'
        assert default.convertion == ''
        assert default.pattern == '2,\u00A03%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BGN',
            '975'))
        assert default.__repr__() == (
            'BulgarianLev('
            f'amount: {result}, '
            'alpha_code: "BGN", '
            'numeric_code: "975", '
            'symbol: "лв.", '
            'localized_symbol: "лв.", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'лв.10.00,00000'),
        (-1000, 'лв.10.00,00000-')
    ])
    def test_bulgarian_lev_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BulgarianLev(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BGN'
        assert custom.numeric_code == '975'
        assert custom.symbol == 'лв.'
        assert custom.localized_symbol == 'лв.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BGN',
            '975'))
        assert custom.__repr__() == (
            'BulgarianLev('
            f'amount: {amount}, '
            'alpha_code: "BGN", '
            'numeric_code: "975", '
            'symbol: "лв.", '
            'localized_symbol: "лв.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bulgarian_lev_recreate(amount, new_amount):
        default = BulgarianLev(amount)
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
    def test_bulgarian_lev_change_attributes(attribute, value):
        immutable = BulgarianLev(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BulgarianLev\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bulgarian_lev_add_attributes(attribute, value):
        immutable = BulgarianLev(1000)
        with raises(
                AttributeError,
                match=f'\'BulgarianLev\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bulgarian_lev_one, bulgarian_lev_one, bulgarian_lev_two, None),
        (bulgarian_lev_one, bulgarian_lev_one_other, bulgarian_lev_two, None),
        (bulgarian_lev_two, bulgarian_lev_minus_one, bulgarian_lev_one, None),
        (bulgarian_lev_one, other, None, CurrencyMismatchException),
        (bulgarian_lev_one, 1.00, None, CurrencyTypeException),
        (bulgarian_lev_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bulgarian_lev_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bulgarian_lev_one)
    ])
    def test_bulgarian_lev_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BGN'
        assert new.numeric_code == '975'
        assert new.symbol == 'лв.'
        assert new.localized_symbol == 'лв.'
        assert new.convertion == ''
        assert new.pattern == '2,\u00A03%a\u00A0%s'
