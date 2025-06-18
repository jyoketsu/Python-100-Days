"""
添加、删除元素
"""

# 添加
print("添加元素")

languages = ["Python", "Java", "C++", "Java"]
languages.append("JavaScript")
print(languages)
languages.insert(1, "SQL")
print(languages)

print()

# 删除
print("删除元素")

if "Java" in languages:
    languages.remove("Java")
if "Swift" in languages:
    languages.remove("Swift")
print(languages)

languages.pop()
print(languages)
languages.pop(1)
print(languages)

del languages[0]
print(languages)

print()

"""
元素位置和频次
"""
languages = ["Python", "Java", "C++", "Java"]
print("元素位置和频次")
print(languages.index("Python"))
print(languages.index("Java", 2))
print(languages.count("Java"))

print()

"""
元素排序和反转
"""
print("元素排序和反转")
languages.sort()
print(languages)

languages.reverse()
print(languages)

print()

"""
列表生成式
"""
print("列表生成式")
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)

nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)

print()

"""
嵌套列表
"""
print("嵌套列表")
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0])
print(scores[0][1])