# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kyat currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kyat import Kyat


class TestKyat:
    """Kyat currency tests."""

    kyat_minus_one = Kyat(-1)
    kyat_one_other = Kyat(1)
    kyat_one = Kyat(1)
    kyat_two = Kyat(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '၃.၁၄\xa0K'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '၃.၁၄\xa0K'),
        (10, '10', '၁၀.၀၀\xa0K'),
        (Decimal('10'), '10', '၁၀.၀၀\xa0K'),
        ('-3.14', '-3.14', '-၃.၁၄\xa0K'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-၃.၁၄\xa0K'),
        (-10, '-10', '-၁၀.၀၀\xa0K'),
        (Decimal('-10'), '-10', '-၁၀.၀၀\xa0K')
    ])
    def test_kyat_default(amount, result, printed):
        default = Kyat(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MMK'
        assert default.numeric_code == '104'
        assert default.symbol == 'K'
        assert default.localized_symbol == 'K'
        assert default.convertion == '၀၁၂၃၄၅၆၇၈၉-'
        assert default.pattern == '2.,3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MMK',
            '104'))
        assert default.__repr__() == (
            'Kyat('
            f'amount: {result}, '
            'alpha_code: "MMK", '
            'numeric_code: "104", '
            'symbol: "K", '
            'localized_symbol: "K", '
            'convertion: "၀၁၂၃၄၅၆၇၈၉-", '
            'pattern: "2.,3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'K၁၀.၀၀,၀၀၀၀၀'),
        (-1000, 'K၁၀.၀၀,၀၀၀၀၀-')
    ])
    def test_kyat_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Kyat(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MMK'
        assert custom.numeric_code == '104'
        assert custom.symbol == 'K'
        assert custom.localized_symbol == 'K'
        assert custom.convertion == '၀၁၂၃၄၅၆၇၈၉-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MMK',
            '104'))
        assert custom.__repr__() == (
            'Kyat('
            f'amount: {amount}, '
            'alpha_code: "MMK", '
            'numeric_code: "104", '
            'symbol: "K", '
            'localized_symbol: "K", '
            'convertion: "၀၁၂၃၄၅၆၇၈၉-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kyat_recreate(amount, new_amount):
        default = Kyat(amount)
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
    def test_kyat_change_attributes(attribute, value):
        immutable = Kyat(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Kyat\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kyat_add_attributes(attribute, value):
        immutable = Kyat(1000)
        with raises(
                AttributeError,
                match=f'\'Kyat\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kyat_one, kyat_one, kyat_two, None),
        (kyat_one, kyat_one_other, kyat_two, None),
        (kyat_two, kyat_minus_one, kyat_one, None),
        (kyat_one, other, None, CurrencyMismatchException),
        (kyat_one, 1.00, None, CurrencyTypeException),
        (kyat_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kyat_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kyat_one)
    ])
    def test_kyat_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MMK'
        assert new.numeric_code == '104'
        assert new.symbol == 'K'
        assert new.localized_symbol == 'K'
        assert new.convertion == '၀၁၂၃၄၅၆၇၈၉-'
        assert new.pattern == '2.,3%a\u00A0%s'
