# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Leu currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)
from multicurrency import (
    MoldovanLeu,
    Leu)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Moldovan Leu representation."""


class TestMoldovanLeu:
    """MoldovanLeu currency tests."""

    def test_moldovan_leu(self):
        """test_moldovan_leu."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        moldovan_leu = MoldovanLeu(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert moldovan_leu.amount == decimal
        assert moldovan_leu.numeric_code == '498'
        assert moldovan_leu.alpha_code == 'MDL'
        assert moldovan_leu.decimal_places == 2
        assert moldovan_leu.decimal_sign == ','
        assert moldovan_leu.grouping_places == 3
        assert moldovan_leu.grouping_sign == '.'
        assert not moldovan_leu.international
        assert moldovan_leu.symbol == 'L'
        assert not moldovan_leu.symbol_ahead
        assert moldovan_leu.symbol_separator == '\u00A0'
        assert moldovan_leu.localized_symbol == 'L'
        assert moldovan_leu.convertion == ''
        assert moldovan_leu.__hash__() == hash(
            (moldovan_leu.__class__, decimal, 'MDL', '498'))
        assert moldovan_leu.__repr__() == (
            'MoldovanLeu(amount: 0.1428571428571428571428571429, '
            'alpha_code: "MDL", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "498", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert moldovan_leu.__str__() == '0,14 L'

    def test_moldovan_leu_negative(self):
        """test_moldovan_leu_negative."""
        amount = -100
        moldovan_leu = MoldovanLeu(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert moldovan_leu.numeric_code == '498'
        assert moldovan_leu.alpha_code == 'MDL'
        assert moldovan_leu.decimal_places == 2
        assert moldovan_leu.decimal_sign == ','
        assert moldovan_leu.grouping_places == 3
        assert moldovan_leu.grouping_sign == '.'
        assert not moldovan_leu.international
        assert moldovan_leu.symbol == 'L'
        assert not moldovan_leu.symbol_ahead
        assert moldovan_leu.symbol_separator == '\u00A0'
        assert moldovan_leu.localized_symbol == 'L'
        assert moldovan_leu.convertion == ''
        assert moldovan_leu.__hash__() == hash(
            (moldovan_leu.__class__, decimal, 'MDL', '498'))
        assert moldovan_leu.__repr__() == (
            'MoldovanLeu(amount: -100, '
            'alpha_code: "MDL", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "498", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert moldovan_leu.__str__() == '-100,00 L'

    def test_moldovan_leu_custom(self):
        """test_moldovan_leu_custom."""
        amount = 1000
        moldovan_leu = MoldovanLeu(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert moldovan_leu.amount == decimal
        assert moldovan_leu.numeric_code == '498'
        assert moldovan_leu.alpha_code == 'MDL'
        assert moldovan_leu.decimal_places == 5
        assert moldovan_leu.decimal_sign == '.'
        assert moldovan_leu.grouping_places == 2
        assert moldovan_leu.grouping_sign == ','
        assert moldovan_leu.international
        assert moldovan_leu.symbol == 'L'
        assert not moldovan_leu.symbol_ahead
        assert moldovan_leu.symbol_separator == '_'
        assert moldovan_leu.localized_symbol == 'L'
        assert moldovan_leu.convertion == ''
        assert moldovan_leu.__hash__() == hash(
            (moldovan_leu.__class__, decimal, 'MDL', '498'))
        assert moldovan_leu.__repr__() == (
            'MoldovanLeu(amount: 1000, '
            'alpha_code: "MDL", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "L", '
            'numeric_code: "498", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert moldovan_leu.__str__() == 'MDL 10,00.00000'

    def test_moldovan_leu_changed(self):
        """test_cmoldovan_leu_changed."""
        moldovan_leu = MoldovanLeu(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            moldovan_leu.international = True

    def test_moldovan_leu_math_add(self):
        """test_moldovan_leu_math_add."""
        moldovan_leu_one = MoldovanLeu(amount=1)
        moldovan_leu_two = MoldovanLeu(amount=2)
        moldovan_leu_three = MoldovanLeu(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency MDL and OTHER.'):
            _ = moldovan_leu_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'leu.MoldovanLeu\'> '
                    'and <class \'str\'>.')):
            _ = moldovan_leu_one.__add__('1.00')
        assert (
            moldovan_leu_one +
            moldovan_leu_two) == moldovan_leu_three

    def test_moldovan_leu_slots(self):
        """test_moldovan_leu_slots."""
        moldovan_leu = MoldovanLeu(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'MoldovanLeu\' '
                    'object has no attribute \'new_variable\'')):
            moldovan_leu.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Leu representation."""


class TestLeu:
    """Leu currency tests."""

    def test_leu(self):
        """test_leu."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        leu = Leu(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert leu.amount == decimal
        assert leu.numeric_code == '946'
        assert leu.alpha_code == 'RON'
        assert leu.decimal_places == 2
        assert leu.decimal_sign == ','
        assert leu.grouping_places == 3
        assert leu.grouping_sign == '.'
        assert not leu.international
        assert leu.symbol == 'L'
        assert not leu.symbol_ahead
        assert leu.symbol_separator == '\u00A0'
        assert leu.localized_symbol == 'L'
        assert leu.convertion == ''
        assert leu.__hash__() == hash(
            (leu.__class__, decimal, 'RON', '946'))
        assert leu.__repr__() == (
            'Leu(amount: 0.1428571428571428571428571429, '
            'alpha_code: "RON", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "946", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert leu.__str__() == '0,14 L'

    def test_leu_negative(self):
        """test_leu_negative."""
        amount = -100
        leu = Leu(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert leu.numeric_code == '946'
        assert leu.alpha_code == 'RON'
        assert leu.decimal_places == 2
        assert leu.decimal_sign == ','
        assert leu.grouping_places == 3
        assert leu.grouping_sign == '.'
        assert not leu.international
        assert leu.symbol == 'L'
        assert not leu.symbol_ahead
        assert leu.symbol_separator == '\u00A0'
        assert leu.localized_symbol == 'L'
        assert leu.convertion == ''
        assert leu.__hash__() == hash(
            (leu.__class__, decimal, 'RON', '946'))
        assert leu.__repr__() == (
            'Leu(amount: -100, '
            'alpha_code: "RON", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "L", '
            'numeric_code: "946", '
            'decimal_places: "2", '
            'decimal_sign: ",", '
            'grouping_places: "3", '
            'grouping_sign: ".", '
            'convertion: "", '
            'international: False)')
        assert leu.__str__() == '-100,00 L'

    def test_leu_custom(self):
        """test_leu_custom."""
        amount = 1000
        leu = Leu(
            amount=amount,
            decimal_places=5,
            decimal_sign='.',
            grouping_places=2,
            grouping_sign=',',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert leu.amount == decimal
        assert leu.numeric_code == '946'
        assert leu.alpha_code == 'RON'
        assert leu.decimal_places == 5
        assert leu.decimal_sign == '.'
        assert leu.grouping_places == 2
        assert leu.grouping_sign == ','
        assert leu.international
        assert leu.symbol == 'L'
        assert not leu.symbol_ahead
        assert leu.symbol_separator == '_'
        assert leu.localized_symbol == 'L'
        assert leu.convertion == ''
        assert leu.__hash__() == hash(
            (leu.__class__, decimal, 'RON', '946'))
        assert leu.__repr__() == (
            'Leu(amount: 1000, '
            'alpha_code: "RON", '
            'symbol: "L", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "L", '
            'numeric_code: "946", '
            'decimal_places: "5", '
            'decimal_sign: ".", '
            'grouping_places: "2", '
            'grouping_sign: ",", '
            'convertion: "", '
            'international: True)')
        assert leu.__str__() == 'RON 10,00.00000'

    def test_leu_changed(self):
        """test_cleu_changed."""
        leu = Leu(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.numeric_code = '978'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.decimal_places = 3
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.decimal_sign = ','
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            leu.international = True

    def test_leu_math_add(self):
        """test_leu_math_add."""
        leu_one = Leu(amount=1)
        leu_two = Leu(amount=2)
        leu_three = Leu(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
        with raises(
                CurrencyMismatchException,
                match='unsupported operation between currency RON and OTHER.'):
            _ = leu_one + currency
        with raises(
                CurrencyTypeException,
                match=(
                    'unsupported operation between <class \'multicurrency.'
                    'leu.Leu\'> '
                    'and <class \'str\'>.')):
            _ = leu_one.__add__('1.00')
        assert (
            leu_one +
            leu_two) == leu_three

    def test_leu_slots(self):
        """test_leu_slots."""
        leu = Leu(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'Leu\' '
                    'object has no attribute \'new_variable\'')):
            leu.new_variable = 'fail'  # pylint: disable=assigning-non-slot
