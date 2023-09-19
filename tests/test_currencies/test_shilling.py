# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Shilling currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.shilling import (
    KenyanShilling,
    SomaliShilling,
    TanzanianShilling,
    UgandaShilling)


class TestKenyanShilling:
    """Kenyan Shilling currency tests."""

    kenyan_shilling_minus_one = KenyanShilling(-1)
    kenyan_shilling_one_other = KenyanShilling(1)
    kenyan_shilling_one = KenyanShilling(1)
    kenyan_shilling_two = KenyanShilling(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Ksh\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Ksh\xa03.14'),
        (10, '10', 'Ksh\xa010.00'),
        (Decimal('10'), '10', 'Ksh\xa010.00'),
        ('-3.14', '-3.14', 'Ksh\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Ksh\xa0-3.14'),
        (-10, '-10', 'Ksh\xa0-10.00'),
        (Decimal('-10'), '-10', 'Ksh\xa0-10.00')
    ])
    def test_kenyan_shilling_default(amount, result, printed):
        default = KenyanShilling(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KES'
        assert default.numeric_code == '404'
        assert default.symbol == 'Ksh'
        assert default.localized_symbol == 'Ksh'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KES',
            '404'))
        assert default.__repr__() == (
            'KenyanShilling('
            f'amount: {result}, '
            'alpha_code: "KES", '
            'numeric_code: "404", '
            'symbol: "Ksh", '
            'localized_symbol: "Ksh", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Ksh10.00,00000'),
        (-1000, 'Ksh10.00,00000-')
    ])
    def test_kenyan_shilling_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = KenyanShilling(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KES'
        assert custom.numeric_code == '404'
        assert custom.symbol == 'Ksh'
        assert custom.localized_symbol == 'Ksh'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KES',
            '404'))
        assert custom.__repr__() == (
            'KenyanShilling('
            f'amount: {amount}, '
            'alpha_code: "KES", '
            'numeric_code: "404", '
            'symbol: "Ksh", '
            'localized_symbol: "Ksh", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kenyan_shilling_recreate(amount, new_amount):
        default = KenyanShilling(amount)
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
    def test_kenyan_shilling_change_attributes(attribute, value):
        immutable = KenyanShilling(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'KenyanShilling\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kenyan_shilling_add_attributes(attribute, value):
        immutable = KenyanShilling(1000)
        with raises(
                AttributeError,
                match=f'\'KenyanShilling\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kenyan_shilling_one, kenyan_shilling_one, kenyan_shilling_two, None),
        (kenyan_shilling_one, kenyan_shilling_one_other, kenyan_shilling_two, None),
        (kenyan_shilling_two, kenyan_shilling_minus_one, kenyan_shilling_one, None),
        (kenyan_shilling_one, other, None, CurrencyMismatchException),
        (kenyan_shilling_one, 1.00, None, CurrencyTypeException),
        (kenyan_shilling_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kenyan_shilling_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kenyan_shilling_one)
    ])
    def test_kenyan_shilling_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KES'
        assert new.numeric_code == '404'
        assert new.symbol == 'Ksh'
        assert new.localized_symbol == 'Ksh'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestSomaliShilling:
    """Somali Shilling currency tests."""

    somali_shilling_minus_one = SomaliShilling(-1)
    somali_shilling_one_other = SomaliShilling(1)
    somali_shilling_one = SomaliShilling(1)
    somali_shilling_two = SomaliShilling(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'SSh\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'SSh\xa03.14'),
        (10, '10', 'SSh\xa010.00'),
        (Decimal('10'), '10', 'SSh\xa010.00'),
        ('-3.14', '-3.14', 'SSh\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'SSh\xa0-3.14'),
        (-10, '-10', 'SSh\xa0-10.00'),
        (Decimal('-10'), '-10', 'SSh\xa0-10.00')
    ])
    def test_somali_shilling_default(amount, result, printed):
        default = SomaliShilling(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SOS'
        assert default.numeric_code == '706'
        assert default.symbol == 'SSh'
        assert default.localized_symbol == 'SSh'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SOS',
            '706'))
        assert default.__repr__() == (
            'SomaliShilling('
            f'amount: {result}, '
            'alpha_code: "SOS", '
            'numeric_code: "706", '
            'symbol: "SSh", '
            'localized_symbol: "SSh", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'SSh10.00,00000'),
        (-1000, 'SSh10.00,00000-')
    ])
    def test_somali_shilling_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SomaliShilling(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SOS'
        assert custom.numeric_code == '706'
        assert custom.symbol == 'SSh'
        assert custom.localized_symbol == 'SSh'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SOS',
            '706'))
        assert custom.__repr__() == (
            'SomaliShilling('
            f'amount: {amount}, '
            'alpha_code: "SOS", '
            'numeric_code: "706", '
            'symbol: "SSh", '
            'localized_symbol: "SSh", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_somali_shilling_recreate(amount, new_amount):
        default = SomaliShilling(amount)
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
    def test_somali_shilling_change_attributes(attribute, value):
        immutable = SomaliShilling(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SomaliShilling\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_somali_shilling_add_attributes(attribute, value):
        immutable = SomaliShilling(1000)
        with raises(
                AttributeError,
                match=f'\'SomaliShilling\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (somali_shilling_one, somali_shilling_one, somali_shilling_two, None),
        (somali_shilling_one, somali_shilling_one_other, somali_shilling_two, None),
        (somali_shilling_two, somali_shilling_minus_one, somali_shilling_one, None),
        (somali_shilling_one, other, None, CurrencyMismatchException),
        (somali_shilling_one, 1.00, None, CurrencyTypeException),
        (somali_shilling_one, '1.00', None, CurrencyTypeException)
    ])
    def test_somali_shilling_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (somali_shilling_one)
    ])
    def test_somali_shilling_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SOS'
        assert new.numeric_code == '706'
        assert new.symbol == 'SSh'
        assert new.localized_symbol == 'SSh'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestTanzanianShilling:
    """Tanzanian Shilling currency tests."""

    tanzanian_shilling_minus_one = TanzanianShilling(-1)
    tanzanian_shilling_one_other = TanzanianShilling(1)
    tanzanian_shilling_one = TanzanianShilling(1)
    tanzanian_shilling_two = TanzanianShilling(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'TSh\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'TSh\xa03.14'),
        (10, '10', 'TSh\xa010.00'),
        (Decimal('10'), '10', 'TSh\xa010.00'),
        ('-3.14', '-3.14', 'TSh\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'TSh\xa0-3.14'),
        (-10, '-10', 'TSh\xa0-10.00'),
        (Decimal('-10'), '-10', 'TSh\xa0-10.00')
    ])
    def test_tanzanian_shilling_default(amount, result, printed):
        default = TanzanianShilling(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TZS'
        assert default.numeric_code == '834'
        assert default.symbol == 'TSh'
        assert default.localized_symbol == 'TSh'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TZS',
            '834'))
        assert default.__repr__() == (
            'TanzanianShilling('
            f'amount: {result}, '
            'alpha_code: "TZS", '
            'numeric_code: "834", '
            'symbol: "TSh", '
            'localized_symbol: "TSh", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'TSh10.00,00000'),
        (-1000, 'TSh10.00,00000-')
    ])
    def test_tanzanian_shilling_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TanzanianShilling(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TZS'
        assert custom.numeric_code == '834'
        assert custom.symbol == 'TSh'
        assert custom.localized_symbol == 'TSh'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TZS',
            '834'))
        assert custom.__repr__() == (
            'TanzanianShilling('
            f'amount: {amount}, '
            'alpha_code: "TZS", '
            'numeric_code: "834", '
            'symbol: "TSh", '
            'localized_symbol: "TSh", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tanzanian_shilling_recreate(amount, new_amount):
        default = TanzanianShilling(amount)
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
    def test_tanzanian_shilling_change_attributes(attribute, value):
        immutable = TanzanianShilling(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TanzanianShilling\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tanzanian_shilling_add_attributes(attribute, value):
        immutable = TanzanianShilling(1000)
        with raises(
                AttributeError,
                match=f'\'TanzanianShilling\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tanzanian_shilling_one, tanzanian_shilling_one, tanzanian_shilling_two, None),
        (tanzanian_shilling_one, tanzanian_shilling_one_other, tanzanian_shilling_two, None),
        (tanzanian_shilling_two, tanzanian_shilling_minus_one, tanzanian_shilling_one, None),
        (tanzanian_shilling_one, other, None, CurrencyMismatchException),
        (tanzanian_shilling_one, 1.00, None, CurrencyTypeException),
        (tanzanian_shilling_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tanzanian_shilling_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tanzanian_shilling_one)
    ])
    def test_tanzanian_shilling_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TZS'
        assert new.numeric_code == '834'
        assert new.symbol == 'TSh'
        assert new.localized_symbol == 'TSh'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestUgandaShilling:
    """Uganda Shilling currency tests."""

    uganda_shilling_minus_one = UgandaShilling(-1)
    uganda_shilling_one_other = UgandaShilling(1)
    uganda_shilling_one = UgandaShilling(1)
    uganda_shilling_two = UgandaShilling(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'USh\xa03'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'USh\xa03'),
        (10, '10', 'USh\xa010'),
        (Decimal('10'), '10', 'USh\xa010'),
        ('-3.14', '-3.14', 'USh\xa0-3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'USh\xa0-3'),
        (-10, '-10', 'USh\xa0-10'),
        (Decimal('-10'), '-10', 'USh\xa0-10')
    ])
    def test_uganda_shilling_default(amount, result, printed):
        default = UgandaShilling(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'UGX'
        assert default.numeric_code == '800'
        assert default.symbol == 'USh'
        assert default.localized_symbol == 'USh'
        assert default.convertion == ''
        assert default.pattern == '0.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'UGX',
            '800'))
        assert default.__repr__() == (
            'UgandaShilling('
            f'amount: {result}, '
            'alpha_code: "UGX", '
            'numeric_code: "800", '
            'symbol: "USh", '
            'localized_symbol: "USh", '
            'convertion: "", '
            'pattern: "0.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'USh10.00,00000'),
        (-1000, 'USh10.00,00000-')
    ])
    def test_uganda_shilling_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = UgandaShilling(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'UGX'
        assert custom.numeric_code == '800'
        assert custom.symbol == 'USh'
        assert custom.localized_symbol == 'USh'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'UGX',
            '800'))
        assert custom.__repr__() == (
            'UgandaShilling('
            f'amount: {amount}, '
            'alpha_code: "UGX", '
            'numeric_code: "800", '
            'symbol: "USh", '
            'localized_symbol: "USh", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_uganda_shilling_recreate(amount, new_amount):
        default = UgandaShilling(amount)
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
    def test_uganda_shilling_change_attributes(attribute, value):
        immutable = UgandaShilling(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'UgandaShilling\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_uganda_shilling_add_attributes(attribute, value):
        immutable = UgandaShilling(1000)
        with raises(
                AttributeError,
                match=f'\'UgandaShilling\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (uganda_shilling_one, uganda_shilling_one, uganda_shilling_two, None),
        (uganda_shilling_one, uganda_shilling_one_other, uganda_shilling_two, None),
        (uganda_shilling_two, uganda_shilling_minus_one, uganda_shilling_one, None),
        (uganda_shilling_one, other, None, CurrencyMismatchException),
        (uganda_shilling_one, 1.00, None, CurrencyTypeException),
        (uganda_shilling_one, '1.00', None, CurrencyTypeException)
    ])
    def test_uganda_shilling_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (uganda_shilling_one)
    ])
    def test_uganda_shilling_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'UGX'
        assert new.numeric_code == '800'
        assert new.symbol == 'USh'
        assert new.localized_symbol == 'USh'
        assert new.convertion == ''
        assert new.pattern == '0.,3%s\u00A0%a'
