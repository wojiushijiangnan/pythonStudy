import requests
import plotly.express as px
import json
# 图形化展示了github中最受欢迎的java项目

url = "https://api.github.com/search/repositories"
url += "?q=language:java+sort:stars+stars:>10000"
headers = {"Accept": "application/vnd.github.v3+json"}

# 禁用代理
# 这里的r打印出来是一个键值对，要转化成jsion格式才可以
r = requests.get(url, headers=headers, proxies={"http": None, "https": None})
# 如果是两百就代表响应成功了
print(f'ok?:{r}')
# 将http响应转化为json格式的python对象
r = r.json()
# 接收一个python对象后返回一个json格式的字符串
# r = json.dumps(r)
# print(f'得到的响应数据是：{r}')
#
# r = r.json()
# total_count = r["total_count"]
# print(f'total_count:{total_count}')
# result = r["incomplete_results"]
# print(f'result:{not result}')

# 定义x轴 就是每一个项目的名称
items = r['items']
print(f'names列表中的第一个元素是：{items[0]}')
names = []
for itme in items:
    name = itme['name']
    names.append(name)
print(f'names:{names}')

fig = px.bar(x=names, y=[item['stargazers_count'] for item in items])
fig.show()
# names是一个列表
# 定义y轴 就是每一个项目的星星数量
# 要先得到画图对象
