#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''
import sys


"类"
class Person:
    def __init__(self,name):
        self.name=name;
        print("当类被创建时候,__init__方法会执行,此时会打印这句话.....");
    def sayHi(self):
        print("Hi "+self.name);

p=  Person("wangpx");
p.sayHi();


"模块"
'''
    相当于java中依赖的jar包
    导入:
    import module_name
    
    module.function();
    module.variable;
'''

sys.stdout.write("Hello Module! \n");
sys.stdout.write("标准的输出方法,需要显示的提供换行字符")
