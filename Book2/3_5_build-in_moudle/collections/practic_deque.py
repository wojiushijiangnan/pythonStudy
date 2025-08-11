#deque翻译叫：双队列，列表的列
# 当一个列表很大的时候对他执行增删改查效率太低了
# 使用双队列大大提高效率
from collections import deque
deq = deque([1,2,3,4,5])
print(deq)

deq.append(6)
print(deq)

deq.appendleft(0)
print(deq)

deq.pop()
print(deq)

deq.popleft()
print(deq)

deq.extend([7,8,9])
print(deq)

deq.extendleft([0,1,2])
print(deq)

# 把最后一个元素，放到第一个位置
deq.rotate(1)
print(deq)

# remove删除指定元素 insert在某个位置插入某个元素 reverse队列逆序

