#继承
#所有的类都默认继承了object，object是所有类的祖宗
class Person(object):#()里面不写的话也是默认继承object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def inof(self):
        print(self.name,self.age)

class Student(Person): #这表示Student类继承了Person类                                   Python支持多继承
    def __init__(self,name,age,stu_no):
        super().__init__(name,age) #使用super()函数传入它父类的name,age两个变量
        self.stu_no=stu_no
    # 方法重写：对父类中的方法不满意时，可以进行方法重写
    def inof(self):#对父类的info方法进行重写
        super().inof()#如果还需要用到父类的方法，就是用super()函数进行调用
        print(self.stu_no)#可以理解为先调用再改写方法

class Teacher(Person):
    def __init__(self,name,age,teachofyears):
        super().__init__(name,age)
        self.teachofyears=teachofyears
    def inof(self):
        super().inof()
        print(self.teachofyears)


stu=Student('张三',20,1001)
ter=Teacher('李四',35,10)
stu.inof()
ter.inof()#子类的实例对象可以调用父类的方法
print('---------')


