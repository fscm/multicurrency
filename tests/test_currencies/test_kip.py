# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kip currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kip import Kip


class TestKip:
    """Kip currency tests."""

    kip_minus_one = Kip(-1)
    kip_one_other = Kip(1)
    kip_one = Kip(1)
    kip_two = Kip(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₭3,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₭3,14'),
        (10, '10', '₭10,00'),
        (Decimal('10'), '10', '₭10,00'),
        ('-3.14', '-3.14', '-₭3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₭3,14'),
        (-10, '-10', '-₭10,00'),
        (Decimal('-10'), '-10', '-₭10,00')
    ])
    def test_kip_default(amount, result, printed):
        default = Kip(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LAK'
        assert default.numeric_code == '418'
        assert default.symbol == '₭'
        assert default.localized_symbol == '₭'
        assert default.convertion == ''
        assert default.pattern == '2,.3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LAK',
            '418'))
        assert default.__repr__() == (
            'Kip('
            f'amount: {result}, '
            'alpha_code: "LAK", '
            'numeric_code: "418", '
            'symbol: "₭", '
            'localized_symbol: "₭", '
            'convertion: "", '
            'pattern: "2,.3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₭10.00,00000'),
        (-1000, '₭10.00,00000-')
    ])
    def test_kip_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Kip(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LAK'
        assert custom.numeric_code == '418'
        assert custom.symbol == '₭'
        assert custom.localized_symbol == '₭'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LAK',
            '418'))
        assert custom.__repr__() == (
            'Kip('
            f'amount: {amount}, '
            'alpha_code: "LAK", '
            'numeric_code: "418", '
            'symbol: "₭", '
            'localized_symbol: "₭", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kip_recreate(amount, new_amount):
        default = Kip(amount)
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
    def test_kip_change_attributes(attribute, value):
        immutable = Kip(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Kip\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kip_add_attributes(attribute, value):
        immutable = Kip(1000)
        with raises(
                AttributeError,
                match=f'\'Kip\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kip_one, kip_one, kip_two, None),
        (kip_one, kip_one_other, kip_two, None),
        (kip_two, kip_minus_one, kip_one, None),
        (kip_one, other, None, CurrencyMismatchException),
        (kip_one, 1.00, None, CurrencyTypeException),
        (kip_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kip_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kip_one)
    ])
    def test_kip_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LAK'
        assert new.numeric_code == '418'
        assert new.symbol == '₭'
        assert new.localized_symbol == '₭'
        assert new.convertion == ''
        assert new.pattern == '2,.3%-%s%u'
