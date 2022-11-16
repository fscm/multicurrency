# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Riyal currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class SaudiRiyal(Currency):
    """Riyal (Saudi Arabia) currency representation.

    Simple usage example:

        >>> from multicurrency import SaudiRiyal
        >>> saudi_riyal = SaudiRiyal(
        ...     amount='123456.789')
        >>> print(saudi_riyal)
        ر.س. ١٢٣٬٤٥٦٫٧٩

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%s\u00A0%a'
    ) -> 'SaudiRiyal':
        """Class creator.

        Returns:
            SaudiRiyal: new `SaudiRiyal` object.
        """
        return cast(
            SaudiRiyal,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SAR',
                numeric_code='682',
                symbol='ر.س.',
                localized_symbol='ر.س.',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SaudiRiyal':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
