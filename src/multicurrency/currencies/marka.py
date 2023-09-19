# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Marka currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class KonvertibilnaMarka(Currency):
    """Marka (Bosnia and Herzegovina) currency representation.

    Simple usage example:

        >>> from multicurrency import KonvertibilnaMarka
        >>> konvertibilna_marka = KonvertibilnaMarka(
        ...     amount='123456.789')
        >>> print(konvertibilna_marka)
        123,456.79 КМ

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2.,3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            KonvertibilnaMarka: new `KonvertibilnaMarka` object.
        """
        return cast(
            KonvertibilnaMarka,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BAM',
                numeric_code='977',
                symbol='КМ',
                localized_symbol='КМ',
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
