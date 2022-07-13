<%text># -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT</%text>

"""Tests for the ${module_name} currency representation(s)."""

from decimal import Decimal
from pytest import mark, raises
from multicurrency import (
    Currency,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.currencies.${module_lname} import ${class_list}
% for currency in currencies:


class Test${currency.class_name}:
    """${currency.name} currency tests."""

    ${currency.class_lname}_minus_one = ${currency.class_name}(-1)
    ${currency.class_lname}_one_other = ${currency.class_name}(1)
    ${currency.class_lname}_one = ${currency.class_name}(1)
    ${currency.class_lname}_two = ${currency.class_name}(2)
    other = Currency(amount=1, alpha_code='ZZZ')

    @staticmethod
    @mark.parametrize('amount,result,printed', [
        <% _data_ = ',\n        '.join(currency.tests.test_default) %>${_data_}
    ])
    def test_${currency.class_lname}_default(amount, result, printed):
        default = ${currency.class_name}(amount)
        assert default.amount == Decimal(result)
        assert default.alpha_code == '${currency.alpha_code}'
        assert default.numeric_code == '${currency.numeric_code}'
        assert default.symbol == '${currency.symbol}'
        assert default.localized_symbol == '${currency.localized_symbol}'
        assert default.convertion == '${currency.convertion}'
        assert default.pattern == '${currency.pattern}'
        assert default.__hash__() == hash((
            default.__class__,
            Decimal(str(amount)),
            '${currency.alpha_code}',
            '${currency.numeric_code}'))
        assert default.__repr__() == (
            '${currency.class_name}('
            f'amount: {result}, '
            'alpha_code: "${currency.alpha_code}", '
            'numeric_code: "${currency.numeric_code}", '
            'symbol: "${currency.symbol}", '
            'localized_symbol: "${currency.localized_symbol}", '
            'convertion: "${currency.convertion}", '
            'pattern: "<% _pattern_ = bytes(currency.pattern, 'utf-8').decode('unicode_escape').replace("'", "\\'") %>${_pattern_}")')
        assert default.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,printed', [
        <% _data_ = ',\n        '.join(currency.tests.test_custom) %>${_data_}
    ])
    def test_${currency.class_lname}_custom(amount, printed):
        pattern = r'5,.2%s%u%-'
        custom = ${currency.class_name}(
            amount=amount,
            pattern=pattern)
        assert custom.amount == Decimal(amount)
        assert custom.alpha_code == '${currency.alpha_code}'
        assert custom.numeric_code == '${currency.numeric_code}'
        assert custom.symbol == '${currency.symbol}'
        assert custom.localized_symbol == '${currency.localized_symbol}'
        assert custom.convertion == '${currency.convertion}'
        assert custom.pattern == pattern
        assert custom.__hash__() == hash((
            custom.__class__,
            Decimal(amount),
            '${currency.alpha_code}',
            '${currency.numeric_code}'))
        assert custom.__repr__() == (
            '${currency.class_name}('
            f'amount: {amount}, '
            'alpha_code: "${currency.alpha_code}", '
            'numeric_code: "${currency.numeric_code}", '
            'symbol: "${currency.symbol}", '
            'localized_symbol: "${currency.localized_symbol}", '
            'convertion: "${currency.convertion}", '
            f'pattern: "{pattern}")')
        assert custom.__str__() == printed

    @staticmethod
    @mark.parametrize('amount,new_amount', [
        (1000, 2000),
        (-1000, -2000)
    ])
    def test_${currency.class_lname}_recreate(amount, new_amount):
        default = ${currency.class_name}(amount)
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
    def test_${currency.class_lname}_change_attributes(attribute, value):
        immutable = ${currency.class_name}(1000)
        with raises(
                AttributeError,
                match=f'can\'t set attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('attribute,value', [
        ('new_variable', 'fail')
    ])
    def test_${currency.class_lname}_add_attributes(attribute, value):
        immutable = ${currency.class_name}(1000)
        with raises(
                AttributeError,
                match=f'\'${currency.class_name}\' object has no attribute \'{attribute}\''):
            setattr(immutable, attribute, value)

    @staticmethod
    @mark.parametrize('first,second,result,exception', [
        (${currency.class_lname}_one, ${currency.class_lname}_one, ${currency.class_lname}_two, None),
        (${currency.class_lname}_one, ${currency.class_lname}_one_other, ${currency.class_lname}_two, None),
        (${currency.class_lname}_two, ${currency.class_lname}_minus_one, ${currency.class_lname}_one, None),
        (${currency.class_lname}_one, other, None, CurrencyMismatchException),
        (${currency.class_lname}_one, 1.00, None, CurrencyTypeException),
        (${currency.class_lname}_one, '1.00', None, CurrencyTypeException)
    ])
    def test_${currency.class_lname}_math_add(first, second, result, exception):
        if exception:
            with raises(exception):
                first.__add__(second)
        else:
            assert (first + second) == result
            assert first.__add__(second) == result

    @staticmethod
    @mark.parametrize('original', [
        (${currency.class_lname}_one)
    ])
    def test_${currency.class_lname}_copy(original):
        new = original.__copy__()
        assert new == original
        assert new is not original
        assert new.alpha_code == '${currency.alpha_code}'
        assert new.numeric_code == '${currency.numeric_code}'
        assert new.symbol == '${currency.symbol}'
        assert new.localized_symbol == '${currency.localized_symbol}'
        assert new.convertion == '${currency.convertion}'
        assert new.pattern == '${currency.pattern}'
% endfor
