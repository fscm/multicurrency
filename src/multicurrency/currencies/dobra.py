# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dobra currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Dobra(Currency):
    """Dobra (Sao Tome and Principe) currency representation.

    Simple usage example:

        >>> from multicurrency import Dobra
        >>> dobra = Dobra(
        ...     amount='123456.789')
        >>> print(dobra)
        123.456,79 Db

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
    ) -> 'Dobra':
        """Class creator.

        Returns:
            Dobra: new `Dobra` object.
        """
        return cast(
            Dobra,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='STN',
                numeric_code='930',
                symbol='Db',
                localized_symbol='Db',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Dobra':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
