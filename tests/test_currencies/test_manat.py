# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Manat currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.manat import (
    AzerbaijanianManat,
    Manat)


class TestAzerbaijanianManat:
    """Azerbaijanian Manat currency tests."""

    azerbaijanian_manat_minus_one = AzerbaijanianManat(-1)
    azerbaijanian_manat_one_other = AzerbaijanianManat(1)
    azerbaijanian_manat_one = AzerbaijanianManat(1)
    azerbaijanian_manat_two = AzerbaijanianManat(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0₼'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0₼'),
        (10, '10', '10,00\xa0₼'),
        (Decimal('10'), '10', '10,00\xa0₼'),
        ('-3.14', '-3.14', '-3,14\xa0₼'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0₼'),
        (-10, '-10', '-10,00\xa0₼'),
        (Decimal('-10'), '-10', '-10,00\xa0₼')
    ])
    def test_azerbaijanian_manat_default(amount, result, printed):
        default = AzerbaijanianManat(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AZN'
        assert default.numeric_code == '944'
        assert default.symbol == '₼'
        assert default.localized_symbol == '₼'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AZN',
            '944'))
        assert default.__repr__() == (
            'AzerbaijanianManat('
            f'amount: {result}, '
            'alpha_code: "AZN", '
            'numeric_code: "944", '
            'symbol: "₼", '
            'localized_symbol: "₼", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₼10.00,00000'),
        (-1000, '₼10.00,00000-')
    ])
    def test_azerbaijanian_manat_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AzerbaijanianManat(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AZN'
        assert custom.numeric_code == '944'
        assert custom.symbol == '₼'
        assert custom.localized_symbol == '₼'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AZN',
            '944'))
        assert custom.__repr__() == (
            'AzerbaijanianManat('
            f'amount: {amount}, '
            'alpha_code: "AZN", '
            'numeric_code: "944", '
            'symbol: "₼", '
            'localized_symbol: "₼", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_azerbaijanian_manat_recreate(amount, new_amount):
        default = AzerbaijanianManat(amount)
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
    def test_azerbaijanian_manat_change_attributes(attribute, value):
        immutable = AzerbaijanianManat(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AzerbaijanianManat\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_azerbaijanian_manat_add_attributes(attribute, value):
        immutable = AzerbaijanianManat(1000)
        with raises(
                AttributeError,
                match=f'\'AzerbaijanianManat\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (azerbaijanian_manat_one, azerbaijanian_manat_one, azerbaijanian_manat_two, None),
        (azerbaijanian_manat_one, azerbaijanian_manat_one_other, azerbaijanian_manat_two, None),
        (azerbaijanian_manat_two, azerbaijanian_manat_minus_one, azerbaijanian_manat_one, None),
        (azerbaijanian_manat_one, other, None, CurrencyMismatchException),
        (azerbaijanian_manat_one, 1.00, None, CurrencyTypeException),
        (azerbaijanian_manat_one, '1.00', None, CurrencyTypeException)
    ])
    def test_azerbaijanian_manat_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (azerbaijanian_manat_one)
    ])
    def test_azerbaijanian_manat_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AZN'
        assert new.numeric_code == '944'
        assert new.symbol == '₼'
        assert new.localized_symbol == '₼'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestManat:
    """Manat currency tests."""

    manat_minus_one = Manat(-1)
    manat_one_other = Manat(1)
    manat_one = Manat(1)
    manat_two = Manat(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0m'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0m'),
        (10, '10', '10,00\xa0m'),
        (Decimal('10'), '10', '10,00\xa0m'),
        ('-3.14', '-3.14', '-3,14\xa0m'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0m'),
        (-10, '-10', '-10,00\xa0m'),
        (Decimal('-10'), '-10', '-10,00\xa0m')
    ])
    def test_manat_default(amount, result, printed):
        default = Manat(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TMT'
        assert default.numeric_code == '934'
        assert default.symbol == 'm'
        assert default.localized_symbol == 'm'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TMT',
            '934'))
        assert default.__repr__() == (
            'Manat('
            f'amount: {result}, '
            'alpha_code: "TMT", '
            'numeric_code: "934", '
            'symbol: "m", '
            'localized_symbol: "m", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'm10.00,00000'),
        (-1000, 'm10.00,00000-')
    ])
    def test_manat_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Manat(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TMT'
        assert custom.numeric_code == '934'
        assert custom.symbol == 'm'
        assert custom.localized_symbol == 'm'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TMT',
            '934'))
        assert custom.__repr__() == (
            'Manat('
            f'amount: {amount}, '
            'alpha_code: "TMT", '
            'numeric_code: "934", '
            'symbol: "m", '
            'localized_symbol: "m", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_manat_recreate(amount, new_amount):
        default = Manat(amount)
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
    def test_manat_change_attributes(attribute, value):
        immutable = Manat(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Manat\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_manat_add_attributes(attribute, value):
        immutable = Manat(1000)
        with raises(
                AttributeError,
                match=f'\'Manat\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (manat_one, manat_one, manat_two, None),
        (manat_one, manat_one_other, manat_two, None),
        (manat_two, manat_minus_one, manat_one, None),
        (manat_one, other, None, CurrencyMismatchException),
        (manat_one, 1.00, None, CurrencyTypeException),
        (manat_one, '1.00', None, CurrencyTypeException)
    ])
    def test_manat_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (manat_one)
    ])
    def test_manat_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TMT'
        assert new.numeric_code == '934'
        assert new.symbol == 'm'
        assert new.localized_symbol == 'm'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
