# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dram currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class ArmenianDram(Currency):
    """Dram (Armenia) currency representation.

    Simple usage example:

        >>> from multicurrency import ArmenianDram
        >>> armenian_dram = ArmenianDram(
        ...     amount=123456.789)
        >>> print(armenian_dram)
        123 456,79 Դ

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = []

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'ArmenianDram':
        """Class creator.

        Returns:
            ArmenianDram: new `ArmenianDram` object.
        """
        return cast(
            ArmenianDram,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AMD',
                numeric_code='051',
                symbol='Դ',
                localized_symbol='Դ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ArmenianDram':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])