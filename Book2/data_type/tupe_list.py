#请针对如下两个列表编写一段Python代码，
# 实现功能：如果元素不相同则两两封装成一个元组，
# 并将所有这样的元组打包成一个列表。
# 预期的结果是，​[(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]


# 在python中，元组一旦创建，其中的元素就不可以再被增删改查
list_a = [1, 2, 3]
list_b = [2, 7]
j = 0
list_c = []
for list in list_a:
    for i in list_b:
        if list != i:
            tuple_a = (list, i)
            list_c.append(tuple_a)
            j = j + 1
print(list_c)

# 用列表推导式实现上述效果
# if条件成立才会加入结果列表
different_num = [(i, j) for i in list_a for j in list_b if i != j]
#



# 第二题：在Python里面如何实现元组和列表的转换？
tupe = (1, 2, 3)
list = list(tupe)
tupe = tuple(list)

# 第三题：删除一个列表中的重复元素
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 如果有重复出现的元素就删除
for i in list:
    # count可以找出元素出现的次数
    if list.count(i) > 1:
        list.remove(i)
print( list)















