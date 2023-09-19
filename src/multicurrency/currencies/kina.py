# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kina currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class Kina(Currency):
    """Kina (Papua New Guinea) currency representation.

    Simple usage example:

        >>> from multicurrency import Kina
        >>> kina = Kina(
        ...     amount='123456.789')
        >>> print(kina)
        K 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            Kina: new `Kina` object.
        """
        return cast(
            Kina,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='PGK',
                numeric_code='598',
                symbol='K',
                localized_symbol='K',
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
