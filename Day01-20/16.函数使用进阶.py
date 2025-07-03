"""
高阶函数
"""


# *args用于接收任意数量的位置参数
# **kwargs用于接收任意数量的关键字参数
# 同时使用两者,可以同时接受位置参数和关键字参数
def calc(init_value, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_value
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(0, add, 1, 2, 3, 4, 5))

print(calc(1, mul, 1, 2, 3, a=4, b=5))

"""
Lambda函数 (匿名函数)
"""
print(calc(0, lambda x, y: x + y, 1, 2, 3, 4, 5))

"""
偏函数
"""
import functools

add2and3 = functools.partial(add, 2, 3)
print(add2and3())

add2 = functools.partial(add, 2)
print(add2(3))
