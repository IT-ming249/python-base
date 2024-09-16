#Pyth中的else 不单只能跟if一起使用
#还能跟for whilepassword=0 一起使用，在没有执行break且循环的正常次数执行完的时候执行else
password=0
for i in [1,2,3]:
    password=input('请输入密码')
    if password=='123':
        print('欢迎使用')
        break
    else:
        print('密码错误，请重新输入')
else:
    print('三次机会用完')