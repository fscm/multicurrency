# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Guarani currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Guarani(Currency):
    """Guarani (Paraguay) currency representation.

    Simple usage example:

        >>> from multicurrency import Guarani
        >>> guarani = Guarani(
        ...     amount='123456.789')
        >>> print(guarani)
        ₲ 123.457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0,.3%s\u00A0%a'
    ) -> 'Guarani':
        """Class creator.

        Returns:
            Guarani: new `Guarani` object.
        """
        return cast(
            Guarani,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='PYG',
                numeric_code='600',
                symbol='₲',
                localized_symbol='₲',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Guarani':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
