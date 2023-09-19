# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lev currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class BulgarianLev(Currency):
    """Lev (Bulgaria) currency representation.

    Simple usage example:

        >>> from multicurrency import BulgarianLev
        >>> bulgarian_lev = BulgarianLev(
        ...     amount='123456.789')
        >>> print(bulgarian_lev)
        123 456,79 лв.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2,\u00A03%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            BulgarianLev: new `BulgarianLev` object.
        """
        return cast(
            BulgarianLev,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BGN',
                numeric_code='975',
                symbol='лв.',
                localized_symbol='лв.',
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
