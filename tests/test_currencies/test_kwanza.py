# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Kwanza currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.kwanza import Kwanza


class TestKwanza:
    """Kwanza currency tests."""

    kwanza_minus_one = Kwanza(-1)
    kwanza_one_other = Kwanza(1)
    kwanza_one = Kwanza(1)
    kwanza_two = Kwanza(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0Kz'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0Kz'),
        (10, '10', '10,00\xa0Kz'),
        (Decimal('10'), '10', '10,00\xa0Kz'),
        ('-3.14', '-3.14', '-3,14\xa0Kz'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0Kz'),
        (-10, '-10', '-10,00\xa0Kz'),
        (Decimal('-10'), '-10', '-10,00\xa0Kz')
    ])
    def test_kwanza_default(amount, result, printed):
        default = Kwanza(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AOA'
        assert default.numeric_code == '973'
        assert default.symbol == 'Kz'
        assert default.localized_symbol == 'Kz'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AOA',
            '973'))
        assert default.__repr__() == (
            'Kwanza('
            f'amount: {result}, '
            'alpha_code: "AOA", '
            'numeric_code: "973", '
            'symbol: "Kz", '
            'localized_symbol: "Kz", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Kz10.00,00000'),
        (-1000, 'Kz10.00,00000-')
    ])
    def test_kwanza_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Kwanza(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AOA'
        assert custom.numeric_code == '973'
        assert custom.symbol == 'Kz'
        assert custom.localized_symbol == 'Kz'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AOA',
            '973'))
        assert custom.__repr__() == (
            'Kwanza('
            f'amount: {amount}, '
            'alpha_code: "AOA", '
            'numeric_code: "973", '
            'symbol: "Kz", '
            'localized_symbol: "Kz", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_kwanza_recreate(amount, new_amount):
        default = Kwanza(amount)
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
    def test_kwanza_change_attributes(attribute, value):
        immutable = Kwanza(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Kwanza\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_kwanza_add_attributes(attribute, value):
        immutable = Kwanza(1000)
        with raises(
                AttributeError,
                match=f'\'Kwanza\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (kwanza_one, kwanza_one, kwanza_two, None),
        (kwanza_one, kwanza_one_other, kwanza_two, None),
        (kwanza_two, kwanza_minus_one, kwanza_one, None),
        (kwanza_one, other, None, CurrencyMismatchException),
        (kwanza_one, 1.00, None, CurrencyTypeException),
        (kwanza_one, '1.00', None, CurrencyTypeException)
    ])
    def test_kwanza_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (kwanza_one)
    ])
    def test_kwanza_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AOA'
        assert new.numeric_code == '973'
        assert new.symbol == 'Kz'
        assert new.localized_symbol == 'Kz'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'
