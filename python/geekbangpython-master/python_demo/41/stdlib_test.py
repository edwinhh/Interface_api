# 日常应用比较广泛的模块是：
# 1. 文字处理的 re
# 2. 日期类型的time、datetime
# 3. 数字和数学类型的math、random
# 4. 文件和目录访问的pathlib、os.path
# 5. 数据压缩和归档的tarfile
# 6. 通用操作系统的os、logging、argparse
# 7. 多线程的 threading、queue
# 8. Internet数据处理的 base64 、json、urllib
# 9. 结构化标记处理工具的 html、xml
# 10. 开发工具的unitest
# 11. 调试工具的 timeit
# 12. 软件包发布的venv
# 13. 运行服务的__main__


#  ^ $ . ? * +  {m} {m,n} [] |  \d \D \s ()
# ^$
# .*?

import re


p = re.compile(r'(\d+)-(\d+)-(\d+)')
print (p.search('aa1-05-10bb').group())
print (p.match('2018-05-10').group(1) )

t=re.compile('d{1,5}')
# print('a','b',end='\n')
# print('a','b',end='\n')
# print(t.match('ddddddccccc').group() )
# year, month, day = p.match('2018-05-10').groups()
# print(year)
#
#print (p.search('aa2018-05-10bb'))
phone = '123-456-789 # 这是电话号码'
# p2 = re.sub(r'#.*$','',phone)
# print(p2)
# p3 = re.sub(r'\D','',p2)
# print(p3)
# findall()

string="abcdefg  acbdgef  abcdgfe  cadbgfe"

#带括号与不带括号的区别
#不带括号
#re=re.compile("((\w+)\s+\W+)")

string="abcdefg  acbdgef  abcdgfe  cadbgfe"

#带括号与不带括号的区别
#不带括号
regex=re.compile("((\w+)\s+\w+)")
print(regex.findall(string))
#输出：[('abcdefg  acbdgef', 'abcdefg'), ('abcdgfe  cadbgfe', 'abcdgfe')]

regex1=re.compile("(\w+)\s+\w+")
print(regex1.findall(string))
#输出：['abcdefg', 'abcdgfe']

regex2=re.compile("\w+\s+\w+")
print(regex2.findall(string))
#输出：['abcdefg  acbdgef', 'abcdgfe  cadbgfe']