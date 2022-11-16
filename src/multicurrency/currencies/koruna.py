# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Koruna currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class CzechKoruna(Currency):
    """Koruna (Czech Republic) currency representation.

    Simple usage example:

        >>> from multicurrency import CzechKoruna
        >>> czech_koruna = CzechKoruna(
        ...     amount='123456.789')
        >>> print(czech_koruna)
        123 456,79 Kč

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'CzechKoruna':
        """Class creator.

        Returns:
            CzechKoruna: new `CzechKoruna` object.
        """
        return cast(
            CzechKoruna,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CZK',
                numeric_code='203',
                symbol='Kč',
                localized_symbol='Kč',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CzechKoruna':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
