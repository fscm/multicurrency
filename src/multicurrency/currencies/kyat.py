# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kyat currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class Kyat(Currency):
    """Kyat (Myanmar (Burma)) currency representation.

    Simple usage example:

        >>> from multicurrency import Kyat
        >>> kyat = Kyat(
        ...     amount='123456.789')
        >>> print(kyat)
        ၁၂၃,၄၅၆.၇၉ K

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
            Kyat: new `Kyat` object.
        """
        return cast(
            Kyat,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MMK',
                numeric_code='104',
                symbol='K',
                localized_symbol='K',
                convertion='၀၁၂၃၄၅၆၇၈၉-',
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
