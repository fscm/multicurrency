# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Metical currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Metical(Currency):
    """Metical (Mozambique) currency representation.

    Simple usage example:

        >>> from multicurrency import Metical
        >>> metical = Metical(
        ...     amount='123456.789')
        >>> print(metical)
        123.457 MTn

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0,.3%a\u00A0%s'
    ) -> 'Metical':
        """Class creator.

        Returns:
            Metical: new `Metical` object.
        """
        return cast(
            Metical,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MZN',
                numeric_code='943',
                symbol='MTn',
                localized_symbol='MTn',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Metical':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
