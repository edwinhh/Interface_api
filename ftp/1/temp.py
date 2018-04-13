#-*- coding: utf-8 -*-
import requests
import ssl
p=[]
r=[]
url = "https://218.17.248.243:40115/tip"
data = {'q': '未央区明光路159号', \
        'city': '西安', \
        'ak': 'a4fbd3a08ecc4f9e41bc9b06421ef3b5'}
res = requests.get(url, params=data,verify=False)

p.append(data)
r.append(res.text)
print(p)
print(r)

# print unicode(eval(ss),"gbk")

