#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: test_selenium.py
# @Time    : 2020/3/31 14:51
"""
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestSelenium(object):

    def test_selenium(self):
        capabilities = DesiredCapabilities.OPERA
        driver = webdriver.Remote(command_executor=f"http://127.0.0.1:4446/wd/hub",
                                  desired_capabilities=capabilities)
        driver.get("https://www.baidu.com")
