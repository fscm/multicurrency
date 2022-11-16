# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Euro currency representation(s)."""

from decimal import Decimal
from typing import Optional, Union, cast
from multicurrency.pycurrency import Currency


class Euro(Currency):
    """Euro currency representation.

    Simple usage example:

        >>> from multicurrency import Euro
        >>> euro = Euro(
        ...     amount='123456.789')
        >>> print(euro)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'Euro':
        """Class creator.

        Returns:
            Euro: new `Euro` object.
        """
        return cast(
            Euro,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'Euro':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroSBA(Currency):
    """Euro (Akrotiri and Dhekelia) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroSBA
        >>> eurosba = EuroSBA(
        ...     amount='123456.789')
        >>> print(eurosba)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroSBA':
        """Class creator.

        Returns:
            EuroSBA: new `EuroSBA` object.
        """
        return cast(
            EuroSBA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroSBA':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroAD(Currency):
    """Euro (Andorra) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroAD
        >>> euroad = EuroAD(
        ...     amount='123456.789')
        >>> print(euroad)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroAD':
        """Class creator.

        Returns:
            EuroAD: new `EuroAD` object.
        """
        return cast(
            EuroAD,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='AD€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroAD':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroAT(Currency):
    """Euro (Austria) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroAT
        >>> euroat = EuroAT(
        ...     amount='123456.789')
        >>> print(euroat)
        € 123.456,79

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
    ) -> 'EuroAT':
        """Class creator.

        Returns:
            EuroAT: new `EuroAT` object.
        """
        return cast(
            EuroAT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='AT€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroAT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroBE(Currency):
    """Euro (Belgium) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroBE
        >>> eurobe = EuroBE(
        ...     amount='123456.789')
        >>> print(eurobe)
        € 123.456,79

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
    ) -> 'EuroBE':
        """Class creator.

        Returns:
            EuroBE: new `EuroBE` object.
        """
        return cast(
            EuroBE,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='BE€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroBE':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroCY(Currency):
    """Euro (Cyprus) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroCY
        >>> eurocy = EuroCY(
        ...     amount='123456.789')
        >>> print(eurocy)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroCY':
        """Class creator.

        Returns:
            EuroCY: new `EuroCY` object.
        """
        return cast(
            EuroCY,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='CY€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroCY':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroEE(Currency):
    """Euro (Estonia) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroEE
        >>> euroee = EuroEE(
        ...     amount='123456.789')
        >>> print(euroee)
        123 456,79 €

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
    ) -> 'EuroEE':
        """Class creator.

        Returns:
            EuroEE: new `EuroEE` object.
        """
        return cast(
            EuroEE,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='EE€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroEE':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroFI(Currency):
    """Euro (Finland) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroFI
        >>> eurofi = EuroFI(
        ...     amount='123456.789')
        >>> print(eurofi)
        123 456,79 €

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
    ) -> 'EuroFI':
        """Class creator.

        Returns:
            EuroFI: new `EuroFI` object.
        """
        return cast(
            EuroFI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='FI€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroFI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroFR(Currency):
    """Euro (France) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroFR
        >>> eurofr = EuroFR(
        ...     amount='123456.789')
        >>> print(eurofr)
        123 456,79 €

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
    ) -> 'EuroFR':
        """Class creator.

        Returns:
            EuroFR: new `EuroFR` object.
        """
        return cast(
            EuroFR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='FR€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroFR':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroDE(Currency):
    """Euro (Germany) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroDE
        >>> eurode = EuroDE(
        ...     amount='123456.789')
        >>> print(eurode)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroDE':
        """Class creator.

        Returns:
            EuroDE: new `EuroDE` object.
        """
        return cast(
            EuroDE,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='DE€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroDE':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroGR(Currency):
    """Euro (Greece) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroGR
        >>> eurogr = EuroGR(
        ...     amount='123456.789')
        >>> print(eurogr)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroGR':
        """Class creator.

        Returns:
            EuroGR: new `EuroGR` object.
        """
        return cast(
            EuroGR,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='GR€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroGR':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroIE(Currency):
    """Euro (Ireland) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroIE
        >>> euroie = EuroIE(
        ...     amount='123456.789')
        >>> print(euroie)
        €123,456.79

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
    ) -> 'EuroIE':
        """Class creator.

        Returns:
            EuroIE: new `EuroIE` object.
        """
        return cast(
            EuroIE,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='IR€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroIE':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroIT(Currency):
    """Euro (Italy) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroIT
        >>> euroit = EuroIT(
        ...     amount='123456.789')
        >>> print(euroit)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroIT':
        """Class creator.

        Returns:
            EuroIT: new `EuroIT` object.
        """
        return cast(
            EuroIT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='IT€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroIT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroXK(Currency):
    """Euro (Kosovo) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroXK
        >>> euroxk = EuroXK(
        ...     amount='123456.789')
        >>> print(euroxk)
        123 456,79 €

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
    ) -> 'EuroXK':
        """Class creator.

        Returns:
            EuroXK: new `EuroXK` object.
        """
        return cast(
            EuroXK,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='XK€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroXK':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroLV(Currency):
    """Euro (Latvia) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroLV
        >>> eurolv = EuroLV(
        ...     amount='123456.789')
        >>> print(eurolv)
        123 456,79 €

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
    ) -> 'EuroLV':
        """Class creator.

        Returns:
            EuroLV: new `EuroLV` object.
        """
        return cast(
            EuroLV,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='LV€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroLV':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroLT(Currency):
    """Euro (Lithuania) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroLT
        >>> eurolt = EuroLT(
        ...     amount='123456.789')
        >>> print(eurolt)
        123 456,79 €

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
    ) -> 'EuroLT':
        """Class creator.

        Returns:
            EuroLT: new `EuroLT` object.
        """
        return cast(
            EuroLT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='LT€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroLT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroLU(Currency):
    """Euro (Luxembourg) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroLU
        >>> eurolu = EuroLU(
        ...     amount='123456.789')
        >>> print(eurolu)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroLU':
        """Class creator.

        Returns:
            EuroLU: new `EuroLU` object.
        """
        return cast(
            EuroLU,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='LU€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroLU':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroMT(Currency):
    """Euro (Malta) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroMT
        >>> euromt = EuroMT(
        ...     amount='123456.789')
        >>> print(euromt)
        €123,456.79

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
    ) -> 'EuroMT':
        """Class creator.

        Returns:
            EuroMT: new `EuroMT` object.
        """
        return cast(
            EuroMT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='MT€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroMT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroMC(Currency):
    """Euro (Monaco) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroMC
        >>> euromc = EuroMC(
        ...     amount='123456.789')
        >>> print(euromc)
        123 456,79 €

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
    ) -> 'EuroMC':
        """Class creator.

        Returns:
            EuroMC: new `EuroMC` object.
        """
        return cast(
            EuroMC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='MC€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroMC':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroME(Currency):
    """Euro (Montenegro) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroME
        >>> eurome = EuroME(
        ...     amount='123456.789')
        >>> print(eurome)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroME':
        """Class creator.

        Returns:
            EuroME: new `EuroME` object.
        """
        return cast(
            EuroME,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='ME€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroME':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroNL(Currency):
    """Euro (Netherlands) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroNL
        >>> euronl = EuroNL(
        ...     amount='123456.789')
        >>> print(euronl)
        € 123.456,79

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
    ) -> 'EuroNL':
        """Class creator.

        Returns:
            EuroNL: new `EuroNL` object.
        """
        return cast(
            EuroNL,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='NL€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroNL':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroPT(Currency):
    """Euro (Portugal) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroPT
        >>> europt = EuroPT(
        ...     amount='123456.789')
        >>> print(europt)
        € 123.456,79

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
    ) -> 'EuroPT':
        """Class creator.

        Returns:
            EuroPT: new `EuroPT` object.
        """
        return cast(
            EuroPT,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='PT€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroPT':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroSM(Currency):
    """Euro (San-Marino) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroSM
        >>> eurosm = EuroSM(
        ...     amount='123456.789')
        >>> print(eurosm)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroSM':
        """Class creator.

        Returns:
            EuroSM: new `EuroSM` object.
        """
        return cast(
            EuroSM,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='SM€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroSM':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroSK(Currency):
    """Euro (Slovakia) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroSK
        >>> eurosk = EuroSK(
        ...     amount='123456.789')
        >>> print(eurosk)
        123 456,79 €

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
    ) -> 'EuroSK':
        """Class creator.

        Returns:
            EuroSK: new `EuroSK` object.
        """
        return cast(
            EuroSK,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='SK€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroSK':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroSI(Currency):
    """Euro (Slovenia) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroSI
        >>> eurosi = EuroSI(
        ...     amount='123456.789')
        >>> print(eurosi)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroSI':
        """Class creator.

        Returns:
            EuroSI: new `EuroSI` object.
        """
        return cast(
            EuroSI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='SI€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroSI':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroES(Currency):
    """Euro (Spain) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroES
        >>> euroes = EuroES(
        ...     amount='123456.789')
        >>> print(euroes)
        123.456,79 €

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (Union[str, int, float, Decimal]): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2,.3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls,
        amount: Union[str, int, float, Decimal],
        pattern: Optional[str] = '2,.3%a\u00A0%s'
    ) -> 'EuroES':
        """Class creator.

        Returns:
            EuroES: new `EuroES` object.
        """
        return cast(
            EuroES,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='ES€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroES':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])


class EuroVA(Currency):
    """Euro (Vatican) currency representation.

    Simple usage example:

        >>> from multicurrency import EuroVA
        >>> eurova = EuroVA(
        ...     amount='123456.789')
        >>> print(eurova)
        €123,456.79

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
    ) -> 'EuroVA':
        """Class creator.

        Returns:
            EuroVA: new `EuroVA` object.
        """
        return cast(
            EuroVA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='EUR',
                numeric_code='978',
                symbol='€',
                localized_symbol='VA€',
                convertion='',
                pattern=pattern))

    def __recreate__(
            self,
            amount: Union[str, int, float, Decimal]
    ) -> 'EuroVA':
        """Recreates self with a different `amount`.

        Args:
            amount (Union[str, int, float, Decimal]): Represented value.

        Returns:
            Currency: new opbject.
        """
        return self.__class__(amount, self._info[5])
