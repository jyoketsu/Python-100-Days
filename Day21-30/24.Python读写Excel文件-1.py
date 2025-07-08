"""
写Excel文件
"""

import random

import xlwt

student_names = ["关羽", "张飞", "赵云", "马超", "黄忠"]
scores = [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()
# 创建工作表对象（Worksheet）
sheet = wb.add_sheet("一年级二班")
# 添加表头数据
titles = ("姓名", "语文", "数学", "英语")

# enumerate()函数用于给可迭代对象添加索引，形成（索引，元素）的元组
for index, title in enumerate(titles):
    # 写入表头，0行，index列
    sheet.write(0, index, title)
# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    # 写入学生姓名，row+1行，0列
    sheet.write(row + 1, 0, student_names[row])
    for col in range(len(scores[row])):
        # 写入考试成绩，row+1行,col+1列
        sheet.write(row + 1, col + 1, scores[row][col])
# 保存Excel工作簿
wb.save("考试成绩表.xls")


"""
读Excel文件
"""

import xlrd

# 打开Excel文件，返回Book对象（工作簿）
wb = xlrd.open_workbook("考试成绩表.xls")
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetnames = wb.sheet_names()
print(f"sheetnames: {sheetnames}")

# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetnames[0])
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(f"sheet.nrows, sheet.ncols: {sheet.nrows, sheet.ncols}")
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        print(value, end="\t")
    print()

# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(f"last_cell_type: {last_cell_type}")

# 获取第一行的值（列表）
print(sheet.row_values(0))
# 获取指定行指定列范围的数据（列表）
# 第一个参数代表行索引，第二个和第三个参数代表列的开始（含）和结束（不含）索引
print(sheet.row_slice(3, 0, 2))


"""
调整单元格样式
"""

from xlrd import open_workbook
from xlutils.copy import copy

# 1. 用xlrd打开已存在的文件
rb = open_workbook("考试成绩表.xls")
# 2. 创建可写的副本
wb = copy(rb)
sheet = wb.get_sheet(0)  # 获取第一个工作表

# 3. 创建新的表头样式
header_style = xlwt.XFStyle()

font = xlwt.Font()
font.bold = True
font.colour_index = xlwt.Style.colour_map["red"]
header_style.font = font

# 设置背景色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlwt.Style.colour_map["gray25"]
header_style.pattern = pattern

align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align

borders = xlwt.Borders()
props = (
    ("top", "top_colour"),
    ("right", "right_colour"),
    ("bottom", "bottom_colour"),
    ("left", "left_colour"),
)
# 通过循环对四个方向的边框样式及颜色进行设定
for position, color in props:
    # 使用setattr内置函数动态给对象指定的属性赋值
    setattr(borders, position, xlwt.Borders.DASHED)
    setattr(borders, color, 5)
header_style.borders = borders

# 4. 修改表头样式
for col in range(4):  # 假设有4列表头
    # 需要重新写入单元格才能应用样式
    sheet.write(0, col, titles[col], header_style)
    sheet.col(col).width = 256 * 15  # 调整列宽

# 5. 另存为新文件（xlutils不能覆盖原文件）
wb.save("考试成绩表_样式修改.xls")


"""
公式计算
"""
rb = open_workbook("考试成绩表.xls")
wb = copy(rb)
sheet = wb.get_sheet(0)  # 获取第一个工作表

sheet.write(0, 4, "总分")

# 先获取原始数据行数
original_sheet = rb.sheet_by_index(0)
# 获取行数
total_rows = original_sheet.nrows

# 添加总分列公式（从第2行开始）
for row_idx in range(1, total_rows):
    # 设置SUM公式（B列到D列）
    formula = f"SUM(B{row_idx+1}:D{row_idx+1})"  # Excel行号从1开始
    sheet.write(row_idx, 4, xlwt.Formula(formula))  # 第5列（索引4）写入公式

# 调整总分列宽
sheet.col(4).width = 256 * 15

# 保存带公式的新文件
wb.save("考试成绩表_带公式.xls")
