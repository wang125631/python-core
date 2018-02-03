#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''

"字典"

'''
            字典为key-value
'''

aDict = {'name':'wpx'}
aDict['addr']="河南";
print(aDict);
for key in aDict:
    print(key+" : "+aDict[key])