#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: conftest.py.py
# @Time    : 2020/3/1 20:43
"""

import pytest


def pytest_addoption(parser):
    parser.addoption("--env", action="store")
    parser.addoption("--browser", action="store")
    parser.addoption("--site", action="store")


@pytest.fixture
def env(request):
    print("env")
    return request.config.getoption("--env")


@pytest.fixture
def browser(request):
    print("browser")
    return request.config.getoption("--browser")

@pytest.fixture()
def site(request):
    print("site")
    return request.config.getoption("--site")
