# # @Time : 2021/1/3
# # @Author : FPP
# # a = "1234567"
# b = (1, 2, 3, 4, 5)
# c = [1, 2, 3, 4, 5]
# e = {"A":"1", "B":"2", "C":"3"}
# d = ["a1", "a2", "a3", "a4"]
#
# print("元组中的每一个值为{}".format(*b))
# print(*e)
# print('A的值是{A}，B的值是{B}，C的值是{C}'.format(**e))
# # # print(id(a))
# # print(a[2])
# # print(b[3])
# # print(c[4])
# # print(d[0])
# # print(e["A"])
# # print(e["A"])
# # print(e["A"])
# #
# # def func(a,b,c):
# #     print("a")
# #     return a
# # func(*(1, 2, 3))
#
# # c = [1, 2, 3, 4, 5]
# # del c[:]
# # print(c)


# 输入输出，格式化方法
# import sys
# a = "hog"
# b = 3
# print("{1}{0}".format(a,b))
# a = "hello"
# b = (1, 2, 3, 4, 5)
# c = [1, 2, 3, 4, 5]
# d = {"A":"1", "B":"2", "C":"3"}
# print(f"第一个变量是{a}，第二个变量是{b}，第三个变量是{c}，第四个变量是{d}")
# print(f"b的第一个值是{b[0]},c的第二个值是{c[1]},d的C值是{d['C']}")

# name = "Lili"
# print(f"我的名字是{(lambda x: x+1)(2)}")


# 文件
# with open('data.txt') as f:
#     print(f.read())
#     # while True:
#     #     line = f.read()
#     #     if line:
#     #         print(line)
#     #     else:
#     #         break


# 类
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问的是实例的变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print(f"我的名字是{name}，我的年龄是{age}，我的性别是{gender}，我的重量是{weight}")

    def eat(self):
        print("我会吃")


# 类的实例化
ps = Person("fpp", 29, "女", 43.5)  # 实例化调用时，类名加括号，此时会直接跑init初始化方法，此为内置函数
# 访问实例变量
print(f"我的名字是:{ps.name}，我的年龄是:{ps.age}，我的性别是:{ps.gender}，我的重量是:{ps.weight}")
ps.eat()  # 调用类里的方法
# 类再实例化一个
ps = Person("fpp1", 30, "女", 43.5)
# 访问类变量
print(Person.name)
Person.eat()  # eat缺少一个self参数，而实例化时Person(),相当于默认传了self参数进去，且传给了eat()


# 加装饰器@classmethod
class Person:
    # 类变量
    name = "default"
    age = 0
    gender = "male"
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问的是实例的变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight
        print(f"我的名字是{name}，我的年龄是{age}，我的性别是{gender}，我的重量是{weight}")

    @classmethod
    def eat(self):
        print("我会吃")


Person.eat()
