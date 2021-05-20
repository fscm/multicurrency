# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Bolivar Fuerte representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, BolivarFuerte
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_bolivar_fuerte():
    """test_bolivar_fuerte."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    bolivar_fuerte = BolivarFuerte(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bolivar_fuerte.amount == decimal
    assert bolivar_fuerte.numeric_code == '937'
    assert bolivar_fuerte.alpha_code == 'VEF'
    assert bolivar_fuerte.decimal_places == 2
    assert bolivar_fuerte.decimal_sign == ','
    assert bolivar_fuerte.grouping_sign == '.'
    assert not bolivar_fuerte.international
    assert bolivar_fuerte.symbol == 'Bs.F.'
    assert bolivar_fuerte.symbol_ahead
    assert bolivar_fuerte.symbol_separator == '\u00A0'
    assert bolivar_fuerte.convertion == ''
    assert bolivar_fuerte.__hash__() == hash((decimal, 'VEF', '937'))
    assert bolivar_fuerte.__repr__() == (
        'BolivarFuerte(amount: 0.1428571428571428571428571429, '
        'alpha_code: "VEF", '
        'symbol: "Bs.F.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "937", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert bolivar_fuerte.__str__() == 'Bs.F. 0,14'


def test_bolivar_fuerte_negative():
    """test_bolivar_fuerte_negative."""
    amount = -100
    bolivar_fuerte = BolivarFuerte(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert bolivar_fuerte.numeric_code == '937'
    assert bolivar_fuerte.alpha_code == 'VEF'
    assert bolivar_fuerte.decimal_places == 2
    assert bolivar_fuerte.decimal_sign == ','
    assert bolivar_fuerte.grouping_sign == '.'
    assert not bolivar_fuerte.international
    assert bolivar_fuerte.symbol == 'Bs.F.'
    assert bolivar_fuerte.symbol_ahead
    assert bolivar_fuerte.symbol_separator == '\u00A0'
    assert bolivar_fuerte.convertion == ''
    assert bolivar_fuerte.__hash__() == hash((decimal, 'VEF', '937'))
    assert bolivar_fuerte.__repr__() == (
        'BolivarFuerte(amount: -100, '
        'alpha_code: "VEF", '
        'symbol: "Bs.F.", '
        'symbol_ahead: True, '
        'symbol_separator: "\u00A0", '
        'numeric_code: "937", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'convertion: "", '
        'international: False)')
    assert bolivar_fuerte.__str__() == 'Bs.F. -100,00'


def test_bolivar_fuerte_custom():
    """test_bolivar_fuerte_custom."""
    amount = 1000
    bolivar_fuerte = BolivarFuerte(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True,
        symbol_ahead=False,
        symbol_separator='_')
    decimal = CONTEXT.create_decimal(amount)
    assert bolivar_fuerte.amount == decimal
    assert bolivar_fuerte.numeric_code == '937'
    assert bolivar_fuerte.alpha_code == 'VEF'
    assert bolivar_fuerte.decimal_places == 5
    assert bolivar_fuerte.decimal_sign == '.'
    assert bolivar_fuerte.grouping_sign == ','
    assert bolivar_fuerte.international
    assert bolivar_fuerte.symbol == 'Bs.F.'
    assert not bolivar_fuerte.symbol_ahead
    assert bolivar_fuerte.symbol_separator == '_'
    assert bolivar_fuerte.convertion == ''
    assert bolivar_fuerte.__hash__() == hash((decimal, 'VEF', '937'))
    assert bolivar_fuerte.__repr__() == (
        'BolivarFuerte(amount: 1000, '
        'alpha_code: "VEF", '
        'symbol: "Bs.F.", '
        'symbol_ahead: False, '
        'symbol_separator: "_", '
        'numeric_code: "937", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'convertion: "", '
        'international: True)')
    assert bolivar_fuerte.__str__() == 'VEF 1,000.00000'


def test_bolivar_fuerte_changed():
    """test_cbolivar_fuerte_changed."""
    bolivar_fuerte = BolivarFuerte(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.alpha_code = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.convertion = '0123456789,.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.symbol_ahead = False
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.symbol_separator = '_'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.numeric_code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        bolivar_fuerte.international = True


def test_bolivar_fuerte_math_add():
    """test_bolivar_fuerte_math_add."""
    bolivar_fuerte_one = BolivarFuerte(amount=1)
    bolivar_fuerte_two = BolivarFuerte(amount=2)
    bolivar_fuerte_three = BolivarFuerte(amount=3)
    currency = Currency(amount=1, alpha_code='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency VEF and OTHER.'):
        _ = bolivar_fuerte_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'fuerte.BolivarFuerte\'> '
                   'and <class \'str\'>.')):
        _ = bolivar_fuerte_one.__add__('1.00')
    assert (
        bolivar_fuerte_one +
        bolivar_fuerte_two) == bolivar_fuerte_three


def test_bolivar_fuerte_slots():
    """test_bolivar_fuerte_slots."""
    bolivar_fuerte = BolivarFuerte(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'BolivarFuerte\' '
                'object has no attribute \'new_variable\'')):
        bolivar_fuerte.new_variable = 'fail'  # pylint: disable=assigning-non-slot
