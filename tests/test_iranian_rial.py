# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Iranian Rial representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, IranianRial
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_iranian_rial():
    """test_iranian_rial."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    iranian_rial = IranianRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iranian_rial.amount == decimal
    assert iranian_rial.numeric_code == '364'
    assert iranian_rial.alpha_code == 'IRR'
    assert iranian_rial.decimal_places == 2
    assert iranian_rial.decimal_sign == '.'
    assert iranian_rial.grouping_sign == ','
    assert not iranian_rial.international
    assert iranian_rial.symbol == '﷼'
    assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
    assert iranian_rial.__repr__() == (
        'IranianRial(amount: 0.1428571428571428571428571429, '
        'alpha_code: "IRR", '
        'symbol: "﷼", '
        'numeric_code: "364", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert iranian_rial.__str__() == '﷼0.14'


def test_iranian_rial_negative():
    """test_iranian_rial_negative."""
    amount = -100
    iranian_rial = IranianRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert iranian_rial.numeric_code == '364'
    assert iranian_rial.alpha_code == 'IRR'
    assert iranian_rial.decimal_places == 2
    assert iranian_rial.decimal_sign == '.'
    assert iranian_rial.grouping_sign == ','
    assert not iranian_rial.international
    assert iranian_rial.symbol == '﷼'
    assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
    assert iranian_rial.__repr__() == (
        'IranianRial(amount: -100, '
        'alpha_code: "IRR", '
        'symbol: "﷼", '
        'numeric_code: "364", '
        'decimal_places: "2", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: False)')
    assert iranian_rial.__str__() == '﷼-100.00'


def test_iranian_rial_custom():
    """test_iranian_rial_custom."""
    amount = 1000
    iranian_rial = IranianRial(
        amount=amount,
        decimal_places=5,
        decimal_sign=',',
        grouping_sign='.',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert iranian_rial.amount == decimal
    assert iranian_rial.numeric_code == '364'
    assert iranian_rial.alpha_code == 'IRR'
    assert iranian_rial.decimal_places == 5
    assert iranian_rial.decimal_sign == ','
    assert iranian_rial.grouping_sign == '.'
    assert iranian_rial.international
    assert iranian_rial.symbol == '﷼'
    assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
    assert iranian_rial.__repr__() == (
        'IranianRial(amount: 1000, '
        'alpha_code: "IRR", '
        'symbol: "﷼", '
        'numeric_code: "364", '
        'decimal_places: "5", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: True)')
    assert iranian_rial.__str__() == 'IRR 1.000,00000'


def test_iranian_rial_changed():
    """test_ciranian_rial_changed."""
    iranian_rial = IranianRial(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        iranian_rial.international = True


def test_iranian_rial_math_add():
    """test_iranian_rial_math_add."""
    iranian_rial_one = IranianRial(amount=1)
    iranian_rial_two = IranianRial(amount=2)
    iranian_rial_three = IranianRial(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency IRR and OTHER.'):
        _ = iranian_rial_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rial.IranianRial\'> '
                   'and <class \'str\'>.')):
        _ = iranian_rial_one.__add__('1.00')
    assert (iranian_rial_one + iranian_rial_two) == iranian_rial_three


def test_currency_slots():
    """test_currency_slots."""
    euro = IranianRial(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'IranianRial\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
