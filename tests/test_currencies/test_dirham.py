# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dirham currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dirham import (
    UAEDirham,
    MoroccanDirham)


class TestUAEDirham:
    """UAE Dirham currency tests."""

    uae_dirham_minus_one = UAEDirham(-1)
    uae_dirham_one_other = UAEDirham(1)
    uae_dirham_one = UAEDirham(1)
    uae_dirham_two = UAEDirham(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'د.إ.\xa0٣٫١٤'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'د.إ.\xa0٣٫١٤'),
        (10, '10', 'د.إ.\xa0١٠٫٠٠'),
        (Decimal('10'), '10', 'د.إ.\xa0١٠٫٠٠'),
        ('-3.14', '-3.14', 'د.إ.\xa0-٣٫١٤'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'د.إ.\xa0-٣٫١٤'),
        (-10, '-10', 'د.إ.\xa0-١٠٫٠٠'),
        (Decimal('-10'), '-10', 'د.إ.\xa0-١٠٫٠٠')
    ])
    def test_uae_dirham_default(amount, result, printed):
        default = UAEDirham(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AED'
        assert default.numeric_code == '784'
        assert default.symbol == 'د.إ.'
        assert default.localized_symbol == 'د.إ.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AED',
            '784'))
        assert default.__repr__() == (
            'UAEDirham('
            f'amount: {result}, '
            'alpha_code: "AED", '
            'numeric_code: "784", '
            'symbol: "د.إ.", '
            'localized_symbol: "د.إ.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.إ.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.إ.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_uae_dirham_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = UAEDirham(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AED'
        assert custom.numeric_code == '784'
        assert custom.symbol == 'د.إ.'
        assert custom.localized_symbol == 'د.إ.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AED',
            '784'))
        assert custom.__repr__() == (
            'UAEDirham('
            f'amount: {amount}, '
            'alpha_code: "AED", '
            'numeric_code: "784", '
            'symbol: "د.إ.", '
            'localized_symbol: "د.إ.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_uae_dirham_recreate(amount, new_amount):
        default = UAEDirham(amount)
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
    def test_uae_dirham_change_attributes(attribute, value):
        immutable = UAEDirham(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'UAEDirham\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_uae_dirham_add_attributes(attribute, value):
        immutable = UAEDirham(1000)
        with raises(
                AttributeError,
                match=f'\'UAEDirham\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (uae_dirham_one, uae_dirham_one, uae_dirham_two, None),
        (uae_dirham_one, uae_dirham_one_other, uae_dirham_two, None),
        (uae_dirham_two, uae_dirham_minus_one, uae_dirham_one, None),
        (uae_dirham_one, other, None, CurrencyMismatchException),
        (uae_dirham_one, 1.00, None, CurrencyTypeException),
        (uae_dirham_one, '1.00', None, CurrencyTypeException)
    ])
    def test_uae_dirham_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (uae_dirham_one)
    ])
    def test_uae_dirham_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AED'
        assert new.numeric_code == '784'
        assert new.symbol == 'د.إ.'
        assert new.localized_symbol == 'د.إ.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%s\u00A0%a'


class TestMoroccanDirham:
    """Moroccan Dirham currency tests."""

    moroccan_dirham_minus_one = MoroccanDirham(-1)
    moroccan_dirham_one_other = MoroccanDirham(1)
    moroccan_dirham_one = MoroccanDirham(1)
    moroccan_dirham_two = MoroccanDirham(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '٣٫١٤\xa0د.م.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '٣٫١٤\xa0د.م.'),
        (10, '10', '١٠٫٠٠\xa0د.م.'),
        (Decimal('10'), '10', '١٠٫٠٠\xa0د.م.'),
        ('-3.14', '-3.14', '-٣٫١٤\xa0د.م.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-٣٫١٤\xa0د.م.'),
        (-10, '-10', '-١٠٫٠٠\xa0د.م.'),
        (Decimal('-10'), '-10', '-١٠٫٠٠\xa0د.م.')
    ])
    def test_moroccan_dirham_default(amount, result, printed):
        default = MoroccanDirham(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MAD'
        assert default.numeric_code == '504'
        assert default.symbol == 'د.م.'
        assert default.localized_symbol == 'د.م.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MAD',
            '504'))
        assert default.__repr__() == (
            'MoroccanDirham('
            f'amount: {result}, '
            'alpha_code: "MAD", '
            'numeric_code: "504", '
            'symbol: "د.م.", '
            'localized_symbol: "د.م.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'د.م.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'د.م.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_moroccan_dirham_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MoroccanDirham(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MAD'
        assert custom.numeric_code == '504'
        assert custom.symbol == 'د.م.'
        assert custom.localized_symbol == 'د.م.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MAD',
            '504'))
        assert custom.__repr__() == (
            'MoroccanDirham('
            f'amount: {amount}, '
            'alpha_code: "MAD", '
            'numeric_code: "504", '
            'symbol: "د.م.", '
            'localized_symbol: "د.م.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_moroccan_dirham_recreate(amount, new_amount):
        default = MoroccanDirham(amount)
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
    def test_moroccan_dirham_change_attributes(attribute, value):
        immutable = MoroccanDirham(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MoroccanDirham\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_moroccan_dirham_add_attributes(attribute, value):
        immutable = MoroccanDirham(1000)
        with raises(
                AttributeError,
                match=f'\'MoroccanDirham\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (moroccan_dirham_one, moroccan_dirham_one, moroccan_dirham_two, None),
        (moroccan_dirham_one, moroccan_dirham_one_other, moroccan_dirham_two, None),
        (moroccan_dirham_two, moroccan_dirham_minus_one, moroccan_dirham_one, None),
        (moroccan_dirham_one, other, None, CurrencyMismatchException),
        (moroccan_dirham_one, 1.00, None, CurrencyTypeException),
        (moroccan_dirham_one, '1.00', None, CurrencyTypeException)
    ])
    def test_moroccan_dirham_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (moroccan_dirham_one)
    ])
    def test_moroccan_dirham_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MAD'
        assert new.numeric_code == '504'
        assert new.symbol == 'د.م.'
        assert new.localized_symbol == 'د.م.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'
