# import xlrd,xlwt
# from xlutils import copy
import random,time
import threading
import multiprocessing
import openpyxl
from datetime import datetime
from datetime import timedelta
from openpyxl import Workbook
from openpyxl import load_workbook
import time,os




# thread=[]
# # wb=openpyxl.load_workbook(filename='2017-04-08-12_03_30.xlsx',read_only=False)
# # ts=wb.create_sheet("test11")
# now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
#
# class xls(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.wt = openpyxl.Workbook()
#         self.ts = self.wt.create_sheet("test")
#
#
#     def xls(self):
#
#         for i in range(1,6):
#             # for j in range(1,3):
#             self.ts.cell(row =i, column = 1,value = random.randint(100, 200))
#             self.ts.cell(row=i, column=2, value=random.randint(100, 200))
#
#
#     def run(self):
#         self.xls()
#
#     def save(self):
#         self.wt.save(now + ".xlsx")
#
#
#
# for i in range(1):
#     t1=xls()
#     thread.append(t1)
#
# start=time.time()
# for i in thread:
#     print('%s start' %i)
#
#     i.start()
#
# for i in thread:
#     print('%s join' %i)
#     i.join()
# end=time.time()
#
# print("closing...")
# print("time=%s" %(end-start))
# t1.save()
# print("end")




# wt = openpyxl.Workbook()
# ts = wt.create_sheet("test22")
# nrows=300
# pro=1
#
# def xls(ts):
#     for i in range(1,nrows):
#         for j in range(1,10):
#             ts.cell(row=i, column=j, value=random.randint(100, 200))
#     wt.save(now + ".xlsx")

#从excel读取tile和每行数据，然后将title和每行数据组成字典形式，存入list，形成传参
def get_data(filename,sheet_name):
    url_=[]
    url=[]#申明list
    tile=[]
    data=[]
    workbook_ = openpyxl.load_workbook(filename) #导入工作表
    sheetnames =workbook_.get_sheet_names() #获得表单名字
    # sheet = workbook_.get_sheet_by_name(sheetnames[sheet_name]) #从工作表中提取某一表单
    sheet = workbook_.get_sheet_by_name(sheet_name)
    print ("Work Sheet Rows:", sheet.max_row)

    for rowNum in range(1,sheet.max_row+1):
        if rowNum==1:
            for colNum in range(1, sheet.max_column + 1):
                tile.append(sheet.cell(row=1, column=colNum).value)
        else:
            url_ = []
            for colNum in range(1, sheet.max_column + 1):

                url_.append(sheet.cell(row=rowNum,column=colNum).value)
            url.append(url_)
        #print(url_)#获得数据
    # print(tile)
    # print(url)
    for i in range(len(url)):
        data.append(dict(zip(tile,url[i-1])))
    return data

#v=get_data("1.xlsx",'dic')

# if __name__ == '__main__':

    # for i in range(pro):
    #     t1=multiprocessing.Process(target =xls, args=())
    #     thread.append(t1)
    #
    # s=time.time()
    # for i in thread:
    #     print('%s start' %i)
    #     i.start()
    #
    # for i in thread:
    #     print('%s join' %i)
    #     i.join()
    # end=time.time()
    #
    # print("closing...")
    # print("time=%s" %(end-s))
    # pool = multiprocessing.Pool(processes=3)
    # for i in range(4):
    #     msg = "hello %d" % (i)
    #     pool.apply_async(xls,(msg, ))  # 维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    #
    # pool.close()
    # pool.join()

    # wt.save(now + ".xlsx")
    # print("end")

def report(name,url, p, r):
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    wb = Workbook()
    ws1 = wb.create_sheet(title=name)
    # 给第一行、第一列赋值，此处不同版本，起始行号可能不同
    ws1.cell(row=1, column=1).value = url
    print(len(p))
    for rowNum in range(1,len(p)+1):
        ws1.cell(row=rowNum, column=2).value = str(p[rowNum - 1])
        ws1.cell(row=rowNum, column=3).value = str(r[rowNum - 1])
    wb.save(name+ now + ".xlsx")

def reporttxt(name,url, p, r,n='test'):
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


    file=os.path.dirname(os.path.dirname(__file__))+ '/report'+'/'+name+"_"+now+".txt"
    with open(file,'w+',encoding='utf_8')as f:
        f.write(url)
        f.write('\n\n')
        for i in range(len(p)):
            temp = []
            f.write(str(i+1))
            f.write('\t')
            # f.write(n[i])
            f.write('\n')
            for key in p[i]:
                temp.append(key+"="+p[i][key])
            parameters="&".join(temp)
            case=url+"?"+parameters
            f.write(case)
            f.write('\n\n')
            f.write(str(p[i]))
            f.write('\n')
            f.write(str(r[i]))
            f.write('\n\n\n')






