#b:以二进制的方式打开文件，一般不能单独使用，需要伴随wb,rb使用
#示例：复制图片
scr_file=open('logo.PNG','rb')
target_file=open('copyloge.PNG','wb')
target_file.write(scr_file.read())#读取scr中的内容并写入trget
scr_file.close()
target_file.close()