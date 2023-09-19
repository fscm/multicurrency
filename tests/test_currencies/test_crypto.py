# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Crypto currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.crypto import (
    EOS,
    Ethereum,
    Bitcoin,
    StellarLumens,
    Monero,
    Ripple,
    Tezos,
    Zcash)


class TestEOS:
    """EOS currency tests."""

    eos_minus_one = EOS(-1)
    eos_one_other = EOS(1)
    eos_one = EOS(1)
    eos_two = EOS(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ε3.1400'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ε3.1400'),
        (10, '10', 'ε10.0000'),
        (Decimal('10'), '10', 'ε10.0000'),
        ('-3.14', '-3.14', '-ε3.1400'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-ε3.1400'),
        (-10, '-10', '-ε10.0000'),
        (Decimal('-10'), '-10', '-ε10.0000')
    ])
    def test_eos_default(amount, result, printed):
        default = EOS(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'EOS'
        assert default.numeric_code == '0'
        assert default.symbol == 'ε'
        assert default.localized_symbol == 'ε'
        assert default.convertion == ''
        assert default.pattern == '4.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'EOS',
            '0'))
        assert default.__repr__() == (
            'EOS('
            f'amount: {result}, '
            'alpha_code: "EOS", '
            'numeric_code: "0", '
            'symbol: "ε", '
            'localized_symbol: "ε", '
            'convertion: "", '
            'pattern: "4.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ε10.00,00000'),
        (-1000, 'ε10.00,00000-')
    ])
    def test_eos_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = EOS(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'EOS'
        assert custom.numeric_code == '0'
        assert custom.symbol == 'ε'
        assert custom.localized_symbol == 'ε'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'EOS',
            '0'))
        assert custom.__repr__() == (
            'EOS('
            f'amount: {amount}, '
            'alpha_code: "EOS", '
            'numeric_code: "0", '
            'symbol: "ε", '
            'localized_symbol: "ε", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_eos_recreate(amount, new_amount):
        default = EOS(amount)
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
    def test_eos_change_attributes(attribute, value):
        immutable = EOS(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'EOS\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_eos_add_attributes(attribute, value):
        immutable = EOS(1000)
        with raises(
                AttributeError,
                match=f'\'EOS\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (eos_one, eos_one, eos_two, None),
        (eos_one, eos_one_other, eos_two, None),
        (eos_two, eos_minus_one, eos_one, None),
        (eos_one, other, None, CurrencyMismatchException),
        (eos_one, 1.00, None, CurrencyTypeException),
        (eos_one, '1.00', None, CurrencyTypeException)
    ])
    def test_eos_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (eos_one)
    ])
    def test_eos_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'EOS'
        assert new.numeric_code == '0'
        assert new.symbol == 'ε'
        assert new.localized_symbol == 'ε'
        assert new.convertion == ''
        assert new.pattern == '4.,3%-%s%u'


class TestEthereum:
    """Ethereum currency tests."""

    ethereum_minus_one = Ethereum(-1)
    ethereum_one_other = Ethereum(1)
    ethereum_one = Ethereum(1)
    ethereum_two = Ethereum(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'Ξ3.140000000000000000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'Ξ3.140000000000000124'),
        (10, '10', 'Ξ10.000000000000000000'),
        (Decimal('10'), '10', 'Ξ10.000000000000000000'),
        ('-3.14', '-3.14', '-Ξ3.140000000000000000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-Ξ3.140000000000000124'),
        (-10, '-10', '-Ξ10.000000000000000000'),
        (Decimal('-10'), '-10', '-Ξ10.000000000000000000')
    ])
    def test_ethereum_default(amount, result, printed):
        default = Ethereum(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ETH'
        assert default.numeric_code == '0'
        assert default.symbol == 'Ξ'
        assert default.localized_symbol == 'Ξ'
        assert default.convertion == ''
        assert default.pattern == '18.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ETH',
            '0'))
        assert default.__repr__() == (
            'Ethereum('
            f'amount: {result}, '
            'alpha_code: "ETH", '
            'numeric_code: "0", '
            'symbol: "Ξ", '
            'localized_symbol: "Ξ", '
            'convertion: "", '
            'pattern: "18.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'Ξ10.00,00000'),
        (-1000, 'Ξ10.00,00000-')
    ])
    def test_ethereum_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Ethereum(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ETH'
        assert custom.numeric_code == '0'
        assert custom.symbol == 'Ξ'
        assert custom.localized_symbol == 'Ξ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ETH',
            '0'))
        assert custom.__repr__() == (
            'Ethereum('
            f'amount: {amount}, '
            'alpha_code: "ETH", '
            'numeric_code: "0", '
            'symbol: "Ξ", '
            'localized_symbol: "Ξ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_ethereum_recreate(amount, new_amount):
        default = Ethereum(amount)
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
    def test_ethereum_change_attributes(attribute, value):
        immutable = Ethereum(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Ethereum\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_ethereum_add_attributes(attribute, value):
        immutable = Ethereum(1000)
        with raises(
                AttributeError,
                match=f'\'Ethereum\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (ethereum_one, ethereum_one, ethereum_two, None),
        (ethereum_one, ethereum_one_other, ethereum_two, None),
        (ethereum_two, ethereum_minus_one, ethereum_one, None),
        (ethereum_one, other, None, CurrencyMismatchException),
        (ethereum_one, 1.00, None, CurrencyTypeException),
        (ethereum_one, '1.00', None, CurrencyTypeException)
    ])
    def test_ethereum_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (ethereum_one)
    ])
    def test_ethereum_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ETH'
        assert new.numeric_code == '0'
        assert new.symbol == 'Ξ'
        assert new.localized_symbol == 'Ξ'
        assert new.convertion == ''
        assert new.pattern == '18.,3%-%s%u'


class TestBitcoin:
    """Bitcoin currency tests."""

    bitcoin_minus_one = Bitcoin(-1)
    bitcoin_one_other = Bitcoin(1)
    bitcoin_one = Bitcoin(1)
    bitcoin_two = Bitcoin(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '₿3.14000000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '₿3.14000000'),
        (10, '10', '₿10.00000000'),
        (Decimal('10'), '10', '₿10.00000000'),
        ('-3.14', '-3.14', '-₿3.14000000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-₿3.14000000'),
        (-10, '-10', '-₿10.00000000'),
        (Decimal('-10'), '-10', '-₿10.00000000')
    ])
    def test_bitcoin_default(amount, result, printed):
        default = Bitcoin(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XBT'
        assert default.numeric_code == '0'
        assert default.symbol == '₿'
        assert default.localized_symbol == '₿'
        assert default.convertion == ''
        assert default.pattern == '8.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XBT',
            '0'))
        assert default.__repr__() == (
            'Bitcoin('
            f'amount: {result}, '
            'alpha_code: "XBT", '
            'numeric_code: "0", '
            'symbol: "₿", '
            'localized_symbol: "₿", '
            'convertion: "", '
            'pattern: "8.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '₿10.00,00000'),
        (-1000, '₿10.00,00000-')
    ])
    def test_bitcoin_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Bitcoin(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XBT'
        assert custom.numeric_code == '0'
        assert custom.symbol == '₿'
        assert custom.localized_symbol == '₿'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XBT',
            '0'))
        assert custom.__repr__() == (
            'Bitcoin('
            f'amount: {amount}, '
            'alpha_code: "XBT", '
            'numeric_code: "0", '
            'symbol: "₿", '
            'localized_symbol: "₿", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_bitcoin_recreate(amount, new_amount):
        default = Bitcoin(amount)
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
    def test_bitcoin_change_attributes(attribute, value):
        immutable = Bitcoin(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Bitcoin\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_bitcoin_add_attributes(attribute, value):
        immutable = Bitcoin(1000)
        with raises(
                AttributeError,
                match=f'\'Bitcoin\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (bitcoin_one, bitcoin_one, bitcoin_two, None),
        (bitcoin_one, bitcoin_one_other, bitcoin_two, None),
        (bitcoin_two, bitcoin_minus_one, bitcoin_one, None),
        (bitcoin_one, other, None, CurrencyMismatchException),
        (bitcoin_one, 1.00, None, CurrencyTypeException),
        (bitcoin_one, '1.00', None, CurrencyTypeException)
    ])
    def test_bitcoin_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (bitcoin_one)
    ])
    def test_bitcoin_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XBT'
        assert new.numeric_code == '0'
        assert new.symbol == '₿'
        assert new.localized_symbol == '₿'
        assert new.convertion == ''
        assert new.pattern == '8.,3%-%s%u'


class TestStellarLumens:
    """Stellar Lumens currency tests."""

    stellar_lumens_minus_one = StellarLumens(-1)
    stellar_lumens_one_other = StellarLumens(1)
    stellar_lumens_one = StellarLumens(1)
    stellar_lumens_two = StellarLumens(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '*3.1400000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '*3.1400000'),
        (10, '10', '*10.0000000'),
        (Decimal('10'), '10', '*10.0000000'),
        ('-3.14', '-3.14', '-*3.1400000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-*3.1400000'),
        (-10, '-10', '-*10.0000000'),
        (Decimal('-10'), '-10', '-*10.0000000')
    ])
    def test_stellar_lumens_default(amount, result, printed):
        default = StellarLumens(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XLM'
        assert default.numeric_code == '0'
        assert default.symbol == '*'
        assert default.localized_symbol == '*'
        assert default.convertion == ''
        assert default.pattern == '7.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XLM',
            '0'))
        assert default.__repr__() == (
            'StellarLumens('
            f'amount: {result}, '
            'alpha_code: "XLM", '
            'numeric_code: "0", '
            'symbol: "*", '
            'localized_symbol: "*", '
            'convertion: "", '
            'pattern: "7.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '*10.00,00000'),
        (-1000, '*10.00,00000-')
    ])
    def test_stellar_lumens_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = StellarLumens(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XLM'
        assert custom.numeric_code == '0'
        assert custom.symbol == '*'
        assert custom.localized_symbol == '*'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XLM',
            '0'))
        assert custom.__repr__() == (
            'StellarLumens('
            f'amount: {amount}, '
            'alpha_code: "XLM", '
            'numeric_code: "0", '
            'symbol: "*", '
            'localized_symbol: "*", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_stellar_lumens_recreate(amount, new_amount):
        default = StellarLumens(amount)
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
    def test_stellar_lumens_change_attributes(attribute, value):
        immutable = StellarLumens(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'StellarLumens\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_stellar_lumens_add_attributes(attribute, value):
        immutable = StellarLumens(1000)
        with raises(
                AttributeError,
                match=f'\'StellarLumens\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (stellar_lumens_one, stellar_lumens_one, stellar_lumens_two, None),
        (stellar_lumens_one, stellar_lumens_one_other, stellar_lumens_two, None),
        (stellar_lumens_two, stellar_lumens_minus_one, stellar_lumens_one, None),
        (stellar_lumens_one, other, None, CurrencyMismatchException),
        (stellar_lumens_one, 1.00, None, CurrencyTypeException),
        (stellar_lumens_one, '1.00', None, CurrencyTypeException)
    ])
    def test_stellar_lumens_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (stellar_lumens_one)
    ])
    def test_stellar_lumens_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XLM'
        assert new.numeric_code == '0'
        assert new.symbol == '*'
        assert new.localized_symbol == '*'
        assert new.convertion == ''
        assert new.pattern == '7.,3%-%s%u'


class TestMonero:
    """Monero currency tests."""

    monero_minus_one = Monero(-1)
    monero_one_other = Monero(1)
    monero_one = Monero(1)
    monero_two = Monero(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ɱ3.140000000000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ɱ3.140000000000'),
        (10, '10', 'ɱ10.000000000000'),
        (Decimal('10'), '10', 'ɱ10.000000000000'),
        ('-3.14', '-3.14', '-ɱ3.140000000000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-ɱ3.140000000000'),
        (-10, '-10', '-ɱ10.000000000000'),
        (Decimal('-10'), '-10', '-ɱ10.000000000000')
    ])
    def test_monero_default(amount, result, printed):
        default = Monero(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XMR'
        assert default.numeric_code == '0'
        assert default.symbol == 'ɱ'
        assert default.localized_symbol == 'ɱ'
        assert default.convertion == ''
        assert default.pattern == '12.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XMR',
            '0'))
        assert default.__repr__() == (
            'Monero('
            f'amount: {result}, '
            'alpha_code: "XMR", '
            'numeric_code: "0", '
            'symbol: "ɱ", '
            'localized_symbol: "ɱ", '
            'convertion: "", '
            'pattern: "12.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ɱ10.00,00000'),
        (-1000, 'ɱ10.00,00000-')
    ])
    def test_monero_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Monero(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XMR'
        assert custom.numeric_code == '0'
        assert custom.symbol == 'ɱ'
        assert custom.localized_symbol == 'ɱ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XMR',
            '0'))
        assert custom.__repr__() == (
            'Monero('
            f'amount: {amount}, '
            'alpha_code: "XMR", '
            'numeric_code: "0", '
            'symbol: "ɱ", '
            'localized_symbol: "ɱ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_monero_recreate(amount, new_amount):
        default = Monero(amount)
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
    def test_monero_change_attributes(attribute, value):
        immutable = Monero(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Monero\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_monero_add_attributes(attribute, value):
        immutable = Monero(1000)
        with raises(
                AttributeError,
                match=f'\'Monero\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (monero_one, monero_one, monero_two, None),
        (monero_one, monero_one_other, monero_two, None),
        (monero_two, monero_minus_one, monero_one, None),
        (monero_one, other, None, CurrencyMismatchException),
        (monero_one, 1.00, None, CurrencyTypeException),
        (monero_one, '1.00', None, CurrencyTypeException)
    ])
    def test_monero_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (monero_one)
    ])
    def test_monero_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XMR'
        assert new.numeric_code == '0'
        assert new.symbol == 'ɱ'
        assert new.localized_symbol == 'ɱ'
        assert new.convertion == ''
        assert new.pattern == '12.,3%-%s%u'


class TestRipple:
    """Ripple currency tests."""

    ripple_minus_one = Ripple(-1)
    ripple_one_other = Ripple(1)
    ripple_one = Ripple(1)
    ripple_two = Ripple(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', '✕3.140000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', '✕3.140000'),
        (10, '10', '✕10.000000'),
        (Decimal('10'), '10', '✕10.000000'),
        ('-3.14', '-3.14', '-✕3.140000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-✕3.140000'),
        (-10, '-10', '-✕10.000000'),
        (Decimal('-10'), '-10', '-✕10.000000')
    ])
    def test_ripple_default(amount, result, printed):
        default = Ripple(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XRP'
        assert default.numeric_code == '0'
        assert default.symbol == '✕'
        assert default.localized_symbol == '✕'
        assert default.convertion == ''
        assert default.pattern == '6.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XRP',
            '0'))
        assert default.__repr__() == (
            'Ripple('
            f'amount: {result}, '
            'alpha_code: "XRP", '
            'numeric_code: "0", '
            'symbol: "✕", '
            'localized_symbol: "✕", '
            'convertion: "", '
            'pattern: "6.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, '✕10.00,00000'),
        (-1000, '✕10.00,00000-')
    ])
    def test_ripple_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Ripple(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XRP'
        assert custom.numeric_code == '0'
        assert custom.symbol == '✕'
        assert custom.localized_symbol == '✕'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XRP',
            '0'))
        assert custom.__repr__() == (
            'Ripple('
            f'amount: {amount}, '
            'alpha_code: "XRP", '
            'numeric_code: "0", '
            'symbol: "✕", '
            'localized_symbol: "✕", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_ripple_recreate(amount, new_amount):
        default = Ripple(amount)
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
    def test_ripple_change_attributes(attribute, value):
        immutable = Ripple(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Ripple\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_ripple_add_attributes(attribute, value):
        immutable = Ripple(1000)
        with raises(
                AttributeError,
                match=f'\'Ripple\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (ripple_one, ripple_one, ripple_two, None),
        (ripple_one, ripple_one_other, ripple_two, None),
        (ripple_two, ripple_minus_one, ripple_one, None),
        (ripple_one, other, None, CurrencyMismatchException),
        (ripple_one, 1.00, None, CurrencyTypeException),
        (ripple_one, '1.00', None, CurrencyTypeException)
    ])
    def test_ripple_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (ripple_one)
    ])
    def test_ripple_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XRP'
        assert new.numeric_code == '0'
        assert new.symbol == '✕'
        assert new.localized_symbol == '✕'
        assert new.convertion == ''
        assert new.pattern == '6.,3%-%s%u'


class TestTezos:
    """Tezos currency tests."""

    tezos_minus_one = Tezos(-1)
    tezos_one_other = Tezos(1)
    tezos_one = Tezos(1)
    tezos_two = Tezos(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ꜩ3.140000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ꜩ3.140000'),
        (10, '10', 'ꜩ10.000000'),
        (Decimal('10'), '10', 'ꜩ10.000000'),
        ('-3.14', '-3.14', '-ꜩ3.140000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-ꜩ3.140000'),
        (-10, '-10', '-ꜩ10.000000'),
        (Decimal('-10'), '-10', '-ꜩ10.000000')
    ])
    def test_tezos_default(amount, result, printed):
        default = Tezos(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'XTZ'
        assert default.numeric_code == '0'
        assert default.symbol == 'ꜩ'
        assert default.localized_symbol == 'ꜩ'
        assert default.convertion == ''
        assert default.pattern == '6.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'XTZ',
            '0'))
        assert default.__repr__() == (
            'Tezos('
            f'amount: {result}, '
            'alpha_code: "XTZ", '
            'numeric_code: "0", '
            'symbol: "ꜩ", '
            'localized_symbol: "ꜩ", '
            'convertion: "", '
            'pattern: "6.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ꜩ10.00,00000'),
        (-1000, 'ꜩ10.00,00000-')
    ])
    def test_tezos_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Tezos(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'XTZ'
        assert custom.numeric_code == '0'
        assert custom.symbol == 'ꜩ'
        assert custom.localized_symbol == 'ꜩ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'XTZ',
            '0'))
        assert custom.__repr__() == (
            'Tezos('
            f'amount: {amount}, '
            'alpha_code: "XTZ", '
            'numeric_code: "0", '
            'symbol: "ꜩ", '
            'localized_symbol: "ꜩ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_tezos_recreate(amount, new_amount):
        default = Tezos(amount)
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
    def test_tezos_change_attributes(attribute, value):
        immutable = Tezos(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Tezos\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_tezos_add_attributes(attribute, value):
        immutable = Tezos(1000)
        with raises(
                AttributeError,
                match=f'\'Tezos\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (tezos_one, tezos_one, tezos_two, None),
        (tezos_one, tezos_one_other, tezos_two, None),
        (tezos_two, tezos_minus_one, tezos_one, None),
        (tezos_one, other, None, CurrencyMismatchException),
        (tezos_one, 1.00, None, CurrencyTypeException),
        (tezos_one, '1.00', None, CurrencyTypeException)
    ])
    def test_tezos_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (tezos_one)
    ])
    def test_tezos_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'XTZ'
        assert new.numeric_code == '0'
        assert new.symbol == 'ꜩ'
        assert new.localized_symbol == 'ꜩ'
        assert new.convertion == ''
        assert new.pattern == '6.,3%-%s%u'


class TestZcash:
    """Zcash currency tests."""

    zcash_minus_one = Zcash(-1)
    zcash_one_other = Zcash(1)
    zcash_one = Zcash(1)
    zcash_two = Zcash(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        ('3.14', '3.14', 'ⓩ3.14000000'),
        (3.14, '3.140000000000000124344978758017532527446746826171875', 'ⓩ3.14000000'),
        (10, '10', 'ⓩ10.00000000'),
        (Decimal('10'), '10', 'ⓩ10.00000000'),
        ('-3.14', '-3.14', '-ⓩ3.14000000'),
        (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-ⓩ3.14000000'),
        (-10, '-10', '-ⓩ10.00000000'),
        (Decimal('-10'), '-10', '-ⓩ10.00000000')
    ])
    def test_zcash_default(amount, result, printed):
        default = Zcash(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == 'ZEC'
        assert default.numeric_code == '0'
        assert default.symbol == 'ⓩ'
        assert default.localized_symbol == 'ⓩ'
        assert default.convertion == ''
        assert default.pattern == '8.,3%-%s%u'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(amount),
            'ZEC',
            '0'))
        assert default.__repr__() == (
            'Zcash('
            f'amount: {result}, '
            'alpha_code: "ZEC", '
            'numeric_code: "0", '
            'symbol: "ⓩ", '
            'localized_symbol: "ⓩ", '
            'convertion: "", '
            'pattern: "8.,3%-%s%u")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        (1000, 'ⓩ10.00,00000'),
        (-1000, 'ⓩ10.00,00000-')
    ])
    def test_zcash_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = Zcash(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == 'ZEC'
        assert custom.numeric_code == '0'
        assert custom.symbol == 'ⓩ'
        assert custom.localized_symbol == 'ⓩ'
        assert custom.convertion == ''
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            'ZEC',
            '0'))
        assert custom.__repr__() == (
            'Zcash('
            f'amount: {amount}, '
            'alpha_code: "ZEC", '
            'numeric_code: "0", '
            'symbol: "ⓩ", '
            'localized_symbol: "ⓩ", '
            'convertion: "", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_zcash_recreate(amount, new_amount):
        default = Zcash(amount)
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
    def test_zcash_change_attributes(attribute, value):
        immutable = Zcash(1000)
        with raises(
                AttributeError,
                match=f'property \'{attribute}\' of \'Zcash\' object has no setter'):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_zcash_add_attributes(attribute, value):
        immutable = Zcash(1000)
        with raises(
                AttributeError,
                match=f'\'Zcash\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (zcash_one, zcash_one, zcash_two, None),
        (zcash_one, zcash_one_other, zcash_two, None),
        (zcash_two, zcash_minus_one, zcash_one, None),
        (zcash_one, other, None, CurrencyMismatchException),
        (zcash_one, 1.00, None, CurrencyTypeException),
        (zcash_one, '1.00', None, CurrencyTypeException)
    ])
    def test_zcash_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (zcash_one)
    ])
    def test_zcash_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == 'ZEC'
        assert new.numeric_code == '0'
        assert new.symbol == 'ⓩ'
        assert new.localized_symbol == 'ⓩ'
        assert new.convertion == ''
        assert new.pattern == '8.,3%-%s%u'
