"""
使用变量保存数据并进行加减乘除运算
"""

a = 45
b = 12
print(a, b)
print(a + b, a - b, a * b, a / b)


"""
使用type函数检查变量的类型
"""
a = 100
b = 123.45
c = "hello, world"
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


"""
变量的类型转换操作
"""

print(int('123'))
print(float('123.45'))
print(str(100))

print(chr(100))            # 将整数（字符编码）转换成对应的（一个字符的）字符串'
print(ord('d'))            # 将（一个字符的）字符串转换成对应的整数（字符编码）