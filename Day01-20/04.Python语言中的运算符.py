"""
算术运算符
"""

print(321 + 12)  # 加法运算，输出333
print(321 - 12)  # 减法运算，输出309
print(321 * 12)  # 乘法运算，输出3852
print(321 / 12)  # 除法运算，输出26.75
print(321 // 12)  # 整除运算，输出26
print(321 % 12)  # 求模运算，输出9
print(321**12)  # 求幂运算，输出1196906950228928915420617322241


"""
赋值运算符和复合赋值运算符
"""
a = 10
b = 3
a += b  # 相当于：a = a + b
a *= a + 2  # 相当于：a = a * (a + 2)
print(a)


"""
海象运算符
variable := expression
将 expression 的计算结果赋值给 variable，并返回该值
"""
print((n := len("data")) > 10)


"""
比较运算符和逻辑运算符的使用
"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not flag0
print("flag0 =", flag0)  # flag0 = True
print("flag1 =", flag1)  # flag1 = True
print("flag2 =", flag2)  # flag2 = False
print("flag3 =", flag3)  # flag3 = False
print("flag4 =", flag4)  # flag4 = True
print("flag5 =", flag5)  # flag5 = False
print(flag1 and not flag2)  # True
print(1 > 2 or 2 == 3)  # False

"""
应用
输入半径计算圆的周长和面积
"""
import math

radius = float(input("请输入圆的半径: "))
perimeter = 2 * math.pi * radius
area = math.pi * radius**2
print(f"周长: {perimeter:.2f}")
print(f"面积: {area:.2f}")
