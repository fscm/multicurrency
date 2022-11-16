# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Boliviano currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Boliviano(Currency):
    """Boliviano (Bolivia) currency representation.

    Simple usage example:

        >>> from multicurrency import Boliviano
        >>> boliviano = Boliviano(
        ...     amount='123456.789')
        >>> print(boliviano)
        Bs. 123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%s\u00A0%a'
    ) -> 'Boliviano':
        """Class creator.

        Returns:
            Boliviano: new `Boliviano` object.
        """
        return cast(
            Boliviano,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BOB',
                numeric_code='068',
                symbol='Bs.',
                localized_symbol='Bs.',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Boliviano':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
