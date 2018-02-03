#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''
from anaconda_navigator.utils.py3compat import cmp

"列表和元组"

'''
  列表使用 [] 包裹,元组使用() 包裹
  
  Tuple 是不可变的list ,一旦创建就不能改变
  Tuple 和   List 一样按定义的次序进行排序,索引为0开始
  Tuple 和  List都可以使用切片操作
  
  Tuple不能存在的方法:
  不能向tuple中添加元素,Tuple没有append或extend 方法
  不能从puple中删除元素,Tuple没有remove或pop方法
  
'''

#定义一个Tuple
my_tuple=(1,)
print(1 in my_tuple);   "in 方法查看元素是否存在于Tuple中"
list(my_tuple); "将元组转化为列表"

#定义两个List
my_list01 = ["name","age","wangpx",123];
my_list02 = ["name","age","wangpx",123];
my_list03 = [1,22,90,123];

print(cmp(my_list01,my_list02));    "比较两个列表的元素"
print(len(my_list01));   "列表元素个数"
print(max(my_list03));   "返回列表的最大值"
print(min(my_list03)); "返回列表的最小值"

my_list03.append(234);  "在列表末尾添加元素"
my_list03.extend(my_list01);    "在列表后一次性追加另一个序列"
print(my_list03);

print(my_list03.index("wangpx")); " 找出对应值索引"
my_list03.insert(1, "安阳"); "指定位置插入元素"
my_list03.pop();    "移除列表中一个元素,默认为最后"
my_list03.remove(123); "移除第一个匹配项"
my_list03.reverse(); "对列表进行反转"
print(my_list03);

del my_list03

print(my_list03)