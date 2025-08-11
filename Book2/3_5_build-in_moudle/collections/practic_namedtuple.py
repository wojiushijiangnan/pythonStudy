from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
# namedtupe数据类型给出了元组的实例p
p = Point(1, 2)
# namedtupe实际是一个工厂类，通过namedtuple加工出来的依然是元组的子类，只不过不同的类各有个性罢了
# 比如Point依然是元组的子类

# 解包unpacking
# 会把一个可迭代对象一一赋值给一组变量
a,b = p
print(a,b)

# 元组一样可以通过索引来访问
