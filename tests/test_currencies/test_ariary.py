# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Ariary currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.ariary import MalagasyAriary


class TestMalagasyAriary:
    """Malagasy Ariary currency tests."""

    malagasy_ariary_minus_one = MalagasyAriary(-1)
    malagasy_ariary_one_other = MalagasyAriary(1)
    malagasy_ariary_one = MalagasyAriary(1)
    malagasy_ariary_two = MalagasyAriary(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0Ar'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0Ar'),
        (10, '10', '10\xa0Ar'),
        (Decimal('10'), '10', '10\xa0Ar'),
        ('-3.14', '-3.14', '-3\xa0Ar'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0Ar'),
        (-10, '-10', '-10\xa0Ar'),
        (Decimal('-10'), '-10', '-10\xa0Ar')
    ])
    def test_malagasy_ariary_default(amount, result, printed):
        default = MalagasyAriary(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MGA'
        assert default.numeric_code == '969'
        assert default.symbol == 'Ar'
        assert default.localized_symbol == 'Ar'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MGA',
            '969'))
        assert default.__repr__() == (
            'MalagasyAriary('
            f'amount: {result}, '
            'alpha_code: "MGA", '
            'numeric_code: "969", '
            'symbol: "Ar", '
            'localized_symbol: "Ar", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Ar10.00,00000'),
        (-1000, 'Ar10.00,00000-')
    ])
    def test_malagasy_ariary_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MalagasyAriary(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MGA'
        assert custom.numeric_code == '969'
        assert custom.symbol == 'Ar'
        assert custom.localized_symbol == 'Ar'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MGA',
            '969'))
        assert custom.__repr__() == (
            'MalagasyAriary('
            f'amount: {amount}, '
            'alpha_code: "MGA", '
            'numeric_code: "969", '
            'symbol: "Ar", '
            'localized_symbol: "Ar", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_malagasy_ariary_recreate(amount, new_amount):
        default = MalagasyAriary(amount)
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
    def test_malagasy_ariary_change_attributes(attribute, value):
        immutable = MalagasyAriary(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MalagasyAriary\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_malagasy_ariary_add_attributes(attribute, value):
        immutable = MalagasyAriary(1000)
        with raises(
                AttributeError,
                match=f'\'MalagasyAriary\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (malagasy_ariary_one, malagasy_ariary_one, malagasy_ariary_two, None),
        (malagasy_ariary_one, malagasy_ariary_one_other, malagasy_ariary_two, None),
        (malagasy_ariary_two, malagasy_ariary_minus_one, malagasy_ariary_one, None),
        (malagasy_ariary_one, other, None, CurrencyMismatchException),
        (malagasy_ariary_one, 1.00, None, CurrencyTypeException),
        (malagasy_ariary_one, '1.00', None, CurrencyTypeException)
    ])
    def test_malagasy_ariary_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (malagasy_ariary_one)
    ])
    def test_malagasy_ariary_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MGA'
        assert new.numeric_code == '969'
        assert new.symbol == 'Ar'
        assert new.localized_symbol == 'Ar'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'
