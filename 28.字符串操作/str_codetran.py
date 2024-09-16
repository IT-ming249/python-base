#字符串的编码转换
#编码：将字符串转换为二进制数据
#解码：将bytes类型转换为字符串类型
s='研究生真累'
#编码
print(s.encode(encoding='GBK'))#GBK为编码格式 一个中文占两个字节  输出结果的b表示二进制
print(s.encode(encoding='UTF-8'))#UTF-8为编码格式   一个中文占三个字节
#解码：用什么格式编的码距要用什么格式解码
s1=s.encode(encoding='GBK')#编码
print(s1.decode(encoding='GBK'))#解码
s2=s.encode(encoding='UTF-8')
print(s2.decode(encoding='UTF-8'))