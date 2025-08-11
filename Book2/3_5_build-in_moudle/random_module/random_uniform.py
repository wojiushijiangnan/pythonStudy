import random
# 生成一个0~1之间的随机浮点数
a = random.random()
print(a)

# 使用uniform生成一个指定范围之间的随机浮点数
a = random.uniform(1, 10)
print(a)

# 只产生一次随机数 _ 设定种子 一旦设定了种子后续每次产生的随机数都是相同的
random.seed(10)
a = random.uniform(1, 10)
print(a)

# 产生一个指定步长和范围的随机数
a = random.randrange(1, 10, 2)
print(a)

a = random.uniform(1, 10)
print(a)

# choice选取一个随机元素
# choices选取多个随机元素 参数为k
# sample选取多个不重复元素
# shuffle 打乱队列