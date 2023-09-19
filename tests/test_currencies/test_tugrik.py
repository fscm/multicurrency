# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Tugrik currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.tugrik import Tugrik


class TestTugrik:
    """Tugrik currency tests."""

    tugrik_minus_one = Tugrik(-1)
    tugrik_one_other = Tugrik(1)
    tugrik_one = Tugrik(1)
    tugrik_two = Tugrik(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₮\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₮\xa03.14'),
        (10, '10', '₮\xa010.00'),
        (Decimal('10'), '10', '₮\xa010.00'),
        ('-3.14', '-3.14', '₮\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₮\xa0-3.14'),
        (-10, '-10', '₮\xa0-10.00'),
        (Decimal('-10'), '-10', '₮\xa0-10.00')
    ])
    def test_tugrik_default(amount, result, printed):
        default = Tugrik(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MNT'
        assert default.numeric_code == '496'
        assert default.symbol == '₮'
        assert default.localized_symbol == '₮'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MNT',
            '496'))
        assert default.__repr__() == (
            'Tugrik('
            f'amount: {result}, '
            'alpha_code: "MNT", '
            'numeric_code: "496", '
            'symbol: "₮", '
            'localized_symbol: "₮", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₮10.00,00000'),
        (-1000, '₮10.00,00000-')
    ])
    def test_tugrik_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Tugrik(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MNT'
        assert custom.numeric_code == '496'
        assert custom.symbol == '₮'
        assert custom.localized_symbol == '₮'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MNT',
            '496'))
        assert custom.__repr__() == (
            'Tugrik('
            f'amount: {amount}, '
            'alpha_code: "MNT", '
            'numeric_code: "496", '
            'symbol: "₮", '
            'localized_symbol: "₮", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tugrik_recreate(amount, new_amount):
        default = Tugrik(amount)
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
    def test_tugrik_change_attributes(attribute, value):
        immutable = Tugrik(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Tugrik\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tugrik_add_attributes(attribute, value):
        immutable = Tugrik(1000)
        with raises(
                AttributeError,
                match=f'\'Tugrik\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tugrik_one, tugrik_one, tugrik_two, None),
        (tugrik_one, tugrik_one_other, tugrik_two, None),
        (tugrik_two, tugrik_minus_one, tugrik_one, None),
        (tugrik_one, other, None, CurrencyMismatchException),
        (tugrik_one, 1.00, None, CurrencyTypeException),
        (tugrik_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tugrik_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tugrik_one)
    ])
    def test_tugrik_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MNT'
        assert new.numeric_code == '496'
        assert new.symbol == '₮'
        assert new.localized_symbol == '₮'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
