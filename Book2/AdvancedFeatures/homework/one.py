#这是一个dna类
class Dna:
    def __init__(self,num,des,dna):
        self.num = num
        self.des = des
        self.dna = self.__clean(dna)
    # 清空所有属性
    def __clean(self,dna):
        return dna.replace("\n","")

    #    计算gc在dna中的百分比
    def gc_percent(self,dna):
        dna = dna.upper()
        gc_percent = dna.count("G") + dna.count("C")/len(dna)
        return gc_percent

# 创建测试实例
dna = Dna(1,"test","ATGC")
print(dna.gc_percent(dna.dna))

# replace方法 replace（old，new，count【】）
# old是要被替换的字符串，new是要把old替换成什么
# 默认全部替换

# count方法，字符串对象.count（‘要搜索的字符’）
# return：该字符出现的次数
