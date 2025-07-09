"""
生成式（推导式）的用法
"""

prices = {
    "AAPL": 191.88,
    "GOOG": 1186.96,
    "IBM": 149.24,
    "ORCL": 48.44,
    "ACN": 166.89,
    "FB": 208.09,
    "SYMC": 21.29,
}

# 用股票价格大于100元的股票构造一个新的字典
prices2 = {
    # 结果表达式：保留键值对
    key: value
    # 遍历原始字典的键值对
    for key, value in prices.items()
    # 过滤条件：值大于100
    if value > 100
}
print(prices2)

# 注意：
# 直接遍历字典（获取键）
for key in prices:
    print(key)  # 输出：AAPL, GOOG, IBM...

# 遍历字典的items（获取键值对）
for key, value in prices.items():
    print(key, value)  # 输出：AAPL 191.88, GOOG 1186.96...
