# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lari currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lari import (
    Lari,
    GeorgiaLari,
    SouthOssetiaLari)


class TestLari:
    """Lari currency tests."""

    lari_minus_one = Lari(-1)
    lari_one_other = Lari(1)
    lari_one = Lari(1)
    lari_two = Lari(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0ლ'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0ლ'),
        (10, '10', '10,00\xa0ლ'),
        (Decimal('10'), '10', '10,00\xa0ლ'),
        ('-3.14', '-3.14', '-3,14\xa0ლ'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0ლ'),
        (-10, '-10', '-10,00\xa0ლ'),
        (Decimal('-10'), '-10', '-10,00\xa0ლ')
    ])
    def test_lari_default(amount, result, printed):
        default = Lari(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GEL'
        assert default.numeric_code == '981'
        assert default.symbol == 'ლ'
        assert default.localized_symbol == 'GEლ'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert default.__repr__() == (
            'Lari('
            f'amount: {result}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ლ10.00,00000'),
        (-1000, 'ლ10.00,00000-')
    ])
    def test_lari_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Lari(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GEL'
        assert custom.numeric_code == '981'
        assert custom.symbol == 'ლ'
        assert custom.localized_symbol == 'GEლ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert custom.__repr__() == (
            'Lari('
            f'amount: {amount}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_lari_recreate(amount, new_amount):
        default = Lari(amount)
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
    def test_lari_change_attributes(attribute, value):
        immutable = Lari(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Lari\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_lari_add_attributes(attribute, value):
        immutable = Lari(1000)
        with raises(
                AttributeError,
                match=f'\'Lari\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (lari_one, lari_one, lari_two, None),
        (lari_one, lari_one_other, lari_two, None),
        (lari_two, lari_minus_one, lari_one, None),
        (lari_one, other, None, CurrencyMismatchException),
        (lari_one, 1.00, None, CurrencyTypeException),
        (lari_one, '1.00', None, CurrencyTypeException)
    ])
    def test_lari_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (lari_one)
    ])
    def test_lari_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GEL'
        assert new.numeric_code == '981'
        assert new.symbol == 'ლ'
        assert new.localized_symbol == 'GEლ'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestGeorgiaLari:
    """Georgia Lari currency tests."""

    georgia_lari_minus_one = GeorgiaLari(-1)
    georgia_lari_one_other = GeorgiaLari(1)
    georgia_lari_one = GeorgiaLari(1)
    georgia_lari_two = GeorgiaLari(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0ლ'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0ლ'),
        (10, '10', '10,00\xa0ლ'),
        (Decimal('10'), '10', '10,00\xa0ლ'),
        ('-3.14', '-3.14', '-3,14\xa0ლ'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0ლ'),
        (-10, '-10', '-10,00\xa0ლ'),
        (Decimal('-10'), '-10', '-10,00\xa0ლ')
    ])
    def test_georgia_lari_default(amount, result, printed):
        default = GeorgiaLari(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GEL'
        assert default.numeric_code == '981'
        assert default.symbol == 'ლ'
        assert default.localized_symbol == 'GEლ'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert default.__repr__() == (
            'GeorgiaLari('
            f'amount: {result}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ლ10.00,00000'),
        (-1000, 'ლ10.00,00000-')
    ])
    def test_georgia_lari_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = GeorgiaLari(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GEL'
        assert custom.numeric_code == '981'
        assert custom.symbol == 'ლ'
        assert custom.localized_symbol == 'GEლ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert custom.__repr__() == (
            'GeorgiaLari('
            f'amount: {amount}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_georgia_lari_recreate(amount, new_amount):
        default = GeorgiaLari(amount)
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
    def test_georgia_lari_change_attributes(attribute, value):
        immutable = GeorgiaLari(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'GeorgiaLari\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_georgia_lari_add_attributes(attribute, value):
        immutable = GeorgiaLari(1000)
        with raises(
                AttributeError,
                match=f'\'GeorgiaLari\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (georgia_lari_one, georgia_lari_one, georgia_lari_two, None),
        (georgia_lari_one, georgia_lari_one_other, georgia_lari_two, None),
        (georgia_lari_two, georgia_lari_minus_one, georgia_lari_one, None),
        (georgia_lari_one, other, None, CurrencyMismatchException),
        (georgia_lari_one, 1.00, None, CurrencyTypeException),
        (georgia_lari_one, '1.00', None, CurrencyTypeException)
    ])
    def test_georgia_lari_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (georgia_lari_one)
    ])
    def test_georgia_lari_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GEL'
        assert new.numeric_code == '981'
        assert new.symbol == 'ლ'
        assert new.localized_symbol == 'GEლ'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestSouthOssetiaLari:
    """South Ossetia Lari currency tests."""

    south_ossetia_lari_minus_one = SouthOssetiaLari(-1)
    south_ossetia_lari_one_other = SouthOssetiaLari(1)
    south_ossetia_lari_one = SouthOssetiaLari(1)
    south_ossetia_lari_two = SouthOssetiaLari(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0ლ'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0ლ'),
        (10, '10', '10,00\xa0ლ'),
        (Decimal('10'), '10', '10,00\xa0ლ'),
        ('-3.14', '-3.14', '-3,14\xa0ლ'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0ლ'),
        (-10, '-10', '-10,00\xa0ლ'),
        (Decimal('-10'), '-10', '-10,00\xa0ლ')
    ])
    def test_south_ossetia_lari_default(amount, result, printed):
        default = SouthOssetiaLari(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GEL'
        assert default.numeric_code == '981'
        assert default.symbol == 'ლ'
        assert default.localized_symbol == 'GEლ'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert default.__repr__() == (
            'SouthOssetiaLari('
            f'amount: {result}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ლ10.00,00000'),
        (-1000, 'ლ10.00,00000-')
    ])
    def test_south_ossetia_lari_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SouthOssetiaLari(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GEL'
        assert custom.numeric_code == '981'
        assert custom.symbol == 'ლ'
        assert custom.localized_symbol == 'GEლ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GEL',
            '981'))
        assert custom.__repr__() == (
            'SouthOssetiaLari('
            f'amount: {amount}, '
            'alpha_code: "GEL", '
            'numeric_code: "981", '
            'symbol: "ლ", '
            'localized_symbol: "GEლ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_south_ossetia_lari_recreate(amount, new_amount):
        default = SouthOssetiaLari(amount)
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
    def test_south_ossetia_lari_change_attributes(attribute, value):
        immutable = SouthOssetiaLari(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SouthOssetiaLari\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_south_ossetia_lari_add_attributes(attribute, value):
        immutable = SouthOssetiaLari(1000)
        with raises(
                AttributeError,
                match=f'\'SouthOssetiaLari\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (south_ossetia_lari_one, south_ossetia_lari_one, south_ossetia_lari_two, None),
        (south_ossetia_lari_one, south_ossetia_lari_one_other, south_ossetia_lari_two, None),
        (south_ossetia_lari_two, south_ossetia_lari_minus_one, south_ossetia_lari_one, None),
        (south_ossetia_lari_one, other, None, CurrencyMismatchException),
        (south_ossetia_lari_one, 1.00, None, CurrencyTypeException),
        (south_ossetia_lari_one, '1.00', None, CurrencyTypeException)
    ])
    def test_south_ossetia_lari_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (south_ossetia_lari_one)
    ])
    def test_south_ossetia_lari_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GEL'
        assert new.numeric_code == '981'
        assert new.symbol == 'ლ'
        assert new.localized_symbol == 'GEლ'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
