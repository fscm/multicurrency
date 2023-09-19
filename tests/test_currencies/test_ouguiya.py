# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ouguiya currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.ouguiya import Ouguiya


class TestOuguiya:
    """Ouguiya currency tests."""

    ouguiya_minus_one = Ouguiya(-1)
    ouguiya_one_other = Ouguiya(1)
    ouguiya_one = Ouguiya(1)
    ouguiya_two = Ouguiya(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '٣٫١٤\xa0أ.م'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '٣٫١٤\xa0أ.م'),
        (10, '10', '١٠٫٠٠\xa0أ.م'),
        (Decimal('10'), '10', '١٠٫٠٠\xa0أ.م'),
        ('-3.14', '-3.14', '-٣٫١٤\xa0أ.م'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-٣٫١٤\xa0أ.م'),
        (-10, '-10', '-١٠٫٠٠\xa0أ.م'),
        (Decimal('-10'), '-10', '-١٠٫٠٠\xa0أ.م')
    ])
    def test_ouguiya_default(amount, result, printed):
        default = Ouguiya(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MRU'
        assert default.numeric_code == '929'
        assert default.symbol == 'أ.م'
        assert default.localized_symbol == 'أ.م'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MRU',
            '929'))
        assert default.__repr__() == (
            'Ouguiya('
            f'amount: {result}, '
            'alpha_code: "MRU", '
            'numeric_code: "929", '
            'symbol: "أ.م", '
            'localized_symbol: "أ.م", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'أ.م١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'أ.م١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_ouguiya_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Ouguiya(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MRU'
        assert custom.numeric_code == '929'
        assert custom.symbol == 'أ.م'
        assert custom.localized_symbol == 'أ.م'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MRU',
            '929'))
        assert custom.__repr__() == (
            'Ouguiya('
            f'amount: {amount}, '
            'alpha_code: "MRU", '
            'numeric_code: "929", '
            'symbol: "أ.م", '
            'localized_symbol: "أ.م", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_ouguiya_recreate(amount, new_amount):
        default = Ouguiya(amount)
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
    def test_ouguiya_change_attributes(attribute, value):
        immutable = Ouguiya(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Ouguiya\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_ouguiya_add_attributes(attribute, value):
        immutable = Ouguiya(1000)
        with raises(
                AttributeError,
                match=f'\'Ouguiya\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (ouguiya_one, ouguiya_one, ouguiya_two, None),
        (ouguiya_one, ouguiya_one_other, ouguiya_two, None),
        (ouguiya_two, ouguiya_minus_one, ouguiya_one, None),
        (ouguiya_one, other, None, CurrencyMismatchException),
        (ouguiya_one, 1.00, None, CurrencyTypeException),
        (ouguiya_one, '1.00', None, CurrencyTypeException)
    ])
    def test_ouguiya_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (ouguiya_one)
    ])
    def test_ouguiya_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MRU'
        assert new.numeric_code == '929'
        assert new.symbol == 'أ.م'
        assert new.localized_symbol == 'أ.م'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'
