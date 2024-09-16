#练习：写出100到999之间的水仙花数
#eg:153=1^3+5^3+3^3
count=1
sum=0
for i in range(100,1000):
    ge=i%10
    shi=i//10%10
    bai=i//100
    #print(ge,shi,bai)
    if ge**3+shi**3+bai**3==i:
        print(i)

