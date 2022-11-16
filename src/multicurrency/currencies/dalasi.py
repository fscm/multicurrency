# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dalasi currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Dalasi(Currency):
    """Dalasi (Gambia) currency representation.

    Simple usage example:

        >>> from multicurrency import Dalasi
        >>> dalasi = Dalasi(
        ...     amount='123456.789')
        >>> print(dalasi)
        D 123,456.79

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
    ) -> 'Dalasi':
        """Class creator.

        Returns:
            Dalasi: new `Dalasi` object.
        """
        return cast(
            Dalasi,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GMD',
                numeric_code='270',
                symbol='D',
                localized_symbol='D',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Dalasi':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
