#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)#a 上只有 1 个盘子
    else:#a 上有 2 个盘子
        move(n-1,a,c,b)# 把 a 上的 n-1 块移动到 b
        move(1,a,b,c)# 把 a 上的最后一块移动到 c
        move(n-1,b,a,c)# 把 b 上的 n-1 块移动到 c
