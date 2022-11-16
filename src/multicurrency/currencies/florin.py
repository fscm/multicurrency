# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Florin currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class ArubanFlorin(Currency):
    """Florin (Aruba) currency representation.

    Simple usage example:

        >>> from multicurrency import ArubanFlorin
        >>> aruban_florin = ArubanFlorin(
        ...     amount='123456.789')
        >>> print(aruban_florin)
        ƒ123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'ArubanFlorin':
        """Class creator.

        Returns:
            ArubanFlorin: new `ArubanFlorin` object.
        """
        return cast(
            ArubanFlorin,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AWG',
                numeric_code='533',
                symbol='ƒ',
                localized_symbol='ƒ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ArubanFlorin':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
