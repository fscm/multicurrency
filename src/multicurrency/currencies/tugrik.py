# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Tugrik currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Tugrik(Currency):
    """Tugrik (Mongolia) currency representation.

    Simple usage example:

        >>> from multicurrency import Tugrik
        >>> tugrik = Tugrik(
        ...     amount='123456.789')
        >>> print(tugrik)
        ₮ 123,456.79

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
    ) -> 'Tugrik':
        """Class creator.

        Returns:
            Tugrik: new `Tugrik` object.
        """
        return cast(
            Tugrik,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MNT',
                numeric_code='496',
                symbol='₮',
                localized_symbol='₮',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Tugrik':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
