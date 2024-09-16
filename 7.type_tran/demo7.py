#数据类型转换
name='张三'
age=20
print(type(name),type(age))
#print('我叫'+name+',今年'+age+'岁')#+表示连接符号,int类型不能直接与字符串类型连接，需要进行类型转换
print('我叫'+name+',今年'+str(age)+'岁')#str()表示将()内的类型转成str类型
#类型转换包含 int(),float(),str()
#注意： 格式：要转成的类型（要转的数据）
#1.str转int，字符串为数字串
#2.float转int，舍弃小数部分
#3.str转int，报错，因为字符串为小数串，要转的话str必须是数字串（整数）
#4.str转float，非数字串不能转换
#5.int转float，后面加.0