#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''

"函数"

'''
    Python中的函数使用小括号调用
              在调用之前先定义,无return语句,自动返回None对象
    
    定义:
    def function_name([args]):
        function_suite
    
'''

def addDouble(x):
    "将输入的值乘以2并返回"
    return (x*2);

print(addDouble(5));
print(addDouble("wpx"));
print(addDouble([6,8]));

