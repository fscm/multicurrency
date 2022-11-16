# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Vatu currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Vatu(Currency):
    """Vatu (Vanuatu) currency representation.

    Simple usage example:

        >>> from multicurrency import Vatu
        >>> vatu = Vatu(
        ...     amount='123456.789')
        >>> print(vatu)
        Vt 123,457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0.,3%s\u00A0%a'
    ) -> 'Vatu':
        """Class creator.

        Returns:
            Vatu: new `Vatu` object.
        """
        return cast(
            Vatu,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='VUV',
                numeric_code='548',
                symbol='Vt',
                localized_symbol='Vt',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Vatu':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
