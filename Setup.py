#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: Setup.py.py
# @Time    : 2020/3/28 13:50
"""
import os
os.system('pip install pipreqs')
os.system('pipreqs --force ./')
os.system('pip install -r requirements.txt')
