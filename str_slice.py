#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#对字符串首尾空格切片（递归）

def trim(s):
    if s[:1] == ' ':
        return trim(s[1:])
    if s[-1:] == ' ':
        return trim(s[:-1])
    return s
