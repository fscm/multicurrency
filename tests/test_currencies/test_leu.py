# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leu currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.leu import (
    MoldovanLeu,
    Leu)


class TestMoldovanLeu:
    """Moldovan Leu currency tests."""

    moldovan_leu_minus_one = MoldovanLeu(-1)
    moldovan_leu_one_other = MoldovanLeu(1)
    moldovan_leu_one = MoldovanLeu(1)
    moldovan_leu_two = MoldovanLeu(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0L'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0L'),
        (10, '10', '10,00\xa0L'),
        (Decimal('10'), '10', '10,00\xa0L'),
        ('-3.14', '-3.14', '-3,14\xa0L'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0L'),
        (-10, '-10', '-10,00\xa0L'),
        (Decimal('-10'), '-10', '-10,00\xa0L')
    ])
    def test_moldovan_leu_default(amount, result, printed):
        default = MoldovanLeu(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MDL'
        assert default.numeric_code == '498'
        assert default.symbol == 'L'
        assert default.localized_symbol == 'L'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MDL',
            '498'))
        assert default.__repr__() == (
            'MoldovanLeu('
            f'amount: {result}, '
            'alpha_code: "MDL", '
            'numeric_code: "498", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'L10.00,00000'),
        (-1000, 'L10.00,00000-')
    ])
    def test_moldovan_leu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MoldovanLeu(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MDL'
        assert custom.numeric_code == '498'
        assert custom.symbol == 'L'
        assert custom.localized_symbol == 'L'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MDL',
            '498'))
        assert custom.__repr__() == (
            'MoldovanLeu('
            f'amount: {amount}, '
            'alpha_code: "MDL", '
            'numeric_code: "498", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_moldovan_leu_recreate(amount, new_amount):
        default = MoldovanLeu(amount)
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
    def test_moldovan_leu_change_attributes(attribute, value):
        immutable = MoldovanLeu(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MoldovanLeu\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_moldovan_leu_add_attributes(attribute, value):
        immutable = MoldovanLeu(1000)
        with raises(
                AttributeError,
                match=f'\'MoldovanLeu\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (moldovan_leu_one, moldovan_leu_one, moldovan_leu_two, None),
        (moldovan_leu_one, moldovan_leu_one_other, moldovan_leu_two, None),
        (moldovan_leu_two, moldovan_leu_minus_one, moldovan_leu_one, None),
        (moldovan_leu_one, other, None, CurrencyMismatchException),
        (moldovan_leu_one, 1.00, None, CurrencyTypeException),
        (moldovan_leu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_moldovan_leu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (moldovan_leu_one)
    ])
    def test_moldovan_leu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MDL'
        assert new.numeric_code == '498'
        assert new.symbol == 'L'
        assert new.localized_symbol == 'L'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestLeu:
    """Leu currency tests."""

    leu_minus_one = Leu(-1)
    leu_one_other = Leu(1)
    leu_one = Leu(1)
    leu_two = Leu(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0L'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0L'),
        (10, '10', '10,00\xa0L'),
        (Decimal('10'), '10', '10,00\xa0L'),
        ('-3.14', '-3.14', '-3,14\xa0L'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0L'),
        (-10, '-10', '-10,00\xa0L'),
        (Decimal('-10'), '-10', '-10,00\xa0L')
    ])
    def test_leu_default(amount, result, printed):
        default = Leu(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RON'
        assert default.numeric_code == '946'
        assert default.symbol == 'L'
        assert default.localized_symbol == 'L'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RON',
            '946'))
        assert default.__repr__() == (
            'Leu('
            f'amount: {result}, '
            'alpha_code: "RON", '
            'numeric_code: "946", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'L10.00,00000'),
        (-1000, 'L10.00,00000-')
    ])
    def test_leu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Leu(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RON'
        assert custom.numeric_code == '946'
        assert custom.symbol == 'L'
        assert custom.localized_symbol == 'L'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RON',
            '946'))
        assert custom.__repr__() == (
            'Leu('
            f'amount: {amount}, '
            'alpha_code: "RON", '
            'numeric_code: "946", '
            'symbol: "L", '
            'localized_symbol: "L", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_leu_recreate(amount, new_amount):
        default = Leu(amount)
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
    def test_leu_change_attributes(attribute, value):
        immutable = Leu(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Leu\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_leu_add_attributes(attribute, value):
        immutable = Leu(1000)
        with raises(
                AttributeError,
                match=f'\'Leu\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (leu_one, leu_one, leu_two, None),
        (leu_one, leu_one_other, leu_two, None),
        (leu_two, leu_minus_one, leu_one, None),
        (leu_one, other, None, CurrencyMismatchException),
        (leu_one, 1.00, None, CurrencyTypeException),
        (leu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_leu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (leu_one)
    ])
    def test_leu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RON'
        assert new.numeric_code == '946'
        assert new.symbol == 'L'
        assert new.localized_symbol == 'L'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'
