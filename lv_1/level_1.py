#!/usr/bin/python
# -*- coding: utf-8 -*-

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# change_alphabet = "cdefghijklmnopqrstuvwxyzab"
# Step 2
# K -> M : 2
# O -> Q : 2
# E -> G : 2


def ascii_to_char(origin_text):
    result = ""
    for i in origin_text:
        if i == " " or i == "." or i == "'" or i == "(" or i == ")":
            result += i
        else:
            if ord(i) + 2 == 123:
                result += chr(97)
            elif ord(i) + 2 == 124:
                result += chr(98)
            else:
                result += chr(ord(i) + 2)
    return result


def answer(origin_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    change_alphabet = "cdefghijklmnopqrstuvwxyzab"
    trans_text = origin_text.maketrans(alphabet, change_alphabet)
    result = origin_text.translate(trans_text)
    return result


if __name__ == "__main__":
    text_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    html_str = "map.html"
    uri_str = "map"
    print(ascii_to_char(html_str))
    print(answer(uri_str))
