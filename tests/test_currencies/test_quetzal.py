# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Quetzal currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.quetzal import Quetzal


class TestQuetzal:
    """Quetzal currency tests."""

    quetzal_minus_one = Quetzal(-1)
    quetzal_one_other = Quetzal(1)
    quetzal_one = Quetzal(1)
    quetzal_two = Quetzal(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Q\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Q\xa03.14'),
        (10, '10', 'Q\xa010.00'),
        (Decimal('10'), '10', 'Q\xa010.00'),
        ('-3.14', '-3.14', 'Q\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Q\xa0-3.14'),
        (-10, '-10', 'Q\xa0-10.00'),
        (Decimal('-10'), '-10', 'Q\xa0-10.00')
    ])
    def test_quetzal_default(amount, result, printed):
        default = Quetzal(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GTQ'
        assert default.numeric_code == '320'
        assert default.symbol == 'Q'
        assert default.localized_symbol == 'Q'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GTQ',
            '320'))
        assert default.__repr__() == (
            'Quetzal('
            f'amount: {result}, '
            'alpha_code: "GTQ", '
            'numeric_code: "320", '
            'symbol: "Q", '
            'localized_symbol: "Q", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Q10.00,00000'),
        (-1000, 'Q10.00,00000-')
    ])
    def test_quetzal_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Quetzal(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GTQ'
        assert custom.numeric_code == '320'
        assert custom.symbol == 'Q'
        assert custom.localized_symbol == 'Q'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GTQ',
            '320'))
        assert custom.__repr__() == (
            'Quetzal('
            f'amount: {amount}, '
            'alpha_code: "GTQ", '
            'numeric_code: "320", '
            'symbol: "Q", '
            'localized_symbol: "Q", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_quetzal_recreate(amount, new_amount):
        default = Quetzal(amount)
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
    def test_quetzal_change_attributes(attribute, value):
        immutable = Quetzal(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Quetzal\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_quetzal_add_attributes(attribute, value):
        immutable = Quetzal(1000)
        with raises(
                AttributeError,
                match=f'\'Quetzal\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (quetzal_one, quetzal_one, quetzal_two, None),
        (quetzal_one, quetzal_one_other, quetzal_two, None),
        (quetzal_two, quetzal_minus_one, quetzal_one, None),
        (quetzal_one, other, None, CurrencyMismatchException),
        (quetzal_one, 1.00, None, CurrencyTypeException),
        (quetzal_one, '1.00', None, CurrencyTypeException)
    ])
    def test_quetzal_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (quetzal_one)
    ])
    def test_quetzal_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GTQ'
        assert new.numeric_code == '320'
        assert new.symbol == 'Q'
        assert new.localized_symbol == 'Q'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
