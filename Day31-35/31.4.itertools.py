"""
迭代工具模块
"""

import itertools

"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
# 返回的是迭代器对象（内存高效，不会立即生成所有组合）
perm = itertools.permutations("ABCD")

# 转换为列表查看结果（实际使用时建议直接遍历）
print(list(perm))

# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCD和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))