"""
for-in循环
从1到100的整数求和
"""

total = 0
for i in range(1, 101):
    total += i
print(total)


"""
while循环
从1到100的整数求和
"""
total = 0
i = 1
while i <= 100:
    total += i
    i += 1
print(total)

"""
break
从1到100的偶数求和
"""
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total)

"""
continue
从1到100的偶数求和
"""
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)

print()

"""
嵌套的循环结构
打印乘法口诀表

\t : 制表符
print() : 换行
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}×{j}={i * j}", end="\t")
    print()
