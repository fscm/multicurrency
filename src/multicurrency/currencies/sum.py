# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Sum currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class UzbekistanSum(Currency):
    """Sum (Uzbekistan) currency representation.

    Simple usage example:

        >>> from multicurrency import UzbekistanSum
        >>> uzbekistan_sum = UzbekistanSum(
        ...     amount='123456.789')
        >>> print(uzbekistan_sum)
        123 456,79 сўм

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'UzbekistanSum':
        """Class creator.

        Returns:
            UzbekistanSum: new `UzbekistanSum` object.
        """
        return cast(
            UzbekistanSum,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='UZS',
                numeric_code='860',
                symbol='сўм',
                localized_symbol='сўм',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'UzbekistanSum':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
