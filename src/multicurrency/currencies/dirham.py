# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dirham currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class UAEDirham(Currency):
    """Dirham (UAE) currency representation.

    Simple usage example:

        >>> from multicurrency import UAEDirham
        >>> uae_dirham = UAEDirham(
        ...     amount='123456.789')
        >>> print(uae_dirham)
        د.إ. ١٢٣٬٤٥٦٫٧٩

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%s\u00A0%a'
    ) -> 'UAEDirham':
        """Class creator.

        Returns:
            UAEDirham: new `UAEDirham` object.
        """
        return cast(
            UAEDirham,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AED',
                numeric_code='784',
                symbol='د.إ.',
                localized_symbol='د.إ.',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'UAEDirham':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class MoroccanDirham(Currency):
    """Dirham (Morocco) currency representation.

    Simple usage example:

        >>> from multicurrency import MoroccanDirham
        >>> moroccan_dirham = MoroccanDirham(
        ...     amount='123456.789')
        >>> print(moroccan_dirham)
        ١٢٣٬٤٥٦٫٧٩ د.م.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%a\u00A0%s'
    ) -> 'MoroccanDirham':
        """Class creator.

        Returns:
            MoroccanDirham: new `MoroccanDirham` object.
        """
        return cast(
            MoroccanDirham,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MAD',
                numeric_code='504',
                symbol='د.م.',
                localized_symbol='د.م.',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'MoroccanDirham':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
