#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# -*- coding: utf-8 -*-
from functools import reduce
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2float(s):
    def fn(x, y):
        return x * 10 + y
    def fuck(x, y):
        return x * 0.1 + y

    def char2num(s):
        return DIGITS[s]

    integer = reduce(fn, map(char2num, s.split('.')[0]))
    little = 0.1 * reduce(fuck, map(char2num, s.split('.')[1][::-1]))
    return integer + little

# 测试:
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
