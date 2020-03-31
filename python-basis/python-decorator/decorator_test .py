#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# @Author  : Tim wang
# @FileName: decorator_test .py
# @Time    : 2020/3/23 17:07
"""

"""
装饰器使用方法：
1. 尝试用类来实现装饰器==================================================
介绍：https://www.zlovezl.cn/articles/tips-on-decorators/
"""

import functools
import random
import time


class DelayFunc:
    def __init__(self, duration, func):
        self.duration = duration
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        print('Call without delay')
        return self.func(*args, **kwargs)


def delay(duration):
    """装饰器：推迟某个函数的执行。同时提供 .eager_call 方法立即执行
    """
    # 此处为了避免定义额外函数，直接使用 functools.partial 帮助构造
    # DelayFunc 实例
    return functools.partial(DelayFunc, duration)


@delay(duration=2)
def add(a, b):
    return a + b


if __name__ == '__main__':
    # 这次调用将会延迟 2 秒
    add(1, 2)
    # 这次调用将会立即执行
    add.eager_call(1, 2)

"""
2. 使用 wrapt 模块编写更扁平的装饰器===============================================

"""


def provide_number(min_num, max_num):
    """装饰器：随机生成一个在 [min_num, max_num] 范围的整数，追加为函数的第一个位置参数
    """

    def test(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)
            # 将 num 作为第一个参数追加后调用函数
            return func(num, *args, **kwargs)

        return decorated

    return test


"""
类调用装饰器
"""


class Foo:
    @provide_number(1, 100)
    def print_random_number(self, num):
        print(num)


"""
方法调用装饰器
"""


@provide_number(1, 100)
def print_random_number(num):
    print(num)


"""
装饰器模式=======================

"""


def s32_u16(x):
    if x < 0:
        sign = 0xf000
    else:
        sign = 0

    bottom = x & 0x00007ffff
    return bottom | sign


def seed_from_xy(x, y):
    return s32_u16(x) | (s32_u16(y) << 16)


class RandomSquare:
    def __init__(self, seed_modifier):
        self.seed_modifier = seed_modifier

    def get(self, x, y):
        seed = seed_from_xy(x, y) ^ self.seed_modifier
        random.seed(seed)
        return random.randint(0, 255)


class DataSquare:
    def __init__(self, initial_value=None):
        self.data = [initial_value] * 10 * 10

    def get(self, x, y):
        return self.data[(y * 10) + x]

    def set(self, x, y, u):
        self.data[(y * 10) + x] = u


class CacheDecorator:
    def __init__(self, decorated):
        self.decorated = decorated
        self.cache = DataSquare()

    def get(self, x, y):
        if self.cache.get(x, y) is None:
            self.cache.set(x, y, self.decorated.get(x, y))
        return self.cache.get(x, y)


class MaxDecorator:
    def __init__(self, decorated, max):
        self.decorated = decorated
        self.max = max

    def get(self, x, y):
        if self.decorated.get(x, y) > self.max:
            return self.max
        return self.decorated.get(x, y)


class MinDecorator:
    def __init__(self, decorated, min):
        self.decorated = decorated
        self.min = min

    def get(self, x, y):
        if self.decorated.get(x, y) < self.min:
            return self.min
        return self.decorated.get(x, y)


class VisibilityDecorator:
    def __init__(self, decorated):
        self.decorated = decorated

    def get(self, x, y):
        return self.decorated.get(x, y)

    def draw(self):
        for y in range(10):
            for x in range(10):
                print("%3d" % self.get(x, y)),


# Now, build up a pipeline of decorators:

random_square = RandomSquare(635)
random_cache = CacheDecorator(random_square)
max_filtered = MaxDecorator(random_cache, 200)
min_filtered = MinDecorator(max_filtered, 100)
final = VisibilityDecorator(min_filtered)

final.draw()

if __name__ == '__main__':
    print_random_number()

    Foo().print_random_number()
