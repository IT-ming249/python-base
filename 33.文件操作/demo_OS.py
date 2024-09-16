#目录管理
#os模块是与系统相关的一个模块
import os
#os.system('notepad.exe')#打开记事本
#os.system('calc.exe')#打开计算器


#直接调用可执行文件
#os.startfile('C:\\Program Files (x86)\\Tencent\\WeChat\\Wechat.exe')#打开了微信

#os模块的常用函数
#1.getcwd() 获取当前目录
print(os.getcwd())
print('----------------')
#2.listdir(path) 返回指定路径下的文件和，目录信息
lst=os.listdir('../33.文件操作')#../表示返回上一级
print(lst)
print('-----------------')
#3.创建目录
#os.mkdir('newdir')
print('--------------')
#4.创建多级目录
#os.makedirs('A/B/C')
#5.删除目录
#os.rmdir('newdir')
#6.删除多级目录
#os.removedirs('A/B/C')
#7.chdir(path) 将path设置为当前工作目录
#os.chdir('E//')