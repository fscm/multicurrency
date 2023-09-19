# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Currency module."""

import math
import pickle
from decimal import Decimal, localcontext
from pytest import mark, raises
from multicurrency import (
    CurrencyInvalidDivision,
    CurrencyInvalidFormat,
    CurrencyInvalidMultiplication,
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency.pycurrency import Currency


euro_minus_one = Currency(amount=-1, alpha_code='EUR')
euro_zero = Currency(amount=0, alpha_code='EUR')
euro_one = Currency(amount=1, alpha_code='EUR')
euro_one_other = Currency(amount=1, alpha_code='EUR')
euro_two = Currency(amount=2, alpha_code='EUR')
euro_three = Currency(amount=3, alpha_code='EUR')
euro_fifteen = Currency(amount=15, alpha_code='EUR')
euro_custom = Currency(
    amount=1/7*1_000_000,
    alpha_code='EUR',
    numeric_code='978',
    symbol='€',
    localized_symbol='PT€',
    convertion='0123456789-',
    pattern=r'2,.3%-%s%u')
euro_custom_negative = Currency(
    amount=1/7*-1_000_000,
    alpha_code='EUR',
    numeric_code='978',
    symbol='€',
    localized_symbol='PT€',
    convertion='0123456789-',
    pattern=r'2,.3%-%s%u')
usd_one = Currency(amount=1, alpha_code='USD')
kyat_custom = Currency(
    amount=1/7*-1_000_000,
    alpha_code='MMK',
    numeric_code='104',
    symbol='K',
    localized_symbol='K',
    convertion='၀၁၂၃၄၅၆၇၈၉-',
    pattern='2.,3%a\u00A0%s')


@mark.parametrize('amount,result,printed', [
    ('3.14', '3.14', '3.14'),
    (3.14, '3.140000000000000124344978758017532527446746826171875', '3.14'),
    (10, '10', '10.00'),
    (Decimal(10), '10', '10.00'),
    ('-3.14', '-3.14', '-3.14'),
    (-3.14, '-3.140000000000000124344978758017532527446746826171875', '-3.14'),
    (-10, '-10', '-10.00'),
    (Decimal(-10), '-10', '-10.00')
])
def test_pycurrency_default(amount, result, printed):
    default = Currency(amount)
    assert default.amount == Decimal(result)
    assert default.alpha_code == ''
    assert default.numeric_code == '0'
    assert default.symbol == ''
    assert default.localized_symbol == ''
    assert default.convertion == ''
    assert default.pattern == r'2.,3%a%s'
    assert default.__hash__() == hash((
        default.__class__,
        Decimal(amount),
        '',
        '0'))
    assert default.__repr__() == (
        'Currency('
        f'amount: {result}, '
        'alpha_code: "", '
        'numeric_code: "0", '
        'symbol: "", '
        'localized_symbol: "", '
        'convertion: "", '
        'pattern: "2.,3%a%s")')
    assert default.__str__() == printed


@mark.parametrize('amount,printed', [
    (1000, '€1.000,00'),
    (-1000, '-€1.000,00')
])
def test_pycurrency_custom(amount, printed):
    pattern = r'2,.3%-%s%u'
    euro = Currency(
        amount=amount,
        alpha_code='EUR',
        numeric_code='978',
        symbol='€',
        localized_symbol='PT€',
        convertion='0123456789-',
        pattern=pattern)
    assert euro.amount == Decimal(amount)
    assert euro.alpha_code == 'EUR'
    assert euro.numeric_code == '978'
    assert euro.symbol == '€'
    assert euro.localized_symbol == 'PT€'
    assert euro.convertion == '0123456789-'
    assert euro.pattern == pattern
    assert euro.__hash__() == hash((
        euro.__class__,
        Decimal(amount),
        'EUR',
        '978'))
    assert euro.__repr__() == (
        'Currency('
        f'amount: {amount}, '
        'alpha_code: "EUR", '
        'numeric_code: "978", '
        'symbol: "€", '
        'localized_symbol: "PT€", '
        'convertion: "0123456789-", '
        f'pattern: "{pattern}")')
    assert euro.__str__() == printed


@mark.parametrize('amount,new_amount', [
    (1000, 2000),
    (-1000, -2000)
])
def test_pycurrency_recreate(amount, new_amount):
    default = Currency(amount)
    new = default.__recreate__(new_amount)
    assert new is not default
    assert default.amount == amount
    assert new.amount == new_amount


@mark.parametrize('amount,pattern,exception,printed', [
    (1000, '4.,3%a', None, '1,000.0000'),
    (1000, '1.,3%a', None, '1,000.0'),
    (1000, '0.,3%a', None, '1,000'),
    (1000, '-2.,3%a', CurrencyInvalidFormat, 'Invalid currency format')
])
def test_pycurrency_decimal_places(amount, pattern, exception, printed):
    if exception:
        with raises(exception, match=printed):
            _ = Currency(amount=amount, pattern=pattern)
    else:
        default = Currency(amount=amount, pattern=pattern)
        assert default.__str__() == printed


@mark.parametrize('amount,pattern,exception,printed', [
    (10000, '2.,4%a', None, '1,0000.00'),
    (10000, '2.,1%a', None, '1,0,0,0,0.00'),
    (10000, '2.,0%a', None, '10000.00'),
    (10000, '2.,-2%a', CurrencyInvalidFormat, 'Invalid currency format')
])
def test_pycurrency_grouping_places(amount, pattern, exception, printed):
    if exception:
        with raises(exception, match=printed):
            _ = Currency(amount=amount, pattern=pattern)
    else:
        default = Currency(amount=amount, pattern=pattern)
        assert default.__str__() == printed


@mark.parametrize('amount,convertion,printed', [
    (123456789, 'zabcdef', 'abc,def,789.zz'),
    (123456789, 'zabcdefghi-', 'abc,def,ghi.zz'),
    (-123456789, 'zabcdefghi-', '-abc,def,ghi.zz'),
    (-123456789, 'zabcdefghi_', '_abc,def,ghi.zz')
])
def test_pycurrency_convertion(amount, convertion, printed):
    default = Currency(amount=amount, convertion=convertion)
    assert default.__str__() == printed


@mark.parametrize('attribute,value', [
    ('amount', 999),
    ('alpha_code', 'EUR'),
    ('numeric_code', '978'),
    ('symbol', '€'),
    ('localized_symbol', 'PT€'),
    ('convertion', '0123456789-'),
    ('pattern', '2,.3%-%s%u')
])
def test_pycurrency_change_attributes(attribute, value):
    default = Currency(1000)
    with raises(
            AttributeError,
            match=f'property \'{attribute}\' of \'Currency\' object has no setter'):
        setattr(default, attribute, value)


@mark.parametrize('attribute,value', [
    ('new_variable', 'fail')
])
def test_pycurrency_add_attributes(attribute, value):
    default = Currency(1000)
    with raises(
            AttributeError,
            match=f'\'Currency\' object has no attribute \'{attribute}\''):
        setattr(default, attribute, value)


@mark.parametrize('first,second,equal', [
    (euro_one, euro_one, True),
    (euro_one, euro_one_other, True),
    (euro_one, euro_minus_one, False),
    (euro_one, usd_one, False),
    (euro_one, '1.00', False)
])
def test_pycurrency_comparison_eq(first, second, equal):
    if equal:
        assert first == second
        assert first.__eq__(second)
    else:
        assert not first.__eq__(second)


@mark.parametrize('first,second,greater_equal,exception', [
    (euro_one, euro_one, True, None),
    (euro_one, euro_one_other, True, None),
    (euro_one, euro_minus_one, True, None),
    (euro_minus_one, euro_one, False, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_comparison_ge(first, second, greater_equal, exception):
    if exception:
        with raises(exception):
            first.__ge__(second)
    elif greater_equal:
        assert first >= second
        assert first.__ge__(second)
    else:
        assert not first >= second
        assert not first.__ge__(second)


@mark.parametrize('first,second,greater_than,exception', [
    (euro_one, euro_minus_one, True, None),
    (euro_one, euro_one, False, None),
    (euro_one, euro_one_other, False, None),
    (euro_minus_one, euro_one, False, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_comparison_gt(first, second, greater_than, exception):
    if exception:
        with raises(exception):
            first.__gt__(second)
    elif greater_than:
        assert first > second
        assert first.__gt__(second)
    else:
        assert not first > second
        assert not first.__gt__(second)


@mark.parametrize('first,second,less_equal,exception', [
    (euro_one, euro_one, True, None),
    (euro_one, euro_one_other, True, None),
    (euro_minus_one, euro_one, True, None),
    (euro_one, euro_minus_one, False, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_comparison_le(first, second, less_equal, exception):
    if exception:
        with raises(exception):
            first.__le__(second)
    elif less_equal:
        assert first <= second
        assert first.__le__(second)
    else:
        assert not first <= second
        assert not first.__le__(second)


@mark.parametrize('first,second,less_than,exception', [
    (euro_minus_one, euro_one, True, None),
    (euro_one, euro_one, False, None),
    (euro_one, euro_one_other, False, None),
    (euro_one, euro_minus_one, False, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_comparison_lt(first, second, less_than, exception):
    if exception:
        with raises(exception):
            first.__lt__(second)
    elif less_than:
        assert first < second
        assert first.__lt__(second)
    else:
        assert not first < second
        assert not first.__lt__(second)


@mark.parametrize('first,second,equal', [
    (euro_one, euro_one, True),
    (euro_one, euro_one_other, True),
    (euro_one, euro_minus_one, False),
    (euro_one, usd_one, False),
    (euro_one, '1.00', False)
])
def test_pycurrency_comparison_ne(first, second, equal):
    if equal:
        assert not first.__ne__(second)
    else:
        assert first != second
        assert first.__ne__(second)


@mark.parametrize('first,second,result,exception', [
    (euro_one, euro_one, euro_two, None),
    (euro_one, euro_one_other, euro_two, None),
    (euro_two, euro_minus_one, euro_one, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, 1.00, None, CurrencyTypeException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_math_add(first, second, result, exception):
    if exception:
        with raises(exception):
            first.__add__(second)
    else:
        assert (first + second) == result
        assert first.__add__(second) == result


@mark.parametrize('dividend,divisor,result,exception', [
    (euro_fifteen, 7, (euro_two, euro_one), None),
    (euro_fifteen, 16, (euro_zero, euro_fifteen), None),
    (euro_one, 0, None, ZeroDivisionError),
    (euro_one, usd_one, None, CurrencyInvalidDivision),
    (euro_one, '1.00', None, CurrencyInvalidDivision)
])
def test_pycurrency_math_divmod(dividend, divisor, result, exception):
    if exception:
        with raises(exception):
            dividend.__divmod__(divisor)
    else:
        assert divmod(dividend, divisor) == result
        assert dividend.__divmod__(divisor) == result


@mark.parametrize('dividend,divisor,result,exception', [
    (euro_fifteen, 7, euro_two, None),
    (euro_fifteen, 16, euro_zero, None),
    (euro_one, 0, None, ZeroDivisionError),
    (euro_one, usd_one, None, CurrencyInvalidDivision),
    (euro_one, '1.00', None, CurrencyInvalidDivision)
])
def test_pycurrency_math_floordiv(dividend, divisor, result, exception):
    if exception:
        with raises(exception):
            dividend.__floordiv__(divisor)
    else:
        assert (dividend // divisor) == result
        assert dividend.__floordiv__(divisor) == result


@mark.parametrize('dividend,divisor,result,exception', [
    (euro_fifteen, 4, euro_three, None),
    (euro_fifteen, 16, euro_fifteen, None),
    (euro_one, 0, None, ZeroDivisionError),
    (euro_one, usd_one, None, CurrencyInvalidDivision),
    (euro_one, '1.00', None, CurrencyInvalidDivision)
])
def test_pycurrency_math_mod(dividend, divisor, result, exception):
    if exception:
        with raises(exception):
            dividend.__mod__(divisor)
    else:
        assert (dividend % divisor) == result
        assert dividend.__mod__(divisor) == result


@mark.parametrize('first,second,result,exception', [
    (euro_one, 3, euro_three, None),
    (euro_two, 0, euro_zero, None),
    (euro_one, usd_one, None, CurrencyInvalidMultiplication),
    (euro_one, euro_three, None, CurrencyInvalidMultiplication),
    (euro_one, '1.00', None, CurrencyInvalidMultiplication)
])
def test_pycurrency_math_mul(first, second, result, exception):
    if exception:
        with raises(exception):
            first.__mul__(second)
    else:
        assert (first * second) == result
        assert (second * first) == result
        assert first.__mul__(second) == result
        assert first.__rmul__(second) == result


@mark.parametrize('first,second,result,exception', [
    (euro_two, euro_one, euro_one, None),
    (euro_one, euro_two, euro_minus_one, None),
    (euro_two, euro_minus_one, euro_three, None),
    (euro_one, usd_one, None, CurrencyMismatchException),
    (euro_one, 1.00, None, CurrencyTypeException),
    (euro_one, '1.00', None, CurrencyTypeException)
])
def test_pycurrency_math_sub(first, second, result, exception):
    if exception:
        with raises(exception):
            first.__sub__(second)
        with raises(exception):
            first.__rsub__(second)
    else:
        assert (first - second) == result
        assert first.__sub__(second) == result
        assert second.__rsub__(first) == result


@mark.parametrize('dividend,divisor,result,exception', [
    (euro_three, 3, euro_one, None),
    (euro_one, -1, euro_minus_one, None),
    (euro_one, 0, None, ZeroDivisionError),
    (euro_one, usd_one, None, CurrencyInvalidDivision),
    (euro_one, '1.00', None, CurrencyInvalidDivision)
])
def test_pycurrency_math_truediv(dividend, divisor, result, exception):
    if exception:
        with raises(exception):
            dividend.__truediv__(divisor)
    else:
        assert (dividend / divisor) == result
        assert dividend.__truediv__(divisor) == result


@mark.parametrize('currency,result', [
    (euro_one, euro_one),
    (euro_minus_one, euro_one)
])
def test_pycurrency_abs(currency, result):
    assert currency.__abs__() == result
    assert abs(currency) == result


@mark.parametrize('currency,result', [
    (euro_minus_one, True),
    (euro_zero, False),
    (euro_one, True)
])
def test_pycurrency_bool(currency, result):
    if result:
        assert currency
        assert currency.__bool__()
    else:
        assert not currency
        assert not currency.__bool__()


@mark.parametrize('currency,result', [
    (Currency(amount=1/7, alpha_code='EUR'), euro_one),
    (Currency(amount=-1/7, alpha_code='EUR'), euro_zero)
])
def test_pycurrency_ceil(currency, result):
    assert math.ceil(currency) == result
    assert currency.__ceil__() == result


def test_pycurrency_copy():
    euro = Currency(
        amount=1,
        alpha_code='EUR',
        numeric_code='978',
        symbol='€',
        localized_symbol='PT€',
        convertion='0123456789-',
        pattern=r'2,.3%-%s%u')
    new_euro = euro.__copy__()
    assert new_euro == euro
    assert new_euro is not euro
    assert new_euro.alpha_code == 'EUR'
    assert new_euro.numeric_code == '978'
    assert new_euro.symbol == '€'
    assert new_euro.localized_symbol == 'PT€'
    assert new_euro.convertion == '0123456789-'
    assert new_euro.pattern == r'2,.3%-%s%u'
    assert new_euro.__repr__() == (
        'Currency('
        'amount: 1, '
        'alpha_code: "EUR", '
        'numeric_code: "978", '
        'symbol: "€", '
        'localized_symbol: "PT€", '
        'convertion: "0123456789-", '
        'pattern: "2,.3%-%s%u")')
    assert new_euro.__str__() == '€1,00'


def test_pycurrency_deepcopy():
    euro = Currency(
        amount=1,
        alpha_code='EUR',
        numeric_code='978',
        symbol='€',
        localized_symbol='PT€',
        convertion='0123456789-',
        pattern=r'2,.3%-%s%u')
    new_euro = euro.__deepcopy__()
    assert new_euro == euro
    assert new_euro is not euro
    assert new_euro.alpha_code == 'EUR'
    assert new_euro.numeric_code == '978'
    assert new_euro.symbol == '€'
    assert new_euro.localized_symbol == 'PT€'
    assert new_euro.convertion == '0123456789-'
    assert new_euro.pattern == r'2,.3%-%s%u'
    assert new_euro.__repr__() == (
        'Currency('
        'amount: 1, '
        'alpha_code: "EUR", '
        'numeric_code: "978", '
        'symbol: "€", '
        'localized_symbol: "PT€", '
        'convertion: "0123456789-", '
        'pattern: "2,.3%-%s%u")')
    assert new_euro.__str__() == '€1,00'


@mark.parametrize('value,result', [
    (1/7, 0.14285714285714285),
    (0.3, 0.3),
    ('0.3', 0.3),
    (1/3, 0.3333333333333333)
])
def test_pycurrency_float(value, result):
    default = Currency(value)
    assert float(default) == result
    assert default.__float__() == result


@mark.parametrize('value,result', [
    (1/7, euro_zero),
    (1.5, euro_one)
])
def test_pycurrency_floor(value, result):
    default = Currency(amount=value, alpha_code='EUR')
    assert math.floor(default) == result
    assert default.__floor__() == result


@mark.parametrize('currency,pattern,result,exception', [
    (euro_custom_negative, 1, None, TypeError),
    (euro_custom_negative, '%a', '-142.857,14', None),
    (euro_custom_negative, '%A', '-142,857.14', None),
    (euro_custom_negative, '%c', 'EUR', None),
    (euro_custom_negative, '%s', '€', None),
    (euro_custom_negative, '%S', 'PT€', None),
    (euro_custom_negative, '%u', '142.857,14', None),
    (euro_custom_negative, '%U', '142,857.14', None),
    (euro_custom_negative, '%-', '-', None),
    (euro_custom_negative, '%%', '%', None),
    (euro_custom_negative, '1', '-€142.857,1', None),
    (euro_custom_negative, '_', '-€142.857_14', None),
    (euro_custom_negative, '.,', '-€142,857.14', None),
    (euro_custom_negative, '.,2', '-€14,28,57.14', None),
    (euro_custom_negative, '1.,2', '-€14,28,57.1', None),
    (euro_custom_negative, '0.,2', '-€14,28,57', None),
    (euro_custom_negative, '2.,0', '-€142857.14', None),
    (euro_custom_negative, '1.,%a', '-142,857.1', None),
    (euro_custom_negative, '%a\u00A0%S', '-142.857,14\xa0PT€', None),
    (euro_custom_negative, '%a\u00A0%c', '-142.857,14\xa0EUR', None),
    (euro_custom_negative, '', '-€142.857,14', None)
])
def test_pycurrency_format(currency, pattern, result, exception):
    if exception:
        with raises(exception):
            currency.__format__(pattern)
    else:
        assert format(currency, pattern) == result
        assert currency.__format__(pattern) == result


@mark.parametrize('value,result', [
    (1/7, 0),
    ('0.3', 0),
    (1.3, 1),
    (1.5, 1)
])
def test_pycurrency_int(value, result):
    default = Currency(value)
    assert int(default) == result
    assert default.__int__() == result


@mark.parametrize('currency,negation', [
    (euro_one, euro_minus_one),
    (euro_minus_one, euro_one)
])
def test_pycurrency_neg(currency, negation):
    assert currency != negation
    assert -currency == negation
    assert -currency.amount == negation.amount
    assert currency.__neg__() == negation
    assert currency.__neg__().amount == negation.amount


@mark.parametrize('currency,unary_plus', [
    (euro_one, euro_one),
    (euro_minus_one, euro_minus_one)
])
def test_pycurrency_pos(currency, unary_plus):
    assert currency == unary_plus
    assert +currency.amount == unary_plus.amount
    assert currency.__pos__() == unary_plus
    assert currency.__pos__().amount == unary_plus.amount


def test_pycurrency_reduce():
    representation = pickle.dumps(euro_custom_negative)
    unpickled_currency = pickle.loads(representation)
    assert euro_custom_negative == unpickled_currency


@mark.parametrize('value, decimals, rounded', [
    (1/7, 0, 0),
    (1/7, 2, 0.14),
    (1/7, 3, 0.143)
])
def test_pycurrency_round(value, decimals, rounded):
    orig = Currency(value)
    final = Currency(str(rounded))
    assert round(orig, decimals) == final
    assert round(orig, decimals).amount == Decimal(str(rounded))


@mark.parametrize('currency,is_signed', [
    (euro_one, False),
    (euro_minus_one, True)
])
def test_pycurrency_is_signed(currency, is_signed):
    if is_signed:
        assert currency.is_signed()
    else:
        assert not currency.is_signed()


@mark.parametrize('precision,result', [
    (None, '-PT€142.857,14'),
    (-1, '-PT€142.857'),
    (0, '-PT€142.857'),
    (1, '-PT€142.857,1'),
    (2, '-PT€142.857,14'),
    (3, '-PT€142.857,143'),
    (4, '-PT€142.857,1429')
])
def test_pycurrency_localized(precision, result):
    assert euro_custom_negative.localized(precision) == result


@mark.parametrize('currency,precision,result', [
    (Currency(1/7)*100_000, None, '14,285.71'),
    (Currency(1/7)*100_000, 0, '14,286'),
    (Currency(1/7)*100_000, 1, '14,285.7'),
    (Currency(1/7)*100_000, 2, '14,285.71'),
    (Currency(1/7)*100_000, 3, '14,285.714')
])
def test_pycurrency_precision(currency, precision, result):
    assert currency.precision(precision) == result


@mark.parametrize('currency,amount,string', [
    ((Currency('1.01') - Currency('0.99')) * 1e18, Decimal('2E+16'), '20,000,000,000,000,000.00'),
    (Currency('0.1') + Currency('0.1') + Currency('0.1'), Decimal('0.3'), '0.30')
])
def test_pycurrency_precision_amount(currency, amount, string):
    assert currency.amount == amount
    assert currency.__str__() == string


@mark.parametrize('precision,result', [
    (None, '-142,857.14\xa0EUR'),
    (-1, '-142,857\xa0EUR'),
    (0, '-142,857\xa0EUR'),
    (1, '-142,857.1\xa0EUR'),
    (2, '-142,857.14\xa0EUR'),
    (3, '-142,857.143\xa0EUR'),
    (4, '-142,857.1429\xa0EUR')
])
def test_pycurrency_international(precision, result):
    assert euro_custom_negative.international(precision) == result


@mark.parametrize('precision,result', [
    (None, '-142,857.14\xa0MMK'),
    (-1, '-142,857\xa0MMK'),
    (0, '-142,857\xa0MMK'),
    (1, '-142,857.1\xa0MMK'),
    (2, '-142,857.14\xa0MMK'),
    (3, '-142,857.143\xa0MMK'),
    (4, '-142,857.1429\xa0MMK')
])
def test_pycurrency_international_custom(precision, result):
    assert kyat_custom.international(precision) == result


@mark.parametrize('currency,rounding,results', [
    (Currency(1/7), 'ROUND_CEILING', {2: '0.15', 3: '0.143', 4: '0.1429'}),
    (Currency(1/7), 'ROUND_DOWN', {2: '0.14', 3: '0.142', 4: '0.1428'}),
    (Currency(1/7), 'ROUND_FLOOR', {2: '0.14', 3: '0.142', 4: '0.1428'}),
    (Currency(1/7), 'ROUND_HALF_DOWN', {2: '0.14', 3: '0.143', 4: '0.1429'}),
    (Currency(1/7), 'ROUND_HALF_EVEN', {2: '0.14', 3: '0.143', 4: '0.1429'}),
    (Currency(1/7), 'ROUND_HALF_UP', {2: '0.14', 3: '0.143', 4: '0.1429'}),
    (Currency(1/7), 'ROUND_UP', {2: '0.15', 3: '0.143', 4: '0.1429'}),
    (Currency(1/7), 'ROUND_05UP', {2: '0.14', 3: '0.142', 4: '0.1428'}),
    (Currency(-1/7), 'ROUND_CEILING', {2: '-0.14', 3: '-0.142', 4: '-0.1428'}),
    (Currency(-1/7), 'ROUND_DOWN', {2: '-0.14', 3: '-0.142', 4: '-0.1428'}),
    (Currency(-1/7), 'ROUND_FLOOR', {2: '-0.15', 3: '-0.143', 4: '-0.1429'}),
    (Currency(-1/7), 'ROUND_HALF_DOWN', {2: '-0.14', 3: '-0.143', 4: '-0.1429'}),
    (Currency(-1/7), 'ROUND_HALF_EVEN', {2: '-0.14', 3: '-0.143', 4: '-0.1429'}),
    (Currency(-1/7), 'ROUND_HALF_UP', {2: '-0.14', 3: '-0.143', 4: '-0.1429'}),
    (Currency(-1/7), 'ROUND_UP', {2: '-0.15', 3: '-0.143', 4: '-0.1429'}),
    (Currency(-1/7), 'ROUND_05UP', {2: '-0.14', 3: '-0.142', 4: '-0.1428'})
])
def test_pycurrency_rounding(currency, rounding, results):
    with localcontext() as context:
        context.rounding = rounding
        for precision, result in results.items():
            context.prec = precision
            test_currency = currency
            assert test_currency.precision(precision) == result
