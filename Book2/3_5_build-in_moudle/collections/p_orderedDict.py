from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

# 其中的键是按照键的插入顺序来排列的;
# 按照插入键的顺序返回
list(od.keys())

keys = ['apple','banana','cat']
value = [4,5,6]
# 合并两个列表为一个字典
od.update(zip(keys,value))
print(od)

# 将键为'apple'的元素移到末尾
od.move_to_end('apple')
