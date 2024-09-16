#多分支结构
#例子：录入一个成绩，判断它的范围
score=int(input(('请输入你的成绩')))
if 90<=score<100: #<-python能这么写， 厉害吧！！#(score<100 and score>=90):
    print('A级')
    #Python的else if->elif
elif 80<=score<90:#score<90 and score >=80:
    print('B级')
elif 70<=score<80:#score<80 and score>=70:
    print('C级')
elif 60<=score<70:#score<70 and score >=60:
    print('D级')
else:
    print('不及格或非法输入')

