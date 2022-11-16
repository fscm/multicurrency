# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Lek currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Lek(Currency):
    """Lek (Albania) currency representation.

    Simple usage example:

        >>> from multicurrency import Lek
        >>> lek = Lek(
        ...     amount='123456.789')
        >>> print(lek)
        123 456,79 Lek

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
    ) -> 'Lek':
        """Class creator.

        Returns:
            Lek: new `Lek` object.
        """
        return cast(
            Lek,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ALL',
                numeric_code='008',
                symbol='Lek',
                localized_symbol='Lek',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Lek':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
