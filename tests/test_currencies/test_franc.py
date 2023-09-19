# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Franc currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.franc import (
    BurundiFranc,
    CongoleseFranc,
    SwissFranc,
    SwissFrancLI,
    SwissFrancCH,
    DjiboutiFranc,
    GuineaFranc,
    RwandaFranc,
    CFAFrancBEAC,
    CFAFrancBEACCM,
    CFAFrancBEACCF,
    CFAFrancBEACTD,
    CFAFrancBEACCD,
    CFAFrancBEACGQ,
    CFAFrancBEACGA,
    CFAFrancBCEAO,
    CFAFrancBCEAOBJ,
    CFAFrancBCEAOBF,
    CFAFrancBCEAOCI,
    CFAFrancBCEAOGW,
    CFAFrancBCEAOML,
    CFAFrancBCEAONG,
    CFAFrancBCEAOSN,
    CFAFrancBCEAOTG,
    CFPFranc,
    CFPFrancPF,
    CFPFrancNC,
    CFPFrancWF)


class TestBurundiFranc:
    """Burundi Franc currency tests."""

    burundi_franc_minus_one = BurundiFranc(-1)
    burundi_franc_one_other = BurundiFranc(1)
    burundi_franc_one = BurundiFranc(1)
    burundi_franc_two = BurundiFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_burundi_franc_default(amount, result, printed):
        default = BurundiFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BIF'
        assert default.numeric_code == '108'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'BI₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BIF',
            '108'))
        assert default.__repr__() == (
            'BurundiFranc('
            f'amount: {result}, '
            'alpha_code: "BIF", '
            'numeric_code: "108", '
            'symbol: "₣", '
            'localized_symbol: "BI₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_burundi_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BurundiFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BIF'
        assert custom.numeric_code == '108'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'BI₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BIF',
            '108'))
        assert custom.__repr__() == (
            'BurundiFranc('
            f'amount: {amount}, '
            'alpha_code: "BIF", '
            'numeric_code: "108", '
            'symbol: "₣", '
            'localized_symbol: "BI₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_burundi_franc_recreate(amount, new_amount):
        default = BurundiFranc(amount)
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
    def test_burundi_franc_change_attributes(attribute, value):
        immutable = BurundiFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BurundiFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_burundi_franc_add_attributes(attribute, value):
        immutable = BurundiFranc(1000)
        with raises(
                AttributeError,
                match=f'\'BurundiFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (burundi_franc_one, burundi_franc_one, burundi_franc_two, None),
        (burundi_franc_one, burundi_franc_one_other, burundi_franc_two, None),
        (burundi_franc_two, burundi_franc_minus_one, burundi_franc_one, None),
        (burundi_franc_one, other, None, CurrencyMismatchException),
        (burundi_franc_one, 1.00, None, CurrencyTypeException),
        (burundi_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_burundi_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (burundi_franc_one)
    ])
    def test_burundi_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BIF'
        assert new.numeric_code == '108'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'BI₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCongoleseFranc:
    """Congolese Franc currency tests."""

    congolese_franc_minus_one = CongoleseFranc(-1)
    congolese_franc_one_other = CongoleseFranc(1)
    congolese_franc_one = CongoleseFranc(1)
    congolese_franc_two = CongoleseFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0₣'),
        (10, '10', '10,00\xa0₣'),
        (Decimal('10'), '10', '10,00\xa0₣'),
        ('-3.14', '-3.14', '-3,14\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0₣'),
        (-10, '-10', '-10,00\xa0₣'),
        (Decimal('-10'), '-10', '-10,00\xa0₣')
    ])
    def test_congolese_franc_default(amount, result, printed):
        default = CongoleseFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CDF'
        assert default.numeric_code == '976'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CD₣'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CDF',
            '976'))
        assert default.__repr__() == (
            'CongoleseFranc('
            f'amount: {result}, '
            'alpha_code: "CDF", '
            'numeric_code: "976", '
            'symbol: "₣", '
            'localized_symbol: "CD₣", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_congolese_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CongoleseFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CDF'
        assert custom.numeric_code == '976'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CD₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CDF',
            '976'))
        assert custom.__repr__() == (
            'CongoleseFranc('
            f'amount: {amount}, '
            'alpha_code: "CDF", '
            'numeric_code: "976", '
            'symbol: "₣", '
            'localized_symbol: "CD₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_congolese_franc_recreate(amount, new_amount):
        default = CongoleseFranc(amount)
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
    def test_congolese_franc_change_attributes(attribute, value):
        immutable = CongoleseFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CongoleseFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_congolese_franc_add_attributes(attribute, value):
        immutable = CongoleseFranc(1000)
        with raises(
                AttributeError,
                match=f'\'CongoleseFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (congolese_franc_one, congolese_franc_one, congolese_franc_two, None),
        (congolese_franc_one, congolese_franc_one_other, congolese_franc_two, None),
        (congolese_franc_two, congolese_franc_minus_one, congolese_franc_one, None),
        (congolese_franc_one, other, None, CurrencyMismatchException),
        (congolese_franc_one, 1.00, None, CurrencyTypeException),
        (congolese_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_congolese_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (congolese_franc_one)
    ])
    def test_congolese_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CDF'
        assert new.numeric_code == '976'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CD₣'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestSwissFranc:
    """Swiss Franc currency tests."""

    swiss_franc_minus_one = SwissFranc(-1)
    swiss_franc_one_other = SwissFranc(1)
    swiss_franc_one = SwissFranc(1)
    swiss_franc_two = SwissFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₣\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₣\xa03.14'),
        (10, '10', '₣\xa010.00'),
        (Decimal('10'), '10', '₣\xa010.00'),
        ('-3.14', '-3.14', '₣\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₣\xa0-3.14'),
        (-10, '-10', '₣\xa0-10.00'),
        (Decimal('-10'), '-10', '₣\xa0-10.00')
    ])
    def test_swiss_franc_default(amount, result, printed):
        default = SwissFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CHF'
        assert default.numeric_code == '756'
        assert default.symbol == '₣'
        assert default.localized_symbol == '₣'
        assert default.convertion == ''
        assert default.pattern == '2.\u00273%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert default.__repr__() == (
            'SwissFranc('
            f'amount: {result}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            'pattern: "2.\'3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_swiss_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SwissFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CHF'
        assert custom.numeric_code == '756'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == '₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert custom.__repr__() == (
            'SwissFranc('
            f'amount: {amount}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_swiss_franc_recreate(amount, new_amount):
        default = SwissFranc(amount)
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
    def test_swiss_franc_change_attributes(attribute, value):
        immutable = SwissFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SwissFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_swiss_franc_add_attributes(attribute, value):
        immutable = SwissFranc(1000)
        with raises(
                AttributeError,
                match=f'\'SwissFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (swiss_franc_one, swiss_franc_one, swiss_franc_two, None),
        (swiss_franc_one, swiss_franc_one_other, swiss_franc_two, None),
        (swiss_franc_two, swiss_franc_minus_one, swiss_franc_one, None),
        (swiss_franc_one, other, None, CurrencyMismatchException),
        (swiss_franc_one, 1.00, None, CurrencyTypeException),
        (swiss_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_swiss_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (swiss_franc_one)
    ])
    def test_swiss_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CHF'
        assert new.numeric_code == '756'
        assert new.symbol == '₣'
        assert new.localized_symbol == '₣'
        assert new.convertion == ''
        assert new.pattern == '2.\u00273%s\u00A0%a'


class TestSwissFrancLI:
    """Swiss Franc LI currency tests."""

    swiss_franc_li_minus_one = SwissFrancLI(-1)
    swiss_franc_li_one_other = SwissFrancLI(1)
    swiss_franc_li_one = SwissFrancLI(1)
    swiss_franc_li_two = SwissFrancLI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₣\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₣\xa03.14'),
        (10, '10', '₣\xa010.00'),
        (Decimal('10'), '10', '₣\xa010.00'),
        ('-3.14', '-3.14', '₣\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₣\xa0-3.14'),
        (-10, '-10', '₣\xa0-10.00'),
        (Decimal('-10'), '-10', '₣\xa0-10.00')
    ])
    def test_swiss_franc_li_default(amount, result, printed):
        default = SwissFrancLI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CHF'
        assert default.numeric_code == '756'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'LI₣'
        assert default.convertion == ''
        assert default.pattern == '2.\u00273%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert default.__repr__() == (
            'SwissFrancLI('
            f'amount: {result}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "LI₣", '
            'convertion: "", '
            'pattern: "2.\'3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_swiss_franc_li_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SwissFrancLI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CHF'
        assert custom.numeric_code == '756'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'LI₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert custom.__repr__() == (
            'SwissFrancLI('
            f'amount: {amount}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "LI₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_swiss_franc_li_recreate(amount, new_amount):
        default = SwissFrancLI(amount)
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
    def test_swiss_franc_li_change_attributes(attribute, value):
        immutable = SwissFrancLI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SwissFrancLI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_swiss_franc_li_add_attributes(attribute, value):
        immutable = SwissFrancLI(1000)
        with raises(
                AttributeError,
                match=f'\'SwissFrancLI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (swiss_franc_li_one, swiss_franc_li_one, swiss_franc_li_two, None),
        (swiss_franc_li_one, swiss_franc_li_one_other, swiss_franc_li_two, None),
        (swiss_franc_li_two, swiss_franc_li_minus_one, swiss_franc_li_one, None),
        (swiss_franc_li_one, other, None, CurrencyMismatchException),
        (swiss_franc_li_one, 1.00, None, CurrencyTypeException),
        (swiss_franc_li_one, '1.00', None, CurrencyTypeException)
    ])
    def test_swiss_franc_li_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (swiss_franc_li_one)
    ])
    def test_swiss_franc_li_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CHF'
        assert new.numeric_code == '756'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'LI₣'
        assert new.convertion == ''
        assert new.pattern == '2.\u00273%s\u00A0%a'


class TestSwissFrancCH:
    """Swiss Franc CH currency tests."""

    swiss_franc_ch_minus_one = SwissFrancCH(-1)
    swiss_franc_ch_one_other = SwissFrancCH(1)
    swiss_franc_ch_one = SwissFrancCH(1)
    swiss_franc_ch_two = SwissFrancCH(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₣\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₣\xa03.14'),
        (10, '10', '₣\xa010.00'),
        (Decimal('10'), '10', '₣\xa010.00'),
        ('-3.14', '-3.14', '₣\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₣\xa0-3.14'),
        (-10, '-10', '₣\xa0-10.00'),
        (Decimal('-10'), '-10', '₣\xa0-10.00')
    ])
    def test_swiss_franc_ch_default(amount, result, printed):
        default = SwissFrancCH(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CHF'
        assert default.numeric_code == '756'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CH₣'
        assert default.convertion == ''
        assert default.pattern == '2.\u00273%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert default.__repr__() == (
            'SwissFrancCH('
            f'amount: {result}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "CH₣", '
            'convertion: "", '
            'pattern: "2.\'3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_swiss_franc_ch_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SwissFrancCH(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CHF'
        assert custom.numeric_code == '756'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CH₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CHF',
            '756'))
        assert custom.__repr__() == (
            'SwissFrancCH('
            f'amount: {amount}, '
            'alpha_code: "CHF", '
            'numeric_code: "756", '
            'symbol: "₣", '
            'localized_symbol: "CH₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_swiss_franc_ch_recreate(amount, new_amount):
        default = SwissFrancCH(amount)
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
    def test_swiss_franc_ch_change_attributes(attribute, value):
        immutable = SwissFrancCH(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SwissFrancCH\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_swiss_franc_ch_add_attributes(attribute, value):
        immutable = SwissFrancCH(1000)
        with raises(
                AttributeError,
                match=f'\'SwissFrancCH\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (swiss_franc_ch_one, swiss_franc_ch_one, swiss_franc_ch_two, None),
        (swiss_franc_ch_one, swiss_franc_ch_one_other, swiss_franc_ch_two, None),
        (swiss_franc_ch_two, swiss_franc_ch_minus_one, swiss_franc_ch_one, None),
        (swiss_franc_ch_one, other, None, CurrencyMismatchException),
        (swiss_franc_ch_one, 1.00, None, CurrencyTypeException),
        (swiss_franc_ch_one, '1.00', None, CurrencyTypeException)
    ])
    def test_swiss_franc_ch_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (swiss_franc_ch_one)
    ])
    def test_swiss_franc_ch_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CHF'
        assert new.numeric_code == '756'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CH₣'
        assert new.convertion == ''
        assert new.pattern == '2.\u00273%s\u00A0%a'


class TestDjiboutiFranc:
    """Djibouti Franc currency tests."""

    djibouti_franc_minus_one = DjiboutiFranc(-1)
    djibouti_franc_one_other = DjiboutiFranc(1)
    djibouti_franc_one = DjiboutiFranc(1)
    djibouti_franc_two = DjiboutiFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_djibouti_franc_default(amount, result, printed):
        default = DjiboutiFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'DJF'
        assert default.numeric_code == '262'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'DJ₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'DJF',
            '262'))
        assert default.__repr__() == (
            'DjiboutiFranc('
            f'amount: {result}, '
            'alpha_code: "DJF", '
            'numeric_code: "262", '
            'symbol: "₣", '
            'localized_symbol: "DJ₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_djibouti_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = DjiboutiFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'DJF'
        assert custom.numeric_code == '262'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'DJ₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'DJF',
            '262'))
        assert custom.__repr__() == (
            'DjiboutiFranc('
            f'amount: {amount}, '
            'alpha_code: "DJF", '
            'numeric_code: "262", '
            'symbol: "₣", '
            'localized_symbol: "DJ₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_djibouti_franc_recreate(amount, new_amount):
        default = DjiboutiFranc(amount)
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
    def test_djibouti_franc_change_attributes(attribute, value):
        immutable = DjiboutiFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'DjiboutiFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_djibouti_franc_add_attributes(attribute, value):
        immutable = DjiboutiFranc(1000)
        with raises(
                AttributeError,
                match=f'\'DjiboutiFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (djibouti_franc_one, djibouti_franc_one, djibouti_franc_two, None),
        (djibouti_franc_one, djibouti_franc_one_other, djibouti_franc_two, None),
        (djibouti_franc_two, djibouti_franc_minus_one, djibouti_franc_one, None),
        (djibouti_franc_one, other, None, CurrencyMismatchException),
        (djibouti_franc_one, 1.00, None, CurrencyTypeException),
        (djibouti_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_djibouti_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (djibouti_franc_one)
    ])
    def test_djibouti_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'DJF'
        assert new.numeric_code == '262'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'DJ₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestGuineaFranc:
    """Guinea Franc currency tests."""

    guinea_franc_minus_one = GuineaFranc(-1)
    guinea_franc_one_other = GuineaFranc(1)
    guinea_franc_one = GuineaFranc(1)
    guinea_franc_two = GuineaFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_guinea_franc_default(amount, result, printed):
        default = GuineaFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GNF'
        assert default.numeric_code == '324'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'GN₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GNF',
            '324'))
        assert default.__repr__() == (
            'GuineaFranc('
            f'amount: {result}, '
            'alpha_code: "GNF", '
            'numeric_code: "324", '
            'symbol: "₣", '
            'localized_symbol: "GN₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_guinea_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = GuineaFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GNF'
        assert custom.numeric_code == '324'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'GN₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GNF',
            '324'))
        assert custom.__repr__() == (
            'GuineaFranc('
            f'amount: {amount}, '
            'alpha_code: "GNF", '
            'numeric_code: "324", '
            'symbol: "₣", '
            'localized_symbol: "GN₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_guinea_franc_recreate(amount, new_amount):
        default = GuineaFranc(amount)
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
    def test_guinea_franc_change_attributes(attribute, value):
        immutable = GuineaFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'GuineaFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_guinea_franc_add_attributes(attribute, value):
        immutable = GuineaFranc(1000)
        with raises(
                AttributeError,
                match=f'\'GuineaFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (guinea_franc_one, guinea_franc_one, guinea_franc_two, None),
        (guinea_franc_one, guinea_franc_one_other, guinea_franc_two, None),
        (guinea_franc_two, guinea_franc_minus_one, guinea_franc_one, None),
        (guinea_franc_one, other, None, CurrencyMismatchException),
        (guinea_franc_one, 1.00, None, CurrencyTypeException),
        (guinea_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_guinea_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (guinea_franc_one)
    ])
    def test_guinea_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GNF'
        assert new.numeric_code == '324'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'GN₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestRwandaFranc:
    """Rwanda Franc currency tests."""

    rwanda_franc_minus_one = RwandaFranc(-1)
    rwanda_franc_one_other = RwandaFranc(1)
    rwanda_franc_one = RwandaFranc(1)
    rwanda_franc_two = RwandaFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₣\xa03'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₣\xa03'),
        (10, '10', '₣\xa010'),
        (Decimal('10'), '10', '₣\xa010'),
        ('-3.14', '-3.14', '₣\xa0-3'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '₣\xa0-3'),
        (-10, '-10', '₣\xa0-10'),
        (Decimal('-10'), '-10', '₣\xa0-10')
    ])
    def test_rwanda_franc_default(amount, result, printed):
        default = RwandaFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'RWF'
        assert default.numeric_code == '646'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'RW₣'
        assert default.convertion == ''
        assert default.pattern == '0,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'RWF',
            '646'))
        assert default.__repr__() == (
            'RwandaFranc('
            f'amount: {result}, '
            'alpha_code: "RWF", '
            'numeric_code: "646", '
            'symbol: "₣", '
            'localized_symbol: "RW₣", '
            'convertion: "", '
            'pattern: "0,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_rwanda_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RwandaFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'RWF'
        assert custom.numeric_code == '646'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'RW₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'RWF',
            '646'))
        assert custom.__repr__() == (
            'RwandaFranc('
            f'amount: {amount}, '
            'alpha_code: "RWF", '
            'numeric_code: "646", '
            'symbol: "₣", '
            'localized_symbol: "RW₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rwanda_franc_recreate(amount, new_amount):
        default = RwandaFranc(amount)
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
    def test_rwanda_franc_change_attributes(attribute, value):
        immutable = RwandaFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RwandaFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rwanda_franc_add_attributes(attribute, value):
        immutable = RwandaFranc(1000)
        with raises(
                AttributeError,
                match=f'\'RwandaFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rwanda_franc_one, rwanda_franc_one, rwanda_franc_two, None),
        (rwanda_franc_one, rwanda_franc_one_other, rwanda_franc_two, None),
        (rwanda_franc_two, rwanda_franc_minus_one, rwanda_franc_one, None),
        (rwanda_franc_one, other, None, CurrencyMismatchException),
        (rwanda_franc_one, 1.00, None, CurrencyTypeException),
        (rwanda_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rwanda_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rwanda_franc_one)
    ])
    def test_rwanda_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'RWF'
        assert new.numeric_code == '646'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'RW₣'
        assert new.convertion == ''
        assert new.pattern == '0,.3%s\u00A0%a'


class TestCFAFrancBEAC:
    """CFA Franc BEAC currency tests."""

    cfa_franc_beac_minus_one = CFAFrancBEAC(-1)
    cfa_franc_beac_one_other = CFAFrancBEAC(1)
    cfa_franc_beac_one = CFAFrancBEAC(1)
    cfa_franc_beac_two = CFAFrancBEAC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_default(amount, result, printed):
        default = CFAFrancBEAC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == '₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEAC('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEAC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == '₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEAC('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_recreate(amount, new_amount):
        default = CFAFrancBEAC(amount)
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
    def test_cfa_franc_beac_change_attributes(attribute, value):
        immutable = CFAFrancBEAC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEAC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_add_attributes(attribute, value):
        immutable = CFAFrancBEAC(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEAC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_one, cfa_franc_beac_one, cfa_franc_beac_two, None),
        (cfa_franc_beac_one, cfa_franc_beac_one_other, cfa_franc_beac_two, None),
        (cfa_franc_beac_two, cfa_franc_beac_minus_one, cfa_franc_beac_one, None),
        (cfa_franc_beac_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_one)
    ])
    def test_cfa_franc_beac_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == '₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACCM:
    """CFA Franc BEAC CM currency tests."""

    cfa_franc_beac_cm_minus_one = CFAFrancBEACCM(-1)
    cfa_franc_beac_cm_one_other = CFAFrancBEACCM(1)
    cfa_franc_beac_cm_one = CFAFrancBEACCM(1)
    cfa_franc_beac_cm_two = CFAFrancBEACCM(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_cm_default(amount, result, printed):
        default = CFAFrancBEACCM(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CM₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACCM('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CM₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_cm_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACCM(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CM₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACCM('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CM₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_cm_recreate(amount, new_amount):
        default = CFAFrancBEACCM(amount)
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
    def test_cfa_franc_beac_cm_change_attributes(attribute, value):
        immutable = CFAFrancBEACCM(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACCM\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_cm_add_attributes(attribute, value):
        immutable = CFAFrancBEACCM(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACCM\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_cm_one, cfa_franc_beac_cm_one, cfa_franc_beac_cm_two, None),
        (cfa_franc_beac_cm_one, cfa_franc_beac_cm_one_other, cfa_franc_beac_cm_two, None),
        (cfa_franc_beac_cm_two, cfa_franc_beac_cm_minus_one, cfa_franc_beac_cm_one, None),
        (cfa_franc_beac_cm_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_cm_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_cm_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_cm_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_cm_one)
    ])
    def test_cfa_franc_beac_cm_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CM₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACCF:
    """CFA Franc BEAC CF currency tests."""

    cfa_franc_beac_cf_minus_one = CFAFrancBEACCF(-1)
    cfa_franc_beac_cf_one_other = CFAFrancBEACCF(1)
    cfa_franc_beac_cf_one = CFAFrancBEACCF(1)
    cfa_franc_beac_cf_two = CFAFrancBEACCF(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_cf_default(amount, result, printed):
        default = CFAFrancBEACCF(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CF₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACCF('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CF₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_cf_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACCF(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CF₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACCF('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CF₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_cf_recreate(amount, new_amount):
        default = CFAFrancBEACCF(amount)
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
    def test_cfa_franc_beac_cf_change_attributes(attribute, value):
        immutable = CFAFrancBEACCF(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACCF\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_cf_add_attributes(attribute, value):
        immutable = CFAFrancBEACCF(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACCF\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_cf_one, cfa_franc_beac_cf_one, cfa_franc_beac_cf_two, None),
        (cfa_franc_beac_cf_one, cfa_franc_beac_cf_one_other, cfa_franc_beac_cf_two, None),
        (cfa_franc_beac_cf_two, cfa_franc_beac_cf_minus_one, cfa_franc_beac_cf_one, None),
        (cfa_franc_beac_cf_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_cf_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_cf_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_cf_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_cf_one)
    ])
    def test_cfa_franc_beac_cf_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CF₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACTD:
    """CFA Franc BEAC TD currency tests."""

    cfa_franc_beac_td_minus_one = CFAFrancBEACTD(-1)
    cfa_franc_beac_td_one_other = CFAFrancBEACTD(1)
    cfa_franc_beac_td_one = CFAFrancBEACTD(1)
    cfa_franc_beac_td_two = CFAFrancBEACTD(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_td_default(amount, result, printed):
        default = CFAFrancBEACTD(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'TD₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACTD('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "TD₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_td_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACTD(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'TD₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACTD('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "TD₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_td_recreate(amount, new_amount):
        default = CFAFrancBEACTD(amount)
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
    def test_cfa_franc_beac_td_change_attributes(attribute, value):
        immutable = CFAFrancBEACTD(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACTD\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_td_add_attributes(attribute, value):
        immutable = CFAFrancBEACTD(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACTD\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_td_one, cfa_franc_beac_td_one, cfa_franc_beac_td_two, None),
        (cfa_franc_beac_td_one, cfa_franc_beac_td_one_other, cfa_franc_beac_td_two, None),
        (cfa_franc_beac_td_two, cfa_franc_beac_td_minus_one, cfa_franc_beac_td_one, None),
        (cfa_franc_beac_td_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_td_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_td_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_td_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_td_one)
    ])
    def test_cfa_franc_beac_td_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'TD₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACCD:
    """CFA Franc BEAC CD currency tests."""

    cfa_franc_beac_cd_minus_one = CFAFrancBEACCD(-1)
    cfa_franc_beac_cd_one_other = CFAFrancBEACCD(1)
    cfa_franc_beac_cd_one = CFAFrancBEACCD(1)
    cfa_franc_beac_cd_two = CFAFrancBEACCD(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_cd_default(amount, result, printed):
        default = CFAFrancBEACCD(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CD₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACCD('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CD₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_cd_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACCD(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CD₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACCD('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "CD₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_cd_recreate(amount, new_amount):
        default = CFAFrancBEACCD(amount)
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
    def test_cfa_franc_beac_cd_change_attributes(attribute, value):
        immutable = CFAFrancBEACCD(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACCD\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_cd_add_attributes(attribute, value):
        immutable = CFAFrancBEACCD(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACCD\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_cd_one, cfa_franc_beac_cd_one, cfa_franc_beac_cd_two, None),
        (cfa_franc_beac_cd_one, cfa_franc_beac_cd_one_other, cfa_franc_beac_cd_two, None),
        (cfa_franc_beac_cd_two, cfa_franc_beac_cd_minus_one, cfa_franc_beac_cd_one, None),
        (cfa_franc_beac_cd_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_cd_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_cd_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_cd_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_cd_one)
    ])
    def test_cfa_franc_beac_cd_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CD₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACGQ:
    """CFA Franc BEAC GQ currency tests."""

    cfa_franc_beac_gq_minus_one = CFAFrancBEACGQ(-1)
    cfa_franc_beac_gq_one_other = CFAFrancBEACGQ(1)
    cfa_franc_beac_gq_one = CFAFrancBEACGQ(1)
    cfa_franc_beac_gq_two = CFAFrancBEACGQ(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_gq_default(amount, result, printed):
        default = CFAFrancBEACGQ(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'GQ₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACGQ('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "GQ₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_gq_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACGQ(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'GQ₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACGQ('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "GQ₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_gq_recreate(amount, new_amount):
        default = CFAFrancBEACGQ(amount)
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
    def test_cfa_franc_beac_gq_change_attributes(attribute, value):
        immutable = CFAFrancBEACGQ(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACGQ\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_gq_add_attributes(attribute, value):
        immutable = CFAFrancBEACGQ(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACGQ\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_gq_one, cfa_franc_beac_gq_one, cfa_franc_beac_gq_two, None),
        (cfa_franc_beac_gq_one, cfa_franc_beac_gq_one_other, cfa_franc_beac_gq_two, None),
        (cfa_franc_beac_gq_two, cfa_franc_beac_gq_minus_one, cfa_franc_beac_gq_one, None),
        (cfa_franc_beac_gq_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_gq_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_gq_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_gq_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_gq_one)
    ])
    def test_cfa_franc_beac_gq_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'GQ₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBEACGA:
    """CFA Franc BEAC GA currency tests."""

    cfa_franc_beac_ga_minus_one = CFAFrancBEACGA(-1)
    cfa_franc_beac_ga_one_other = CFAFrancBEACGA(1)
    cfa_franc_beac_ga_one = CFAFrancBEACGA(1)
    cfa_franc_beac_ga_two = CFAFrancBEACGA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_beac_ga_default(amount, result, printed):
        default = CFAFrancBEACGA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XAF'
        assert default.numeric_code == '950'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'GA₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert default.__repr__() == (
            'CFAFrancBEACGA('
            f'amount: {result}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "GA₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_beac_ga_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBEACGA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XAF'
        assert custom.numeric_code == '950'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'GA₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XAF',
            '950'))
        assert custom.__repr__() == (
            'CFAFrancBEACGA('
            f'amount: {amount}, '
            'alpha_code: "XAF", '
            'numeric_code: "950", '
            'symbol: "₣", '
            'localized_symbol: "GA₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_beac_ga_recreate(amount, new_amount):
        default = CFAFrancBEACGA(amount)
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
    def test_cfa_franc_beac_ga_change_attributes(attribute, value):
        immutable = CFAFrancBEACGA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBEACGA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_beac_ga_add_attributes(attribute, value):
        immutable = CFAFrancBEACGA(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBEACGA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_beac_ga_one, cfa_franc_beac_ga_one, cfa_franc_beac_ga_two, None),
        (cfa_franc_beac_ga_one, cfa_franc_beac_ga_one_other, cfa_franc_beac_ga_two, None),
        (cfa_franc_beac_ga_two, cfa_franc_beac_ga_minus_one, cfa_franc_beac_ga_one, None),
        (cfa_franc_beac_ga_one, other, None, CurrencyMismatchException),
        (cfa_franc_beac_ga_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_beac_ga_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_beac_ga_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_beac_ga_one)
    ])
    def test_cfa_franc_beac_ga_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XAF'
        assert new.numeric_code == '950'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'GA₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAO:
    """CFA Franc BCEAO currency tests."""

    cfa_franc_bceao_minus_one = CFAFrancBCEAO(-1)
    cfa_franc_bceao_one_other = CFAFrancBCEAO(1)
    cfa_franc_bceao_one = CFAFrancBCEAO(1)
    cfa_franc_bceao_two = CFAFrancBCEAO(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_default(amount, result, printed):
        default = CFAFrancBCEAO(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == '₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAO('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAO(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == '₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAO('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_recreate(amount, new_amount):
        default = CFAFrancBCEAO(amount)
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
    def test_cfa_franc_bceao_change_attributes(attribute, value):
        immutable = CFAFrancBCEAO(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAO\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_add_attributes(attribute, value):
        immutable = CFAFrancBCEAO(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAO\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_one, cfa_franc_bceao_one, cfa_franc_bceao_two, None),
        (cfa_franc_bceao_one, cfa_franc_bceao_one_other, cfa_franc_bceao_two, None),
        (cfa_franc_bceao_two, cfa_franc_bceao_minus_one, cfa_franc_bceao_one, None),
        (cfa_franc_bceao_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_one)
    ])
    def test_cfa_franc_bceao_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == '₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOBJ:
    """CFA Franc BCEAO BJ currency tests."""

    cfa_franc_bceao_bj_minus_one = CFAFrancBCEAOBJ(-1)
    cfa_franc_bceao_bj_one_other = CFAFrancBCEAOBJ(1)
    cfa_franc_bceao_bj_one = CFAFrancBCEAOBJ(1)
    cfa_franc_bceao_bj_two = CFAFrancBCEAOBJ(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_bj_default(amount, result, printed):
        default = CFAFrancBCEAOBJ(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'BJ₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOBJ('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "BJ₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_bj_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOBJ(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'BJ₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOBJ('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "BJ₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_bj_recreate(amount, new_amount):
        default = CFAFrancBCEAOBJ(amount)
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
    def test_cfa_franc_bceao_bj_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOBJ(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOBJ\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_bj_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOBJ(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOBJ\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_bj_one, cfa_franc_bceao_bj_one, cfa_franc_bceao_bj_two, None),
        (cfa_franc_bceao_bj_one, cfa_franc_bceao_bj_one_other, cfa_franc_bceao_bj_two, None),
        (cfa_franc_bceao_bj_two, cfa_franc_bceao_bj_minus_one, cfa_franc_bceao_bj_one, None),
        (cfa_franc_bceao_bj_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_bj_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_bj_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_bj_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_bj_one)
    ])
    def test_cfa_franc_bceao_bj_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'BJ₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOBF:
    """CFA Franc BCEAO BF currency tests."""

    cfa_franc_bceao_bf_minus_one = CFAFrancBCEAOBF(-1)
    cfa_franc_bceao_bf_one_other = CFAFrancBCEAOBF(1)
    cfa_franc_bceao_bf_one = CFAFrancBCEAOBF(1)
    cfa_franc_bceao_bf_two = CFAFrancBCEAOBF(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_bf_default(amount, result, printed):
        default = CFAFrancBCEAOBF(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'BF₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOBF('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "BF₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_bf_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOBF(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'BF₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOBF('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "BF₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_bf_recreate(amount, new_amount):
        default = CFAFrancBCEAOBF(amount)
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
    def test_cfa_franc_bceao_bf_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOBF(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOBF\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_bf_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOBF(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOBF\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_bf_one, cfa_franc_bceao_bf_one, cfa_franc_bceao_bf_two, None),
        (cfa_franc_bceao_bf_one, cfa_franc_bceao_bf_one_other, cfa_franc_bceao_bf_two, None),
        (cfa_franc_bceao_bf_two, cfa_franc_bceao_bf_minus_one, cfa_franc_bceao_bf_one, None),
        (cfa_franc_bceao_bf_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_bf_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_bf_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_bf_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_bf_one)
    ])
    def test_cfa_franc_bceao_bf_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'BF₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOCI:
    """CFA Franc BCEAO CI currency tests."""

    cfa_franc_bceao_ci_minus_one = CFAFrancBCEAOCI(-1)
    cfa_franc_bceao_ci_one_other = CFAFrancBCEAOCI(1)
    cfa_franc_bceao_ci_one = CFAFrancBCEAOCI(1)
    cfa_franc_bceao_ci_two = CFAFrancBCEAOCI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_ci_default(amount, result, printed):
        default = CFAFrancBCEAOCI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'CI₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOCI('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "CI₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_ci_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOCI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'CI₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOCI('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "CI₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_ci_recreate(amount, new_amount):
        default = CFAFrancBCEAOCI(amount)
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
    def test_cfa_franc_bceao_ci_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOCI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOCI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_ci_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOCI(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOCI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_ci_one, cfa_franc_bceao_ci_one, cfa_franc_bceao_ci_two, None),
        (cfa_franc_bceao_ci_one, cfa_franc_bceao_ci_one_other, cfa_franc_bceao_ci_two, None),
        (cfa_franc_bceao_ci_two, cfa_franc_bceao_ci_minus_one, cfa_franc_bceao_ci_one, None),
        (cfa_franc_bceao_ci_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_ci_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_ci_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_ci_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_ci_one)
    ])
    def test_cfa_franc_bceao_ci_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'CI₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOGW:
    """CFA Franc BCEAO GW currency tests."""

    cfa_franc_bceao_gw_minus_one = CFAFrancBCEAOGW(-1)
    cfa_franc_bceao_gw_one_other = CFAFrancBCEAOGW(1)
    cfa_franc_bceao_gw_one = CFAFrancBCEAOGW(1)
    cfa_franc_bceao_gw_two = CFAFrancBCEAOGW(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_gw_default(amount, result, printed):
        default = CFAFrancBCEAOGW(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'GW₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOGW('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "GW₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_gw_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOGW(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'GW₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOGW('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "GW₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_gw_recreate(amount, new_amount):
        default = CFAFrancBCEAOGW(amount)
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
    def test_cfa_franc_bceao_gw_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOGW(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOGW\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_gw_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOGW(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOGW\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_gw_one, cfa_franc_bceao_gw_one, cfa_franc_bceao_gw_two, None),
        (cfa_franc_bceao_gw_one, cfa_franc_bceao_gw_one_other, cfa_franc_bceao_gw_two, None),
        (cfa_franc_bceao_gw_two, cfa_franc_bceao_gw_minus_one, cfa_franc_bceao_gw_one, None),
        (cfa_franc_bceao_gw_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_gw_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_gw_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_gw_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_gw_one)
    ])
    def test_cfa_franc_bceao_gw_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'GW₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOML:
    """CFA Franc BCEAO ML currency tests."""

    cfa_franc_bceao_ml_minus_one = CFAFrancBCEAOML(-1)
    cfa_franc_bceao_ml_one_other = CFAFrancBCEAOML(1)
    cfa_franc_bceao_ml_one = CFAFrancBCEAOML(1)
    cfa_franc_bceao_ml_two = CFAFrancBCEAOML(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_ml_default(amount, result, printed):
        default = CFAFrancBCEAOML(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'ML₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOML('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "ML₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_ml_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOML(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'ML₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOML('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "ML₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_ml_recreate(amount, new_amount):
        default = CFAFrancBCEAOML(amount)
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
    def test_cfa_franc_bceao_ml_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOML(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOML\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_ml_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOML(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOML\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_ml_one, cfa_franc_bceao_ml_one, cfa_franc_bceao_ml_two, None),
        (cfa_franc_bceao_ml_one, cfa_franc_bceao_ml_one_other, cfa_franc_bceao_ml_two, None),
        (cfa_franc_bceao_ml_two, cfa_franc_bceao_ml_minus_one, cfa_franc_bceao_ml_one, None),
        (cfa_franc_bceao_ml_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_ml_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_ml_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_ml_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_ml_one)
    ])
    def test_cfa_franc_bceao_ml_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'ML₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAONG:
    """CFA Franc BCEAO NG currency tests."""

    cfa_franc_bceao_ng_minus_one = CFAFrancBCEAONG(-1)
    cfa_franc_bceao_ng_one_other = CFAFrancBCEAONG(1)
    cfa_franc_bceao_ng_one = CFAFrancBCEAONG(1)
    cfa_franc_bceao_ng_two = CFAFrancBCEAONG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_ng_default(amount, result, printed):
        default = CFAFrancBCEAONG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'NG₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAONG('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "NG₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_ng_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAONG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'NG₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAONG('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "NG₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_ng_recreate(amount, new_amount):
        default = CFAFrancBCEAONG(amount)
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
    def test_cfa_franc_bceao_ng_change_attributes(attribute, value):
        immutable = CFAFrancBCEAONG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAONG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_ng_add_attributes(attribute, value):
        immutable = CFAFrancBCEAONG(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAONG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_ng_one, cfa_franc_bceao_ng_one, cfa_franc_bceao_ng_two, None),
        (cfa_franc_bceao_ng_one, cfa_franc_bceao_ng_one_other, cfa_franc_bceao_ng_two, None),
        (cfa_franc_bceao_ng_two, cfa_franc_bceao_ng_minus_one, cfa_franc_bceao_ng_one, None),
        (cfa_franc_bceao_ng_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_ng_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_ng_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_ng_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_ng_one)
    ])
    def test_cfa_franc_bceao_ng_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'NG₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOSN:
    """CFA Franc BCEAO SN currency tests."""

    cfa_franc_bceao_sn_minus_one = CFAFrancBCEAOSN(-1)
    cfa_franc_bceao_sn_one_other = CFAFrancBCEAOSN(1)
    cfa_franc_bceao_sn_one = CFAFrancBCEAOSN(1)
    cfa_franc_bceao_sn_two = CFAFrancBCEAOSN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_sn_default(amount, result, printed):
        default = CFAFrancBCEAOSN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'SN₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOSN('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "SN₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_sn_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOSN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'SN₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOSN('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "SN₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_sn_recreate(amount, new_amount):
        default = CFAFrancBCEAOSN(amount)
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
    def test_cfa_franc_bceao_sn_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOSN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOSN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_sn_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOSN(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOSN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_sn_one, cfa_franc_bceao_sn_one, cfa_franc_bceao_sn_two, None),
        (cfa_franc_bceao_sn_one, cfa_franc_bceao_sn_one_other, cfa_franc_bceao_sn_two, None),
        (cfa_franc_bceao_sn_two, cfa_franc_bceao_sn_minus_one, cfa_franc_bceao_sn_one, None),
        (cfa_franc_bceao_sn_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_sn_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_sn_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_sn_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_sn_one)
    ])
    def test_cfa_franc_bceao_sn_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'SN₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFAFrancBCEAOTG:
    """CFA Franc BCEAO TG currency tests."""

    cfa_franc_bceao_tg_minus_one = CFAFrancBCEAOTG(-1)
    cfa_franc_bceao_tg_one_other = CFAFrancBCEAOTG(1)
    cfa_franc_bceao_tg_one = CFAFrancBCEAOTG(1)
    cfa_franc_bceao_tg_two = CFAFrancBCEAOTG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfa_franc_bceao_tg_default(amount, result, printed):
        default = CFAFrancBCEAOTG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XOF'
        assert default.numeric_code == '952'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'TG₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert default.__repr__() == (
            'CFAFrancBCEAOTG('
            f'amount: {result}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "TG₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfa_franc_bceao_tg_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFAFrancBCEAOTG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XOF'
        assert custom.numeric_code == '952'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'TG₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XOF',
            '952'))
        assert custom.__repr__() == (
            'CFAFrancBCEAOTG('
            f'amount: {amount}, '
            'alpha_code: "XOF", '
            'numeric_code: "952", '
            'symbol: "₣", '
            'localized_symbol: "TG₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfa_franc_bceao_tg_recreate(amount, new_amount):
        default = CFAFrancBCEAOTG(amount)
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
    def test_cfa_franc_bceao_tg_change_attributes(attribute, value):
        immutable = CFAFrancBCEAOTG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFAFrancBCEAOTG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfa_franc_bceao_tg_add_attributes(attribute, value):
        immutable = CFAFrancBCEAOTG(1000)
        with raises(
                AttributeError,
                match=f'\'CFAFrancBCEAOTG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfa_franc_bceao_tg_one, cfa_franc_bceao_tg_one, cfa_franc_bceao_tg_two, None),
        (cfa_franc_bceao_tg_one, cfa_franc_bceao_tg_one_other, cfa_franc_bceao_tg_two, None),
        (cfa_franc_bceao_tg_two, cfa_franc_bceao_tg_minus_one, cfa_franc_bceao_tg_one, None),
        (cfa_franc_bceao_tg_one, other, None, CurrencyMismatchException),
        (cfa_franc_bceao_tg_one, 1.00, None, CurrencyTypeException),
        (cfa_franc_bceao_tg_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfa_franc_bceao_tg_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfa_franc_bceao_tg_one)
    ])
    def test_cfa_franc_bceao_tg_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XOF'
        assert new.numeric_code == '952'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'TG₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFPFranc:
    """CFP Franc currency tests."""

    cfp_franc_minus_one = CFPFranc(-1)
    cfp_franc_one_other = CFPFranc(1)
    cfp_franc_one = CFPFranc(1)
    cfp_franc_two = CFPFranc(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfp_franc_default(amount, result, printed):
        default = CFPFranc(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XPF'
        assert default.numeric_code == '953'
        assert default.symbol == '₣'
        assert default.localized_symbol == '₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert default.__repr__() == (
            'CFPFranc('
            f'amount: {result}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfp_franc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFPFranc(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XPF'
        assert custom.numeric_code == '953'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == '₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert custom.__repr__() == (
            'CFPFranc('
            f'amount: {amount}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfp_franc_recreate(amount, new_amount):
        default = CFPFranc(amount)
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
    def test_cfp_franc_change_attributes(attribute, value):
        immutable = CFPFranc(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFPFranc\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfp_franc_add_attributes(attribute, value):
        immutable = CFPFranc(1000)
        with raises(
                AttributeError,
                match=f'\'CFPFranc\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfp_franc_one, cfp_franc_one, cfp_franc_two, None),
        (cfp_franc_one, cfp_franc_one_other, cfp_franc_two, None),
        (cfp_franc_two, cfp_franc_minus_one, cfp_franc_one, None),
        (cfp_franc_one, other, None, CurrencyMismatchException),
        (cfp_franc_one, 1.00, None, CurrencyTypeException),
        (cfp_franc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfp_franc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfp_franc_one)
    ])
    def test_cfp_franc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XPF'
        assert new.numeric_code == '953'
        assert new.symbol == '₣'
        assert new.localized_symbol == '₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFPFrancPF:
    """CFP Franc PF currency tests."""

    cfp_franc_pf_minus_one = CFPFrancPF(-1)
    cfp_franc_pf_one_other = CFPFrancPF(1)
    cfp_franc_pf_one = CFPFrancPF(1)
    cfp_franc_pf_two = CFPFrancPF(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfp_franc_pf_default(amount, result, printed):
        default = CFPFrancPF(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XPF'
        assert default.numeric_code == '953'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'PF₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert default.__repr__() == (
            'CFPFrancPF('
            f'amount: {result}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "PF₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfp_franc_pf_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFPFrancPF(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XPF'
        assert custom.numeric_code == '953'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'PF₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert custom.__repr__() == (
            'CFPFrancPF('
            f'amount: {amount}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "PF₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfp_franc_pf_recreate(amount, new_amount):
        default = CFPFrancPF(amount)
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
    def test_cfp_franc_pf_change_attributes(attribute, value):
        immutable = CFPFrancPF(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFPFrancPF\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfp_franc_pf_add_attributes(attribute, value):
        immutable = CFPFrancPF(1000)
        with raises(
                AttributeError,
                match=f'\'CFPFrancPF\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfp_franc_pf_one, cfp_franc_pf_one, cfp_franc_pf_two, None),
        (cfp_franc_pf_one, cfp_franc_pf_one_other, cfp_franc_pf_two, None),
        (cfp_franc_pf_two, cfp_franc_pf_minus_one, cfp_franc_pf_one, None),
        (cfp_franc_pf_one, other, None, CurrencyMismatchException),
        (cfp_franc_pf_one, 1.00, None, CurrencyTypeException),
        (cfp_franc_pf_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfp_franc_pf_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfp_franc_pf_one)
    ])
    def test_cfp_franc_pf_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XPF'
        assert new.numeric_code == '953'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'PF₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFPFrancNC:
    """CFP Franc NC currency tests."""

    cfp_franc_nc_minus_one = CFPFrancNC(-1)
    cfp_franc_nc_one_other = CFPFrancNC(1)
    cfp_franc_nc_one = CFPFrancNC(1)
    cfp_franc_nc_two = CFPFrancNC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfp_franc_nc_default(amount, result, printed):
        default = CFPFrancNC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XPF'
        assert default.numeric_code == '953'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'NC₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert default.__repr__() == (
            'CFPFrancNC('
            f'amount: {result}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "NC₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfp_franc_nc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFPFrancNC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XPF'
        assert custom.numeric_code == '953'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'NC₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert custom.__repr__() == (
            'CFPFrancNC('
            f'amount: {amount}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "NC₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfp_franc_nc_recreate(amount, new_amount):
        default = CFPFrancNC(amount)
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
    def test_cfp_franc_nc_change_attributes(attribute, value):
        immutable = CFPFrancNC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFPFrancNC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfp_franc_nc_add_attributes(attribute, value):
        immutable = CFPFrancNC(1000)
        with raises(
                AttributeError,
                match=f'\'CFPFrancNC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfp_franc_nc_one, cfp_franc_nc_one, cfp_franc_nc_two, None),
        (cfp_franc_nc_one, cfp_franc_nc_one_other, cfp_franc_nc_two, None),
        (cfp_franc_nc_two, cfp_franc_nc_minus_one, cfp_franc_nc_one, None),
        (cfp_franc_nc_one, other, None, CurrencyMismatchException),
        (cfp_franc_nc_one, 1.00, None, CurrencyTypeException),
        (cfp_franc_nc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfp_franc_nc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfp_franc_nc_one)
    ])
    def test_cfp_franc_nc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XPF'
        assert new.numeric_code == '953'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'NC₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'


class TestCFPFrancWF:
    """CFP Franc WF currency tests."""

    cfp_franc_wf_minus_one = CFPFrancWF(-1)
    cfp_franc_wf_one_other = CFPFrancWF(1)
    cfp_franc_wf_one = CFPFrancWF(1)
    cfp_franc_wf_two = CFPFrancWF(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3\xa0₣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3\xa0₣'),
        (10, '10', '10\xa0₣'),
        (Decimal('10'), '10', '10\xa0₣'),
        ('-3.14', '-3.14', '-3\xa0₣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3\xa0₣'),
        (-10, '-10', '-10\xa0₣'),
        (Decimal('-10'), '-10', '-10\xa0₣')
    ])
    def test_cfp_franc_wf_default(amount, result, printed):
        default = CFPFrancWF(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XPF'
        assert default.numeric_code == '953'
        assert default.symbol == '₣'
        assert default.localized_symbol == 'WF₣'
        assert default.convertion == ''
        assert default.pattern == '0,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert default.__repr__() == (
            'CFPFrancWF('
            f'amount: {result}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "WF₣", '
            'convertion: "", '
            'pattern: "0, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₣10.00,00000'),
        (-1000, '₣10.00,00000-')
    ])
    def test_cfp_franc_wf_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CFPFrancWF(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XPF'
        assert custom.numeric_code == '953'
        assert custom.symbol == '₣'
        assert custom.localized_symbol == 'WF₣'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XPF',
            '953'))
        assert custom.__repr__() == (
            'CFPFrancWF('
            f'amount: {amount}, '
            'alpha_code: "XPF", '
            'numeric_code: "953", '
            'symbol: "₣", '
            'localized_symbol: "WF₣", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cfp_franc_wf_recreate(amount, new_amount):
        default = CFPFrancWF(amount)
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
    def test_cfp_franc_wf_change_attributes(attribute, value):
        immutable = CFPFrancWF(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CFPFrancWF\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cfp_franc_wf_add_attributes(attribute, value):
        immutable = CFPFrancWF(1000)
        with raises(
                AttributeError,
                match=f'\'CFPFrancWF\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cfp_franc_wf_one, cfp_franc_wf_one, cfp_franc_wf_two, None),
        (cfp_franc_wf_one, cfp_franc_wf_one_other, cfp_franc_wf_two, None),
        (cfp_franc_wf_two, cfp_franc_wf_minus_one, cfp_franc_wf_one, None),
        (cfp_franc_wf_one, other, None, CurrencyMismatchException),
        (cfp_franc_wf_one, 1.00, None, CurrencyTypeException),
        (cfp_franc_wf_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cfp_franc_wf_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cfp_franc_wf_one)
    ])
    def test_cfp_franc_wf_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XPF'
        assert new.numeric_code == '953'
        assert new.symbol == '₣'
        assert new.localized_symbol == 'WF₣'
        assert new.convertion == ''
        assert new.pattern == '0,\u202F3%a\u00A0%s'
