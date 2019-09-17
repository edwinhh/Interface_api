d = {'b': 1, 'a': 2, 'c': 10}
d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
print(d_sorted_by_key)
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
print(d_sorted_by_value)

a=sorted(d.items(),key=lambda x:x[0])
a=sorted(d.items(),key=lambda x:x[1])

# name = input('your name:')
# gender = input('you are a boy?(y/n)')
#
#
# welcome_str = 'Welcome to the matrix {prefix} {name}.'
# welcome_dic = {
#     'prefix': 'Mr.' if gender == 'y' else 'Mrs',
#     'name': name
# }
#
# print('authorizing...')
# print(welcome_str.format(**welcome_dic))

import json

import json

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

# with open('params.json', 'w') as fout:
#     params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)

print('after json deserialization')
print('type of original_params = {}, original_params = {}'.format(type(original_params), original_params))

mport
json
import time

'''
SERVER端处理流程：
1.读取config.json文件
2.判断状态，若status=1,表示文件已经上传，需要等待下载，仍然回到第1步
3.若status=0,表示可上传文件到网盘，则读取要上传的源文件，大小不超过5G，并写入网盘文件
4.判断断源文件是否已经读完，若未读完，修改status=1，写回config.json，仍然回到第1步
5.否则，修改status=2，写回config.json,Server端程序结束。
'''


def getFileStatus():
    # 因第一次写Python，不知道怎么获取网盘文件，暂时用本地文件代替
    with open('F:\\temp\\config.json', 'r') as jsonfin:
        filestatus = json.load(jsonfin)
    
    return filestatus


def setFileStatus(filestatus):
    # 因第一次写Python，不知道怎么获取网盘文件，暂时用本地文件代替
    with open('F:\\temp\\config.json', 'w') as jsonfout:
        json.dump(filestatus, jsonfout)
    
    return

#------------------------------------------------------------------------------------------



