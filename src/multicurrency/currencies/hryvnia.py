# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Hryvnia currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Hryvnia(Currency):
    """Hryvnia (Ukraine) currency representation.

    Simple usage example:

        >>> from multicurrency import Hryvnia
        >>> hryvnia = Hryvnia(
        ...     amount='123456.789')
        >>> print(hryvnia)
        123 456,79 ₴

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
    ) -> 'Hryvnia':
        """Class creator.

        Returns:
            Hryvnia: new `Hryvnia` object.
        """
        return cast(
            Hryvnia,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='UAH',
                numeric_code='980',
                symbol='₴',
                localized_symbol='₴',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Hryvnia':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
