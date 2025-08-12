import random
import string

'''（1）利用random模块相关知识，尝试生成500个优惠券激活码（长度为n，n可自定义
激活码一般都是由字母和数字组成的，首先要有一个包含所有字母和数字的字符串，然后随机取出几个字母或数字。
（2）尝试把生成的500个优惠券激活码利用json模块保存到本地，文件名为coupon.json。
（3）读取coupon.json，提示用户激活，验证成功后，该激活码失效。'''''

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
       'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
b = 0
str = ''
jihuomas = []
while b < 500:
    ji_huoma = random.choices(num, k=5)

    for i in ji_huoma:
        str = i+ str
    jihuomas.append(str)
    str = ''
    b = b+1
print(jihuomas)
print(len(jihuomas))

# 把jihuomas写入文件
import json
jihuomas = json.dumps(jihuomas)
# 给一个w参数 然后再用writ方法即可
with open('coupon.json', 'w') as f:
    f.write(jihuomas)
    print('写入成功')

# （3）读取coupon.json，提示用户激活，验证成功后，该激活码失效。'''''
with open('coupon.json', 'r') as f:
    jihuomas = json.load(f)

input_j = input('请输入激活码：')
if input_j in jihuomas:
    print('激活成功')
    jihuomas.remove(input_j)
else:
    print('激活码错误')

# 用列表推导式生成500个激活码
jihuomas = ["".join(random.choices(string.printable[:62], k=5)) for i in range(500)]