# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Nakfa currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.nakfa import Nakfa


class TestNakfa:
    """Nakfa currency tests."""

    nakfa_minus_one = Nakfa(-1)
    nakfa_one_other = Nakfa(1)
    nakfa_one = Nakfa(1)
    nakfa_two = Nakfa(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Nfk\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Nfk\xa03.14'),
        (10, '10', 'Nfk\xa010.00'),
        (Decimal('10'), '10', 'Nfk\xa010.00'),
        ('-3.14', '-3.14', 'Nfk\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Nfk\xa0-3.14'),
        (-10, '-10', 'Nfk\xa0-10.00'),
        (Decimal('-10'), '-10', 'Nfk\xa0-10.00')
    ])
    def test_nakfa_default(amount, result, printed):
        default = Nakfa(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ERN'
        assert default.numeric_code == '232'
        assert default.symbol == 'Nfk'
        assert default.localized_symbol == 'Nfk'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ERN',
            '232'))
        assert default.__repr__() == (
            'Nakfa('
            f'amount: {result}, '
            'alpha_code: "ERN", '
            'numeric_code: "232", '
            'symbol: "Nfk", '
            'localized_symbol: "Nfk", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Nfk10.00,00000'),
        (-1000, 'Nfk10.00,00000-')
    ])
    def test_nakfa_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Nakfa(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ERN'
        assert custom.numeric_code == '232'
        assert custom.symbol == 'Nfk'
        assert custom.localized_symbol == 'Nfk'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ERN',
            '232'))
        assert custom.__repr__() == (
            'Nakfa('
            f'amount: {amount}, '
            'alpha_code: "ERN", '
            'numeric_code: "232", '
            'symbol: "Nfk", '
            'localized_symbol: "Nfk", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_nakfa_recreate(amount, new_amount):
        default = Nakfa(amount)
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
    def test_nakfa_change_attributes(attribute, value):
        immutable = Nakfa(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Nakfa\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_nakfa_add_attributes(attribute, value):
        immutable = Nakfa(1000)
        with raises(
                AttributeError,
                match=f'\'Nakfa\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (nakfa_one, nakfa_one, nakfa_two, None),
        (nakfa_one, nakfa_one_other, nakfa_two, None),
        (nakfa_two, nakfa_minus_one, nakfa_one, None),
        (nakfa_one, other, None, CurrencyMismatchException),
        (nakfa_one, 1.00, None, CurrencyTypeException),
        (nakfa_one, '1.00', None, CurrencyTypeException)
    ])
    def test_nakfa_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (nakfa_one)
    ])
    def test_nakfa_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ERN'
        assert new.numeric_code == '232'
        assert new.symbol == 'Nfk'
        assert new.localized_symbol == 'Nfk'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
