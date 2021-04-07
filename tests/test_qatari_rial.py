# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Qatari Rial representation."""

from decimal import Context
from pytest import raises
from multicurrency import Currency, QatariRial
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


def test_qatari_rial():
    """test_qatari_rial."""
    amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
    qatari_rial = QatariRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert qatari_rial.amount == decimal
    assert qatari_rial.code == '634'
    assert qatari_rial.currency == 'QAR'
    assert qatari_rial.decimal_places == 2
    assert qatari_rial.decimal_sign == ','
    assert qatari_rial.grouping_sign == '.'
    assert not qatari_rial.international
    assert qatari_rial.symbol == 'ر.ق'
    assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
    assert qatari_rial.__repr__() == (
        'QatariRial(amount: 0.1428571428571428571428571429, '
        'currency: "QAR", '
        'symbol: "ر.ق", '
        'code: "634", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert qatari_rial.__str__() == 'ر.ق0,14'


def test_qatari_rial_negative():
    """test_qatari_rial_negative."""
    amount = -100
    qatari_rial = QatariRial(amount=amount)
    decimal = CONTEXT.create_decimal(amount)
    assert qatari_rial.code == '634'
    assert qatari_rial.currency == 'QAR'
    assert qatari_rial.decimal_places == 2
    assert qatari_rial.decimal_sign == ','
    assert qatari_rial.grouping_sign == '.'
    assert not qatari_rial.international
    assert qatari_rial.symbol == 'ر.ق'
    assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
    assert qatari_rial.__repr__() == (
        'QatariRial(amount: -100, '
        'currency: "QAR", '
        'symbol: "ر.ق", '
        'code: "634", '
        'decimal_places: "2", '
        'decimal_sign: ",", '
        'grouping_sign: ".", '
        'international: False)')
    assert qatari_rial.__str__() == 'ر.ق-100,00'


def test_qatari_rial_custom():
    """test_qatari_rial_custom."""
    amount = 1000
    qatari_rial = QatariRial(
        amount=amount,
        decimal_places=5,
        decimal_sign='.',
        grouping_sign=',',
        international=True)
    decimal = CONTEXT.create_decimal(amount)
    assert qatari_rial.amount == decimal
    assert qatari_rial.code == '634'
    assert qatari_rial.currency == 'QAR'
    assert qatari_rial.decimal_places == 5
    assert qatari_rial.decimal_sign == '.'
    assert qatari_rial.grouping_sign == ','
    assert qatari_rial.international
    assert qatari_rial.symbol == 'ر.ق'
    assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
    assert qatari_rial.__repr__() == (
        'QatariRial(amount: 1000, '
        'currency: "QAR", '
        'symbol: "ر.ق", '
        'code: "634", '
        'decimal_places: "5", '
        'decimal_sign: ".", '
        'grouping_sign: ",", '
        'international: True)')
    assert qatari_rial.__str__() == 'QAR 1,000.00000'


def test_qatari_rial_changed():
    """test_cqatari_rial_changed."""
    qatari_rial = QatariRial(amount=1000)
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.amount = 999
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.currency = 'EUR'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.symbol = '€'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.code = '978'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.decimal_places = 3
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.decimal_sign = ','
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.grouping_sign = '.'
    with raises(
            AttributeError,
            match='can\'t set attribute'):
        qatari_rial.international = True


def test_qatari_rial_math_add():
    """test_qatari_rial_math_add."""
    qatari_rial_one = QatariRial(amount=1)
    qatari_rial_two = QatariRial(amount=2)
    qatari_rial_three = QatariRial(amount=3)
    currency = Currency(amount=1, currency='OTHER')
    with raises(
            CurrencyMismatchException,
            match='unsupported operation between currency QAR and OTHER.'):
        _ = qatari_rial_one + currency
    with raises(
            CurrencyTypeException,
            match=('unsupported operation between <class \'multicurrency.'
                   'rial.QatariRial\'> '
                   'and <class \'str\'>.')):
        _ = qatari_rial_one.__add__('1.00')
    assert (qatari_rial_one + qatari_rial_two) == qatari_rial_three


def test_currency_slots():
    """test_currency_slots."""
    euro = QatariRial(amount=1000)
    with raises(
            AttributeError,
            match=(
                '\'QatariRial\' '
                'object has no attribute \'new_variable\'')):
        euro.new_variable = 'fail'  # pylint: disable=assigning-non-slot
