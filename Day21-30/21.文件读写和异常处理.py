"""
读文件
"""

print("########################### file.read() ####################################")

file = open("致橡树.txt", "r", encoding="utf-8")
print(file.read())
file.close()

print()
print("########################### for-in ####################################")

file = open("致橡树.txt", "r", encoding="utf-8")
for line in file:
    print(line, end="")
file.close()

print()
print()
print("########################### readlines ####################################")

file = open("致橡树.txt", "r", encoding="utf-8")
lines = file.readlines()
for line in lines:
    print(line, end="")
file.close()

"""
写文件
"""
file = open("致橡树.txt", "a", encoding="utf-8")
# file.write("\n标题：《致橡树》")
# file.write("\n作者：舒婷")
# file.write("\n时间：1977年3月")
file.close()


"""
异常处理
"""
print()
print()

file = None
try:
    file = open("异常.txt", "r", encoding="utf-8")
    print(file.read())
except FileNotFoundError:
    print("无法打开指定的文件!")
except LookupError:
    print("指定了未知的编码!")
except UnicodeDecodeError:
    print("读取文件时解码错误!")
finally:
    if file:
        file.close()


# raise 抛出异常
class InputError(ValueError):
    """自定义异常类型"""

    pass


def fac(num):
    """求阶乘"""
    if num < 0:
        raise InputError("只能计算非负整数的阶乘")
    if num in (0, 1):
        return 1
    return num * fac(num - 1)


# 捕获异常
flag = True
while flag:
    num = int(input("n = "))
    try:
        print(f"{num}! = {fac(num)}")
        flag = False
    except InputError as err:
        print(err)


# 上下文管理器语法
try:
    with open("1致橡树.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("无法打开指定的文件!")
except LookupError:
    print("指定了未知的编码!")
except UnicodeDecodeError:
    print("读取文件时解码错误!")


"""
读写二进制文件
"""
try:
    with open("guido.jpg", "rb") as file1:
        data = file1.read()
    with open("吉多.jpg", "wb") as file2:
        file2.write(data)
except FileNotFoundError:
    print("指定的文件无法打开.")
except IOError:
    print("读写文件时出现错误.")
print("程序执行结束.")

"""
大文件循环读写
size: 字节数
"""
try:
    with open("guido.jpg", "rb") as file1, open("吉多.jpg", "wb") as file2:
        data = file1.read(512)
        while data:
            file2.write(data)
            data = file1.read()
except FileNotFoundError:
    print("指定的文件无法打开.")
except IOError:
    print("读写文件时出现错误.")
print("程序执行结束.")
