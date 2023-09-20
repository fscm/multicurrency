<%text># -*- coding: UTF-8 -*-
#
# copyright: 2020-2022, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT</%text>
<%! from tabulate import tabulate %>
"""Currencies.

The Currencies module provides the implementation of the several existing
currencies as extensions of `multicurrency.pycurrency.Currency`. It supports
several different currencies.

The currencies supported by this module were created with information
(alphabetic code, numeric code, and minor unit size) from ISO-4217.

.. note::
    Cryptocurrencies are not represented in the ISO-4217. Information on
    cryptocurrencies was collected on other sources.

<%text>## Supported Currencies</%text>

Table of supported currencies:

<%
    _currencies_ = []
    _cryptocurrencies_ = []
    for module, info in sorted(currencies.items()):
        if module == 'crypto':
             _cryptocurrencies_.extend([
            (c.class_name, (f'`multicurrency.currencies.{module}.{c.class_name}`', c.example.output, c.example.docstring[0], c.example.docstring[1]))
            for c in info['currencies']])
        else:
            _currencies_.extend([
            (c.class_name, (f'`multicurrency.currencies.{module}.{c.class_name}`', c.country, c.example.output, c.example.docstring[0], c.example.docstring[1]))
            for c in info['currencies']])
    table_currencies = tabulate(
        [c[1] for c in sorted(_currencies_)],
        headers=['Currency', 'Country', 'Default', 'Localized', 'International'],
        tablefmt="pipe",
        colalign=('left', 'left', 'right', 'right', 'right'))
    table_cryptocurrencies = tabulate(
        [c[1] for c in sorted(_cryptocurrencies_)],
        headers=['Cryptocurrency', 'Default', 'Localized', 'International'],
        tablefmt="pipe",
        colalign=('left', 'right', 'right', 'right'))
%>${table_currencies}

<%text>## Supported Cryptocurrencies</%text>

Table of supported cryptocurrencies:

${table_cryptocurrencies}
""" # pylint: disable=line-too-long  # noqa: E501,W505

% for module, info in sorted(currencies.items()):
from multicurrency.currencies.${module} import <%
    classes = [c.class_name for c in info['currencies']]
    if len(classes) > 1:
        _classes_ = "(\n    " + ",\n    ".join(sorted(classes)) + ",\n)"
    else:
        _classes_ = classes[0]
%>${_classes_}
% endfor
<%
    all_list = []
    for info in currencies.values():
        for currency in info['currencies']:
            all_list.append(currency.class_name)
    _all_list_ = "'" + "',\n    '".join(sorted(all_list)) + "'"
%>

__all__ = (
    ${_all_list_})
