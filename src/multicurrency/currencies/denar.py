# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Denar currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Denar(Currency):
    """Denar (Macedonia) currency representation.

    Simple usage example:

        >>> from multicurrency import Denar
        >>> denar = Denar(
        ...     amount='123456.789')
        >>> print(denar)
        123.456,79 ден.

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
    ) -> 'Denar':
        """Class creator.

        Returns:
            Denar: new `Denar` object.
        """
        return cast(
            Denar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MKD',
                numeric_code='807',
                symbol='ден.',
                localized_symbol='ден.',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Denar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
