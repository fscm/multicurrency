# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Pound currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.pound import (
    EgyptianPound,
    FalklandIslandsPound,
    PoundSterling,
    PoundSterlingGG,
    PoundSterlingIO,
    PoundSterlingGB,
    PoundSterlingIM,
    GibraltarPound,
    LebanesePound,
    SudanesePound,
    SaintHelenaPoundAI,
    SaintHelenaPound,
    SaintHelenaPoundTC,
    SyrianPound)


class TestEgyptianPound:
    """Egyptian Pound currency tests."""

    egyptian_pound_minus_one = EgyptianPound(-1)
    egyptian_pound_one_other = EgyptianPound(1)
    egyptian_pound_one = EgyptianPound(1)
    egyptian_pound_two = EgyptianPound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ج.م.\xa0٣٫١٤'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ج.م.\xa0٣٫١٤'),
        (10, '10', 'ج.م.\xa0١٠٫٠٠'),
        (Decimal('10'), '10', 'ج.م.\xa0١٠٫٠٠'),
        ('-3.14', '-3.14', 'ج.م.\xa0-٣٫١٤'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ج.م.\xa0-٣٫١٤'),
        (-10, '-10', 'ج.م.\xa0-١٠٫٠٠'),
        (Decimal('-10'), '-10', 'ج.م.\xa0-١٠٫٠٠')
    ])
    def test_egyptian_pound_default(amount, result, printed):
        default = EgyptianPound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EGP'
        assert default.numeric_code == '818'
        assert default.symbol == 'ج.م.'
        assert default.localized_symbol == 'ج.م.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EGP',
            '818'))
        assert default.__repr__() == (
            'EgyptianPound('
            f'amount: {result}, '
            'alpha_code: "EGP", '
            'numeric_code: "818", '
            'symbol: "ج.م.", '
            'localized_symbol: "ج.م.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ج.م.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ج.م.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_egyptian_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EgyptianPound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EGP'
        assert custom.numeric_code == '818'
        assert custom.symbol == 'ج.م.'
        assert custom.localized_symbol == 'ج.م.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EGP',
            '818'))
        assert custom.__repr__() == (
            'EgyptianPound('
            f'amount: {amount}, '
            'alpha_code: "EGP", '
            'numeric_code: "818", '
            'symbol: "ج.م.", '
            'localized_symbol: "ج.م.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_egyptian_pound_recreate(amount, new_amount):
        default = EgyptianPound(amount)
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
    def test_egyptian_pound_change_attributes(attribute, value):
        immutable = EgyptianPound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EgyptianPound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_egyptian_pound_add_attributes(attribute, value):
        immutable = EgyptianPound(1000)
        with raises(
                AttributeError,
                match=f'\'EgyptianPound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (egyptian_pound_one, egyptian_pound_one, egyptian_pound_two, None),
        (egyptian_pound_one, egyptian_pound_one_other, egyptian_pound_two, None),
        (egyptian_pound_two, egyptian_pound_minus_one, egyptian_pound_one, None),
        (egyptian_pound_one, other, None, CurrencyMismatchException),
        (egyptian_pound_one, 1.00, None, CurrencyTypeException),
        (egyptian_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_egyptian_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (egyptian_pound_one)
    ])
    def test_egyptian_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EGP'
        assert new.numeric_code == '818'
        assert new.symbol == 'ج.م.'
        assert new.localized_symbol == 'ج.م.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%s\u00A0%a'


class TestFalklandIslandsPound:
    """Falkland Islands Pound currency tests."""

    falkland_islands_pound_minus_one = FalklandIslandsPound(-1)
    falkland_islands_pound_one_other = FalklandIslandsPound(1)
    falkland_islands_pound_one = FalklandIslandsPound(1)
    falkland_islands_pound_two = FalklandIslandsPound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_falkland_islands_pound_default(amount, result, printed):
        default = FalklandIslandsPound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'FKP'
        assert default.numeric_code == '238'
        assert default.symbol == '£'
        assert default.localized_symbol == 'FK£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'FKP',
            '238'))
        assert default.__repr__() == (
            'FalklandIslandsPound('
            f'amount: {result}, '
            'alpha_code: "FKP", '
            'numeric_code: "238", '
            'symbol: "£", '
            'localized_symbol: "FK£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_falkland_islands_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = FalklandIslandsPound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'FKP'
        assert custom.numeric_code == '238'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'FK£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'FKP',
            '238'))
        assert custom.__repr__() == (
            'FalklandIslandsPound('
            f'amount: {amount}, '
            'alpha_code: "FKP", '
            'numeric_code: "238", '
            'symbol: "£", '
            'localized_symbol: "FK£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_falkland_islands_pound_recreate(amount, new_amount):
        default = FalklandIslandsPound(amount)
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
    def test_falkland_islands_pound_change_attributes(attribute, value):
        immutable = FalklandIslandsPound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'FalklandIslandsPound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_falkland_islands_pound_add_attributes(attribute, value):
        immutable = FalklandIslandsPound(1000)
        with raises(
                AttributeError,
                match=f'\'FalklandIslandsPound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (falkland_islands_pound_one, falkland_islands_pound_one, falkland_islands_pound_two, None),
        (falkland_islands_pound_one, falkland_islands_pound_one_other, falkland_islands_pound_two, None),
        (falkland_islands_pound_two, falkland_islands_pound_minus_one, falkland_islands_pound_one, None),
        (falkland_islands_pound_one, other, None, CurrencyMismatchException),
        (falkland_islands_pound_one, 1.00, None, CurrencyTypeException),
        (falkland_islands_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_falkland_islands_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (falkland_islands_pound_one)
    ])
    def test_falkland_islands_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'FKP'
        assert new.numeric_code == '238'
        assert new.symbol == '£'
        assert new.localized_symbol == 'FK£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPoundSterling:
    """Pound Sterling currency tests."""

    pound_sterling_minus_one = PoundSterling(-1)
    pound_sterling_one_other = PoundSterling(1)
    pound_sterling_one = PoundSterling(1)
    pound_sterling_two = PoundSterling(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_pound_sterling_default(amount, result, printed):
        default = PoundSterling(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GBP'
        assert default.numeric_code == '826'
        assert default.symbol == '£'
        assert default.localized_symbol == '£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert default.__repr__() == (
            'PoundSterling('
            f'amount: {result}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_pound_sterling_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PoundSterling(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GBP'
        assert custom.numeric_code == '826'
        assert custom.symbol == '£'
        assert custom.localized_symbol == '£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert custom.__repr__() == (
            'PoundSterling('
            f'amount: {amount}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pound_sterling_recreate(amount, new_amount):
        default = PoundSterling(amount)
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
    def test_pound_sterling_change_attributes(attribute, value):
        immutable = PoundSterling(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PoundSterling\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pound_sterling_add_attributes(attribute, value):
        immutable = PoundSterling(1000)
        with raises(
                AttributeError,
                match=f'\'PoundSterling\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pound_sterling_one, pound_sterling_one, pound_sterling_two, None),
        (pound_sterling_one, pound_sterling_one_other, pound_sterling_two, None),
        (pound_sterling_two, pound_sterling_minus_one, pound_sterling_one, None),
        (pound_sterling_one, other, None, CurrencyMismatchException),
        (pound_sterling_one, 1.00, None, CurrencyTypeException),
        (pound_sterling_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pound_sterling_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pound_sterling_one)
    ])
    def test_pound_sterling_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GBP'
        assert new.numeric_code == '826'
        assert new.symbol == '£'
        assert new.localized_symbol == '£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPoundSterlingGG:
    """Pound Sterling GG currency tests."""

    pound_sterling_gg_minus_one = PoundSterlingGG(-1)
    pound_sterling_gg_one_other = PoundSterlingGG(1)
    pound_sterling_gg_one = PoundSterlingGG(1)
    pound_sterling_gg_two = PoundSterlingGG(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_pound_sterling_gg_default(amount, result, printed):
        default = PoundSterlingGG(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GBP'
        assert default.numeric_code == '826'
        assert default.symbol == '£'
        assert default.localized_symbol == 'GG£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert default.__repr__() == (
            'PoundSterlingGG('
            f'amount: {result}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "GG£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_pound_sterling_gg_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PoundSterlingGG(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GBP'
        assert custom.numeric_code == '826'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'GG£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert custom.__repr__() == (
            'PoundSterlingGG('
            f'amount: {amount}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "GG£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pound_sterling_gg_recreate(amount, new_amount):
        default = PoundSterlingGG(amount)
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
    def test_pound_sterling_gg_change_attributes(attribute, value):
        immutable = PoundSterlingGG(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PoundSterlingGG\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pound_sterling_gg_add_attributes(attribute, value):
        immutable = PoundSterlingGG(1000)
        with raises(
                AttributeError,
                match=f'\'PoundSterlingGG\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pound_sterling_gg_one, pound_sterling_gg_one, pound_sterling_gg_two, None),
        (pound_sterling_gg_one, pound_sterling_gg_one_other, pound_sterling_gg_two, None),
        (pound_sterling_gg_two, pound_sterling_gg_minus_one, pound_sterling_gg_one, None),
        (pound_sterling_gg_one, other, None, CurrencyMismatchException),
        (pound_sterling_gg_one, 1.00, None, CurrencyTypeException),
        (pound_sterling_gg_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pound_sterling_gg_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pound_sterling_gg_one)
    ])
    def test_pound_sterling_gg_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GBP'
        assert new.numeric_code == '826'
        assert new.symbol == '£'
        assert new.localized_symbol == 'GG£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPoundSterlingIO:
    """Pound Sterling IO currency tests."""

    pound_sterling_io_minus_one = PoundSterlingIO(-1)
    pound_sterling_io_one_other = PoundSterlingIO(1)
    pound_sterling_io_one = PoundSterlingIO(1)
    pound_sterling_io_two = PoundSterlingIO(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_pound_sterling_io_default(amount, result, printed):
        default = PoundSterlingIO(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GBP'
        assert default.numeric_code == '826'
        assert default.symbol == '£'
        assert default.localized_symbol == 'IO£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert default.__repr__() == (
            'PoundSterlingIO('
            f'amount: {result}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "IO£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_pound_sterling_io_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PoundSterlingIO(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GBP'
        assert custom.numeric_code == '826'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'IO£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert custom.__repr__() == (
            'PoundSterlingIO('
            f'amount: {amount}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "IO£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pound_sterling_io_recreate(amount, new_amount):
        default = PoundSterlingIO(amount)
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
    def test_pound_sterling_io_change_attributes(attribute, value):
        immutable = PoundSterlingIO(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PoundSterlingIO\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pound_sterling_io_add_attributes(attribute, value):
        immutable = PoundSterlingIO(1000)
        with raises(
                AttributeError,
                match=f'\'PoundSterlingIO\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pound_sterling_io_one, pound_sterling_io_one, pound_sterling_io_two, None),
        (pound_sterling_io_one, pound_sterling_io_one_other, pound_sterling_io_two, None),
        (pound_sterling_io_two, pound_sterling_io_minus_one, pound_sterling_io_one, None),
        (pound_sterling_io_one, other, None, CurrencyMismatchException),
        (pound_sterling_io_one, 1.00, None, CurrencyTypeException),
        (pound_sterling_io_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pound_sterling_io_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pound_sterling_io_one)
    ])
    def test_pound_sterling_io_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GBP'
        assert new.numeric_code == '826'
        assert new.symbol == '£'
        assert new.localized_symbol == 'IO£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPoundSterlingGB:
    """Pound Sterling GB currency tests."""

    pound_sterling_gb_minus_one = PoundSterlingGB(-1)
    pound_sterling_gb_one_other = PoundSterlingGB(1)
    pound_sterling_gb_one = PoundSterlingGB(1)
    pound_sterling_gb_two = PoundSterlingGB(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_pound_sterling_gb_default(amount, result, printed):
        default = PoundSterlingGB(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GBP'
        assert default.numeric_code == '826'
        assert default.symbol == '£'
        assert default.localized_symbol == 'GB£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert default.__repr__() == (
            'PoundSterlingGB('
            f'amount: {result}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "GB£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_pound_sterling_gb_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PoundSterlingGB(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GBP'
        assert custom.numeric_code == '826'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'GB£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert custom.__repr__() == (
            'PoundSterlingGB('
            f'amount: {amount}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "GB£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pound_sterling_gb_recreate(amount, new_amount):
        default = PoundSterlingGB(amount)
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
    def test_pound_sterling_gb_change_attributes(attribute, value):
        immutable = PoundSterlingGB(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PoundSterlingGB\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pound_sterling_gb_add_attributes(attribute, value):
        immutable = PoundSterlingGB(1000)
        with raises(
                AttributeError,
                match=f'\'PoundSterlingGB\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pound_sterling_gb_one, pound_sterling_gb_one, pound_sterling_gb_two, None),
        (pound_sterling_gb_one, pound_sterling_gb_one_other, pound_sterling_gb_two, None),
        (pound_sterling_gb_two, pound_sterling_gb_minus_one, pound_sterling_gb_one, None),
        (pound_sterling_gb_one, other, None, CurrencyMismatchException),
        (pound_sterling_gb_one, 1.00, None, CurrencyTypeException),
        (pound_sterling_gb_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pound_sterling_gb_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pound_sterling_gb_one)
    ])
    def test_pound_sterling_gb_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GBP'
        assert new.numeric_code == '826'
        assert new.symbol == '£'
        assert new.localized_symbol == 'GB£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestPoundSterlingIM:
    """Pound Sterling IM currency tests."""

    pound_sterling_im_minus_one = PoundSterlingIM(-1)
    pound_sterling_im_one_other = PoundSterlingIM(1)
    pound_sterling_im_one = PoundSterlingIM(1)
    pound_sterling_im_two = PoundSterlingIM(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_pound_sterling_im_default(amount, result, printed):
        default = PoundSterlingIM(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GBP'
        assert default.numeric_code == '826'
        assert default.symbol == '£'
        assert default.localized_symbol == 'IM£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert default.__repr__() == (
            'PoundSterlingIM('
            f'amount: {result}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "IM£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_pound_sterling_im_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = PoundSterlingIM(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GBP'
        assert custom.numeric_code == '826'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'IM£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GBP',
            '826'))
        assert custom.__repr__() == (
            'PoundSterlingIM('
            f'amount: {amount}, '
            'alpha_code: "GBP", '
            'numeric_code: "826", '
            'symbol: "£", '
            'localized_symbol: "IM£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_pound_sterling_im_recreate(amount, new_amount):
        default = PoundSterlingIM(amount)
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
    def test_pound_sterling_im_change_attributes(attribute, value):
        immutable = PoundSterlingIM(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'PoundSterlingIM\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_pound_sterling_im_add_attributes(attribute, value):
        immutable = PoundSterlingIM(1000)
        with raises(
                AttributeError,
                match=f'\'PoundSterlingIM\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (pound_sterling_im_one, pound_sterling_im_one, pound_sterling_im_two, None),
        (pound_sterling_im_one, pound_sterling_im_one_other, pound_sterling_im_two, None),
        (pound_sterling_im_two, pound_sterling_im_minus_one, pound_sterling_im_one, None),
        (pound_sterling_im_one, other, None, CurrencyMismatchException),
        (pound_sterling_im_one, 1.00, None, CurrencyTypeException),
        (pound_sterling_im_one, '1.00', None, CurrencyTypeException)
    ])
    def test_pound_sterling_im_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (pound_sterling_im_one)
    ])
    def test_pound_sterling_im_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GBP'
        assert new.numeric_code == '826'
        assert new.symbol == '£'
        assert new.localized_symbol == 'IM£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestGibraltarPound:
    """Gibraltar Pound currency tests."""

    gibraltar_pound_minus_one = GibraltarPound(-1)
    gibraltar_pound_one_other = GibraltarPound(1)
    gibraltar_pound_one = GibraltarPound(1)
    gibraltar_pound_two = GibraltarPound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_gibraltar_pound_default(amount, result, printed):
        default = GibraltarPound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'GIP'
        assert default.numeric_code == '292'
        assert default.symbol == '£'
        assert default.localized_symbol == 'GI£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'GIP',
            '292'))
        assert default.__repr__() == (
            'GibraltarPound('
            f'amount: {result}, '
            'alpha_code: "GIP", '
            'numeric_code: "292", '
            'symbol: "£", '
            'localized_symbol: "GI£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_gibraltar_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = GibraltarPound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'GIP'
        assert custom.numeric_code == '292'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'GI£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'GIP',
            '292'))
        assert custom.__repr__() == (
            'GibraltarPound('
            f'amount: {amount}, '
            'alpha_code: "GIP", '
            'numeric_code: "292", '
            'symbol: "£", '
            'localized_symbol: "GI£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_gibraltar_pound_recreate(amount, new_amount):
        default = GibraltarPound(amount)
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
    def test_gibraltar_pound_change_attributes(attribute, value):
        immutable = GibraltarPound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'GibraltarPound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_gibraltar_pound_add_attributes(attribute, value):
        immutable = GibraltarPound(1000)
        with raises(
                AttributeError,
                match=f'\'GibraltarPound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (gibraltar_pound_one, gibraltar_pound_one, gibraltar_pound_two, None),
        (gibraltar_pound_one, gibraltar_pound_one_other, gibraltar_pound_two, None),
        (gibraltar_pound_two, gibraltar_pound_minus_one, gibraltar_pound_one, None),
        (gibraltar_pound_one, other, None, CurrencyMismatchException),
        (gibraltar_pound_one, 1.00, None, CurrencyTypeException),
        (gibraltar_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_gibraltar_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (gibraltar_pound_one)
    ])
    def test_gibraltar_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'GIP'
        assert new.numeric_code == '292'
        assert new.symbol == '£'
        assert new.localized_symbol == 'GI£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestLebanesePound:
    """Lebanese Pound currency tests."""

    lebanese_pound_minus_one = LebanesePound(-1)
    lebanese_pound_one_other = LebanesePound(1)
    lebanese_pound_one = LebanesePound(1)
    lebanese_pound_two = LebanesePound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ل.ل.\xa0٣'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ل.ل.\xa0٣'),
        (10, '10', 'ل.ل.\xa0١٠'),
        (Decimal('10'), '10', 'ل.ل.\xa0١٠'),
        ('-3.14', '-3.14', 'ل.ل.\xa0-٣'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ل.ل.\xa0-٣'),
        (-10, '-10', 'ل.ل.\xa0-١٠'),
        (Decimal('-10'), '-10', 'ل.ل.\xa0-١٠')
    ])
    def test_lebanese_pound_default(amount, result, printed):
        default = LebanesePound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'LBP'
        assert default.numeric_code == '422'
        assert default.symbol == 'ل.ل.'
        assert default.localized_symbol == 'ل.ل.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '0\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'LBP',
            '422'))
        assert default.__repr__() == (
            'LebanesePound('
            f'amount: {result}, '
            'alpha_code: "LBP", '
            'numeric_code: "422", '
            'symbol: "ل.ل.", '
            'localized_symbol: "ل.ل.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "0٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ل.ل.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ل.ل.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_lebanese_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = LebanesePound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'LBP'
        assert custom.numeric_code == '422'
        assert custom.symbol == 'ل.ل.'
        assert custom.localized_symbol == 'ل.ل.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'LBP',
            '422'))
        assert custom.__repr__() == (
            'LebanesePound('
            f'amount: {amount}, '
            'alpha_code: "LBP", '
            'numeric_code: "422", '
            'symbol: "ل.ل.", '
            'localized_symbol: "ل.ل.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_lebanese_pound_recreate(amount, new_amount):
        default = LebanesePound(amount)
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
    def test_lebanese_pound_change_attributes(attribute, value):
        immutable = LebanesePound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'LebanesePound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_lebanese_pound_add_attributes(attribute, value):
        immutable = LebanesePound(1000)
        with raises(
                AttributeError,
                match=f'\'LebanesePound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (lebanese_pound_one, lebanese_pound_one, lebanese_pound_two, None),
        (lebanese_pound_one, lebanese_pound_one_other, lebanese_pound_two, None),
        (lebanese_pound_two, lebanese_pound_minus_one, lebanese_pound_one, None),
        (lebanese_pound_one, other, None, CurrencyMismatchException),
        (lebanese_pound_one, 1.00, None, CurrencyTypeException),
        (lebanese_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_lebanese_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (lebanese_pound_one)
    ])
    def test_lebanese_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'LBP'
        assert new.numeric_code == '422'
        assert new.symbol == 'ل.ل.'
        assert new.localized_symbol == 'ل.ل.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '0\u066B\u066C3%s\u00A0%a'


class TestSudanesePound:
    """Sudanese Pound currency tests."""

    sudanese_pound_minus_one = SudanesePound(-1)
    sudanese_pound_one_other = SudanesePound(1)
    sudanese_pound_one = SudanesePound(1)
    sudanese_pound_two = SudanesePound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '٣٫١٤\xa0ج.س'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '٣٫١٤\xa0ج.س'),
        (10, '10', '١٠٫٠٠\xa0ج.س'),
        (Decimal('10'), '10', '١٠٫٠٠\xa0ج.س'),
        ('-3.14', '-3.14', '-٣٫١٤\xa0ج.س'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-٣٫١٤\xa0ج.س'),
        (-10, '-10', '-١٠٫٠٠\xa0ج.س'),
        (Decimal('-10'), '-10', '-١٠٫٠٠\xa0ج.س')
    ])
    def test_sudanese_pound_default(amount, result, printed):
        default = SudanesePound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SDG'
        assert default.numeric_code == '938'
        assert default.symbol == 'ج.س'
        assert default.localized_symbol == 'ج.س'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SDG',
            '938'))
        assert default.__repr__() == (
            'SudanesePound('
            f'amount: {result}, '
            'alpha_code: "SDG", '
            'numeric_code: "938", '
            'symbol: "ج.س", '
            'localized_symbol: "ج.س", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ج.س١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ج.س١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_sudanese_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SudanesePound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SDG'
        assert custom.numeric_code == '938'
        assert custom.symbol == 'ج.س'
        assert custom.localized_symbol == 'ج.س'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SDG',
            '938'))
        assert custom.__repr__() == (
            'SudanesePound('
            f'amount: {amount}, '
            'alpha_code: "SDG", '
            'numeric_code: "938", '
            'symbol: "ج.س", '
            'localized_symbol: "ج.س", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_sudanese_pound_recreate(amount, new_amount):
        default = SudanesePound(amount)
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
    def test_sudanese_pound_change_attributes(attribute, value):
        immutable = SudanesePound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SudanesePound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_sudanese_pound_add_attributes(attribute, value):
        immutable = SudanesePound(1000)
        with raises(
                AttributeError,
                match=f'\'SudanesePound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (sudanese_pound_one, sudanese_pound_one, sudanese_pound_two, None),
        (sudanese_pound_one, sudanese_pound_one_other, sudanese_pound_two, None),
        (sudanese_pound_two, sudanese_pound_minus_one, sudanese_pound_one, None),
        (sudanese_pound_one, other, None, CurrencyMismatchException),
        (sudanese_pound_one, 1.00, None, CurrencyTypeException),
        (sudanese_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_sudanese_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (sudanese_pound_one)
    ])
    def test_sudanese_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SDG'
        assert new.numeric_code == '938'
        assert new.symbol == 'ج.س'
        assert new.localized_symbol == 'ج.س'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'


class TestSaintHelenaPoundAI:
    """Saint Helena Pound AI currency tests."""

    saint_helena_pound_ai_minus_one = SaintHelenaPoundAI(-1)
    saint_helena_pound_ai_one_other = SaintHelenaPoundAI(1)
    saint_helena_pound_ai_one = SaintHelenaPoundAI(1)
    saint_helena_pound_ai_two = SaintHelenaPoundAI(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_saint_helena_pound_ai_default(amount, result, printed):
        default = SaintHelenaPoundAI(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SHP'
        assert default.numeric_code == '654'
        assert default.symbol == '£'
        assert default.localized_symbol == 'SH£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert default.__repr__() == (
            'SaintHelenaPoundAI('
            f'amount: {result}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_saint_helena_pound_ai_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SaintHelenaPoundAI(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SHP'
        assert custom.numeric_code == '654'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'SH£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert custom.__repr__() == (
            'SaintHelenaPoundAI('
            f'amount: {amount}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_saint_helena_pound_ai_recreate(amount, new_amount):
        default = SaintHelenaPoundAI(amount)
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
    def test_saint_helena_pound_ai_change_attributes(attribute, value):
        immutable = SaintHelenaPoundAI(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SaintHelenaPoundAI\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_saint_helena_pound_ai_add_attributes(attribute, value):
        immutable = SaintHelenaPoundAI(1000)
        with raises(
                AttributeError,
                match=f'\'SaintHelenaPoundAI\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (saint_helena_pound_ai_one, saint_helena_pound_ai_one, saint_helena_pound_ai_two, None),
        (saint_helena_pound_ai_one, saint_helena_pound_ai_one_other, saint_helena_pound_ai_two, None),
        (saint_helena_pound_ai_two, saint_helena_pound_ai_minus_one, saint_helena_pound_ai_one, None),
        (saint_helena_pound_ai_one, other, None, CurrencyMismatchException),
        (saint_helena_pound_ai_one, 1.00, None, CurrencyTypeException),
        (saint_helena_pound_ai_one, '1.00', None, CurrencyTypeException)
    ])
    def test_saint_helena_pound_ai_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (saint_helena_pound_ai_one)
    ])
    def test_saint_helena_pound_ai_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SHP'
        assert new.numeric_code == '654'
        assert new.symbol == '£'
        assert new.localized_symbol == 'SH£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSaintHelenaPound:
    """Saint Helena Pound currency tests."""

    saint_helena_pound_minus_one = SaintHelenaPound(-1)
    saint_helena_pound_one_other = SaintHelenaPound(1)
    saint_helena_pound_one = SaintHelenaPound(1)
    saint_helena_pound_two = SaintHelenaPound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_saint_helena_pound_default(amount, result, printed):
        default = SaintHelenaPound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SHP'
        assert default.numeric_code == '654'
        assert default.symbol == '£'
        assert default.localized_symbol == 'SH£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert default.__repr__() == (
            'SaintHelenaPound('
            f'amount: {result}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_saint_helena_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SaintHelenaPound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SHP'
        assert custom.numeric_code == '654'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'SH£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert custom.__repr__() == (
            'SaintHelenaPound('
            f'amount: {amount}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_saint_helena_pound_recreate(amount, new_amount):
        default = SaintHelenaPound(amount)
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
    def test_saint_helena_pound_change_attributes(attribute, value):
        immutable = SaintHelenaPound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SaintHelenaPound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_saint_helena_pound_add_attributes(attribute, value):
        immutable = SaintHelenaPound(1000)
        with raises(
                AttributeError,
                match=f'\'SaintHelenaPound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (saint_helena_pound_one, saint_helena_pound_one, saint_helena_pound_two, None),
        (saint_helena_pound_one, saint_helena_pound_one_other, saint_helena_pound_two, None),
        (saint_helena_pound_two, saint_helena_pound_minus_one, saint_helena_pound_one, None),
        (saint_helena_pound_one, other, None, CurrencyMismatchException),
        (saint_helena_pound_one, 1.00, None, CurrencyTypeException),
        (saint_helena_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_saint_helena_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (saint_helena_pound_one)
    ])
    def test_saint_helena_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SHP'
        assert new.numeric_code == '654'
        assert new.symbol == '£'
        assert new.localized_symbol == 'SH£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSaintHelenaPoundTC:
    """Saint Helena Pound TC currency tests."""

    saint_helena_pound_tc_minus_one = SaintHelenaPoundTC(-1)
    saint_helena_pound_tc_one_other = SaintHelenaPoundTC(1)
    saint_helena_pound_tc_one = SaintHelenaPoundTC(1)
    saint_helena_pound_tc_two = SaintHelenaPoundTC(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '£3.14'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '£3.14'),
        (10, '10', '£10.00'),
        (Decimal('10'), '10', '£10.00'),
        ('-3.14', '-3.14', '-£3.14'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-£3.14'),
        (-10, '-10', '-£10.00'),
        (Decimal('-10'), '-10', '-£10.00')
    ])
    def test_saint_helena_pound_tc_default(amount, result, printed):
        default = SaintHelenaPoundTC(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SHP'
        assert default.numeric_code == '654'
        assert default.symbol == '£'
        assert default.localized_symbol == 'SH£'
        assert default.convertion == ''
        assert default.pattern == '2.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert default.__repr__() == (
            'SaintHelenaPoundTC('
            f'amount: {result}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            'pattern: "2.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '£10.00,00000'),
        (-1000, '£10.00,00000-')
    ])
    def test_saint_helena_pound_tc_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SaintHelenaPoundTC(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SHP'
        assert custom.numeric_code == '654'
        assert custom.symbol == '£'
        assert custom.localized_symbol == 'SH£'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SHP',
            '654'))
        assert custom.__repr__() == (
            'SaintHelenaPoundTC('
            f'amount: {amount}, '
            'alpha_code: "SHP", '
            'numeric_code: "654", '
            'symbol: "£", '
            'localized_symbol: "SH£", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_saint_helena_pound_tc_recreate(amount, new_amount):
        default = SaintHelenaPoundTC(amount)
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
    def test_saint_helena_pound_tc_change_attributes(attribute, value):
        immutable = SaintHelenaPoundTC(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SaintHelenaPoundTC\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_saint_helena_pound_tc_add_attributes(attribute, value):
        immutable = SaintHelenaPoundTC(1000)
        with raises(
                AttributeError,
                match=f'\'SaintHelenaPoundTC\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (saint_helena_pound_tc_one, saint_helena_pound_tc_one, saint_helena_pound_tc_two, None),
        (saint_helena_pound_tc_one, saint_helena_pound_tc_one_other, saint_helena_pound_tc_two, None),
        (saint_helena_pound_tc_two, saint_helena_pound_tc_minus_one, saint_helena_pound_tc_one, None),
        (saint_helena_pound_tc_one, other, None, CurrencyMismatchException),
        (saint_helena_pound_tc_one, 1.00, None, CurrencyTypeException),
        (saint_helena_pound_tc_one, '1.00', None, CurrencyTypeException)
    ])
    def test_saint_helena_pound_tc_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (saint_helena_pound_tc_one)
    ])
    def test_saint_helena_pound_tc_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SHP'
        assert new.numeric_code == '654'
        assert new.symbol == '£'
        assert new.localized_symbol == 'SH£'
        assert new.convertion == ''
        assert new.pattern == '2.,3%-%s%u'


class TestSyrianPound:
    """Syrian Pound currency tests."""

    syrian_pound_minus_one = SyrianPound(-1)
    syrian_pound_one_other = SyrianPound(1)
    syrian_pound_one = SyrianPound(1)
    syrian_pound_two = SyrianPound(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '٣٫١٤\xa0ل.س'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '٣٫١٤\xa0ل.س'),
        (10, '10', '١٠٫٠٠\xa0ل.س'),
        (Decimal('10'), '10', '١٠٫٠٠\xa0ل.س'),
        ('-3.14', '-3.14', '-٣٫١٤\xa0ل.س'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-٣٫١٤\xa0ل.س'),
        (-10, '-10', '-١٠٫٠٠\xa0ل.س'),
        (Decimal('-10'), '-10', '-١٠٫٠٠\xa0ل.س')
    ])
    def test_syrian_pound_default(amount, result, printed):
        default = SyrianPound(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'SYP'
        assert default.numeric_code == '760'
        assert default.symbol == 'ل.س'
        assert default.localized_symbol == 'ل.س'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'SYP',
            '760'))
        assert default.__repr__() == (
            'SyrianPound('
            f'amount: {result}, '
            'alpha_code: "SYP", '
            'numeric_code: "760", '
            'symbol: "ل.س", '
            'localized_symbol: "ل.س", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ل.س١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ل.س١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_syrian_pound_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = SyrianPound(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'SYP'
        assert custom.numeric_code == '760'
        assert custom.symbol == 'ل.س'
        assert custom.localized_symbol == 'ل.س'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'SYP',
            '760'))
        assert custom.__repr__() == (
            'SyrianPound('
            f'amount: {amount}, '
            'alpha_code: "SYP", '
            'numeric_code: "760", '
            'symbol: "ل.س", '
            'localized_symbol: "ل.س", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_syrian_pound_recreate(amount, new_amount):
        default = SyrianPound(amount)
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
    def test_syrian_pound_change_attributes(attribute, value):
        immutable = SyrianPound(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'SyrianPound\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_syrian_pound_add_attributes(attribute, value):
        immutable = SyrianPound(1000)
        with raises(
                AttributeError,
                match=f'\'SyrianPound\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (syrian_pound_one, syrian_pound_one, syrian_pound_two, None),
        (syrian_pound_one, syrian_pound_one_other, syrian_pound_two, None),
        (syrian_pound_two, syrian_pound_minus_one, syrian_pound_one, None),
        (syrian_pound_one, other, None, CurrencyMismatchException),
        (syrian_pound_one, 1.00, None, CurrencyTypeException),
        (syrian_pound_one, '1.00', None, CurrencyTypeException)
    ])
    def test_syrian_pound_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (syrian_pound_one)
    ])
    def test_syrian_pound_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'SYP'
        assert new.numeric_code == '760'
        assert new.symbol == 'ل.س'
        assert new.localized_symbol == 'ل.س'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'
