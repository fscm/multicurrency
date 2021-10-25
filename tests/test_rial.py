# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tests for the Rial currency representation(s)."""

from decimal import Context
from pytest import raises
from multicurrency import Currency
from multicurrency import (
    CurrencyMismatchException,
    CurrencyTypeException)


CONTEXT = Context(prec=28, rounding='ROUND_HALF_EVEN').copy()


"""Tests for the Iranian Rial representation."""

from multicurrency import IranianRial


class TestIranianRial:

    def test_iranian_rial(self):
        """test_iranian_rial."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        iranian_rial = IranianRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iranian_rial.amount == decimal
        assert iranian_rial.numeric_code == '364'
        assert iranian_rial.alpha_code == 'IRR'
        assert iranian_rial.decimal_places == 2
        assert iranian_rial.decimal_sign == '\u066B'
        assert iranian_rial.grouping_places == 3
        assert iranian_rial.grouping_sign == '\u066C'
        assert not iranian_rial.international
        assert iranian_rial.symbol == '﷼'
        assert not iranian_rial.symbol_ahead
        assert iranian_rial.symbol_separator == '\u00A0'
        assert iranian_rial.localized_symbol == '﷼'
        assert iranian_rial.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
        assert iranian_rial.__repr__() == (
            'IranianRial(amount: 0.1428571428571428571428571429, '
            'alpha_code: "IRR", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "﷼", '
            'numeric_code: "364", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            'international: False)')
        assert iranian_rial.__str__() == '۰٫۱۴ ﷼'


    def test_iranian_rial_negative(self):
        """test_iranian_rial_negative."""
        amount = -100
        iranian_rial = IranianRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert iranian_rial.numeric_code == '364'
        assert iranian_rial.alpha_code == 'IRR'
        assert iranian_rial.decimal_places == 2
        assert iranian_rial.decimal_sign == '\u066B'
        assert iranian_rial.grouping_places == 3
        assert iranian_rial.grouping_sign == '\u066C'
        assert not iranian_rial.international
        assert iranian_rial.symbol == '﷼'
        assert not iranian_rial.symbol_ahead
        assert iranian_rial.symbol_separator == '\u00A0'
        assert iranian_rial.localized_symbol == '﷼'
        assert iranian_rial.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
        assert iranian_rial.__repr__() == (
            'IranianRial(amount: -100, '
            'alpha_code: "IRR", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "﷼", '
            'numeric_code: "364", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            'international: False)')
        assert iranian_rial.__str__() == '-۱۰۰٫۰۰ ﷼'


    def test_iranian_rial_custom(self):
        """test_iranian_rial_custom."""
        amount = 1000
        iranian_rial = IranianRial(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert iranian_rial.amount == decimal
        assert iranian_rial.numeric_code == '364'
        assert iranian_rial.alpha_code == 'IRR'
        assert iranian_rial.decimal_places == 5
        assert iranian_rial.decimal_sign == '\u066C'
        assert iranian_rial.grouping_places == 2
        assert iranian_rial.grouping_sign == '\u066B'
        assert iranian_rial.international
        assert iranian_rial.symbol == '﷼'
        assert not iranian_rial.symbol_ahead
        assert iranian_rial.symbol_separator == '_'
        assert iranian_rial.localized_symbol == '﷼'
        assert iranian_rial.convertion == '۰۱۲۳۴۵۶۷۸۹-'
        assert iranian_rial.__hash__() == hash((decimal, 'IRR', '364'))
        assert iranian_rial.__repr__() == (
            'IranianRial(amount: 1000, '
            'alpha_code: "IRR", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "﷼", '
            'numeric_code: "364", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "۰۱۲۳۴۵۶۷۸۹-", '
            'international: True)')
        assert iranian_rial.__str__() == 'IRR 10,00.00000'


    def test_iranian_rial_changed(self):
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
            iranian_rial.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.localized_symbol = '€'
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
            iranian_rial.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            iranian_rial.international = True


    def test_iranian_rial_math_add(self):
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
        assert (
            iranian_rial_one +
            iranian_rial_two) == iranian_rial_three


    def test_iranian_rial_slots(self):
        """test_iranian_rial_slots."""
        iranian_rial = IranianRial(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'IranianRial\' '
                    'object has no attribute \'new_variable\'')):
            iranian_rial.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Rial Omani representation."""

from multicurrency import RialOmani


class TestRialOmani:

    def test_rial_omani(self):
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
        assert rial_omani.localized_symbol == 'ر.ع.'
        assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
        assert rial_omani.__repr__() == (
            'RialOmani(amount: 0.1428571428571428571428571429, '
            'alpha_code: "OMR", '
            'symbol: "ر.ع.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.ع.", '
            'numeric_code: "512", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert rial_omani.__str__() == 'ر.ع. ٠٫١٤٣'


    def test_rial_omani_negative(self):
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
        assert rial_omani.localized_symbol == 'ر.ع.'
        assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
        assert rial_omani.__repr__() == (
            'RialOmani(amount: -100, '
            'alpha_code: "OMR", '
            'symbol: "ر.ع.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.ع.", '
            'numeric_code: "512", '
            'decimal_places: "3", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert rial_omani.__str__() == 'ر.ع. -١٠٠٫٠٠٠'


    def test_rial_omani_custom(self):
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
        assert rial_omani.localized_symbol == 'ر.ع.'
        assert rial_omani.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert rial_omani.__hash__() == hash((decimal, 'OMR', '512'))
        assert rial_omani.__repr__() == (
            'RialOmani(amount: 1000, '
            'alpha_code: "OMR", '
            'symbol: "ر.ع.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ر.ع.", '
            'numeric_code: "512", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert rial_omani.__str__() == 'OMR 10,00.00000'


    def test_rial_omani_changed(self):
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
            rial_omani.localized_symbol = '€'
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


    def test_rial_omani_math_add(self):
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


    def test_rial_omani_slots(self):
        """test_rial_omani_slots."""
        rial_omani = RialOmani(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'RialOmani\' '
                    'object has no attribute \'new_variable\'')):
            rial_omani.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Qatari Rial representation."""

from multicurrency import QatariRial


class TestQatariRial:

    def test_qatari_rial(self):
        """test_qatari_rial."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        qatari_rial = QatariRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert qatari_rial.amount == decimal
        assert qatari_rial.numeric_code == '634'
        assert qatari_rial.alpha_code == 'QAR'
        assert qatari_rial.decimal_places == 2
        assert qatari_rial.decimal_sign == '\u066B'
        assert qatari_rial.grouping_places == 3
        assert qatari_rial.grouping_sign == '\u066C'
        assert not qatari_rial.international
        assert qatari_rial.symbol == 'ر.ق.'
        assert qatari_rial.symbol_ahead
        assert qatari_rial.symbol_separator == '\u00A0'
        assert qatari_rial.localized_symbol == 'ر.ق.'
        assert qatari_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
        assert qatari_rial.__repr__() == (
            'QatariRial(amount: 0.1428571428571428571428571429, '
            'alpha_code: "QAR", '
            'symbol: "ر.ق.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.ق.", '
            'numeric_code: "634", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert qatari_rial.__str__() == 'ر.ق. ٠٫١٤'


    def test_qatari_rial_negative(self):
        """test_qatari_rial_negative."""
        amount = -100
        qatari_rial = QatariRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert qatari_rial.numeric_code == '634'
        assert qatari_rial.alpha_code == 'QAR'
        assert qatari_rial.decimal_places == 2
        assert qatari_rial.decimal_sign == '\u066B'
        assert qatari_rial.grouping_places == 3
        assert qatari_rial.grouping_sign == '\u066C'
        assert not qatari_rial.international
        assert qatari_rial.symbol == 'ر.ق.'
        assert qatari_rial.symbol_ahead
        assert qatari_rial.symbol_separator == '\u00A0'
        assert qatari_rial.localized_symbol == 'ر.ق.'
        assert qatari_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
        assert qatari_rial.__repr__() == (
            'QatariRial(amount: -100, '
            'alpha_code: "QAR", '
            'symbol: "ر.ق.", '
            'symbol_ahead: True, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "ر.ق.", '
            'numeric_code: "634", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert qatari_rial.__str__() == 'ر.ق. -١٠٠٫٠٠'


    def test_qatari_rial_custom(self):
        """test_qatari_rial_custom."""
        amount = 1000
        qatari_rial = QatariRial(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
            grouping_sign='\u066B',
            international=True,
            symbol_ahead=False,
            symbol_separator='_')
        decimal = CONTEXT.create_decimal(amount)
        assert qatari_rial.amount == decimal
        assert qatari_rial.numeric_code == '634'
        assert qatari_rial.alpha_code == 'QAR'
        assert qatari_rial.decimal_places == 5
        assert qatari_rial.decimal_sign == '\u066C'
        assert qatari_rial.grouping_places == 2
        assert qatari_rial.grouping_sign == '\u066B'
        assert qatari_rial.international
        assert qatari_rial.symbol == 'ر.ق.'
        assert not qatari_rial.symbol_ahead
        assert qatari_rial.symbol_separator == '_'
        assert qatari_rial.localized_symbol == 'ر.ق.'
        assert qatari_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert qatari_rial.__hash__() == hash((decimal, 'QAR', '634'))
        assert qatari_rial.__repr__() == (
            'QatariRial(amount: 1000, '
            'alpha_code: "QAR", '
            'symbol: "ر.ق.", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "ر.ق.", '
            'numeric_code: "634", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert qatari_rial.__str__() == 'QAR 10,00.00000'


    def test_qatari_rial_changed(self):
        """test_cqatari_rial_changed."""
        qatari_rial = QatariRial(amount=1000)
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.amount = 999
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.alpha_code = 'EUR'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.convertion = '0123456789,.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.symbol_ahead = False
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.symbol_separator = '_'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.localized_symbol = '€'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.numeric_code = '978'
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
            qatari_rial.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            qatari_rial.international = True


    def test_qatari_rial_math_add(self):
        """test_qatari_rial_math_add."""
        qatari_rial_one = QatariRial(amount=1)
        qatari_rial_two = QatariRial(amount=2)
        qatari_rial_three = QatariRial(amount=3)
        currency = Currency(amount=1, alpha_code='OTHER')
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
        assert (
            qatari_rial_one +
            qatari_rial_two) == qatari_rial_three


    def test_qatari_rial_slots(self):
        """test_qatari_rial_slots."""
        qatari_rial = QatariRial(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'QatariRial\' '
                    'object has no attribute \'new_variable\'')):
            qatari_rial.new_variable = 'fail'  # pylint: disable=assigning-non-slot


"""Tests for the Yemeni Rial representation."""

from multicurrency import YemeniRial


class TestYemeniRial:

    def test_yemeni_rial(self):
        """test_yemeni_rial."""
        amount = CONTEXT.create_decimal(1) / CONTEXT.create_decimal(7)
        yemeni_rial = YemeniRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yemeni_rial.amount == decimal
        assert yemeni_rial.numeric_code == '886'
        assert yemeni_rial.alpha_code == 'YER'
        assert yemeni_rial.decimal_places == 2
        assert yemeni_rial.decimal_sign == '\u066B'
        assert yemeni_rial.grouping_places == 3
        assert yemeni_rial.grouping_sign == '\u066C'
        assert not yemeni_rial.international
        assert yemeni_rial.symbol == '﷼'
        assert not yemeni_rial.symbol_ahead
        assert yemeni_rial.symbol_separator == '\u00A0'
        assert yemeni_rial.localized_symbol == '﷼'
        assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
        assert yemeni_rial.__repr__() == (
            'YemeniRial(amount: 0.1428571428571428571428571429, '
            'alpha_code: "YER", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "﷼", '
            'numeric_code: "886", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert yemeni_rial.__str__() == '٠٫١٤ ﷼'


    def test_yemeni_rial_negative(self):
        """test_yemeni_rial_negative."""
        amount = -100
        yemeni_rial = YemeniRial(amount=amount)
        decimal = CONTEXT.create_decimal(amount)
        assert yemeni_rial.numeric_code == '886'
        assert yemeni_rial.alpha_code == 'YER'
        assert yemeni_rial.decimal_places == 2
        assert yemeni_rial.decimal_sign == '\u066B'
        assert yemeni_rial.grouping_places == 3
        assert yemeni_rial.grouping_sign == '\u066C'
        assert not yemeni_rial.international
        assert yemeni_rial.symbol == '﷼'
        assert not yemeni_rial.symbol_ahead
        assert yemeni_rial.symbol_separator == '\u00A0'
        assert yemeni_rial.localized_symbol == '﷼'
        assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
        assert yemeni_rial.__repr__() == (
            'YemeniRial(amount: -100, '
            'alpha_code: "YER", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "\u00A0", '
            'localized_symbol: "﷼", '
            'numeric_code: "886", '
            'decimal_places: "2", '
            'decimal_sign: "\u066B", '
            'grouping_places: "3", '
            'grouping_sign: "\u066C", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: False)')
        assert yemeni_rial.__str__() == '-١٠٠٫٠٠ ﷼'


    def test_yemeni_rial_custom(self):
        """test_yemeni_rial_custom."""
        amount = 1000
        yemeni_rial = YemeniRial(
            amount=amount,
            decimal_places=5,
            decimal_sign='\u066C',
            grouping_places=2,
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
        assert yemeni_rial.grouping_places == 2
        assert yemeni_rial.grouping_sign == '\u066B'
        assert yemeni_rial.international
        assert yemeni_rial.symbol == '﷼'
        assert not yemeni_rial.symbol_ahead
        assert yemeni_rial.symbol_separator == '_'
        assert yemeni_rial.localized_symbol == '﷼'
        assert yemeni_rial.convertion == '٠١٢٣٤٥٦٧٨٩-'
        assert yemeni_rial.__hash__() == hash((decimal, 'YER', '886'))
        assert yemeni_rial.__repr__() == (
            'YemeniRial(amount: 1000, '
            'alpha_code: "YER", '
            'symbol: "﷼", '
            'symbol_ahead: False, '
            'symbol_separator: "_", '
            'localized_symbol: "﷼", '
            'numeric_code: "886", '
            'decimal_places: "5", '
            'decimal_sign: "\u066C", '
            'grouping_places: "2", '
            'grouping_sign: "\u066B", '
            'convertion: "٠١٢٣٤٥٦٧٨٩-", '
            'international: True)')
        assert yemeni_rial.__str__() == 'YER 10,00.00000'


    def test_yemeni_rial_changed(self):
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
            yemeni_rial.localized_symbol = '€'
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
            yemeni_rial.grouping_places = 4
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yemeni_rial.grouping_sign = '.'
        with raises(
                AttributeError,
                match='can\'t set attribute'):
            yemeni_rial.international = True


    def test_yemeni_rial_math_add(self):
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


    def test_yemeni_rial_slots(self):
        """test_yemeni_rial_slots."""
        yemeni_rial = YemeniRial(amount=1000)
        with raises(
                AttributeError,
                match=(
                    '\'YemeniRial\' '
                    'object has no attribute \'new_variable\'')):
            yemeni_rial.new_variable = 'fail'  # pylint: disable=assigning-non-slot
