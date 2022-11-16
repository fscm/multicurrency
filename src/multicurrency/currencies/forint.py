# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Forint currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Forint(Currency):
    """Forint (Hungary) currency representation.

    Simple usage example:

        >>> from multicurrency import Forint
        >>> forint = Forint(
        ...     amount='123456.789')
        >>> print(forint)
        123 457 Ft

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0,\u202F3%a\u00A0%s'
    ) -> 'Forint':
        """Class creator.

        Returns:
            Forint: new `Forint` object.
        """
        return cast(
            Forint,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='HUF',
                numeric_code='348',
                symbol='Ft',
                localized_symbol='Ft',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Forint':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
