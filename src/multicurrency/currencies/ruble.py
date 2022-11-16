# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ruble currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class BelarusianRuble(Currency):
    """Ruble (Belarus) currency representation.

    Simple usage example:

        >>> from multicurrency import BelarusianRuble
        >>> belarusian_ruble = BelarusianRuble(
        ...     amount='123456.789')
        >>> print(belarusian_ruble)
        123 456,79 Br

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'BelarusianRuble':
        """Class creator.

        Returns:
            BelarusianRuble: new `BelarusianRuble` object.
        """
        return cast(
            BelarusianRuble,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BYN',
                numeric_code='933',
                symbol='Br',
                localized_symbol='Br',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BelarusianRuble':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RussianRuble(Currency):
    """Ruble (Russia) currency representation.

    Simple usage example:

        >>> from multicurrency import RussianRuble
        >>> russian_ruble = RussianRuble(
        ...     amount='123456.789')
        >>> print(russian_ruble)
        123 456,79 ₽

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'RussianRuble':
        """Class creator.

        Returns:
            RussianRuble: new `RussianRuble` object.
        """
        return cast(
            RussianRuble,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RUB',
                numeric_code='643',
                symbol='₽',
                localized_symbol='₽',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'RussianRuble':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RussianRubleRU(Currency):
    """Ruble (Russia) currency representation.

    Simple usage example:

        >>> from multicurrency import RussianRubleRU
        >>> russian_ruble_ru = RussianRubleRU(
        ...     amount='123456.789')
        >>> print(russian_ruble_ru)
        123 456,79 ₽

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'RussianRubleRU':
        """Class creator.

        Returns:
            RussianRubleRU: new `RussianRubleRU` object.
        """
        return cast(
            RussianRubleRU,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RUB',
                numeric_code='643',
                symbol='₽',
                localized_symbol='RU₽',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'RussianRubleRU':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RussianRubleGE(Currency):
    """Ruble (South Ossetia) currency representation.

    Simple usage example:

        >>> from multicurrency import RussianRubleGE
        >>> russian_ruble_ge = RussianRubleGE(
        ...     amount='123456.789')
        >>> print(russian_ruble_ge)
        123 456,79 ₽

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'RussianRubleGE':
        """Class creator.

        Returns:
            RussianRubleGE: new `RussianRubleGE` object.
        """
        return cast(
            RussianRubleGE,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RUB',
                numeric_code='643',
                symbol='₽',
                localized_symbol='GE₽',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'RussianRubleGE':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
