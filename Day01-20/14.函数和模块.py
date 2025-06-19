"""
输入m和n，计算组合数C(m,n)的值
"""


# 通过关键字def定义求阶乘的函数
# 自变量（参数）num是一个非负整数
# 因变量（返回值）是num的阶乘
def fac(num):
    result = 1
    for n in range(2, num + 1):
        result *= n
    return result


m = int(input("m = "))
n = int(input("n = "))
# 计算阶乘的时候不需要写重复的代码而是直接调用函数
# 调用函数的语法是在函数名后面跟上圆括号并传入参数
print(fac(m) // fac(n) // fac(m - n))


"""
math.factorial
输入m和n，计算组合数C(m,n)的值
"""
from math import factorial

m = int(input("m = "))
n = int(input("n = "))
print(factorial(m) // factorial(n) // factorial(m - n))

"""
from import as
输入m和n，计算组合数C(m,n)的值
"""
from math import factorial as f

m = int(input("m = "))
n = int(input("n = "))
print(f(m) // f(n) // f(m - n))


"""
函数的参数
"""


def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 位置参数
print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True

# 关键字参数
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True


"""
强制位置参数
"""


# /前面的参数是强制位置参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
# TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
# print(make_judgement(b=2, c=3, a=1))


"""
强制命名关键字参数
"""


# *后面的参数是命名关键字参数
def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b


# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make_judgement() takes 0 positional arguments but 3 were given
# print(make_judgement(1, 2, 3))


"""
参数的默认值
"""


def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c


# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())  # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))  # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))  # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6


"""
可变参数
"""


# 用星号表达式来表示args可以接收0个或任意多个参数
# 调用函数时传入的n个参数会组装成一个n元组赋给args
# 如果一个参数都没有传入，那么args会是一个空元组
def add(*args):
    total = 0
    # 对保存可变参数的元组进行循环遍历
    for val in args:
        # 对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total


# 在调用add函数时可以传入0个或任意多个参数
print(add())  # 0
print(add(1))  # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, "hello", 3.45, 6))  # 12.45


# 参数列表中的**kwargs可以接收0个或任意多个关键字参数
# 调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
# 如果一个关键字参数都没有传入，那么kwargs会是一个空字典
def foo(*args, **kwargs):
    print(args)
    print(kwargs)


foo(3, 2.1, True, name="骆昊", age=43, gpa=4.95)


"""
用模块管理函数
"""

import module1
import module2

# 用“模块名.函数名”的方式（完全限定名）调用函数，
module1.foo()  # hello, world!
module2.foo()  # goodbye, world!

import module1 as m1
import module2 as m2

m1.foo()  # hello, world!
m2.foo()  # goodbye, world!

from module1 import foo

foo()  # hello, world!

from module2 import foo

foo()  # goodbye, world!

from module1 import foo as f1
from module2 import foo as f2

f1()  # hello, world!
f2()  # goodbye, world!
