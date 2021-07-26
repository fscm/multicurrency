# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rial Omani representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, RialOmani
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_rial_omani():
    """test_rial_omani."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    rial_omani = RialOmani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rial_omani.amount == decimal
    assert rial_omani.numeric_code == '512'
    assert rial_omani.alpha_code == 'OMR'
    assert rial_omani.decimal_places == 3
    assert rial_omani.decimal_sign == '\u066B'
    assert rial_omani.grouping_places == 3
    assert rial_omani.grouping_sign == '\u066C'
    assert not rial_omani.international
    assert rial_omani.symbol == 'ر.ع.'
    assert rial_omani.symbol_ahead
    assert rial_omani.symbol_separator == '\u00A0'
    assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
    assert rial_omani.__repr__() == (
        'RialOmani(amount: 0.1428571428571428571428571429, '
        'alpha_code: "OMR", '
        'symbol: "ر.ع.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "512", '
        'decimal_places: "3", '
        'decimal_sign: "\u066B", '
        'grouping_places: "3", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert rial_omani.__str__() == 'ر.ع. ٠٫١٤٣'


def test_rial_omani_negative():
    """test_rial_omani_negative."""
    amount = -100
    rial_omani = RialOmani(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert rial_omani.numeric_code == '512'
    assert rial_omani.alpha_code == 'OMR'
    assert rial_omani.decimal_places == 3
    assert rial_omani.decimal_sign == '\u066B'
    assert rial_omani.grouping_places == 3
    assert rial_omani.grouping_sign == '\u066C'
    assert not rial_omani.international
    assert rial_omani.symbol == 'ر.ع.'
    assert rial_omani.symbol_ahead
    assert rial_omani.symbol_separator == '\u00A0'
    assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
    assert rial_omani.__repr__() == (
        'RialOmani(amount: -100, '
        'alpha_code: "OMR", '
        'symbol: "ر.ع.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "512", '
        'decimal_places: "3", '
        'decimal_sign: "\u066B", '
        'grouping_places: "3", '
        'grouping_sign: "\u066C", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: False)')
    assert rial_omani.__str__() == 'ر.ع. -١٠٠٫٠٠٠'


def test_rial_omani_custom():
    """test_rial_omani_custom."""
    amount = 1000
    rial_omani = RialOmani(
        amount=amount,
        decimal_places=5,
        decimal_sign='\u066C',
        grouping_places=2,
        grouping_sign='\u066B',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert rial_omani.amount == decimal
    assert rial_omani.numeric_code == '512'
    assert rial_omani.alpha_code == 'OMR'
    assert rial_omani.decimal_places == 5
    assert rial_omani.decimal_sign == '\u066C'
    assert rial_omani.grouping_places == 2
    assert rial_omani.grouping_sign == '\u066B'
    assert rial_omani.international
    assert rial_omani.symbol == 'ر.ع.'
    assert not rial_omani.symbol_ahead
    assert rial_omani.symbol_separator == '_'
    assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
    assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
    assert rial_omani.__repr__() == (
        'RialOmani(amount: 1000, '
        'alpha_code: "OMR", '
        'symbol: "ر.ع.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "512", '
        'decimal_places: "5", '
        'decimal_sign: "\u066C", '
        'grouping_places: "2", '
        'grouping_sign: "\u066B", '
        'convertion: "٠١٢٣٤٥٦٧٨٩-", '
        'international: True)')
    assert rial_omani.__str__() == 'OMR 10,00.00000'


def test_rial_omani_changed():
    """test_crial_omani_changed."""
    rial_omani = RialOmani(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.grouping_places = 4
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        rial_omani.international = True


def test_rial_omani_math_add():
    """test_rial_omani_math_add."""
    rial_omani_one = RialOmani(amount=1)
    rial_omani_two = RialOmani(amount=2)
    rial_omani_three = RialOmani(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency OMR and OTHER.'):
        _ = rial_omani_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rial.RialOmani\'> '
                   'and <class \'str\'>.')):
        _ = rial_omani_one.__add__('1.00')
    assert (
        rial_omani_one +
        rial_omani_two) == rial_omani_three


def test_rial_omani_slots():
    """test_rial_omani_slots."""
    rial_omani = RialOmani(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'RialOmani\' '
                'object has no attribute \'new_variable\'')):
        rial_omani.new_variable = 'fail'  # pylint: disable=assigning-non-slot
