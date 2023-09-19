# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Dollar currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.dollar import (
    AustralianDollar,
    AustralianDollarAU,
    AustralianDollarKI,
    AustralianDollarCC,
    AustralianDollarMR,
    AustralianDollarTV,
    BarbadosDollar,
    BermudianDollar,
    BruneiDollar,
    BruneiDollarBN,
    BruneiDollarSG,
    BahamianDollar,
    BelizeDollar,
    CanadianDollarEN,
    CanadianDollarFR,
    FijiDollar,
    GuyanaDollar,
    HongKongDollar,
    JamaicanDollar,
    CaymanIslandsDollar,
    LiberianDollar,
    NamibiaDollar,
    NewZealandDollar,
    NewZealandDollarCK,
    NewZealandDollarNZ,
    NewZealandDollarNU,
    NewZealandDollarPN,
    SolomonIslandsDollar,
    SingaporeDollar,
    SingaporeDollarBN,
    SingaporeDollarSG,
    SurinameDollar,
    TrinidadandTobagoDollar,
    TaiwanDollar,
    USDollar,
    USDollarAS,
    USDollarIO,
    USDollarVG,
    USDollarGU,
    USDollarHT,
    USDollarMH,
    USDollarFM,
    USDollarMP,
    USDollarPC,
    USDollarPW,
    USDollarPA,
    USDollarPR,
    USDollarTC,
    USDollarVI,
    EasternCaribbeanDollar,
    EasternCaribbeanDollarAI,
    EasternCaribbeanDollarAG,
    EasternCaribbeanDollarDM,
    EasternCaribbeanDollarGD,
    EasternCaribbeanDollarMS,
    EasternCaribbeanDollarKN,
    EasternCaribbeanDollarLC,
    EasternCaribbeanDollarVC,
    ZimbabweDollar)


class TestAustralianDollar:
    """Australian Dollar currency tests."""

    australian_dollar_minus_one = AustralianDollar(-1)
    australian_dollar_one_other = AustralianDollar(1)
    australian_dollar_one = AustralianDollar(1)
    australian_dollar_two = AustralianDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03.14'),
        (10, '10', '$\xa010.00'),
        (Decimal('10'), '10', '$\xa010.00'),
        ('-3.14', '-3.14', '$\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3.14'),
        (-10, '-10', '$\xa0-10.00'),
        (Decimal('-10'), '-10', '$\xa0-10.00')
    ])
    def test_australian_dollar_default(amount, result, printed):
        default = AustralianDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == '$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollar('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == '$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollar('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_recreate(amount, new_amount):
        default = AustralianDollar(amount)
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
    def test_australian_dollar_change_attributes(attribute, value):
        immutable = AustralianDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_add_attributes(attribute, value):
        immutable = AustralianDollar(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_one, australian_dollar_one, australian_dollar_two, None),
        (australian_dollar_one, australian_dollar_one_other, australian_dollar_two, None),
        (australian_dollar_two, australian_dollar_minus_one, australian_dollar_one, None),
        (australian_dollar_one, other, None, CurrencyMismatchException),
        (australian_dollar_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_one)
    ])
    def test_australian_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == '$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'


class TestAustralianDollarAU:
    """Australian Dollar AU currency tests."""

    australian_dollar_au_minus_one = AustralianDollarAU(-1)
    australian_dollar_au_one_other = AustralianDollarAU(1)
    australian_dollar_au_one = AustralianDollarAU(1)
    australian_dollar_au_two = AustralianDollarAU(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_australian_dollar_au_default(amount, result, printed):
        default = AustralianDollarAU(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == 'AU$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollarAU('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "AU$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_au_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollarAU(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'AU$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollarAU('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "AU$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_au_recreate(amount, new_amount):
        default = AustralianDollarAU(amount)
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
    def test_australian_dollar_au_change_attributes(attribute, value):
        immutable = AustralianDollarAU(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollarAU\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_au_add_attributes(attribute, value):
        immutable = AustralianDollarAU(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollarAU\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_au_one, australian_dollar_au_one, australian_dollar_au_two, None),
        (australian_dollar_au_one, australian_dollar_au_one_other, australian_dollar_au_two, None),
        (australian_dollar_au_two, australian_dollar_au_minus_one, australian_dollar_au_one, None),
        (australian_dollar_au_one, other, None, CurrencyMismatchException),
        (australian_dollar_au_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_au_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_au_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_au_one)
    ])
    def test_australian_dollar_au_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == 'AU$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestAustralianDollarKI:
    """Australian Dollar KI currency tests."""

    australian_dollar_ki_minus_one = AustralianDollarKI(-1)
    australian_dollar_ki_one_other = AustralianDollarKI(1)
    australian_dollar_ki_one = AustralianDollarKI(1)
    australian_dollar_ki_two = AustralianDollarKI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_australian_dollar_ki_default(amount, result, printed):
        default = AustralianDollarKI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == 'KI$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollarKI('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "KI$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_ki_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollarKI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'KI$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollarKI('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "KI$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_ki_recreate(amount, new_amount):
        default = AustralianDollarKI(amount)
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
    def test_australian_dollar_ki_change_attributes(attribute, value):
        immutable = AustralianDollarKI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollarKI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_ki_add_attributes(attribute, value):
        immutable = AustralianDollarKI(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollarKI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_ki_one, australian_dollar_ki_one, australian_dollar_ki_two, None),
        (australian_dollar_ki_one, australian_dollar_ki_one_other, australian_dollar_ki_two, None),
        (australian_dollar_ki_two, australian_dollar_ki_minus_one, australian_dollar_ki_one, None),
        (australian_dollar_ki_one, other, None, CurrencyMismatchException),
        (australian_dollar_ki_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_ki_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_ki_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_ki_one)
    ])
    def test_australian_dollar_ki_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == 'KI$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestAustralianDollarCC:
    """Australian Dollar CC currency tests."""

    australian_dollar_cc_minus_one = AustralianDollarCC(-1)
    australian_dollar_cc_one_other = AustralianDollarCC(1)
    australian_dollar_cc_one = AustralianDollarCC(1)
    australian_dollar_cc_two = AustralianDollarCC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_australian_dollar_cc_default(amount, result, printed):
        default = AustralianDollarCC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CC$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollarCC('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "CC$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_cc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollarCC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CC$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollarCC('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "CC$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_cc_recreate(amount, new_amount):
        default = AustralianDollarCC(amount)
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
    def test_australian_dollar_cc_change_attributes(attribute, value):
        immutable = AustralianDollarCC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollarCC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_cc_add_attributes(attribute, value):
        immutable = AustralianDollarCC(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollarCC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_cc_one, australian_dollar_cc_one, australian_dollar_cc_two, None),
        (australian_dollar_cc_one, australian_dollar_cc_one_other, australian_dollar_cc_two, None),
        (australian_dollar_cc_two, australian_dollar_cc_minus_one, australian_dollar_cc_one, None),
        (australian_dollar_cc_one, other, None, CurrencyMismatchException),
        (australian_dollar_cc_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_cc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_cc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_cc_one)
    ])
    def test_australian_dollar_cc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CC$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestAustralianDollarMR:
    """Australian Dollar MR currency tests."""

    australian_dollar_mr_minus_one = AustralianDollarMR(-1)
    australian_dollar_mr_one_other = AustralianDollarMR(1)
    australian_dollar_mr_one = AustralianDollarMR(1)
    australian_dollar_mr_two = AustralianDollarMR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_australian_dollar_mr_default(amount, result, printed):
        default = AustralianDollarMR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == 'NR$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollarMR('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "NR$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_mr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollarMR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'NR$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollarMR('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "NR$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_mr_recreate(amount, new_amount):
        default = AustralianDollarMR(amount)
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
    def test_australian_dollar_mr_change_attributes(attribute, value):
        immutable = AustralianDollarMR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollarMR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_mr_add_attributes(attribute, value):
        immutable = AustralianDollarMR(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollarMR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_mr_one, australian_dollar_mr_one, australian_dollar_mr_two, None),
        (australian_dollar_mr_one, australian_dollar_mr_one_other, australian_dollar_mr_two, None),
        (australian_dollar_mr_two, australian_dollar_mr_minus_one, australian_dollar_mr_one, None),
        (australian_dollar_mr_one, other, None, CurrencyMismatchException),
        (australian_dollar_mr_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_mr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_mr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_mr_one)
    ])
    def test_australian_dollar_mr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == 'NR$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestAustralianDollarTV:
    """Australian Dollar TV currency tests."""

    australian_dollar_tv_minus_one = AustralianDollarTV(-1)
    australian_dollar_tv_one_other = AustralianDollarTV(1)
    australian_dollar_tv_one = AustralianDollarTV(1)
    australian_dollar_tv_two = AustralianDollarTV(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_australian_dollar_tv_default(amount, result, printed):
        default = AustralianDollarTV(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'AUD'
        assert default.numeric_code == '036'
        assert default.symbol == '$'
        assert default.localized_symbol == 'TV$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert default.__repr__() == (
            'AustralianDollarTV('
            f'amount: {result}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "TV$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_australian_dollar_tv_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = AustralianDollarTV(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'AUD'
        assert custom.numeric_code == '036'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'TV$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'AUD',
            '036'))
        assert custom.__repr__() == (
            'AustralianDollarTV('
            f'amount: {amount}, '
            'alpha_code: "AUD", '
            'numeric_code: "036", '
            'symbol: "$", '
            'localized_symbol: "TV$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_australian_dollar_tv_recreate(amount, new_amount):
        default = AustralianDollarTV(amount)
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
    def test_australian_dollar_tv_change_attributes(attribute, value):
        immutable = AustralianDollarTV(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'AustralianDollarTV\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_australian_dollar_tv_add_attributes(attribute, value):
        immutable = AustralianDollarTV(1000)
        with raises(
                AttributeError,
                match=f'\'AustralianDollarTV\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (australian_dollar_tv_one, australian_dollar_tv_one, australian_dollar_tv_two, None),
        (australian_dollar_tv_one, australian_dollar_tv_one_other, australian_dollar_tv_two, None),
        (australian_dollar_tv_two, australian_dollar_tv_minus_one, australian_dollar_tv_one, None),
        (australian_dollar_tv_one, other, None, CurrencyMismatchException),
        (australian_dollar_tv_one, 1.00, None, CurrencyTypeException),
        (australian_dollar_tv_one, '1.00', None, CurrencyTypeException)
    ])
    def test_australian_dollar_tv_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (australian_dollar_tv_one)
    ])
    def test_australian_dollar_tv_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'AUD'
        assert new.numeric_code == '036'
        assert new.symbol == '$'
        assert new.localized_symbol == 'TV$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestBarbadosDollar:
    """Barbados Dollar currency tests."""

    barbados_dollar_minus_one = BarbadosDollar(-1)
    barbados_dollar_one_other = BarbadosDollar(1)
    barbados_dollar_one = BarbadosDollar(1)
    barbados_dollar_two = BarbadosDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_barbados_dollar_default(amount, result, printed):
        default = BarbadosDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BBD'
        assert default.numeric_code == '052'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BB$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BBD',
            '052'))
        assert default.__repr__() == (
            'BarbadosDollar('
            f'amount: {result}, '
            'alpha_code: "BBD", '
            'numeric_code: "052", '
            'symbol: "$", '
            'localized_symbol: "BB$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_barbados_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BarbadosDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BBD'
        assert custom.numeric_code == '052'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BB$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BBD',
            '052'))
        assert custom.__repr__() == (
            'BarbadosDollar('
            f'amount: {amount}, '
            'alpha_code: "BBD", '
            'numeric_code: "052", '
            'symbol: "$", '
            'localized_symbol: "BB$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_barbados_dollar_recreate(amount, new_amount):
        default = BarbadosDollar(amount)
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
    def test_barbados_dollar_change_attributes(attribute, value):
        immutable = BarbadosDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BarbadosDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_barbados_dollar_add_attributes(attribute, value):
        immutable = BarbadosDollar(1000)
        with raises(
                AttributeError,
                match=f'\'BarbadosDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (barbados_dollar_one, barbados_dollar_one, barbados_dollar_two, None),
        (barbados_dollar_one, barbados_dollar_one_other, barbados_dollar_two, None),
        (barbados_dollar_two, barbados_dollar_minus_one, barbados_dollar_one, None),
        (barbados_dollar_one, other, None, CurrencyMismatchException),
        (barbados_dollar_one, 1.00, None, CurrencyTypeException),
        (barbados_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_barbados_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (barbados_dollar_one)
    ])
    def test_barbados_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BBD'
        assert new.numeric_code == '052'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BB$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestBermudianDollar:
    """Bermudian Dollar currency tests."""

    bermudian_dollar_minus_one = BermudianDollar(-1)
    bermudian_dollar_one_other = BermudianDollar(1)
    bermudian_dollar_one = BermudianDollar(1)
    bermudian_dollar_two = BermudianDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_bermudian_dollar_default(amount, result, printed):
        default = BermudianDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BMD'
        assert default.numeric_code == '060'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BM$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BMD',
            '060'))
        assert default.__repr__() == (
            'BermudianDollar('
            f'amount: {result}, '
            'alpha_code: "BMD", '
            'numeric_code: "060", '
            'symbol: "$", '
            'localized_symbol: "BM$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_bermudian_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BermudianDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BMD'
        assert custom.numeric_code == '060'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BM$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BMD',
            '060'))
        assert custom.__repr__() == (
            'BermudianDollar('
            f'amount: {amount}, '
            'alpha_code: "BMD", '
            'numeric_code: "060", '
            'symbol: "$", '
            'localized_symbol: "BM$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bermudian_dollar_recreate(amount, new_amount):
        default = BermudianDollar(amount)
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
    def test_bermudian_dollar_change_attributes(attribute, value):
        immutable = BermudianDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BermudianDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bermudian_dollar_add_attributes(attribute, value):
        immutable = BermudianDollar(1000)
        with raises(
                AttributeError,
                match=f'\'BermudianDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bermudian_dollar_one, bermudian_dollar_one, bermudian_dollar_two, None),
        (bermudian_dollar_one, bermudian_dollar_one_other, bermudian_dollar_two, None),
        (bermudian_dollar_two, bermudian_dollar_minus_one, bermudian_dollar_one, None),
        (bermudian_dollar_one, other, None, CurrencyMismatchException),
        (bermudian_dollar_one, 1.00, None, CurrencyTypeException),
        (bermudian_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bermudian_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bermudian_dollar_one)
    ])
    def test_bermudian_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BMD'
        assert new.numeric_code == '060'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BM$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestBruneiDollar:
    """Brunei Dollar currency tests."""

    brunei_dollar_minus_one = BruneiDollar(-1)
    brunei_dollar_one_other = BruneiDollar(1)
    brunei_dollar_one = BruneiDollar(1)
    brunei_dollar_two = BruneiDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_brunei_dollar_default(amount, result, printed):
        default = BruneiDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BND'
        assert default.numeric_code == '096'
        assert default.symbol == '$'
        assert default.localized_symbol == '$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert default.__repr__() == (
            'BruneiDollar('
            f'amount: {result}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_brunei_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BruneiDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BND'
        assert custom.numeric_code == '096'
        assert custom.symbol == '$'
        assert custom.localized_symbol == '$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert custom.__repr__() == (
            'BruneiDollar('
            f'amount: {amount}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_brunei_dollar_recreate(amount, new_amount):
        default = BruneiDollar(amount)
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
    def test_brunei_dollar_change_attributes(attribute, value):
        immutable = BruneiDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BruneiDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_brunei_dollar_add_attributes(attribute, value):
        immutable = BruneiDollar(1000)
        with raises(
                AttributeError,
                match=f'\'BruneiDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (brunei_dollar_one, brunei_dollar_one, brunei_dollar_two, None),
        (brunei_dollar_one, brunei_dollar_one_other, brunei_dollar_two, None),
        (brunei_dollar_two, brunei_dollar_minus_one, brunei_dollar_one, None),
        (brunei_dollar_one, other, None, CurrencyMismatchException),
        (brunei_dollar_one, 1.00, None, CurrencyTypeException),
        (brunei_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_brunei_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (brunei_dollar_one)
    ])
    def test_brunei_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BND'
        assert new.numeric_code == '096'
        assert new.symbol == '$'
        assert new.localized_symbol == '$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestBruneiDollarBN:
    """Brunei Dollar BN currency tests."""

    brunei_dollar_bn_minus_one = BruneiDollarBN(-1)
    brunei_dollar_bn_one_other = BruneiDollarBN(1)
    brunei_dollar_bn_one = BruneiDollarBN(1)
    brunei_dollar_bn_two = BruneiDollarBN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_brunei_dollar_bn_default(amount, result, printed):
        default = BruneiDollarBN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BND'
        assert default.numeric_code == '096'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BN$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert default.__repr__() == (
            'BruneiDollarBN('
            f'amount: {result}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "BN$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_brunei_dollar_bn_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BruneiDollarBN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BND'
        assert custom.numeric_code == '096'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BN$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert custom.__repr__() == (
            'BruneiDollarBN('
            f'amount: {amount}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "BN$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_brunei_dollar_bn_recreate(amount, new_amount):
        default = BruneiDollarBN(amount)
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
    def test_brunei_dollar_bn_change_attributes(attribute, value):
        immutable = BruneiDollarBN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BruneiDollarBN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_brunei_dollar_bn_add_attributes(attribute, value):
        immutable = BruneiDollarBN(1000)
        with raises(
                AttributeError,
                match=f'\'BruneiDollarBN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (brunei_dollar_bn_one, brunei_dollar_bn_one, brunei_dollar_bn_two, None),
        (brunei_dollar_bn_one, brunei_dollar_bn_one_other, brunei_dollar_bn_two, None),
        (brunei_dollar_bn_two, brunei_dollar_bn_minus_one, brunei_dollar_bn_one, None),
        (brunei_dollar_bn_one, other, None, CurrencyMismatchException),
        (brunei_dollar_bn_one, 1.00, None, CurrencyTypeException),
        (brunei_dollar_bn_one, '1.00', None, CurrencyTypeException)
    ])
    def test_brunei_dollar_bn_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (brunei_dollar_bn_one)
    ])
    def test_brunei_dollar_bn_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BND'
        assert new.numeric_code == '096'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BN$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestBruneiDollarSG:
    """Brunei Dollar SG currency tests."""

    brunei_dollar_sg_minus_one = BruneiDollarSG(-1)
    brunei_dollar_sg_one_other = BruneiDollarSG(1)
    brunei_dollar_sg_one = BruneiDollarSG(1)
    brunei_dollar_sg_two = BruneiDollarSG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_brunei_dollar_sg_default(amount, result, printed):
        default = BruneiDollarSG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BND'
        assert default.numeric_code == '096'
        assert default.symbol == '$'
        assert default.localized_symbol == 'SG$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert default.__repr__() == (
            'BruneiDollarSG('
            f'amount: {result}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "SG$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_brunei_dollar_sg_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BruneiDollarSG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BND'
        assert custom.numeric_code == '096'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'SG$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BND',
            '096'))
        assert custom.__repr__() == (
            'BruneiDollarSG('
            f'amount: {amount}, '
            'alpha_code: "BND", '
            'numeric_code: "096", '
            'symbol: "$", '
            'localized_symbol: "SG$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_brunei_dollar_sg_recreate(amount, new_amount):
        default = BruneiDollarSG(amount)
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
    def test_brunei_dollar_sg_change_attributes(attribute, value):
        immutable = BruneiDollarSG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BruneiDollarSG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_brunei_dollar_sg_add_attributes(attribute, value):
        immutable = BruneiDollarSG(1000)
        with raises(
                AttributeError,
                match=f'\'BruneiDollarSG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (brunei_dollar_sg_one, brunei_dollar_sg_one, brunei_dollar_sg_two, None),
        (brunei_dollar_sg_one, brunei_dollar_sg_one_other, brunei_dollar_sg_two, None),
        (brunei_dollar_sg_two, brunei_dollar_sg_minus_one, brunei_dollar_sg_one, None),
        (brunei_dollar_sg_one, other, None, CurrencyMismatchException),
        (brunei_dollar_sg_one, 1.00, None, CurrencyTypeException),
        (brunei_dollar_sg_one, '1.00', None, CurrencyTypeException)
    ])
    def test_brunei_dollar_sg_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (brunei_dollar_sg_one)
    ])
    def test_brunei_dollar_sg_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BND'
        assert new.numeric_code == '096'
        assert new.symbol == '$'
        assert new.localized_symbol == 'SG$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestBahamianDollar:
    """Bahamian Dollar currency tests."""

    bahamian_dollar_minus_one = BahamianDollar(-1)
    bahamian_dollar_one_other = BahamianDollar(1)
    bahamian_dollar_one = BahamianDollar(1)
    bahamian_dollar_two = BahamianDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_bahamian_dollar_default(amount, result, printed):
        default = BahamianDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BSD'
        assert default.numeric_code == '044'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BS$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BSD',
            '044'))
        assert default.__repr__() == (
            'BahamianDollar('
            f'amount: {result}, '
            'alpha_code: "BSD", '
            'numeric_code: "044", '
            'symbol: "$", '
            'localized_symbol: "BS$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_bahamian_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BahamianDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BSD'
        assert custom.numeric_code == '044'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BS$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BSD',
            '044'))
        assert custom.__repr__() == (
            'BahamianDollar('
            f'amount: {amount}, '
            'alpha_code: "BSD", '
            'numeric_code: "044", '
            'symbol: "$", '
            'localized_symbol: "BS$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bahamian_dollar_recreate(amount, new_amount):
        default = BahamianDollar(amount)
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
    def test_bahamian_dollar_change_attributes(attribute, value):
        immutable = BahamianDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BahamianDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bahamian_dollar_add_attributes(attribute, value):
        immutable = BahamianDollar(1000)
        with raises(
                AttributeError,
                match=f'\'BahamianDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bahamian_dollar_one, bahamian_dollar_one, bahamian_dollar_two, None),
        (bahamian_dollar_one, bahamian_dollar_one_other, bahamian_dollar_two, None),
        (bahamian_dollar_two, bahamian_dollar_minus_one, bahamian_dollar_one, None),
        (bahamian_dollar_one, other, None, CurrencyMismatchException),
        (bahamian_dollar_one, 1.00, None, CurrencyTypeException),
        (bahamian_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bahamian_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bahamian_dollar_one)
    ])
    def test_bahamian_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BSD'
        assert new.numeric_code == '044'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BS$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestBelizeDollar:
    """Belize Dollar currency tests."""

    belize_dollar_minus_one = BelizeDollar(-1)
    belize_dollar_one_other = BelizeDollar(1)
    belize_dollar_one = BelizeDollar(1)
    belize_dollar_two = BelizeDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_belize_dollar_default(amount, result, printed):
        default = BelizeDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'BZD'
        assert default.numeric_code == '084'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BZ$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'BZD',
            '084'))
        assert default.__repr__() == (
            'BelizeDollar('
            f'amount: {result}, '
            'alpha_code: "BZD", '
            'numeric_code: "084", '
            'symbol: "$", '
            'localized_symbol: "BZ$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_belize_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = BelizeDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'BZD'
        assert custom.numeric_code == '084'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BZ$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'BZD',
            '084'))
        assert custom.__repr__() == (
            'BelizeDollar('
            f'amount: {amount}, '
            'alpha_code: "BZD", '
            'numeric_code: "084", '
            'symbol: "$", '
            'localized_symbol: "BZ$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_belize_dollar_recreate(amount, new_amount):
        default = BelizeDollar(amount)
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
    def test_belize_dollar_change_attributes(attribute, value):
        immutable = BelizeDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'BelizeDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_belize_dollar_add_attributes(attribute, value):
        immutable = BelizeDollar(1000)
        with raises(
                AttributeError,
                match=f'\'BelizeDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (belize_dollar_one, belize_dollar_one, belize_dollar_two, None),
        (belize_dollar_one, belize_dollar_one_other, belize_dollar_two, None),
        (belize_dollar_two, belize_dollar_minus_one, belize_dollar_one, None),
        (belize_dollar_one, other, None, CurrencyMismatchException),
        (belize_dollar_one, 1.00, None, CurrencyTypeException),
        (belize_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_belize_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (belize_dollar_one)
    ])
    def test_belize_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'BZD'
        assert new.numeric_code == '084'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BZ$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestCanadianDollarEN:
    """Canadian Dollar EN currency tests."""

    canadian_dollar_en_minus_one = CanadianDollarEN(-1)
    canadian_dollar_en_one_other = CanadianDollarEN(1)
    canadian_dollar_en_one = CanadianDollarEN(1)
    canadian_dollar_en_two = CanadianDollarEN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_canadian_dollar_en_default(amount, result, printed):
        default = CanadianDollarEN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CAD'
        assert default.numeric_code == '124'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CA$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CAD',
            '124'))
        assert default.__repr__() == (
            'CanadianDollarEN('
            f'amount: {result}, '
            'alpha_code: "CAD", '
            'numeric_code: "124", '
            'symbol: "$", '
            'localized_symbol: "CA$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_canadian_dollar_en_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CanadianDollarEN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CAD'
        assert custom.numeric_code == '124'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CA$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CAD',
            '124'))
        assert custom.__repr__() == (
            'CanadianDollarEN('
            f'amount: {amount}, '
            'alpha_code: "CAD", '
            'numeric_code: "124", '
            'symbol: "$", '
            'localized_symbol: "CA$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_canadian_dollar_en_recreate(amount, new_amount):
        default = CanadianDollarEN(amount)
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
    def test_canadian_dollar_en_change_attributes(attribute, value):
        immutable = CanadianDollarEN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CanadianDollarEN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_canadian_dollar_en_add_attributes(attribute, value):
        immutable = CanadianDollarEN(1000)
        with raises(
                AttributeError,
                match=f'\'CanadianDollarEN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (canadian_dollar_en_one, canadian_dollar_en_one, canadian_dollar_en_two, None),
        (canadian_dollar_en_one, canadian_dollar_en_one_other, canadian_dollar_en_two, None),
        (canadian_dollar_en_two, canadian_dollar_en_minus_one, canadian_dollar_en_one, None),
        (canadian_dollar_en_one, other, None, CurrencyMismatchException),
        (canadian_dollar_en_one, 1.00, None, CurrencyTypeException),
        (canadian_dollar_en_one, '1.00', None, CurrencyTypeException)
    ])
    def test_canadian_dollar_en_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (canadian_dollar_en_one)
    ])
    def test_canadian_dollar_en_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CAD'
        assert new.numeric_code == '124'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CA$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestCanadianDollarFR:
    """Canadian Dollar FR currency tests."""

    canadian_dollar_fr_minus_one = CanadianDollarFR(-1)
    canadian_dollar_fr_one_other = CanadianDollarFR(1)
    canadian_dollar_fr_one = CanadianDollarFR(1)
    canadian_dollar_fr_two = CanadianDollarFR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '3,14\xa0$'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '3,14\xa0$'),
        (10, '10', '10,00\xa0$'),
        (Decimal('10'), '10', '10,00\xa0$'),
        ('-3.14', '-3.14', '-3,14\xa0$'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3,14\xa0$'),
        (-10, '-10', '-10,00\xa0$'),
        (Decimal('-10'), '-10', '-10,00\xa0$')
    ])
    def test_canadian_dollar_fr_default(amount, result, printed):
        default = CanadianDollarFR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'CAD'
        assert default.numeric_code == '124'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CA$'
        assert default.convertion == ''
        assert default.pattern == '2,\u202F3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'CAD',
            '124'))
        assert default.__repr__() == (
            'CanadianDollarFR('
            f'amount: {result}, '
            'alpha_code: "CAD", '
            'numeric_code: "124", '
            'symbol: "$", '
            'localized_symbol: "CA$", '
            'convertion: "", '
            'pattern: "2, 3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_canadian_dollar_fr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CanadianDollarFR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'CAD'
        assert custom.numeric_code == '124'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CA$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'CAD',
            '124'))
        assert custom.__repr__() == (
            'CanadianDollarFR('
            f'amount: {amount}, '
            'alpha_code: "CAD", '
            'numeric_code: "124", '
            'symbol: "$", '
            'localized_symbol: "CA$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_canadian_dollar_fr_recreate(amount, new_amount):
        default = CanadianDollarFR(amount)
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
    def test_canadian_dollar_fr_change_attributes(attribute, value):
        immutable = CanadianDollarFR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CanadianDollarFR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_canadian_dollar_fr_add_attributes(attribute, value):
        immutable = CanadianDollarFR(1000)
        with raises(
                AttributeError,
                match=f'\'CanadianDollarFR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (canadian_dollar_fr_one, canadian_dollar_fr_one, canadian_dollar_fr_two, None),
        (canadian_dollar_fr_one, canadian_dollar_fr_one_other, canadian_dollar_fr_two, None),
        (canadian_dollar_fr_two, canadian_dollar_fr_minus_one, canadian_dollar_fr_one, None),
        (canadian_dollar_fr_one, other, None, CurrencyMismatchException),
        (canadian_dollar_fr_one, 1.00, None, CurrencyTypeException),
        (canadian_dollar_fr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_canadian_dollar_fr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (canadian_dollar_fr_one)
    ])
    def test_canadian_dollar_fr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'CAD'
        assert new.numeric_code == '124'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CA$'
        assert new.convertion == ''
        assert new.pattern == '2,\u202F3%a\u00A0%s'


class TestFijiDollar:
    """Fiji Dollar currency tests."""

    fiji_dollar_minus_one = FijiDollar(-1)
    fiji_dollar_one_other = FijiDollar(1)
    fiji_dollar_one = FijiDollar(1)
    fiji_dollar_two = FijiDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_fiji_dollar_default(amount, result, printed):
        default = FijiDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'FJD'
        assert default.numeric_code == '242'
        assert default.symbol == '$'
        assert default.localized_symbol == 'FJ$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'FJD',
            '242'))
        assert default.__repr__() == (
            'FijiDollar('
            f'amount: {result}, '
            'alpha_code: "FJD", '
            'numeric_code: "242", '
            'symbol: "$", '
            'localized_symbol: "FJ$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_fiji_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = FijiDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'FJD'
        assert custom.numeric_code == '242'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'FJ$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'FJD',
            '242'))
        assert custom.__repr__() == (
            'FijiDollar('
            f'amount: {amount}, '
            'alpha_code: "FJD", '
            'numeric_code: "242", '
            'symbol: "$", '
            'localized_symbol: "FJ$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_fiji_dollar_recreate(amount, new_amount):
        default = FijiDollar(amount)
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
    def test_fiji_dollar_change_attributes(attribute, value):
        immutable = FijiDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'FijiDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_fiji_dollar_add_attributes(attribute, value):
        immutable = FijiDollar(1000)
        with raises(
                AttributeError,
                match=f'\'FijiDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (fiji_dollar_one, fiji_dollar_one, fiji_dollar_two, None),
        (fiji_dollar_one, fiji_dollar_one_other, fiji_dollar_two, None),
        (fiji_dollar_two, fiji_dollar_minus_one, fiji_dollar_one, None),
        (fiji_dollar_one, other, None, CurrencyMismatchException),
        (fiji_dollar_one, 1.00, None, CurrencyTypeException),
        (fiji_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_fiji_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (fiji_dollar_one)
    ])
    def test_fiji_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'FJD'
        assert new.numeric_code == '242'
        assert new.symbol == '$'
        assert new.localized_symbol == 'FJ$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestGuyanaDollar:
    """Guyana Dollar currency tests."""

    guyana_dollar_minus_one = GuyanaDollar(-1)
    guyana_dollar_one_other = GuyanaDollar(1)
    guyana_dollar_one = GuyanaDollar(1)
    guyana_dollar_two = GuyanaDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_guyana_dollar_default(amount, result, printed):
        default = GuyanaDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GYD'
        assert default.numeric_code == '328'
        assert default.symbol == '$'
        assert default.localized_symbol == 'GY$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GYD',
            '328'))
        assert default.__repr__() == (
            'GuyanaDollar('
            f'amount: {result}, '
            'alpha_code: "GYD", '
            'numeric_code: "328", '
            'symbol: "$", '
            'localized_symbol: "GY$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_guyana_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = GuyanaDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GYD'
        assert custom.numeric_code == '328'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'GY$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GYD',
            '328'))
        assert custom.__repr__() == (
            'GuyanaDollar('
            f'amount: {amount}, '
            'alpha_code: "GYD", '
            'numeric_code: "328", '
            'symbol: "$", '
            'localized_symbol: "GY$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_guyana_dollar_recreate(amount, new_amount):
        default = GuyanaDollar(amount)
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
    def test_guyana_dollar_change_attributes(attribute, value):
        immutable = GuyanaDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'GuyanaDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_guyana_dollar_add_attributes(attribute, value):
        immutable = GuyanaDollar(1000)
        with raises(
                AttributeError,
                match=f'\'GuyanaDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (guyana_dollar_one, guyana_dollar_one, guyana_dollar_two, None),
        (guyana_dollar_one, guyana_dollar_one_other, guyana_dollar_two, None),
        (guyana_dollar_two, guyana_dollar_minus_one, guyana_dollar_one, None),
        (guyana_dollar_one, other, None, CurrencyMismatchException),
        (guyana_dollar_one, 1.00, None, CurrencyTypeException),
        (guyana_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_guyana_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (guyana_dollar_one)
    ])
    def test_guyana_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GYD'
        assert new.numeric_code == '328'
        assert new.symbol == '$'
        assert new.localized_symbol == 'GY$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestHongKongDollar:
    """Hong Kong Dollar currency tests."""

    hong_kong_dollar_minus_one = HongKongDollar(-1)
    hong_kong_dollar_one_other = HongKongDollar(1)
    hong_kong_dollar_one = HongKongDollar(1)
    hong_kong_dollar_two = HongKongDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_hong_kong_dollar_default(amount, result, printed):
        default = HongKongDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'HKD'
        assert default.numeric_code == '344'
        assert default.symbol == '$'
        assert default.localized_symbol == 'HK$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'HKD',
            '344'))
        assert default.__repr__() == (
            'HongKongDollar('
            f'amount: {result}, '
            'alpha_code: "HKD", '
            'numeric_code: "344", '
            'symbol: "$", '
            'localized_symbol: "HK$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_hong_kong_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = HongKongDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'HKD'
        assert custom.numeric_code == '344'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'HK$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'HKD',
            '344'))
        assert custom.__repr__() == (
            'HongKongDollar('
            f'amount: {amount}, '
            'alpha_code: "HKD", '
            'numeric_code: "344", '
            'symbol: "$", '
            'localized_symbol: "HK$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_hong_kong_dollar_recreate(amount, new_amount):
        default = HongKongDollar(amount)
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
    def test_hong_kong_dollar_change_attributes(attribute, value):
        immutable = HongKongDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'HongKongDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_hong_kong_dollar_add_attributes(attribute, value):
        immutable = HongKongDollar(1000)
        with raises(
                AttributeError,
                match=f'\'HongKongDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (hong_kong_dollar_one, hong_kong_dollar_one, hong_kong_dollar_two, None),
        (hong_kong_dollar_one, hong_kong_dollar_one_other, hong_kong_dollar_two, None),
        (hong_kong_dollar_two, hong_kong_dollar_minus_one, hong_kong_dollar_one, None),
        (hong_kong_dollar_one, other, None, CurrencyMismatchException),
        (hong_kong_dollar_one, 1.00, None, CurrencyTypeException),
        (hong_kong_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_hong_kong_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (hong_kong_dollar_one)
    ])
    def test_hong_kong_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'HKD'
        assert new.numeric_code == '344'
        assert new.symbol == '$'
        assert new.localized_symbol == 'HK$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestJamaicanDollar:
    """Jamaican Dollar currency tests."""

    jamaican_dollar_minus_one = JamaicanDollar(-1)
    jamaican_dollar_one_other = JamaicanDollar(1)
    jamaican_dollar_one = JamaicanDollar(1)
    jamaican_dollar_two = JamaicanDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_jamaican_dollar_default(amount, result, printed):
        default = JamaicanDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'JMD'
        assert default.numeric_code == '388'
        assert default.symbol == '$'
        assert default.localized_symbol == 'JM$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'JMD',
            '388'))
        assert default.__repr__() == (
            'JamaicanDollar('
            f'amount: {result}, '
            'alpha_code: "JMD", '
            'numeric_code: "388", '
            'symbol: "$", '
            'localized_symbol: "JM$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_jamaican_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = JamaicanDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'JMD'
        assert custom.numeric_code == '388'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'JM$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'JMD',
            '388'))
        assert custom.__repr__() == (
            'JamaicanDollar('
            f'amount: {amount}, '
            'alpha_code: "JMD", '
            'numeric_code: "388", '
            'symbol: "$", '
            'localized_symbol: "JM$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_jamaican_dollar_recreate(amount, new_amount):
        default = JamaicanDollar(amount)
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
    def test_jamaican_dollar_change_attributes(attribute, value):
        immutable = JamaicanDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'JamaicanDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_jamaican_dollar_add_attributes(attribute, value):
        immutable = JamaicanDollar(1000)
        with raises(
                AttributeError,
                match=f'\'JamaicanDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (jamaican_dollar_one, jamaican_dollar_one, jamaican_dollar_two, None),
        (jamaican_dollar_one, jamaican_dollar_one_other, jamaican_dollar_two, None),
        (jamaican_dollar_two, jamaican_dollar_minus_one, jamaican_dollar_one, None),
        (jamaican_dollar_one, other, None, CurrencyMismatchException),
        (jamaican_dollar_one, 1.00, None, CurrencyTypeException),
        (jamaican_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_jamaican_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (jamaican_dollar_one)
    ])
    def test_jamaican_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'JMD'
        assert new.numeric_code == '388'
        assert new.symbol == '$'
        assert new.localized_symbol == 'JM$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestCaymanIslandsDollar:
    """Cayman Islands Dollar currency tests."""

    cayman_islands_dollar_minus_one = CaymanIslandsDollar(-1)
    cayman_islands_dollar_one_other = CaymanIslandsDollar(1)
    cayman_islands_dollar_one = CaymanIslandsDollar(1)
    cayman_islands_dollar_two = CaymanIslandsDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_cayman_islands_dollar_default(amount, result, printed):
        default = CaymanIslandsDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'KYD'
        assert default.numeric_code == '136'
        assert default.symbol == '$'
        assert default.localized_symbol == 'KY$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'KYD',
            '136'))
        assert default.__repr__() == (
            'CaymanIslandsDollar('
            f'amount: {result}, '
            'alpha_code: "KYD", '
            'numeric_code: "136", '
            'symbol: "$", '
            'localized_symbol: "KY$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_cayman_islands_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = CaymanIslandsDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'KYD'
        assert custom.numeric_code == '136'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'KY$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'KYD',
            '136'))
        assert custom.__repr__() == (
            'CaymanIslandsDollar('
            f'amount: {amount}, '
            'alpha_code: "KYD", '
            'numeric_code: "136", '
            'symbol: "$", '
            'localized_symbol: "KY$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_cayman_islands_dollar_recreate(amount, new_amount):
        default = CaymanIslandsDollar(amount)
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
    def test_cayman_islands_dollar_change_attributes(attribute, value):
        immutable = CaymanIslandsDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'CaymanIslandsDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_cayman_islands_dollar_add_attributes(attribute, value):
        immutable = CaymanIslandsDollar(1000)
        with raises(
                AttributeError,
                match=f'\'CaymanIslandsDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (cayman_islands_dollar_one, cayman_islands_dollar_one, cayman_islands_dollar_two, None),
        (cayman_islands_dollar_one, cayman_islands_dollar_one_other, cayman_islands_dollar_two, None),
        (cayman_islands_dollar_two, cayman_islands_dollar_minus_one, cayman_islands_dollar_one, None),
        (cayman_islands_dollar_one, other, None, CurrencyMismatchException),
        (cayman_islands_dollar_one, 1.00, None, CurrencyTypeException),
        (cayman_islands_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_cayman_islands_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (cayman_islands_dollar_one)
    ])
    def test_cayman_islands_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'KYD'
        assert new.numeric_code == '136'
        assert new.symbol == '$'
        assert new.localized_symbol == 'KY$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestLiberianDollar:
    """Liberian Dollar currency tests."""

    liberian_dollar_minus_one = LiberianDollar(-1)
    liberian_dollar_one_other = LiberianDollar(1)
    liberian_dollar_one = LiberianDollar(1)
    liberian_dollar_two = LiberianDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_liberian_dollar_default(amount, result, printed):
        default = LiberianDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LRD'
        assert default.numeric_code == '430'
        assert default.symbol == '$'
        assert default.localized_symbol == 'LR$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LRD',
            '430'))
        assert default.__repr__() == (
            'LiberianDollar('
            f'amount: {result}, '
            'alpha_code: "LRD", '
            'numeric_code: "430", '
            'symbol: "$", '
            'localized_symbol: "LR$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_liberian_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = LiberianDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LRD'
        assert custom.numeric_code == '430'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'LR$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LRD',
            '430'))
        assert custom.__repr__() == (
            'LiberianDollar('
            f'amount: {amount}, '
            'alpha_code: "LRD", '
            'numeric_code: "430", '
            'symbol: "$", '
            'localized_symbol: "LR$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_liberian_dollar_recreate(amount, new_amount):
        default = LiberianDollar(amount)
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
    def test_liberian_dollar_change_attributes(attribute, value):
        immutable = LiberianDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'LiberianDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_liberian_dollar_add_attributes(attribute, value):
        immutable = LiberianDollar(1000)
        with raises(
                AttributeError,
                match=f'\'LiberianDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (liberian_dollar_one, liberian_dollar_one, liberian_dollar_two, None),
        (liberian_dollar_one, liberian_dollar_one_other, liberian_dollar_two, None),
        (liberian_dollar_two, liberian_dollar_minus_one, liberian_dollar_one, None),
        (liberian_dollar_one, other, None, CurrencyMismatchException),
        (liberian_dollar_one, 1.00, None, CurrencyTypeException),
        (liberian_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_liberian_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (liberian_dollar_one)
    ])
    def test_liberian_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LRD'
        assert new.numeric_code == '430'
        assert new.symbol == '$'
        assert new.localized_symbol == 'LR$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNamibiaDollar:
    """Namibia Dollar currency tests."""

    namibia_dollar_minus_one = NamibiaDollar(-1)
    namibia_dollar_one_other = NamibiaDollar(1)
    namibia_dollar_one = NamibiaDollar(1)
    namibia_dollar_two = NamibiaDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_namibia_dollar_default(amount, result, printed):
        default = NamibiaDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NAD'
        assert default.numeric_code == '516'
        assert default.symbol == '$'
        assert default.localized_symbol == 'NA$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NAD',
            '516'))
        assert default.__repr__() == (
            'NamibiaDollar('
            f'amount: {result}, '
            'alpha_code: "NAD", '
            'numeric_code: "516", '
            'symbol: "$", '
            'localized_symbol: "NA$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_namibia_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NamibiaDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NAD'
        assert custom.numeric_code == '516'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'NA$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NAD',
            '516'))
        assert custom.__repr__() == (
            'NamibiaDollar('
            f'amount: {amount}, '
            'alpha_code: "NAD", '
            'numeric_code: "516", '
            'symbol: "$", '
            'localized_symbol: "NA$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_namibia_dollar_recreate(amount, new_amount):
        default = NamibiaDollar(amount)
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
    def test_namibia_dollar_change_attributes(attribute, value):
        immutable = NamibiaDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NamibiaDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_namibia_dollar_add_attributes(attribute, value):
        immutable = NamibiaDollar(1000)
        with raises(
                AttributeError,
                match=f'\'NamibiaDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (namibia_dollar_one, namibia_dollar_one, namibia_dollar_two, None),
        (namibia_dollar_one, namibia_dollar_one_other, namibia_dollar_two, None),
        (namibia_dollar_two, namibia_dollar_minus_one, namibia_dollar_one, None),
        (namibia_dollar_one, other, None, CurrencyMismatchException),
        (namibia_dollar_one, 1.00, None, CurrencyTypeException),
        (namibia_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_namibia_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (namibia_dollar_one)
    ])
    def test_namibia_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NAD'
        assert new.numeric_code == '516'
        assert new.symbol == '$'
        assert new.localized_symbol == 'NA$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNewZealandDollar:
    """New Zealand Dollar currency tests."""

    new_zealand_dollar_minus_one = NewZealandDollar(-1)
    new_zealand_dollar_one_other = NewZealandDollar(1)
    new_zealand_dollar_one = NewZealandDollar(1)
    new_zealand_dollar_two = NewZealandDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_new_zealand_dollar_default(amount, result, printed):
        default = NewZealandDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NZD'
        assert default.numeric_code == '554'
        assert default.symbol == '$'
        assert default.localized_symbol == '$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert default.__repr__() == (
            'NewZealandDollar('
            f'amount: {result}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_new_zealand_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewZealandDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NZD'
        assert custom.numeric_code == '554'
        assert custom.symbol == '$'
        assert custom.localized_symbol == '$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert custom.__repr__() == (
            'NewZealandDollar('
            f'amount: {amount}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_zealand_dollar_recreate(amount, new_amount):
        default = NewZealandDollar(amount)
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
    def test_new_zealand_dollar_change_attributes(attribute, value):
        immutable = NewZealandDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewZealandDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_zealand_dollar_add_attributes(attribute, value):
        immutable = NewZealandDollar(1000)
        with raises(
                AttributeError,
                match=f'\'NewZealandDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_zealand_dollar_one, new_zealand_dollar_one, new_zealand_dollar_two, None),
        (new_zealand_dollar_one, new_zealand_dollar_one_other, new_zealand_dollar_two, None),
        (new_zealand_dollar_two, new_zealand_dollar_minus_one, new_zealand_dollar_one, None),
        (new_zealand_dollar_one, other, None, CurrencyMismatchException),
        (new_zealand_dollar_one, 1.00, None, CurrencyTypeException),
        (new_zealand_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_zealand_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_zealand_dollar_one)
    ])
    def test_new_zealand_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NZD'
        assert new.numeric_code == '554'
        assert new.symbol == '$'
        assert new.localized_symbol == '$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNewZealandDollarCK:
    """New Zealand Dollar CK currency tests."""

    new_zealand_dollar_ck_minus_one = NewZealandDollarCK(-1)
    new_zealand_dollar_ck_one_other = NewZealandDollarCK(1)
    new_zealand_dollar_ck_one = NewZealandDollarCK(1)
    new_zealand_dollar_ck_two = NewZealandDollarCK(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_new_zealand_dollar_ck_default(amount, result, printed):
        default = NewZealandDollarCK(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NZD'
        assert default.numeric_code == '554'
        assert default.symbol == '$'
        assert default.localized_symbol == 'CK$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert default.__repr__() == (
            'NewZealandDollarCK('
            f'amount: {result}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "CK$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_new_zealand_dollar_ck_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewZealandDollarCK(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NZD'
        assert custom.numeric_code == '554'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'CK$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert custom.__repr__() == (
            'NewZealandDollarCK('
            f'amount: {amount}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "CK$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_zealand_dollar_ck_recreate(amount, new_amount):
        default = NewZealandDollarCK(amount)
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
    def test_new_zealand_dollar_ck_change_attributes(attribute, value):
        immutable = NewZealandDollarCK(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewZealandDollarCK\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_zealand_dollar_ck_add_attributes(attribute, value):
        immutable = NewZealandDollarCK(1000)
        with raises(
                AttributeError,
                match=f'\'NewZealandDollarCK\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_zealand_dollar_ck_one, new_zealand_dollar_ck_one, new_zealand_dollar_ck_two, None),
        (new_zealand_dollar_ck_one, new_zealand_dollar_ck_one_other, new_zealand_dollar_ck_two, None),
        (new_zealand_dollar_ck_two, new_zealand_dollar_ck_minus_one, new_zealand_dollar_ck_one, None),
        (new_zealand_dollar_ck_one, other, None, CurrencyMismatchException),
        (new_zealand_dollar_ck_one, 1.00, None, CurrencyTypeException),
        (new_zealand_dollar_ck_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_zealand_dollar_ck_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_zealand_dollar_ck_one)
    ])
    def test_new_zealand_dollar_ck_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NZD'
        assert new.numeric_code == '554'
        assert new.symbol == '$'
        assert new.localized_symbol == 'CK$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNewZealandDollarNZ:
    """New Zealand Dollar NZ currency tests."""

    new_zealand_dollar_nz_minus_one = NewZealandDollarNZ(-1)
    new_zealand_dollar_nz_one_other = NewZealandDollarNZ(1)
    new_zealand_dollar_nz_one = NewZealandDollarNZ(1)
    new_zealand_dollar_nz_two = NewZealandDollarNZ(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_new_zealand_dollar_nz_default(amount, result, printed):
        default = NewZealandDollarNZ(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NZD'
        assert default.numeric_code == '554'
        assert default.symbol == '$'
        assert default.localized_symbol == 'NZ$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert default.__repr__() == (
            'NewZealandDollarNZ('
            f'amount: {result}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "NZ$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_new_zealand_dollar_nz_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewZealandDollarNZ(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NZD'
        assert custom.numeric_code == '554'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'NZ$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert custom.__repr__() == (
            'NewZealandDollarNZ('
            f'amount: {amount}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "NZ$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_zealand_dollar_nz_recreate(amount, new_amount):
        default = NewZealandDollarNZ(amount)
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
    def test_new_zealand_dollar_nz_change_attributes(attribute, value):
        immutable = NewZealandDollarNZ(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewZealandDollarNZ\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_zealand_dollar_nz_add_attributes(attribute, value):
        immutable = NewZealandDollarNZ(1000)
        with raises(
                AttributeError,
                match=f'\'NewZealandDollarNZ\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_zealand_dollar_nz_one, new_zealand_dollar_nz_one, new_zealand_dollar_nz_two, None),
        (new_zealand_dollar_nz_one, new_zealand_dollar_nz_one_other, new_zealand_dollar_nz_two, None),
        (new_zealand_dollar_nz_two, new_zealand_dollar_nz_minus_one, new_zealand_dollar_nz_one, None),
        (new_zealand_dollar_nz_one, other, None, CurrencyMismatchException),
        (new_zealand_dollar_nz_one, 1.00, None, CurrencyTypeException),
        (new_zealand_dollar_nz_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_zealand_dollar_nz_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_zealand_dollar_nz_one)
    ])
    def test_new_zealand_dollar_nz_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NZD'
        assert new.numeric_code == '554'
        assert new.symbol == '$'
        assert new.localized_symbol == 'NZ$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNewZealandDollarNU:
    """New Zealand Dollar NU currency tests."""

    new_zealand_dollar_nu_minus_one = NewZealandDollarNU(-1)
    new_zealand_dollar_nu_one_other = NewZealandDollarNU(1)
    new_zealand_dollar_nu_one = NewZealandDollarNU(1)
    new_zealand_dollar_nu_two = NewZealandDollarNU(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_new_zealand_dollar_nu_default(amount, result, printed):
        default = NewZealandDollarNU(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NZD'
        assert default.numeric_code == '554'
        assert default.symbol == '$'
        assert default.localized_symbol == 'NU$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert default.__repr__() == (
            'NewZealandDollarNU('
            f'amount: {result}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "NU$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_new_zealand_dollar_nu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewZealandDollarNU(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NZD'
        assert custom.numeric_code == '554'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'NU$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert custom.__repr__() == (
            'NewZealandDollarNU('
            f'amount: {amount}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "NU$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_zealand_dollar_nu_recreate(amount, new_amount):
        default = NewZealandDollarNU(amount)
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
    def test_new_zealand_dollar_nu_change_attributes(attribute, value):
        immutable = NewZealandDollarNU(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewZealandDollarNU\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_zealand_dollar_nu_add_attributes(attribute, value):
        immutable = NewZealandDollarNU(1000)
        with raises(
                AttributeError,
                match=f'\'NewZealandDollarNU\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_zealand_dollar_nu_one, new_zealand_dollar_nu_one, new_zealand_dollar_nu_two, None),
        (new_zealand_dollar_nu_one, new_zealand_dollar_nu_one_other, new_zealand_dollar_nu_two, None),
        (new_zealand_dollar_nu_two, new_zealand_dollar_nu_minus_one, new_zealand_dollar_nu_one, None),
        (new_zealand_dollar_nu_one, other, None, CurrencyMismatchException),
        (new_zealand_dollar_nu_one, 1.00, None, CurrencyTypeException),
        (new_zealand_dollar_nu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_zealand_dollar_nu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_zealand_dollar_nu_one)
    ])
    def test_new_zealand_dollar_nu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NZD'
        assert new.numeric_code == '554'
        assert new.symbol == '$'
        assert new.localized_symbol == 'NU$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestNewZealandDollarPN:
    """New Zealand Dollar PN currency tests."""

    new_zealand_dollar_pn_minus_one = NewZealandDollarPN(-1)
    new_zealand_dollar_pn_one_other = NewZealandDollarPN(1)
    new_zealand_dollar_pn_one = NewZealandDollarPN(1)
    new_zealand_dollar_pn_two = NewZealandDollarPN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_new_zealand_dollar_pn_default(amount, result, printed):
        default = NewZealandDollarPN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'NZD'
        assert default.numeric_code == '554'
        assert default.symbol == '$'
        assert default.localized_symbol == 'PN$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert default.__repr__() == (
            'NewZealandDollarPN('
            f'amount: {result}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "PN$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_new_zealand_dollar_pn_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = NewZealandDollarPN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'NZD'
        assert custom.numeric_code == '554'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'PN$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'NZD',
            '554'))
        assert custom.__repr__() == (
            'NewZealandDollarPN('
            f'amount: {amount}, '
            'alpha_code: "NZD", '
            'numeric_code: "554", '
            'symbol: "$", '
            'localized_symbol: "PN$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_new_zealand_dollar_pn_recreate(amount, new_amount):
        default = NewZealandDollarPN(amount)
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
    def test_new_zealand_dollar_pn_change_attributes(attribute, value):
        immutable = NewZealandDollarPN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'NewZealandDollarPN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_new_zealand_dollar_pn_add_attributes(attribute, value):
        immutable = NewZealandDollarPN(1000)
        with raises(
                AttributeError,
                match=f'\'NewZealandDollarPN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (new_zealand_dollar_pn_one, new_zealand_dollar_pn_one, new_zealand_dollar_pn_two, None),
        (new_zealand_dollar_pn_one, new_zealand_dollar_pn_one_other, new_zealand_dollar_pn_two, None),
        (new_zealand_dollar_pn_two, new_zealand_dollar_pn_minus_one, new_zealand_dollar_pn_one, None),
        (new_zealand_dollar_pn_one, other, None, CurrencyMismatchException),
        (new_zealand_dollar_pn_one, 1.00, None, CurrencyTypeException),
        (new_zealand_dollar_pn_one, '1.00', None, CurrencyTypeException)
    ])
    def test_new_zealand_dollar_pn_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (new_zealand_dollar_pn_one)
    ])
    def test_new_zealand_dollar_pn_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'NZD'
        assert new.numeric_code == '554'
        assert new.symbol == '$'
        assert new.localized_symbol == 'PN$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSolomonIslandsDollar:
    """Solomon Islands Dollar currency tests."""

    solomon_islands_dollar_minus_one = SolomonIslandsDollar(-1)
    solomon_islands_dollar_one_other = SolomonIslandsDollar(1)
    solomon_islands_dollar_one = SolomonIslandsDollar(1)
    solomon_islands_dollar_two = SolomonIslandsDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_solomon_islands_dollar_default(amount, result, printed):
        default = SolomonIslandsDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SBD'
        assert default.numeric_code == '090'
        assert default.symbol == '$'
        assert default.localized_symbol == 'SB$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SBD',
            '090'))
        assert default.__repr__() == (
            'SolomonIslandsDollar('
            f'amount: {result}, '
            'alpha_code: "SBD", '
            'numeric_code: "090", '
            'symbol: "$", '
            'localized_symbol: "SB$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_solomon_islands_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SolomonIslandsDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SBD'
        assert custom.numeric_code == '090'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'SB$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SBD',
            '090'))
        assert custom.__repr__() == (
            'SolomonIslandsDollar('
            f'amount: {amount}, '
            'alpha_code: "SBD", '
            'numeric_code: "090", '
            'symbol: "$", '
            'localized_symbol: "SB$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_solomon_islands_dollar_recreate(amount, new_amount):
        default = SolomonIslandsDollar(amount)
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
    def test_solomon_islands_dollar_change_attributes(attribute, value):
        immutable = SolomonIslandsDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SolomonIslandsDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_solomon_islands_dollar_add_attributes(attribute, value):
        immutable = SolomonIslandsDollar(1000)
        with raises(
                AttributeError,
                match=f'\'SolomonIslandsDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (solomon_islands_dollar_one, solomon_islands_dollar_one, solomon_islands_dollar_two, None),
        (solomon_islands_dollar_one, solomon_islands_dollar_one_other, solomon_islands_dollar_two, None),
        (solomon_islands_dollar_two, solomon_islands_dollar_minus_one, solomon_islands_dollar_one, None),
        (solomon_islands_dollar_one, other, None, CurrencyMismatchException),
        (solomon_islands_dollar_one, 1.00, None, CurrencyTypeException),
        (solomon_islands_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_solomon_islands_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (solomon_islands_dollar_one)
    ])
    def test_solomon_islands_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SBD'
        assert new.numeric_code == '090'
        assert new.symbol == '$'
        assert new.localized_symbol == 'SB$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSingaporeDollar:
    """Singapore Dollar currency tests."""

    singapore_dollar_minus_one = SingaporeDollar(-1)
    singapore_dollar_one_other = SingaporeDollar(1)
    singapore_dollar_one = SingaporeDollar(1)
    singapore_dollar_two = SingaporeDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_singapore_dollar_default(amount, result, printed):
        default = SingaporeDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SGD'
        assert default.numeric_code == '702'
        assert default.symbol == '$'
        assert default.localized_symbol == '$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert default.__repr__() == (
            'SingaporeDollar('
            f'amount: {result}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_singapore_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SingaporeDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SGD'
        assert custom.numeric_code == '702'
        assert custom.symbol == '$'
        assert custom.localized_symbol == '$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert custom.__repr__() == (
            'SingaporeDollar('
            f'amount: {amount}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_singapore_dollar_recreate(amount, new_amount):
        default = SingaporeDollar(amount)
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
    def test_singapore_dollar_change_attributes(attribute, value):
        immutable = SingaporeDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SingaporeDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_singapore_dollar_add_attributes(attribute, value):
        immutable = SingaporeDollar(1000)
        with raises(
                AttributeError,
                match=f'\'SingaporeDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (singapore_dollar_one, singapore_dollar_one, singapore_dollar_two, None),
        (singapore_dollar_one, singapore_dollar_one_other, singapore_dollar_two, None),
        (singapore_dollar_two, singapore_dollar_minus_one, singapore_dollar_one, None),
        (singapore_dollar_one, other, None, CurrencyMismatchException),
        (singapore_dollar_one, 1.00, None, CurrencyTypeException),
        (singapore_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_singapore_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (singapore_dollar_one)
    ])
    def test_singapore_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SGD'
        assert new.numeric_code == '702'
        assert new.symbol == '$'
        assert new.localized_symbol == '$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSingaporeDollarBN:
    """Singapore Dollar BN currency tests."""

    singapore_dollar_bn_minus_one = SingaporeDollarBN(-1)
    singapore_dollar_bn_one_other = SingaporeDollarBN(1)
    singapore_dollar_bn_one = SingaporeDollarBN(1)
    singapore_dollar_bn_two = SingaporeDollarBN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_singapore_dollar_bn_default(amount, result, printed):
        default = SingaporeDollarBN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SGD'
        assert default.numeric_code == '702'
        assert default.symbol == '$'
        assert default.localized_symbol == 'BN$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert default.__repr__() == (
            'SingaporeDollarBN('
            f'amount: {result}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "BN$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_singapore_dollar_bn_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SingaporeDollarBN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SGD'
        assert custom.numeric_code == '702'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'BN$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert custom.__repr__() == (
            'SingaporeDollarBN('
            f'amount: {amount}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "BN$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_singapore_dollar_bn_recreate(amount, new_amount):
        default = SingaporeDollarBN(amount)
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
    def test_singapore_dollar_bn_change_attributes(attribute, value):
        immutable = SingaporeDollarBN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SingaporeDollarBN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_singapore_dollar_bn_add_attributes(attribute, value):
        immutable = SingaporeDollarBN(1000)
        with raises(
                AttributeError,
                match=f'\'SingaporeDollarBN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (singapore_dollar_bn_one, singapore_dollar_bn_one, singapore_dollar_bn_two, None),
        (singapore_dollar_bn_one, singapore_dollar_bn_one_other, singapore_dollar_bn_two, None),
        (singapore_dollar_bn_two, singapore_dollar_bn_minus_one, singapore_dollar_bn_one, None),
        (singapore_dollar_bn_one, other, None, CurrencyMismatchException),
        (singapore_dollar_bn_one, 1.00, None, CurrencyTypeException),
        (singapore_dollar_bn_one, '1.00', None, CurrencyTypeException)
    ])
    def test_singapore_dollar_bn_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (singapore_dollar_bn_one)
    ])
    def test_singapore_dollar_bn_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SGD'
        assert new.numeric_code == '702'
        assert new.symbol == '$'
        assert new.localized_symbol == 'BN$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSingaporeDollarSG:
    """Singapore Dollar SG currency tests."""

    singapore_dollar_sg_minus_one = SingaporeDollarSG(-1)
    singapore_dollar_sg_one_other = SingaporeDollarSG(1)
    singapore_dollar_sg_one = SingaporeDollarSG(1)
    singapore_dollar_sg_two = SingaporeDollarSG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_singapore_dollar_sg_default(amount, result, printed):
        default = SingaporeDollarSG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SGD'
        assert default.numeric_code == '702'
        assert default.symbol == '$'
        assert default.localized_symbol == 'SG$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert default.__repr__() == (
            'SingaporeDollarSG('
            f'amount: {result}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "SG$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_singapore_dollar_sg_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SingaporeDollarSG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SGD'
        assert custom.numeric_code == '702'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'SG$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SGD',
            '702'))
        assert custom.__repr__() == (
            'SingaporeDollarSG('
            f'amount: {amount}, '
            'alpha_code: "SGD", '
            'numeric_code: "702", '
            'symbol: "$", '
            'localized_symbol: "SG$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_singapore_dollar_sg_recreate(amount, new_amount):
        default = SingaporeDollarSG(amount)
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
    def test_singapore_dollar_sg_change_attributes(attribute, value):
        immutable = SingaporeDollarSG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SingaporeDollarSG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_singapore_dollar_sg_add_attributes(attribute, value):
        immutable = SingaporeDollarSG(1000)
        with raises(
                AttributeError,
                match=f'\'SingaporeDollarSG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (singapore_dollar_sg_one, singapore_dollar_sg_one, singapore_dollar_sg_two, None),
        (singapore_dollar_sg_one, singapore_dollar_sg_one_other, singapore_dollar_sg_two, None),
        (singapore_dollar_sg_two, singapore_dollar_sg_minus_one, singapore_dollar_sg_one, None),
        (singapore_dollar_sg_one, other, None, CurrencyMismatchException),
        (singapore_dollar_sg_one, 1.00, None, CurrencyTypeException),
        (singapore_dollar_sg_one, '1.00', None, CurrencyTypeException)
    ])
    def test_singapore_dollar_sg_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (singapore_dollar_sg_one)
    ])
    def test_singapore_dollar_sg_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SGD'
        assert new.numeric_code == '702'
        assert new.symbol == '$'
        assert new.localized_symbol == 'SG$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSurinameDollar:
    """Suriname Dollar currency tests."""

    suriname_dollar_minus_one = SurinameDollar(-1)
    suriname_dollar_one_other = SurinameDollar(1)
    suriname_dollar_one = SurinameDollar(1)
    suriname_dollar_two = SurinameDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03,14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03,14'),
        (10, '10', '$\xa010,00'),
        (Decimal('10'), '10', '$\xa010,00'),
        ('-3.14', '-3.14', '$\xa0-3,14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3,14'),
        (-10, '-10', '$\xa0-10,00'),
        (Decimal('-10'), '-10', '$\xa0-10,00')
    ])
    def test_suriname_dollar_default(amount, result, printed):
        default = SurinameDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SRD'
        assert default.numeric_code == '968'
        assert default.symbol == '$'
        assert default.localized_symbol == 'SR$'
        assert default.convertion == ''
        assert default.pattern == '2,.3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SRD',
            '968'))
        assert default.__repr__() == (
            'SurinameDollar('
            f'amount: {result}, '
            'alpha_code: "SRD", '
            'numeric_code: "968", '
            'symbol: "$", '
            'localized_symbol: "SR$", '
            'convertion: "", '
            'pattern: "2,.3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_suriname_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SurinameDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SRD'
        assert custom.numeric_code == '968'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'SR$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SRD',
            '968'))
        assert custom.__repr__() == (
            'SurinameDollar('
            f'amount: {amount}, '
            'alpha_code: "SRD", '
            'numeric_code: "968", '
            'symbol: "$", '
            'localized_symbol: "SR$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_suriname_dollar_recreate(amount, new_amount):
        default = SurinameDollar(amount)
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
    def test_suriname_dollar_change_attributes(attribute, value):
        immutable = SurinameDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SurinameDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_suriname_dollar_add_attributes(attribute, value):
        immutable = SurinameDollar(1000)
        with raises(
                AttributeError,
                match=f'\'SurinameDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (suriname_dollar_one, suriname_dollar_one, suriname_dollar_two, None),
        (suriname_dollar_one, suriname_dollar_one_other, suriname_dollar_two, None),
        (suriname_dollar_two, suriname_dollar_minus_one, suriname_dollar_one, None),
        (suriname_dollar_one, other, None, CurrencyMismatchException),
        (suriname_dollar_one, 1.00, None, CurrencyTypeException),
        (suriname_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_suriname_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (suriname_dollar_one)
    ])
    def test_suriname_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SRD'
        assert new.numeric_code == '968'
        assert new.symbol == '$'
        assert new.localized_symbol == 'SR$'
        assert new.convertion == ''
        assert new.pattern == '2,.3%s\u00A0%a'


class TestTrinidadandTobagoDollar:
    """Trinidad and Tobago Dollar currency tests."""

    trinidad_and_tobago_dollar_minus_one = TrinidadandTobagoDollar(-1)
    trinidad_and_tobago_dollar_one_other = TrinidadandTobagoDollar(1)
    trinidad_and_tobago_dollar_one = TrinidadandTobagoDollar(1)
    trinidad_and_tobago_dollar_two = TrinidadandTobagoDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_trinidad_and_tobago_dollar_default(amount, result, printed):
        default = TrinidadandTobagoDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TTD'
        assert default.numeric_code == '780'
        assert default.symbol == '$'
        assert default.localized_symbol == 'TT$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TTD',
            '780'))
        assert default.__repr__() == (
            'TrinidadandTobagoDollar('
            f'amount: {result}, '
            'alpha_code: "TTD", '
            'numeric_code: "780", '
            'symbol: "$", '
            'localized_symbol: "TT$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_trinidad_and_tobago_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TrinidadandTobagoDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TTD'
        assert custom.numeric_code == '780'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'TT$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TTD',
            '780'))
        assert custom.__repr__() == (
            'TrinidadandTobagoDollar('
            f'amount: {amount}, '
            'alpha_code: "TTD", '
            'numeric_code: "780", '
            'symbol: "$", '
            'localized_symbol: "TT$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_trinidad_and_tobago_dollar_recreate(amount, new_amount):
        default = TrinidadandTobagoDollar(amount)
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
    def test_trinidad_and_tobago_dollar_change_attributes(attribute, value):
        immutable = TrinidadandTobagoDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TrinidadandTobagoDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_trinidad_and_tobago_dollar_add_attributes(attribute, value):
        immutable = TrinidadandTobagoDollar(1000)
        with raises(
                AttributeError,
                match=f'\'TrinidadandTobagoDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (trinidad_and_tobago_dollar_one, trinidad_and_tobago_dollar_one, trinidad_and_tobago_dollar_two, None),
        (trinidad_and_tobago_dollar_one, trinidad_and_tobago_dollar_one_other, trinidad_and_tobago_dollar_two, None),
        (trinidad_and_tobago_dollar_two, trinidad_and_tobago_dollar_minus_one, trinidad_and_tobago_dollar_one, None),
        (trinidad_and_tobago_dollar_one, other, None, CurrencyMismatchException),
        (trinidad_and_tobago_dollar_one, 1.00, None, CurrencyTypeException),
        (trinidad_and_tobago_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_trinidad_and_tobago_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (trinidad_and_tobago_dollar_one)
    ])
    def test_trinidad_and_tobago_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TTD'
        assert new.numeric_code == '780'
        assert new.symbol == '$'
        assert new.localized_symbol == 'TT$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestTaiwanDollar:
    """Taiwan Dollar currency tests."""

    taiwan_dollar_minus_one = TaiwanDollar(-1)
    taiwan_dollar_one_other = TaiwanDollar(1)
    taiwan_dollar_one = TaiwanDollar(1)
    taiwan_dollar_two = TaiwanDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_taiwan_dollar_default(amount, result, printed):
        default = TaiwanDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'TWD'
        assert default.numeric_code == '901'
        assert default.symbol == '$'
        assert default.localized_symbol == 'TW$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'TWD',
            '901'))
        assert default.__repr__() == (
            'TaiwanDollar('
            f'amount: {result}, '
            'alpha_code: "TWD", '
            'numeric_code: "901", '
            'symbol: "$", '
            'localized_symbol: "TW$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_taiwan_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = TaiwanDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'TWD'
        assert custom.numeric_code == '901'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'TW$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'TWD',
            '901'))
        assert custom.__repr__() == (
            'TaiwanDollar('
            f'amount: {amount}, '
            'alpha_code: "TWD", '
            'numeric_code: "901", '
            'symbol: "$", '
            'localized_symbol: "TW$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_taiwan_dollar_recreate(amount, new_amount):
        default = TaiwanDollar(amount)
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
    def test_taiwan_dollar_change_attributes(attribute, value):
        immutable = TaiwanDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'TaiwanDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_taiwan_dollar_add_attributes(attribute, value):
        immutable = TaiwanDollar(1000)
        with raises(
                AttributeError,
                match=f'\'TaiwanDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (taiwan_dollar_one, taiwan_dollar_one, taiwan_dollar_two, None),
        (taiwan_dollar_one, taiwan_dollar_one_other, taiwan_dollar_two, None),
        (taiwan_dollar_two, taiwan_dollar_minus_one, taiwan_dollar_one, None),
        (taiwan_dollar_one, other, None, CurrencyMismatchException),
        (taiwan_dollar_one, 1.00, None, CurrencyTypeException),
        (taiwan_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_taiwan_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (taiwan_dollar_one)
    ])
    def test_taiwan_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'TWD'
        assert new.numeric_code == '901'
        assert new.symbol == '$'
        assert new.localized_symbol == 'TW$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollar:
    """US Dollar currency tests."""

    us_dollar_minus_one = USDollar(-1)
    us_dollar_one_other = USDollar(1)
    us_dollar_one = USDollar(1)
    us_dollar_two = USDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_default(amount, result, printed):
        default = USDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'US$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollar('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "US$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'US$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollar('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "US$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_recreate(amount, new_amount):
        default = USDollar(amount)
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
    def test_us_dollar_change_attributes(attribute, value):
        immutable = USDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_add_attributes(attribute, value):
        immutable = USDollar(1000)
        with raises(
                AttributeError,
                match=f'\'USDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_one, us_dollar_one, us_dollar_two, None),
        (us_dollar_one, us_dollar_one_other, us_dollar_two, None),
        (us_dollar_two, us_dollar_minus_one, us_dollar_one, None),
        (us_dollar_one, other, None, CurrencyMismatchException),
        (us_dollar_one, 1.00, None, CurrencyTypeException),
        (us_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_one)
    ])
    def test_us_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'US$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarAS:
    """US Dollar AS currency tests."""

    us_dollar_as_minus_one = USDollarAS(-1)
    us_dollar_as_one_other = USDollarAS(1)
    us_dollar_as_one = USDollarAS(1)
    us_dollar_as_two = USDollarAS(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_as_default(amount, result, printed):
        default = USDollarAS(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'AS$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarAS('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "AS$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_as_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarAS(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'AS$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarAS('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "AS$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_as_recreate(amount, new_amount):
        default = USDollarAS(amount)
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
    def test_us_dollar_as_change_attributes(attribute, value):
        immutable = USDollarAS(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarAS\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_as_add_attributes(attribute, value):
        immutable = USDollarAS(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarAS\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_as_one, us_dollar_as_one, us_dollar_as_two, None),
        (us_dollar_as_one, us_dollar_as_one_other, us_dollar_as_two, None),
        (us_dollar_as_two, us_dollar_as_minus_one, us_dollar_as_one, None),
        (us_dollar_as_one, other, None, CurrencyMismatchException),
        (us_dollar_as_one, 1.00, None, CurrencyTypeException),
        (us_dollar_as_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_as_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_as_one)
    ])
    def test_us_dollar_as_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'AS$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarIO:
    """US Dollar IO currency tests."""

    us_dollar_io_minus_one = USDollarIO(-1)
    us_dollar_io_one_other = USDollarIO(1)
    us_dollar_io_one = USDollarIO(1)
    us_dollar_io_two = USDollarIO(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_io_default(amount, result, printed):
        default = USDollarIO(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'IO$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarIO('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "IO$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_io_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarIO(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'IO$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarIO('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "IO$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_io_recreate(amount, new_amount):
        default = USDollarIO(amount)
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
    def test_us_dollar_io_change_attributes(attribute, value):
        immutable = USDollarIO(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarIO\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_io_add_attributes(attribute, value):
        immutable = USDollarIO(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarIO\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_io_one, us_dollar_io_one, us_dollar_io_two, None),
        (us_dollar_io_one, us_dollar_io_one_other, us_dollar_io_two, None),
        (us_dollar_io_two, us_dollar_io_minus_one, us_dollar_io_one, None),
        (us_dollar_io_one, other, None, CurrencyMismatchException),
        (us_dollar_io_one, 1.00, None, CurrencyTypeException),
        (us_dollar_io_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_io_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_io_one)
    ])
    def test_us_dollar_io_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'IO$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarVG:
    """US Dollar VG currency tests."""

    us_dollar_vg_minus_one = USDollarVG(-1)
    us_dollar_vg_one_other = USDollarVG(1)
    us_dollar_vg_one = USDollarVG(1)
    us_dollar_vg_two = USDollarVG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_vg_default(amount, result, printed):
        default = USDollarVG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'VG$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarVG('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "VG$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_vg_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarVG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'VG$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarVG('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "VG$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_vg_recreate(amount, new_amount):
        default = USDollarVG(amount)
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
    def test_us_dollar_vg_change_attributes(attribute, value):
        immutable = USDollarVG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarVG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_vg_add_attributes(attribute, value):
        immutable = USDollarVG(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarVG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_vg_one, us_dollar_vg_one, us_dollar_vg_two, None),
        (us_dollar_vg_one, us_dollar_vg_one_other, us_dollar_vg_two, None),
        (us_dollar_vg_two, us_dollar_vg_minus_one, us_dollar_vg_one, None),
        (us_dollar_vg_one, other, None, CurrencyMismatchException),
        (us_dollar_vg_one, 1.00, None, CurrencyTypeException),
        (us_dollar_vg_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_vg_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_vg_one)
    ])
    def test_us_dollar_vg_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'VG$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarGU:
    """US Dollar GU currency tests."""

    us_dollar_gu_minus_one = USDollarGU(-1)
    us_dollar_gu_one_other = USDollarGU(1)
    us_dollar_gu_one = USDollarGU(1)
    us_dollar_gu_two = USDollarGU(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_gu_default(amount, result, printed):
        default = USDollarGU(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'GU$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarGU('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "GU$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_gu_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarGU(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'GU$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarGU('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "GU$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_gu_recreate(amount, new_amount):
        default = USDollarGU(amount)
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
    def test_us_dollar_gu_change_attributes(attribute, value):
        immutable = USDollarGU(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarGU\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_gu_add_attributes(attribute, value):
        immutable = USDollarGU(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarGU\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_gu_one, us_dollar_gu_one, us_dollar_gu_two, None),
        (us_dollar_gu_one, us_dollar_gu_one_other, us_dollar_gu_two, None),
        (us_dollar_gu_two, us_dollar_gu_minus_one, us_dollar_gu_one, None),
        (us_dollar_gu_one, other, None, CurrencyMismatchException),
        (us_dollar_gu_one, 1.00, None, CurrencyTypeException),
        (us_dollar_gu_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_gu_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_gu_one)
    ])
    def test_us_dollar_gu_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'GU$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarHT:
    """US Dollar HT currency tests."""

    us_dollar_ht_minus_one = USDollarHT(-1)
    us_dollar_ht_one_other = USDollarHT(1)
    us_dollar_ht_one = USDollarHT(1)
    us_dollar_ht_two = USDollarHT(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_ht_default(amount, result, printed):
        default = USDollarHT(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'HT$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarHT('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "HT$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_ht_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarHT(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'HT$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarHT('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "HT$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_ht_recreate(amount, new_amount):
        default = USDollarHT(amount)
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
    def test_us_dollar_ht_change_attributes(attribute, value):
        immutable = USDollarHT(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarHT\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_ht_add_attributes(attribute, value):
        immutable = USDollarHT(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarHT\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_ht_one, us_dollar_ht_one, us_dollar_ht_two, None),
        (us_dollar_ht_one, us_dollar_ht_one_other, us_dollar_ht_two, None),
        (us_dollar_ht_two, us_dollar_ht_minus_one, us_dollar_ht_one, None),
        (us_dollar_ht_one, other, None, CurrencyMismatchException),
        (us_dollar_ht_one, 1.00, None, CurrencyTypeException),
        (us_dollar_ht_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_ht_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_ht_one)
    ])
    def test_us_dollar_ht_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'HT$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarMH:
    """US Dollar MH currency tests."""

    us_dollar_mh_minus_one = USDollarMH(-1)
    us_dollar_mh_one_other = USDollarMH(1)
    us_dollar_mh_one = USDollarMH(1)
    us_dollar_mh_two = USDollarMH(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_mh_default(amount, result, printed):
        default = USDollarMH(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'MH$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarMH('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "MH$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_mh_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarMH(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'MH$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarMH('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "MH$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_mh_recreate(amount, new_amount):
        default = USDollarMH(amount)
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
    def test_us_dollar_mh_change_attributes(attribute, value):
        immutable = USDollarMH(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarMH\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_mh_add_attributes(attribute, value):
        immutable = USDollarMH(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarMH\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_mh_one, us_dollar_mh_one, us_dollar_mh_two, None),
        (us_dollar_mh_one, us_dollar_mh_one_other, us_dollar_mh_two, None),
        (us_dollar_mh_two, us_dollar_mh_minus_one, us_dollar_mh_one, None),
        (us_dollar_mh_one, other, None, CurrencyMismatchException),
        (us_dollar_mh_one, 1.00, None, CurrencyTypeException),
        (us_dollar_mh_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_mh_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_mh_one)
    ])
    def test_us_dollar_mh_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'MH$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarFM:
    """US Dollar FM currency tests."""

    us_dollar_fm_minus_one = USDollarFM(-1)
    us_dollar_fm_one_other = USDollarFM(1)
    us_dollar_fm_one = USDollarFM(1)
    us_dollar_fm_two = USDollarFM(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_fm_default(amount, result, printed):
        default = USDollarFM(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'FM$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarFM('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "FM$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_fm_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarFM(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'FM$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarFM('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "FM$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_fm_recreate(amount, new_amount):
        default = USDollarFM(amount)
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
    def test_us_dollar_fm_change_attributes(attribute, value):
        immutable = USDollarFM(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarFM\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_fm_add_attributes(attribute, value):
        immutable = USDollarFM(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarFM\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_fm_one, us_dollar_fm_one, us_dollar_fm_two, None),
        (us_dollar_fm_one, us_dollar_fm_one_other, us_dollar_fm_two, None),
        (us_dollar_fm_two, us_dollar_fm_minus_one, us_dollar_fm_one, None),
        (us_dollar_fm_one, other, None, CurrencyMismatchException),
        (us_dollar_fm_one, 1.00, None, CurrencyTypeException),
        (us_dollar_fm_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_fm_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_fm_one)
    ])
    def test_us_dollar_fm_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'FM$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarMP:
    """US Dollar MP currency tests."""

    us_dollar_mp_minus_one = USDollarMP(-1)
    us_dollar_mp_one_other = USDollarMP(1)
    us_dollar_mp_one = USDollarMP(1)
    us_dollar_mp_two = USDollarMP(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_mp_default(amount, result, printed):
        default = USDollarMP(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'MP$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarMP('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "MP$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_mp_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarMP(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'MP$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarMP('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "MP$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_mp_recreate(amount, new_amount):
        default = USDollarMP(amount)
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
    def test_us_dollar_mp_change_attributes(attribute, value):
        immutable = USDollarMP(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarMP\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_mp_add_attributes(attribute, value):
        immutable = USDollarMP(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarMP\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_mp_one, us_dollar_mp_one, us_dollar_mp_two, None),
        (us_dollar_mp_one, us_dollar_mp_one_other, us_dollar_mp_two, None),
        (us_dollar_mp_two, us_dollar_mp_minus_one, us_dollar_mp_one, None),
        (us_dollar_mp_one, other, None, CurrencyMismatchException),
        (us_dollar_mp_one, 1.00, None, CurrencyTypeException),
        (us_dollar_mp_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_mp_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_mp_one)
    ])
    def test_us_dollar_mp_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'MP$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarPC:
    """US Dollar PC currency tests."""

    us_dollar_pc_minus_one = USDollarPC(-1)
    us_dollar_pc_one_other = USDollarPC(1)
    us_dollar_pc_one = USDollarPC(1)
    us_dollar_pc_two = USDollarPC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_pc_default(amount, result, printed):
        default = USDollarPC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'PC$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarPC('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PC$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_pc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarPC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'PC$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarPC('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PC$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_pc_recreate(amount, new_amount):
        default = USDollarPC(amount)
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
    def test_us_dollar_pc_change_attributes(attribute, value):
        immutable = USDollarPC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarPC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_pc_add_attributes(attribute, value):
        immutable = USDollarPC(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarPC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_pc_one, us_dollar_pc_one, us_dollar_pc_two, None),
        (us_dollar_pc_one, us_dollar_pc_one_other, us_dollar_pc_two, None),
        (us_dollar_pc_two, us_dollar_pc_minus_one, us_dollar_pc_one, None),
        (us_dollar_pc_one, other, None, CurrencyMismatchException),
        (us_dollar_pc_one, 1.00, None, CurrencyTypeException),
        (us_dollar_pc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_pc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_pc_one)
    ])
    def test_us_dollar_pc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'PC$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarPW:
    """US Dollar PW currency tests."""

    us_dollar_pw_minus_one = USDollarPW(-1)
    us_dollar_pw_one_other = USDollarPW(1)
    us_dollar_pw_one = USDollarPW(1)
    us_dollar_pw_two = USDollarPW(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_pw_default(amount, result, printed):
        default = USDollarPW(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'PW$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarPW('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PW$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_pw_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarPW(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'PW$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarPW('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PW$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_pw_recreate(amount, new_amount):
        default = USDollarPW(amount)
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
    def test_us_dollar_pw_change_attributes(attribute, value):
        immutable = USDollarPW(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarPW\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_pw_add_attributes(attribute, value):
        immutable = USDollarPW(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarPW\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_pw_one, us_dollar_pw_one, us_dollar_pw_two, None),
        (us_dollar_pw_one, us_dollar_pw_one_other, us_dollar_pw_two, None),
        (us_dollar_pw_two, us_dollar_pw_minus_one, us_dollar_pw_one, None),
        (us_dollar_pw_one, other, None, CurrencyMismatchException),
        (us_dollar_pw_one, 1.00, None, CurrencyTypeException),
        (us_dollar_pw_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_pw_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_pw_one)
    ])
    def test_us_dollar_pw_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'PW$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarPA:
    """US Dollar PA currency tests."""

    us_dollar_pa_minus_one = USDollarPA(-1)
    us_dollar_pa_one_other = USDollarPA(1)
    us_dollar_pa_one = USDollarPA(1)
    us_dollar_pa_two = USDollarPA(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_pa_default(amount, result, printed):
        default = USDollarPA(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'PA$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarPA('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PA$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_pa_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarPA(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'PA$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarPA('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PA$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_pa_recreate(amount, new_amount):
        default = USDollarPA(amount)
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
    def test_us_dollar_pa_change_attributes(attribute, value):
        immutable = USDollarPA(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarPA\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_pa_add_attributes(attribute, value):
        immutable = USDollarPA(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarPA\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_pa_one, us_dollar_pa_one, us_dollar_pa_two, None),
        (us_dollar_pa_one, us_dollar_pa_one_other, us_dollar_pa_two, None),
        (us_dollar_pa_two, us_dollar_pa_minus_one, us_dollar_pa_one, None),
        (us_dollar_pa_one, other, None, CurrencyMismatchException),
        (us_dollar_pa_one, 1.00, None, CurrencyTypeException),
        (us_dollar_pa_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_pa_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_pa_one)
    ])
    def test_us_dollar_pa_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'PA$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarPR:
    """US Dollar PR currency tests."""

    us_dollar_pr_minus_one = USDollarPR(-1)
    us_dollar_pr_one_other = USDollarPR(1)
    us_dollar_pr_one = USDollarPR(1)
    us_dollar_pr_two = USDollarPR(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_pr_default(amount, result, printed):
        default = USDollarPR(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'PR$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarPR('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PR$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_pr_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarPR(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'PR$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarPR('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "PR$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_pr_recreate(amount, new_amount):
        default = USDollarPR(amount)
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
    def test_us_dollar_pr_change_attributes(attribute, value):
        immutable = USDollarPR(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarPR\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_pr_add_attributes(attribute, value):
        immutable = USDollarPR(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarPR\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_pr_one, us_dollar_pr_one, us_dollar_pr_two, None),
        (us_dollar_pr_one, us_dollar_pr_one_other, us_dollar_pr_two, None),
        (us_dollar_pr_two, us_dollar_pr_minus_one, us_dollar_pr_one, None),
        (us_dollar_pr_one, other, None, CurrencyMismatchException),
        (us_dollar_pr_one, 1.00, None, CurrencyTypeException),
        (us_dollar_pr_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_pr_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_pr_one)
    ])
    def test_us_dollar_pr_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'PR$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarTC:
    """US Dollar TC currency tests."""

    us_dollar_tc_minus_one = USDollarTC(-1)
    us_dollar_tc_one_other = USDollarTC(1)
    us_dollar_tc_one = USDollarTC(1)
    us_dollar_tc_two = USDollarTC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_tc_default(amount, result, printed):
        default = USDollarTC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'TC$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarTC('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "TC$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_tc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarTC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'TC$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarTC('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "TC$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_tc_recreate(amount, new_amount):
        default = USDollarTC(amount)
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
    def test_us_dollar_tc_change_attributes(attribute, value):
        immutable = USDollarTC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarTC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_tc_add_attributes(attribute, value):
        immutable = USDollarTC(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarTC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_tc_one, us_dollar_tc_one, us_dollar_tc_two, None),
        (us_dollar_tc_one, us_dollar_tc_one_other, us_dollar_tc_two, None),
        (us_dollar_tc_two, us_dollar_tc_minus_one, us_dollar_tc_one, None),
        (us_dollar_tc_one, other, None, CurrencyMismatchException),
        (us_dollar_tc_one, 1.00, None, CurrencyTypeException),
        (us_dollar_tc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_tc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_tc_one)
    ])
    def test_us_dollar_tc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'TC$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestUSDollarVI:
    """US Dollar VI currency tests."""

    us_dollar_vi_minus_one = USDollarVI(-1)
    us_dollar_vi_one_other = USDollarVI(1)
    us_dollar_vi_one = USDollarVI(1)
    us_dollar_vi_two = USDollarVI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_us_dollar_vi_default(amount, result, printed):
        default = USDollarVI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'USD'
        assert default.numeric_code == '840'
        assert default.symbol == '$'
        assert default.localized_symbol == 'VI$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert default.__repr__() == (
            'USDollarVI('
            f'amount: {result}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "VI$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_us_dollar_vi_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = USDollarVI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'USD'
        assert custom.numeric_code == '840'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'VI$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'USD',
            '840'))
        assert custom.__repr__() == (
            'USDollarVI('
            f'amount: {amount}, '
            'alpha_code: "USD", '
            'numeric_code: "840", '
            'symbol: "$", '
            'localized_symbol: "VI$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_us_dollar_vi_recreate(amount, new_amount):
        default = USDollarVI(amount)
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
    def test_us_dollar_vi_change_attributes(attribute, value):
        immutable = USDollarVI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'USDollarVI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_us_dollar_vi_add_attributes(attribute, value):
        immutable = USDollarVI(1000)
        with raises(
                AttributeError,
                match=f'\'USDollarVI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (us_dollar_vi_one, us_dollar_vi_one, us_dollar_vi_two, None),
        (us_dollar_vi_one, us_dollar_vi_one_other, us_dollar_vi_two, None),
        (us_dollar_vi_two, us_dollar_vi_minus_one, us_dollar_vi_one, None),
        (us_dollar_vi_one, other, None, CurrencyMismatchException),
        (us_dollar_vi_one, 1.00, None, CurrencyTypeException),
        (us_dollar_vi_one, '1.00', None, CurrencyTypeException)
    ])
    def test_us_dollar_vi_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (us_dollar_vi_one)
    ])
    def test_us_dollar_vi_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'USD'
        assert new.numeric_code == '840'
        assert new.symbol == '$'
        assert new.localized_symbol == 'VI$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollar:
    """Eastern Caribbean Dollar currency tests."""

    eastern_caribbean_dollar_minus_one = EasternCaribbeanDollar(-1)
    eastern_caribbean_dollar_one_other = EasternCaribbeanDollar(1)
    eastern_caribbean_dollar_one = EasternCaribbeanDollar(1)
    eastern_caribbean_dollar_two = EasternCaribbeanDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_default(amount, result, printed):
        default = EasternCaribbeanDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == '$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollar('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == '$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollar('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_recreate(amount, new_amount):
        default = EasternCaribbeanDollar(amount)
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
    def test_eastern_caribbean_dollar_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollar(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_one, eastern_caribbean_dollar_one, eastern_caribbean_dollar_two, None),
        (eastern_caribbean_dollar_one, eastern_caribbean_dollar_one_other, eastern_caribbean_dollar_two, None),
        (eastern_caribbean_dollar_two, eastern_caribbean_dollar_minus_one, eastern_caribbean_dollar_one, None),
        (eastern_caribbean_dollar_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_one)
    ])
    def test_eastern_caribbean_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == '$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarAI:
    """Eastern Caribbean Dollar AI currency tests."""

    eastern_caribbean_dollar_ai_minus_one = EasternCaribbeanDollarAI(-1)
    eastern_caribbean_dollar_ai_one_other = EasternCaribbeanDollarAI(1)
    eastern_caribbean_dollar_ai_one = EasternCaribbeanDollarAI(1)
    eastern_caribbean_dollar_ai_two = EasternCaribbeanDollarAI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_ai_default(amount, result, printed):
        default = EasternCaribbeanDollarAI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'AI$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarAI('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "AI$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_ai_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarAI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'AI$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarAI('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "AI$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_ai_recreate(amount, new_amount):
        default = EasternCaribbeanDollarAI(amount)
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
    def test_eastern_caribbean_dollar_ai_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarAI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarAI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_ai_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarAI(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarAI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_ai_one, eastern_caribbean_dollar_ai_one, eastern_caribbean_dollar_ai_two, None),
        (eastern_caribbean_dollar_ai_one, eastern_caribbean_dollar_ai_one_other, eastern_caribbean_dollar_ai_two, None),
        (eastern_caribbean_dollar_ai_two, eastern_caribbean_dollar_ai_minus_one, eastern_caribbean_dollar_ai_one, None),
        (eastern_caribbean_dollar_ai_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_ai_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_ai_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_ai_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_ai_one)
    ])
    def test_eastern_caribbean_dollar_ai_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'AI$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarAG:
    """Eastern Caribbean Dollar AG currency tests."""

    eastern_caribbean_dollar_ag_minus_one = EasternCaribbeanDollarAG(-1)
    eastern_caribbean_dollar_ag_one_other = EasternCaribbeanDollarAG(1)
    eastern_caribbean_dollar_ag_one = EasternCaribbeanDollarAG(1)
    eastern_caribbean_dollar_ag_two = EasternCaribbeanDollarAG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_ag_default(amount, result, printed):
        default = EasternCaribbeanDollarAG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'AG$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarAG('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "AG$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_ag_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarAG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'AG$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarAG('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "AG$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_ag_recreate(amount, new_amount):
        default = EasternCaribbeanDollarAG(amount)
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
    def test_eastern_caribbean_dollar_ag_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarAG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarAG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_ag_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarAG(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarAG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_ag_one, eastern_caribbean_dollar_ag_one, eastern_caribbean_dollar_ag_two, None),
        (eastern_caribbean_dollar_ag_one, eastern_caribbean_dollar_ag_one_other, eastern_caribbean_dollar_ag_two, None),
        (eastern_caribbean_dollar_ag_two, eastern_caribbean_dollar_ag_minus_one, eastern_caribbean_dollar_ag_one, None),
        (eastern_caribbean_dollar_ag_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_ag_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_ag_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_ag_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_ag_one)
    ])
    def test_eastern_caribbean_dollar_ag_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'AG$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarDM:
    """Eastern Caribbean Dollar DM currency tests."""

    eastern_caribbean_dollar_dm_minus_one = EasternCaribbeanDollarDM(-1)
    eastern_caribbean_dollar_dm_one_other = EasternCaribbeanDollarDM(1)
    eastern_caribbean_dollar_dm_one = EasternCaribbeanDollarDM(1)
    eastern_caribbean_dollar_dm_two = EasternCaribbeanDollarDM(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_dm_default(amount, result, printed):
        default = EasternCaribbeanDollarDM(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'DM$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarDM('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "DM$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_dm_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarDM(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'DM$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarDM('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "DM$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_dm_recreate(amount, new_amount):
        default = EasternCaribbeanDollarDM(amount)
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
    def test_eastern_caribbean_dollar_dm_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarDM(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarDM\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_dm_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarDM(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarDM\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_dm_one, eastern_caribbean_dollar_dm_one, eastern_caribbean_dollar_dm_two, None),
        (eastern_caribbean_dollar_dm_one, eastern_caribbean_dollar_dm_one_other, eastern_caribbean_dollar_dm_two, None),
        (eastern_caribbean_dollar_dm_two, eastern_caribbean_dollar_dm_minus_one, eastern_caribbean_dollar_dm_one, None),
        (eastern_caribbean_dollar_dm_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_dm_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_dm_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_dm_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_dm_one)
    ])
    def test_eastern_caribbean_dollar_dm_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'DM$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarGD:
    """Eastern Caribbean Dollar GD currency tests."""

    eastern_caribbean_dollar_gd_minus_one = EasternCaribbeanDollarGD(-1)
    eastern_caribbean_dollar_gd_one_other = EasternCaribbeanDollarGD(1)
    eastern_caribbean_dollar_gd_one = EasternCaribbeanDollarGD(1)
    eastern_caribbean_dollar_gd_two = EasternCaribbeanDollarGD(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_gd_default(amount, result, printed):
        default = EasternCaribbeanDollarGD(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'GD$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarGD('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "GD$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_gd_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarGD(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'GD$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarGD('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "GD$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_gd_recreate(amount, new_amount):
        default = EasternCaribbeanDollarGD(amount)
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
    def test_eastern_caribbean_dollar_gd_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarGD(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarGD\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_gd_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarGD(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarGD\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_gd_one, eastern_caribbean_dollar_gd_one, eastern_caribbean_dollar_gd_two, None),
        (eastern_caribbean_dollar_gd_one, eastern_caribbean_dollar_gd_one_other, eastern_caribbean_dollar_gd_two, None),
        (eastern_caribbean_dollar_gd_two, eastern_caribbean_dollar_gd_minus_one, eastern_caribbean_dollar_gd_one, None),
        (eastern_caribbean_dollar_gd_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_gd_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_gd_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_gd_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_gd_one)
    ])
    def test_eastern_caribbean_dollar_gd_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'GD$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarMS:
    """Eastern Caribbean Dollar MS currency tests."""

    eastern_caribbean_dollar_ms_minus_one = EasternCaribbeanDollarMS(-1)
    eastern_caribbean_dollar_ms_one_other = EasternCaribbeanDollarMS(1)
    eastern_caribbean_dollar_ms_one = EasternCaribbeanDollarMS(1)
    eastern_caribbean_dollar_ms_two = EasternCaribbeanDollarMS(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_ms_default(amount, result, printed):
        default = EasternCaribbeanDollarMS(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'MS$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarMS('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "MS$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_ms_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarMS(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'MS$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarMS('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "MS$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_ms_recreate(amount, new_amount):
        default = EasternCaribbeanDollarMS(amount)
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
    def test_eastern_caribbean_dollar_ms_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarMS(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarMS\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_ms_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarMS(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarMS\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_ms_one, eastern_caribbean_dollar_ms_one, eastern_caribbean_dollar_ms_two, None),
        (eastern_caribbean_dollar_ms_one, eastern_caribbean_dollar_ms_one_other, eastern_caribbean_dollar_ms_two, None),
        (eastern_caribbean_dollar_ms_two, eastern_caribbean_dollar_ms_minus_one, eastern_caribbean_dollar_ms_one, None),
        (eastern_caribbean_dollar_ms_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_ms_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_ms_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_ms_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_ms_one)
    ])
    def test_eastern_caribbean_dollar_ms_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'MS$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarKN:
    """Eastern Caribbean Dollar KN currency tests."""

    eastern_caribbean_dollar_kn_minus_one = EasternCaribbeanDollarKN(-1)
    eastern_caribbean_dollar_kn_one_other = EasternCaribbeanDollarKN(1)
    eastern_caribbean_dollar_kn_one = EasternCaribbeanDollarKN(1)
    eastern_caribbean_dollar_kn_two = EasternCaribbeanDollarKN(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_kn_default(amount, result, printed):
        default = EasternCaribbeanDollarKN(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'KN$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarKN('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "KN$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_kn_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarKN(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'KN$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarKN('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "KN$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_kn_recreate(amount, new_amount):
        default = EasternCaribbeanDollarKN(amount)
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
    def test_eastern_caribbean_dollar_kn_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarKN(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarKN\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_kn_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarKN(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarKN\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_kn_one, eastern_caribbean_dollar_kn_one, eastern_caribbean_dollar_kn_two, None),
        (eastern_caribbean_dollar_kn_one, eastern_caribbean_dollar_kn_one_other, eastern_caribbean_dollar_kn_two, None),
        (eastern_caribbean_dollar_kn_two, eastern_caribbean_dollar_kn_minus_one, eastern_caribbean_dollar_kn_one, None),
        (eastern_caribbean_dollar_kn_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_kn_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_kn_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_kn_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_kn_one)
    ])
    def test_eastern_caribbean_dollar_kn_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'KN$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarLC:
    """Eastern Caribbean Dollar LC currency tests."""

    eastern_caribbean_dollar_lc_minus_one = EasternCaribbeanDollarLC(-1)
    eastern_caribbean_dollar_lc_one_other = EasternCaribbeanDollarLC(1)
    eastern_caribbean_dollar_lc_one = EasternCaribbeanDollarLC(1)
    eastern_caribbean_dollar_lc_two = EasternCaribbeanDollarLC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_lc_default(amount, result, printed):
        default = EasternCaribbeanDollarLC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'LC$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarLC('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "LC$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_lc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarLC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'LC$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarLC('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "LC$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_lc_recreate(amount, new_amount):
        default = EasternCaribbeanDollarLC(amount)
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
    def test_eastern_caribbean_dollar_lc_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarLC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarLC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_lc_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarLC(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarLC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_lc_one, eastern_caribbean_dollar_lc_one, eastern_caribbean_dollar_lc_two, None),
        (eastern_caribbean_dollar_lc_one, eastern_caribbean_dollar_lc_one_other, eastern_caribbean_dollar_lc_two, None),
        (eastern_caribbean_dollar_lc_two, eastern_caribbean_dollar_lc_minus_one, eastern_caribbean_dollar_lc_one, None),
        (eastern_caribbean_dollar_lc_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_lc_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_lc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_lc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_lc_one)
    ])
    def test_eastern_caribbean_dollar_lc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'LC$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestEasternCaribbeanDollarVC:
    """Eastern Caribbean Dollar VC currency tests."""

    eastern_caribbean_dollar_vc_minus_one = EasternCaribbeanDollarVC(-1)
    eastern_caribbean_dollar_vc_one_other = EasternCaribbeanDollarVC(1)
    eastern_caribbean_dollar_vc_one = EasternCaribbeanDollarVC(1)
    eastern_caribbean_dollar_vc_two = EasternCaribbeanDollarVC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$3.14'),
        (10, '10', '$10.00'),
        (Decimal('10'), '10', '$10.00'),
        ('-3.14', '-3.14', '-$3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-$3.14'),
        (-10, '-10', '-$10.00'),
        (Decimal('-10'), '-10', '-$10.00')
    ])
    def test_eastern_caribbean_dollar_vc_default(amount, result, printed):
        default = EasternCaribbeanDollarVC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XCD'
        assert default.numeric_code == '951'
        assert default.symbol == '$'
        assert default.localized_symbol == 'VC$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert default.__repr__() == (
            'EasternCaribbeanDollarVC('
            f'amount: {result}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "VC$", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_eastern_caribbean_dollar_vc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EasternCaribbeanDollarVC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XCD'
        assert custom.numeric_code == '951'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'VC$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XCD',
            '951'))
        assert custom.__repr__() == (
            'EasternCaribbeanDollarVC('
            f'amount: {amount}, '
            'alpha_code: "XCD", '
            'numeric_code: "951", '
            'symbol: "$", '
            'localized_symbol: "VC$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eastern_caribbean_dollar_vc_recreate(amount, new_amount):
        default = EasternCaribbeanDollarVC(amount)
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
    def test_eastern_caribbean_dollar_vc_change_attributes(attribute, value):
        immutable = EasternCaribbeanDollarVC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EasternCaribbeanDollarVC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eastern_caribbean_dollar_vc_add_attributes(attribute, value):
        immutable = EasternCaribbeanDollarVC(1000)
        with raises(
                AttributeError,
                match=f'\'EasternCaribbeanDollarVC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eastern_caribbean_dollar_vc_one, eastern_caribbean_dollar_vc_one, eastern_caribbean_dollar_vc_two, None),
        (eastern_caribbean_dollar_vc_one, eastern_caribbean_dollar_vc_one_other, eastern_caribbean_dollar_vc_two, None),
        (eastern_caribbean_dollar_vc_two, eastern_caribbean_dollar_vc_minus_one, eastern_caribbean_dollar_vc_one, None),
        (eastern_caribbean_dollar_vc_one, other, None, CurrencyMismatchException),
        (eastern_caribbean_dollar_vc_one, 1.00, None, CurrencyTypeException),
        (eastern_caribbean_dollar_vc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eastern_caribbean_dollar_vc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eastern_caribbean_dollar_vc_one)
    ])
    def test_eastern_caribbean_dollar_vc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XCD'
        assert new.numeric_code == '951'
        assert new.symbol == '$'
        assert new.localized_symbol == 'VC$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestZimbabweDollar:
    """Zimbabwe Dollar currency tests."""

    zimbabwe_dollar_minus_one = ZimbabweDollar(-1)
    zimbabwe_dollar_one_other = ZimbabweDollar(1)
    zimbabwe_dollar_one = ZimbabweDollar(1)
    zimbabwe_dollar_two = ZimbabweDollar(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '$\xa03.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '$\xa03.14'),
        (10, '10', '$\xa010.00'),
        (Decimal('10'), '10', '$\xa010.00'),
        ('-3.14', '-3.14', '$\xa0-3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '$\xa0-3.14'),
        (-10, '-10', '$\xa0-10.00'),
        (Decimal('-10'), '-10', '$\xa0-10.00')
    ])
    def test_zimbabwe_dollar_default(amount, result, printed):
        default = ZimbabweDollar(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZWL'
        assert default.numeric_code == '932'
        assert default.symbol == '$'
        assert default.localized_symbol == 'ZW$'
        assert default.convertion == ''
        assert default.pattern == '2.,3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZWL',
            '932'))
        assert default.__repr__() == (
            'ZimbabweDollar('
            f'amount: {result}, '
            'alpha_code: "ZWL", '
            'numeric_code: "932", '
            'symbol: "$", '
            'localized_symbol: "ZW$", '
            'convertion: "", '
            'pattern: "2.,3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '$10.00,00000'),
        (-1000, '$10.00,00000-')
    ])
    def test_zimbabwe_dollar_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ZimbabweDollar(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZWL'
        assert custom.numeric_code == '932'
        assert custom.symbol == '$'
        assert custom.localized_symbol == 'ZW$'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZWL',
            '932'))
        assert custom.__repr__() == (
            'ZimbabweDollar('
            f'amount: {amount}, '
            'alpha_code: "ZWL", '
            'numeric_code: "932", '
            'symbol: "$", '
            'localized_symbol: "ZW$", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_zimbabwe_dollar_recreate(amount, new_amount):
        default = ZimbabweDollar(amount)
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
    def test_zimbabwe_dollar_change_attributes(attribute, value):
        immutable = ZimbabweDollar(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'ZimbabweDollar\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_zimbabwe_dollar_add_attributes(attribute, value):
        immutable = ZimbabweDollar(1000)
        with raises(
                AttributeError,
                match=f'\'ZimbabweDollar\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (zimbabwe_dollar_one, zimbabwe_dollar_one, zimbabwe_dollar_two, None),
        (zimbabwe_dollar_one, zimbabwe_dollar_one_other, zimbabwe_dollar_two, None),
        (zimbabwe_dollar_two, zimbabwe_dollar_minus_one, zimbabwe_dollar_one, None),
        (zimbabwe_dollar_one, other, None, CurrencyMismatchException),
        (zimbabwe_dollar_one, 1.00, None, CurrencyTypeException),
        (zimbabwe_dollar_one, '1.00', None, CurrencyTypeException)
    ])
    def test_zimbabwe_dollar_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (zimbabwe_dollar_one)
    ])
    def test_zimbabwe_dollar_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZWL'
        assert new.numeric_code == '932'
        assert new.symbol == '$'
        assert new.localized_symbol == 'ZW$'
        assert new.convertion == ''
        assert new.pattern == '2.,3%s\u00A0%a'
