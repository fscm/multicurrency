# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kwanza currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Kwanza(Currency):
    """Kwanza (Angola) currency representation.

    Simple usage example:

        >>> from multicurrency import Kwanza
        >>> kwanza = Kwanza(
        ...     amount='123456.789')
        >>> print(kwanza)
        123 456,79 Kz

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
    ) -> 'Kwanza':
        """Class creator.

        Returns:
            Kwanza: new `Kwanza` object.
        """
        return cast(
            Kwanza,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AOA',
                numeric_code='973',
                symbol='Kz',
                localized_symbol='Kz',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Kwanza':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
