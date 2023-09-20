# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rial currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class IranianRial(Currency):
    """Rial (Iran) currency representation.

    Simple usage example:

        >>> from multicurrency import IranianRial
        >>> iranian_rial = IranianRial(
        ...     amount='123456.789')
        >>> print(iranian_rial)
        ۱۲۳٬۴۵۶٫۷۹ ﷼

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
            IranianRial: new `IranianRial` object.
        """
        return cast(
            IranianRial,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='IRR',
                numeric_code='364',
                symbol='﷼',
                localized_symbol='﷼',
                convertion='۰۱۲۳۴۵۶۷۸۹-',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            IranianRial: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RialOmani(Currency):
    """Rial (Oman) currency representation.

    Simple usage example:

        >>> from multicurrency import RialOmani
        >>> rial_omani = RialOmani(
        ...     amount='123456.789')
        >>> print(rial_omani)
        ر.ع. ١٢٣٬٤٥٦٫٧٨٩

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '3٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '3\u066B\u066C3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            RialOmani: new `RialOmani` object.
        """
        return cast(
            RialOmani,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='OMR',
                numeric_code='512',
                symbol='ر.ع.',
                localized_symbol='ر.ع.',
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
            RialOmani: new opbject.
        """
        return self.__class__(amount, self._info[5])


class QatariRial(Currency):
    """Rial (Qatar) currency representation.

    Simple usage example:

        >>> from multicurrency import QatariRial
        >>> qatari_rial = QatariRial(
        ...     amount='123456.789')
        >>> print(qatari_rial)
        ر.ق. ١٢٣٬٤٥٦٫٧٩

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2\u066B\u066C3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            QatariRial: new `QatariRial` object.
        """
        return cast(
            QatariRial,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='QAR',
                numeric_code='634',
                symbol='ر.ق.',
                localized_symbol='ر.ق.',
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
            QatariRial: new opbject.
        """
        return self.__class__(amount, self._info[5])


class YemeniRial(Currency):
    """Rial (Yemen) currency representation.

    Simple usage example:

        >>> from multicurrency import YemeniRial
        >>> yemeni_rial = YemeniRial(
        ...     amount='123456.789')
        >>> print(yemeni_rial)
        ١٢٣٬٤٥٦٫٧٩ ﷼

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
            YemeniRial: new `YemeniRial` object.
        """
        return cast(
            YemeniRial,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='YER',
                numeric_code='886',
                symbol='﷼',
                localized_symbol='﷼',
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
            YemeniRial: new opbject.
        """
        return self.__class__(amount, self._info[5])
