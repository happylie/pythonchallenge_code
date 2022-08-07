#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    f = open('text_str.txt', 'r')
    re_special_char = f.read()
    new_str = ''.join(filter(str.isalpha, re_special_char))
    print(new_str)
    f.close()
