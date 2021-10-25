#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# copyright: 2020-2021, Frederico Martins
# author: Frederico Martins <http://github.com/fscm>
# license: SPDX-License-Identifier: MIT

import csv
import os

CSV_FILE = 'currency.csv'
workfolder = os.getcwd()

with open(f'{workfolder}/{CSV_FILE}', 'r') as csv_file:
    new_content = []
    csv_reader = csv.reader(csv_file, delimiter=',')
    headers = next(csv_reader, None)
    headers.insert(2, 'Localized Symbol')
    new_content.append(headers)
    for record in csv_reader:
        if len(record) == 0:
            new_content.append(record)
        else:
            record.insert(2, record[1])
            new_content.append(record)

with open(f'{workfolder}/new_{CSV_FILE}', 'w') as new_csv_file:
    csv_writer = csv.writer(new_csv_file, quoting=csv.QUOTE_ALL, lineterminator='\n')
    csv_writer.writerows(new_content)
