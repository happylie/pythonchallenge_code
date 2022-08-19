#!/usr/bin/python
# -*- coding: utf-8 -*-
import pickle

with open('banner.p', 'rb') as f:
    data = pickle.load(f)
    line = 0

for row in data:
    line = line + 1
    ret = ""
    for r in row:
        ret += r[0] * r[1]
    print("{line}행: {ret}".format(line=line, ret=ret))

