#课程案例
#要求：列出指定目录下的所有py文件
import  os
import os.path
path=os.getcwd() #获取当前目录
lst=os.listdir(path) #将当前目录内容使用一个列表储存
for f in lst:
    if f.endswith('.py'):
        print(f)
print('---------------')
#课程案例2
#要求：walk方法获取所有的路径，目录，文件
path=os.getcwd() #获取当前目录
lst_files=os.walk(path) #walk返回的是一个三元组(root,dirs,files)（路径，目录，文件）
print(lst_files)#这是一个迭代体对象
for dirpath,dirname,filename in lst_files:
    '''print(dirpath)
    print(dirname)
    print(filename)
    print('------------------')'''
    for dir in dirname:#获取所有路径下的文件夹
        print(os.path.join(dirpath,dir))

    for files in filename:#获取所有路径下的文件
        print(os.path.join(dirpath,files))
    print('--------------------')