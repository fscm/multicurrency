# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rial currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.rial import (
    IranianRial,
    RialOmani,
    QatariRial,
    YemeniRial)


class TestIranianRial:
    """Iranian Rial currency tests."""

    iranian_rial_minus_one = IranianRial(-1)
    iranian_rial_one_other = IranianRial(1)
    iranian_rial_one = IranianRial(1)
    iranian_rial_two = IranianRial(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '۳٫۱۴\xa0﷼'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '۳٫۱۴\xa0﷼'),
        (10, '10', '۱۰٫۰۰\xa0﷼'),
        (Decimal('10'), '10', '۱۰٫۰۰\xa0﷼'),
        ('-3.14', '-3.14', '-۳٫۱۴\xa0﷼'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-۳٫۱۴\xa0﷼'),
        (-10, '-10', '-۱۰٫۰۰\xa0﷼'),
        (Decimal('-10'), '-10', '-۱۰٫۰۰\xa0﷼')
    ])
    def test_iranian_rial_default(amount, result, printed):
        default = IranianRial(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'IRR'
        assert default.numeric_code == '364'
        assert default.symbol == '﷼'
        assert default.localized_symbol == '﷼'
        assert default.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'IRR',
            '364'))
        assert default.__repr__() == (
            'IranianRial('
            f'amount: {result}, '
            'alpha_code: "IRR", '
            'numeric_code: "364", '
            'symbol: "﷼", '
            'localized_symbol: "﷼", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '﷼۱۰.۰۰,۰۰۰۰۰'),
        (-1000, '﷼۱۰.۰۰,۰۰۰۰۰-')
    ])
    def test_iranian_rial_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = IranianRial(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'IRR'
        assert custom.numeric_code == '364'
        assert custom.symbol == '﷼'
        assert custom.localized_symbol == '﷼'
        assert custom.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'IRR',
            '364'))
        assert custom.__repr__() == (
            'IranianRial('
            f'amount: {amount}, '
            'alpha_code: "IRR", '
            'numeric_code: "364", '
            'symbol: "﷼", '
            'localized_symbol: "﷼", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_iranian_rial_recreate(amount, new_amount):
        default = IranianRial(amount)
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
    def test_iranian_rial_change_attributes(attribute, value):
        immutable = IranianRial(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'IranianRial\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_iranian_rial_add_attributes(attribute, value):
        immutable = IranianRial(1000)
        with raises(
                AttributeError,
                match=f'\'IranianRial\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (iranian_rial_one, iranian_rial_one, iranian_rial_two, None),
        (iranian_rial_one, iranian_rial_one_other, iranian_rial_two, None),
        (iranian_rial_two, iranian_rial_minus_one, iranian_rial_one, None),
        (iranian_rial_one, other, None, CurrencyMismatchException),
        (iranian_rial_one, 1.00, None, CurrencyTypeException),
        (iranian_rial_one, '1.00', None, CurrencyTypeException)
    ])
    def test_iranian_rial_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (iranian_rial_one)
    ])
    def test_iranian_rial_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'IRR'
        assert new.numeric_code == '364'
        assert new.symbol == '﷼'
        assert new.localized_symbol == '﷼'
        assert new.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'


class TestRialOmani:
    """Rial Omani currency tests."""

    rial_omani_minus_one = RialOmani(-1)
    rial_omani_one_other = RialOmani(1)
    rial_omani_one = RialOmani(1)
    rial_omani_two = RialOmani(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ر.ع.\xa0٣٫١٤٠'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ر.ع.\xa0٣٫١٤٠'),
        (10, '10', 'ر.ع.\xa0١٠٫٠٠٠'),
        (Decimal('10'), '10', 'ر.ع.\xa0١٠٫٠٠٠'),
        ('-3.14', '-3.14', 'ر.ع.\xa0-٣٫١٤٠'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ر.ع.\xa0-٣٫١٤٠'),
        (-10, '-10', 'ر.ع.\xa0-١٠٫٠٠٠'),
        (Decimal('-10'), '-10', 'ر.ع.\xa0-١٠٫٠٠٠')
    ])
    def test_rial_omani_default(amount, result, printed):
        default = RialOmani(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'OMR'
        assert default.numeric_code == '512'
        assert default.symbol == 'ر.ع.'
        assert default.localized_symbol == 'ر.ع.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '3\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'OMR',
            '512'))
        assert default.__repr__() == (
            'RialOmani('
            f'amount: {result}, '
            'alpha_code: "OMR", '
            'numeric_code: "512", '
            'symbol: "ر.ع.", '
            'localized_symbol: "ر.ع.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "3٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ر.ع.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ر.ع.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_rial_omani_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = RialOmani(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'OMR'
        assert custom.numeric_code == '512'
        assert custom.symbol == 'ر.ع.'
        assert custom.localized_symbol == 'ر.ع.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'OMR',
            '512'))
        assert custom.__repr__() == (
            'RialOmani('
            f'amount: {amount}, '
            'alpha_code: "OMR", '
            'numeric_code: "512", '
            'symbol: "ر.ع.", '
            'localized_symbol: "ر.ع.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_rial_omani_recreate(amount, new_amount):
        default = RialOmani(amount)
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
    def test_rial_omani_change_attributes(attribute, value):
        immutable = RialOmani(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'RialOmani\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_rial_omani_add_attributes(attribute, value):
        immutable = RialOmani(1000)
        with raises(
                AttributeError,
                match=f'\'RialOmani\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (rial_omani_one, rial_omani_one, rial_omani_two, None),
        (rial_omani_one, rial_omani_one_other, rial_omani_two, None),
        (rial_omani_two, rial_omani_minus_one, rial_omani_one, None),
        (rial_omani_one, other, None, CurrencyMismatchException),
        (rial_omani_one, 1.00, None, CurrencyTypeException),
        (rial_omani_one, '1.00', None, CurrencyTypeException)
    ])
    def test_rial_omani_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (rial_omani_one)
    ])
    def test_rial_omani_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'OMR'
        assert new.numeric_code == '512'
        assert new.symbol == 'ر.ع.'
        assert new.localized_symbol == 'ر.ع.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '3\u066B\u066C3%s\u00A0%a'


class TestQatariRial:
    """Qatari Rial currency tests."""

    qatari_rial_minus_one = QatariRial(-1)
    qatari_rial_one_other = QatariRial(1)
    qatari_rial_one = QatariRial(1)
    qatari_rial_two = QatariRial(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ر.ق.\xa0٣٫١٤'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ر.ق.\xa0٣٫١٤'),
        (10, '10', 'ر.ق.\xa0١٠٫٠٠'),
        (Decimal('10'), '10', 'ر.ق.\xa0١٠٫٠٠'),
        ('-3.14', '-3.14', 'ر.ق.\xa0-٣٫١٤'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', 'ر.ق.\xa0-٣٫١٤'),
        (-10, '-10', 'ر.ق.\xa0-١٠٫٠٠'),
        (Decimal('-10'), '-10', 'ر.ق.\xa0-١٠٫٠٠')
    ])
    def test_qatari_rial_default(amount, result, printed):
        default = QatariRial(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'QAR'
        assert default.numeric_code == '634'
        assert default.symbol == 'ر.ق.'
        assert default.localized_symbol == 'ر.ق.'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%s\u00A0%a'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'QAR',
            '634'))
        assert default.__repr__() == (
            'QatariRial('
            f'amount: {result}, '
            'alpha_code: "QAR", '
            'numeric_code: "634", '
            'symbol: "ر.ق.", '
            'localized_symbol: "ر.ق.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%s %a")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ر.ق.١٠.٠٠,٠٠٠٠٠'),
        (-1000, 'ر.ق.١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_qatari_rial_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = QatariRial(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'QAR'
        assert custom.numeric_code == '634'
        assert custom.symbol == 'ر.ق.'
        assert custom.localized_symbol == 'ر.ق.'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'QAR',
            '634'))
        assert custom.__repr__() == (
            'QatariRial('
            f'amount: {amount}, '
            'alpha_code: "QAR", '
            'numeric_code: "634", '
            'symbol: "ر.ق.", '
            'localized_symbol: "ر.ق.", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_qatari_rial_recreate(amount, new_amount):
        default = QatariRial(amount)
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
    def test_qatari_rial_change_attributes(attribute, value):
        immutable = QatariRial(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'QatariRial\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_qatari_rial_add_attributes(attribute, value):
        immutable = QatariRial(1000)
        with raises(
                AttributeError,
                match=f'\'QatariRial\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (qatari_rial_one, qatari_rial_one, qatari_rial_two, None),
        (qatari_rial_one, qatari_rial_one_other, qatari_rial_two, None),
        (qatari_rial_two, qatari_rial_minus_one, qatari_rial_one, None),
        (qatari_rial_one, other, None, CurrencyMismatchException),
        (qatari_rial_one, 1.00, None, CurrencyTypeException),
        (qatari_rial_one, '1.00', None, CurrencyTypeException)
    ])
    def test_qatari_rial_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (qatari_rial_one)
    ])
    def test_qatari_rial_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'QAR'
        assert new.numeric_code == '634'
        assert new.symbol == 'ر.ق.'
        assert new.localized_symbol == 'ر.ق.'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%s\u00A0%a'


class TestYemeniRial:
    """Yemeni Rial currency tests."""

    yemeni_rial_minus_one = YemeniRial(-1)
    yemeni_rial_one_other = YemeniRial(1)
    yemeni_rial_one = YemeniRial(1)
    yemeni_rial_two = YemeniRial(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '٣٫١٤\xa0﷼'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '٣٫١٤\xa0﷼'),
        (10, '10', '١٠٫٠٠\xa0﷼'),
        (Decimal('10'), '10', '١٠٫٠٠\xa0﷼'),
        ('-3.14', '-3.14', '-٣٫١٤\xa0﷼'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-٣٫١٤\xa0﷼'),
        (-10, '-10', '-١٠٫٠٠\xa0﷼'),
        (Decimal('-10'), '-10', '-١٠٫٠٠\xa0﷼')
    ])
    def test_yemeni_rial_default(amount, result, printed):
        default = YemeniRial(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'YER'
        assert default.numeric_code == '886'
        assert default.symbol == '﷼'
        assert default.localized_symbol == '﷼'
        assert default.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert default.pattern == '2\u066B\u066C3%a\u00A0%s'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'YER',
            '886'))
        assert default.__repr__() == (
            'YemeniRial('
            f'amount: {result}, '
            'alpha_code: "YER", '
            'numeric_code: "886", '
            'symbol: "﷼", '
            'localized_symbol: "﷼", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'pattern: "2٫٬3%a %s")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '﷼١٠.٠٠,٠٠٠٠٠'),
        (-1000, '﷼١٠.٠٠,٠٠٠٠٠-')
    ])
    def test_yemeni_rial_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = YemeniRial(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'YER'
        assert custom.numeric_code == '886'
        assert custom.symbol == '﷼'
        assert custom.localized_symbol == '﷼'
        assert custom.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'YER',
            '886'))
        assert custom.__repr__() == (
            'YemeniRial('
            f'amount: {amount}, '
            'alpha_code: "YER", '
            'numeric_code: "886", '
            'symbol: "﷼", '
            'localized_symbol: "﷼", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_yemeni_rial_recreate(amount, new_amount):
        default = YemeniRial(amount)
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
    def test_yemeni_rial_change_attributes(attribute, value):
        immutable = YemeniRial(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'YemeniRial\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_yemeni_rial_add_attributes(attribute, value):
        immutable = YemeniRial(1000)
        with raises(
                AttributeError,
                match=f'\'YemeniRial\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (yemeni_rial_one, yemeni_rial_one, yemeni_rial_two, None),
        (yemeni_rial_one, yemeni_rial_one_other, yemeni_rial_two, None),
        (yemeni_rial_two, yemeni_rial_minus_one, yemeni_rial_one, None),
        (yemeni_rial_one, other, None, CurrencyMismatchException),
        (yemeni_rial_one, 1.00, None, CurrencyTypeException),
        (yemeni_rial_one, '1.00', None, CurrencyTypeException)
    ])
    def test_yemeni_rial_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (yemeni_rial_one)
    ])
    def test_yemeni_rial_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'YER'
        assert new.numeric_code == '886'
        assert new.symbol == '﷼'
        assert new.localized_symbol == '﷼'
        assert new.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert new.pattern == '2\u066B\u066C3%a\u00A0%s'
