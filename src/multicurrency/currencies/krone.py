# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Krone currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class DanishKrone(Currency):
    """Krone (Denmark) currency representation.

    Simple usage example:

        >>> from multicurrency import DanishKrone
        >>> danish_krone = DanishKrone(
        ...     amount='123456.789')
        >>> print(danish_krone)
        123.456,79 kr

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
    ) -> 'DanishKrone':
        """Class creator.

        Returns:
            DanishKrone: new `DanishKrone` object.
        """
        return cast(
            DanishKrone,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='DKK',
                numeric_code='208',
                symbol='kr',
                localized_symbol='kr',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'DanishKrone':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NorwegianKrone(Currency):
    """Krone (Norway) currency representation.

    Simple usage example:

        >>> from multicurrency import NorwegianKrone
        >>> norwegian_krone = NorwegianKrone(
        ...     amount='123456.789')
        >>> print(norwegian_krone)
        kr 123 456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%s\u00A0%a'
    ) -> 'NorwegianKrone':
        """Class creator.

        Returns:
            NorwegianKrone: new `NorwegianKrone` object.
        """
        return cast(
            NorwegianKrone,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NOK',
                numeric_code='578',
                symbol='kr',
                localized_symbol='kr',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NorwegianKrone':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
