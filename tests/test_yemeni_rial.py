# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Yemeni Rial representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, YemeniRial
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_yemeni_rial():
    """test_yemeni_rial."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    yemeni_rial = YemeniRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert yemeni_rial.amount == decimal
    assert yemeni_rial.numeric_code == '886'
    assert yemeni_rial.alpha_code == 'YER'
    assert yemeni_rial.decimal_places == 2
    assert yemeni_rial.decimal_sign == '\u066B'
    assert yemeni_rial.grouping_sign == '\u066C'
    assert not yemeni_rial.international
    assert yemeni_rial.symbol == '﷼'
    assert not yemeni_rial.symbol_ahead
    assert yemeni_rial.symbol_separator == '\u00A0'
    assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
    assert yemeni_rial.__repr__() == (
        'YemeniRial(amount: 0.1428571428571428571428571429, '
        'alpha_code: "YER", '
        'symbol: "﷼", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "886", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert yemeni_rial.__str__() == '٠٫١٤ ﷼'


def test_yemeni_rial_negative():
    """test_yemeni_rial_negative."""
    amount = -100
    yemeni_rial = YemeniRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert yemeni_rial.numeric_code == '886'
    assert yemeni_rial.alpha_code == 'YER'
    assert yemeni_rial.decimal_places == 2
    assert yemeni_rial.decimal_sign == '\u066B'
    assert yemeni_rial.grouping_sign == '\u066C'
    assert not yemeni_rial.international
    assert yemeni_rial.symbol == '﷼'
    assert not yemeni_rial.symbol_ahead
    assert yemeni_rial.symbol_separator == '\u00A0'
    assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
    assert yemeni_rial.__repr__() == (
        'YemeniRial(amount: -100, '
        'alpha_code: "YER", '
        'symbol: "﷼", '
        'symbol_ahead: False, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "886", '
        'decimal_places: "2", '
        'decimal_sign: "\u066B", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert yemeni_rial.__str__() == '-١٠٠٫٠٠ ﷼'


def test_yemeni_rial_custom():
    """test_yemeni_rial_custom."""
    amount = 1000
    yemeni_rial = YemeniRial(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert yemeni_rial.amount == decimal
    assert yemeni_rial.numeric_code == '886'
    assert yemeni_rial.alpha_code == 'YER'
    assert yemeni_rial.decimal_places == 5
    assert yemeni_rial.decimal_sign == '\u066C'
    assert yemeni_rial.grouping_sign == '\u066B'
    assert yemeni_rial.international
    assert yemeni_rial.symbol == '﷼'
    assert not yemeni_rial.symbol_ahead
    assert yemeni_rial.symbol_separator == '_'
    assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
    assert yemeni_rial.__repr__() == (
        'YemeniRial(amount: 1000, '
        'alpha_code: "YER", '
        'symbol: "﷼", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "886", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert yemeni_rial.__str__() == 'YER 1,000.00000'


def test_yemeni_rial_changed():
    """test_cyemeni_rial_changed."""
    yemeni_rial = YemeniRial(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        yemeni_rial.international = True


def test_yemeni_rial_math_add():
    """test_yemeni_rial_math_add."""
    yemeni_rial_one = YemeniRial(amount=1)
    yemeni_rial_two = YemeniRial(amount=2)
    yemeni_rial_three = YemeniRial(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency YER and OTHER.'):
        _ = yemeni_rial_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rial.YemeniRial\'> '
                   'and <class \'str\'>.')):
        _ = yemeni_rial_one.__add__('1.00')
    assert (
        yemeni_rial_one +
        yemeni_rial_two) == yemeni_rial_three


def test_yemeni_rial_slots():
    """test_yemeni_rial_slots."""
    yemeni_rial = YemeniRial(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'YemeniRial\' '
                'object has no attribute \'new_variable\'')):
        yemeni_rial.new_variable = 'fail'  # pylint: disable=assigning-non-slot
