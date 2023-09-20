# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Leu currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class MoldovanLeu(Currency):
    """Leu (Moldova) currency representation.

    Simple usage example:

        >>> from multicurrency import MoldovanLeu
        >>> moldovan_leu = MoldovanLeu(
        ...     amount='123456.789')
        >>> print(moldovan_leu)
        123.456,79 L

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            MoldovanLeu: new `MoldovanLeu` object.
        """
        return cast(
            MoldovanLeu,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MDL',
                numeric_code='498',
                symbol='L',
                localized_symbol='L',
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
            MoldovanLeu: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Leu(Currency):
    """Leu (Romania) currency representation.

    Simple usage example:

        >>> from multicurrency import Leu
        >>> leu = Leu(
        ...     amount='123456.789')
        >>> print(leu)
        123.456,79 L

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            Leu: new `Leu` object.
        """
        return cast(
            Leu,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RON',
                numeric_code='946',
                symbol='L',
                localized_symbol='L',
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
            Leu: new opbject.
        """
        return self.__class__(amount, self._info[5])
