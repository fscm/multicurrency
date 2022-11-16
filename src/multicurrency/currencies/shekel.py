# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Shekel currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class NewIsraeliShekel(Currency):
    """Shekel (Israel) currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekel
        >>> new_israeli_shekel = NewIsraeliShekel(
        ...     amount='123456.789')
        >>> print(new_israeli_shekel)
        123,456.79 ₪

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%a\u00A0%s'
    ) -> 'NewIsraeliShekel':
        """Class creator.

        Returns:
            NewIsraeliShekel: new `NewIsraeliShekel` object.
        """
        return cast(
            NewIsraeliShekel,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ILS',
                numeric_code='376',
                symbol='₪',
                localized_symbol='₪',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewIsraeliShekel':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewIsraeliShekelIL(Currency):
    """Shekel (Israel) currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekelIL
        >>> new_israeli_shekel_il = NewIsraeliShekelIL(
        ...     amount='123456.789')
        >>> print(new_israeli_shekel_il)
        123,456.79 ₪

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%a\u00A0%s'
    ) -> 'NewIsraeliShekelIL':
        """Class creator.

        Returns:
            NewIsraeliShekelIL: new `NewIsraeliShekelIL` object.
        """
        return cast(
            NewIsraeliShekelIL,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ILS',
                numeric_code='376',
                symbol='₪',
                localized_symbol='IL₪',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewIsraeliShekelIL':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewIsraeliShekelPS(Currency):
    """Shekel (Palestine) currency representation.

    Simple usage example:

        >>> from multicurrency import NewIsraeliShekelPS
        >>> new_israeli_shekel_ps = NewIsraeliShekelPS(
        ...     amount='123456.789')
        >>> print(new_israeli_shekel_ps)
        123,456.79 ₪

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%a\u00A0%s'
    ) -> 'NewIsraeliShekelPS':
        """Class creator.

        Returns:
            NewIsraeliShekelPS: new `NewIsraeliShekelPS` object.
        """
        return cast(
            NewIsraeliShekelPS,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ILS',
                numeric_code='376',
                symbol='₪',
                localized_symbol='PS₪',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewIsraeliShekelPS':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
