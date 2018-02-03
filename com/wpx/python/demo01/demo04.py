#encoding=utf-8

'''
@author:     wangpx

@copyright:  2018
'''


"列表和元素"


'''
        列表用括号 [] 包裹
       元素的个数和元素的值可以改变
'''

aList = [1,2,3,4]

print(aList[0]);
print(aList[:2]);
aList[1] = 8;
print(aList);

'''
            元组用 ()包裹
            元组也可以进行切片,得到的结果也是元组(不能被修改)
'''

aTuple = (123,"wangpx",234.5);
print(aTuple[:2]);
print(aTuple[1]);
aTuple[1]="wpx";