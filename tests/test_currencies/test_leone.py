# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leone currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.leone import Leone


class TestLeone:
    """Leone currency tests."""

    leone_minus_one = Leone(-1)
    leone_one_other = Leone(1)
    leone_one = Leone(1)
    leone_two = Leone(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Le\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Le\xa03.14'),
        (10, '10', 'Le\xa010.00'),
        (Decimal('10'), '10', 'Le\xa010.00'),
        ('-3.14', '-3.14', 'Le\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Le\xa0-3.14'),
        (-10, '-10', 'Le\xa0-10.00'),
        (Decimal('-10'), '-10', 'Le\xa0-10.00')
    ])
    def test_leone_default(amount, result, printed):
        default = Leone(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SLL'
        assert default.numeric_code == '694'
        assert default.symbol == 'Le'
        assert default.localized_symbol == 'Le'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SLL',
            '694'))
        assert default.__repr__() == (
            'Leone('
            f'amount: {result}, '
            'alpha_code: "SLL", '
            'numeric_code: "694", '
            'symbol: "Le", '
            'localized_symbol: "Le", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Le10.00,00000'),
        (-1000, 'Le10.00,00000-')
    ])
    def test_leone_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Leone(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SLL'
        assert custom.numeric_code == '694'
        assert custom.symbol == 'Le'
        assert custom.localized_symbol == 'Le'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SLL',
            '694'))
        assert custom.__repr__() == (
            'Leone('
            f'amount: {amount}, '
            'alpha_code: "SLL", '
            'numeric_code: "694", '
            'symbol: "Le", '
            'localized_symbol: "Le", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_leone_recreate(amount, new_amount):
        default = Leone(amount)
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
    def test_leone_change_attributes(attribute, value):
        immutable = Leone(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Leone\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_leone_add_attributes(attribute, value):
        immutable = Leone(1000)
        with raises(
                AttributeError,
                match=f'\'Leone\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (leone_one, leone_one, leone_two, None),
        (leone_one, leone_one_other, leone_two, None),
        (leone_two, leone_minus_one, leone_one, None),
        (leone_one, other, None, CurrencyMismatchException),
        (leone_one, 1.00, None, CurrencyTypeException),
        (leone_one, '1.00', None, CurrencyTypeException)
    ])
    def test_leone_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (leone_one)
    ])
    def test_leone_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SLL'
        assert new.numeric_code == '694'
        assert new.symbol == 'Le'
        assert new.localized_symbol == 'Le'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
