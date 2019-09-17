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