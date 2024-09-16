#字符串比较
#比较规则：首先比较两个字符串的第一个字符，如果相等则比较下一个字符，依次比下去直到发现不相等的字符为止
#其比较结果就是两个字符粗的比较结果，后续字符则不再进行比较
print('apple'>'app')
print('apple'>'bnanna')#这两个字符串第一个就不一样 97当然不大于98
print(ord('a'),ord('b'))#获取a和b的原始值
print(chr(97),chr(98))
#==与is的区别:
#==比较的是值是否相等
#is比较的是id是否相等
a=b='python'
c='python'
print(a==c,a==b)
print(a is b,a is c)#字符串的驻留机制再次体现