# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dobra currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dobra import Dobra


class TestDobra:
    """Dobra currency tests."""

    dobra_minus_one = Dobra(-1)
    dobra_one_other = Dobra(1)
    dobra_one = Dobra(1)
    dobra_two = Dobra(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Db'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Db'),
        (10, '10', '10,00\xa0Db'),
        (Decimal('10'), '10', '10,00\xa0Db'),
        ('-3.14', '-3.14', '-3,14\xa0Db'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Db'),
        (-10, '-10', '-10,00\xa0Db'),
        (Decimal('-10'), '-10', '-10,00\xa0Db')
    ])
    def test_dobra_default(amount, result, printed):
        default = Dobra(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'STN'
        assert default.numeric_code == '930'
        assert default.symbol == 'Db'
        assert default.localized_symbol == 'Db'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'STN',
            '930'))
        assert default.__repr__() == (
            'Dobra('
            f'amount: {result}, '
            'alpha_code: "STN", '
            'numeric_code: "930", '
            'symbol: "Db", '
            'localized_symbol: "Db", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Db10.00,00000'),
        (-1000, 'Db10.00,00000-')
    ])
    def test_dobra_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Dobra(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'STN'
        assert custom.numeric_code == '930'
        assert custom.symbol == 'Db'
        assert custom.localized_symbol == 'Db'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'STN',
            '930'))
        assert custom.__repr__() == (
            'Dobra('
            f'amount: {amount}, '
            'alpha_code: "STN", '
            'numeric_code: "930", '
            'symbol: "Db", '
            'localized_symbol: "Db", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_dobra_recreate(amount, new_amount):
        default = Dobra(amount)
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
    def test_dobra_change_attributes(attribute, value):
        immutable = Dobra(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Dobra\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_dobra_add_attributes(attribute, value):
        immutable = Dobra(1000)
        with raises(
                AttributeError,
                match=f'\'Dobra\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (dobra_one, dobra_one, dobra_two, None),
        (dobra_one, dobra_one_other, dobra_two, None),
        (dobra_two, dobra_minus_one, dobra_one, None),
        (dobra_one, other, None, CurrencyMismatchException),
        (dobra_one, 1.00, None, CurrencyTypeException),
        (dobra_one, '1.00', None, CurrencyTypeException)
    ])
    def test_dobra_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (dobra_one)
    ])
    def test_dobra_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'STN'
        assert new.numeric_code == '930'
        assert new.symbol == 'Db'
        assert new.localized_symbol == 'Db'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'
