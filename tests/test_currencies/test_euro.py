# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Euro currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.euro import (
    Euro,
    EuroSBA,
    EuroAD,
    EuroAT,
    EuroBE,
    EuroCY,
    EuroEE,
    EuroFI,
    EuroFR,
    EuroDE,
    EuroGR,
    EuroIE,
    EuroIT,
    EuroXK,
    EuroLV,
    EuroLT,
    EuroLU,
    EuroMT,
    EuroMC,
    EuroME,
    EuroNL,
    EuroPT,
    EuroSM,
    EuroSK,
    EuroSI,
    EuroES,
    EuroVA)


class TestEuro:
    """Euro currency tests."""

    euro_minus_one = Euro(-1)
    euro_one_other = Euro(1)
    euro_one = Euro(1)
    euro_two = Euro(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euro_default(amount, result, printed):
        default = Euro(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == '€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'Euro('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euro_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Euro(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == '€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'Euro('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euro_recreate(amount, new_amount):
        default = Euro(amount)
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
    def test_euro_change_attributes(attribute, value):
        immutable = Euro(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Euro\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euro_add_attributes(attribute, value):
        immutable = Euro(1000)
        with raises(
                AttributeError,
                match=f'\'Euro\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euro_one, euro_one, euro_two, None),
        (euro_one, euro_one_other, euro_two, None),
        (euro_two, euro_minus_one, euro_one, None),
        (euro_one, other, None, CurrencyMismatchException),
        (euro_one, 1.00, None, CurrencyTypeException),
        (euro_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euro_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euro_one)
    ])
    def test_euro_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == '€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroSBA:
    """EuroSBA currency tests."""

    eurosba_minus_one = EuroSBA(-1)
    eurosba_one_other = EuroSBA(1)
    eurosba_one = EuroSBA(1)
    eurosba_two = EuroSBA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurosba_default(amount, result, printed):
        default = EuroSBA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == '€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroSBA('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurosba_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroSBA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == '€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroSBA('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurosba_recreate(amount, new_amount):
        default = EuroSBA(amount)
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
    def test_eurosba_change_attributes(attribute, value):
        immutable = EuroSBA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroSBA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurosba_add_attributes(attribute, value):
        immutable = EuroSBA(1000)
        with raises(
                AttributeError,
                match=f'\'EuroSBA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurosba_one, eurosba_one, eurosba_two, None),
        (eurosba_one, eurosba_one_other, eurosba_two, None),
        (eurosba_two, eurosba_minus_one, eurosba_one, None),
        (eurosba_one, other, None, CurrencyMismatchException),
        (eurosba_one, 1.00, None, CurrencyTypeException),
        (eurosba_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurosba_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurosba_one)
    ])
    def test_eurosba_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == '€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroAD:
    """EuroAD currency tests."""

    euroad_minus_one = EuroAD(-1)
    euroad_one_other = EuroAD(1)
    euroad_one = EuroAD(1)
    euroad_two = EuroAD(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euroad_default(amount, result, printed):
        default = EuroAD(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'AD€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroAD('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "AD€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroad_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroAD(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'AD€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroAD('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "AD€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroad_recreate(amount, new_amount):
        default = EuroAD(amount)
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
    def test_euroad_change_attributes(attribute, value):
        immutable = EuroAD(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroAD\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroad_add_attributes(attribute, value):
        immutable = EuroAD(1000)
        with raises(
                AttributeError,
                match=f'\'EuroAD\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroad_one, euroad_one, euroad_two, None),
        (euroad_one, euroad_one_other, euroad_two, None),
        (euroad_two, euroad_minus_one, euroad_one, None),
        (euroad_one, other, None, CurrencyMismatchException),
        (euroad_one, 1.00, None, CurrencyTypeException),
        (euroad_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroad_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroad_one)
    ])
    def test_euroad_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'AD€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroAT:
    """EuroAT currency tests."""

    euroat_minus_one = EuroAT(-1)
    euroat_one_other = EuroAT(1)
    euroat_one = EuroAT(1)
    euroat_two = EuroAT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€\xa03,14'),
        (10, '10', '€\xa010,00'),
        (Decimal('10'), '10', '€\xa010,00'),
        ('-3.14', '-3.14', '€\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '€\xa0-3,14'),
        (-10, '-10', '€\xa0-10,00'),
        (Decimal('-10'), '-10', '€\xa0-10,00')
    ])
    def test_euroat_default(amount, result, printed):
        default = EuroAT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'AT€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroAT('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "AT€", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroat_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroAT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'AT€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroAT('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "AT€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroat_recreate(amount, new_amount):
        default = EuroAT(amount)
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
    def test_euroat_change_attributes(attribute, value):
        immutable = EuroAT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroAT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroat_add_attributes(attribute, value):
        immutable = EuroAT(1000)
        with raises(
                AttributeError,
                match=f'\'EuroAT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroat_one, euroat_one, euroat_two, None),
        (euroat_one, euroat_one_other, euroat_two, None),
        (euroat_two, euroat_minus_one, euroat_one, None),
        (euroat_one, other, None, CurrencyMismatchException),
        (euroat_one, 1.00, None, CurrencyTypeException),
        (euroat_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroat_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroat_one)
    ])
    def test_euroat_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'AT€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestEuroBE:
    """EuroBE currency tests."""

    eurobe_minus_one = EuroBE(-1)
    eurobe_one_other = EuroBE(1)
    eurobe_one = EuroBE(1)
    eurobe_two = EuroBE(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€\xa03,14'),
        (10, '10', '€\xa010,00'),
        (Decimal('10'), '10', '€\xa010,00'),
        ('-3.14', '-3.14', '€\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '€\xa0-3,14'),
        (-10, '-10', '€\xa0-10,00'),
        (Decimal('-10'), '-10', '€\xa0-10,00')
    ])
    def test_eurobe_default(amount, result, printed):
        default = EuroBE(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'BE€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroBE('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "BE€", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurobe_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroBE(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'BE€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroBE('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "BE€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurobe_recreate(amount, new_amount):
        default = EuroBE(amount)
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
    def test_eurobe_change_attributes(attribute, value):
        immutable = EuroBE(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroBE\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurobe_add_attributes(attribute, value):
        immutable = EuroBE(1000)
        with raises(
                AttributeError,
                match=f'\'EuroBE\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurobe_one, eurobe_one, eurobe_two, None),
        (eurobe_one, eurobe_one_other, eurobe_two, None),
        (eurobe_two, eurobe_minus_one, eurobe_one, None),
        (eurobe_one, other, None, CurrencyMismatchException),
        (eurobe_one, 1.00, None, CurrencyTypeException),
        (eurobe_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurobe_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurobe_one)
    ])
    def test_eurobe_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'BE€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestEuroCY:
    """EuroCY currency tests."""

    eurocy_minus_one = EuroCY(-1)
    eurocy_one_other = EuroCY(1)
    eurocy_one = EuroCY(1)
    eurocy_two = EuroCY(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurocy_default(amount, result, printed):
        default = EuroCY(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'CY€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroCY('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "CY€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurocy_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroCY(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'CY€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroCY('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "CY€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurocy_recreate(amount, new_amount):
        default = EuroCY(amount)
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
    def test_eurocy_change_attributes(attribute, value):
        immutable = EuroCY(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroCY\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurocy_add_attributes(attribute, value):
        immutable = EuroCY(1000)
        with raises(
                AttributeError,
                match=f'\'EuroCY\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurocy_one, eurocy_one, eurocy_two, None),
        (eurocy_one, eurocy_one_other, eurocy_two, None),
        (eurocy_two, eurocy_minus_one, eurocy_one, None),
        (eurocy_one, other, None, CurrencyMismatchException),
        (eurocy_one, 1.00, None, CurrencyTypeException),
        (eurocy_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurocy_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurocy_one)
    ])
    def test_eurocy_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'CY€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroEE:
    """EuroEE currency tests."""

    euroee_minus_one = EuroEE(-1)
    euroee_one_other = EuroEE(1)
    euroee_one = EuroEE(1)
    euroee_two = EuroEE(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euroee_default(amount, result, printed):
        default = EuroEE(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'EE€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroEE('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "EE€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroEE(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'EE€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroEE('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "EE€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroee_recreate(amount, new_amount):
        default = EuroEE(amount)
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
    def test_euroee_change_attributes(attribute, value):
        immutable = EuroEE(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroEE\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroee_add_attributes(attribute, value):
        immutable = EuroEE(1000)
        with raises(
                AttributeError,
                match=f'\'EuroEE\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroee_one, euroee_one, euroee_two, None),
        (euroee_one, euroee_one_other, euroee_two, None),
        (euroee_two, euroee_minus_one, euroee_one, None),
        (euroee_one, other, None, CurrencyMismatchException),
        (euroee_one, 1.00, None, CurrencyTypeException),
        (euroee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroee_one)
    ])
    def test_euroee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'EE€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroFI:
    """EuroFI currency tests."""

    eurofi_minus_one = EuroFI(-1)
    eurofi_one_other = EuroFI(1)
    eurofi_one = EuroFI(1)
    eurofi_two = EuroFI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurofi_default(amount, result, printed):
        default = EuroFI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'FI€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroFI('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "FI€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurofi_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroFI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'FI€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroFI('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "FI€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurofi_recreate(amount, new_amount):
        default = EuroFI(amount)
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
    def test_eurofi_change_attributes(attribute, value):
        immutable = EuroFI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroFI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurofi_add_attributes(attribute, value):
        immutable = EuroFI(1000)
        with raises(
                AttributeError,
                match=f'\'EuroFI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurofi_one, eurofi_one, eurofi_two, None),
        (eurofi_one, eurofi_one_other, eurofi_two, None),
        (eurofi_two, eurofi_minus_one, eurofi_one, None),
        (eurofi_one, other, None, CurrencyMismatchException),
        (eurofi_one, 1.00, None, CurrencyTypeException),
        (eurofi_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurofi_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurofi_one)
    ])
    def test_eurofi_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'FI€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroFR:
    """EuroFR currency tests."""

    eurofr_minus_one = EuroFR(-1)
    eurofr_one_other = EuroFR(1)
    eurofr_one = EuroFR(1)
    eurofr_two = EuroFR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurofr_default(amount, result, printed):
        default = EuroFR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'FR€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroFR('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "FR€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurofr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroFR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'FR€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroFR('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "FR€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurofr_recreate(amount, new_amount):
        default = EuroFR(amount)
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
    def test_eurofr_change_attributes(attribute, value):
        immutable = EuroFR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroFR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurofr_add_attributes(attribute, value):
        immutable = EuroFR(1000)
        with raises(
                AttributeError,
                match=f'\'EuroFR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurofr_one, eurofr_one, eurofr_two, None),
        (eurofr_one, eurofr_one_other, eurofr_two, None),
        (eurofr_two, eurofr_minus_one, eurofr_one, None),
        (eurofr_one, other, None, CurrencyMismatchException),
        (eurofr_one, 1.00, None, CurrencyTypeException),
        (eurofr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurofr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurofr_one)
    ])
    def test_eurofr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'FR€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroDE:
    """EuroDE currency tests."""

    eurode_minus_one = EuroDE(-1)
    eurode_one_other = EuroDE(1)
    eurode_one = EuroDE(1)
    eurode_two = EuroDE(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurode_default(amount, result, printed):
        default = EuroDE(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'DE€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroDE('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "DE€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurode_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroDE(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'DE€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroDE('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "DE€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurode_recreate(amount, new_amount):
        default = EuroDE(amount)
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
    def test_eurode_change_attributes(attribute, value):
        immutable = EuroDE(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroDE\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurode_add_attributes(attribute, value):
        immutable = EuroDE(1000)
        with raises(
                AttributeError,
                match=f'\'EuroDE\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurode_one, eurode_one, eurode_two, None),
        (eurode_one, eurode_one_other, eurode_two, None),
        (eurode_two, eurode_minus_one, eurode_one, None),
        (eurode_one, other, None, CurrencyMismatchException),
        (eurode_one, 1.00, None, CurrencyTypeException),
        (eurode_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurode_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurode_one)
    ])
    def test_eurode_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'DE€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroGR:
    """EuroGR currency tests."""

    eurogr_minus_one = EuroGR(-1)
    eurogr_one_other = EuroGR(1)
    eurogr_one = EuroGR(1)
    eurogr_two = EuroGR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurogr_default(amount, result, printed):
        default = EuroGR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'GR€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroGR('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "GR€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurogr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroGR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'GR€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroGR('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "GR€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurogr_recreate(amount, new_amount):
        default = EuroGR(amount)
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
    def test_eurogr_change_attributes(attribute, value):
        immutable = EuroGR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroGR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurogr_add_attributes(attribute, value):
        immutable = EuroGR(1000)
        with raises(
                AttributeError,
                match=f'\'EuroGR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurogr_one, eurogr_one, eurogr_two, None),
        (eurogr_one, eurogr_one_other, eurogr_two, None),
        (eurogr_two, eurogr_minus_one, eurogr_one, None),
        (eurogr_one, other, None, CurrencyMismatchException),
        (eurogr_one, 1.00, None, CurrencyTypeException),
        (eurogr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurogr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurogr_one)
    ])
    def test_eurogr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'GR€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroIE:
    """EuroIE currency tests."""

    euroie_minus_one = EuroIE(-1)
    euroie_one_other = EuroIE(1)
    euroie_one = EuroIE(1)
    euroie_two = EuroIE(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€3.14'),
        (10, '10', '€10.00'),
        (Decimal('10'), '10', '€10.00'),
        ('-3.14', '-3.14', '-€3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-€3.14'),
        (-10, '-10', '-€10.00'),
        (Decimal('-10'), '-10', '-€10.00')
    ])
    def test_euroie_default(amount, result, printed):
        default = EuroIE(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'IR€'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroIE('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "IR€", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroie_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroIE(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'IR€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroIE('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "IR€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroie_recreate(amount, new_amount):
        default = EuroIE(amount)
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
    def test_euroie_change_attributes(attribute, value):
        immutable = EuroIE(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroIE\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroie_add_attributes(attribute, value):
        immutable = EuroIE(1000)
        with raises(
                AttributeError,
                match=f'\'EuroIE\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroie_one, euroie_one, euroie_two, None),
        (euroie_one, euroie_one_other, euroie_two, None),
        (euroie_two, euroie_minus_one, euroie_one, None),
        (euroie_one, other, None, CurrencyMismatchException),
        (euroie_one, 1.00, None, CurrencyTypeException),
        (euroie_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroie_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroie_one)
    ])
    def test_euroie_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'IR€'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEuroIT:
    """EuroIT currency tests."""

    euroit_minus_one = EuroIT(-1)
    euroit_one_other = EuroIT(1)
    euroit_one = EuroIT(1)
    euroit_two = EuroIT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euroit_default(amount, result, printed):
        default = EuroIT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'IT€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroIT('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "IT€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroit_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroIT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'IT€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroIT('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "IT€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroit_recreate(amount, new_amount):
        default = EuroIT(amount)
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
    def test_euroit_change_attributes(attribute, value):
        immutable = EuroIT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroIT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroit_add_attributes(attribute, value):
        immutable = EuroIT(1000)
        with raises(
                AttributeError,
                match=f'\'EuroIT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroit_one, euroit_one, euroit_two, None),
        (euroit_one, euroit_one_other, euroit_two, None),
        (euroit_two, euroit_minus_one, euroit_one, None),
        (euroit_one, other, None, CurrencyMismatchException),
        (euroit_one, 1.00, None, CurrencyTypeException),
        (euroit_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroit_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroit_one)
    ])
    def test_euroit_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'IT€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroXK:
    """EuroXK currency tests."""

    euroxk_minus_one = EuroXK(-1)
    euroxk_one_other = EuroXK(1)
    euroxk_one = EuroXK(1)
    euroxk_two = EuroXK(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euroxk_default(amount, result, printed):
        default = EuroXK(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'XK€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroXK('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "XK€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroxk_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroXK(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'XK€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroXK('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "XK€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroxk_recreate(amount, new_amount):
        default = EuroXK(amount)
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
    def test_euroxk_change_attributes(attribute, value):
        immutable = EuroXK(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroXK\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroxk_add_attributes(attribute, value):
        immutable = EuroXK(1000)
        with raises(
                AttributeError,
                match=f'\'EuroXK\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroxk_one, euroxk_one, euroxk_two, None),
        (euroxk_one, euroxk_one_other, euroxk_two, None),
        (euroxk_two, euroxk_minus_one, euroxk_one, None),
        (euroxk_one, other, None, CurrencyMismatchException),
        (euroxk_one, 1.00, None, CurrencyTypeException),
        (euroxk_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroxk_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroxk_one)
    ])
    def test_euroxk_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'XK€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroLV:
    """EuroLV currency tests."""

    eurolv_minus_one = EuroLV(-1)
    eurolv_one_other = EuroLV(1)
    eurolv_one = EuroLV(1)
    eurolv_two = EuroLV(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurolv_default(amount, result, printed):
        default = EuroLV(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'LV€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroLV('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LV€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurolv_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroLV(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'LV€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroLV('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LV€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurolv_recreate(amount, new_amount):
        default = EuroLV(amount)
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
    def test_eurolv_change_attributes(attribute, value):
        immutable = EuroLV(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroLV\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurolv_add_attributes(attribute, value):
        immutable = EuroLV(1000)
        with raises(
                AttributeError,
                match=f'\'EuroLV\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurolv_one, eurolv_one, eurolv_two, None),
        (eurolv_one, eurolv_one_other, eurolv_two, None),
        (eurolv_two, eurolv_minus_one, eurolv_one, None),
        (eurolv_one, other, None, CurrencyMismatchException),
        (eurolv_one, 1.00, None, CurrencyTypeException),
        (eurolv_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurolv_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurolv_one)
    ])
    def test_eurolv_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'LV€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroLT:
    """EuroLT currency tests."""

    eurolt_minus_one = EuroLT(-1)
    eurolt_one_other = EuroLT(1)
    eurolt_one = EuroLT(1)
    eurolt_two = EuroLT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurolt_default(amount, result, printed):
        default = EuroLT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'LT€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroLT('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LT€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurolt_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroLT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'LT€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroLT('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LT€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurolt_recreate(amount, new_amount):
        default = EuroLT(amount)
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
    def test_eurolt_change_attributes(attribute, value):
        immutable = EuroLT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroLT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurolt_add_attributes(attribute, value):
        immutable = EuroLT(1000)
        with raises(
                AttributeError,
                match=f'\'EuroLT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurolt_one, eurolt_one, eurolt_two, None),
        (eurolt_one, eurolt_one_other, eurolt_two, None),
        (eurolt_two, eurolt_minus_one, eurolt_one, None),
        (eurolt_one, other, None, CurrencyMismatchException),
        (eurolt_one, 1.00, None, CurrencyTypeException),
        (eurolt_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurolt_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurolt_one)
    ])
    def test_eurolt_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'LT€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroLU:
    """EuroLU currency tests."""

    eurolu_minus_one = EuroLU(-1)
    eurolu_one_other = EuroLU(1)
    eurolu_one = EuroLU(1)
    eurolu_two = EuroLU(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurolu_default(amount, result, printed):
        default = EuroLU(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'LU€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroLU('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LU€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurolu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroLU(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'LU€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroLU('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "LU€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurolu_recreate(amount, new_amount):
        default = EuroLU(amount)
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
    def test_eurolu_change_attributes(attribute, value):
        immutable = EuroLU(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroLU\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurolu_add_attributes(attribute, value):
        immutable = EuroLU(1000)
        with raises(
                AttributeError,
                match=f'\'EuroLU\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurolu_one, eurolu_one, eurolu_two, None),
        (eurolu_one, eurolu_one_other, eurolu_two, None),
        (eurolu_two, eurolu_minus_one, eurolu_one, None),
        (eurolu_one, other, None, CurrencyMismatchException),
        (eurolu_one, 1.00, None, CurrencyTypeException),
        (eurolu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurolu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurolu_one)
    ])
    def test_eurolu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'LU€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroMT:
    """EuroMT currency tests."""

    euromt_minus_one = EuroMT(-1)
    euromt_one_other = EuroMT(1)
    euromt_one = EuroMT(1)
    euromt_two = EuroMT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€3.14'),
        (10, '10', '€10.00'),
        (Decimal('10'), '10', '€10.00'),
        ('-3.14', '-3.14', '-€3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-€3.14'),
        (-10, '-10', '-€10.00'),
        (Decimal('-10'), '-10', '-€10.00')
    ])
    def test_euromt_default(amount, result, printed):
        default = EuroMT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'MT€'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroMT('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "MT€", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euromt_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroMT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'MT€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroMT('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "MT€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euromt_recreate(amount, new_amount):
        default = EuroMT(amount)
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
    def test_euromt_change_attributes(attribute, value):
        immutable = EuroMT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroMT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euromt_add_attributes(attribute, value):
        immutable = EuroMT(1000)
        with raises(
                AttributeError,
                match=f'\'EuroMT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euromt_one, euromt_one, euromt_two, None),
        (euromt_one, euromt_one_other, euromt_two, None),
        (euromt_two, euromt_minus_one, euromt_one, None),
        (euromt_one, other, None, CurrencyMismatchException),
        (euromt_one, 1.00, None, CurrencyTypeException),
        (euromt_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euromt_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euromt_one)
    ])
    def test_euromt_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'MT€'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEuroMC:
    """EuroMC currency tests."""

    euromc_minus_one = EuroMC(-1)
    euromc_one_other = EuroMC(1)
    euromc_one = EuroMC(1)
    euromc_two = EuroMC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euromc_default(amount, result, printed):
        default = EuroMC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'MC€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroMC('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "MC€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euromc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroMC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'MC€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroMC('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "MC€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euromc_recreate(amount, new_amount):
        default = EuroMC(amount)
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
    def test_euromc_change_attributes(attribute, value):
        immutable = EuroMC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroMC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euromc_add_attributes(attribute, value):
        immutable = EuroMC(1000)
        with raises(
                AttributeError,
                match=f'\'EuroMC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euromc_one, euromc_one, euromc_two, None),
        (euromc_one, euromc_one_other, euromc_two, None),
        (euromc_two, euromc_minus_one, euromc_one, None),
        (euromc_one, other, None, CurrencyMismatchException),
        (euromc_one, 1.00, None, CurrencyTypeException),
        (euromc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euromc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euromc_one)
    ])
    def test_euromc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'MC€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroME:
    """EuroME currency tests."""

    eurome_minus_one = EuroME(-1)
    eurome_one_other = EuroME(1)
    eurome_one = EuroME(1)
    eurome_two = EuroME(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurome_default(amount, result, printed):
        default = EuroME(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'ME€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroME('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "ME€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurome_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroME(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'ME€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroME('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "ME€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurome_recreate(amount, new_amount):
        default = EuroME(amount)
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
    def test_eurome_change_attributes(attribute, value):
        immutable = EuroME(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroME\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurome_add_attributes(attribute, value):
        immutable = EuroME(1000)
        with raises(
                AttributeError,
                match=f'\'EuroME\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurome_one, eurome_one, eurome_two, None),
        (eurome_one, eurome_one_other, eurome_two, None),
        (eurome_two, eurome_minus_one, eurome_one, None),
        (eurome_one, other, None, CurrencyMismatchException),
        (eurome_one, 1.00, None, CurrencyTypeException),
        (eurome_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurome_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurome_one)
    ])
    def test_eurome_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'ME€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroNL:
    """EuroNL currency tests."""

    euronl_minus_one = EuroNL(-1)
    euronl_one_other = EuroNL(1)
    euronl_one = EuroNL(1)
    euronl_two = EuroNL(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€\xa03,14'),
        (10, '10', '€\xa010,00'),
        (Decimal('10'), '10', '€\xa010,00'),
        ('-3.14', '-3.14', '€\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '€\xa0-3,14'),
        (-10, '-10', '€\xa0-10,00'),
        (Decimal('-10'), '-10', '€\xa0-10,00')
    ])
    def test_euronl_default(amount, result, printed):
        default = EuroNL(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'NL€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroNL('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "NL€", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euronl_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroNL(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'NL€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroNL('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "NL€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euronl_recreate(amount, new_amount):
        default = EuroNL(amount)
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
    def test_euronl_change_attributes(attribute, value):
        immutable = EuroNL(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroNL\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euronl_add_attributes(attribute, value):
        immutable = EuroNL(1000)
        with raises(
                AttributeError,
                match=f'\'EuroNL\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euronl_one, euronl_one, euronl_two, None),
        (euronl_one, euronl_one_other, euronl_two, None),
        (euronl_two, euronl_minus_one, euronl_one, None),
        (euronl_one, other, None, CurrencyMismatchException),
        (euronl_one, 1.00, None, CurrencyTypeException),
        (euronl_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euronl_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euronl_one)
    ])
    def test_euronl_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'NL€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestEuroPT:
    """EuroPT currency tests."""

    europt_minus_one = EuroPT(-1)
    europt_one_other = EuroPT(1)
    europt_one = EuroPT(1)
    europt_two = EuroPT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€\xa03,14'),
        (10, '10', '€\xa010,00'),
        (Decimal('10'), '10', '€\xa010,00'),
        ('-3.14', '-3.14', '€\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '€\xa0-3,14'),
        (-10, '-10', '€\xa0-10,00'),
        (Decimal('-10'), '-10', '€\xa0-10,00')
    ])
    def test_europt_default(amount, result, printed):
        default = EuroPT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'PT€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroPT('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "PT€", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_europt_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroPT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'PT€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroPT('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "PT€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_europt_recreate(amount, new_amount):
        default = EuroPT(amount)
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
    def test_europt_change_attributes(attribute, value):
        immutable = EuroPT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroPT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_europt_add_attributes(attribute, value):
        immutable = EuroPT(1000)
        with raises(
                AttributeError,
                match=f'\'EuroPT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (europt_one, europt_one, europt_two, None),
        (europt_one, europt_one_other, europt_two, None),
        (europt_two, europt_minus_one, europt_one, None),
        (europt_one, other, None, CurrencyMismatchException),
        (europt_one, 1.00, None, CurrencyTypeException),
        (europt_one, '1.00', None, CurrencyTypeException)
    ])
    def test_europt_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (europt_one)
    ])
    def test_europt_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'PT€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestEuroSM:
    """EuroSM currency tests."""

    eurosm_minus_one = EuroSM(-1)
    eurosm_one_other = EuroSM(1)
    eurosm_one = EuroSM(1)
    eurosm_two = EuroSM(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurosm_default(amount, result, printed):
        default = EuroSM(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'SM€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroSM('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SM€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurosm_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroSM(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'SM€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroSM('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SM€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurosm_recreate(amount, new_amount):
        default = EuroSM(amount)
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
    def test_eurosm_change_attributes(attribute, value):
        immutable = EuroSM(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroSM\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurosm_add_attributes(attribute, value):
        immutable = EuroSM(1000)
        with raises(
                AttributeError,
                match=f'\'EuroSM\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurosm_one, eurosm_one, eurosm_two, None),
        (eurosm_one, eurosm_one_other, eurosm_two, None),
        (eurosm_two, eurosm_minus_one, eurosm_one, None),
        (eurosm_one, other, None, CurrencyMismatchException),
        (eurosm_one, 1.00, None, CurrencyTypeException),
        (eurosm_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurosm_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurosm_one)
    ])
    def test_eurosm_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'SM€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroSK:
    """EuroSK currency tests."""

    eurosk_minus_one = EuroSK(-1)
    eurosk_one_other = EuroSK(1)
    eurosk_one = EuroSK(1)
    eurosk_two = EuroSK(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurosk_default(amount, result, printed):
        default = EuroSK(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'SK€'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroSK('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SK€", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurosk_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroSK(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'SK€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroSK('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SK€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurosk_recreate(amount, new_amount):
        default = EuroSK(amount)
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
    def test_eurosk_change_attributes(attribute, value):
        immutable = EuroSK(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroSK\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurosk_add_attributes(attribute, value):
        immutable = EuroSK(1000)
        with raises(
                AttributeError,
                match=f'\'EuroSK\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurosk_one, eurosk_one, eurosk_two, None),
        (eurosk_one, eurosk_one_other, eurosk_two, None),
        (eurosk_two, eurosk_minus_one, eurosk_one, None),
        (eurosk_one, other, None, CurrencyMismatchException),
        (eurosk_one, 1.00, None, CurrencyTypeException),
        (eurosk_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurosk_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurosk_one)
    ])
    def test_eurosk_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'SK€'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestEuroSI:
    """EuroSI currency tests."""

    eurosi_minus_one = EuroSI(-1)
    eurosi_one_other = EuroSI(1)
    eurosi_one = EuroSI(1)
    eurosi_two = EuroSI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_eurosi_default(amount, result, printed):
        default = EuroSI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'SI€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroSI('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SI€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurosi_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroSI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'SI€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroSI('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "SI€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurosi_recreate(amount, new_amount):
        default = EuroSI(amount)
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
    def test_eurosi_change_attributes(attribute, value):
        immutable = EuroSI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroSI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurosi_add_attributes(attribute, value):
        immutable = EuroSI(1000)
        with raises(
                AttributeError,
                match=f'\'EuroSI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurosi_one, eurosi_one, eurosi_two, None),
        (eurosi_one, eurosi_one_other, eurosi_two, None),
        (eurosi_two, eurosi_minus_one, eurosi_one, None),
        (eurosi_one, other, None, CurrencyMismatchException),
        (eurosi_one, 1.00, None, CurrencyTypeException),
        (eurosi_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurosi_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurosi_one)
    ])
    def test_eurosi_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'SI€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroES:
    """EuroES currency tests."""

    euroes_minus_one = EuroES(-1)
    euroes_one_other = EuroES(1)
    euroes_one = EuroES(1)
    euroes_two = EuroES(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0€'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0€'),
        (10, '10', '10,00\xa0€'),
        (Decimal('10'), '10', '10,00\xa0€'),
        ('-3.14', '-3.14', '-3,14\xa0€'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0€'),
        (-10, '-10', '-10,00\xa0€'),
        (Decimal('-10'), '-10', '-10,00\xa0€')
    ])
    def test_euroes_default(amount, result, printed):
        default = EuroES(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'ES€'
        assert default.convertion == ''
        assert default.pattern == '2,.3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroES('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "ES€", '
            'convertion: "", '
            'pattern: "2,.3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_euroes_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroES(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'ES€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroES('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "ES€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_euroes_recreate(amount, new_amount):
        default = EuroES(amount)
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
    def test_euroes_change_attributes(attribute, value):
        immutable = EuroES(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroES\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_euroes_add_attributes(attribute, value):
        immutable = EuroES(1000)
        with raises(
                AttributeError,
                match=f'\'EuroES\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (euroes_one, euroes_one, euroes_two, None),
        (euroes_one, euroes_one_other, euroes_two, None),
        (euroes_two, euroes_minus_one, euroes_one, None),
        (euroes_one, other, None, CurrencyMismatchException),
        (euroes_one, 1.00, None, CurrencyTypeException),
        (euroes_one, '1.00', None, CurrencyTypeException)
    ])
    def test_euroes_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (euroes_one)
    ])
    def test_euroes_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'ES€'
        assert new.convertion == ''
        assert new.pattern == '2,.3%a\u00A0%s'


class TestEuroVA:
    """EuroVA currency tests."""

    eurova_minus_one = EuroVA(-1)
    eurova_one_other = EuroVA(1)
    eurova_one = EuroVA(1)
    eurova_two = EuroVA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '€3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '€3.14'),
        (10, '10', '€10.00'),
        (Decimal('10'), '10', '€10.00'),
        ('-3.14', '-3.14', '-€3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-€3.14'),
        (-10, '-10', '-€10.00'),
        (Decimal('-10'), '-10', '-€10.00')
    ])
    def test_eurova_default(amount, result, printed):
        default = EuroVA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EUR'
        assert default.numeric_code == '978'
        assert default.symbol == '€'
        assert default.localized_symbol == 'VA€'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert default.__repr__() == (
            'EuroVA('
            f'amount: {result}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "VA€", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '€10.00,00000'),
        (-1000, '€10.00,00000-')
    ])
    def test_eurova_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EuroVA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EUR'
        assert custom.numeric_code == '978'
        assert custom.symbol == '€'
        assert custom.localized_symbol == 'VA€'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EUR',
            '978'))
        assert custom.__repr__() == (
            'EuroVA('
            f'amount: {amount}, '
            'alpha_code: "EUR", '
            'numeric_code: "978", '
            'symbol: "€", '
            'localized_symbol: "VA€", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eurova_recreate(amount, new_amount):
        default = EuroVA(amount)
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
    def test_eurova_change_attributes(attribute, value):
        immutable = EuroVA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EuroVA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eurova_add_attributes(attribute, value):
        immutable = EuroVA(1000)
        with raises(
                AttributeError,
                match=f'\'EuroVA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eurova_one, eurova_one, eurova_two, None),
        (eurova_one, eurova_one_other, eurova_two, None),
        (eurova_two, eurova_minus_one, eurova_one, None),
        (eurova_one, other, None, CurrencyMismatchException),
        (eurova_one, 1.00, None, CurrencyTypeException),
        (eurova_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eurova_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eurova_one)
    ])
    def test_eurova_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EUR'
        assert new.numeric_code == '978'
        assert new.symbol == '€'
        assert new.localized_symbol == 'VA€'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'
