#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''
from builtins import range


'''
    列表解析  可以在一行中使用一个for循环将所有值放到一个列表当中
'''

squared = [x ** 3 for x in range(5)];
for i in squared:
    print(i);
    
sqdEvent = [x**2 for x in range(8) if not x % 3]
for i in sqdEvent:
    print(i);