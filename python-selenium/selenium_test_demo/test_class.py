#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: test_class.py
# @Time    : 2020/2/27 20:10
"""
import pytest

class TestClass(object):

    def test_class(self, env):
        if env == "1":
            print("数据传入正常 %s " % env)
            assert 1
        else:
            print("数据不正常 %s " % env)
            with pytest.raises(RuntimeError) as excinfo:

                def f():
                    f()

                f()
            assert "maximum recursion" in str(excinfo.value)


    def test_browser(self, browser):
        if browser == "1":
            print("浏览器数据正常 %s " % browser)
            assert 1

        elif browser == "2":
            print("浏览器数据为 %s" % browser ,"合格 %s"  % browser)
            assert 1
        else:
            print("浏览器数据异常  请重新输入 %s " % browser)
            assert 0

    def test_site(self, site):
        if site == "us":
            print("浏览器数据正常 %s " % site)
            assert 1

        elif site == "in":
            print("浏览器数据为 %s" % site ,"合格 %s"  % site)
            assert 1
        else:
            print("浏览器数据异常  请重新输入 %s " % site)
            assert 0
