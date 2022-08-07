#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


if __name__ == "__main__":
    f = open('text_str.txt', 'r')
    data = f.read()
    f.close()

    # Challenge_1st
    c1 = re.findall('[A-Z]{3}[a-z]{1}[A-Z]{3}', data)
    print(c1)
    c1_1 = re.findall('[a-z]{1}', str(c1))
    print(c1_1)
    print(''.join(c1_1))
    print(set(c1_1))

    # Challenge_2nd
    c2 = re.findall('[a-z][A-Z]{3}[a-z]{1}[A-Z]{3}[a-z]', data)
    print(c2)
    c2_2 = re.findall('[A-Z]{3}[a-z]{1}[A-Z]{3}', str(c2))
    print(c2_2)
    c2_3 = re.findall('[a-z]{1}', str(c2_2))
    print(c2_3)
    print('answer:{answer}'.format(answer=''.join(c2_3)))
