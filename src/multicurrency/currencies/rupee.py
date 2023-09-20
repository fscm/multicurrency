# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rupee currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class IndianRupee(Currency):
    """Rupee (India) currency representation.

    Simple usage example:

        >>> from multicurrency import IndianRupee
        >>> indian_rupee = IndianRupee(
        ...     amount='123456.789')
        >>> print(indian_rupee)
        ₹123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            IndianRupee: new `IndianRupee` object.
        """
        return cast(
            IndianRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='INR',
                numeric_code='356',
                symbol='₹',
                localized_symbol='₹',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            IndianRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])


class IndianRupeeBT(Currency):
    """Rupee (Bhutan) currency representation.

    Simple usage example:

        >>> from multicurrency import IndianRupeeBT
        >>> indian_rupee_bt = IndianRupeeBT(
        ...     amount='123456.789')
        >>> print(indian_rupee_bt)
        ₹123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            IndianRupeeBT: new `IndianRupeeBT` object.
        """
        return cast(
            IndianRupeeBT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='INR',
                numeric_code='356',
                symbol='₹',
                localized_symbol='BT₹',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            IndianRupeeBT: new opbject.
        """
        return self.__class__(amount, self._info[5])


class IndianRupeeIN(Currency):
    """Rupee (India) currency representation.

    Simple usage example:

        >>> from multicurrency import IndianRupeeIN
        >>> indian_rupee_in = IndianRupeeIN(
        ...     amount='123456.789')
        >>> print(indian_rupee_in)
        ₹123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%-%s%u',
    ) -> Self:
        """Class creator.

        Returns:
            IndianRupeeIN: new `IndianRupeeIN` object.
        """
        return cast(
            IndianRupeeIN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='INR',
                numeric_code='356',
                symbol='₹',
                localized_symbol='IN₹',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            IndianRupeeIN: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SriLankaRupee(Currency):
    """Rupee (Sri Lanka) currency representation.

    Simple usage example:

        >>> from multicurrency import SriLankaRupee
        >>> sri_lanka_rupee = SriLankaRupee(
        ...     amount='123456.789')
        >>> print(sri_lanka_rupee)
        රු. 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            SriLankaRupee: new `SriLankaRupee` object.
        """
        return cast(
            SriLankaRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='LKR',
                numeric_code='144',
                symbol='රු.',
                localized_symbol='රු.',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            SriLankaRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])


class MauritiusRupee(Currency):
    """Rupee (Mauritius) currency representation.

    Simple usage example:

        >>> from multicurrency import MauritiusRupee
        >>> mauritius_rupee = MauritiusRupee(
        ...     amount='123456.789')
        >>> print(mauritius_rupee)
        ₨ 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            MauritiusRupee: new `MauritiusRupee` object.
        """
        return cast(
            MauritiusRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MUR',
                numeric_code='480',
                symbol='₨',
                localized_symbol='₨',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            MauritiusRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NepaleseRupee(Currency):
    """Rupee (Nepal) currency representation.

    Simple usage example:

        >>> from multicurrency import NepaleseRupee
        >>> nepalese_rupee = NepaleseRupee(
        ...     amount='123456.789')
        >>> print(nepalese_rupee)
        नेरू १२३,४५६.७९

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            NepaleseRupee: new `NepaleseRupee` object.
        """
        return cast(
            NepaleseRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NPR',
                numeric_code='524',
                symbol='नेरू',
                localized_symbol='नेरू',
                convertion='०१२३४५६७८९-',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            NepaleseRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PakistanRupee(Currency):
    """Rupee (Pakistan) currency representation.

    Simple usage example:

        >>> from multicurrency import PakistanRupee
        >>> pakistan_rupee = PakistanRupee(
        ...     amount='123456.789')
        >>> print(pakistan_rupee)
        ₨ 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            PakistanRupee: new `PakistanRupee` object.
        """
        return cast(
            PakistanRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='PKR',
                numeric_code='586',
                symbol='₨',
                localized_symbol='₨',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            PakistanRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SeychellesRupee(Currency):
    """Rupee (Seychelles) currency representation.

    Simple usage example:

        >>> from multicurrency import SeychellesRupee
        >>> seychelles_rupee = SeychellesRupee(
        ...     amount='123456.789')
        >>> print(seychelles_rupee)
        ₨ 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.,3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            SeychellesRupee: new `SeychellesRupee` object.
        """
        return cast(
            SeychellesRupee,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SCR',
                numeric_code='690',
                symbol='₨',
                localized_symbol='₨',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            SeychellesRupee: new opbject.
        """
        return self.__class__(amount, self._info[5])
