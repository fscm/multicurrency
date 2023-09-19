# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rand currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.rand import (
    Rand,
    RandLS,
    RandNA,
    RandZA)


class TestRand:
    """Rand currency tests."""

    rand_minus_one = Rand(-1)
    rand_one_other = Rand(1)
    rand_one = Rand(1)
    rand_two = Rand(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'R\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'R\xa03.14'),
        (10, '10', 'R\xa010.00'),
        (Decimal('10'), '10', 'R\xa010.00'),
        ('-3.14', '-3.14', 'R\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'R\xa0-3.14'),
        (-10, '-10', 'R\xa0-10.00'),
        (Decimal('-10'), '-10', 'R\xa0-10.00')
    ])
    def test_rand_default(amount, result, printed):
        default = Rand(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZAR'
        assert default.numeric_code == '710'
        assert default.symbol == 'R'
        assert default.localized_symbol == 'R'
        assert default.convertion == ''
        assert default.pattern == '2.\u202F3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert default.__repr__() == (
            'Rand('
            f'amount: {result}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "R", '
            'convertion: "", '
            'pattern: "2. 3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'R10.00,00000'),
        (-1000, 'R10.00,00000-')
    ])
    def test_rand_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Rand(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZAR'
        assert custom.numeric_code == '710'
        assert custom.symbol == 'R'
        assert custom.localized_symbol == 'R'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert custom.__repr__() == (
            'Rand('
            f'amount: {amount}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "R", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rand_recreate(amount, new_amount):
        default = Rand(amount)
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
    def test_rand_change_attributes(attribute, value):
        immutable = Rand(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Rand\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rand_add_attributes(attribute, value):
        immutable = Rand(1000)
        with raises(
                AttributeError,
                match=f'\'Rand\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rand_one, rand_one, rand_two, None),
        (rand_one, rand_one_other, rand_two, None),
        (rand_two, rand_minus_one, rand_one, None),
        (rand_one, other, None, CurrencyMismatchException),
        (rand_one, 1.00, None, CurrencyTypeException),
        (rand_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rand_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rand_one)
    ])
    def test_rand_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZAR'
        assert new.numeric_code == '710'
        assert new.symbol == 'R'
        assert new.localized_symbol == 'R'
        assert new.convertion == ''
        assert new.pattern == '2.\u202F3%s\u00A0%a'


class TestRandLS:
    """Rand LS currency tests."""

    rand_ls_minus_one = RandLS(-1)
    rand_ls_one_other = RandLS(1)
    rand_ls_one = RandLS(1)
    rand_ls_two = RandLS(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'R\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'R\xa03.14'),
        (10, '10', 'R\xa010.00'),
        (Decimal('10'), '10', 'R\xa010.00'),
        ('-3.14', '-3.14', 'R\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'R\xa0-3.14'),
        (-10, '-10', 'R\xa0-10.00'),
        (Decimal('-10'), '-10', 'R\xa0-10.00')
    ])
    def test_rand_ls_default(amount, result, printed):
        default = RandLS(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZAR'
        assert default.numeric_code == '710'
        assert default.symbol == 'R'
        assert default.localized_symbol == 'LSR'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert default.__repr__() == (
            'RandLS('
            f'amount: {result}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "LSR", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'R10.00,00000'),
        (-1000, 'R10.00,00000-')
    ])
    def test_rand_ls_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RandLS(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZAR'
        assert custom.numeric_code == '710'
        assert custom.symbol == 'R'
        assert custom.localized_symbol == 'LSR'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert custom.__repr__() == (
            'RandLS('
            f'amount: {amount}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "LSR", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rand_ls_recreate(amount, new_amount):
        default = RandLS(amount)
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
    def test_rand_ls_change_attributes(attribute, value):
        immutable = RandLS(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RandLS\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rand_ls_add_attributes(attribute, value):
        immutable = RandLS(1000)
        with raises(
                AttributeError,
                match=f'\'RandLS\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rand_ls_one, rand_ls_one, rand_ls_two, None),
        (rand_ls_one, rand_ls_one_other, rand_ls_two, None),
        (rand_ls_two, rand_ls_minus_one, rand_ls_one, None),
        (rand_ls_one, other, None, CurrencyMismatchException),
        (rand_ls_one, 1.00, None, CurrencyTypeException),
        (rand_ls_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rand_ls_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rand_ls_one)
    ])
    def test_rand_ls_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZAR'
        assert new.numeric_code == '710'
        assert new.symbol == 'R'
        assert new.localized_symbol == 'LSR'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestRandNA:
    """Rand NA currency tests."""

    rand_na_minus_one = RandNA(-1)
    rand_na_one_other = RandNA(1)
    rand_na_one = RandNA(1)
    rand_na_two = RandNA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'R\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'R\xa03.14'),
        (10, '10', 'R\xa010.00'),
        (Decimal('10'), '10', 'R\xa010.00'),
        ('-3.14', '-3.14', 'R\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'R\xa0-3.14'),
        (-10, '-10', 'R\xa0-10.00'),
        (Decimal('-10'), '-10', 'R\xa0-10.00')
    ])
    def test_rand_na_default(amount, result, printed):
        default = RandNA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZAR'
        assert default.numeric_code == '710'
        assert default.symbol == 'R'
        assert default.localized_symbol == 'NAR'
        assert default.convertion == ''
        assert default.pattern == '2.\u202F3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert default.__repr__() == (
            'RandNA('
            f'amount: {result}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "NAR", '
            'convertion: "", '
            'pattern: "2. 3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'R10.00,00000'),
        (-1000, 'R10.00,00000-')
    ])
    def test_rand_na_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RandNA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZAR'
        assert custom.numeric_code == '710'
        assert custom.symbol == 'R'
        assert custom.localized_symbol == 'NAR'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert custom.__repr__() == (
            'RandNA('
            f'amount: {amount}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "NAR", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rand_na_recreate(amount, new_amount):
        default = RandNA(amount)
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
    def test_rand_na_change_attributes(attribute, value):
        immutable = RandNA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RandNA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rand_na_add_attributes(attribute, value):
        immutable = RandNA(1000)
        with raises(
                AttributeError,
                match=f'\'RandNA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rand_na_one, rand_na_one, rand_na_two, None),
        (rand_na_one, rand_na_one_other, rand_na_two, None),
        (rand_na_two, rand_na_minus_one, rand_na_one, None),
        (rand_na_one, other, None, CurrencyMismatchException),
        (rand_na_one, 1.00, None, CurrencyTypeException),
        (rand_na_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rand_na_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rand_na_one)
    ])
    def test_rand_na_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZAR'
        assert new.numeric_code == '710'
        assert new.symbol == 'R'
        assert new.localized_symbol == 'NAR'
        assert new.convertion == ''
        assert new.pattern == '2.\u202F3%s\u00A0%a'


class TestRandZA:
    """Rand ZA currency tests."""

    rand_za_minus_one = RandZA(-1)
    rand_za_one_other = RandZA(1)
    rand_za_one = RandZA(1)
    rand_za_two = RandZA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'R\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'R\xa03.14'),
        (10, '10', 'R\xa010.00'),
        (Decimal('10'), '10', 'R\xa010.00'),
        ('-3.14', '-3.14', 'R\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'R\xa0-3.14'),
        (-10, '-10', 'R\xa0-10.00'),
        (Decimal('-10'), '-10', 'R\xa0-10.00')
    ])
    def test_rand_za_default(amount, result, printed):
        default = RandZA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZAR'
        assert default.numeric_code == '710'
        assert default.symbol == 'R'
        assert default.localized_symbol == 'ZAR'
        assert default.convertion == ''
        assert default.pattern == '2.\u202F3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert default.__repr__() == (
            'RandZA('
            f'amount: {result}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "ZAR", '
            'convertion: "", '
            'pattern: "2. 3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'R10.00,00000'),
        (-1000, 'R10.00,00000-')
    ])
    def test_rand_za_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RandZA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZAR'
        assert custom.numeric_code == '710'
        assert custom.symbol == 'R'
        assert custom.localized_symbol == 'ZAR'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZAR',
            '710'))
        assert custom.__repr__() == (
            'RandZA('
            f'amount: {amount}, '
            'alpha_code: "ZAR", '
            'numeric_code: "710", '
            'symbol: "R", '
            'localized_symbol: "ZAR", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rand_za_recreate(amount, new_amount):
        default = RandZA(amount)
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
    def test_rand_za_change_attributes(attribute, value):
        immutable = RandZA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RandZA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rand_za_add_attributes(attribute, value):
        immutable = RandZA(1000)
        with raises(
                AttributeError,
                match=f'\'RandZA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rand_za_one, rand_za_one, rand_za_two, None),
        (rand_za_one, rand_za_one_other, rand_za_two, None),
        (rand_za_two, rand_za_minus_one, rand_za_one, None),
        (rand_za_one, other, None, CurrencyMismatchException),
        (rand_za_one, 1.00, None, CurrencyTypeException),
        (rand_za_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rand_za_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rand_za_one)
    ])
    def test_rand_za_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZAR'
        assert new.numeric_code == '710'
        assert new.symbol == 'R'
        assert new.localized_symbol == 'ZAR'
        assert new.convertion == ''
        assert new.pattern == '2.\u202F3%s\u00A0%a'
