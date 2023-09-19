# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Afghani currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.afghani import Afghani


class TestAfghani:
    """Afghani currency tests."""

    afghani_minus_one = Afghani(-1)
    afghani_one_other = Afghani(1)
    afghani_one = Afghani(1)
    afghani_two = Afghani(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '؋\xa0۳٫۱۴'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '؋\xa0۳٫۱۴'),
        (10, '10', '؋\xa0۱۰٫۰۰'),
        (Decimal('10'), '10', '؋\xa0۱۰٫۰۰'),
        ('-3.14', '-3.14', '؋\xa0-۳٫۱۴'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '؋\xa0-۳٫۱۴'),
        (-10, '-10', '؋\xa0-۱۰٫۰۰'),
        (Decimal('-10'), '-10', '؋\xa0-۱۰٫۰۰')
    ])
    def test_afghani_default(amount, result, printed):
        default = Afghani(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AFN'
        assert default.numeric_code == '971'
        assert default.symbol == '؋'
        assert default.localized_symbol == '؋'
        assert default.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert default.pattern == '2\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AFN',
            '971'))
        assert default.__repr__() == (
            'Afghani('
            f'amount: {result}, '
            'alpha_code: "AFN", '
            'numeric_code: "971", '
            'symbol: "؋", '
            'localized_symbol: "؋", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            'pattern: "2٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '؋۱۰.۰۰,۰۰۰۰۰'),
        (-1000, '؋۱۰.۰۰,۰۰۰۰۰-')
    ])
    def test_afghani_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Afghani(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AFN'
        assert custom.numeric_code == '971'
        assert custom.symbol == '؋'
        assert custom.localized_symbol == '؋'
        assert custom.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AFN',
            '971'))
        assert custom.__repr__() == (
            'Afghani('
            f'amount: {amount}, '
            'alpha_code: "AFN", '
            'numeric_code: "971", '
            'symbol: "؋", '
            'localized_symbol: "؋", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_afghani_recreate(amount, new_amount):
        default = Afghani(amount)
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
    def test_afghani_change_attributes(attribute, value):
        immutable = Afghani(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Afghani\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_afghani_add_attributes(attribute, value):
        immutable = Afghani(1000)
        with raises(
                AttributeError,
                match=f'\'Afghani\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (afghani_one, afghani_one, afghani_two, None),
        (afghani_one, afghani_one_other, afghani_two, None),
        (afghani_two, afghani_minus_one, afghani_one, None),
        (afghani_one, other, None, CurrencyMismatchException),
        (afghani_one, 1.00, None, CurrencyTypeException),
        (afghani_one, '1.00', None, CurrencyTypeException)
    ])
    def test_afghani_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (afghani_one)
    ])
    def test_afghani_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AFN'
        assert new.numeric_code == '971'
        assert new.symbol == '؋'
        assert new.localized_symbol == '؋'
        assert new.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert new.pattern == '2\u066B\u066C3%s\u00A0%a'
