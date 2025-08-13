#在Python的函数设计中，
# 可变参数中的＊args和＊＊kwargs的作用分别是什么？如何使用它们？​
# （这是一道面试真题）

# *是元组
# **是字典
# 两者都可以传入不定量的参数



# ——————————————假设我们用元组表示学生名字和成绩，-------------------------
# 不同的元组放在一起构成一个成绩列表Scores，
# 请设计两个函数，分别按名字和成绩排序。
from collections import namedtuple
from random import choice

Students = namedtuple("Student", ["name", "score"])
s1 = Students("Tom", 90)
s2 = Students("Jerry", 80)
s3 = Students("Mike", 70)
s4 = Students("Lucy", 60)
s5 = Students("Mary", 50)
Scores = [s1,s2,s3,s4,s5]
Scores.sort(key=lambda x:x.name)
Scores.sort(key=lambda x:x.score)
print(Scores)

# ----------------------------------------------------------------------
# ---有两个人，第一个人先从1和2中挑一个数字，第二个人可以在对方的基础上选择加1或者加2，
# 然后又轮到第一个人，他也可以选择加1或者加2，之后再把选择权交给对方，
# 就这样双方交替地选择加1或者加2，谁先加到20，谁就赢了。对于这个游戏，
# 你用什么策略保证一定能赢？
from random import randint
b = 0
a = 0
a_num = randint(1, 2)
def play(a_num):
    global a,b
    a_num = randint(1,2)
    a = a + a_num
    b_num = randint(1,2)
    b = b + b_num
    total = a + b
