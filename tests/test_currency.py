# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Currency representation."""

import math
import pickle
from decimal import Context
from pytest import raises
from multicurrency import Currency, CurrencyContext
from multicurrency import (
    CurrencyMismatchException,
    CurrencyInvalidDivision,
    CurrencyInvalidMultiplication,
    CurrencyTypeException)

CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()

currency_euro_zero = Currency(amount=0, currency='EUR')
currency_euro_one = Currency(amount=1, currency='EUR')
currency_euro_two = Currency(amount=2, currency='EUR')
currency_euro_three = Currency(amount=3, currency='EUR')
currency_euro_fifteen = Currency(amount=15, currency='EUR')
currency_another_euro_one = Currency(amount=1, currency='EUR')
currency_another_euro_negative_one = Currency(amount=-1, currency='EUR')
currency_euro_negative_one = Currency(amount=-1, currency='EUR')
currency_euro_negative_two = Currency(amount=-2, currency='EUR')
currency_euro_negative_three = Currency(amount=-3, currency='EUR')
currency_usd_one = Currency(amount=1, currency='USD')
currency = Currency(
    amount=CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7),
    currency='EUR',
    symbol='€',
    code='978',
    decimal_places=2,
    decimal_sign=',',
    grouping_sign='.',
    international=True)


def test_currency_default():
    """test_currency_default."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    default = Currency(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert default.amount == decimal
    assert default.code == '0'
    assert default.currency == ''
    assert default.decimal_places == 2
    assert default.decimal_sign == '.'
    assert default.grouping_sign == ','
    assert not default.international
    assert default.symbol == ''
    assert default.__hash__() == hash((decimal, '', '0'))
    assert default.__repr__() == (
        'Currency(amount: 0.1428571428571428571428571429, currency: "", '
        'symbol: "", code: "0", decimal_places: "2", decimal_sign: ".", '
        'grouping_sign: ",", international: False)')
    assert default.__str__() == '0.14'


def test_currency_negative():
    """test_currency_negative."""
    amount = -100
    default = Currency(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert default.amount == decimal
    assert default.code == '0'
    assert default.currency == ''
    assert default.decimal_sign == '.'
    assert default.grouping_sign == ','
    assert not default.international
    assert default.symbol == ''
    assert default.__hash__() == hash((decimal, '', '0'))
    assert default.__repr__() == (
        'Currency(amount: -100, currency: "", symbol: "", code: "0", '
        'decimal_places: "2", decimal_sign: ".", grouping_sign: ",", '
        'international: False)')
    assert default.__str__() == '-100.00'


def test_currency_custom():
    """test_currency_custom."""
    amount = 1000
    euro = Currency(
        amount=amount,
        currency='EUR',
        symbol='€',
        code='978',
        decimal_places=2,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert euro.amount == decimal
    assert euro.code == '978'
    assert euro.currency == 'EUR'
    assert euro.decimal_places == 2
    assert euro.decimal_sign == ','
    assert euro.grouping_sign == '.'
    assert euro.international
    assert euro.symbol == '€'
    assert euro.__hash__() == hash((decimal, 'EUR', '978'))
    assert euro.__repr__() == (
        'Currency(amount: 1000, currency: "EUR", symbol: "€", code: "978", '
        'decimal_places: "2", decimal_sign: ",", grouping_sign: ".", '
        'international: True)')
    assert euro.__str__() == 'EUR 1.000,00'


def test_currency_decimal_places():
    """test_currency_decimal_places."""
    euro = Currency(
        amount=1000,
        currency='EUR',
        symbol='€',
        code='978',
        decimal_places=-2)
    assert euro.code == '978'
    assert euro.currency == 'EUR'
    assert euro.decimal_places == 0
    assert euro.__str__() == '€1,000'
    assert euro.pstr(-2) == '€1,000'
    assert euro.pstr(0) == '€1,000'
    assert euro.pstr(1) == '€1,000.0'


def test_currency_changed():
    """test_currency_changed."""
    euro = Currency(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        euro.international = True


def test_currency_slots():
    """test_currency_slots."""
    euro = Currency(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'Currency\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot


def test_currency_comparison_eq():
    """test_currency_comparison_eq."""
    assert currency_euro_one == currency_another_euro_one
    assert currency_euro_negative_one == currency_another_euro_negative_one
    assert currency_euro_one.__eq__(currency_another_euro_one)
    assert not currency_euro_one.__eq__(currency_euro_two)
    assert not currency_euro_one.__eq__(currency_usd_one)
    assert not currency_euro_one.__eq__('1.00')
    assert not currency_euro_negative_one.__eq__(currency_euro_negative_two)


def test_currency_comparison_ge():
    """test_currency_comparison_ge."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        currency_euro_one.__ge__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        currency_euro_one.__ge__('1.00')
    assert currency_euro_one >= currency_another_euro_one
    assert currency_euro_two >= currency_euro_one
    assert currency_euro_one.__ge__(currency_another_euro_one)
    assert currency_euro_two.__ge__(currency_euro_one)
    assert currency_euro_negative_one.__ge__(currency_euro_negative_two)
    assert currency_euro_negative_one.__ge__(
        currency_another_euro_negative_one)
    assert not currency_euro_one.__ge__(currency_euro_two)
    assert not currency_euro_negative_two.__ge__(currency_euro_negative_one)


def test_currency_comparison_gt():
    """test_currency_comparison_gt."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        currency_euro_one.__gt__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        currency_euro_one.__gt__('1.00')
    assert currency_euro_two > currency_euro_one
    assert currency_euro_two.__gt__(currency_euro_one)
    assert currency_euro_negative_one.__gt__(currency_euro_negative_two)
    assert not currency_euro_one.__gt__(currency_another_euro_one)
    assert not currency_euro_negative_one.__lt__(
        currency_another_euro_negative_one)


def test_currency_comparison_le():
    """test_currency_comparison_le."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        currency_euro_one.__le__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        currency_euro_one.__le__('1.00')
    assert currency_euro_one <= currency_another_euro_one
    assert currency_euro_one <= currency_euro_two
    assert currency_euro_one.__le__(currency_another_euro_one)
    assert currency_euro_one.__le__(currency_euro_two)
    assert currency_euro_negative_two.__le__(currency_euro_negative_one)
    assert currency_euro_negative_one.__ge__(
        currency_another_euro_negative_one)
    assert not currency_euro_two.__le__(currency_euro_one)
    assert not currency_euro_negative_one.__le__(currency_euro_negative_two)


def test_currency_comparison_lt():
    """test_currency_comparison_lt."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        currency_euro_one.__lt__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        currency_euro_one.__lt__('1.00')
    assert currency_euro_one < currency_euro_two
    assert currency_euro_one.__lt__(currency_euro_two)
    assert currency_euro_negative_two.__lt__(currency_euro_negative_one)
    assert not currency_euro_one.__lt__(currency_another_euro_one)
    assert not currency_euro_negative_one.__lt__(
        currency_another_euro_negative_one)


def test_currency_comparison_ne():
    """test_currency_comparison_ne."""
    assert currency_euro_one != currency_euro_two
    assert currency_euro_negative_one != currency_euro_negative_two
    assert currency_euro_one.__ne__(currency_euro_two)
    assert currency_euro_one.__ne__(currency_usd_one)
    assert currency_euro_one.__ne__('1.00')
    assert not currency_euro_one.__ne__(currency_another_euro_one)
    assert not currency_euro_negative_one.__ne__(
        currency_another_euro_negative_one)


def test_currency_math_add():
    """test_currency_math_add."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        _ = currency_euro_one.__add__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_one.__add__('1.00')
    assert (currency_euro_one + currency_euro_two) == currency_euro_three
    assert (currency_euro_negative_one + currency_euro_negative_two) == (
        currency_euro_negative_three)


def test_currency_math_divmod():
    """test_currency_math_divmod."""
    with raises(
            CurrencyInvalidDivision,
            match=('division not supported between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_fifteen.__divmod__('1')
    with raises(
            ZeroDivisionError,
            match=''):
        _ = currency_euro_fifteen.__divmod__(0)
    assert divmod(currency_euro_fifteen, 7) == (
        currency_euro_two, currency_euro_one)
    assert divmod(currency_euro_fifteen, 16) == (
        currency_euro_zero, currency_euro_fifteen)
    assert currency_euro_fifteen.__divmod__(7) == (
        currency_euro_two, currency_euro_one)


def test_currency_math_floordiv():
    """test_currency_math_floordiv."""
    with raises(
            CurrencyInvalidDivision,
            match=('division not supported between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_fifteen.__floordiv__('1')
    with raises(
            ZeroDivisionError,
            match=''):
        _ = currency_euro_fifteen.__floordiv__(0)
    assert (currency_euro_fifteen // 7) == currency_euro_two
    assert (currency_euro_fifteen // 16) == currency_euro_zero
    assert currency_euro_fifteen.__floordiv__(7) == currency_euro_two


def test_currency_math_mod():
    """test_currency_math_mod."""
    with raises(
            CurrencyInvalidDivision,
            match=('division not supported between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_fifteen.__mod__('1')
    with raises(
            ZeroDivisionError,
            match=''):
        _ = currency_euro_fifteen.__mod__(0)
    assert (currency_euro_fifteen % 4) == currency_euro_three
    assert (currency_euro_fifteen % 16) == currency_euro_fifteen
    assert currency_euro_fifteen.__mod__(4) == currency_euro_three


def test_currency_math_mul_rmul():
    """test_currency_math_mul_rmul."""
    with raises(
            CurrencyInvalidMultiplication,
            match=('multiplication not supported between <class '
                   '\'multicurrency.currency.Currency\'> and <class '
                   '\'str\'>.')):
        _ = currency_euro_one.__mul__('1')
    assert (currency_euro_one * 3) == currency_euro_three
    assert (3 * currency_euro_one) == currency_euro_three
    assert currency_euro_one.__mul__(3) == currency_euro_three


def test_currency_math_sub():
    """test_currency_math_sub."""
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency EUR and USD.'):
        _ = currency_euro_one.__sub__(currency_usd_one)
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_one.__sub__('1.00')
    assert (currency_euro_three - currency_euro_one) == currency_euro_two
    assert (currency_euro_negative_three - currency_euro_negative_one) == (
        currency_euro_negative_two)


def test_currency_math_truediv():
    """test_currency_math_truediv."""
    with raises(
            CurrencyInvalidDivision,
            match=('division not supported between <class \'multicurrency.'
                   'currency.Currency\'> and <class \'str\'>.')):
        _ = currency_euro_one.__truediv__('1')
    with raises(
            ZeroDivisionError,
            match=''):
        _ = currency_euro_one.__truediv__(0)
    assert (currency_euro_three / 3) == currency_euro_one
    assert currency_euro_three.__truediv__(3) == currency_euro_one


def test_currency_abs():
    """test_currency_abs."""
    assert abs(currency_euro_one) == currency_euro_one
    assert abs(currency_euro_negative_one) == currency_euro_one
    assert currency_euro_one.__abs__() == currency_euro_one
    assert currency_euro_negative_one.__abs__() == currency_euro_one


def test_currency_bool():
    """test_currency_bool."""
    assert not currency_euro_zero
    assert currency_euro_one
    assert not currency_euro_zero.__bool__()
    assert currency_euro_one.__bool__()


def test_currency_ceil():
    """test_currency_ceil."""
    assert math.ceil(currency) == currency_euro_one
    assert currency.__ceil__() == currency_euro_one


def test_currency_copy():
    """test_currency_copy."""
    new_currency = currency.__copy__()
    assert new_currency == currency
    assert new_currency.code == '978'
    assert new_currency.currency == 'EUR'
    assert new_currency.decimal_places == 2
    assert new_currency.decimal_sign == ','
    assert new_currency.grouping_sign == '.'
    assert new_currency.international
    assert new_currency.symbol == '€'
    assert new_currency.__repr__() == (
        'Currency(amount: 0.1428571428571428571428571429, currency: "EUR", '
        'symbol: "€", code: "978", decimal_places: "2", decimal_sign: ",", '
        'grouping_sign: ".", international: True)')
    assert new_currency.__str__() == 'EUR 0,14'


def test_currency_float():
    """test_currency_float."""
    #assert float(currency) == 0.143
    #assert currency.__float__() == 0.143
    assert float(currency) == 0.14285714285714285
    assert currency.__float__() == 0.14285714285714285


def test_currency_floor():
    """test_currency_floor."""
    assert math.floor(currency) == currency_euro_zero
    assert currency.__floor__() == currency_euro_zero


def test_currency_int():
    """test_currency_int."""
    assert int(currency) == 0
    assert currency.__int__() == 0


def test_currency_neg():
    """test_currency_neg."""
    assert currency != -currency
    assert currency.amount != -currency.amount
    assert currency_euro_negative_one == -currency_euro_one
    assert currency_euro_negative_one.amount == -currency_euro_one.amount
    assert currency != currency.__neg__()
    assert currency_euro_negative_one == currency_euro_one.__neg__()


def test_currency_pos():
    """test_currency_pos."""
    assert currency == +currency
    assert currency.amount == +currency.amount
    assert currency == currency.__pos__()
    assert currency.amount == currency.amount.__pos__()


def test_currency_reduce():
    """test_currency_reduce."""
    representation = pickle.dumps(currency)
    unpickled_currency = pickle.loads(representation)
    assert currency == unpickled_currency


def test_currency_round():
    """test_currency_round."""
    assert round(currency).amount == CONTEXT.create_decimal('0')
    assert round(currency, 2).amount == round(
        CONTEXT.create_decimal('0.14'), 2)


def test_currency_is_signed():
    """test_currency_is_signed."""
    assert currency_euro_negative_one.is_signed()
    assert not currency_euro_one.is_signed()


def test_currency_precision():
    """test_currency_precision."""
    test_currency = (Currency(1.01) - Currency(0.99)) * 1e18
    assert test_currency.amount == (
        (CONTEXT.create_decimal('1.01') - CONTEXT.create_decimal('0.99')) *
        CONTEXT.create_decimal('1e18'))
    assert test_currency.__str__() == '20,000,000,000,000,000.00'


def test_currency_roundings_positive():
    """test_currency_roundings_positive."""
    roundings = {
        'ROUND_CEILING': {2: '0.15', 3: '0.143', 4: '0.1429'},
        'ROUND_DOWN': {2: '0.14', 3: '0.142', 4: '0.1428'},
        'ROUND_FLOOR': {2: '0.14', 3: '0.142', 4: '0.1428'},
        'ROUND_HALF_DOWN': {2: '0.14', 3: '0.143', 4: '0.1429'},
        'ROUND_HALF_EVEN': {2: '0.14', 3: '0.143', 4: '0.1429'},
        'ROUND_HALF_UP': {2: '0.14', 3: '0.143', 4: '0.1429'},
        'ROUND_UP': {2: '0.15', 3: '0.143', 4: '0.1429'},
        'ROUND_05UP': {2: '0.14', 3: '0.142', 4: '0.1428'}}
    for mode, results in roundings.items():
        CurrencyContext.rounding = mode
        for precision, result in results.items():
            CurrencyContext.prec = precision
            test_currency = currency_euro_one / 7
            assert test_currency.pstr(precision) == result
    CurrencyContext.rounding = 'ROUND_HALF_EVEN'
    CurrencyContext.prec = 28


def test_currency_roundings_negative():
    """test_currency_roundings_negative."""
    roundings = {
        'ROUND_CEILING': {2: '-0.14', 3: '-0.142', 4: '-0.1428'},
        'ROUND_DOWN': {2: '-0.14', 3: '-0.142', 4: '-0.1428'},
        'ROUND_FLOOR': {2: '-0.15', 3: '-0.143', 4: '-0.1429'},
        'ROUND_HALF_DOWN': {2: '-0.14', 3: '-0.143', 4: '-0.1429'},
        'ROUND_HALF_EVEN': {2: '-0.14', 3: '-0.143', 4: '-0.1429'},
        'ROUND_HALF_UP': {2: '-0.14', 3: '-0.143', 4: '-0.1429'},
        'ROUND_UP': {2: '-0.15', 3: '-0.143', 4: '-0.1429'},
        'ROUND_05UP': {2: '-0.14', 3: '-0.142', 4: '-0.1428'}}
    for mode, results in roundings.items():
        CurrencyContext.rounding = mode
        for precision, result in results.items():
            CurrencyContext.prec = precision
            test_currency = currency_euro_negative_one / 7
            assert test_currency.pstr(precision) == result
    CurrencyContext.rounding = 'ROUND_HALF_EVEN'
    CurrencyContext.prec = 28