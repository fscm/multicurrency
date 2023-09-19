# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Oro currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class CordobaOro(Currency):
    """Oro (Nicaragua) currency representation.

    Simple usage example:

        >>> from multicurrency import CordobaOro
        >>> cordoba_oro = CordobaOro(
        ...     amount='123456.789')
        >>> print(cordoba_oro)
        C$123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            CordobaOro: new `CordobaOro` object.
        """
        return cast(
            CordobaOro,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NIO',
                numeric_code='558',
                symbol='C$',
                localized_symbol='C$',
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
