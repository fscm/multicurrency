# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ouguiya currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class Ouguiya(Currency):
    """Ouguiya (Mauritania) currency representation.

    Simple usage example:

        >>> from multicurrency import Ouguiya
        >>> ouguiya = Ouguiya(
        ...     amount='123456.789')
        >>> print(ouguiya)
        ١٢٣٬٤٥٦٫٧٩ أ.م

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2\u066B\u066C3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            Ouguiya: new `Ouguiya` object.
        """
        return cast(
            Ouguiya,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MRU',
                numeric_code='929',
                symbol='أ.م',
                localized_symbol='أ.م',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            Ouguiya: new opbject.
        """
        return self.__class__(amount, self._info[5])
