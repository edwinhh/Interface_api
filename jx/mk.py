import unittest
import mock

l=[1,2.3]
class Person():
        arg_0 =5
        def __init__(self):
                self.arg_1 = 10
                pass
        def add(self):
                return 20
p = Person()
mock_obj = mock.Mock(return_value=p)
a = mock_obj()

# mock_obj = mock.Mock() 只是返回一个mock实例
# 要他的返回值时a  = mock_obj ()，a就是return_value
print ('a: ',a)
print('a.add=',a.add())
