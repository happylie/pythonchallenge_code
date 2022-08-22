#!/usr/bin/python
# -*- coding: utf-8 -*-
import zipfile

z = zipfile.ZipFile('channel.zip', 'r')
n = '90052'  # 처음 확인된 nothing 파라미터 값
result = ''
while True:
    file_path = '{nothing}.txt'.format(nothing=n)
    data = z.read(file_path).decode('utf-8')
    print(data)
    result += z.getinfo(file_path).comment.decode('utf-8')
    if data.split('Next nothing is'):
        try:
            n = data.split('Next nothing is')[1].strip()
        except IndexError as err:
            break
    else:
        break
print(result)
