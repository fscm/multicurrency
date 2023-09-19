# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Krona currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.krona import (
    IcelandKrona,
    SwedishKrona)


class TestIcelandKrona:
    """Iceland Krona currency tests."""

    iceland_krona_minus_one = IcelandKrona(-1)
    iceland_krona_one_other = IcelandKrona(1)
    iceland_krona_one = IcelandKrona(1)
    iceland_krona_two = IcelandKrona(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0Kr'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0Kr'),
        (10, '10', '10\xa0Kr'),
        (Decimal('10'), '10', '10\xa0Kr'),
        ('-3.14', '-3.14', '-3\xa0Kr'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0Kr'),
        (-10, '-10', '-10\xa0Kr'),
        (Decimal('-10'), '-10', '-10\xa0Kr')
    ])
    def test_iceland_krona_default(amount, result, printed):
        default = IcelandKrona(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ISK'
        assert default.numeric_code == '352'
        assert default.symbol == 'Kr'
        assert default.localized_symbol == 'Kr'
        assert default.convertion == ''
        assert default.pattern == '0,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ISK',
            '352'))
        assert default.__repr__() == (
            'IcelandKrona('
            f'amount: {result}, '
            'alpha_code: "ISK", '
            'numeric_code: "352", '
            'symbol: "Kr", '
            'localized_symbol: "Kr", '
            'convertion: "", '
            'pattern: "0,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Kr10.00,00000'),
        (-1000, 'Kr10.00,00000-')
    ])
    def test_iceland_krona_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IcelandKrona(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ISK'
        assert custom.numeric_code == '352'
        assert custom.symbol == 'Kr'
        assert custom.localized_symbol == 'Kr'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ISK',
            '352'))
        assert custom.__repr__() == (
            'IcelandKrona('
            f'amount: {amount}, '
            'alpha_code: "ISK", '
            'numeric_code: "352", '
            'symbol: "Kr", '
            'localized_symbol: "Kr", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_iceland_krona_recreate(amount, new_amount):
        default = IcelandKrona(amount)
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
    def test_iceland_krona_change_attributes(attribute, value):
        immutable = IcelandKrona(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IcelandKrona\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_iceland_krona_add_attributes(attribute, value):
        immutable = IcelandKrona(1000)
        with raises(
                AttributeError,
                match=f'\'IcelandKrona\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (iceland_krona_one, iceland_krona_one, iceland_krona_two, None),
        (iceland_krona_one, iceland_krona_one_other, iceland_krona_two, None),
        (iceland_krona_two, iceland_krona_minus_one, iceland_krona_one, None),
        (iceland_krona_one, other, None, CurrencyMismatchException),
        (iceland_krona_one, 1.00, None, CurrencyTypeException),
        (iceland_krona_one, '1.00', None, CurrencyTypeException)
    ])
    def test_iceland_krona_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (iceland_krona_one)
    ])
    def test_iceland_krona_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ISK'
        assert new.numeric_code == '352'
        assert new.symbol == 'Kr'
        assert new.localized_symbol == 'Kr'
        assert new.convertion == ''
        assert new.pattern == '0,.3%a\u00A0%s'


class TestSwedishKrona:
    """Swedish Krona currency tests."""

    swedish_krona_minus_one = SwedishKrona(-1)
    swedish_krona_one_other = SwedishKrona(1)
    swedish_krona_one = SwedishKrona(1)
    swedish_krona_two = SwedishKrona(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0kr'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0kr'),
        (10, '10', '10,00\xa0kr'),
        (Decimal('10'), '10', '10,00\xa0kr'),
        ('-3.14', '-3.14', '-3,14\xa0kr'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0kr'),
        (-10, '-10', '-10,00\xa0kr'),
        (Decimal('-10'), '-10', '-10,00\xa0kr')
    ])
    def test_swedish_krona_default(amount, result, printed):
        default = SwedishKrona(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SEK'
        assert default.numeric_code == '752'
        assert default.symbol == 'kr'
        assert default.localized_symbol == 'kr'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SEK',
            '752'))
        assert default.__repr__() == (
            'SwedishKrona('
            f'amount: {result}, '
            'alpha_code: "SEK", '
            'numeric_code: "752", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'kr10.00,00000'),
        (-1000, 'kr10.00,00000-')
    ])
    def test_swedish_krona_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SwedishKrona(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SEK'
        assert custom.numeric_code == '752'
        assert custom.symbol == 'kr'
        assert custom.localized_symbol == 'kr'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SEK',
            '752'))
        assert custom.__repr__() == (
            'SwedishKrona('
            f'amount: {amount}, '
            'alpha_code: "SEK", '
            'numeric_code: "752", '
            'symbol: "kr", '
            'localized_symbol: "kr", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_swedish_krona_recreate(amount, new_amount):
        default = SwedishKrona(amount)
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
    def test_swedish_krona_change_attributes(attribute, value):
        immutable = SwedishKrona(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SwedishKrona\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_swedish_krona_add_attributes(attribute, value):
        immutable = SwedishKrona(1000)
        with raises(
                AttributeError,
                match=f'\'SwedishKrona\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (swedish_krona_one, swedish_krona_one, swedish_krona_two, None),
        (swedish_krona_one, swedish_krona_one_other, swedish_krona_two, None),
        (swedish_krona_two, swedish_krona_minus_one, swedish_krona_one, None),
        (swedish_krona_one, other, None, CurrencyMismatchException),
        (swedish_krona_one, 1.00, None, CurrencyTypeException),
        (swedish_krona_one, '1.00', None, CurrencyTypeException)
    ])
    def test_swedish_krona_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (swedish_krona_one)
    ])
    def test_swedish_krona_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SEK'
        assert new.numeric_code == '752'
        assert new.symbol == 'kr'
        assert new.localized_symbol == 'kr'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
