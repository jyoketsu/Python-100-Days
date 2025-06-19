# 定义一个三元组
t1 = (35, 12, 98)
# 定义一个四元组
t2 = ("骆昊", 45, True, "四川成都")

# 查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>

# 查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4

# 索引运算
print(t1[0])  # 35
print(t1[2])  # 98
print(t2[-1])  # 四川成都

# 切片运算
print(t2[:2])  # ('骆昊', 43)
print(t2[::3])  # ('骆昊', '四川成都')

# 循环遍历元组中的元素
for elem in t1:
    print(elem)

# 成员运算
print(12 in t1)  # True
print(99 in t1)  # False
print("Hao" not in t2)  # True

# 拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '骆昊', 43, True, '四川成都')

# 比较运算
print(t1 == t3)  # False
print(t1 >= t3)  # False
print(t1 <= (35, 11, 99))  # False

# 元组中只有一个元素，需要加上一个逗号
a = ()
print(type(a))  # <class 'tuple'>
b = "hello"
print(type(b))  # <class 'str'>
c = 100
print(type(c))  # <class 'int'>
d = ("hello",)
print(type(d))  # <class 'tuple'>
e = (100,)
print(type(e))  # <class 'tuple'>


"""
打包和解包操作
"""

# 打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)  # (1, 10, 100)

# 解包操作
i, j, k = a
print(i, j, k)  # 1 10 100

# 解包 星号表达式
a = 1, 10, 100, 1000
i, *j = a
print(i, j, k)  # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)  # 1 [10, 100] 1000

# 解包 其他序列（范围，数组，字符串）
a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = "hello"
print(a, b, c)

"""
交换变量的值
"""
a, b, c = b, c, a
