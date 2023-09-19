# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rupee currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.rupee import (
    IndianRupee,
    IndianRupeeBT,
    IndianRupeeIN,
    SriLankaRupee,
    MauritiusRupee,
    NepaleseRupee,
    PakistanRupee,
    SeychellesRupee)


class TestIndianRupee:
    """Indian Rupee currency tests."""

    indian_rupee_minus_one = IndianRupee(-1)
    indian_rupee_one_other = IndianRupee(1)
    indian_rupee_one = IndianRupee(1)
    indian_rupee_two = IndianRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₹3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₹3.14'),
        (10, '10', '₹10.00'),
        (Decimal('10'), '10', '₹10.00'),
        ('-3.14', '-3.14', '-₹3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₹3.14'),
        (-10, '-10', '-₹10.00'),
        (Decimal('-10'), '-10', '-₹10.00')
    ])
    def test_indian_rupee_default(amount, result, printed):
        default = IndianRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'INR'
        assert default.numeric_code == '356'
        assert default.symbol == '₹'
        assert default.localized_symbol == '₹'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert default.__repr__() == (
            'IndianRupee('
            f'amount: {result}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "₹", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₹10.00,00000'),
        (-1000, '₹10.00,00000-')
    ])
    def test_indian_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IndianRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'INR'
        assert custom.numeric_code == '356'
        assert custom.symbol == '₹'
        assert custom.localized_symbol == '₹'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert custom.__repr__() == (
            'IndianRupee('
            f'amount: {amount}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "₹", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_indian_rupee_recreate(amount, new_amount):
        default = IndianRupee(amount)
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
    def test_indian_rupee_change_attributes(attribute, value):
        immutable = IndianRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IndianRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_indian_rupee_add_attributes(attribute, value):
        immutable = IndianRupee(1000)
        with raises(
                AttributeError,
                match=f'\'IndianRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (indian_rupee_one, indian_rupee_one, indian_rupee_two, None),
        (indian_rupee_one, indian_rupee_one_other, indian_rupee_two, None),
        (indian_rupee_two, indian_rupee_minus_one, indian_rupee_one, None),
        (indian_rupee_one, other, None, CurrencyMismatchException),
        (indian_rupee_one, 1.00, None, CurrencyTypeException),
        (indian_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_indian_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (indian_rupee_one)
    ])
    def test_indian_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'INR'
        assert new.numeric_code == '356'
        assert new.symbol == '₹'
        assert new.localized_symbol == '₹'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestIndianRupeeBT:
    """Indian Rupee BT currency tests."""

    indian_rupee_bt_minus_one = IndianRupeeBT(-1)
    indian_rupee_bt_one_other = IndianRupeeBT(1)
    indian_rupee_bt_one = IndianRupeeBT(1)
    indian_rupee_bt_two = IndianRupeeBT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₹3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₹3.14'),
        (10, '10', '₹10.00'),
        (Decimal('10'), '10', '₹10.00'),
        ('-3.14', '-3.14', '-₹3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₹3.14'),
        (-10, '-10', '-₹10.00'),
        (Decimal('-10'), '-10', '-₹10.00')
    ])
    def test_indian_rupee_bt_default(amount, result, printed):
        default = IndianRupeeBT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'INR'
        assert default.numeric_code == '356'
        assert default.symbol == '₹'
        assert default.localized_symbol == 'BT₹'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert default.__repr__() == (
            'IndianRupeeBT('
            f'amount: {result}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "BT₹", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₹10.00,00000'),
        (-1000, '₹10.00,00000-')
    ])
    def test_indian_rupee_bt_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IndianRupeeBT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'INR'
        assert custom.numeric_code == '356'
        assert custom.symbol == '₹'
        assert custom.localized_symbol == 'BT₹'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert custom.__repr__() == (
            'IndianRupeeBT('
            f'amount: {amount}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "BT₹", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_indian_rupee_bt_recreate(amount, new_amount):
        default = IndianRupeeBT(amount)
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
    def test_indian_rupee_bt_change_attributes(attribute, value):
        immutable = IndianRupeeBT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IndianRupeeBT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_indian_rupee_bt_add_attributes(attribute, value):
        immutable = IndianRupeeBT(1000)
        with raises(
                AttributeError,
                match=f'\'IndianRupeeBT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (indian_rupee_bt_one, indian_rupee_bt_one, indian_rupee_bt_two, None),
        (indian_rupee_bt_one, indian_rupee_bt_one_other, indian_rupee_bt_two, None),
        (indian_rupee_bt_two, indian_rupee_bt_minus_one, indian_rupee_bt_one, None),
        (indian_rupee_bt_one, other, None, CurrencyMismatchException),
        (indian_rupee_bt_one, 1.00, None, CurrencyTypeException),
        (indian_rupee_bt_one, '1.00', None, CurrencyTypeException)
    ])
    def test_indian_rupee_bt_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (indian_rupee_bt_one)
    ])
    def test_indian_rupee_bt_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'INR'
        assert new.numeric_code == '356'
        assert new.symbol == '₹'
        assert new.localized_symbol == 'BT₹'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestIndianRupeeIN:
    """Indian Rupee IN currency tests."""

    indian_rupee_in_minus_one = IndianRupeeIN(-1)
    indian_rupee_in_one_other = IndianRupeeIN(1)
    indian_rupee_in_one = IndianRupeeIN(1)
    indian_rupee_in_two = IndianRupeeIN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₹3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₹3.14'),
        (10, '10', '₹10.00'),
        (Decimal('10'), '10', '₹10.00'),
        ('-3.14', '-3.14', '-₹3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₹3.14'),
        (-10, '-10', '-₹10.00'),
        (Decimal('-10'), '-10', '-₹10.00')
    ])
    def test_indian_rupee_in_default(amount, result, printed):
        default = IndianRupeeIN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'INR'
        assert default.numeric_code == '356'
        assert default.symbol == '₹'
        assert default.localized_symbol == 'IN₹'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert default.__repr__() == (
            'IndianRupeeIN('
            f'amount: {result}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "IN₹", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₹10.00,00000'),
        (-1000, '₹10.00,00000-')
    ])
    def test_indian_rupee_in_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IndianRupeeIN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'INR'
        assert custom.numeric_code == '356'
        assert custom.symbol == '₹'
        assert custom.localized_symbol == 'IN₹'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'INR',
            '356'))
        assert custom.__repr__() == (
            'IndianRupeeIN('
            f'amount: {amount}, '
            'alpha_code: "INR", '
            'numeric_code: "356", '
            'symbol: "₹", '
            'localized_symbol: "IN₹", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_indian_rupee_in_recreate(amount, new_amount):
        default = IndianRupeeIN(amount)
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
    def test_indian_rupee_in_change_attributes(attribute, value):
        immutable = IndianRupeeIN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IndianRupeeIN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_indian_rupee_in_add_attributes(attribute, value):
        immutable = IndianRupeeIN(1000)
        with raises(
                AttributeError,
                match=f'\'IndianRupeeIN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (indian_rupee_in_one, indian_rupee_in_one, indian_rupee_in_two, None),
        (indian_rupee_in_one, indian_rupee_in_one_other, indian_rupee_in_two, None),
        (indian_rupee_in_two, indian_rupee_in_minus_one, indian_rupee_in_one, None),
        (indian_rupee_in_one, other, None, CurrencyMismatchException),
        (indian_rupee_in_one, 1.00, None, CurrencyTypeException),
        (indian_rupee_in_one, '1.00', None, CurrencyTypeException)
    ])
    def test_indian_rupee_in_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (indian_rupee_in_one)
    ])
    def test_indian_rupee_in_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'INR'
        assert new.numeric_code == '356'
        assert new.symbol == '₹'
        assert new.localized_symbol == 'IN₹'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSriLankaRupee:
    """Sri Lanka Rupee currency tests."""

    sri_lanka_rupee_minus_one = SriLankaRupee(-1)
    sri_lanka_rupee_one_other = SriLankaRupee(1)
    sri_lanka_rupee_one = SriLankaRupee(1)
    sri_lanka_rupee_two = SriLankaRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'රු.\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'රු.\xa03.14'),
        (10, '10', 'රු.\xa010.00'),
        (Decimal('10'), '10', 'රු.\xa010.00'),
        ('-3.14', '-3.14', 'රු.\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'රු.\xa0-3.14'),
        (-10, '-10', 'රු.\xa0-10.00'),
        (Decimal('-10'), '-10', 'රු.\xa0-10.00')
    ])
    def test_sri_lanka_rupee_default(amount, result, printed):
        default = SriLankaRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LKR'
        assert default.numeric_code == '144'
        assert default.symbol == 'රු.'
        assert default.localized_symbol == 'රු.'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LKR',
            '144'))
        assert default.__repr__() == (
            'SriLankaRupee('
            f'amount: {result}, '
            'alpha_code: "LKR", '
            'numeric_code: "144", '
            'symbol: "රු.", '
            'localized_symbol: "රු.", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'රු.10.00,00000'),
        (-1000, 'රු.10.00,00000-')
    ])
    def test_sri_lanka_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SriLankaRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LKR'
        assert custom.numeric_code == '144'
        assert custom.symbol == 'රු.'
        assert custom.localized_symbol == 'රු.'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LKR',
            '144'))
        assert custom.__repr__() == (
            'SriLankaRupee('
            f'amount: {amount}, '
            'alpha_code: "LKR", '
            'numeric_code: "144", '
            'symbol: "රු.", '
            'localized_symbol: "රු.", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_sri_lanka_rupee_recreate(amount, new_amount):
        default = SriLankaRupee(amount)
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
    def test_sri_lanka_rupee_change_attributes(attribute, value):
        immutable = SriLankaRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SriLankaRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_sri_lanka_rupee_add_attributes(attribute, value):
        immutable = SriLankaRupee(1000)
        with raises(
                AttributeError,
                match=f'\'SriLankaRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (sri_lanka_rupee_one, sri_lanka_rupee_one, sri_lanka_rupee_two, None),
        (sri_lanka_rupee_one, sri_lanka_rupee_one_other, sri_lanka_rupee_two, None),
        (sri_lanka_rupee_two, sri_lanka_rupee_minus_one, sri_lanka_rupee_one, None),
        (sri_lanka_rupee_one, other, None, CurrencyMismatchException),
        (sri_lanka_rupee_one, 1.00, None, CurrencyTypeException),
        (sri_lanka_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_sri_lanka_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (sri_lanka_rupee_one)
    ])
    def test_sri_lanka_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LKR'
        assert new.numeric_code == '144'
        assert new.symbol == 'රු.'
        assert new.localized_symbol == 'රු.'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestMauritiusRupee:
    """Mauritius Rupee currency tests."""

    mauritius_rupee_minus_one = MauritiusRupee(-1)
    mauritius_rupee_one_other = MauritiusRupee(1)
    mauritius_rupee_one = MauritiusRupee(1)
    mauritius_rupee_two = MauritiusRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₨\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₨\xa03.14'),
        (10, '10', '₨\xa010.00'),
        (Decimal('10'), '10', '₨\xa010.00'),
        ('-3.14', '-3.14', '₨\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₨\xa0-3.14'),
        (-10, '-10', '₨\xa0-10.00'),
        (Decimal('-10'), '-10', '₨\xa0-10.00')
    ])
    def test_mauritius_rupee_default(amount, result, printed):
        default = MauritiusRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'MUR'
        assert default.numeric_code == '480'
        assert default.symbol == '₨'
        assert default.localized_symbol == '₨'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'MUR',
            '480'))
        assert default.__repr__() == (
            'MauritiusRupee('
            f'amount: {result}, '
            'alpha_code: "MUR", '
            'numeric_code: "480", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₨10.00,00000'),
        (-1000, '₨10.00,00000-')
    ])
    def test_mauritius_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = MauritiusRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'MUR'
        assert custom.numeric_code == '480'
        assert custom.symbol == '₨'
        assert custom.localized_symbol == '₨'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'MUR',
            '480'))
        assert custom.__repr__() == (
            'MauritiusRupee('
            f'amount: {amount}, '
            'alpha_code: "MUR", '
            'numeric_code: "480", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_mauritius_rupee_recreate(amount, new_amount):
        default = MauritiusRupee(amount)
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
    def test_mauritius_rupee_change_attributes(attribute, value):
        immutable = MauritiusRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'MauritiusRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_mauritius_rupee_add_attributes(attribute, value):
        immutable = MauritiusRupee(1000)
        with raises(
                AttributeError,
                match=f'\'MauritiusRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (mauritius_rupee_one, mauritius_rupee_one, mauritius_rupee_two, None),
        (mauritius_rupee_one, mauritius_rupee_one_other, mauritius_rupee_two, None),
        (mauritius_rupee_two, mauritius_rupee_minus_one, mauritius_rupee_one, None),
        (mauritius_rupee_one, other, None, CurrencyMismatchException),
        (mauritius_rupee_one, 1.00, None, CurrencyTypeException),
        (mauritius_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_mauritius_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (mauritius_rupee_one)
    ])
    def test_mauritius_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'MUR'
        assert new.numeric_code == '480'
        assert new.symbol == '₨'
        assert new.localized_symbol == '₨'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestNepaleseRupee:
    """Nepalese Rupee currency tests."""

    nepalese_rupee_minus_one = NepaleseRupee(-1)
    nepalese_rupee_one_other = NepaleseRupee(1)
    nepalese_rupee_one = NepaleseRupee(1)
    nepalese_rupee_two = NepaleseRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'नेरू\xa0३.१४'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'नेरू\xa0३.१४'),
        (10, '10', 'नेरू\xa0१०.००'),
        (Decimal('10'), '10', 'नेरू\xa0१०.००'),
        ('-3.14', '-3.14', 'नेरू\xa0-३.१४'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'नेरू\xa0-३.१४'),
        (-10, '-10', 'नेरू\xa0-१०.००'),
        (Decimal('-10'), '-10', 'नेरू\xa0-१०.००')
    ])
    def test_nepalese_rupee_default(amount, result, printed):
        default = NepaleseRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NPR'
        assert default.numeric_code == '524'
        assert default.symbol == 'नेरू'
        assert default.localized_symbol == 'नेरू'
        assert default.convertion == '०१२३४५६७८९-'
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NPR',
            '524'))
        assert default.__repr__() == (
            'NepaleseRupee('
            f'amount: {result}, '
            'alpha_code: "NPR", '
            'numeric_code: "524", '
            'symbol: "नेरू", '
            'localized_symbol: "नेरू", '
            'convertion: "०१२३४५६७८९-", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'नेरू१०.००,०००००'),
        (-1000, 'नेरू१०.००,०००००-')
    ])
    def test_nepalese_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NepaleseRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NPR'
        assert custom.numeric_code == '524'
        assert custom.symbol == 'नेरू'
        assert custom.localized_symbol == 'नेरू'
        assert custom.convertion == '०१२३४५६७८९-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NPR',
            '524'))
        assert custom.__repr__() == (
            'NepaleseRupee('
            f'amount: {amount}, '
            'alpha_code: "NPR", '
            'numeric_code: "524", '
            'symbol: "नेरू", '
            'localized_symbol: "नेरू", '
            'convertion: "०१२३४५६७८९-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_nepalese_rupee_recreate(amount, new_amount):
        default = NepaleseRupee(amount)
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
    def test_nepalese_rupee_change_attributes(attribute, value):
        immutable = NepaleseRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NepaleseRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_nepalese_rupee_add_attributes(attribute, value):
        immutable = NepaleseRupee(1000)
        with raises(
                AttributeError,
                match=f'\'NepaleseRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (nepalese_rupee_one, nepalese_rupee_one, nepalese_rupee_two, None),
        (nepalese_rupee_one, nepalese_rupee_one_other, nepalese_rupee_two, None),
        (nepalese_rupee_two, nepalese_rupee_minus_one, nepalese_rupee_one, None),
        (nepalese_rupee_one, other, None, CurrencyMismatchException),
        (nepalese_rupee_one, 1.00, None, CurrencyTypeException),
        (nepalese_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_nepalese_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (nepalese_rupee_one)
    ])
    def test_nepalese_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NPR'
        assert new.numeric_code == '524'
        assert new.symbol == 'नेरू'
        assert new.localized_symbol == 'नेरू'
        assert new.convertion == '०१२३४५६७८९-'
        assert new.pattern == '2.,3%s\u00A0%a'


class TestPakistanRupee:
    """Pakistan Rupee currency tests."""

    pakistan_rupee_minus_one = PakistanRupee(-1)
    pakistan_rupee_one_other = PakistanRupee(1)
    pakistan_rupee_one = PakistanRupee(1)
    pakistan_rupee_two = PakistanRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₨\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₨\xa03.14'),
        (10, '10', '₨\xa010.00'),
        (Decimal('10'), '10', '₨\xa010.00'),
        ('-3.14', '-3.14', '₨\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₨\xa0-3.14'),
        (-10, '-10', '₨\xa0-10.00'),
        (Decimal('-10'), '-10', '₨\xa0-10.00')
    ])
    def test_pakistan_rupee_default(amount, result, printed):
        default = PakistanRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'PKR'
        assert default.numeric_code == '586'
        assert default.symbol == '₨'
        assert default.localized_symbol == '₨'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'PKR',
            '586'))
        assert default.__repr__() == (
            'PakistanRupee('
            f'amount: {result}, '
            'alpha_code: "PKR", '
            'numeric_code: "586", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₨10.00,00000'),
        (-1000, '₨10.00,00000-')
    ])
    def test_pakistan_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PakistanRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'PKR'
        assert custom.numeric_code == '586'
        assert custom.symbol == '₨'
        assert custom.localized_symbol == '₨'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'PKR',
            '586'))
        assert custom.__repr__() == (
            'PakistanRupee('
            f'amount: {amount}, '
            'alpha_code: "PKR", '
            'numeric_code: "586", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pakistan_rupee_recreate(amount, new_amount):
        default = PakistanRupee(amount)
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
    def test_pakistan_rupee_change_attributes(attribute, value):
        immutable = PakistanRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PakistanRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pakistan_rupee_add_attributes(attribute, value):
        immutable = PakistanRupee(1000)
        with raises(
                AttributeError,
                match=f'\'PakistanRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pakistan_rupee_one, pakistan_rupee_one, pakistan_rupee_two, None),
        (pakistan_rupee_one, pakistan_rupee_one_other, pakistan_rupee_two, None),
        (pakistan_rupee_two, pakistan_rupee_minus_one, pakistan_rupee_one, None),
        (pakistan_rupee_one, other, None, CurrencyMismatchException),
        (pakistan_rupee_one, 1.00, None, CurrencyTypeException),
        (pakistan_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pakistan_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pakistan_rupee_one)
    ])
    def test_pakistan_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'PKR'
        assert new.numeric_code == '586'
        assert new.symbol == '₨'
        assert new.localized_symbol == '₨'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestSeychellesRupee:
    """Seychelles Rupee currency tests."""

    seychelles_rupee_minus_one = SeychellesRupee(-1)
    seychelles_rupee_one_other = SeychellesRupee(1)
    seychelles_rupee_one = SeychellesRupee(1)
    seychelles_rupee_two = SeychellesRupee(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₨\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₨\xa03.14'),
        (10, '10', '₨\xa010.00'),
        (Decimal('10'), '10', '₨\xa010.00'),
        ('-3.14', '-3.14', '₨\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₨\xa0-3.14'),
        (-10, '-10', '₨\xa0-10.00'),
        (Decimal('-10'), '-10', '₨\xa0-10.00')
    ])
    def test_seychelles_rupee_default(amount, result, printed):
        default = SeychellesRupee(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SCR'
        assert default.numeric_code == '690'
        assert default.symbol == '₨'
        assert default.localized_symbol == '₨'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SCR',
            '690'))
        assert default.__repr__() == (
            'SeychellesRupee('
            f'amount: {result}, '
            'alpha_code: "SCR", '
            'numeric_code: "690", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₨10.00,00000'),
        (-1000, '₨10.00,00000-')
    ])
    def test_seychelles_rupee_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SeychellesRupee(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SCR'
        assert custom.numeric_code == '690'
        assert custom.symbol == '₨'
        assert custom.localized_symbol == '₨'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SCR',
            '690'))
        assert custom.__repr__() == (
            'SeychellesRupee('
            f'amount: {amount}, '
            'alpha_code: "SCR", '
            'numeric_code: "690", '
            'symbol: "₨", '
            'localized_symbol: "₨", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_seychelles_rupee_recreate(amount, new_amount):
        default = SeychellesRupee(amount)
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
    def test_seychelles_rupee_change_attributes(attribute, value):
        immutable = SeychellesRupee(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SeychellesRupee\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_seychelles_rupee_add_attributes(attribute, value):
        immutable = SeychellesRupee(1000)
        with raises(
                AttributeError,
                match=f'\'SeychellesRupee\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (seychelles_rupee_one, seychelles_rupee_one, seychelles_rupee_two, None),
        (seychelles_rupee_one, seychelles_rupee_one_other, seychelles_rupee_two, None),
        (seychelles_rupee_two, seychelles_rupee_minus_one, seychelles_rupee_one, None),
        (seychelles_rupee_one, other, None, CurrencyMismatchException),
        (seychelles_rupee_one, 1.00, None, CurrencyTypeException),
        (seychelles_rupee_one, '1.00', None, CurrencyTypeException)
    ])
    def test_seychelles_rupee_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (seychelles_rupee_one)
    ])
    def test_seychelles_rupee_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SCR'
        assert new.numeric_code == '690'
        assert new.symbol == '₨'
        assert new.localized_symbol == '₨'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
