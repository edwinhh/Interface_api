import re
import pylru

class SearchEngineBase(object):
    def __init__(self):
        pass

    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)

    def process_corpus(self, id, text):
        raise Exception('process_corpus not implemented.')

    def search(self, query):
        raise Exception('search not implemented.')

def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus(file_path)

    while True:
        query = input('input query:')
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)



class LRUCache(object):
	def __init__(self, size=64):
		self.cache = pylru.lrucache(size)
	
	def has(self, key):
		return key in self.cache
	
	def get(self, key):
		return self.cache[key]
	
	def set(self, key, value):
		self.cache[key] = value






class BOWInvertedIndexEngine(SearchEngineBase):
	def __init__(self):
		super(BOWInvertedIndexEngine, self).__init__()
		self.inverted_index = {}
	
	def process_corpus(self, id, text):
		words = self.parse_text_to_words(text)
		for word in words:
			if word not in self.inverted_index:
				self.inverted_index[word] = []
			self.inverted_index[word].append(id)

	
	def search(self, query):
		query_words = list(self.parse_text_to_words(query))
		query_words_index = list()

		for query_word in query_words:
			query_words_index.append(0)
		print('query_words_index:',query_words_index)
		
		# 如果某一个查询单词的倒序索引为空，我们就立刻返回
		for query_word in query_words:
			if query_word not in self.inverted_index:
				return []
		
		result = []
		while True:
			
			# 首先，获得当前状态下所有倒序索引的 index
			current_ids = []
			
			for idx, query_word in enumerate(query_words):
				print('idx:',idx)
				print('query_word:',query_word)
				current_index = query_words_index[idx]
				print('current_index:',current_index)
				current_inverted_list = self.inverted_index[query_word]
				print('current_inverted_list:',current_inverted_list)
				
				# 已经遍历到了某一个倒序索引的末尾，结束 search
				if current_index >= len(current_inverted_list):
					return result
				
				current_ids.append(current_inverted_list[current_index])
				print('current_ids:',current_ids)
				print('\n')
			
			# 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中都出现了

			if all(x == current_ids[0] for x in current_ids):
		
				result.append(current_ids[0])
				query_words_index = [x + 1 for x in query_words_index]
				continue
			
			#如果不是，我们就把最小的元素加一
			print("current_ids:",current_ids)
			min_val = min(current_ids)
			print('min_val:',min_val)
			min_val_pos = current_ids.index(min_val)
			print('min_val_pos:',min_val_pos)
			print('query_words_index', query_words_index)
			print('query_words_index[min_val_pos]:', query_words_index[min_val_pos])
			query_words_index[min_val_pos] += 1
			print('query_words_index+1',query_words_index)
			print('query_words_index[min_val_pos]:',query_words_index[min_val_pos])
			print('current_index:',current_index)
			print('\n')

	
	@staticmethod
	def parse_text_to_words(text):
		# 使用正则表达式去除标点符号和换行符
		text = re.sub(r'[^\w ]', ' ', text)
		# 转为小写
		text = text.lower()
		# 生成所有单词的列表
		word_list = text.split(' ')
		# 去除空白单词
		word_list = filter(None, word_list)
		# 返回单词的 set
		return set(word_list)


class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
	def __init__(self):
		super(BOWInvertedIndexEngineWithCache, self).__init__()
		LRUCache.__init__(self)
		#BOWInvertedIndexEngine.__init__(self)
	
	
	def search(self, query):
		# if self.has(query):
		# 	print('cache hit!')
		# 	return self.get(query)
		if super().has(query):
			print('cache hit!')
			return self.get(query)
		
		result = super(BOWInvertedIndexEngineWithCache, self).search(query)
		#result=self.search(query)

		self.set(query, result)
		
		return result


search_engine = BOWInvertedIndexEngineWithCache()
main(search_engine)


# search_engine = BOWInvertedIndexEngine()
# main(search_engine)



