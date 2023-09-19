# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tenge currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class Tenge(Currency):
    """Tenge (Kazakhstan) currency representation.

    Simple usage example:

        >>> from multicurrency import Tenge
        >>> tenge = Tenge(
        ...     amount='123456.789')
        >>> print(tenge)
        123 456,79 〒

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            Tenge: new `Tenge` object.
        """
        return cast(
            Tenge,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KZT',
                numeric_code='398',
                symbol='〒',
                localized_symbol='〒',
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
