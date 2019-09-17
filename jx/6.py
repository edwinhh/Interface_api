#NLP 例子中的 word count 实现一遍？不过这次，in.txt 可能非常非常大（意味着你不能一次读取到内存中），而 output.txt 不会很大（意味着重复的单词数量...
import re

CHUNK_SIZE = 100 # 这个数表示一次最多读取的字符长度

# 这个函数每次会接收上一次得到的 last_word，然后和这次的 text 合并起来处理。
# 合并后判断最后一个词有没有可能连续，并分离出来，然后返回。
# 这里的代码没有 if 语句，但是仍然是正确的，可以想一想为什么。

def parse_to_word_list(text, last_word, word_list):
	print("Text:{}".format(text))
	text = re.sub(r'[^\w ]', ' ', last_word + text)
	text = text.lower()
	cur_word_list = text.split(' ')
	cur_word_list, last_word = cur_word_list[:-1], cur_word_list[-1]
	word_list += filter(None, cur_word_list)
	print("text:{}".format(text))
	print("last_word:{}".format(last_word))
	#print("last_word:{}".format(last_word))
	return last_word

def solve():
    with open('in.txt', 'r') as fin:
        word_list, last_word = [], ''
        while True:
            text = fin.read(CHUNK_SIZE)
            if not text:
                break # 读取完毕，中断循环
            last_word = parse_to_word_list(text, last_word, word_list)
			
        word_cnt = {}
        for word in word_list:
            if word not in word_cnt:
                word_cnt[word] = 0
            word_cnt[word] += 1
		
            sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)
        return sorted_word_cnt

print(solve())



#------------------------------------------------------------------------------------------------------

'''
你应该使用过类似百度网盘、Dropbox 等网盘，但是它们可能空间有限（比如 5GB）。如果有一天，你计划把家里的 100GB 数据传送到公司
每次从家里向 Dropbox 网盘写入不超过 5GB 的数据,而公司电脑一旦侦测到新数据,就立即拷贝到本地,然后删除网盘上的数据。等家里电脑侦测到本次数据全部传入公司电脑后,再进行下一次写入,
直到所有数据都传输
根据这个想法,你计划在家写一个 server.py,在公司写一个 client.py 来实现这个需求
提示：我们假设每个文件都不超过 5GB。
你可以通过写入一个控制文件(config.json)来同步状态。不过,要小心设计状态,这里有可能产生 race condition。
你也可以通过直接侦测文件是否产生，或者是否被删除来同步状态，，这是最简单的做法。
'''



#server.py
# 我们假设 server 电脑上的所有的文件都在 BASR_DIR 中，为了简化不考虑文件夹结构，网盘的路径在 NET_DIR

import os
from shutil import copyfile
import time

BASE_DIR = 'server/'
NET_DIR = 'net/'

def server():
    filenames = os.listdir(BASE_DIR)
    for i, filename in enumerate(filenames):
        print('copying {} into net drive... {}/{}'.format(filename, i + 1, len(filenames)))
        copyfile(BASE_DIR + filename, NET_DIR + filename)
        print('copied {} into net drive, waiting client complete... {}/{}'.format(filename, i + 1, len(filenames)))

        while os.path.exists(NET_DIR + filename):
            time.sleep(3)

    print('transferred {} into client. {}/{}'.format(filename, i + 1, len(filenames)))




#client.py
# 我们假设 client 电脑上要输出的文件夹在 BASR_DIR ，网盘的路径在 NET_DIR

import os
from shutil import copyfile
import time

BASE_DIR = 'client/'
NET_DIR = 'net/'

def client():
    while True:
        filenames = os.listdir(NET_DIR)
        for filename in filenames:
            print('downloading {} into local disk...'.format(filename))
            copyfile(NET_DIR + filename, BASE_DIR + filename)
            os.remove(NET_DIR + filename) # 我们需要删除这个文件，网盘会提我们同步这个操作，从而 server 知晓已完成
            print('downloaded {} into local disk.'.format(filename))
        time.sleep(3)

if __name__ == "__main__":
	pass