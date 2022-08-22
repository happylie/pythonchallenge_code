#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys


def get_file_read(file_path):
    file_path = '{dir_path}/{file_path}.txt'.format(dir_path=dir_path, file_path=file_path)
    with open(file_path, 'r') as f:
        for line in f:
            try:
                ret = line.split('Next nothing is')
                print(ret)
                return ret[1].strip()
            except IndexError:
                break


if __name__ == "__main__":
    n = '90052'  # 처음 확인된 nothing 파라미터 값
    dir_path = 'channel'
    dir_len = len(os.listdir(dir_path))
    try:
        for i in range(dir_len):
            n = get_file_read(n)
            print('{i} 번째'.format(i=i+2))
            print('nothing : {n}'.format(n=n))
            if not n:
                sys.exit()
    except Exception as err:
        sys.exit()
