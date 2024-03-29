# -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

"""Franc currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal


class BurundiFranc(Currency):
    """Franc (Burundi) currency representation.

    Simple usage example:

        >>> from multicurrency import BurundiFranc
        >>> burundi_franc = BurundiFranc(
        ...     amount='123456.789')
        >>> print(burundi_franc)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            BurundiFranc: new `BurundiFranc` object.
        """
        return cast(
            BurundiFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='BIF',
                numeric_code='108',
                symbol='₣',
                localized_symbol='BI₣',
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
            BurundiFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CongoleseFranc(Currency):
    """Franc (Congo (Kinshasa)) currency representation.

    Simple usage example:

        >>> from multicurrency import CongoleseFranc
        >>> congolese_franc = CongoleseFranc(
        ...     amount='123456.789')
        >>> print(congolese_franc)
        123 456,79 ₣

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
            CongoleseFranc: new `CongoleseFranc` object.
        """
        return cast(
            CongoleseFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CDF',
                numeric_code='976',
                symbol='₣',
                localized_symbol='CD₣',
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
            CongoleseFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SwissFranc(Currency):
    """Franc (Switzerland) currency representation.

    Simple usage example:

        >>> from multicurrency import SwissFranc
        >>> swiss_franc = SwissFranc(
        ...     amount='123456.789')
        >>> print(swiss_franc)
        ₣ 123'456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.'3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u00273%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            SwissFranc: new `SwissFranc` object.
        """
        return cast(
            SwissFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CHF',
                numeric_code='756',
                symbol='₣',
                localized_symbol='₣',
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
            SwissFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SwissFrancLI(Currency):
    """Franc (Liechtenstein) currency representation.

    Simple usage example:

        >>> from multicurrency import SwissFrancLI
        >>> swiss_franc_li = SwissFrancLI(
        ...     amount='123456.789')
        >>> print(swiss_franc_li)
        ₣ 123'456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.'3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u00273%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            SwissFrancLI: new `SwissFrancLI` object.
        """
        return cast(
            SwissFrancLI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CHF',
                numeric_code='756',
                symbol='₣',
                localized_symbol='LI₣',
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
            SwissFrancLI: new opbject.
        """
        return self.__class__(amount, self._info[5])


class SwissFrancCH(Currency):
    """Franc (Switzerland) currency representation.

    Simple usage example:

        >>> from multicurrency import SwissFrancCH
        >>> swiss_franc_ch = SwissFrancCH(
        ...     amount='123456.789')
        >>> print(swiss_franc_ch)
        ₣ 123'456.79

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '2.'3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '2.\u00273%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            SwissFrancCH: new `SwissFrancCH` object.
        """
        return cast(
            SwissFrancCH,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='CHF',
                numeric_code='756',
                symbol='₣',
                localized_symbol='CH₣',
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
            SwissFrancCH: new opbject.
        """
        return self.__class__(amount, self._info[5])


class DjiboutiFranc(Currency):
    """Franc (Djibouti) currency representation.

    Simple usage example:

        >>> from multicurrency import DjiboutiFranc
        >>> djibouti_franc = DjiboutiFranc(
        ...     amount='123456.789')
        >>> print(djibouti_franc)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            DjiboutiFranc: new `DjiboutiFranc` object.
        """
        return cast(
            DjiboutiFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='DJF',
                numeric_code='262',
                symbol='₣',
                localized_symbol='DJ₣',
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
            DjiboutiFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class GuineaFranc(Currency):
    """Franc (Guinea) currency representation.

    Simple usage example:

        >>> from multicurrency import GuineaFranc
        >>> guinea_franc = GuineaFranc(
        ...     amount='123456.789')
        >>> print(guinea_franc)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            GuineaFranc: new `GuineaFranc` object.
        """
        return cast(
            GuineaFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='GNF',
                numeric_code='324',
                symbol='₣',
                localized_symbol='GN₣',
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
            GuineaFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class RwandaFranc(Currency):
    """Franc (Rwanda) currency representation.

    Simple usage example:

        >>> from multicurrency import RwandaFranc
        >>> rwanda_franc = RwandaFranc(
        ...     amount='123456.789')
        >>> print(rwanda_franc)
        ₣ 123.457

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0,.3%s %a'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,.3%s\u00A0%a',
    ) -> Self:
        """Class creator.

        Returns:
            RwandaFranc: new `RwandaFranc` object.
        """
        return cast(
            RwandaFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='RWF',
                numeric_code='646',
                symbol='₣',
                localized_symbol='RW₣',
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
            RwandaFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEAC(Currency):
    """Franc (Cameroon) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEAC
        >>> cfa_franc_beac = CFAFrancBEAC(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEAC: new `CFAFrancBEAC` object.
        """
        return cast(
            CFAFrancBEAC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='₣',
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
            CFAFrancBEAC: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACCM(Currency):
    """Franc (Cameroon) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACCM
        >>> cfa_franc_beac_cm = CFAFrancBEACCM(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_cm)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACCM: new `CFAFrancBEACCM` object.
        """
        return cast(
            CFAFrancBEACCM,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='CM₣',
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
            CFAFrancBEACCM: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACCF(Currency):
    """Franc (Central African Republic) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACCF
        >>> cfa_franc_beac_cf = CFAFrancBEACCF(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_cf)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACCF: new `CFAFrancBEACCF` object.
        """
        return cast(
            CFAFrancBEACCF,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='CF₣',
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
            CFAFrancBEACCF: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACTD(Currency):
    """Franc (Chad) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACTD
        >>> cfa_franc_beac_td = CFAFrancBEACTD(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_td)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACTD: new `CFAFrancBEACTD` object.
        """
        return cast(
            CFAFrancBEACTD,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='TD₣',
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
            CFAFrancBEACTD: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACCD(Currency):
    """Franc (Congo (Brazzaville)) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACCD
        >>> cfa_franc_beac_cd = CFAFrancBEACCD(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_cd)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACCD: new `CFAFrancBEACCD` object.
        """
        return cast(
            CFAFrancBEACCD,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='CD₣',
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
            CFAFrancBEACCD: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACGQ(Currency):
    """Franc (Equatorial Guinea) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACGQ
        >>> cfa_franc_beac_gq = CFAFrancBEACGQ(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_gq)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACGQ: new `CFAFrancBEACGQ` object.
        """
        return cast(
            CFAFrancBEACGQ,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='GQ₣',
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
            CFAFrancBEACGQ: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBEACGA(Currency):
    """Franc (Gabon) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBEACGA
        >>> cfa_franc_beac_ga = CFAFrancBEACGA(
        ...     amount='123456.789')
        >>> print(cfa_franc_beac_ga)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBEACGA: new `CFAFrancBEACGA` object.
        """
        return cast(
            CFAFrancBEACGA,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XAF',
                numeric_code='950',
                symbol='₣',
                localized_symbol='GA₣',
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
            CFAFrancBEACGA: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAO(Currency):
    """Franc (Senegal) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAO
        >>> cfa_franc_bceao = CFAFrancBCEAO(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAO: new `CFAFrancBCEAO` object.
        """
        return cast(
            CFAFrancBCEAO,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='₣',
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
            CFAFrancBCEAO: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOBJ(Currency):
    """Franc (Benin) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOBJ
        >>> cfa_franc_bceao_bj = CFAFrancBCEAOBJ(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_bj)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOBJ: new `CFAFrancBCEAOBJ` object.
        """
        return cast(
            CFAFrancBCEAOBJ,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='BJ₣',
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
            CFAFrancBCEAOBJ: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOBF(Currency):
    """Franc (Burkina Faso) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOBF
        >>> cfa_franc_bceao_bf = CFAFrancBCEAOBF(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_bf)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOBF: new `CFAFrancBCEAOBF` object.
        """
        return cast(
            CFAFrancBCEAOBF,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='BF₣',
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
            CFAFrancBCEAOBF: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOCI(Currency):
    """Franc (Côte d'Ivoire) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOCI
        >>> cfa_franc_bceao_ci = CFAFrancBCEAOCI(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_ci)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOCI: new `CFAFrancBCEAOCI` object.
        """
        return cast(
            CFAFrancBCEAOCI,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='CI₣',
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
            CFAFrancBCEAOCI: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOGW(Currency):
    """Franc (Guinea-Bissau) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOGW
        >>> cfa_franc_bceao_gw = CFAFrancBCEAOGW(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_gw)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOGW: new `CFAFrancBCEAOGW` object.
        """
        return cast(
            CFAFrancBCEAOGW,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='GW₣',
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
            CFAFrancBCEAOGW: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOML(Currency):
    """Franc (Mali) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOML
        >>> cfa_franc_bceao_ml = CFAFrancBCEAOML(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_ml)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOML: new `CFAFrancBCEAOML` object.
        """
        return cast(
            CFAFrancBCEAOML,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='ML₣',
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
            CFAFrancBCEAOML: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAONG(Currency):
    """Franc (Niger) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAONG
        >>> cfa_franc_bceao_ng = CFAFrancBCEAONG(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_ng)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAONG: new `CFAFrancBCEAONG` object.
        """
        return cast(
            CFAFrancBCEAONG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='NG₣',
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
            CFAFrancBCEAONG: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOSN(Currency):
    """Franc (Senegal) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOSN
        >>> cfa_franc_bceao_sn = CFAFrancBCEAOSN(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_sn)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOSN: new `CFAFrancBCEAOSN` object.
        """
        return cast(
            CFAFrancBCEAOSN,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='SN₣',
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
            CFAFrancBCEAOSN: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFAFrancBCEAOTG(Currency):
    """Franc (Togo) currency representation.

    Simple usage example:

        >>> from multicurrency import CFAFrancBCEAOTG
        >>> cfa_franc_bceao_tg = CFAFrancBCEAOTG(
        ...     amount='123456.789')
        >>> print(cfa_franc_bceao_tg)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFAFrancBCEAOTG: new `CFAFrancBCEAOTG` object.
        """
        return cast(
            CFAFrancBCEAOTG,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XOF',
                numeric_code='952',
                symbol='₣',
                localized_symbol='TG₣',
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
            CFAFrancBCEAOTG: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFPFranc(Currency):
    """Franc (French Polynesia) currency representation.

    Simple usage example:

        >>> from multicurrency import CFPFranc
        >>> cfp_franc = CFPFranc(
        ...     amount='123456.789')
        >>> print(cfp_franc)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFPFranc: new `CFPFranc` object.
        """
        return cast(
            CFPFranc,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XPF',
                numeric_code='953',
                symbol='₣',
                localized_symbol='₣',
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
            CFPFranc: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFPFrancPF(Currency):
    """Franc (French Polynesia) currency representation.

    Simple usage example:

        >>> from multicurrency import CFPFrancPF
        >>> cfp_franc_pf = CFPFrancPF(
        ...     amount='123456.789')
        >>> print(cfp_franc_pf)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFPFrancPF: new `CFPFrancPF` object.
        """
        return cast(
            CFPFrancPF,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XPF',
                numeric_code='953',
                symbol='₣',
                localized_symbol='PF₣',
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
            CFPFrancPF: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFPFrancNC(Currency):
    """Franc (New Caledonia) currency representation.

    Simple usage example:

        >>> from multicurrency import CFPFrancNC
        >>> cfp_franc_nc = CFPFrancNC(
        ...     amount='123456.789')
        >>> print(cfp_franc_nc)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFPFrancNC: new `CFPFrancNC` object.
        """
        return cast(
            CFPFrancNC,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XPF',
                numeric_code='953',
                symbol='₣',
                localized_symbol='NC₣',
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
            CFPFrancNC: new opbject.
        """
        return self.__class__(amount, self._info[5])


class CFPFrancWF(Currency):
    """Franc (Wallis and Futuna) currency representation.

    Simple usage example:

        >>> from multicurrency import CFPFrancWF
        >>> cfp_franc_wf = CFPFrancWF(
        ...     amount='123456.789')
        >>> print(cfp_franc_wf)
        123 457 ₣

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '0, 3%a %s'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '0,\u202F3%a\u00A0%s',
    ) -> Self:
        """Class creator.

        Returns:
            CFPFrancWF: new `CFPFrancWF` object.
        """
        return cast(
            CFPFrancWF,
            super().__new__(
                cls,
                amount=amount,
                alpha_code='XPF',
                numeric_code='953',
                symbol='₣',
                localized_symbol='WF₣',
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
            CFPFrancWF: new opbject.
        """
        return self.__class__(amount, self._info[5])
