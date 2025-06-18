"""
创建列表
"""

print("创建列表")

items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ["Python", "Java", "JavaScript"]
items3 = [100, 12.3, "Python", True]
print(items1)
print(items2)
print(items3)

items4 = list(range(1, 11))
items5 = list("goku")
print(items4)
print(items5)

print()


"""
列表的运算
"""
print("列表的运算")

print("+ 列表拼接: ", items1 + items2)
print("* 重复运算：", items5 * 3)
print(35 in items1)
print("Nodejs" not in items2)

print()

"""
索引
"""
print("索引")

print(items2)
print("第0个元素：", items2[0])
print("第-1个元素：", items2[-1])

print()

"""
切片运算符
[start:end:stride] stride:跨度
start为0，可省略
end为元素个数，可省略
stride为1，可省略
"""
print("切片运算符")

print(items1)
print("[4:6]: ", items1[4:6])
print("[1:6:2]: ", items1[1:6:2])
print("[-4:-1:2]: ", items1[-4:-1:2])
print("[-2::-2]: ", items1[-2::-2])
print()
items6 = [1, 2, 3, 4]
print(items6)
items6[0:2] = [-1, -2]
print(items6)

print()

"""
元素的遍历
"""
languages = ["Python", "Java", "C++", "Kotlin"]
for item in languages:
    print(item)

languages = ['Python', 'Java', 'C++', 'Kotlin']
for index in range(len(languages)):
    print(languages[index])