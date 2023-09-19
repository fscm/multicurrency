# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dinar currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dinar import (
    BahrainiDinar,
    AlgerianDinar,
    IraqiDinar,
    JordanianDinar,
    KuwaitiDinar,
    LibyanDinar,
    SerbianDinarXK,
    SerbianDinarSR,
    TunisianDinar)


class TestBahrainiDinar:
    """Bahraini Dinar currency tests."""

    bahraini_dinar_minus_one = BahrainiDinar(-1)
    bahraini_dinar_one_other = BahrainiDinar(1)
    bahraini_dinar_one = BahrainiDinar(1)
    bahraini_dinar_two = BahrainiDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.ب.\xa0٣٫١٤٠'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.ب.\xa0٣٫١٤٠'),
        (10, '10', 'د.ب.\xa0١٠٫٠٠٠'),
        (Decimal('10'), '10', 'د.ب.\xa0١٠٫٠٠٠'),
        ('-3.14', '-3.14', 'د.ب.\xa0-٣٫١٤٠'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.ب.\xa0-٣٫١٤٠'),
        (-10, '-10', 'د.ب.\xa0-١٠٫٠٠٠'),
        (Decimal('-10'), '-10', 'د.ب.\xa0-١٠٫٠٠٠')
    ])
    def test_bahraini_dinar_default(amount, result, printed):
        default = BahrainiDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BHD'
        assert default.numeric_code == '048'
        assert default.symbol == 'د.ب.'
        assert default.localized_symbol == 'د.ب.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '3\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BHD',
            '048'))
        assert default.__repr__() == (
            'BahrainiDinar('
            f'amount: {result}, '
            'alpha_code: "BHD", '
            'numeric_code: "048", '
            'symbol: "د.ب.", '
            'localized_symbol: "د.ب.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "3٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ب.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.ب.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_bahraini_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BahrainiDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BHD'
        assert custom.numeric_code == '048'
        assert custom.symbol == 'د.ب.'
        assert custom.localized_symbol == 'د.ب.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BHD',
            '048'))
        assert custom.__repr__() == (
            'BahrainiDinar('
            f'amount: {amount}, '
            'alpha_code: "BHD", '
            'numeric_code: "048", '
            'symbol: "د.ب.", '
            'localized_symbol: "د.ب.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bahraini_dinar_recreate(amount, new_amount):
        default = BahrainiDinar(amount)
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
    def test_bahraini_dinar_change_attributes(attribute, value):
        immutable = BahrainiDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BahrainiDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bahraini_dinar_add_attributes(attribute, value):
        immutable = BahrainiDinar(1000)
        with raises(
                AttributeError,
                match=f'\'BahrainiDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bahraini_dinar_one, bahraini_dinar_one, bahraini_dinar_two, None),
        (bahraini_dinar_one, bahraini_dinar_one_other, bahraini_dinar_two, None),
        (bahraini_dinar_two, bahraini_dinar_minus_one, bahraini_dinar_one, None),
        (bahraini_dinar_one, other, None, CurrencyMismatchException),
        (bahraini_dinar_one, 1.00, None, CurrencyTypeException),
        (bahraini_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bahraini_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bahraini_dinar_one)
    ])
    def test_bahraini_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BHD'
        assert new.numeric_code == '048'
        assert new.symbol == 'د.ب.'
        assert new.localized_symbol == 'د.ب.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '3\u066B\u066C3%s\u00A0%a'


class TestAlgerianDinar:
    """Algerian Dinar currency tests."""

    algerian_dinar_minus_one = AlgerianDinar(-1)
    algerian_dinar_one_other = AlgerianDinar(1)
    algerian_dinar_one = AlgerianDinar(1)
    algerian_dinar_two = AlgerianDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0د.ج.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0د.ج.'),
        (10, '10', '10,00\xa0د.ج.'),
        (Decimal('10'), '10', '10,00\xa0د.ج.'),
        ('-3.14', '-3.14', '-3,14\xa0د.ج.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0د.ج.'),
        (-10, '-10', '-10,00\xa0د.ج.'),
        (Decimal('-10'), '-10', '-10,00\xa0د.ج.')
    ])
    def test_algerian_dinar_default(amount, result, printed):
        default = AlgerianDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'DZD'
        assert default.numeric_code == '012'
        assert default.symbol == 'د.ج.'
        assert default.localized_symbol == 'د.ج.'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'DZD',
            '012'))
        assert default.__repr__() == (
            'AlgerianDinar('
            f'amount: {result}, '
            'alpha_code: "DZD", '
            'numeric_code: "012", '
            'symbol: "د.ج.", '
            'localized_symbol: "د.ج.", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ج.10.00,00000'),
        (-1000, 'د.ج.10.00,00000-')
    ])
    def test_algerian_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AlgerianDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'DZD'
        assert custom.numeric_code == '012'
        assert custom.symbol == 'د.ج.'
        assert custom.localized_symbol == 'د.ج.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'DZD',
            '012'))
        assert custom.__repr__() == (
            'AlgerianDinar('
            f'amount: {amount}, '
            'alpha_code: "DZD", '
            'numeric_code: "012", '
            'symbol: "د.ج.", '
            'localized_symbol: "د.ج.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_algerian_dinar_recreate(amount, new_amount):
        default = AlgerianDinar(amount)
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
    def test_algerian_dinar_change_attributes(attribute, value):
        immutable = AlgerianDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AlgerianDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_algerian_dinar_add_attributes(attribute, value):
        immutable = AlgerianDinar(1000)
        with raises(
                AttributeError,
                match=f'\'AlgerianDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (algerian_dinar_one, algerian_dinar_one, algerian_dinar_two, None),
        (algerian_dinar_one, algerian_dinar_one_other, algerian_dinar_two, None),
        (algerian_dinar_two, algerian_dinar_minus_one, algerian_dinar_one, None),
        (algerian_dinar_one, other, None, CurrencyMismatchException),
        (algerian_dinar_one, 1.00, None, CurrencyTypeException),
        (algerian_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_algerian_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (algerian_dinar_one)
    ])
    def test_algerian_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'DZD'
        assert new.numeric_code == '012'
        assert new.symbol == 'د.ج.'
        assert new.localized_symbol == 'د.ج.'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestIraqiDinar:
    """Iraqi Dinar currency tests."""

    iraqi_dinar_minus_one = IraqiDinar(-1)
    iraqi_dinar_one_other = IraqiDinar(1)
    iraqi_dinar_one = IraqiDinar(1)
    iraqi_dinar_two = IraqiDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.ع.\xa0٣٫١٤٠'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.ع.\xa0٣٫١٤٠'),
        (10, '10', 'د.ع.\xa0١٠٫٠٠٠'),
        (Decimal('10'), '10', 'د.ع.\xa0١٠٫٠٠٠'),
        ('-3.14', '-3.14', 'د.ع.\xa0-٣٫١٤٠'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.ع.\xa0-٣٫١٤٠'),
        (-10, '-10', 'د.ع.\xa0-١٠٫٠٠٠'),
        (Decimal('-10'), '-10', 'د.ع.\xa0-١٠٫٠٠٠')
    ])
    def test_iraqi_dinar_default(amount, result, printed):
        default = IraqiDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'IQD'
        assert default.numeric_code == '368'
        assert default.symbol == 'د.ع.'
        assert default.localized_symbol == 'د.ع.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '3\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'IQD',
            '368'))
        assert default.__repr__() == (
            'IraqiDinar('
            f'amount: {result}, '
            'alpha_code: "IQD", '
            'numeric_code: "368", '
            'symbol: "د.ع.", '
            'localized_symbol: "د.ع.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "3٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ع.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.ع.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_iraqi_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IraqiDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'IQD'
        assert custom.numeric_code == '368'
        assert custom.symbol == 'د.ع.'
        assert custom.localized_symbol == 'د.ع.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'IQD',
            '368'))
        assert custom.__repr__() == (
            'IraqiDinar('
            f'amount: {amount}, '
            'alpha_code: "IQD", '
            'numeric_code: "368", '
            'symbol: "د.ع.", '
            'localized_symbol: "د.ع.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_iraqi_dinar_recreate(amount, new_amount):
        default = IraqiDinar(amount)
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
    def test_iraqi_dinar_change_attributes(attribute, value):
        immutable = IraqiDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IraqiDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_iraqi_dinar_add_attributes(attribute, value):
        immutable = IraqiDinar(1000)
        with raises(
                AttributeError,
                match=f'\'IraqiDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (iraqi_dinar_one, iraqi_dinar_one, iraqi_dinar_two, None),
        (iraqi_dinar_one, iraqi_dinar_one_other, iraqi_dinar_two, None),
        (iraqi_dinar_two, iraqi_dinar_minus_one, iraqi_dinar_one, None),
        (iraqi_dinar_one, other, None, CurrencyMismatchException),
        (iraqi_dinar_one, 1.00, None, CurrencyTypeException),
        (iraqi_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_iraqi_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (iraqi_dinar_one)
    ])
    def test_iraqi_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'IQD'
        assert new.numeric_code == '368'
        assert new.symbol == 'د.ع.'
        assert new.localized_symbol == 'د.ع.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '3\u066B\u066C3%s\u00A0%a'


class TestJordanianDinar:
    """Jordanian Dinar currency tests."""

    jordanian_dinar_minus_one = JordanianDinar(-1)
    jordanian_dinar_one_other = JordanianDinar(1)
    jordanian_dinar_one = JordanianDinar(1)
    jordanian_dinar_two = JordanianDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.أ.\xa0٣٫١٤٠'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.أ.\xa0٣٫١٤٠'),
        (10, '10', 'د.أ.\xa0١٠٫٠٠٠'),
        (Decimal('10'), '10', 'د.أ.\xa0١٠٫٠٠٠'),
        ('-3.14', '-3.14', 'د.أ.\xa0-٣٫١٤٠'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.أ.\xa0-٣٫١٤٠'),
        (-10, '-10', 'د.أ.\xa0-١٠٫٠٠٠'),
        (Decimal('-10'), '-10', 'د.أ.\xa0-١٠٫٠٠٠')
    ])
    def test_jordanian_dinar_default(amount, result, printed):
        default = JordanianDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'JOD'
        assert default.numeric_code == '400'
        assert default.symbol == 'د.أ.'
        assert default.localized_symbol == 'د.أ.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '3\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'JOD',
            '400'))
        assert default.__repr__() == (
            'JordanianDinar('
            f'amount: {result}, '
            'alpha_code: "JOD", '
            'numeric_code: "400", '
            'symbol: "د.أ.", '
            'localized_symbol: "د.أ.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "3٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.أ.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.أ.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_jordanian_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = JordanianDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'JOD'
        assert custom.numeric_code == '400'
        assert custom.symbol == 'د.أ.'
        assert custom.localized_symbol == 'د.أ.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'JOD',
            '400'))
        assert custom.__repr__() == (
            'JordanianDinar('
            f'amount: {amount}, '
            'alpha_code: "JOD", '
            'numeric_code: "400", '
            'symbol: "د.أ.", '
            'localized_symbol: "د.أ.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_jordanian_dinar_recreate(amount, new_amount):
        default = JordanianDinar(amount)
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
    def test_jordanian_dinar_change_attributes(attribute, value):
        immutable = JordanianDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'JordanianDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_jordanian_dinar_add_attributes(attribute, value):
        immutable = JordanianDinar(1000)
        with raises(
                AttributeError,
                match=f'\'JordanianDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (jordanian_dinar_one, jordanian_dinar_one, jordanian_dinar_two, None),
        (jordanian_dinar_one, jordanian_dinar_one_other, jordanian_dinar_two, None),
        (jordanian_dinar_two, jordanian_dinar_minus_one, jordanian_dinar_one, None),
        (jordanian_dinar_one, other, None, CurrencyMismatchException),
        (jordanian_dinar_one, 1.00, None, CurrencyTypeException),
        (jordanian_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_jordanian_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (jordanian_dinar_one)
    ])
    def test_jordanian_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'JOD'
        assert new.numeric_code == '400'
        assert new.symbol == 'د.أ.'
        assert new.localized_symbol == 'د.أ.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '3\u066B\u066C3%s\u00A0%a'


class TestKuwaitiDinar:
    """Kuwaiti Dinar currency tests."""

    kuwaiti_dinar_minus_one = KuwaitiDinar(-1)
    kuwaiti_dinar_one_other = KuwaitiDinar(1)
    kuwaiti_dinar_one = KuwaitiDinar(1)
    kuwaiti_dinar_two = KuwaitiDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.ك.\xa0٣٫١٤٠'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.ك.\xa0٣٫١٤٠'),
        (10, '10', 'د.ك.\xa0١٠٫٠٠٠'),
        (Decimal('10'), '10', 'د.ك.\xa0١٠٫٠٠٠'),
        ('-3.14', '-3.14', 'د.ك.\xa0-٣٫١٤٠'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.ك.\xa0-٣٫١٤٠'),
        (-10, '-10', 'د.ك.\xa0-١٠٫٠٠٠'),
        (Decimal('-10'), '-10', 'د.ك.\xa0-١٠٫٠٠٠')
    ])
    def test_kuwaiti_dinar_default(amount, result, printed):
        default = KuwaitiDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KWD'
        assert default.numeric_code == '414'
        assert default.symbol == 'د.ك.'
        assert default.localized_symbol == 'د.ك.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '3\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KWD',
            '414'))
        assert default.__repr__() == (
            'KuwaitiDinar('
            f'amount: {result}, '
            'alpha_code: "KWD", '
            'numeric_code: "414", '
            'symbol: "د.ك.", '
            'localized_symbol: "د.ك.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "3٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ك.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.ك.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_kuwaiti_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = KuwaitiDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KWD'
        assert custom.numeric_code == '414'
        assert custom.symbol == 'د.ك.'
        assert custom.localized_symbol == 'د.ك.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KWD',
            '414'))
        assert custom.__repr__() == (
            'KuwaitiDinar('
            f'amount: {amount}, '
            'alpha_code: "KWD", '
            'numeric_code: "414", '
            'symbol: "د.ك.", '
            'localized_symbol: "د.ك.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kuwaiti_dinar_recreate(amount, new_amount):
        default = KuwaitiDinar(amount)
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
    def test_kuwaiti_dinar_change_attributes(attribute, value):
        immutable = KuwaitiDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'KuwaitiDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kuwaiti_dinar_add_attributes(attribute, value):
        immutable = KuwaitiDinar(1000)
        with raises(
                AttributeError,
                match=f'\'KuwaitiDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kuwaiti_dinar_one, kuwaiti_dinar_one, kuwaiti_dinar_two, None),
        (kuwaiti_dinar_one, kuwaiti_dinar_one_other, kuwaiti_dinar_two, None),
        (kuwaiti_dinar_two, kuwaiti_dinar_minus_one, kuwaiti_dinar_one, None),
        (kuwaiti_dinar_one, other, None, CurrencyMismatchException),
        (kuwaiti_dinar_one, 1.00, None, CurrencyTypeException),
        (kuwaiti_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kuwaiti_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kuwaiti_dinar_one)
    ])
    def test_kuwaiti_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KWD'
        assert new.numeric_code == '414'
        assert new.symbol == 'د.ك.'
        assert new.localized_symbol == 'د.ك.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '3\u066B\u066C3%s\u00A0%a'


class TestLibyanDinar:
    """Libyan Dinar currency tests."""

    libyan_dinar_minus_one = LibyanDinar(-1)
    libyan_dinar_one_other = LibyanDinar(1)
    libyan_dinar_one = LibyanDinar(1)
    libyan_dinar_two = LibyanDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.ل.\xa03,140'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.ل.\xa03,140'),
        (10, '10', 'د.ل.\xa010,000'),
        (Decimal('10'), '10', 'د.ل.\xa010,000'),
        ('-3.14', '-3.14', 'د.ل.\xa0-3,140'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.ل.\xa0-3,140'),
        (-10, '-10', 'د.ل.\xa0-10,000'),
        (Decimal('-10'), '-10', 'د.ل.\xa0-10,000')
    ])
    def test_libyan_dinar_default(amount, result, printed):
        default = LibyanDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LYD'
        assert default.numeric_code == '434'
        assert default.symbol == 'د.ل.'
        assert default.localized_symbol == 'د.ل.'
        assert default.convertion == ''
        assert default.pattern == '3,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LYD',
            '434'))
        assert default.__repr__() == (
            'LibyanDinar('
            f'amount: {result}, '
            'alpha_code: "LYD", '
            'numeric_code: "434", '
            'symbol: "د.ل.", '
            'localized_symbol: "د.ل.", '
            'convertion: "", '
            'pattern: "3,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ل.10.00,00000'),
        (-1000, 'د.ل.10.00,00000-')
    ])
    def test_libyan_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = LibyanDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LYD'
        assert custom.numeric_code == '434'
        assert custom.symbol == 'د.ل.'
        assert custom.localized_symbol == 'د.ل.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LYD',
            '434'))
        assert custom.__repr__() == (
            'LibyanDinar('
            f'amount: {amount}, '
            'alpha_code: "LYD", '
            'numeric_code: "434", '
            'symbol: "د.ل.", '
            'localized_symbol: "د.ل.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_libyan_dinar_recreate(amount, new_amount):
        default = LibyanDinar(amount)
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
    def test_libyan_dinar_change_attributes(attribute, value):
        immutable = LibyanDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'LibyanDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_libyan_dinar_add_attributes(attribute, value):
        immutable = LibyanDinar(1000)
        with raises(
                AttributeError,
                match=f'\'LibyanDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (libyan_dinar_one, libyan_dinar_one, libyan_dinar_two, None),
        (libyan_dinar_one, libyan_dinar_one_other, libyan_dinar_two, None),
        (libyan_dinar_two, libyan_dinar_minus_one, libyan_dinar_one, None),
        (libyan_dinar_one, other, None, CurrencyMismatchException),
        (libyan_dinar_one, 1.00, None, CurrencyTypeException),
        (libyan_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_libyan_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (libyan_dinar_one)
    ])
    def test_libyan_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LYD'
        assert new.numeric_code == '434'
        assert new.symbol == 'د.ل.'
        assert new.localized_symbol == 'د.ل.'
        assert new.convertion == ''
        assert new.pattern == '3,.3%s\u00A0%a'


class TestSerbianDinarXK:
    """Serbian Dinar XK currency tests."""

    serbian_dinar_xk_minus_one = SerbianDinarXK(-1)
    serbian_dinar_xk_one_other = SerbianDinarXK(1)
    serbian_dinar_xk_one = SerbianDinarXK(1)
    serbian_dinar_xk_two = SerbianDinarXK(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0дин.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0дин.'),
        (10, '10', '10,00\xa0дин.'),
        (Decimal('10'), '10', '10,00\xa0дин.'),
        ('-3.14', '-3.14', '-3,14\xa0дин.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0дин.'),
        (-10, '-10', '-10,00\xa0дин.'),
        (Decimal('-10'), '-10', '-10,00\xa0дин.')
    ])
    def test_serbian_dinar_xk_default(amount, result, printed):
        default = SerbianDinarXK(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RSD'
        assert default.numeric_code == '941'
        assert default.symbol == 'дин.'
        assert default.localized_symbol == 'дин.'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RSD',
            '941'))
        assert default.__repr__() == (
            'SerbianDinarXK('
            f'amount: {result}, '
            'alpha_code: "RSD", '
            'numeric_code: "941", '
            'symbol: "дин.", '
            'localized_symbol: "дин.", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'дин.10.00,00000'),
        (-1000, 'дин.10.00,00000-')
    ])
    def test_serbian_dinar_xk_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SerbianDinarXK(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RSD'
        assert custom.numeric_code == '941'
        assert custom.symbol == 'дин.'
        assert custom.localized_symbol == 'дин.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RSD',
            '941'))
        assert custom.__repr__() == (
            'SerbianDinarXK('
            f'amount: {amount}, '
            'alpha_code: "RSD", '
            'numeric_code: "941", '
            'symbol: "дин.", '
            'localized_symbol: "дин.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_serbian_dinar_xk_recreate(amount, new_amount):
        default = SerbianDinarXK(amount)
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
    def test_serbian_dinar_xk_change_attributes(attribute, value):
        immutable = SerbianDinarXK(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SerbianDinarXK\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_serbian_dinar_xk_add_attributes(attribute, value):
        immutable = SerbianDinarXK(1000)
        with raises(
                AttributeError,
                match=f'\'SerbianDinarXK\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (serbian_dinar_xk_one, serbian_dinar_xk_one, serbian_dinar_xk_two, None),
        (serbian_dinar_xk_one, serbian_dinar_xk_one_other, serbian_dinar_xk_two, None),
        (serbian_dinar_xk_two, serbian_dinar_xk_minus_one, serbian_dinar_xk_one, None),
        (serbian_dinar_xk_one, other, None, CurrencyMismatchException),
        (serbian_dinar_xk_one, 1.00, None, CurrencyTypeException),
        (serbian_dinar_xk_one, '1.00', None, CurrencyTypeException)
    ])
    def test_serbian_dinar_xk_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (serbian_dinar_xk_one)
    ])
    def test_serbian_dinar_xk_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RSD'
        assert new.numeric_code == '941'
        assert new.symbol == 'дин.'
        assert new.localized_symbol == 'дин.'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestSerbianDinarSR:
    """Serbian Dinar SR currency tests."""

    serbian_dinar_sr_minus_one = SerbianDinarSR(-1)
    serbian_dinar_sr_one_other = SerbianDinarSR(1)
    serbian_dinar_sr_one = SerbianDinarSR(1)
    serbian_dinar_sr_two = SerbianDinarSR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0дин.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0дин.'),
        (10, '10', '10,00\xa0дин.'),
        (Decimal('10'), '10', '10,00\xa0дин.'),
        ('-3.14', '-3.14', '-3,14\xa0дин.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0дин.'),
        (-10, '-10', '-10,00\xa0дин.'),
        (Decimal('-10'), '-10', '-10,00\xa0дин.')
    ])
    def test_serbian_dinar_sr_default(amount, result, printed):
        default = SerbianDinarSR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RSD'
        assert default.numeric_code == '941'
        assert default.symbol == 'дин.'
        assert default.localized_symbol == 'дин.'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RSD',
            '941'))
        assert default.__repr__() == (
            'SerbianDinarSR('
            f'amount: {result}, '
            'alpha_code: "RSD", '
            'numeric_code: "941", '
            'symbol: "дин.", '
            'localized_symbol: "дин.", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'дин.10.00,00000'),
        (-1000, 'дин.10.00,00000-')
    ])
    def test_serbian_dinar_sr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SerbianDinarSR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RSD'
        assert custom.numeric_code == '941'
        assert custom.symbol == 'дин.'
        assert custom.localized_symbol == 'дин.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RSD',
            '941'))
        assert custom.__repr__() == (
            'SerbianDinarSR('
            f'amount: {amount}, '
            'alpha_code: "RSD", '
            'numeric_code: "941", '
            'symbol: "дин.", '
            'localized_symbol: "дин.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_serbian_dinar_sr_recreate(amount, new_amount):
        default = SerbianDinarSR(amount)
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
    def test_serbian_dinar_sr_change_attributes(attribute, value):
        immutable = SerbianDinarSR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SerbianDinarSR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_serbian_dinar_sr_add_attributes(attribute, value):
        immutable = SerbianDinarSR(1000)
        with raises(
                AttributeError,
                match=f'\'SerbianDinarSR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (serbian_dinar_sr_one, serbian_dinar_sr_one, serbian_dinar_sr_two, None),
        (serbian_dinar_sr_one, serbian_dinar_sr_one_other, serbian_dinar_sr_two, None),
        (serbian_dinar_sr_two, serbian_dinar_sr_minus_one, serbian_dinar_sr_one, None),
        (serbian_dinar_sr_one, other, None, CurrencyMismatchException),
        (serbian_dinar_sr_one, 1.00, None, CurrencyTypeException),
        (serbian_dinar_sr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_serbian_dinar_sr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (serbian_dinar_sr_one)
    ])
    def test_serbian_dinar_sr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RSD'
        assert new.numeric_code == '941'
        assert new.symbol == 'дин.'
        assert new.localized_symbol == 'дин.'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestTunisianDinar:
    """Tunisian Dinar currency tests."""

    tunisian_dinar_minus_one = TunisianDinar(-1)
    tunisian_dinar_one_other = TunisianDinar(1)
    tunisian_dinar_one = TunisianDinar(1)
    tunisian_dinar_two = TunisianDinar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.ت.\xa03,140'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.ت.\xa03,140'),
        (10, '10', 'د.ت.\xa010,000'),
        (Decimal('10'), '10', 'د.ت.\xa010,000'),
        ('-3.14', '-3.14', 'د.ت.\xa0-3,140'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.ت.\xa0-3,140'),
        (-10, '-10', 'د.ت.\xa0-10,000'),
        (Decimal('-10'), '-10', 'د.ت.\xa0-10,000')
    ])
    def test_tunisian_dinar_default(amount, result, printed):
        default = TunisianDinar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TND'
        assert default.numeric_code == '788'
        assert default.symbol == 'د.ت.'
        assert default.localized_symbol == 'د.ت.'
        assert default.convertion == ''
        assert default.pattern == '3,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TND',
            '788'))
        assert default.__repr__() == (
            'TunisianDinar('
            f'amount: {result}, '
            'alpha_code: "TND", '
            'numeric_code: "788", '
            'symbol: "د.ت.", '
            'localized_symbol: "د.ت.", '
            'convertion: "", '
            'pattern: "3,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.ت.10.00,00000'),
        (-1000, 'د.ت.10.00,00000-')
    ])
    def test_tunisian_dinar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TunisianDinar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TND'
        assert custom.numeric_code == '788'
        assert custom.symbol == 'د.ت.'
        assert custom.localized_symbol == 'د.ت.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TND',
            '788'))
        assert custom.__repr__() == (
            'TunisianDinar('
            f'amount: {amount}, '
            'alpha_code: "TND", '
            'numeric_code: "788", '
            'symbol: "د.ت.", '
            'localized_symbol: "د.ت.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tunisian_dinar_recreate(amount, new_amount):
        default = TunisianDinar(amount)
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
    def test_tunisian_dinar_change_attributes(attribute, value):
        immutable = TunisianDinar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TunisianDinar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tunisian_dinar_add_attributes(attribute, value):
        immutable = TunisianDinar(1000)
        with raises(
                AttributeError,
                match=f'\'TunisianDinar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tunisian_dinar_one, tunisian_dinar_one, tunisian_dinar_two, None),
        (tunisian_dinar_one, tunisian_dinar_one_other, tunisian_dinar_two, None),
        (tunisian_dinar_two, tunisian_dinar_minus_one, tunisian_dinar_one, None),
        (tunisian_dinar_one, other, None, CurrencyMismatchException),
        (tunisian_dinar_one, 1.00, None, CurrencyTypeException),
        (tunisian_dinar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tunisian_dinar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tunisian_dinar_one)
    ])
    def test_tunisian_dinar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TND'
        assert new.numeric_code == '788'
        assert new.symbol == 'د.ت.'
        assert new.localized_symbol == 'د.ت.'
        assert new.convertion == ''
        assert new.pattern == '3,.3%s\u00A0%a'
