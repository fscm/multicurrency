# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ruble currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.ruble import (
    BelarusianRuble,
    RussianRuble,
    RussianRubleRU,
    RussianRubleGE)


class TestBelarusianRuble:
    """Belarusian Ruble currency tests."""

    belarusian_ruble_minus_one = BelarusianRuble(-1)
    belarusian_ruble_one_other = BelarusianRuble(1)
    belarusian_ruble_one = BelarusianRuble(1)
    belarusian_ruble_two = BelarusianRuble(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Br'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Br'),
        (10, '10', '10,00\xa0Br'),
        (Decimal('10'), '10', '10,00\xa0Br'),
        ('-3.14', '-3.14', '-3,14\xa0Br'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Br'),
        (-10, '-10', '-10,00\xa0Br'),
        (Decimal('-10'), '-10', '-10,00\xa0Br')
    ])
    def test_belarusian_ruble_default(amount, result, printed):
        default = BelarusianRuble(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BYN'
        assert default.numeric_code == '933'
        assert default.symbol == 'Br'
        assert default.localized_symbol == 'Br'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BYN',
            '933'))
        assert default.__repr__() == (
            'BelarusianRuble('
            f'amount: {result}, '
            'alpha_code: "BYN", '
            'numeric_code: "933", '
            'symbol: "Br", '
            'localized_symbol: "Br", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Br10.00,00000'),
        (-1000, 'Br10.00,00000-')
    ])
    def test_belarusian_ruble_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BelarusianRuble(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BYN'
        assert custom.numeric_code == '933'
        assert custom.symbol == 'Br'
        assert custom.localized_symbol == 'Br'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BYN',
            '933'))
        assert custom.__repr__() == (
            'BelarusianRuble('
            f'amount: {amount}, '
            'alpha_code: "BYN", '
            'numeric_code: "933", '
            'symbol: "Br", '
            'localized_symbol: "Br", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_belarusian_ruble_recreate(amount, new_amount):
        default = BelarusianRuble(amount)
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
    def test_belarusian_ruble_change_attributes(attribute, value):
        immutable = BelarusianRuble(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BelarusianRuble\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_belarusian_ruble_add_attributes(attribute, value):
        immutable = BelarusianRuble(1000)
        with raises(
                AttributeError,
                match=f'\'BelarusianRuble\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (belarusian_ruble_one, belarusian_ruble_one, belarusian_ruble_two, None),
        (belarusian_ruble_one, belarusian_ruble_one_other, belarusian_ruble_two, None),
        (belarusian_ruble_two, belarusian_ruble_minus_one, belarusian_ruble_one, None),
        (belarusian_ruble_one, other, None, CurrencyMismatchException),
        (belarusian_ruble_one, 1.00, None, CurrencyTypeException),
        (belarusian_ruble_one, '1.00', None, CurrencyTypeException)
    ])
    def test_belarusian_ruble_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (belarusian_ruble_one)
    ])
    def test_belarusian_ruble_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BYN'
        assert new.numeric_code == '933'
        assert new.symbol == 'Br'
        assert new.localized_symbol == 'Br'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestRussianRuble:
    """Russian Ruble currency tests."""

    russian_ruble_minus_one = RussianRuble(-1)
    russian_ruble_one_other = RussianRuble(1)
    russian_ruble_one = RussianRuble(1)
    russian_ruble_two = RussianRuble(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0₽'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0₽'),
        (10, '10', '10,00\xa0₽'),
        (Decimal('10'), '10', '10,00\xa0₽'),
        ('-3.14', '-3.14', '-3,14\xa0₽'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0₽'),
        (-10, '-10', '-10,00\xa0₽'),
        (Decimal('-10'), '-10', '-10,00\xa0₽')
    ])
    def test_russian_ruble_default(amount, result, printed):
        default = RussianRuble(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RUB'
        assert default.numeric_code == '643'
        assert default.symbol == '₽'
        assert default.localized_symbol == '₽'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert default.__repr__() == (
            'RussianRuble('
            f'amount: {result}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "₽", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₽10.00,00000'),
        (-1000, '₽10.00,00000-')
    ])
    def test_russian_ruble_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RussianRuble(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RUB'
        assert custom.numeric_code == '643'
        assert custom.symbol == '₽'
        assert custom.localized_symbol == '₽'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert custom.__repr__() == (
            'RussianRuble('
            f'amount: {amount}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "₽", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_russian_ruble_recreate(amount, new_amount):
        default = RussianRuble(amount)
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
    def test_russian_ruble_change_attributes(attribute, value):
        immutable = RussianRuble(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RussianRuble\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_russian_ruble_add_attributes(attribute, value):
        immutable = RussianRuble(1000)
        with raises(
                AttributeError,
                match=f'\'RussianRuble\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (russian_ruble_one, russian_ruble_one, russian_ruble_two, None),
        (russian_ruble_one, russian_ruble_one_other, russian_ruble_two, None),
        (russian_ruble_two, russian_ruble_minus_one, russian_ruble_one, None),
        (russian_ruble_one, other, None, CurrencyMismatchException),
        (russian_ruble_one, 1.00, None, CurrencyTypeException),
        (russian_ruble_one, '1.00', None, CurrencyTypeException)
    ])
    def test_russian_ruble_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (russian_ruble_one)
    ])
    def test_russian_ruble_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RUB'
        assert new.numeric_code == '643'
        assert new.symbol == '₽'
        assert new.localized_symbol == '₽'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestRussianRubleRU:
    """Russian Ruble RU currency tests."""

    russian_ruble_ru_minus_one = RussianRubleRU(-1)
    russian_ruble_ru_one_other = RussianRubleRU(1)
    russian_ruble_ru_one = RussianRubleRU(1)
    russian_ruble_ru_two = RussianRubleRU(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0₽'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0₽'),
        (10, '10', '10,00\xa0₽'),
        (Decimal('10'), '10', '10,00\xa0₽'),
        ('-3.14', '-3.14', '-3,14\xa0₽'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0₽'),
        (-10, '-10', '-10,00\xa0₽'),
        (Decimal('-10'), '-10', '-10,00\xa0₽')
    ])
    def test_russian_ruble_ru_default(amount, result, printed):
        default = RussianRubleRU(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RUB'
        assert default.numeric_code == '643'
        assert default.symbol == '₽'
        assert default.localized_symbol == 'RU₽'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert default.__repr__() == (
            'RussianRubleRU('
            f'amount: {result}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "RU₽", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₽10.00,00000'),
        (-1000, '₽10.00,00000-')
    ])
    def test_russian_ruble_ru_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RussianRubleRU(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RUB'
        assert custom.numeric_code == '643'
        assert custom.symbol == '₽'
        assert custom.localized_symbol == 'RU₽'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert custom.__repr__() == (
            'RussianRubleRU('
            f'amount: {amount}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "RU₽", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_russian_ruble_ru_recreate(amount, new_amount):
        default = RussianRubleRU(amount)
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
    def test_russian_ruble_ru_change_attributes(attribute, value):
        immutable = RussianRubleRU(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RussianRubleRU\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_russian_ruble_ru_add_attributes(attribute, value):
        immutable = RussianRubleRU(1000)
        with raises(
                AttributeError,
                match=f'\'RussianRubleRU\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (russian_ruble_ru_one, russian_ruble_ru_one, russian_ruble_ru_two, None),
        (russian_ruble_ru_one, russian_ruble_ru_one_other, russian_ruble_ru_two, None),
        (russian_ruble_ru_two, russian_ruble_ru_minus_one, russian_ruble_ru_one, None),
        (russian_ruble_ru_one, other, None, CurrencyMismatchException),
        (russian_ruble_ru_one, 1.00, None, CurrencyTypeException),
        (russian_ruble_ru_one, '1.00', None, CurrencyTypeException)
    ])
    def test_russian_ruble_ru_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (russian_ruble_ru_one)
    ])
    def test_russian_ruble_ru_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RUB'
        assert new.numeric_code == '643'
        assert new.symbol == '₽'
        assert new.localized_symbol == 'RU₽'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestRussianRubleGE:
    """Russian Ruble GE currency tests."""

    russian_ruble_ge_minus_one = RussianRubleGE(-1)
    russian_ruble_ge_one_other = RussianRubleGE(1)
    russian_ruble_ge_one = RussianRubleGE(1)
    russian_ruble_ge_two = RussianRubleGE(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0₽'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0₽'),
        (10, '10', '10,00\xa0₽'),
        (Decimal('10'), '10', '10,00\xa0₽'),
        ('-3.14', '-3.14', '-3,14\xa0₽'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0₽'),
        (-10, '-10', '-10,00\xa0₽'),
        (Decimal('-10'), '-10', '-10,00\xa0₽')
    ])
    def test_russian_ruble_ge_default(amount, result, printed):
        default = RussianRubleGE(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RUB'
        assert default.numeric_code == '643'
        assert default.symbol == '₽'
        assert default.localized_symbol == 'GE₽'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert default.__repr__() == (
            'RussianRubleGE('
            f'amount: {result}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "GE₽", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₽10.00,00000'),
        (-1000, '₽10.00,00000-')
    ])
    def test_russian_ruble_ge_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RussianRubleGE(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RUB'
        assert custom.numeric_code == '643'
        assert custom.symbol == '₽'
        assert custom.localized_symbol == 'GE₽'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RUB',
            '643'))
        assert custom.__repr__() == (
            'RussianRubleGE('
            f'amount: {amount}, '
            'alpha_code: "RUB", '
            'numeric_code: "643", '
            'symbol: "₽", '
            'localized_symbol: "GE₽", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_russian_ruble_ge_recreate(amount, new_amount):
        default = RussianRubleGE(amount)
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
    def test_russian_ruble_ge_change_attributes(attribute, value):
        immutable = RussianRubleGE(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RussianRubleGE\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_russian_ruble_ge_add_attributes(attribute, value):
        immutable = RussianRubleGE(1000)
        with raises(
                AttributeError,
                match=f'\'RussianRubleGE\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (russian_ruble_ge_one, russian_ruble_ge_one, russian_ruble_ge_two, None),
        (russian_ruble_ge_one, russian_ruble_ge_one_other, russian_ruble_ge_two, None),
        (russian_ruble_ge_two, russian_ruble_ge_minus_one, russian_ruble_ge_one, None),
        (russian_ruble_ge_one, other, None, CurrencyMismatchException),
        (russian_ruble_ge_one, 1.00, None, CurrencyTypeException),
        (russian_ruble_ge_one, '1.00', None, CurrencyTypeException)
    ])
    def test_russian_ruble_ge_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (russian_ruble_ge_one)
    ])
    def test_russian_ruble_ge_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RUB'
        assert new.numeric_code == '643'
        assert new.symbol == '₽'
        assert new.localized_symbol == 'GE₽'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
