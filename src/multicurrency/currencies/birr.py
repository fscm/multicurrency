# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Birr currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class EthiopianBirr(Currency):
    """Birr (Ethiopia) currency representation.

    Simple usage example:

        >>> from multicurrency import EthiopianBirr
        >>> ethiopian_birr = EthiopianBirr(
        ...     amount='123456.789')
        >>> print(ethiopian_birr)
        ብር 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'EthiopianBirr':
        """Class creator.

        Returns:
            EthiopianBirr: new `EthiopianBirr` object.
        """
        return cast(
            EthiopianBirr,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ETB',
                numeric_code='230',
                symbol='ብር',
                localized_symbol='ብር',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EthiopianBirr':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
