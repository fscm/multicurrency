# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Denar currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.denar import Denar


class TestDenar:
    """Denar currency tests."""

    denar_minus_one = Denar(-1)
    denar_one_other = Denar(1)
    denar_one = Denar(1)
    denar_two = Denar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0ден.'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0ден.'),
        (10, '10', '10,00\xa0ден.'),
        (Decimal('10'), '10', '10,00\xa0ден.'),
        ('-3.14', '-3.14', '-3,14\xa0ден.'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0ден.'),
        (-10, '-10', '-10,00\xa0ден.'),
        (Decimal('-10'), '-10', '-10,00\xa0ден.')
    ])
    def test_denar_default(amount, result, printed):
        default = Denar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MKD'
        assert default.numeric_code == '807'
        assert default.symbol == 'ден.'
        assert default.localized_symbol == 'ден.'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MKD',
            '807'))
        assert default.__repr__() == (
            'Denar('
            f'amount: {result}, '
            'alpha_code: "MKD", '
            'numeric_code: "807", '
            'symbol: "ден.", '
            'localized_symbol: "ден.", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ден.10.00,00000'),
        (-1000, 'ден.10.00,00000-')
    ])
    def test_denar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Denar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MKD'
        assert custom.numeric_code == '807'
        assert custom.symbol == 'ден.'
        assert custom.localized_symbol == 'ден.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MKD',
            '807'))
        assert custom.__repr__() == (
            'Denar('
            f'amount: {amount}, '
            'alpha_code: "MKD", '
            'numeric_code: "807", '
            'symbol: "ден.", '
            'localized_symbol: "ден.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_denar_recreate(amount, new_amount):
        default = Denar(amount)
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
    def test_denar_change_attributes(attribute, value):
        immutable = Denar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Denar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_denar_add_attributes(attribute, value):
        immutable = Denar(1000)
        with raises(
                AttributeError,
                match=f'\'Denar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (denar_one, denar_one, denar_two, None),
        (denar_one, denar_one_other, denar_two, None),
        (denar_two, denar_minus_one, denar_one, None),
        (denar_one, other, None, CurrencyMismatchException),
        (denar_one, 1.00, None, CurrencyTypeException),
        (denar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_denar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (denar_one)
    ])
    def test_denar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MKD'
        assert new.numeric_code == '807'
        assert new.symbol == 'ден.'
        assert new.localized_symbol == 'ден.'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'
