<%text># -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT</%text>
<%! from textwrap import wrap %>
"""${module_name} currency representation(s)."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self, cast

from multicurrency.pycurrency import Currency


if TYPE_CHECKING:
    from decimal import Decimal
% for currency in currencies:


class ${currency.class_name}(Currency):
    """<%
_country_ = f'({currency.country}) ' if currency.country else ''
_docstring_start_ = (
    f'{currency.main_class} '
    f'{_country_}'
    'currency representation.')
_lines_ = wrap(_docstring_start_, width=69, initial_indent='', subsequent_indent='    ')
docstring_start = '\n'.join(_lines_)
    %>${docstring_start}

    Simple usage example:

        >>> from multicurrency import ${currency.class_name}
        >>> ${currency.example.variable} = ${currency.class_name}(
        ...     amount='${currency.example.value}')
        >>> print(${currency.example.variable})
        ${currency.example.output}

    For more details see `multicurrency.pycurrency.Currency`.

    Args:
        amount (str | int | float | Decimal): Represented value.
        pattern (str, optional): Currency format pattern. Defaults to
            '<% _pattern_ = bytes(currency.pattern, 'utf-8').decode('unicode_escape') %>${_pattern_}'.
    """

    __slots__ = ()

    def __new__(  # pylint: disable=signature-differs
        cls: Self,
        amount: str | float | Decimal,
        pattern: str | None = '${currency.pattern}',
    ) -> Self:
        """Class creator.

        Returns:
            ${currency.class_name}: new `${currency.class_name}` object.
        """
        return cast(
            ${currency.class_name},
            super().__new__(
                cls,
                amount=amount,
                alpha_code='${currency.alpha_code}',
                numeric_code='${currency.numeric_code}',
                symbol='${currency.symbol}',
                localized_symbol='${currency.localized_symbol}',
                convertion='${currency.convertion}',
                pattern=pattern))

    def __recreate__(
            self: Self,
            amount: str | float | Decimal,
    ) -> Self:
        """Recreates self with a different `amount`.

        Args:
            amount (str | int | float | Decimal): Represented value.

        Returns:
            ${currency.class_name}: new opbject.
        """
        return self.__class__(amount, self._info[5])
% endfor
