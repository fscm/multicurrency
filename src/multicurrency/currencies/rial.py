# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Rial currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


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
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%a\u00A0%s'
    ) -> 'IranianRial':
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
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'IranianRial':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
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
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '3٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '3\u066B\u066C3%s\u00A0%a'
    ) -> 'RialOmani':
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
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'RialOmani':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
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
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%s\u00A0%a'
    ) -> 'QatariRial':
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
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'QatariRial':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
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
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2٫٬3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2\u066B\u066C3%a\u00A0%s'
    ) -> 'YemeniRial':
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
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'YemeniRial':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
