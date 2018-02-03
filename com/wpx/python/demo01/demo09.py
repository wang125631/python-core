#encoding=utf-8
'''
@author:     wangpx

@copyright:  2018
'''


"文件"


'''
    handle = open (file_name,access_mode='r');
    file_name 变量包含希望打开的文件的字符串名字
    access_mode中'r'为读取,'w'为写入 ,'a'表示添加
 '''
file=open("D://1.txt",'a');     #添加文件
file.write("Hello Python,I'm Wangpx at Henan");
file.close();
data = open("D://1.txt",'r')
for eachLine in data:
    print(eachLine)
data.close();


"异常"

'''
                           捕获异常 ,python封装在try-except语句
'''
try:
    filehandler=open("D://2.txt", access_mode='r');
    for eachLine in filehandler :
        print(eachLine);
except :
    print("this file is not exist");
    


