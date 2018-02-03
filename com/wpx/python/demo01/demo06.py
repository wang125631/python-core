#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''

"if语句"

temp=input("请输入一个数字");
number=int(temp);
if number>5:
    print("您输入的数字比5大");
elif number==5:
    print("您输入的数字等于5");
else:
    print("您输入的数字小于5");