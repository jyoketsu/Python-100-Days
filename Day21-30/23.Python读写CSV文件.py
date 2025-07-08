# 将数据写入CSV文件
import csv
import random

with open("scores.csv", "w") as file:
    writer = csv.writer(file)

    # 指定分隔符、包围值的字符、包围的方式
    # writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)

    writer.writerow(["姓名", "语文", "数学", "英语"])
    names = ["关羽", "张飞", "赵云", "马超", "黄忠"]
    for name in names:
        # 列表生成式 [表达式 for 变量 in 可迭代对象 if 条件]
        scores = [random.randrange(50, 101) for _ in range(3)]
        scores.insert(0, name)
        writer.writerow(scores)


# 从CSV文件读取数据
with open("scores.csv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    for data_list in reader:
			  # end='\t' 表示打印内容后不换行，而是添加一个制表符
        print(reader.line_num, end="\t")
        for elem in data_list:
            print(elem, end="\t")
        print()

