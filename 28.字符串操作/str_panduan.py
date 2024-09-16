#字符串判断操作
s='hello python'
#isidentifier():判断该字符串是不是合法标识符，合法表示符是字母(汉字也是)，数字，下划线
print('1.',s.isidentifier())
#isspaec():判断指定字符串是否由，空白字符（回车，换行，水平制表符）组成
print('2.',s.isspace())
#isalpha():判断指定字符串是否全部由字母组成
print('3.',s.isalpha())
#isdecimal():判断指定字符串是否全部由十进制数字组成
print('4.',s.isdecimal())
#isnumeric():判断指定字符串是否全部由数字组成
print('5.',s.isnumeric())
#isalnum():判断指定字符串是否全部由数字和字母组成
print('6.',s.isalnum())