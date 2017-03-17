import sys
for dir in ('lib','case'):
	try:
		sys.path.index(sys.path[0] + '/' + dir)
	except Exception,e:
		sys.path.append(sys.path[0] + '/' + dir)
