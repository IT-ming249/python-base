#字符串劈分操作
s='hello word python'
#split():从字符串左边开始劈分，默认劈分字符是空格，返回值是一个列表
#通过参数sep指定劈分符
#通过参数maxsplit指定劈分字符串时最大的劈分次数，剩下的就不会再分了
lst=s.split()
print(lst)
s1='hello/word/python'
print(s1.split())
print(s1.split(sep='/'))
print(s1.split(sep='/',maxsplit=1))
print('--------')
#rsplit():从字符串右边开始劈分，默认劈分字符是空格，返回值是一个列表
#通过参数sep指定劈分符
#通过参数maxsplit指定劈分字符串时最大的劈分次数，剩下的就不会再分了
print(s.rsplit())
print(s1.rsplit(sep='/',maxsplit=1))#这条代码可以看出左右劈分的区别