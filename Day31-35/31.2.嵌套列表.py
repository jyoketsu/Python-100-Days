names = ["关羽", "张飞", "赵云", "马超", "黄忠"]
courses = ["语文", "数学", "英语"]
# 录入五个学生三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
print(scores)
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
        print(scores)

"""
# scores = [[None] * len(courses)] * len(names)
这种写法是错误的，因为这样创建的列表是浅拷贝，即多个子列表实际上是同一个列表对象。

# 一维列表（安全）
row = [None] * 3  # 创建包含3个独立None引用的列表
row[0] = 90       # 只修改第一个元素，其他元素不受影响

# 嵌套列表（危险）
table = [[None] * 3] * 5  # 创建5个指向同一个子列表的引用
table[0][0] = 90          # 所有子列表的第一个元素都会被修改
"""