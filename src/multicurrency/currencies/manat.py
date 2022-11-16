# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Manat currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class AzerbaijanianManat(Currency):
    """Manat (Azerbaijan) currency representation.

    Simple usage example:

        >>> from multicurrency import AzerbaijanianManat
        >>> azerbaijanian_manat = AzerbaijanianManat(
        ...     amount='123456.789')
        >>> print(azerbaijanian_manat)
        123.456,79 ₼

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
    ) -> 'AzerbaijanianManat':
        """Class creator.

        Returns:
            AzerbaijanianManat: new `AzerbaijanianManat` object.
        """
        return cast(
            AzerbaijanianManat,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AZN',
                numeric_code='944',
                symbol='₼',
                localized_symbol='₼',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AzerbaijanianManat':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Manat(Currency):
    """Manat (Turkmenistan) currency representation.

    Simple usage example:

        >>> from multicurrency import Manat
        >>> manat = Manat(
        ...     amount='123456.789')
        >>> print(manat)
        123 456,79 m

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
    ) -> 'Manat':
        """Class creator.

        Returns:
            Manat: new `Manat` object.
        """
        return cast(
            Manat,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TMT',
                numeric_code='934',
                symbol='m',
                localized_symbol='m',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Manat':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
