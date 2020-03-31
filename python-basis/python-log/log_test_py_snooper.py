#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: log_test_py_snooper.py
# @Time    : 2020/3/28 13:07
"""
"""
学习类库,
pysnooper的使用, 介绍：https://zhuanlan.zhihu.com/p/67457275

"""

import pysnooper

list1 = ['physics', 'chemistry', 1997, 2000, 5555]


@pysnooper.snoop(depth=3)
def test_print():
    print("1")


for list_test in list1[1:4]:
    print(list_test)
    test_print()
