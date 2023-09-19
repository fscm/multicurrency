# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Lira currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.lira import (
    TurkishLira,
    TurkishLiraCY,
    TurkishLiraTR)


class TestTurkishLira:
    """Turkish Lira currency tests."""

    turkish_lira_minus_one = TurkishLira(-1)
    turkish_lira_one_other = TurkishLira(1)
    turkish_lira_one = TurkishLira(1)
    turkish_lira_two = TurkishLira(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₤3,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₤3,14'),
        (10, '10', '₤10,00'),
        (Decimal('10'), '10', '₤10,00'),
        ('-3.14', '-3.14', '-₤3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₤3,14'),
        (-10, '-10', '-₤10,00'),
        (Decimal('-10'), '-10', '-₤10,00')
    ])
    def test_turkish_lira_default(amount, result, printed):
        default = TurkishLira(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TRY'
        assert default.numeric_code == '949'
        assert default.symbol == '₤'
        assert default.localized_symbol == '₤'
        assert default.convertion == ''
        assert default.pattern == '2,.3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert default.__repr__() == (
            'TurkishLira('
            f'amount: {result}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "₤", '
            'convertion: "", '
            'pattern: "2,.3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₤10.00,00000'),
        (-1000, '₤10.00,00000-')
    ])
    def test_turkish_lira_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TurkishLira(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TRY'
        assert custom.numeric_code == '949'
        assert custom.symbol == '₤'
        assert custom.localized_symbol == '₤'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert custom.__repr__() == (
            'TurkishLira('
            f'amount: {amount}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "₤", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_turkish_lira_recreate(amount, new_amount):
        default = TurkishLira(amount)
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
    def test_turkish_lira_change_attributes(attribute, value):
        immutable = TurkishLira(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TurkishLira\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_turkish_lira_add_attributes(attribute, value):
        immutable = TurkishLira(1000)
        with raises(
                AttributeError,
                match=f'\'TurkishLira\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (turkish_lira_one, turkish_lira_one, turkish_lira_two, None),
        (turkish_lira_one, turkish_lira_one_other, turkish_lira_two, None),
        (turkish_lira_two, turkish_lira_minus_one, turkish_lira_one, None),
        (turkish_lira_one, other, None, CurrencyMismatchException),
        (turkish_lira_one, 1.00, None, CurrencyTypeException),
        (turkish_lira_one, '1.00', None, CurrencyTypeException)
    ])
    def test_turkish_lira_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (turkish_lira_one)
    ])
    def test_turkish_lira_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TRY'
        assert new.numeric_code == '949'
        assert new.symbol == '₤'
        assert new.localized_symbol == '₤'
        assert new.convertion == ''
        assert new.pattern == '2,.3%-%s%u'


class TestTurkishLiraCY:
    """Turkish Lira CY currency tests."""

    turkish_lira_cy_minus_one = TurkishLiraCY(-1)
    turkish_lira_cy_one_other = TurkishLiraCY(1)
    turkish_lira_cy_one = TurkishLiraCY(1)
    turkish_lira_cy_two = TurkishLiraCY(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₤3,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₤3,14'),
        (10, '10', '₤10,00'),
        (Decimal('10'), '10', '₤10,00'),
        ('-3.14', '-3.14', '-₤3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₤3,14'),
        (-10, '-10', '-₤10,00'),
        (Decimal('-10'), '-10', '-₤10,00')
    ])
    def test_turkish_lira_cy_default(amount, result, printed):
        default = TurkishLiraCY(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TRY'
        assert default.numeric_code == '949'
        assert default.symbol == '₤'
        assert default.localized_symbol == 'CY₤'
        assert default.convertion == ''
        assert default.pattern == '2,.3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert default.__repr__() == (
            'TurkishLiraCY('
            f'amount: {result}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "CY₤", '
            'convertion: "", '
            'pattern: "2,.3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₤10.00,00000'),
        (-1000, '₤10.00,00000-')
    ])
    def test_turkish_lira_cy_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TurkishLiraCY(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TRY'
        assert custom.numeric_code == '949'
        assert custom.symbol == '₤'
        assert custom.localized_symbol == 'CY₤'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert custom.__repr__() == (
            'TurkishLiraCY('
            f'amount: {amount}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "CY₤", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_turkish_lira_cy_recreate(amount, new_amount):
        default = TurkishLiraCY(amount)
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
    def test_turkish_lira_cy_change_attributes(attribute, value):
        immutable = TurkishLiraCY(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TurkishLiraCY\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_turkish_lira_cy_add_attributes(attribute, value):
        immutable = TurkishLiraCY(1000)
        with raises(
                AttributeError,
                match=f'\'TurkishLiraCY\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (turkish_lira_cy_one, turkish_lira_cy_one, turkish_lira_cy_two, None),
        (turkish_lira_cy_one, turkish_lira_cy_one_other, turkish_lira_cy_two, None),
        (turkish_lira_cy_two, turkish_lira_cy_minus_one, turkish_lira_cy_one, None),
        (turkish_lira_cy_one, other, None, CurrencyMismatchException),
        (turkish_lira_cy_one, 1.00, None, CurrencyTypeException),
        (turkish_lira_cy_one, '1.00', None, CurrencyTypeException)
    ])
    def test_turkish_lira_cy_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (turkish_lira_cy_one)
    ])
    def test_turkish_lira_cy_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TRY'
        assert new.numeric_code == '949'
        assert new.symbol == '₤'
        assert new.localized_symbol == 'CY₤'
        assert new.convertion == ''
        assert new.pattern == '2,.3%-%s%u'


class TestTurkishLiraTR:
    """Turkish Lira TR currency tests."""

    turkish_lira_tr_minus_one = TurkishLiraTR(-1)
    turkish_lira_tr_one_other = TurkishLiraTR(1)
    turkish_lira_tr_one = TurkishLiraTR(1)
    turkish_lira_tr_two = TurkishLiraTR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₤3,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₤3,14'),
        (10, '10', '₤10,00'),
        (Decimal('10'), '10', '₤10,00'),
        ('-3.14', '-3.14', '-₤3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₤3,14'),
        (-10, '-10', '-₤10,00'),
        (Decimal('-10'), '-10', '-₤10,00')
    ])
    def test_turkish_lira_tr_default(amount, result, printed):
        default = TurkishLiraTR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TRY'
        assert default.numeric_code == '949'
        assert default.symbol == '₤'
        assert default.localized_symbol == 'TR₤'
        assert default.convertion == ''
        assert default.pattern == '2,.3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert default.__repr__() == (
            'TurkishLiraTR('
            f'amount: {result}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "TR₤", '
            'convertion: "", '
            'pattern: "2,.3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₤10.00,00000'),
        (-1000, '₤10.00,00000-')
    ])
    def test_turkish_lira_tr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TurkishLiraTR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TRY'
        assert custom.numeric_code == '949'
        assert custom.symbol == '₤'
        assert custom.localized_symbol == 'TR₤'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TRY',
            '949'))
        assert custom.__repr__() == (
            'TurkishLiraTR('
            f'amount: {amount}, '
            'alpha_code: "TRY", '
            'numeric_code: "949", '
            'symbol: "₤", '
            'localized_symbol: "TR₤", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_turkish_lira_tr_recreate(amount, new_amount):
        default = TurkishLiraTR(amount)
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
    def test_turkish_lira_tr_change_attributes(attribute, value):
        immutable = TurkishLiraTR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TurkishLiraTR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_turkish_lira_tr_add_attributes(attribute, value):
        immutable = TurkishLiraTR(1000)
        with raises(
                AttributeError,
                match=f'\'TurkishLiraTR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (turkish_lira_tr_one, turkish_lira_tr_one, turkish_lira_tr_two, None),
        (turkish_lira_tr_one, turkish_lira_tr_one_other, turkish_lira_tr_two, None),
        (turkish_lira_tr_two, turkish_lira_tr_minus_one, turkish_lira_tr_one, None),
        (turkish_lira_tr_one, other, None, CurrencyMismatchException),
        (turkish_lira_tr_one, 1.00, None, CurrencyTypeException),
        (turkish_lira_tr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_turkish_lira_tr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (turkish_lira_tr_one)
    ])
    def test_turkish_lira_tr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TRY'
        assert new.numeric_code == '949'
        assert new.symbol == '₤'
        assert new.localized_symbol == 'TR₤'
        assert new.convertion == ''
        assert new.pattern == '2,.3%-%s%u'
