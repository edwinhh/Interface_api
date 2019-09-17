# class Document():
#     def __init__(self, title, author, context):
#         print('init function called')
#         self.title = title
#         self.author = author
#         self.__context = context # __ 开头的属性是私有属性
#
#     def get_context_length(self):
#         return len(self.__context)
#
#     def intercept_context(self, length):
#         self.__context = self.__context[:length]
#
# harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')
#
# print(harry_potter_book.title)
# print(harry_potter_book.author)
# print(harry_potter_book.get_context_length())
#
# harry_potter_book.intercept_context(10)
#
# print(harry_potter_book.get_context_length())
#
# print(harry_potter_book.__context)
#


class Entity():
	def __init__(self, object_type):
		print('parent class init called')
		self.object_type = object_type
	
	def get_context_length(self):
		raise Exception('get_context_length not implemented')
	
	def print_title(self):
		print(self.title)


class Document(Entity):
	def __init__(self, title, author, context):
		print('Document class init called')
		Entity.__init__(self, 'document')
		self.title = title
		self.author = author
		self.__context = context
	
	def get_context_length(self):
		return len(self.__context)


class Video(Entity):
	def __init__(self, title, author, video_length):
		print('Video class init called')
		Entity.__init__(self, 'video')
		self.title = title
		self.author = author
		self.__video_length = video_length
	
	def get_context_length(self):
		return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
							 '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

# print(harry_potter_book.object_type)
# print(harry_potter_movie.object_type)
#
# harry_potter_book.print_title()
# harry_potter_movie.print_title()
#
# print(harry_potter_book.get_context_length())
# print(harry_potter_movie.get_context_length())

# proto/mat.py



# utils/mat_mul.py

from proto.mat import Matrix

def mat_mul(matrix_1: Matrix, matrix_2: Matrix):
    assert matrix_1.m == matrix_2.n
    n, m, s = matrix_1.n, matrix_1.m, matrix_2.m
    result = [[0 for _ in range(n)] for _ in range(s)]
    for i in range(n):
        for j in range(s):
            for k in range(m):
                result[i][k] += matrix_1.data[i][j] * matrix_2.data[j][k]

    return Matrix(result)






