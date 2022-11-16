# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Dollar currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class AustralianDollar(Currency):
    """Dollar (Australia) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollar
        >>> australian_dollar = AustralianDollar(
        ...     amount='123456.789')
        >>> print(australian_dollar)
        $ 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'AustralianDollar':
        """Class creator.

        Returns:
            AustralianDollar: new `AustralianDollar` object.
        """
        return cast(
            AustralianDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AustralianDollarAU(Currency):
    """Dollar (Australia) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollarAU
        >>> australian_dollar_au = AustralianDollarAU(
        ...     amount='123456.789')
        >>> print(australian_dollar_au)
        $123,456.79

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
    ) -> 'AustralianDollarAU':
        """Class creator.

        Returns:
            AustralianDollarAU: new `AustralianDollarAU` object.
        """
        return cast(
            AustralianDollarAU,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='AU$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollarAU':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AustralianDollarKI(Currency):
    """Dollar (Kiribati) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollarKI
        >>> australian_dollar_ki = AustralianDollarKI(
        ...     amount='123456.789')
        >>> print(australian_dollar_ki)
        $123,456.79

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
    ) -> 'AustralianDollarKI':
        """Class creator.

        Returns:
            AustralianDollarKI: new `AustralianDollarKI` object.
        """
        return cast(
            AustralianDollarKI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='KI$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollarKI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AustralianDollarCC(Currency):
    """Dollar (Coconut Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollarCC
        >>> australian_dollar_cc = AustralianDollarCC(
        ...     amount='123456.789')
        >>> print(australian_dollar_cc)
        $123,456.79

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
    ) -> 'AustralianDollarCC':
        """Class creator.

        Returns:
            AustralianDollarCC: new `AustralianDollarCC` object.
        """
        return cast(
            AustralianDollarCC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='CC$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollarCC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AustralianDollarMR(Currency):
    """Dollar (Nauru) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollarMR
        >>> australian_dollar_mr = AustralianDollarMR(
        ...     amount='123456.789')
        >>> print(australian_dollar_mr)
        $123,456.79

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
    ) -> 'AustralianDollarMR':
        """Class creator.

        Returns:
            AustralianDollarMR: new `AustralianDollarMR` object.
        """
        return cast(
            AustralianDollarMR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='NR$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollarMR':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class AustralianDollarTV(Currency):
    """Dollar (Tuvalu) currency representation.

    Simple usage example:

        >>> from multicurrency import AustralianDollarTV
        >>> australian_dollar_tv = AustralianDollarTV(
        ...     amount='123456.789')
        >>> print(australian_dollar_tv)
        $123,456.79

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
    ) -> 'AustralianDollarTV':
        """Class creator.

        Returns:
            AustralianDollarTV: new `AustralianDollarTV` object.
        """
        return cast(
            AustralianDollarTV,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='AUD',
                numeric_code='036',
                symbol='$',
                localized_symbol='TV$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'AustralianDollarTV':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BarbadosDollar(Currency):
    """Dollar (Barbados) currency representation.

    Simple usage example:

        >>> from multicurrency import BarbadosDollar
        >>> barbados_dollar = BarbadosDollar(
        ...     amount='123456.789')
        >>> print(barbados_dollar)
        $123,456.79

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
    ) -> 'BarbadosDollar':
        """Class creator.

        Returns:
            BarbadosDollar: new `BarbadosDollar` object.
        """
        return cast(
            BarbadosDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BBD',
                numeric_code='052',
                symbol='$',
                localized_symbol='BB$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BarbadosDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BermudianDollar(Currency):
    """Dollar (Bermuda) currency representation.

    Simple usage example:

        >>> from multicurrency import BermudianDollar
        >>> bermudian_dollar = BermudianDollar(
        ...     amount='123456.789')
        >>> print(bermudian_dollar)
        $123,456.79

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
    ) -> 'BermudianDollar':
        """Class creator.

        Returns:
            BermudianDollar: new `BermudianDollar` object.
        """
        return cast(
            BermudianDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BMD',
                numeric_code='060',
                symbol='$',
                localized_symbol='BM$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BermudianDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BruneiDollar(Currency):
    """Dollar (Brunei) currency representation.

    Simple usage example:

        >>> from multicurrency import BruneiDollar
        >>> brunei_dollar = BruneiDollar(
        ...     amount='123456.789')
        >>> print(brunei_dollar)
        $ 123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%s\u00A0%a'
    ) -> 'BruneiDollar':
        """Class creator.

        Returns:
            BruneiDollar: new `BruneiDollar` object.
        """
        return cast(
            BruneiDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BND',
                numeric_code='096',
                symbol='$',
                localized_symbol='$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BruneiDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BruneiDollarBN(Currency):
    """Dollar (Brunei) currency representation.

    Simple usage example:

        >>> from multicurrency import BruneiDollarBN
        >>> brunei_dollar_bn = BruneiDollarBN(
        ...     amount='123456.789')
        >>> print(brunei_dollar_bn)
        $ 123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%s\u00A0%a'
    ) -> 'BruneiDollarBN':
        """Class creator.

        Returns:
            BruneiDollarBN: new `BruneiDollarBN` object.
        """
        return cast(
            BruneiDollarBN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BND',
                numeric_code='096',
                symbol='$',
                localized_symbol='BN$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BruneiDollarBN':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BruneiDollarSG(Currency):
    """Dollar (Singapore) currency representation.

    Simple usage example:

        >>> from multicurrency import BruneiDollarSG
        >>> brunei_dollar_sg = BruneiDollarSG(
        ...     amount='123456.789')
        >>> print(brunei_dollar_sg)
        $ 123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%s\u00A0%a'
    ) -> 'BruneiDollarSG':
        """Class creator.

        Returns:
            BruneiDollarSG: new `BruneiDollarSG` object.
        """
        return cast(
            BruneiDollarSG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BND',
                numeric_code='096',
                symbol='$',
                localized_symbol='SG$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BruneiDollarSG':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BahamianDollar(Currency):
    """Dollar (Bahamas) currency representation.

    Simple usage example:

        >>> from multicurrency import BahamianDollar
        >>> bahamian_dollar = BahamianDollar(
        ...     amount='123456.789')
        >>> print(bahamian_dollar)
        $123,456.79

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
    ) -> 'BahamianDollar':
        """Class creator.

        Returns:
            BahamianDollar: new `BahamianDollar` object.
        """
        return cast(
            BahamianDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BSD',
                numeric_code='044',
                symbol='$',
                localized_symbol='BS$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BahamianDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class BelizeDollar(Currency):
    """Dollar (Belize) currency representation.

    Simple usage example:

        >>> from multicurrency import BelizeDollar
        >>> belize_dollar = BelizeDollar(
        ...     amount='123456.789')
        >>> print(belize_dollar)
        $123,456.79

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
    ) -> 'BelizeDollar':
        """Class creator.

        Returns:
            BelizeDollar: new `BelizeDollar` object.
        """
        return cast(
            BelizeDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BZD',
                numeric_code='084',
                symbol='$',
                localized_symbol='BZ$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'BelizeDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CanadianDollarEN(Currency):
    """Dollar (Canada) currency representation.

    Simple usage example:

        >>> from multicurrency import CanadianDollarEN
        >>> canadian_dollar_en = CanadianDollarEN(
        ...     amount='123456.789')
        >>> print(canadian_dollar_en)
        $123,456.79

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
    ) -> 'CanadianDollarEN':
        """Class creator.

        Returns:
            CanadianDollarEN: new `CanadianDollarEN` object.
        """
        return cast(
            CanadianDollarEN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CAD',
                numeric_code='124',
                symbol='$',
                localized_symbol='CA$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CanadianDollarEN':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CanadianDollarFR(Currency):
    """Dollar (Canada) currency representation.

    Simple usage example:

        >>> from multicurrency import CanadianDollarFR
        >>> canadian_dollar_fr = CanadianDollarFR(
        ...     amount='123456.789')
        >>> print(canadian_dollar_fr)
        123 456,79 $

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,\u202F3%a\u00A0%s'
    ) -> 'CanadianDollarFR':
        """Class creator.

        Returns:
            CanadianDollarFR: new `CanadianDollarFR` object.
        """
        return cast(
            CanadianDollarFR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CAD',
                numeric_code='124',
                symbol='$',
                localized_symbol='CA$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CanadianDollarFR':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class FijiDollar(Currency):
    """Dollar (Fiji) currency representation.

    Simple usage example:

        >>> from multicurrency import FijiDollar
        >>> fiji_dollar = FijiDollar(
        ...     amount='123456.789')
        >>> print(fiji_dollar)
        $123,456.79

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
    ) -> 'FijiDollar':
        """Class creator.

        Returns:
            FijiDollar: new `FijiDollar` object.
        """
        return cast(
            FijiDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='FJD',
                numeric_code='242',
                symbol='$',
                localized_symbol='FJ$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'FijiDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class GuyanaDollar(Currency):
    """Dollar (Guyana) currency representation.

    Simple usage example:

        >>> from multicurrency import GuyanaDollar
        >>> guyana_dollar = GuyanaDollar(
        ...     amount='123456.789')
        >>> print(guyana_dollar)
        $123,456.79

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
    ) -> 'GuyanaDollar':
        """Class creator.

        Returns:
            GuyanaDollar: new `GuyanaDollar` object.
        """
        return cast(
            GuyanaDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GYD',
                numeric_code='328',
                symbol='$',
                localized_symbol='GY$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'GuyanaDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class HongKongDollar(Currency):
    """Dollar (Hong Kong) currency representation.

    Simple usage example:

        >>> from multicurrency import HongKongDollar
        >>> hong_kong_dollar = HongKongDollar(
        ...     amount='123456.789')
        >>> print(hong_kong_dollar)
        $123,456.79

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
    ) -> 'HongKongDollar':
        """Class creator.

        Returns:
            HongKongDollar: new `HongKongDollar` object.
        """
        return cast(
            HongKongDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='HKD',
                numeric_code='344',
                symbol='$',
                localized_symbol='HK$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'HongKongDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class JamaicanDollar(Currency):
    """Dollar (Jamaica) currency representation.

    Simple usage example:

        >>> from multicurrency import JamaicanDollar
        >>> jamaican_dollar = JamaicanDollar(
        ...     amount='123456.789')
        >>> print(jamaican_dollar)
        $123,456.79

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
    ) -> 'JamaicanDollar':
        """Class creator.

        Returns:
            JamaicanDollar: new `JamaicanDollar` object.
        """
        return cast(
            JamaicanDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='JMD',
                numeric_code='388',
                symbol='$',
                localized_symbol='JM$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'JamaicanDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CaymanIslandsDollar(Currency):
    """Dollar (Cayman Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import CaymanIslandsDollar
        >>> cayman_islands_dollar = CaymanIslandsDollar(
        ...     amount='123456.789')
        >>> print(cayman_islands_dollar)
        $123,456.79

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
    ) -> 'CaymanIslandsDollar':
        """Class creator.

        Returns:
            CaymanIslandsDollar: new `CaymanIslandsDollar` object.
        """
        return cast(
            CaymanIslandsDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='KYD',
                numeric_code='136',
                symbol='$',
                localized_symbol='KY$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CaymanIslandsDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class LiberianDollar(Currency):
    """Dollar (Liberia) currency representation.

    Simple usage example:

        >>> from multicurrency import LiberianDollar
        >>> liberian_dollar = LiberianDollar(
        ...     amount='123456.789')
        >>> print(liberian_dollar)
        $123,456.79

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
    ) -> 'LiberianDollar':
        """Class creator.

        Returns:
            LiberianDollar: new `LiberianDollar` object.
        """
        return cast(
            LiberianDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='LRD',
                numeric_code='430',
                symbol='$',
                localized_symbol='LR$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'LiberianDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NamibiaDollar(Currency):
    """Dollar (Namibia) currency representation.

    Simple usage example:

        >>> from multicurrency import NamibiaDollar
        >>> namibia_dollar = NamibiaDollar(
        ...     amount='123456.789')
        >>> print(namibia_dollar)
        $123,456.79

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
    ) -> 'NamibiaDollar':
        """Class creator.

        Returns:
            NamibiaDollar: new `NamibiaDollar` object.
        """
        return cast(
            NamibiaDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NAD',
                numeric_code='516',
                symbol='$',
                localized_symbol='NA$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NamibiaDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewZealandDollar(Currency):
    """Dollar (New Zealand) currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollar
        >>> new_zealand_dollar = NewZealandDollar(
        ...     amount='123456.789')
        >>> print(new_zealand_dollar)
        $123,456.79

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
    ) -> 'NewZealandDollar':
        """Class creator.

        Returns:
            NewZealandDollar: new `NewZealandDollar` object.
        """
        return cast(
            NewZealandDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NZD',
                numeric_code='554',
                symbol='$',
                localized_symbol='$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewZealandDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewZealandDollarCK(Currency):
    """Dollar (Cook Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollarCK
        >>> new_zealand_dollar_ck = NewZealandDollarCK(
        ...     amount='123456.789')
        >>> print(new_zealand_dollar_ck)
        $123,456.79

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
    ) -> 'NewZealandDollarCK':
        """Class creator.

        Returns:
            NewZealandDollarCK: new `NewZealandDollarCK` object.
        """
        return cast(
            NewZealandDollarCK,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NZD',
                numeric_code='554',
                symbol='$',
                localized_symbol='CK$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewZealandDollarCK':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewZealandDollarNZ(Currency):
    """Dollar (New Zealand) currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollarNZ
        >>> new_zealand_dollar_nz = NewZealandDollarNZ(
        ...     amount='123456.789')
        >>> print(new_zealand_dollar_nz)
        $123,456.79

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
    ) -> 'NewZealandDollarNZ':
        """Class creator.

        Returns:
            NewZealandDollarNZ: new `NewZealandDollarNZ` object.
        """
        return cast(
            NewZealandDollarNZ,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NZD',
                numeric_code='554',
                symbol='$',
                localized_symbol='NZ$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewZealandDollarNZ':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewZealandDollarNU(Currency):
    """Dollar (Niue) currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollarNU
        >>> new_zealand_dollar_nu = NewZealandDollarNU(
        ...     amount='123456.789')
        >>> print(new_zealand_dollar_nu)
        $123,456.79

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
    ) -> 'NewZealandDollarNU':
        """Class creator.

        Returns:
            NewZealandDollarNU: new `NewZealandDollarNU` object.
        """
        return cast(
            NewZealandDollarNU,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NZD',
                numeric_code='554',
                symbol='$',
                localized_symbol='NU$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewZealandDollarNU':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class NewZealandDollarPN(Currency):
    """Dollar (Pitcairn Island) currency representation.

    Simple usage example:

        >>> from multicurrency import NewZealandDollarPN
        >>> new_zealand_dollar_pn = NewZealandDollarPN(
        ...     amount='123456.789')
        >>> print(new_zealand_dollar_pn)
        $123,456.79

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
    ) -> 'NewZealandDollarPN':
        """Class creator.

        Returns:
            NewZealandDollarPN: new `NewZealandDollarPN` object.
        """
        return cast(
            NewZealandDollarPN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='NZD',
                numeric_code='554',
                symbol='$',
                localized_symbol='PN$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'NewZealandDollarPN':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SolomonIslandsDollar(Currency):
    """Dollar (Solomon Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import SolomonIslandsDollar
        >>> solomon_islands_dollar = SolomonIslandsDollar(
        ...     amount='123456.789')
        >>> print(solomon_islands_dollar)
        $123,456.79

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
    ) -> 'SolomonIslandsDollar':
        """Class creator.

        Returns:
            SolomonIslandsDollar: new `SolomonIslandsDollar` object.
        """
        return cast(
            SolomonIslandsDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SBD',
                numeric_code='090',
                symbol='$',
                localized_symbol='SB$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SolomonIslandsDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SingaporeDollar(Currency):
    """Dollar (Singapore) currency representation.

    Simple usage example:

        >>> from multicurrency import SingaporeDollar
        >>> singapore_dollar = SingaporeDollar(
        ...     amount='123456.789')
        >>> print(singapore_dollar)
        $123,456.79

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
    ) -> 'SingaporeDollar':
        """Class creator.

        Returns:
            SingaporeDollar: new `SingaporeDollar` object.
        """
        return cast(
            SingaporeDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SGD',
                numeric_code='702',
                symbol='$',
                localized_symbol='$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SingaporeDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SingaporeDollarBN(Currency):
    """Dollar (Brunei) currency representation.

    Simple usage example:

        >>> from multicurrency import SingaporeDollarBN
        >>> singapore_dollar_bn = SingaporeDollarBN(
        ...     amount='123456.789')
        >>> print(singapore_dollar_bn)
        $123,456.79

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
    ) -> 'SingaporeDollarBN':
        """Class creator.

        Returns:
            SingaporeDollarBN: new `SingaporeDollarBN` object.
        """
        return cast(
            SingaporeDollarBN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SGD',
                numeric_code='702',
                symbol='$',
                localized_symbol='BN$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SingaporeDollarBN':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SingaporeDollarSG(Currency):
    """Dollar (Singapore) currency representation.

    Simple usage example:

        >>> from multicurrency import SingaporeDollarSG
        >>> singapore_dollar_sg = SingaporeDollarSG(
        ...     amount='123456.789')
        >>> print(singapore_dollar_sg)
        $123,456.79

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
    ) -> 'SingaporeDollarSG':
        """Class creator.

        Returns:
            SingaporeDollarSG: new `SingaporeDollarSG` object.
        """
        return cast(
            SingaporeDollarSG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SGD',
                numeric_code='702',
                symbol='$',
                localized_symbol='SG$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SingaporeDollarSG':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SurinameDollar(Currency):
    """Dollar (Suriname) currency representation.

    Simple usage example:

        >>> from multicurrency import SurinameDollar
        >>> suriname_dollar = SurinameDollar(
        ...     amount='123456.789')
        >>> print(suriname_dollar)
        $ 123.456,79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%s\u00A0%a'
    ) -> 'SurinameDollar':
        """Class creator.

        Returns:
            SurinameDollar: new `SurinameDollar` object.
        """
        return cast(
            SurinameDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='SRD',
                numeric_code='968',
                symbol='$',
                localized_symbol='SR$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'SurinameDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TrinidadandTobagoDollar(Currency):
    """Dollar (Trinidad and Tobago) currency representation.

    Simple usage example:

        >>> from multicurrency import TrinidadandTobagoDollar
        >>> trinidad_and_tobago_dollar = TrinidadandTobagoDollar(
        ...     amount='123456.789')
        >>> print(trinidad_and_tobago_dollar)
        $123,456.79

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
    ) -> 'TrinidadandTobagoDollar':
        """Class creator.

        Returns:
            TrinidadandTobagoDollar: new `TrinidadandTobagoDollar` object.
        """
        return cast(
            TrinidadandTobagoDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TTD',
                numeric_code='780',
                symbol='$',
                localized_symbol='TT$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'TrinidadandTobagoDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class TaiwanDollar(Currency):
    """Dollar (Taiwan) currency representation.

    Simple usage example:

        >>> from multicurrency import TaiwanDollar
        >>> taiwan_dollar = TaiwanDollar(
        ...     amount='123456.789')
        >>> print(taiwan_dollar)
        $123,456.79

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
    ) -> 'TaiwanDollar':
        """Class creator.

        Returns:
            TaiwanDollar: new `TaiwanDollar` object.
        """
        return cast(
            TaiwanDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='TWD',
                numeric_code='901',
                symbol='$',
                localized_symbol='TW$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'TaiwanDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollar(Currency):
    """Dollar (United States of America) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollar
        >>> us_dollar = USDollar(
        ...     amount='123456.789')
        >>> print(us_dollar)
        $123,456.79

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
    ) -> 'USDollar':
        """Class creator.

        Returns:
            USDollar: new `USDollar` object.
        """
        return cast(
            USDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='US$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarAS(Currency):
    """Dollar (American Samoa) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarAS
        >>> us_dollar_as = USDollarAS(
        ...     amount='123456.789')
        >>> print(us_dollar_as)
        $123,456.79

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
    ) -> 'USDollarAS':
        """Class creator.

        Returns:
            USDollarAS: new `USDollarAS` object.
        """
        return cast(
            USDollarAS,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='AS$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarAS':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarIO(Currency):
    """Dollar (British Indian Ocean Territory) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarIO
        >>> us_dollar_io = USDollarIO(
        ...     amount='123456.789')
        >>> print(us_dollar_io)
        $123,456.79

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
    ) -> 'USDollarIO':
        """Class creator.

        Returns:
            USDollarIO: new `USDollarIO` object.
        """
        return cast(
            USDollarIO,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='IO$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarIO':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarVG(Currency):
    """Dollar (British Virgin Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarVG
        >>> us_dollar_vg = USDollarVG(
        ...     amount='123456.789')
        >>> print(us_dollar_vg)
        $123,456.79

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
    ) -> 'USDollarVG':
        """Class creator.

        Returns:
            USDollarVG: new `USDollarVG` object.
        """
        return cast(
            USDollarVG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='VG$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarVG':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarGU(Currency):
    """Dollar (Guam) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarGU
        >>> us_dollar_gu = USDollarGU(
        ...     amount='123456.789')
        >>> print(us_dollar_gu)
        $123,456.79

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
    ) -> 'USDollarGU':
        """Class creator.

        Returns:
            USDollarGU: new `USDollarGU` object.
        """
        return cast(
            USDollarGU,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='GU$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarGU':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarHT(Currency):
    """Dollar (Haiti) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarHT
        >>> us_dollar_ht = USDollarHT(
        ...     amount='123456.789')
        >>> print(us_dollar_ht)
        $123,456.79

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
    ) -> 'USDollarHT':
        """Class creator.

        Returns:
            USDollarHT: new `USDollarHT` object.
        """
        return cast(
            USDollarHT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='HT$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarHT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarMH(Currency):
    """Dollar (Marshall Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarMH
        >>> us_dollar_mh = USDollarMH(
        ...     amount='123456.789')
        >>> print(us_dollar_mh)
        $123,456.79

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
    ) -> 'USDollarMH':
        """Class creator.

        Returns:
            USDollarMH: new `USDollarMH` object.
        """
        return cast(
            USDollarMH,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='MH$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarMH':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarFM(Currency):
    """Dollar (Micronesia) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarFM
        >>> us_dollar_fm = USDollarFM(
        ...     amount='123456.789')
        >>> print(us_dollar_fm)
        $123,456.79

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
    ) -> 'USDollarFM':
        """Class creator.

        Returns:
            USDollarFM: new `USDollarFM` object.
        """
        return cast(
            USDollarFM,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='FM$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarFM':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarMP(Currency):
    """Dollar (Northern Mariana Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarMP
        >>> us_dollar_mp = USDollarMP(
        ...     amount='123456.789')
        >>> print(us_dollar_mp)
        $123,456.79

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
    ) -> 'USDollarMP':
        """Class creator.

        Returns:
            USDollarMP: new `USDollarMP` object.
        """
        return cast(
            USDollarMP,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='MP$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarMP':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarPC(Currency):
    """Dollar (Pacific Remote Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarPC
        >>> us_dollar_pc = USDollarPC(
        ...     amount='123456.789')
        >>> print(us_dollar_pc)
        $123,456.79

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
    ) -> 'USDollarPC':
        """Class creator.

        Returns:
            USDollarPC: new `USDollarPC` object.
        """
        return cast(
            USDollarPC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='PC$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarPC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarPW(Currency):
    """Dollar (Palau) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarPW
        >>> us_dollar_pw = USDollarPW(
        ...     amount='123456.789')
        >>> print(us_dollar_pw)
        $123,456.79

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
    ) -> 'USDollarPW':
        """Class creator.

        Returns:
            USDollarPW: new `USDollarPW` object.
        """
        return cast(
            USDollarPW,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='PW$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarPW':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarPA(Currency):
    """Dollar (Panama) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarPA
        >>> us_dollar_pa = USDollarPA(
        ...     amount='123456.789')
        >>> print(us_dollar_pa)
        $123,456.79

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
    ) -> 'USDollarPA':
        """Class creator.

        Returns:
            USDollarPA: new `USDollarPA` object.
        """
        return cast(
            USDollarPA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='PA$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarPA':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarPR(Currency):
    """Dollar (Puerto Rico) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarPR
        >>> us_dollar_pr = USDollarPR(
        ...     amount='123456.789')
        >>> print(us_dollar_pr)
        $123,456.79

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
    ) -> 'USDollarPR':
        """Class creator.

        Returns:
            USDollarPR: new `USDollarPR` object.
        """
        return cast(
            USDollarPR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='PR$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarPR':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarTC(Currency):
    """Dollar (Turks and Caicos Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarTC
        >>> us_dollar_tc = USDollarTC(
        ...     amount='123456.789')
        >>> print(us_dollar_tc)
        $123,456.79

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
    ) -> 'USDollarTC':
        """Class creator.

        Returns:
            USDollarTC: new `USDollarTC` object.
        """
        return cast(
            USDollarTC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='TC$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarTC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class USDollarVI(Currency):
    """Dollar (US Virgin Islands) currency representation.

    Simple usage example:

        >>> from multicurrency import USDollarVI
        >>> us_dollar_vi = USDollarVI(
        ...     amount='123456.789')
        >>> print(us_dollar_vi)
        $123,456.79

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
    ) -> 'USDollarVI':
        """Class creator.

        Returns:
            USDollarVI: new `USDollarVI` object.
        """
        return cast(
            USDollarVI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='USD',
                numeric_code='840',
                symbol='$',
                localized_symbol='VI$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'USDollarVI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollar(Currency):
    """Dollar (Organisation of Eastern Caribbean States (OECS)) currency
    representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollar
        >>> eastern_caribbean_dollar = EasternCaribbeanDollar(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollar':
        """Class creator.

        Returns:
            EasternCaribbeanDollar: new `EasternCaribbeanDollar` object.
        """
        return cast(
            EasternCaribbeanDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarAI(Currency):
    """Dollar (Anguilla) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarAI
        >>> eastern_caribbean_dollar_ai = EasternCaribbeanDollarAI(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_ai)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarAI':
        """Class creator.

        Returns:
            EasternCaribbeanDollarAI: new `EasternCaribbeanDollarAI` object.
        """
        return cast(
            EasternCaribbeanDollarAI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='AI$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarAI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarAG(Currency):
    """Dollar (Antigua and Barbuda) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarAG
        >>> eastern_caribbean_dollar_ag = EasternCaribbeanDollarAG(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_ag)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarAG':
        """Class creator.

        Returns:
            EasternCaribbeanDollarAG: new `EasternCaribbeanDollarAG` object.
        """
        return cast(
            EasternCaribbeanDollarAG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='AG$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarAG':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarDM(Currency):
    """Dollar (Dominica) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarDM
        >>> eastern_caribbean_dollar_dm = EasternCaribbeanDollarDM(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_dm)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarDM':
        """Class creator.

        Returns:
            EasternCaribbeanDollarDM: new `EasternCaribbeanDollarDM` object.
        """
        return cast(
            EasternCaribbeanDollarDM,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='DM$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarDM':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarGD(Currency):
    """Dollar (Grenada) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarGD
        >>> eastern_caribbean_dollar_gd = EasternCaribbeanDollarGD(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_gd)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarGD':
        """Class creator.

        Returns:
            EasternCaribbeanDollarGD: new `EasternCaribbeanDollarGD` object.
        """
        return cast(
            EasternCaribbeanDollarGD,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='GD$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarGD':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarMS(Currency):
    """Dollar (Montserrat) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarMS
        >>> eastern_caribbean_dollar_ms = EasternCaribbeanDollarMS(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_ms)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarMS':
        """Class creator.

        Returns:
            EasternCaribbeanDollarMS: new `EasternCaribbeanDollarMS` object.
        """
        return cast(
            EasternCaribbeanDollarMS,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='MS$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarMS':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarKN(Currency):
    """Dollar (Saint Kitts and Nevis) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarKN
        >>> eastern_caribbean_dollar_kn = EasternCaribbeanDollarKN(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_kn)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarKN':
        """Class creator.

        Returns:
            EasternCaribbeanDollarKN: new `EasternCaribbeanDollarKN` object.
        """
        return cast(
            EasternCaribbeanDollarKN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='KN$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarKN':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarLC(Currency):
    """Dollar (Saint Lucia) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarLC
        >>> eastern_caribbean_dollar_lc = EasternCaribbeanDollarLC(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_lc)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarLC':
        """Class creator.

        Returns:
            EasternCaribbeanDollarLC: new `EasternCaribbeanDollarLC` object.
        """
        return cast(
            EasternCaribbeanDollarLC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='LC$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarLC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EasternCaribbeanDollarVC(Currency):
    """Dollar (Saint Vincent and Grenadine) currency representation.

    Simple usage example:

        >>> from multicurrency import EasternCaribbeanDollarVC
        >>> eastern_caribbean_dollar_vc = EasternCaribbeanDollarVC(
        ...     amount='123456.789')
        >>> print(eastern_caribbean_dollar_vc)
        $123,456.79

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
    ) -> 'EasternCaribbeanDollarVC':
        """Class creator.

        Returns:
            EasternCaribbeanDollarVC: new `EasternCaribbeanDollarVC` object.
        """
        return cast(
            EasternCaribbeanDollarVC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XCD',
                numeric_code='951',
                symbol='$',
                localized_symbol='VC$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EasternCaribbeanDollarVC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class ZimbabweDollar(Currency):
    """Dollar (Zimbabwe) currency representation.

    Simple usage example:

        >>> from multicurrency import ZimbabweDollar
        >>> zimbabwe_dollar = ZimbabweDollar(
        ...     amount='123456.789')
        >>> print(zimbabwe_dollar)
        $ 123,456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.,3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2.,3%s\u00A0%a'
    ) -> 'ZimbabweDollar':
        """Class creator.

        Returns:
            ZimbabweDollar: new `ZimbabweDollar` object.
        """
        return cast(
            ZimbabweDollar,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZWL',
                numeric_code='932',
                symbol='$',
                localized_symbol='ZW$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ZimbabweDollar':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
