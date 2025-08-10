from collections import Counter
#请针对如下两个列表编写一段Python代码，
# 实现功能：如果元素不相同则两两封装成一个元组，
# 并将所有这样的元组打包成一个列表。
# 预期的结果是，​[(1, 2), (1, 7), (2, 7), (3, 2), (3, 7)]


# 在python中，元组一旦创建，其中的元素就不可以再被增删改查
list_a = [1, 2, 3]
list_b = [2, 7]
j = 0
list_c = []
for yuansu in list_a:
    for i in list_b:
        if yuansu != i:
            tuple_a = (yuansu, i)
            list_c.append(tuple_a)
            j = j + 1
print(list_c)
# 注意：这里的循环结束后list仍然可以访问

# 用列表推导式实现上述效果
# if条件成立才会加入结果列表
different_num = [(i, j) for i in list_a for j in list_b if i != j]


# 第二题：在Python里面如何实现元组和列表的转换？
tupe = (1, 2, 3)
list_new = list(tupe)
tupe = tuple(list_new)

# 第三题：删除一个列表中的重复元素
list_d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 如果有重复出现的元素就删除
for i in list_d:
    # count可以找出元素出现的次数
    if list_d.count(i) > 1:
        list_d.remove(i)
print(list_d)\
# 除此之外，还可以利用集合的特性来去重
#     还可以利用字典



# 第四题：把names['Bob','JOHN','alice','bob','ALICE','J','Bob']
# 变成{'Alice','Bob','John'}
names = ['Bob','JOHN','alice','bob','ALICE','J','Bob']
i = 0
for w in names:
    if len(w) < 3:
        names.remove(w)
    names[i] = names[i].lower().title()
    i = i + 1
names = set(names)
print(names)

# 使用集合的列表推导式实现第四题
names = ['Bob','JOHN','alice','bob','ALICE','J','Bob']
names = {name[0].upper()+name[1:].lower() for name in names if len(name) >= 3}
print(names)

# 把第四题变成字典的形式，其中key是人名，value是出现的次数
names = ['Bob','JOHN','alice','bob','ALICE','J','Bob']
names = {name[0].upper()+name[1:].lower():names.count(name) for name in names if len(name) >= 3}
print( names)



# 第四题：Ai的答案
names = ['Bob','JOHN','alice','bob','ALICE','J','Bob']
# 先格式化所有名字，再使用Counter统计
# capitalize() 返回第一个字母大写 其余小写的字符串
formatted_names = [name.capitalize() for name in names if len(name) >= 3]
names_dict = dict(Counter(formatted_names))
# Counter对象: Counter({'Bob': 3, 'John': 1, 'Alice': 2})
print(names_dict)

# 第五题：键不区分大小写把值合并
mcase = {'a':10,"A":10,'b':20,"B":20,'c':30,"C":30}
# 把相同键的值相加
# 使用字典推导式
mcase = {key.lower():mcase[key.lower()]+mcase[key.upper()] for key in mcase.keys()}
print(mcase)














