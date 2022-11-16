# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Pound currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class EgyptianPound(Currency):
    """Pound (Egypt) currency representation.

    Simple usage example:

        >>> from multicurrency import EgyptianPound
        >>> egyptian_pound = EgyptianPound(
        ...     amount='123456.789')
        >>> print(egyptian_pound)
        ج.م. ١٢٣٬٤٥٦٫٧٩

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
    ) -> 'EgyptianPound':
        """Class creator.

        Returns:
            EgyptianPound: new `EgyptianPound` object.
        """
        return cast(
            EgyptianPound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EGP',
                numeric_code='818',
                symbol='ج.م.',
                localized_symbol='ج.م.',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EgyptianPound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class FalklandIslandsPound(Currency):
    """Pound (Falkland Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import FalklandIslandsPound
        >>> falkland_islands_pound = FalklandIslandsPound(
        ...     amount='123456.789')
        >>> print(falkland_islands_pound)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'FalklandIslandsPound':
        """Class creator.

        Returns:
            FalklandIslandsPound: new `FalklandIslandsPound` object.
        """
        return cast(
            FalklandIslandsPound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='FKP',
                numeric_code='238',
                symbol='£',
                localized_symbol='FK£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'FalklandIslandsPound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PoundSterling(Currency):
    """Pound (Great Britain) currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterling
        >>> pound_sterling = PoundSterling(
        ...     amount='123456.789')
        >>> print(pound_sterling)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'PoundSterling':
        """Class creator.

        Returns:
            PoundSterling: new `PoundSterling` object.
        """
        return cast(
            PoundSterling,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GBP',
                numeric_code='826',
                symbol='£',
                localized_symbol='£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PoundSterling':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PoundSterlingGG(Currency):
    """Pound (Alderney) currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingGG
        >>> pound_sterling_gg = PoundSterlingGG(
        ...     amount='123456.789')
        >>> print(pound_sterling_gg)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'PoundSterlingGG':
        """Class creator.

        Returns:
            PoundSterlingGG: new `PoundSterlingGG` object.
        """
        return cast(
            PoundSterlingGG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GBP',
                numeric_code='826',
                symbol='£',
                localized_symbol='GG£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PoundSterlingGG':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PoundSterlingIO(Currency):
    """Pound (British Indian Ocean Territory) currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingIO
        >>> pound_sterling_io = PoundSterlingIO(
        ...     amount='123456.789')
        >>> print(pound_sterling_io)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'PoundSterlingIO':
        """Class creator.

        Returns:
            PoundSterlingIO: new `PoundSterlingIO` object.
        """
        return cast(
            PoundSterlingIO,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GBP',
                numeric_code='826',
                symbol='£',
                localized_symbol='IO£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PoundSterlingIO':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PoundSterlingGB(Currency):
    """Pound (Great Britain) currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingGB
        >>> pound_sterling_gb = PoundSterlingGB(
        ...     amount='123456.789')
        >>> print(pound_sterling_gb)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'PoundSterlingGB':
        """Class creator.

        Returns:
            PoundSterlingGB: new `PoundSterlingGB` object.
        """
        return cast(
            PoundSterlingGB,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GBP',
                numeric_code='826',
                symbol='£',
                localized_symbol='GB£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PoundSterlingGB':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PoundSterlingIM(Currency):
    """Pound (Isle of Man) currency representation.

    Simple usage example:

        >>> from multicurrency import PoundSterlingIM
        >>> pound_sterling_im = PoundSterlingIM(
        ...     amount='123456.789')
        >>> print(pound_sterling_im)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'PoundSterlingIM':
        """Class creator.

        Returns:
            PoundSterlingIM: new `PoundSterlingIM` object.
        """
        return cast(
            PoundSterlingIM,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GBP',
                numeric_code='826',
                symbol='£',
                localized_symbol='IM£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PoundSterlingIM':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class GibraltarPound(Currency):
    """Pound (Gibraltar) currency representation.

    Simple usage example:

        >>> from multicurrency import GibraltarPound
        >>> gibraltar_pound = GibraltarPound(
        ...     amount='123456.789')
        >>> print(gibraltar_pound)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'GibraltarPound':
        """Class creator.

        Returns:
            GibraltarPound: new `GibraltarPound` object.
        """
        return cast(
            GibraltarPound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GIP',
                numeric_code='292',
                symbol='£',
                localized_symbol='GI£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'GibraltarPound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class LebanesePound(Currency):
    """Pound (Lebanon) currency representation.

    Simple usage example:

        >>> from multicurrency import LebanesePound
        >>> lebanese_pound = LebanesePound(
        ...     amount='123456.789')
        >>> print(lebanese_pound)
        ل.ل. ١٢٣٬٤٥٧

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0\u066B\u066C3%s\u00A0%a'
    ) -> 'LebanesePound':
        """Class creator.

        Returns:
            LebanesePound: new `LebanesePound` object.
        """
        return cast(
            LebanesePound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='LBP',
                numeric_code='422',
                symbol='ل.ل.',
                localized_symbol='ل.ل.',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'LebanesePound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SudanesePound(Currency):
    """Pound (Sudan) currency representation.

    Simple usage example:

        >>> from multicurrency import SudanesePound
        >>> sudanese_pound = SudanesePound(
        ...     amount='123456.789')
        >>> print(sudanese_pound)
        ١٢٣٬٤٥٦٫٧٩ ج.س

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
    ) -> 'SudanesePound':
        """Class creator.

        Returns:
            SudanesePound: new `SudanesePound` object.
        """
        return cast(
            SudanesePound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SDG',
                numeric_code='938',
                symbol='ج.س',
                localized_symbol='ج.س',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SudanesePound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SaintHelenaPoundAI(Currency):
    """Pound (Ascension Island) currency representation.

    Simple usage example:

        >>> from multicurrency import SaintHelenaPoundAI
        >>> saint_helena_pound_ai = SaintHelenaPoundAI(
        ...     amount='123456.789')
        >>> print(saint_helena_pound_ai)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'SaintHelenaPoundAI':
        """Class creator.

        Returns:
            SaintHelenaPoundAI: new `SaintHelenaPoundAI` object.
        """
        return cast(
            SaintHelenaPoundAI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SHP',
                numeric_code='654',
                symbol='£',
                localized_symbol='SH£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SaintHelenaPoundAI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SaintHelenaPound(Currency):
    """Pound (Saint Helena) currency representation.

    Simple usage example:

        >>> from multicurrency import SaintHelenaPound
        >>> saint_helena_pound = SaintHelenaPound(
        ...     amount='123456.789')
        >>> print(saint_helena_pound)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'SaintHelenaPound':
        """Class creator.

        Returns:
            SaintHelenaPound: new `SaintHelenaPound` object.
        """
        return cast(
            SaintHelenaPound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SHP',
                numeric_code='654',
                symbol='£',
                localized_symbol='SH£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SaintHelenaPound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SaintHelenaPoundTC(Currency):
    """Pound (Tristan da Cunha) currency representation.

    Simple usage example:

        >>> from multicurrency import SaintHelenaPoundTC
        >>> saint_helena_pound_tc = SaintHelenaPoundTC(
        ...     amount='123456.789')
        >>> print(saint_helena_pound_tc)
        £123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%-%s%u'
    ) -> 'SaintHelenaPoundTC':
        """Class creator.

        Returns:
            SaintHelenaPoundTC: new `SaintHelenaPoundTC` object.
        """
        return cast(
            SaintHelenaPoundTC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SHP',
                numeric_code='654',
                symbol='£',
                localized_symbol='SH£',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SaintHelenaPoundTC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SyrianPound(Currency):
    """Pound (Syria) currency representation.

    Simple usage example:

        >>> from multicurrency import SyrianPound
        >>> syrian_pound = SyrianPound(
        ...     amount='123456.789')
        >>> print(syrian_pound)
        ١٢٣٬٤٥٦٫٧٩ ل.س

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
    ) -> 'SyrianPound':
        """Class creator.

        Returns:
            SyrianPound: new `SyrianPound` object.
        """
        return cast(
            SyrianPound,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SYP',
                numeric_code='760',
                symbol='ل.س',
                localized_symbol='ل.س',
                convertion='٠١٢٣٤٥٦٧٨٩-',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SyrianPound':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
