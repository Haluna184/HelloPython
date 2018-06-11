#!/usr/bin/env python
# -*- coding: utf-8 -*-

fname = 'README.md'

idkey = '## 学籍番号:'
namekey = '## 名前:'
mailkey = '## e-mail:'

res = {}
with open(fname, 'r') as f:
    for row in f:
        if idkey in row:
            res['id'] = row.split(':')[1].strip()
        if namekey in row:
            res['name'] = row.split(':')[1].strip()
        if mailkey in row:
            res['mail'] = row.split(':')[1].strip()

for key in ['id', 'name', 'mail']:
    print(res[key])



