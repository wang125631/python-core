#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''

"字典 dict"

d = {"name":"wangpx","age":22,"addr":"Anyang"};
keys = d.keys(); "返回所有的key值"
for eachLine in keys:
    print(eachLine);

print(d.get("name"));  "通过key获取指定的value"
d["age"]=21; "修改年龄大小"
print(d.get("age"));

print("wpx" in d);"判断是够键值存在"
print("wpx" not in d);"判断键值是否不存在"

del d['name'];   "删除name"
print(d);

print(len(d));      "字典长度"
print(type(d.values()));
