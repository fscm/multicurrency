# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Crypto currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class EOS(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import EOS
        >>> eos = EOS(
        ...     amount='123456.789')
        >>> print(eos)
        ε123,456.7890

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '4.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '4.,3%-%s%u'
    ) -> 'EOS':
        """Class creator.

        Returns:
            EOS: new `EOS` object.
        """
        return cast(
            EOS,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EOS',
                numeric_code='0',
                symbol='ε',
                localized_symbol='ε',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EOS':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Ethereum(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Ethereum
        >>> ethereum = Ethereum(
        ...     amount='123456.789')
        >>> print(ethereum)
        Ξ123,456.789000000000000000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '18.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '18.,3%-%s%u'
    ) -> 'Ethereum':
        """Class creator.

        Returns:
            Ethereum: new `Ethereum` object.
        """
        return cast(
            Ethereum,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ETH',
                numeric_code='0',
                symbol='Ξ',
                localized_symbol='Ξ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Ethereum':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Bitcoin(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Bitcoin
        >>> bitcoin = Bitcoin(
        ...     amount='123456.789')
        >>> print(bitcoin)
        ₿123,456.78900000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '8.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '8.,3%-%s%u'
    ) -> 'Bitcoin':
        """Class creator.

        Returns:
            Bitcoin: new `Bitcoin` object.
        """
        return cast(
            Bitcoin,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XBT',
                numeric_code='0',
                symbol='₿',
                localized_symbol='₿',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Bitcoin':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class StellarLumens(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import StellarLumens
        >>> stellar_lumens = StellarLumens(
        ...     amount='123456.789')
        >>> print(stellar_lumens)
        *123,456.7890000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '7.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '7.,3%-%s%u'
    ) -> 'StellarLumens':
        """Class creator.

        Returns:
            StellarLumens: new `StellarLumens` object.
        """
        return cast(
            StellarLumens,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XLM',
                numeric_code='0',
                symbol='*',
                localized_symbol='*',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'StellarLumens':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Monero(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Monero
        >>> monero = Monero(
        ...     amount='123456.789')
        >>> print(monero)
        ɱ123,456.789000000000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '12.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '12.,3%-%s%u'
    ) -> 'Monero':
        """Class creator.

        Returns:
            Monero: new `Monero` object.
        """
        return cast(
            Monero,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XMR',
                numeric_code='0',
                symbol='ɱ',
                localized_symbol='ɱ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Monero':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Ripple(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Ripple
        >>> ripple = Ripple(
        ...     amount='123456.789')
        >>> print(ripple)
        ✕123,456.789000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '6.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '6.,3%-%s%u'
    ) -> 'Ripple':
        """Class creator.

        Returns:
            Ripple: new `Ripple` object.
        """
        return cast(
            Ripple,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XRP',
                numeric_code='0',
                symbol='✕',
                localized_symbol='✕',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Ripple':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Tezos(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Tezos
        >>> tezos = Tezos(
        ...     amount='123456.789')
        >>> print(tezos)
        ꜩ123,456.789000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '6.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '6.,3%-%s%u'
    ) -> 'Tezos':
        """Class creator.

        Returns:
            Tezos: new `Tezos` object.
        """
        return cast(
            Tezos,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XTZ',
                numeric_code='0',
                symbol='ꜩ',
                localized_symbol='ꜩ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Tezos':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class Zcash(Currency):
    """Crypto currency representation.

    Simple usage example:

        >>> from multicurrency import Zcash
        >>> zcash = Zcash(
        ...     amount='123456.789')
        >>> print(zcash)
        ⓩ123,456.78900000

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '8.,3%-%s%u'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '8.,3%-%s%u'
    ) -> 'Zcash':
        """Class creator.

        Returns:
            Zcash: new `Zcash` object.
        """
        return cast(
            Zcash,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='ZEC',
                numeric_code='0',
                symbol='ⓩ',
                localized_symbol='ⓩ',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Zcash':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
