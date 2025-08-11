#实现词频统计
colors = ['red', 'blue', 'green', 'yellow',
          'orange', 'purple', 'pink', 'brown', 'gray',
          'olive', 'cyan', 'magenta','red']

result = {}

for color in colors:
    if result.get(color)==None:
        result[color] = 1
    else:
        result[color] += 1
print(result)

# 利用Counter来实现词频统计
from collections import Counter
colors = ['red', 'blue', 'green', 'yellow','red']
# Counter对象自动记录了元素出现的次数
result = Counter(colors)
# Counter对象无法直接输出,要转化为字典才可以正常输出
print(dict(result))
# most_common()方法可以返回出现次数最多的n个元素
print(result.most_common(2))

