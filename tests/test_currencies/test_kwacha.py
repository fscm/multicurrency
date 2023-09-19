# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwacha currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kwacha import (
    Kwacha,
    ZambianKwacha)


class TestKwacha:
    """Kwacha currency tests."""

    kwacha_minus_one = Kwacha(-1)
    kwacha_one_other = Kwacha(1)
    kwacha_one = Kwacha(1)
    kwacha_two = Kwacha(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'MK\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'MK\xa03.14'),
        (10, '10', 'MK\xa010.00'),
        (Decimal('10'), '10', 'MK\xa010.00'),
        ('-3.14', '-3.14', 'MK\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'MK\xa0-3.14'),
        (-10, '-10', 'MK\xa0-10.00'),
        (Decimal('-10'), '-10', 'MK\xa0-10.00')
    ])
    def test_kwacha_default(amount, result, printed):
        default = Kwacha(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MWK'
        assert default.numeric_code == '454'
        assert default.symbol == 'MK'
        assert default.localized_symbol == 'MK'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MWK',
            '454'))
        assert default.__repr__() == (
            'Kwacha('
            f'amount: {result}, '
            'alpha_code: "MWK", '
            'numeric_code: "454", '
            'symbol: "MK", '
            'localized_symbol: "MK", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'MK10.00,00000'),
        (-1000, 'MK10.00,00000-')
    ])
    def test_kwacha_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Kwacha(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MWK'
        assert custom.numeric_code == '454'
        assert custom.symbol == 'MK'
        assert custom.localized_symbol == 'MK'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MWK',
            '454'))
        assert custom.__repr__() == (
            'Kwacha('
            f'amount: {amount}, '
            'alpha_code: "MWK", '
            'numeric_code: "454", '
            'symbol: "MK", '
            'localized_symbol: "MK", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kwacha_recreate(amount, new_amount):
        default = Kwacha(amount)
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
    def test_kwacha_change_attributes(attribute, value):
        immutable = Kwacha(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Kwacha\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kwacha_add_attributes(attribute, value):
        immutable = Kwacha(1000)
        with raises(
                AttributeError,
                match=f'\'Kwacha\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kwacha_one, kwacha_one, kwacha_two, None),
        (kwacha_one, kwacha_one_other, kwacha_two, None),
        (kwacha_two, kwacha_minus_one, kwacha_one, None),
        (kwacha_one, other, None, CurrencyMismatchException),
        (kwacha_one, 1.00, None, CurrencyTypeException),
        (kwacha_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kwacha_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kwacha_one)
    ])
    def test_kwacha_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MWK'
        assert new.numeric_code == '454'
        assert new.symbol == 'MK'
        assert new.localized_symbol == 'MK'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestZambianKwacha:
    """Zambian Kwacha currency tests."""

    zambian_kwacha_minus_one = ZambianKwacha(-1)
    zambian_kwacha_one_other = ZambianKwacha(1)
    zambian_kwacha_one = ZambianKwacha(1)
    zambian_kwacha_two = ZambianKwacha(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ZK\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ZK\xa03.14'),
        (10, '10', 'ZK\xa010.00'),
        (Decimal('10'), '10', 'ZK\xa010.00'),
        ('-3.14', '-3.14', 'ZK\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ZK\xa0-3.14'),
        (-10, '-10', 'ZK\xa0-10.00'),
        (Decimal('-10'), '-10', 'ZK\xa0-10.00')
    ])
    def test_zambian_kwacha_default(amount, result, printed):
        default = ZambianKwacha(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZMW'
        assert default.numeric_code == '967'
        assert default.symbol == 'ZK'
        assert default.localized_symbol == 'ZK'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZMW',
            '967'))
        assert default.__repr__() == (
            'ZambianKwacha('
            f'amount: {result}, '
            'alpha_code: "ZMW", '
            'numeric_code: "967", '
            'symbol: "ZK", '
            'localized_symbol: "ZK", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ZK10.00,00000'),
        (-1000, 'ZK10.00,00000-')
    ])
    def test_zambian_kwacha_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ZambianKwacha(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZMW'
        assert custom.numeric_code == '967'
        assert custom.symbol == 'ZK'
        assert custom.localized_symbol == 'ZK'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZMW',
            '967'))
        assert custom.__repr__() == (
            'ZambianKwacha('
            f'amount: {amount}, '
            'alpha_code: "ZMW", '
            'numeric_code: "967", '
            'symbol: "ZK", '
            'localized_symbol: "ZK", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_zambian_kwacha_recreate(amount, new_amount):
        default = ZambianKwacha(amount)
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
    def test_zambian_kwacha_change_attributes(attribute, value):
        immutable = ZambianKwacha(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ZambianKwacha\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_zambian_kwacha_add_attributes(attribute, value):
        immutable = ZambianKwacha(1000)
        with raises(
                AttributeError,
                match=f'\'ZambianKwacha\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (zambian_kwacha_one, zambian_kwacha_one, zambian_kwacha_two, None),
        (zambian_kwacha_one, zambian_kwacha_one_other, zambian_kwacha_two, None),
        (zambian_kwacha_two, zambian_kwacha_minus_one, zambian_kwacha_one, None),
        (zambian_kwacha_one, other, None, CurrencyMismatchException),
        (zambian_kwacha_one, 1.00, None, CurrencyTypeException),
        (zambian_kwacha_one, '1.00', None, CurrencyTypeException)
    ])
    def test_zambian_kwacha_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (zambian_kwacha_one)
    ])
    def test_zambian_kwacha_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZMW'
        assert new.numeric_code == '967'
        assert new.symbol == 'ZK'
        assert new.localized_symbol == 'ZK'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
