#dumps方法把python编码成一个json字符串,也可以用来将python对象写入文件
import json
json_str = json.dumps([1,2,3,4,5])
print(type(json_str))

# loads方法,把json字符串编码成一个python对象,也可以用来读取json文件
json_str = '[1,2,3,4,5]'
json_obj = json.loads(json_str)
print(type(json_obj))

