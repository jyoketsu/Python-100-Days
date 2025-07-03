# 可见性
class MobileSuit:

    def __init__(self, name, hp, power, defense):
        self.name = name
        self.__hp = hp
        self._power = power
        self._defense = defense

    def attack(self, enemy_name):
        print(f"{self.name} 攻击了 {enemy_name}")


gundam = MobileSuit("Gundam", 100, 50, 30)
gundam.name = "Gundam"
gundam.attack("zaku")

# 测试可见性
print(gundam._power)
print(gundam._defense)
# print(gundam.__hp)


# 动态属性
gundam.height = 18
print(gundam.height)


# 静态方法和类方法
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     """判断三条边长能否构成三角形(类方法)"""
    #     return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


print(f"是否能构成三角形:{Triangle.is_valid(3, 4, 5)}")


# property装饰器
class Triangle(object):
    """三角形"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


t = Triangle(3, 4, 5)
print(f"周长: {t.perimeter}")
print(f"面积: {t.area}")


# 继承和多态
class Person:
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭.")

    def sleep(self):
        print(f"{self.name}正在睡觉.")


class Student(Person):
    """学生"""

    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f"{self.name}正在学习{course_name}.")


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f"{self.name}{self.title}正在讲授{course_name}.")


stu1 = Student("白元芳", 21)
stu2 = Student("狄仁杰", 22)
tea1 = Teacher("武则天", 35, "副教授")
stu1.eat()
stu2.sleep()
tea1.eat()
stu1.study("Python程序设计")
tea1.teach("Python程序设计")
stu2.study("数据科学导论")
