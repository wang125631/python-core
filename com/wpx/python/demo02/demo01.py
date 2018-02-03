#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''

"语句和语法"

'''
    Python语句中基本规则和特殊字符
    # 表示 Python注释
    \ 表示继续上一行
    : 将代码块的头和体分开
    
'''
import copy

a=8 #
if (a>0) and \
(a<10):
    print("Yes");

"赋值操作符"

'''
    赋值为对象的引用,而非将值赋给一个变量
'''

person=['name',['fist','w','last','px']];

"浅copy "

p1=copy.copy(person);
p2=person[:];
p3=list(person);

print(p1);
print(p2);
print(p3);
"p1 p2 p3 均为person的引用,因此下面的等式是成立的"
print(p1==p2==p3);  

"Python中支持多重赋值"
a=b=c={"name":"wpx"};
print(a)
print(b)
print(c)

"Python中的关键字"

'''
and as assert break
class continue def del
elif else except exec
finally for from global
if import in is
lambda not or pass
print raise return try
while with yield None

'''


