# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Escudo currency representation(s)."""

from decimal import Decimal
from typing import Optional, Self, Union, cast

from multicurrency.pycurrency import Currency


class CapeVerdeEscudo(Currency):
    """Escudo (Cape Verde) currency representation.

    Simple usage example:

        >>> from multicurrency import CapeVerdeEscudo
        >>> cape_verde_escudo = CapeVerdeEscudo(
        ...     amount='123456.789')
        >>> print(cape_verde_escudo)
        123 456$79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2$ 3%a%s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: Union[str, float, Decimal],
        pattern: Optional[str] = '2$\u202F3%a%s',
    ) -> Self:
        """Class creator.

        Returns:
            CapeVerdeEscudo: new `CapeVerdeEscudo` object.
        """
        return cast(
            CapeVerdeEscudo,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CVE',
                numeric_code='132',
                symbol='',
                localized_symbol='',
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
