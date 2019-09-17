text = ' Today,  is, Sunday'
#text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 5]
text_list = [s.strip() for s in text.split(',')]
print(text_list)

x=[1,2]
y=['a',1]
xx=()
yy=()
[(xx, yy) for xx in x for yy in y if xx != yy]
#print(xx)

# file='e:\项目\IPS\输入提示\c++\CollGeoDetail_20171217.csv'
# file1='e:\项目\IPS\输入提示\c++\CollGeoDetail_201712171.csv'
# keys=['广东','广州','深圳','珠海','东莞','佛山','惠州']
# p=open(file1,'w+',encoding='utf-8')
# with open(file,'r',encoding='utf_8') as f:
# 	for line in f.readlines():
# 		for key in keys:
# 			if key in line:
# 				print(line)
# 				p.write(line)
#
# p.close()
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected output:

print([dict(zip(attributes, value)) for value in values])


# def find_largest_element(l):
# 	if not isinstance(l, list):
# 		print('input is not type of list')
# 		return
# 	if len(l) == 0:
# 		print('empty input')
# 		return
# 	largest_element = l[0]
# 	for item in l:
# 		if item > largest_element:
# 			largest_element = item
# 	print('largest element is: {}'.format(largest_element))


def find_bigelement(l):
	if not isinstance(l,list):
		print("no list")
		return
	if len(l)==0:
		print("empty list")
		return
	k=l[0]
	for i in l:
		if i>k:
			k=i
	print("big element is :{}".format(k))
find_bigelement([1,2,-2,10])

squared = map(lambda x: x**2, [1, 2, 3, 4, 5])

l=[1, 2, 3, 4, 5]

a=map(lambda x: x ** 2,l )

print(list(a))

l = [1, 2, 3, 4, 5]
new_list = filter(lambda x: x % 2 == 0, l) # [2, 4]

print(new_list)
print(list(new_list))
print(new_list.__next__)
	
d = {'mike': 10, 'lucy': 2, 'ben': 30}
c=sorted(d.items(),key=lambda x:x[1],reverse=True)

