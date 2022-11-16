# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Taka currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Taka(Currency):
    """Taka (Bangladesh) currency representation.

    Simple usage example:

        >>> from multicurrency import Taka
        >>> taka = Taka(
        ...     amount='123456.789')
        >>> print(taka)
        ১২৩,৪৫৬.৭৯৳

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a%s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%a%s'
    ) -> 'Taka':
        """Class creator.

        Returns:
            Taka: new `Taka` object.
        """
        return cast(
            Taka,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BDT',
                numeric_code='050',
                symbol='৳',
                localized_symbol='৳',
                convertion='০১২৩৪৫৬৭৮৯-,.',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Taka':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
