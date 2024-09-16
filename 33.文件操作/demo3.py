#文件读写操作
#语法规则：file=open(filename(名称),[mode(读或写)，encoding(默认文本文件中的字符编码格式为:gbk)])

#读操作
file=open('a.txt','r')  #现在磁盘上的a.txt文件由变量file接收,r代表模式读取
print(file.readlines()) #读取文件中的所有内容，并放到一个列表当中
file.close()            #每次对文件完成读写操作后需要关闭系统资源

#写操作
file=open('b.txt','w')  #对b.txt进行写操作，如果这个文件不存在就创建它
file.write('hellow_word') #如果文件存在，则新写入的内容会覆盖原有内容
file.close()

#追加操作
file=open('b.txt','a')  #对b.txt进行追加操作，如果这个文件不存在就创建它
file.write('Python')    #如果文件存在，则新写入的内容会在原有内容后面追加
file.close()

#+:以读写方式打开文件,不能单独使用,需要与其它模式一起使用