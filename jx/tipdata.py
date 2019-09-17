import os,sys

dir="e:\项目\IPS\poi_not_hot"
dir2="e:\项目\IPS\poi_hot"
data=open(dir+'\\'+"data2.csv",'a+',encoding='utf-8')

def rline(f):
	count=0
	while 1:
		buffer = f.read(8 * 1024 * 1024)
		if not buffer:
			break
		count += buffer.count('\n')
		return count
	
def tipdata(dir):
	list = os.listdir(dir)  # 列出文件夹下所有的目录与文件
	for i in list:
		print(i)
		with open(dir+'\\'+i,'r',encoding='gb18030', errors='ignore') as f:
			if i=='data.csv' or i=='data2.csv'or i=='qinghai.csv' or i=='shandong.csv':
				continue
			if i=='aomen.csv':
				#kk=rline(f)
				#print(kk)
				for line in f.readlines()[0:30000]:
					data.write(line)
			else:
				for line in f.readlines()[0:160000]:
					data.write(line)

		
		
tipdata(dir)
