#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import requests


def return_nothing(nothing_str):
    check_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing_str}'.format(
        nothing_str=nothing_str
    )
    r = requests.get(url=check_url)
    if r.status_code != 200:
        sys.exit()
    ret = r.text
    print(ret)
    if ret == 'Yes. Divide by two and keep going.':
        return int(int(nothing_str) / 2)
    else:
        return int(ret.split('and the next nothing is')[1].strip())


if __name__ == "__main__":
    n = '44827'  # 처음 확인된 nothing 파라미터 값
    try:
        for i in range(400):
            n = return_nothing(n)
            print('{i} 번째'.format(i=i+1))
            print('nothing : {n}'.format(n=n))
    except Exception as err:
        sys.exit()
