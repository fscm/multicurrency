# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Riyal currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.riyal import SaudiRiyal


class TestSaudiRiyal:
    """Saudi Riyal currency tests."""

    saudi_riyal_minus_one = SaudiRiyal(-1)
    saudi_riyal_one_other = SaudiRiyal(1)
    saudi_riyal_one = SaudiRiyal(1)
    saudi_riyal_two = SaudiRiyal(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ر.س.\xa0٣٫١٤'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ر.س.\xa0٣٫١٤'),
        (10, '10', 'ر.س.\xa0١٠٫٠٠'),
        (Decimal('10'), '10', 'ر.س.\xa0١٠٫٠٠'),
        ('-3.14', '-3.14', 'ر.س.\xa0-٣٫١٤'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ر.س.\xa0-٣٫١٤'),
        (-10, '-10', 'ر.س.\xa0-١٠٫٠٠'),
        (Decimal('-10'), '-10', 'ر.س.\xa0-١٠٫٠٠')
    ])
    def test_saudi_riyal_default(amount, result, printed):
        default = SaudiRiyal(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SAR'
        assert default.numeric_code == '682'
        assert default.symbol == 'ر.س.'
        assert default.localized_symbol == 'ر.س.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SAR',
            '682'))
        assert default.__repr__() == (
            'SaudiRiyal('
            f'amount: {result}, '
            'alpha_code: "SAR", '
            'numeric_code: "682", '
            'symbol: "ر.س.", '
            'localized_symbol: "ر.س.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ر.س.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ر.س.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_saudi_riyal_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SaudiRiyal(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SAR'
        assert custom.numeric_code == '682'
        assert custom.symbol == 'ر.س.'
        assert custom.localized_symbol == 'ر.س.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SAR',
            '682'))
        assert custom.__repr__() == (
            'SaudiRiyal('
            f'amount: {amount}, '
            'alpha_code: "SAR", '
            'numeric_code: "682", '
            'symbol: "ر.س.", '
            'localized_symbol: "ر.س.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_saudi_riyal_recreate(amount, new_amount):
        default = SaudiRiyal(amount)
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
    def test_saudi_riyal_change_attributes(attribute, value):
        immutable = SaudiRiyal(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SaudiRiyal\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_saudi_riyal_add_attributes(attribute, value):
        immutable = SaudiRiyal(1000)
        with raises(
                AttributeError,
                match=f'\'SaudiRiyal\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (saudi_riyal_one, saudi_riyal_one, saudi_riyal_two, None),
        (saudi_riyal_one, saudi_riyal_one_other, saudi_riyal_two, None),
        (saudi_riyal_two, saudi_riyal_minus_one, saudi_riyal_one, None),
        (saudi_riyal_one, other, None, CurrencyMismatchException),
        (saudi_riyal_one, 1.00, None, CurrencyTypeException),
        (saudi_riyal_one, '1.00', None, CurrencyTypeException)
    ])
    def test_saudi_riyal_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (saudi_riyal_one)
    ])
    def test_saudi_riyal_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SAR'
        assert new.numeric_code == '682'
        assert new.symbol == 'ر.س.'
        assert new.localized_symbol == 'ر.س.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%s\u00A0%a'
