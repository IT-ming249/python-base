#动态绑定属性和方法
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age#这两个变量时类的对象创建时都有的
    def eat(self):#这个方法定义在类对象中，也就是所有的实例都可以调用这个方法
        print(self.name+'在吃饭')

#一个Student类可以创建多个Student类的实例对象，每个实体对象的属性值（name,age）不同
stu1=Student('张三',20)
stu2=Student('李四',30)
print('-----------')
print('动态绑定属性')
stu1.gender='女'#动态绑定sut1的性别，这个操作只给stu1绑定
print(stu1.name,stu1.age,stu1.gender)
print(stu2.name,stu2.age)
print('------------')


print('动态绑定方法')
stu1.eat()
stu2.eat()
def show():
    print('定义在类之外的，叫函数')
stu1.show=show#将show这个函数与实例stu1绑定，这个函数与实例对象绑定以后，就是这个对象的方法了
stu1.show()
#stu2.show() 因为stu2没有绑定show方法，它不能调用
