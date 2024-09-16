#文件对象的常用操作

#读操作相关
#file=open('a.txt','r')
#print(file.read())#读取全部内容
#print(file.read(2))#只读取两个字符
#print(file.readline())#读一行
#print(file.readlines())#读取每一行然后放入列表当中
#file.close()

#写操作相关
#file=open('c.txt','a')
#file.write('hello')#将字符串写进内容
#lst=['java','go','python']
#file.writelines(lst)#将列表追加进内容
#file.close

#seek将文件指针指向新的位置
#filie=open('a.txt','r')
#filie.seek(2)#将文件指针跳过两个字节
#print(filie.read())
#print(filie.tell())#返回文件指针当前的位置,指针从第一个英文字符前面开始索引为0,
#filie.close()