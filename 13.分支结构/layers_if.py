##嵌套使用if
'''会员 >=200 8折
        >=100 9折
非会员 >=200 9折
      不打折'''
answer=input('您是会员吗yes/no')
money=int(input('请输入您的消费金额'))
if answer=='yes':#Python的分支归属，看缩进对齐的位置
    if money>=200:
        print('尊敬的会员，给您打8折，您需要付',money*0.8)
    elif money>=100:
        print('尊敬的会员，给您打9折，您需要付',money*0.9)
    else:
        print('这么少会员也不打折')
else:
    if money>=200:
        print('非会员，打9折，您应付',money*0.9)
    else:
        print('非会员不打折')