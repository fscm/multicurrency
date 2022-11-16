# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ngultrum currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Ngultrum(Currency):
    """Ngultrum (Bhutan) currency representation.

    Simple usage example:

        >>> from multicurrency import Ngultrum
        >>> ngultrum = Ngultrum(
        ...     amount='123456.789')
        >>> print(ngultrum)
        Nu. ༡༢༣,༤༥༦.༧༩

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
    ) -> 'Ngultrum':
        """Class creator.

        Returns:
            Ngultrum: new `Ngultrum` object.
        """
        return cast(
            Ngultrum,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BTN',
                numeric_code='064',
                symbol='Nu.',
                localized_symbol='Nu.',
                convertion='༠༡༢༣༤༥༦༧༨༩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Ngultrum':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
