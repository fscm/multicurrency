# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Yuan currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Yuan(Currency):
    """Yuan (China) currency representation.

    Simple usage example:

        >>> from multicurrency import Yuan
        >>> yuan = Yuan(
        ...     amount='123456.789')
        >>> print(yuan)
        ¥123,456.79

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
    ) -> 'Yuan':
        """Class creator.

        Returns:
            Yuan: new `Yuan` object.
        """
        return cast(
            Yuan,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CNY',
                numeric_code='156',
                symbol='¥',
                localized_symbol='¥',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Yuan':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
