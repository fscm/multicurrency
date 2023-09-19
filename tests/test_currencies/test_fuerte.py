# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Fuerte currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.fuerte import BolivarFuerte


class TestBolivarFuerte:
    """Bolivar Fuerte currency tests."""

    bolivar_fuerte_minus_one = BolivarFuerte(-1)
    bolivar_fuerte_one_other = BolivarFuerte(1)
    bolivar_fuerte_one = BolivarFuerte(1)
    bolivar_fuerte_two = BolivarFuerte(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Bs.F.\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Bs.F.\xa03,14'),
        (10, '10', 'Bs.F.\xa010,00'),
        (Decimal('10'), '10', 'Bs.F.\xa010,00'),
        ('-3.14', '-3.14', 'Bs.F.\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'Bs.F.\xa0-3,14'),
        (-10, '-10', 'Bs.F.\xa0-10,00'),
        (Decimal('-10'), '-10', 'Bs.F.\xa0-10,00')
    ])
    def test_bolivar_fuerte_default(amount, result, printed):
        default = BolivarFuerte(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'VEF'
        assert default.numeric_code == '937'
        assert default.symbol == 'Bs.F.'
        assert default.localized_symbol == 'Bs.F.'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'VEF',
            '937'))
        assert default.__repr__() == (
            'BolivarFuerte('
            f'amount: {result}, '
            'alpha_code: "VEF", '
            'numeric_code: "937", '
            'symbol: "Bs.F.", '
            'localized_symbol: "Bs.F.", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Bs.F.10.00,00000'),
        (-1000, 'Bs.F.10.00,00000-')
    ])
    def test_bolivar_fuerte_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BolivarFuerte(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'VEF'
        assert custom.numeric_code == '937'
        assert custom.symbol == 'Bs.F.'
        assert custom.localized_symbol == 'Bs.F.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'VEF',
            '937'))
        assert custom.__repr__() == (
            'BolivarFuerte('
            f'amount: {amount}, '
            'alpha_code: "VEF", '
            'numeric_code: "937", '
            'symbol: "Bs.F.", '
            'localized_symbol: "Bs.F.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bolivar_fuerte_recreate(amount, new_amount):
        default = BolivarFuerte(amount)
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
    def test_bolivar_fuerte_change_attributes(attribute, value):
        immutable = BolivarFuerte(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BolivarFuerte\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bolivar_fuerte_add_attributes(attribute, value):
        immutable = BolivarFuerte(1000)
        with raises(
                AttributeError,
                match=f'\'BolivarFuerte\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bolivar_fuerte_one, bolivar_fuerte_one, bolivar_fuerte_two, None),
        (bolivar_fuerte_one, bolivar_fuerte_one_other, bolivar_fuerte_two, None),
        (bolivar_fuerte_two, bolivar_fuerte_minus_one, bolivar_fuerte_one, None),
        (bolivar_fuerte_one, other, None, CurrencyMismatchException),
        (bolivar_fuerte_one, 1.00, None, CurrencyTypeException),
        (bolivar_fuerte_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bolivar_fuerte_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bolivar_fuerte_one)
    ])
    def test_bolivar_fuerte_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'VEF'
        assert new.numeric_code == '937'
        assert new.symbol == 'Bs.F.'
        assert new.localized_symbol == 'Bs.F.'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'
