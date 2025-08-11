from collections import defaultdict
'''使用字典时，如果所引用的键不存在，就会抛出异常—KeyError，从而导致整个程序终止执行。
如果希望键不存在时能返回一个默认值，就需要使用提供默认值的字典类型defaultdict。'''
dd = defaultdict(lambda:'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])