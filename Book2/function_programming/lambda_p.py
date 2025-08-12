#filter(判断函数，可迭代对象)
# 判断函数就是指定筛选规则，第二个是序列作为第一个函数的参数
# 序列中的每个元素都会传递给函数进行判断 True的就留下
# 过滤奇数，只要偶数
def isdb(*n):
    for i in n:
        if i % 2 == 0:
            return True
        else:
            return False

# 给filter的函数的返回值一定要是True or false
print(list(filter(isdb, range(10))))

# 使用lambda完成
data = filter(lambda x : x % 2 == 0, range(10))
new_data = list(data)
print(new_data)

#————————map函数——————————————————————————————————
# map(函数（函数也是一个对象），可迭代对象)
# map会按照该函数指定的规则，将一个序列转换为另一个序列
# 由于原序列中和被转序列中的元素存在一一对应的关系，所以也把这种关系描述为映射。
# map()函数中第2个（含）以后的参数表示待加工的数据序列，具体需要几个数据序列，
# 取决于第1个参数。如前所述，第1个参数是函数对象，那么它就像一个加工机器，
# 需要几样“原材料”​，其后就跟随几个可迭代的数据序列。
# 比如说，第1个参数对应的函数功能是取某个序列中元素的相反数，
# ​“取反”是一元操作，那么第1个参数之后再跟一个序列参数即可。
# 再比如，第1个参数对应的函数功能是求和，​“求和”是二元操作，
# 那么第1个参数之后就需要两个序列，以此类推
def myfunction(n):
    return len(n)
a_list = ['abcd', 'efgh', 'ijkl', 'mnop']
b_map = map(myfunction,a_list)
b_list = list(b_map)
print(b_list)

# ——————————————————————sorted函数——————————————————————

# 如果比较的数字就可以直接比较，如果比较的是字符串或者字典，那么大小就难以判断
# 因此我们可以给sorted传入一个函数，这个函数定义了排序对的规则
# 传入函数作为排序的参数，需要用key作为关键字参数，其中传入函数名
list_d = [-20,20,30,-62]
list_d = sorted(list_d, key=abs, reverse=True)
# 打印这个没有用，因为不会修改原来的列表
print(list_d)
# 也可以用sort函数对列表本身进行操作。