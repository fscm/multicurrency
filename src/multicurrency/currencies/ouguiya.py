# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Ouguiya currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


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
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%a\u00A0%s'
    ) -> 'Ouguiya':
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
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Ouguiya':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
