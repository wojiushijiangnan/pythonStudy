class persion:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


p1 = persion('张三', 18, 80)
print(p1.name)
print("my name is %s, my age is %d,weight is %d"%(p1.name,p1.age,p1.get_weight()))