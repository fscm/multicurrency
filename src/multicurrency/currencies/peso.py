# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Peso currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class ArgentinePeso(Currency):
    """Peso (Argentina) currency representation.

    Simple usage example:

        >>> from multicurrency import ArgentinePeso
        >>> argentine_peso = ArgentinePeso(
        ...     amount='123456.789')
        >>> print(argentine_peso)
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
    ) -> 'ArgentinePeso':
        """Class creator.

        Returns:
            ArgentinePeso: new `ArgentinePeso` object.
        """
        return cast(
            ArgentinePeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ARS',
                numeric_code='032',
                symbol='$',
                localized_symbol='AR$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ArgentinePeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class ChileanPeso(Currency):
    """Peso (Chile) currency representation.

    Simple usage example:

        >>> from multicurrency import ChileanPeso
        >>> chilean_peso = ChileanPeso(
        ...     amount='123456.789')
        >>> print(chilean_peso)
        $123.457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '0,.3%-%s%u'
    ) -> 'ChileanPeso':
        """Class creator.

        Returns:
            ChileanPeso: new `ChileanPeso` object.
        """
        return cast(
            ChileanPeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CLP',
                numeric_code='152',
                symbol='$',
                localized_symbol='CL$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ChileanPeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class ColombianPeso(Currency):
    """Peso (Colombia) currency representation.

    Simple usage example:

        >>> from multicurrency import ColombianPeso
        >>> colombian_peso = ColombianPeso(
        ...     amount='123456.789')
        >>> print(colombian_peso)
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
    ) -> 'ColombianPeso':
        """Class creator.

        Returns:
            ColombianPeso: new `ColombianPeso` object.
        """
        return cast(
            ColombianPeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='COP',
                numeric_code='170',
                symbol='$',
                localized_symbol='CO$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'ColombianPeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CubanPeso(Currency):
    """Peso (Cuba) currency representation.

    Simple usage example:

        >>> from multicurrency import CubanPeso
        >>> cuban_peso = CubanPeso(
        ...     amount='123456.789')
        >>> print(cuban_peso)
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
    ) -> 'CubanPeso':
        """Class creator.

        Returns:
            CubanPeso: new `CubanPeso` object.
        """
        return cast(
            CubanPeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CUP',
                numeric_code='192',
                symbol='$',
                localized_symbol='CU$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'CubanPeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class DominicanPeso(Currency):
    """Peso (Dominican Republic) currency representation.

    Simple usage example:

        >>> from multicurrency import DominicanPeso
        >>> dominican_peso = DominicanPeso(
        ...     amount='123456.789')
        >>> print(dominican_peso)
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
    ) -> 'DominicanPeso':
        """Class creator.

        Returns:
            DominicanPeso: new `DominicanPeso` object.
        """
        return cast(
            DominicanPeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='DOP',
                numeric_code='214',
                symbol='$',
                localized_symbol='DO$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'DominicanPeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class MexicanPeso(Currency):
    """Peso (Mexico) currency representation.

    Simple usage example:

        >>> from multicurrency import MexicanPeso
        >>> mexican_peso = MexicanPeso(
        ...     amount='123456.789')
        >>> print(mexican_peso)
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
    ) -> 'MexicanPeso':
        """Class creator.

        Returns:
            MexicanPeso: new `MexicanPeso` object.
        """
        return cast(
            MexicanPeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='MXN',
                numeric_code='484',
                symbol='$',
                localized_symbol='MX$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'MexicanPeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PhilippinePeso(Currency):
    """Peso (Philippines) currency representation.

    Simple usage example:

        >>> from multicurrency import PhilippinePeso
        >>> philippine_peso = PhilippinePeso(
        ...     amount='123456.789')
        >>> print(philippine_peso)
        ₱123,456.79

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
    ) -> 'PhilippinePeso':
        """Class creator.

        Returns:
            PhilippinePeso: new `PhilippinePeso` object.
        """
        return cast(
            PhilippinePeso,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='PHP',
                numeric_code='608',
                symbol='₱',
                localized_symbol='₱',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PhilippinePeso':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class PesoUruguayo(Currency):
    """Peso (Uruguay) currency representation.

    Simple usage example:

        >>> from multicurrency import PesoUruguayo
        >>> peso_uruguayo = PesoUruguayo(
        ...     amount='123456.789')
        >>> print(peso_uruguayo)
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
    ) -> 'PesoUruguayo':
        """Class creator.

        Returns:
            PesoUruguayo: new `PesoUruguayo` object.
        """
        return cast(
            PesoUruguayo,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='UYU',
                numeric_code='858',
                symbol='$',
                localized_symbol='UY$',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'PesoUruguayo':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
