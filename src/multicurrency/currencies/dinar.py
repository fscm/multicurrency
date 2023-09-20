# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dinar currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class BahrainiDinar(Currency):
    """Dinar (Bahrain) currency representation.

    Simple usage example:

        >>> from multicurrency import BahrainiDinar
        >>> bahraini_dinar = BahrainiDinar(
        ...     amount='123456.789')
        >>> print(bahraini_dinar)
        د.ب. ١٢٣٬٤٥٦٫٧٨٩

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
            BahrainiDinar: new `BahrainiDinar` object.
        """
        return cast(
            BahrainiDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BHD',
                numeric_code='048',
                symbol='د.ب.',
                localized_symbol='د.ب.',
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
            BahrainiDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AlgerianDinar(Currency):
    """Dinar (Algeria) currency representation.

    Simple usage example:

        >>> from multicurrency import AlgerianDinar
        >>> algerian_dinar = AlgerianDinar(
        ...     amount='123456.789')
        >>> print(algerian_dinar)
        123.456,79 د.ج.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            AlgerianDinar: new `AlgerianDinar` object.
        """
        return cast(
            AlgerianDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='DZD',
                numeric_code='012',
                symbol='د.ج.',
                localized_symbol='د.ج.',
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
            AlgerianDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class IraqiDinar(Currency):
    """Dinar (Iraq) currency representation.

    Simple usage example:

        >>> from multicurrency import IraqiDinar
        >>> iraqi_dinar = IraqiDinar(
        ...     amount='123456.789')
        >>> print(iraqi_dinar)
        د.ع. ١٢٣٬٤٥٦٫٧٨٩

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
            IraqiDinar: new `IraqiDinar` object.
        """
        return cast(
            IraqiDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='IQD',
                numeric_code='368',
                symbol='د.ع.',
                localized_symbol='د.ع.',
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
            IraqiDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class JordanianDinar(Currency):
    """Dinar (Jordan) currency representation.

    Simple usage example:

        >>> from multicurrency import JordanianDinar
        >>> jordanian_dinar = JordanianDinar(
        ...     amount='123456.789')
        >>> print(jordanian_dinar)
        د.أ. ١٢٣٬٤٥٦٫٧٨٩

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
            JordanianDinar: new `JordanianDinar` object.
        """
        return cast(
            JordanianDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='JOD',
                numeric_code='400',
                symbol='د.أ.',
                localized_symbol='د.أ.',
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
            JordanianDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class KuwaitiDinar(Currency):
    """Dinar (Kuwait) currency representation.

    Simple usage example:

        >>> from multicurrency import KuwaitiDinar
        >>> kuwaiti_dinar = KuwaitiDinar(
        ...     amount='123456.789')
        >>> print(kuwaiti_dinar)
        د.ك. ١٢٣٬٤٥٦٫٧٨٩

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
            KuwaitiDinar: new `KuwaitiDinar` object.
        """
        return cast(
            KuwaitiDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KWD',
                numeric_code='414',
                symbol='د.ك.',
                localized_symbol='د.ك.',
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
            KuwaitiDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class LibyanDinar(Currency):
    """Dinar (Libya) currency representation.

    Simple usage example:

        >>> from multicurrency import LibyanDinar
        >>> libyan_dinar = LibyanDinar(
        ...     amount='123456.789')
        >>> print(libyan_dinar)
        د.ل. 123.456,789

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '3,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '3,.3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            LibyanDinar: new `LibyanDinar` object.
        """
        return cast(
            LibyanDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='LYD',
                numeric_code='434',
                symbol='د.ل.',
                localized_symbol='د.ل.',
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
            LibyanDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SerbianDinarXK(Currency):
    """Dinar (Kosovo) currency representation.

    Simple usage example:

        >>> from multicurrency import SerbianDinarXK
        >>> serbian_dinar_xk = SerbianDinarXK(
        ...     amount='123456.789')
        >>> print(serbian_dinar_xk)
        123.456,79 дин.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,.3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            SerbianDinarXK: new `SerbianDinarXK` object.
        """
        return cast(
            SerbianDinarXK,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RSD',
                numeric_code='941',
                symbol='дин.',
                localized_symbol='дин.',
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
            SerbianDinarXK: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SerbianDinarSR(Currency):
    """Dinar (Serbia) currency representation.

    Simple usage example:

        >>> from multicurrency import SerbianDinarSR
        >>> serbian_dinar_sr = SerbianDinarSR(
        ...     amount='123456.789')
        >>> print(serbian_dinar_sr)
        123 456,79 дин.

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            SerbianDinarSR: new `SerbianDinarSR` object.
        """
        return cast(
            SerbianDinarSR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RSD',
                numeric_code='941',
                symbol='дин.',
                localized_symbol='дин.',
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
            SerbianDinarSR: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TunisianDinar(Currency):
    """Dinar (Tunisia) currency representation.

    Simple usage example:

        >>> from multicurrency import TunisianDinar
        >>> tunisian_dinar = TunisianDinar(
        ...     amount='123456.789')
        >>> print(tunisian_dinar)
        د.ت. 123.456,789

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '3,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '3,.3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            TunisianDinar: new `TunisianDinar` object.
        """
        return cast(
            TunisianDinar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TND',
                numeric_code='788',
                symbol='د.ت.',
                localized_symbol='د.ت.',
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
            TunisianDinar: new opbject.
        """
        return self.__class__(amount, self._info[5])
