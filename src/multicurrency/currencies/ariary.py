# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ariary currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class MalagasyAriary(Currency):
    """Ariary (Madagascar) currency representation.

    Simple usage example:

        >>> from multicurrency import MalagasyAriary
        >>> malagasy_ariary = MalagasyAriary(
        ...     amount='123456.789')
        >>> print(malagasy_ariary)
        123 457 Ar

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
    ) -> 'MalagasyAriary':
        """Class creator.

        Returns:
            MalagasyAriary: new `MalagasyAriary` object.
        """
        return cast(
            MalagasyAriary,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MGA',
                numeric_code='969',
                symbol='Ar',
                localized_symbol='Ar',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'MalagasyAriary':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
