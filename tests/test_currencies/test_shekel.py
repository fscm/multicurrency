# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Shekel currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.shekel import (
    NewIsraeliShekel,
    NewIsraeliShekelIL,
    NewIsraeliShekelPS)


class TestNewIsraeliShekel:
    """New Israeli Shekel currency tests."""

    new_israeli_shekel_minus_one = NewIsraeliShekel(-1)
    new_israeli_shekel_one_other = NewIsraeliShekel(1)
    new_israeli_shekel_one = NewIsraeliShekel(1)
    new_israeli_shekel_two = NewIsraeliShekel(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3.14\xa0₪'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3.14\xa0₪'),
        (10, '10', '10.00\xa0₪'),
        (Decimal('10'), '10', '10.00\xa0₪'),
        ('-3.14', '-3.14', '-3.14\xa0₪'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3.14\xa0₪'),
        (-10, '-10', '-10.00\xa0₪'),
        (Decimal('-10'), '-10', '-10.00\xa0₪')
    ])
    def test_new_israeli_shekel_default(amount, result, printed):
        default = NewIsraeliShekel(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ILS'
        assert default.numeric_code == '376'
        assert default.symbol == '₪'
        assert default.localized_symbol == '₪'
        assert default.convertion == ''
        assert default.pattern == '2.,3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert default.__repr__() == (
            'NewIsraeliShekel('
            f'amount: {result}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "₪", '
            'convertion: "", '
            'pattern: "2.,3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₪10.00,00000'),
        (-1000, '₪10.00,00000-')
    ])
    def test_new_israeli_shekel_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewIsraeliShekel(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ILS'
        assert custom.numeric_code == '376'
        assert custom.symbol == '₪'
        assert custom.localized_symbol == '₪'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert custom.__repr__() == (
            'NewIsraeliShekel('
            f'amount: {amount}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "₪", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_israeli_shekel_recreate(amount, new_amount):
        default = NewIsraeliShekel(amount)
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
    def test_new_israeli_shekel_change_attributes(attribute, value):
        immutable = NewIsraeliShekel(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewIsraeliShekel\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_israeli_shekel_add_attributes(attribute, value):
        immutable = NewIsraeliShekel(1000)
        with raises(
                AttributeError,
                match=f'\'NewIsraeliShekel\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_israeli_shekel_one, new_israeli_shekel_one, new_israeli_shekel_two, None),
        (new_israeli_shekel_one, new_israeli_shekel_one_other, new_israeli_shekel_two, None),
        (new_israeli_shekel_two, new_israeli_shekel_minus_one, new_israeli_shekel_one, None),
        (new_israeli_shekel_one, other, None, CurrencyMismatchException),
        (new_israeli_shekel_one, 1.00, None, CurrencyTypeException),
        (new_israeli_shekel_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_israeli_shekel_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_israeli_shekel_one)
    ])
    def test_new_israeli_shekel_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ILS'
        assert new.numeric_code == '376'
        assert new.symbol == '₪'
        assert new.localized_symbol == '₪'
        assert new.convertion == ''
        assert new.pattern == '2.,3%a\u00A0%s'


class TestNewIsraeliShekelIL:
    """New Israeli Shekel IL currency tests."""

    new_israeli_shekel_il_minus_one = NewIsraeliShekelIL(-1)
    new_israeli_shekel_il_one_other = NewIsraeliShekelIL(1)
    new_israeli_shekel_il_one = NewIsraeliShekelIL(1)
    new_israeli_shekel_il_two = NewIsraeliShekelIL(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3.14\xa0₪'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3.14\xa0₪'),
        (10, '10', '10.00\xa0₪'),
        (Decimal('10'), '10', '10.00\xa0₪'),
        ('-3.14', '-3.14', '-3.14\xa0₪'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3.14\xa0₪'),
        (-10, '-10', '-10.00\xa0₪'),
        (Decimal('-10'), '-10', '-10.00\xa0₪')
    ])
    def test_new_israeli_shekel_il_default(amount, result, printed):
        default = NewIsraeliShekelIL(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ILS'
        assert default.numeric_code == '376'
        assert default.symbol == '₪'
        assert default.localized_symbol == 'IL₪'
        assert default.convertion == ''
        assert default.pattern == '2.,3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert default.__repr__() == (
            'NewIsraeliShekelIL('
            f'amount: {result}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "IL₪", '
            'convertion: "", '
            'pattern: "2.,3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₪10.00,00000'),
        (-1000, '₪10.00,00000-')
    ])
    def test_new_israeli_shekel_il_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewIsraeliShekelIL(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ILS'
        assert custom.numeric_code == '376'
        assert custom.symbol == '₪'
        assert custom.localized_symbol == 'IL₪'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert custom.__repr__() == (
            'NewIsraeliShekelIL('
            f'amount: {amount}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "IL₪", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_israeli_shekel_il_recreate(amount, new_amount):
        default = NewIsraeliShekelIL(amount)
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
    def test_new_israeli_shekel_il_change_attributes(attribute, value):
        immutable = NewIsraeliShekelIL(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewIsraeliShekelIL\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_israeli_shekel_il_add_attributes(attribute, value):
        immutable = NewIsraeliShekelIL(1000)
        with raises(
                AttributeError,
                match=f'\'NewIsraeliShekelIL\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_israeli_shekel_il_one, new_israeli_shekel_il_one, new_israeli_shekel_il_two, None),
        (new_israeli_shekel_il_one, new_israeli_shekel_il_one_other, new_israeli_shekel_il_two, None),
        (new_israeli_shekel_il_two, new_israeli_shekel_il_minus_one, new_israeli_shekel_il_one, None),
        (new_israeli_shekel_il_one, other, None, CurrencyMismatchException),
        (new_israeli_shekel_il_one, 1.00, None, CurrencyTypeException),
        (new_israeli_shekel_il_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_israeli_shekel_il_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_israeli_shekel_il_one)
    ])
    def test_new_israeli_shekel_il_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ILS'
        assert new.numeric_code == '376'
        assert new.symbol == '₪'
        assert new.localized_symbol == 'IL₪'
        assert new.convertion == ''
        assert new.pattern == '2.,3%a\u00A0%s'


class TestNewIsraeliShekelPS:
    """New Israeli Shekel PS currency tests."""

    new_israeli_shekel_ps_minus_one = NewIsraeliShekelPS(-1)
    new_israeli_shekel_ps_one_other = NewIsraeliShekelPS(1)
    new_israeli_shekel_ps_one = NewIsraeliShekelPS(1)
    new_israeli_shekel_ps_two = NewIsraeliShekelPS(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3.14\xa0₪'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3.14\xa0₪'),
        (10, '10', '10.00\xa0₪'),
        (Decimal('10'), '10', '10.00\xa0₪'),
        ('-3.14', '-3.14', '-3.14\xa0₪'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3.14\xa0₪'),
        (-10, '-10', '-10.00\xa0₪'),
        (Decimal('-10'), '-10', '-10.00\xa0₪')
    ])
    def test_new_israeli_shekel_ps_default(amount, result, printed):
        default = NewIsraeliShekelPS(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ILS'
        assert default.numeric_code == '376'
        assert default.symbol == '₪'
        assert default.localized_symbol == 'PS₪'
        assert default.convertion == ''
        assert default.pattern == '2.,3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert default.__repr__() == (
            'NewIsraeliShekelPS('
            f'amount: {result}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "PS₪", '
            'convertion: "", '
            'pattern: "2.,3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₪10.00,00000'),
        (-1000, '₪10.00,00000-')
    ])
    def test_new_israeli_shekel_ps_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewIsraeliShekelPS(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ILS'
        assert custom.numeric_code == '376'
        assert custom.symbol == '₪'
        assert custom.localized_symbol == 'PS₪'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ILS',
            '376'))
        assert custom.__repr__() == (
            'NewIsraeliShekelPS('
            f'amount: {amount}, '
            'alpha_code: "ILS", '
            'numeric_code: "376", '
            'symbol: "₪", '
            'localized_symbol: "PS₪", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_israeli_shekel_ps_recreate(amount, new_amount):
        default = NewIsraeliShekelPS(amount)
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
    def test_new_israeli_shekel_ps_change_attributes(attribute, value):
        immutable = NewIsraeliShekelPS(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewIsraeliShekelPS\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_israeli_shekel_ps_add_attributes(attribute, value):
        immutable = NewIsraeliShekelPS(1000)
        with raises(
                AttributeError,
                match=f'\'NewIsraeliShekelPS\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_israeli_shekel_ps_one, new_israeli_shekel_ps_one, new_israeli_shekel_ps_two, None),
        (new_israeli_shekel_ps_one, new_israeli_shekel_ps_one_other, new_israeli_shekel_ps_two, None),
        (new_israeli_shekel_ps_two, new_israeli_shekel_ps_minus_one, new_israeli_shekel_ps_one, None),
        (new_israeli_shekel_ps_one, other, None, CurrencyMismatchException),
        (new_israeli_shekel_ps_one, 1.00, None, CurrencyTypeException),
        (new_israeli_shekel_ps_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_israeli_shekel_ps_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_israeli_shekel_ps_one)
    ])
    def test_new_israeli_shekel_ps_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ILS'
        assert new.numeric_code == '376'
        assert new.symbol == '₪'
        assert new.localized_symbol == 'PS₪'
        assert new.convertion == ''
        assert new.pattern == '2.,3%a\u00A0%s'
