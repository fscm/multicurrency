# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Pula currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class Pula(Currency):
    """Pula (Botswana) currency representation.

    Simple usage example:

        >>> from multicurrency import Pula
        >>> pula = Pula(
        ...     amount='123456.789')
        >>> print(pula)
        P 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            Pula: new `Pula` object.
        """
        return cast(
            Pula,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BWP',
                numeric_code='072',
                symbol='P',
                localized_symbol='P',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: Union[str, float, Decimal],
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
