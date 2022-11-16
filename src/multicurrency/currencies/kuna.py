# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Kuna currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class CroatianKuna(Currency):
    """Kuna (Croatia) currency representation.

    Simple usage example:

        >>> from multicurrency import CroatianKuna
        >>> croatian_kuna = CroatianKuna(
        ...     amount='123456.789')
        >>> print(croatian_kuna)
        123.456,79 Kn

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'CroatianKuna':
        """Class creator.

        Returns:
            CroatianKuna: new `CroatianKuna` object.
        """
        return cast(
            CroatianKuna,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='HRK',
                numeric_code='191',
                symbol='Kn',
                localized_symbol='Kn',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CroatianKuna':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
