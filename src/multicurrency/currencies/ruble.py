# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ruble currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            BelarusianRuble: new opbject.
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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            RussianRuble: new opbject.
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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            RussianRubleRU: new opbject.
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
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
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
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            RussianRubleGE: new opbject.
        """
        return self.__class__(amount, self._info[5])
